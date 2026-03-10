# load_002_snippets PRD

This PRD specifies a change to how code snippets are handled in `load.py`. It supersedes the snippet-handling behavior defined in `load_001_initial.md`.

## Summary of Changes

1. Snippet markdown is no longer stored in a dedicated `entity.snippet_markdown` database column. Instead, when snippets exist, they are appended directly to the entity's content markdown and stored together as `entity.content_markdown`.
2. The `entity.snippet_markdown` column is removed from the database schema and from all code that reads or writes it.

## Behavior Change: Snippet Handling

### Previous behavior (load_001_initial.md)

Snippet files were collected, sorted, and concatenated joined by `"\n\n"`, producing a `snippet_markdown` value that was stored separately in `entity.snippet_markdown`. If no snippets existed, `entity.snippet_markdown` was `NULL`.

### New behavior

Snippet files are still collected, sorted alphabetically by filename, and their contents joined by `"\n\n"`. However, the following additional steps apply:

1. Prepend the string `"\n\n## Code Examples\n\n"` to the concatenated snippet content.
2. Concatenate the result to the entity's `content_markdown` (i.e., append it to the end of the entity root file content).
3. Store the combined string as `entity.content_markdown`.

If the snippets directory does not exist or contains no `*.md` files, the entity's `content_markdown` is stored as-is (no change from the entity root file contents). There is no separate snippet field.

### Updated `collect_snippets()` contract

`collect_snippets()` in `loader.py` must be updated to return the full snippet appendage (including the `## Code Examples` heading) rather than the raw concatenation. Its return value is a string to be appended to `content_markdown`, or `None` if there are no snippets.

The revised implementation must:

1. Locate `builder.get_snippets_dir()`.
2. If the directory does not exist or contains no `*.md` files, return `None`.
3. Otherwise, sort all `*.md` files alphabetically by filename, join their contents with `"\n\n"`, and prepend `"\n\n## Code Examples\n\n"` to produce the return value.

### Updated `load_entity()` contract

`load_entity()` in `loader.py` must be updated to:

1. Call `collect_snippets(builder)` to get the optional snippet appendage.
2. If the appendage is not `None`, concatenate it to `content_markdown` (i.e., `content_markdown += snippet_appendage`).
3. Pass the combined `content_markdown` (and no `snippet_markdown` argument) to `upsert_entity()`.

## Database Schema Change

### Remove `entity.snippet_markdown`

The `snippet_markdown TEXT` column must be removed from the `entity` table in the embedded `SCHEMA_DDL` constant in `db.py`.

#### Updated `entity` table DDL

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

The full updated DDL (to replace `SCHEMA_DDL` in `db.py`) is:

```sql
CREATE TABLE identifier (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE entity_type (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE member_type (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE library (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    content_markdown TEXT NOT NULL
);

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

CREATE TABLE member (
    id INTEGER PRIMARY KEY,
    entity_id INTEGER NOT NULL,
    identifier_id INTEGER NOT NULL,
    member_type_id INTEGER NOT NULL,
    content_markdown TEXT NOT NULL,
    UNIQUE(identifier_id, entity_id),
    FOREIGN KEY (entity_id) REFERENCES entity(id),
    FOREIGN KEY (identifier_id) REFERENCES identifier(id),
    FOREIGN KEY (member_type_id) REFERENCES member_type(id)
);

CREATE INDEX idx_entity_unique ON entity(identifier_id, library_id);

CREATE INDEX idx_member_unique ON member(identifier_id, entity_id);
```

### Updated `upsert_entity()` signature

The `snippet_markdown` parameter must be removed from `upsert_entity()` in `db.py`. The function signature becomes:

```python
def upsert_entity(
    conn: sqlite3.Connection,
    library_id: int,
    identifier_id: int,
    entity_type_id: int,
    content_markdown: str,
) -> int:
```

The corresponding SQL must be updated to omit `snippet_markdown`:

```sql
INSERT INTO entity(library_id, identifier_id, entity_type_id, content_markdown)
VALUES (?, ?, ?, ?)
ON CONFLICT(identifier_id, library_id) DO UPDATE SET
    content_markdown = excluded.content_markdown
```

## Files to Update

| File | Change |
|---|---|
| `make_docs/src/flutterdocs/load/db.py` | Update `SCHEMA_DDL` constant; remove `snippet_markdown` parameter from `upsert_entity()` |
| `make_docs/src/flutterdocs/load/loader.py` | Update `collect_snippets()` to prepend heading; update `load_entity()` to append snippets to `content_markdown` instead of passing separately |

## Test Impact

Tests that assert on `entity.snippet_markdown` must be updated:

- Any test asserting that `entity.snippet_markdown` is non-`NULL` must instead assert that `entity.content_markdown` ends with (or contains) the expected snippet content, including the `## Code Examples` heading.
- Any test asserting that `entity.snippet_markdown` is `NULL` must instead assert that `entity.content_markdown` does not contain `## Code Examples`.
- The `upsert_entity()` unit tests in `test_db.py` must be updated to reflect the removed parameter.
- The database schema tests (if any) must verify that the `entity` table has no `snippet_markdown` column.
