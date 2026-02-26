---
description: "convert.py source structure, CLI, output layout, and test structure."
name: convert_reference
applyTo: "make_docs/src/flutterdocs/convert/**,make_docs/tests/convert/**"
---

# convert.py Reference

## Purpose

`convert.py` (registered as the `convert` script in `pyproject.toml`) converts Flutter/Dart HTML documentation into markdown files organized in a structured output directory. Its output is consumed by `load.py` to populate the sqlite3 database.

## CLI Invocation

`-s` and `-S` are mutually exclusive; exactly one is required.

```
convert -d <doc_dir> (-s <section> | -S <section_list_file>) -o <output_dir> [-v]
```

- `-d` / `--documents`: Root HTML documentation directory (contains `flutter/` and `snippets/` subdirectories).
- `-s` / `--section`: Single documentation section name (e.g., `material`).
- `-S` / `--section-list`: Path to a text file of section names, one per line; blank lines and `#` comments are ignored.
- `-o` / `--output`: Root output directory; writes to `<output_dir>/api/<section>/...`.
- `-v` / `--verbose`: Enable verbose logging.

## Output Structure

All path construction goes through `PathBuilder` (in `_shared/paths.py`). Never construct output paths manually.

`CategoryType` → subdirectory mapping (source of truth: `PathBuilder._get_category_subdir()`):

| `CategoryType` | Subdirectory |
|---|---|
| `CLASS` | `classes` |
| `MIXIN` | `mixins` |
| `ENUM` | `enums` |
| `CONSTANT` | `constants` |
| `EXTENSION_TYPE` | `extension_types` |
| `EXTENSION` | `extensions` |
| `FUNCTION` | `functions` |
| `TYPEDEF` | `typedefs` |

## Shared Code

All shared code lives in `make_docs/src/flutterdocs/_shared/`:

- `constants.py`: `CategoryType` (StrEnum), `MemberType` (StrEnum), `ALL_CATEGORIES`.
- `paths.py`: `PathBuilder`, `ensure_dir_exists()`, `list_entity_names()`, `read_section_list()`.
- `logging.py`: `configure_logging()`, `get_progress_logger()`, `get_notification_logger()`, `log_processing_error()`.

## Source Structure

```
make_docs/src/flutterdocs/
  _shared/
    constants.py       # CategoryType, MemberType, ALL_CATEGORIES
    paths.py           # PathBuilder, ensure_dir_exists, list_entity_names, read_section_list
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

## Test Structure

```
tests/
  conftest.py          # Top-level: output_dir fixture (tmp_path)
  convert/
    conftest.py        # SAMPLES_DIR, run_convert(), build_entity_path_builder(),
                       # build_section_path_builder(), get_available_sections(),
                       # get_class_names_for_section()
    unit/              # Pure unit tests (no filesystem, no subprocess)
    integration/       # End-to-end tests using sample HTML in samples/
      samples/         # Small real Flutter HTML files used as fixtures
        flutter/<section>/
        snippets/
```

