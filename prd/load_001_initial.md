# load.py PRD

`load.py` (registered as the `load` script in `pyproject.toml`) reads the markdown documentation output produced by `convert.py` for a given section and loads it into a sqlite3 database. Simplicity and correctness are the primary goals; performance optimization is not a concern.

## Inputs

`load.py` must accept the following command-line arguments (parallel to `convert.py`):

- Mandatory `--documents {DOC_DIR}` or `-d {DOC_DIR}`, where `{DOC_DIR}` is an absolute or relative path to the root markdown output directory produced by `convert.py` (the same directory passed as `-o` to `convert.py`).
- Mandatory `--section {SECTION}` or `-s {SECTION}`, where `{SECTION}` is the name of the documentation section to load (e.g., `material`, `widgets`).
- Mandatory `--output {DB_FILE}` or `-o {DB_FILE}`, where `{DB_FILE}` is an absolute or relative path to the sqlite3 database file to create or add to.
- Optional `--verbose` or `-v`, which when present enables verbose logging output.
- Optional `--help` or `-h`, which when present displays usage information.

## Outputs

`load.py` writes documentation data for the specified section into the sqlite3 database at `{DB_FILE}`.

If `{DB_FILE}` does not exist, `load.py` must create it and initialize the schema (see [Database Schema](#database-schema)). If it already exists, `load.py` must add to or update the existing data without re-creating the schema.

## Input Directory Structure

`load.py` MUST access all `convert.py` output exclusively via `PathBuilder` methods and `list_entity_names()`. It must never manually construct or hardcode output paths or make assumptions about the directory layout.

The structure of the input is documented in `PATHBUILDER_USAGE.md` and is summarized here for reference only:

- Entity root file: `{DOC_DIR}/api/{section}/{category_subdir}/{entity_name}/{entity_name}.md`
- Member files: `{DOC_DIR}/api/{section}/{category_subdir}/{entity_name}/{member_type}/[native|inherited]/{member_name}.md` (for properties, methods, operators) or `{DOC_DIR}/api/{section}/{category_subdir}/{entity_name}/{member_type}/{member_name}.md` (for constructors, constants, statics)

The canonical source of truth for subdirectory names is `PathBuilder._get_category_subdir()`.

## Functional Requirements

### 1. Validation

Before loading, `load.py` must validate:

- `{DOC_DIR}` exists and is a directory; exit with an error if not.
- `{DOC_DIR}/api/{section}` exists and is a directory (via `PathBuilder.get_api_section_dir()`); exit with an error if not.
- The parent directory of `{DB_FILE}` exists and is writable (if `{DB_FILE}` does not yet exist); exit with an error if not.

### 2. Database Initialization

If `{DB_FILE}` does not exist, `load.py` must create it and execute the DDL to initialize all tables and indexes (see [Database Schema](#database-schema)). The DDL must be embedded directly in the Python source as a string constant; it must not be read from an external file at runtime.

If `{DB_FILE}` already exists, `load.py` must skip schema initialization and proceed directly to loading.

### 3. Library Validation

Each section represents the documentation for a single library. Before loading any non-library entities, `load.py` must:

1. Call `list_entity_names(doc_dir, section, CategoryType.LIBRARY)` to find library entries for the section.
2. If the result contains exactly one entry, load it into the `library` table (see [Database Mapping](#database-mapping)) and retain the resulting `library.id` for use as `library_id` on all `entity` rows in step 4.
3. If the result does not contain exactly one entry, log a notification. Load any LIBRARY entities that do exist into the `library` table, but skip step 4 entirely — no `entity` rows are inserted for this section.

### 4. Entity Enumeration and Loading

For each `CategoryType` in `ALL_CATEGORIES` (canonical iteration order), `load.py` must call `list_entity_names(doc_dir, section, category_type)` to discover all entities of that type. If no entities exist for a category, skip it silently.

`CategoryType.LIBRARY` entities are handled separately in step 3 above. All other `CategoryType` values are loaded into the `entity` table.

For each discovered non-library entity:

1. Create a `PathBuilder` with `section`, `output_dir` (the `{DOC_DIR}` argument), `entity_name`, and `entity_type`.
2. Verify that the entity's root markdown file exists via `builder.get_entity_file()`. If the file does not exist, log a notification and skip this entity (including all its members); continue with the next entity.
3. Enumerate members from all applicable member directories (see below). Count the total number of members found.
4. Log a single progress message of the form `"Loading {category}: {entity_name} ({N} members)"` (e.g., `"Loading class: ListTile (42 members)"`).
5. Insert or upsert the entity and all its members into the database (see [Database Mapping](#database-mapping)).

Member directories to enumerate via `*.md` glob:

- Constructors: `builder.get_constructors_dir()`
- Constants: `builder.get_constants_dir()`
- Native properties: `builder.get_native_properties_dir()`
- Inherited properties: `builder.get_inherited_properties_dir()`
- Native methods: `builder.get_native_methods_dir()`
- Inherited methods: `builder.get_inherited_methods_dir()`
- Native operators: `builder.get_native_operators_dir()`
- Inherited operators: `builder.get_inherited_operators_dir()`
- Statics: `builder.get_statics_dir()`

If a member directory does not exist, skip it silently. Both native and inherited member directories must be enumerated; there will never be an identifier conflict between native and inherited members for the same entity.

The member count logged in the progress message is the total count of member files found across all member directories (before insertion).

**Snippets** are handled separately from members: collect all `*.md` files from `builder.get_snippets_dir()`, sort them alphabetically by filename, and concatenate their contents joined by two blank lines (i.e., `"\n\n"` between each file's content) to produce `snippet_markdown`. Two blank lines are used both for visual spacing and to ensure correct separation when a snippet file does not end with a newline. If the snippets directory does not exist or contains no files, `snippet_markdown` is `None`.

### 5. Logging

- Use `get_progress_logger()` for the `"Loading {category}: {entity_name} ({N} members)"` progress message per entity (gated by `--verbose`).
- Use `get_notification_logger()` for unexpected but non-fatal conditions (e.g., missing entity file, wrong number of library entries, empty section).
- Use `log_processing_error()` for fatal errors that prevent further progress (exits with status 1).

### 6. Exit Behavior

- If no entities are found for the specified section across all categories, print a message and exit with status 0.
- On success, print a summary of the number of entities loaded per category type (categories with zero entities may be omitted from the summary).

## Database Schema

The database has six tables: `identifier`, `entity_type`, `member_type`, `library`, `entity`, and `member`.

The DDL for schema initialization, embedded as a string constant in the Python source, is:

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
    snippet_markdown TEXT,
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

CREATE INDEX idx_entity_identifier ON entity(identifier_id);
CREATE INDEX idx_entity_unique ON entity(identifier_id, library_id);

CREATE INDEX idx_member_identifier ON member(identifier_id);
CREATE INDEX idx_member_unique ON member(identifier_id, entity_id);
```

## Database Mapping

### `identifier` table

All entity names and member names are stored as rows in `identifier`. Before inserting any entity or member, `load.py` must insert the name with `INSERT OR IGNORE INTO identifier(name) VALUES (?)` and then retrieve its `id` with a `SELECT`. The `UNIQUE` constraint ensures deduplication across sections.

### `entity_type` table

All `CategoryType` string values used for entities are stored as rows in `entity_type`. Use `INSERT OR IGNORE INTO entity_type(name) VALUES (?)` and retrieve the `id` with a `SELECT`. Type values come from `CategoryType` (e.g., `"class"`, `"mixin"`, `"enum"`).

### `member_type` table

All `MemberType` string values are stored as rows in `member_type`. Use `INSERT OR IGNORE INTO member_type(name) VALUES (?)` and retrieve the `id` with a `SELECT`. Type values come from `MemberType` (e.g., `"constructors"`, `"methods"`, `"properties"`). Note that `MemberType.SNIPPETS` (`"snippets"`) must NOT be inserted into `member_type` or used as a `member_type_id` value; snippets are stored in `entity.snippet_markdown`, not as `member` rows.

For inherited member directories (`get_inherited_*_dir()`), use the same `MemberType` string as the native counterpart (e.g., `"methods"` for both native and inherited methods).

### `library` table

One row per `CategoryType.LIBRARY` entity.

| DB column | Source |
|---|---|
| `name` | Entity name (from `list_entity_names(..., CategoryType.LIBRARY)`) |
| `content_markdown` | Contents of `builder.get_entity_file()` |

To insert or update a `library` row without changing its `id` (which is referenced as a foreign key by `entity.library_id`), use:

```sql
INSERT INTO library(name, content_markdown)
VALUES (?, ?)
ON CONFLICT(name) DO UPDATE SET content_markdown = excluded.content_markdown
```

### `entity` table

One row per non-`LIBRARY` entity (CLASS, MIXIN, ENUM, CONSTANT, EXTENSION_TYPE, EXTENSION, FUNCTION, TYPEDEF).

| DB column | Source |
|---|---|
| `library_id` | `id` of the single `library` row for this section |
| `identifier_id` | `id` from `identifier` for the entity name |
| `entity_type_id` | `id` from `entity_type` for the `CategoryType` string |
| `content_markdown` | Contents of `builder.get_entity_file()` |
| `snippet_markdown` | Concatenation of sorted `*.md` files from `builder.get_snippets_dir()`, or `NULL` if none |

To insert or update an `entity` row without changing its `id` (which is referenced as a foreign key by `member.entity_id`), use:

```sql
INSERT INTO entity(library_id, identifier_id, entity_type_id, content_markdown, snippet_markdown)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT(identifier_id, library_id) DO UPDATE SET
    content_markdown = excluded.content_markdown,
    snippet_markdown = excluded.snippet_markdown
```

### `member` table

One row per member file enumerated from an entity's member directories.

| DB column | Source |
|---|---|
| `entity_id` | `id` of the parent `entity` row |
| `identifier_id` | `id` from `identifier` for the member filename stem |
| `member_type_id` | `id` from `member_type` for the `MemberType` string |
| `content_markdown` | Contents of the member markdown file |

For consistency with `library` and `entity`, and to preserve `id` stability for any future foreign key references, use:

```sql
INSERT INTO member(entity_id, identifier_id, member_type_id, content_markdown)
VALUES (?, ?, ?, ?)
ON CONFLICT(identifier_id, entity_id) DO UPDATE SET
    content_markdown = excluded.content_markdown
```

## Source Structure

`load.py` must follow the same layered module structure as `convert.py`, within `doc_gen/src/flutterdoc_gen/load/`:

```
doc_gen/src/flutterdoc_gen/load/
  __main__.py     # Entry point (calls cli.main)
  cli.py          # Argument parsing, validation, orchestration loop
  db.py           # Database initialization, connection, upsert helpers
  loader.py       # Entity- and member-level loading logic
                  # (analogous to rootdocs.py / processors.py in convert)
```

Register an entry point script named `load` in `pyproject.toml` pointing to `flutterdoc_gen.load.cli:main`.

## Test Structure

Tests must follow the same layout as `convert` tests under `doc_gen/tests/load/`:

```
tests/
  load/
    conftest.py         # Load-specific fixtures and helpers:
                        #   SAMPLES_DIR, run_load(), db_path fixture
    unit/               # Pure unit tests (no filesystem, no subprocess)
      __init__.py
      test_db.py        # DB initialization, upsert helpers
    integration/        # End-to-end tests using sample markdown in samples/
      __init__.py
      samples/          # Markdown output from running convert against
                        # tests/convert/integration/samples/
        api/
          material/
          widgets/
      test_basic_load.py
      test_cli.py
      test_entity_types.py
      test_member_loading.py
```

The sample markdown files in `tests/load/integration/samples/` are generated by running `convert` against the HTML samples in `tests/convert/integration/samples/`. If `convert.py`'s output format changes, the load samples must be regenerated.

## Error Handling

`load.py` must print a clear error message and exit with a non-zero status code for:

- Missing or invalid command-line arguments.
- `{DOC_DIR}` does not exist or is not a directory.
- `{DOC_DIR}/api/{section}` does not exist or is not a directory.
- `{DB_FILE}` parent directory does not exist or is not writable.
- Any database error during schema creation or data insertion.
- Any unexpected error during file reading.

For per-entity errors that do not prevent loading other entities (e.g., missing entity root file), log a notification via `get_notification_logger()` and continue with the next entity. Do not use `log_processing_error()` for per-entity errors.