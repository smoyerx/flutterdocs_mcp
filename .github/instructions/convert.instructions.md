---
description: "convert.py inputs, outputs, source structure, and test structure. Reference for load.py PRDs and implementation."
name: convert_reference
applyTo: "doc_gen/src/flutterdoc_gen/load/**,doc_gen/tests/load/**"
---

# convert.py Reference

## Purpose

`convert.py` (registered as the `convert` script in `pyproject.toml`) converts Flutter/Dart HTML documentation into markdown files organized in a structured output directory. `load.py` reads this output and loads it into the sqlite3 database defined in `DOCDB_SCHEMA.sql`.

## CLI Invocation

```
convert -d <doc_dir> -s <section> -o <output_dir> [-v]
```

- `-d` / `--documents`: Root HTML documentation directory (contains `flutter/` and `snippets/` subdirectories).
- `-s` / `--section`: Documentation section name (e.g., `material`, `widgets`, `foundation`).
- `-o` / `--output`: Root output directory. convert.py writes to `<output_dir>/api/<section>/...`.
- `-v` / `--verbose`: Enable verbose logging.

## Output Structure

load.py MUST access all convert.py output exclusively via `PathBuilder` methods and `list_entity_names()`. Never construct output paths manually.

`CategoryType` → subdirectory mapping (source of truth: `PathBuilder._get_category_subdir()`):

| `CategoryType` | Subdirectory |
|---|---|
| `CLASS` | `classes` |
| `MIXIN` | `mixins` |
| `ENUM` | `enums` |
| `CONSTANT` | `constants` |
| `LIBRARY` | `library` |
| `EXTENSION_TYPE` | `extension_types` |
| `EXTENSION` | `extensions` |
| `FUNCTION` | `functions` |
| `TYPEDEF` | `typedefs` |

## Shared Code (used by both convert.py and load.py)

All shared code lives in `doc_gen/src/flutterdoc_gen/_shared/`:

- `constants.py`: `CategoryType` (StrEnum), `MemberType` (StrEnum), `ALL_CATEGORIES` (canonical iteration order).
- `paths.py`: `PathBuilder` (immutable dataclass for all path construction), `ensure_dir_exists()`, `list_entity_names()`.
- `logging.py`: `configure_logging()`, `get_progress_logger()`, `get_notification_logger()`, `log_processing_error()`.

See `doc_gen/PATHBUILDER_USAGE.md` for complete `PathBuilder` usage examples for load.py. Key points:
- load.py omits `doc_dir` from `PathBuilder` (only `section`, `output_dir`, `entity_name`, `entity_type` needed).
- Use `list_entity_names(output_dir, section, CategoryType.X)` to discover entities without a `PathBuilder`.
- `builder.get_entity_file()` → root entity markdown file.
- `builder.get_native_methods_dir()`, `builder.get_constructors_dir()`, etc. → member subdirectories; glob `*.md` to enumerate members.

## Source Structure

```
doc_gen/src/flutterdoc_gen/
  _shared/
    constants.py       # CategoryType, MemberType, ALL_CATEGORIES
    paths.py           # PathBuilder, ensure_dir_exists, list_entity_names
    logging.py         # Logging helpers
  convert/
    __main__.py        # Entry point (calls cli.main)
    cli.py             # Argument parsing, orchestration loop
    categorization.py  # find_and_categorize_root_files()
    rootdocs.py        # process_class/mixin/enum/... (one per CategoryType)
    processors.py      # process_constructors/methods/... (member-level)
    conversion.py      # convert_html_to_markdown(), convert_dart_snippet()
    transformations.py # apply_transformations(), link transforms
    parsing.py         # HTML parsing helpers
    patterns.py        # Regex patterns, MCP_URI_PREFIX constant
    templates.py       # Markdown template helpers
```

load.py should follow the same layered structure within `doc_gen/src/flutterdoc_gen/load/`:
- `cli.py` for argument parsing and orchestration
- `__main__.py` as entry point
- Module(s) for entity-level loading (analogous to `rootdocs.py`)
- Register an entry point script named `load` in `pyproject.toml` pointing to `flutterdoc_gen.load.cli:main`

## Test Structure

Convert tests live in `doc_gen/tests/convert/` and are organized by type:

```
tests/
  conftest.py          # Top-level: output_dir fixture (tmp_path)
  convert/
    conftest.py        # Convert-specific fixtures and helpers:
                       #   SAMPLES_DIR, run_convert(), build_entity_path_builder(),
                       #   build_section_path_builder(), get_available_sections(),
                       #   get_class_names_for_section()
    unit/              # Pure unit tests (no filesystem, no subprocess)
      test_categorization.py
      test_conversion.py
      test_parsing.py
      test_paths.py
      test_patterns.py
      test_transformations.py
    integration/       # End-to-end tests using sample HTML in samples/
      samples/         # Small real Flutter HTML files used as test fixtures
        flutter/
          <section>/   # One subdirectory per section
        snippets/
      test_basic_conversion.py
      test_cli.py
      test_entity_types.py
      test_link_transformations.py
      test_member_processing.py
```

load.py tests should follow the same layout under `tests/load/`. The load.py sample data should be the markdown output produced by running `convert` against the convert.py HTML samples in `tests/convert/integration/samples/`. If convert.py's output format changes, the load.py samples must be regenerated.
