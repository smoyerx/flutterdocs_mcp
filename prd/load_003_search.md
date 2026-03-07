# load_003_search PRD

`load.py` (registered as the `load` script in `pyproject.toml`) reads the markdown documentation output produced by `convert.py` for a given section and loads it into a sqlite3 database.

This PRD specifies changes to the sqlite3 database schema and loading algorithm to support a full-text search capability for consumers of this database.

## Summary of Changes

- Denormalize the `entity` table by replacing the `identifier_id` foreign key with an inline `identifier TEXT NOT NULL` column and updating the UNIQUE constraint accordingly.
- Update `idx_entity_unique` to index the new `identifier` column.
- Add an FTS5 external-content virtual table `content_search` over `entity.identifier` and `entity.content_markdown`.
- Add three triggers on `entity` (`entity_ai`, `entity_ad`, `entity_au`) so that SQLite automatically keeps `content_search` in sync on every insert, update, and delete.
- Update `upsert_entity()` in `db.py` to accept `identifier: str` in place of `identifier_id: int` and to write it inline.
- Update `load_entity()` in `loader.py` to pass `entity_name` as `identifier` directly — removing the `get_or_insert_identifier()` call for entities. No extra FTS bookkeeping is required in `loader.py` because the triggers handle it.
- Update `DOCDB_SCHEMA.sql` to match the new schema.
- Update `load.instructions.md` to reflect the new schema.
- Update and add tests.

## Schema Changes

### `entity` table

**Before:**
```sql
CREATE TABLE entity (
    id INTEGER PRIMARY KEY,
    library_id INTEGER NOT NULL,
    identifier_id INTEGER NOT NULL,
    entity_type_id INTEGER NOT NULL,
    content_markdown TEXT NOT NULL,
    UNIQUE(identifier_id, library_id),
    FOREIGN KEY (library_id) REFERENCES library(id),
    FOREIGN KEY (identifier_id) REFERENCES identifier(id),
    FOREIGN KEY (entity_type_id) REFERENCES entity_type(id)
);
```

**After:**
```sql
CREATE TABLE entity (
    id INTEGER PRIMARY KEY,
    library_id INTEGER NOT NULL,
    identifier TEXT NOT NULL,
    entity_type_id INTEGER NOT NULL,
    content_markdown TEXT NOT NULL,
    UNIQUE(identifier, library_id),
    FOREIGN KEY (library_id) REFERENCES library(id),
    FOREIGN KEY (entity_type_id) REFERENCES entity_type(id)
);
```

The `identifier` column stores the entity name string directly (e.g., `"InkWell"`). The FK to the `identifier` table is removed entirely for this table; the `identifier` lookup table is retained and continues to be used by the `member` table.

### `idx_entity_unique` index

**Before:**
```sql
CREATE INDEX idx_entity_unique ON entity(identifier_id, library_id);
```

**After:**
```sql
CREATE INDEX idx_entity_unique ON entity(identifier, library_id);
```

### `content_search` FTS5 virtual table (new)

```sql
CREATE VIRTUAL TABLE content_search USING fts5(
    identifier,
    content_markdown,
    content='entity',
    content_rowid='id',
    tokenize='unicode61 remove_diacritics 2'
);
```

This is an external-content FTS5 table backed by the `entity` table. The three triggers below keep it in sync automatically.

### FTS5 sync triggers (new)

```sql
CREATE TRIGGER entity_ai AFTER INSERT ON entity BEGIN
    INSERT INTO content_search(rowid, identifier, content_markdown)
    VALUES (new.id, new.identifier, new.content_markdown);
END;

CREATE TRIGGER entity_ad AFTER DELETE ON entity BEGIN
    INSERT INTO content_search(content_search, rowid, identifier, content_markdown)
    VALUES ('delete', old.id, old.identifier, old.content_markdown);
END;

CREATE TRIGGER entity_au AFTER UPDATE ON entity BEGIN
    INSERT INTO content_search(content_search, rowid, identifier, content_markdown)
    VALUES ('delete', old.id, old.identifier, old.content_markdown);
    INSERT INTO content_search(rowid, identifier, content_markdown)
    VALUES (new.id, new.identifier, new.content_markdown);
END;
```

These are the standard triggers recommended by the SQLite FTS5 documentation for external-content tables. They fire automatically on every write to `entity`, so no application-level FTS bookkeeping is needed.

## Code Changes

### `db.py`

1. **`SCHEMA_DDL`** — Apply the schema changes above: updated `entity` DDL, updated `idx_entity_unique`, the new `content_search` DDL, and the three trigger DDL statements appended at the end.

2. **`upsert_entity()` signature and body** — Replace `identifier_id: int` parameter with `identifier: str`. Update the `INSERT` SQL to bind `identifier` as a text value and update the `ON CONFLICT(identifier, library_id)` clause. Update the `SELECT` used to retrieve the returned id to query by `identifier` instead of `identifier_id`. Update the docstring accordingly.

### `loader.py`

Remove the `get_or_insert_identifier(conn, entity_name)` call used to obtain `identifier_id` for the entity. Pass `entity_name` directly as the `identifier` keyword argument to `upsert_entity()`. The `get_or_insert_identifier` import is kept because it is still used for member loading.

No FTS-specific code is added to `load_entity()`. The triggers on `entity` handle `content_search` maintenance automatically.

Before:
```python
with conn:
    identifier_id = get_or_insert_identifier(conn, entity_name)
    entity_id = upsert_entity(
        conn,
        library_id=library_id,
        identifier_id=identifier_id,
        entity_type_id=entity_type_id,
        content_markdown=content_markdown,
    )
```

After:
```python
with conn:
    entity_id = upsert_entity(
        conn,
        library_id=library_id,
        identifier=entity_name,
        entity_type_id=entity_type_id,
        content_markdown=content_markdown,
    )
```

## File Updates

### `DOCDB_SCHEMA.sql`

Apply the same schema changes as `SCHEMA_DDL` in `db.py` — updated `entity` table, updated `idx_entity_unique`, and the new `content_search` virtual table and three triggers appended at the end.

### `load.instructions.md`

1. **Database Schema section** — Note the denormalized `entity.identifier TEXT` column (no longer a FK to `identifier`) and the `content_search` FTS5 virtual table maintained automatically by the three triggers.

## Test Changes

### `tests/load/unit/test_db.py`

- **`TestInitDb::test_creates_all_tables`** — Add `"content_search"` to the `expected` set. Note: FTS5 virtual tables may surface multiple entries in `sqlite_master` (e.g., `content_search`, `content_search_data`, etc.); use `issubset` or filter by `name = 'content_search'` rather than exact equality.
- **`TestInitDb::test_creates_triggers`** (new) — Assert that `sqlite_master` contains trigger names `entity_ai`, `entity_ad`, and `entity_au`.
- **`TestInitDb::test_creates_indexes`** — The expected index set is unchanged for what is asserted; no update required unless the test uses exact equality against all index names.
- **`TestUpsertEntity` (all tests)** — Update calls to `upsert_entity()` to pass `identifier="SomeName"` (a string) instead of `identifier_id=<int>`. Remove any preceding `get_or_insert_identifier()` setup calls that were only needed to produce an `identifier_id` for the entity.
- **`TestContentSearchTriggers` (new class)** — Add tests that exercise the triggers via `upsert_entity()` calls:
  - Insert entity → FTS row is automatically queryable.
  - Update entity (call `upsert_entity()` again with changed `content_markdown`) → FTS reflects new content and old tokens are gone.
  - Re-upsert entity → exactly one FTS result row (no duplicates).
  - Delete entity row → FTS row is removed.

### `tests/load/integration/test_basic_load.py`

- **`TestDbCreation::test_creates_all_tables`** — Add `"content_search"` to the expected tables set; use `issubset` for the assertion since FTS5 shadow tables will also be present.

### `tests/load/integration/test_cli.py`

- Add a test class `TestDefaultSearchSync` with at least:
  - A test that runs `load` on the `material` samples and verifies that `content_search` is populated (count > 0).
  - A test that runs `load` and queries `content_search` for a known entity name, asserting a result is returned.
  - A test that verifies the `content_search` row count matches the `entity` row count.

### `tests/load/integration/test_entity_types.py` and `test_member_loading.py`

- Audit for any direct query or assertion on `entity.identifier_id`; replace with `entity.identifier` (a text column). No changes expected unless those tests inspect the `identifier_id` column directly.
