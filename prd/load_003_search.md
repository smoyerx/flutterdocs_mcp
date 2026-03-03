# load_003_search PRD

`load.py` (registered as the `load` script in `pyproject.toml`) reads the markdown documentation output produced by `convert.py` for a given section and loads it into a sqlite3 database.

This PRD specifies changes to the sqlite3 database schema and loading algorithm to support a full-text search capability for consumers of this database.

## Summary of Changes

- Denormalize the `entity` table by replacing the `identifier_id` foreign key with an inline `identifier TEXT NOT NULL` column and updating the UNIQUE constraint accordingly.
- Update `idx_entity_unique` to index the new `identifier` column.
- Add an FTS5 external-content virtual table `content_search` over `entity.identifier` and `entity.content_markdown`.
- Update `upsert_entity()` in `db.py` to accept `identifier: str` in place of `identifier_id: int` and to write it inline.
- Add `upsert_entity_search()` to `db.py` to insert or update a single entity's row in `content_search`.
- Update `load_entity()` in `loader.py` to pass `entity_name` as `identifier` directly — removing the `get_or_insert_identifier()` call for entities — and to write to `content_search` after each entity upsert when `update_search=True` (the default).
- Add `--reindex` flag to `cli.py`. When specified, per-entity FTS writes are skipped and the index is rebuilt in bulk after all sections finish loading. When omitted (the default), each entity is written to both `entity` and `content_search` during loading.
- Update `DOCDB_SCHEMA.sql` to match the new schema.
- Update `load.instructions.md` to reflect the new schema and CLI.
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
    tokenize='porter'
);
```

This is an external-content FTS5 table backed by the `entity` table. By default, `load_entity()` writes to `content_search` after each entity upsert, keeping the two tables in sync. When `--reindex` is specified, per-entity FTS writes are skipped and the index is rebuilt in bulk at the end of the run instead.

## Code Changes

### `db.py`

1. **`SCHEMA_DDL`** — Apply the schema changes above (updated `entity` DDL, updated `idx_entity_unique`, appended `content_search` DDL). The `content_search` statement is added at the end of `SCHEMA_DDL`.

2. **`upsert_entity()` signature and body** — Replace `identifier_id: int` parameter with `identifier: str`. Update the `INSERT` SQL to bind `identifier` as a text value and update the `ON CONFLICT(identifier, library_id)` clause. Update the `SELECT` used to retrieve the returned id to query by `identifier` instead of `identifier_id`. Update the docstring accordingly.

3. **`upsert_entity_search()` (new function)** — Inserts or updates a single row in the `content_search` FTS5 table. Because `content_search` is an external-content table, updates require deleting the old FTS entry (using the pre-upsert values) and inserting a new one. The function signature is:
   ```python
   def upsert_entity_search(
       conn: sqlite3.Connection,
       entity_id: int,
       identifier: str,
       content_markdown: str,
       old_identifier: str | None = None,
       old_content_markdown: str | None = None,
   ) -> None:
   ```
   - If `old_identifier` / `old_content_markdown` are provided (entity already existed), issue the FTS5 delete command with the old values before inserting.
   - Then insert the new row: `INSERT INTO content_search(rowid, identifier, content_markdown) VALUES (entity_id, identifier, content_markdown)`.

4. **`rebuild_search_index()` (new function)** — Executes the FTS5 rebuild command:
   ```python
   def rebuild_search_index(conn: sqlite3.Connection) -> None:
       """Rebuild the FTS5 content_search index from the entity table.

       Should be called after all sections are loaded. Safe to call on an
       already-indexed database; it replaces the existing index content.

       Args:
           conn: Open sqlite3 connection.
       """
       with conn:
           conn.execute("INSERT INTO content_search(content_search) VALUES('rebuild')")
   ```

### `loader.py`

`load_entity()` gains an `update_search: bool = True` parameter. When `True`, it also keeps `content_search` in sync for each entity.

Changes inside `load_entity()`:

1. Remove the `get_or_insert_identifier(conn, entity_name)` call used to obtain `identifier_id` for the entity. Pass `entity_name` directly as the `identifier` keyword argument to `upsert_entity()`. The `get_or_insert_identifier` import is kept because it is still used for member loading.

2. Before calling `upsert_entity()`, query the database for the current entity row (if any) to capture the pre-upsert `identifier` and `content_markdown` as `old_identifier` / `old_content_markdown`. These are needed by `upsert_entity_search()` to issue the correct FTS5 delete command.

3. After calling `upsert_entity()`, when `update_search=True`, call `upsert_entity_search()` inside the same transaction, passing the new values and the captured old values (or `None` for new entities).

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
# Capture pre-upsert values for FTS5 delete (if entity already exists)
existing = conn.execute(
    "SELECT identifier, content_markdown FROM entity WHERE identifier = ? AND library_id = ?",
    (entity_name, library_id),
).fetchone()
old_identifier = existing["identifier"] if existing else None
old_content_markdown = existing["content_markdown"] if existing else None

with conn:
    entity_id = upsert_entity(
        conn,
        library_id=library_id,
        identifier=entity_name,
        entity_type_id=entity_type_id,
        content_markdown=content_markdown,
    )
    if update_search:
        upsert_entity_search(
            conn,
            entity_id=entity_id,
            identifier=entity_name,
            content_markdown=content_markdown,
            old_identifier=old_identifier,
            old_content_markdown=old_content_markdown,
        )
```

Update the import in `loader.py` to include `upsert_entity_search` from `flutterdocs.load.db`.

### `cli.py`

1. **`--reindex` flag** — Add an optional boolean flag to the argument parser:
   ```python
   parser.add_argument(
       "--reindex",
       action="store_true",
       help=(
           "Rebuild the FTS5 full-text search index in bulk after all sections are loaded. "
           "When omitted (default), each entity is written to content_search during loading."
       ),
   )
   ```

2. **`process_section()` signature** — Add `update_search: bool = True` parameter and thread it through to each `load_entity()` call.

3. **Orchestration loop** — Derive `update_search = not args.reindex` before the loop. Pass it to each `process_section()` call. After the loop completes (and before `conn.close()`), call `rebuild_search_index(conn)` when `args.reindex` is `True`. Print a confirmation line such as `"Rebuilt FTS5 search index."`.

4. **Import** — Add `rebuild_search_index` to the import from `flutterdocs.load.db`.

## File Updates

### `DOCDB_SCHEMA.sql`

Apply the same schema changes as `SCHEMA_DDL` in `db.py` — updated `entity` table, updated `idx_entity_unique`, and the new `content_search` virtual table appended at the end.

### `load.instructions.md`

1. **CLI Invocation section** — Add `[--reindex]` to the usage line and document the flag:
   - `--reindex`: Rebuild the FTS5 full-text search index after all sections are loaded.

2. **Database Schema section** — Note the denormalized `entity.identifier TEXT` column (no longer a FK to `identifier`) and the `content_search` FTS5 virtual table.

## Test Changes

### `tests/load/unit/test_db.py`

- **`TestInitDb::test_creates_all_tables`** — Add `"content_search"` to the `expected` set. Note: FTS5 virtual tables may surface multiple entries in `sqlite_master` (e.g., `content_search`, `content_search_data`, etc.); use `issubset` or filter by `name = 'content_search'` rather than exact equality.
- **`TestInitDb::test_creates_indexes`** — The expected index set is unchanged for what is asserted; no update required unless the test uses exact equality against all index names.
- **`TestUpsertEntity` (all tests)** — Update calls to `upsert_entity()` to pass `identifier="SomeName"` (a string) instead of `identifier_id=<int>`. Remove any preceding `get_or_insert_identifier()` setup calls that were only needed to produce an `identifier_id` for the entity.
- **`TestUpsertEntitySearch` (new class)** — Add tests that:
  - Verify inserting a new entity into `content_search` results in a queryable FTS row.
  - Verify updating an existing `content_search` row (by providing old values) produces correct FTS results for the new content.
- **`TestRebuildSearchIndex` (new class)** — Add tests that:
  - Verify `rebuild_search_index()` completes without error on an empty database.
  - Verify `rebuild_search_index()` completes without error after entities have been loaded.
  - Verify that after rebuild the `content_search` FTS5 table returns a result when querying a known entity identifier.

### `tests/load/integration/test_basic_load.py`

- **`TestDbCreation::test_creates_all_tables`** — Add `"content_search"` to the expected tables set; use `issubset` for the assertion since FTS5 shadow tables will also be present.

### `tests/load/integration/test_cli.py`

- Add a test class `TestReindex` with at least:
  - A test that runs `load` with `--reindex` on the `material` samples and asserts exit code 0 and that stdout contains `"Rebuilt FTS5 search index."`.
  - A test that queries the resulting database's `content_search` table after `--reindex` and verifies it returns a result for a known entity name.
- Add a test class `TestDefaultSearchSync` with at least:
  - A test that runs `load` without `--reindex` and verifies that `content_search` is populated (entity count matches).
  - A test that runs `load` without `--reindex` and queries `content_search` for a known entity name, asserting a result is returned.
- Update `run_load()` / `run_load_list()` in `conftest.py` to accept an optional `reindex: bool = False` parameter and append `--reindex` to the command when `True`.

### `tests/load/integration/test_entity_types.py` and `test_member_loading.py`

- Audit for any direct query or assertion on `entity.identifier_id`; replace with `entity.identifier` (a text column). No changes expected unless those tests inspect the `identifier_id` column directly.
