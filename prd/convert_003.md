# convert.py Refactoring Proposal

This document proposes a refactoring of the `convert.py` script from a single-file script into a multi-file Python package. The goal is to improve maintainability, testability, and code organization as the script has grown in complexity.

## Motivation

The `convert.py` script has grown to approximately 1,000 lines of code with the following responsibilities:

1. **Pattern Definitions**: Link transformation patterns and noise strings
2. **Transformation Functions**: Header/footer removal, noise removal, link transformations
3. **Section Parsing**: Section content extraction, member link extraction
4. **File Processing**: HTML-to-markdown conversion, Dart snippet conversion
5. **Class Member Processing**: Constructors, properties, methods, operators, static methods, snippets
6. **CLI Interface**: Argument parsing, logging, main entry point

The corresponding test files have also grown significantly:
- `test_transformations.py`: ~700 lines covering unit tests for transformation and parsing functions
- `test_integration.py`: ~460 lines covering end-to-end conversion tests

Refactoring into a multi-file package will:
- Improve code organization and discoverability
- Enable more focused unit testing per module
- Facilitate future extensions (e.g., processing mixins, enums, or other documentation types)
- Support additional Python scripts/tools in the doc_gen directory
- Follow Python best practices for larger projects

## Proposed Package Structure

The structure uses a `flutterdoc_gen` parent package to support multiple tools (convert, and future scripts) under a unified namespace:

```
doc_gen/
├── pyproject.toml
├── src/
│   └── flutterdoc_gen/
│       ├── __init__.py              # Top-level package (minimal, version info)
│       ├── _shared/                 # Shared utilities across tools (future use)
│       │   ├── __init__.py
│       │   └── logging.py           # Common logging configuration (future)
│       └── convert/
│           ├── __init__.py          # Package exports
│           ├── __main__.py          # CLI entry point (python -m flutterdoc_gen.convert)
│           ├── cli.py               # Argument parsing and main()
│           ├── patterns.py          # Pattern definitions (LINK_PATTERNS, NOISE_STRINGS, etc.)           ├── paths.py             # Output path construction for markdown files│           ├── transformations.py   # Cleanup and link transformation functions
│           ├── parsing.py           # Section extraction and member link parsing
│           ├── conversion.py        # HTML-to-markdown and Dart snippet conversion
│           ├── processors.py        # Class member processing functions
│           └── templates.py         # Inherited member markdown templates
└── tests/
    ├── conftest.py                  # Shared fixtures (samples path, run helpers)
    ├── convert/                     # Tests for convert tool
    │   ├── __init__.py
    │   ├── conftest.py              # Convert-specific fixtures
    │   ├── unit/
    │   │   ├── __init__.py
    │   │   ├── test_patterns.py     # Tests for pattern registry
    │   │   ├── test_transformations.py  # Tests for transformation functions
    │   │   ├── test_parsing.py      # Tests for section/member extraction
    │   │   └── test_conversion.py   # Tests for HTML/Dart conversion functions
    │   └── integration/
    │       ├── __init__.py
    │       ├── test_cli.py          # CLI argument and error handling tests
    │       ├── test_conversion_pipeline.py  # Full conversion pipeline tests
    │       └── samples/             # Sample HTML/Dart files
    │           ├── flutter/
    │           │   ├── material/
    │           │   └── widgets/
    │           └── snippets/
    └── _shared/                     # Tests for shared utilities (future)
        └── __init__.py
```

### Adding Future Scripts

To add a new script (e.g., `index` for building a search index), create:

```
src/flutterdoc_gen/
└── index/
    ├── __init__.py
    ├── __main__.py          # python -m flutterdoc_gen.index
    ├── cli.py
    └── ...                  # Additional modules as needed

tests/
└── index/
    ├── conftest.py
    ├── unit/
    └── integration/
```

## Module Responsibilities

### `patterns.py`

Contains all pattern definitions and constants:

```python
# Contents from current convert.py
- LinkPattern dataclass
- LINK_PATTERNS tuple
- NOISE_STRINGS tuple
- TRACKING_DOMAINS tuple
- UNMATCHED_HTML_LINK_PATTERN regex
```

### `paths.py`

Contains functions for constructing output file paths:

```python
# Output path construction for markdown files
- get_class_file_path(output_dir, section, class_name) -> Path
- get_constructor_file_path(output_dir, section, class_name, constructor) -> Path
- get_native_property_file_path(output_dir, section, class_name, property) -> Path
- get_inherited_property_file_path(output_dir, section, class_name, source_section, source_class, property) -> Path
- get_native_method_file_path(output_dir, section, class_name, method) -> Path
- get_inherited_method_file_path(output_dir, section, class_name, source_section, source_class, method) -> Path
- get_native_operator_file_path(output_dir, section, class_name, operator) -> Path
- get_inherited_operator_file_path(output_dir, section, class_name, source_section, source_class, operator) -> Path
- get_static_method_file_path(output_dir, section, class_name, method) -> Path
- get_snippet_file_path(output_dir, section, class_name, short_name) -> Path

# Directory creation helpers
- ensure_class_directory(output_dir, section, class_name) -> Path
- ensure_constructors_directory(output_dir, section, class_name) -> Path
- ensure_native_properties_directory(output_dir, section, class_name) -> Path
- ensure_inherited_properties_directory(output_dir, section, class_name) -> Path
# ... similar for other member types
```

**Design rationale**: Output path construction is a separate concern from link transformation patterns. Isolating path logic in its own module:
- Makes output structure easily discoverable and modifiable
- Enables other tools to construct paths consistently (e.g., an index tool)
- Simplifies testing of path construction logic
- Reduces coupling between file I/O and business logic

### `transformations.py`

Contains cleanup and link transformation functions:

```python
# Cleanup transformations
- remove_header()
- remove_footer()
- remove_noise_lines()
- remove_tracking_urls()

# Link transformations
- transform_class_links()
- transform_member_links()
- transform_image_links()
- transform_dartpad_links()

# Unmatched pattern tracking
- reset_unmatched_patterns()
- get_unmatched_patterns()
- log_unmatched_summary()
- _collect_unmatched_patterns()

# Combined transformation
- apply_transformations()
```

### `parsing.py`

Contains section and member link parsing functions:

```python
- _normalize_heading_text()
- extract_section_content()
- extract_member_links()
- extract_static_method_links()
```

### `templates.py`

Contains markdown template strings:

```python
- INHERITED_PROPERTY_TEMPLATE
- INHERITED_METHOD_TEMPLATE
- INHERITED_OPERATOR_TEMPLATE
```

### `conversion.py`

Contains core conversion functions:

```python
- convert_html_to_markdown()
- convert_dart_snippet()
```

### `processors.py`

Contains class member processing functions:

```python
- process_constructors()
- process_properties()
- process_methods()
- process_operators()
- process_static_methods()
- process_snippets()
- process_class()
```

### `cli.py`

Contains CLI-related functions:

```python
- find_class_files()
- validate_directories()
- create_output_directory()
- parse_args()
- main()
```

### `flutterdoc_gen/__init__.py`

Minimal top-level package initialization:

```python
"""flutterdoc_gen - Tools for generating Flutter/Dart documentation."""

__version__ = "0.2.0"
```

### `flutterdoc_gen/convert/__init__.py`

Exports the public API of the convert package:

```python
from flutterdoc_gen.convert.cli import main
from flutterdoc_gen.convert.transformations import (
    apply_transformations,
    transform_class_links,
    transform_member_links,
    # ... other public functions
)
from flutterdoc_gen.convert.parsing import (
    extract_section_content,
    extract_member_links,
    # ...
)
from flutterdoc_gen.convert.patterns import LINK_PATTERNS, LinkPattern
```

### `flutterdoc_gen/convert/__main__.py`

Enables `python -m flutterdoc_gen.convert` execution:

```python
from flutterdoc_gen.convert.cli import main

if __name__ == "__main__":
    main()
```

## Test Structure

### Shared Fixtures (`tests/conftest.py`)

Top-level fixtures shared across all tools:

```python
import pytest
from pathlib import Path

@pytest.fixture
def output_dir(tmp_path: Path) -> Path:
    """Temporary output directory for any tool."""
    return tmp_path / "output"
```

### Convert-Specific Fixtures (`tests/convert/conftest.py`)

```python
import pytest
from pathlib import Path

SAMPLES_DIR = Path(__file__).parent / "integration" / "samples"

@pytest.fixture
def samples_dir() -> Path:
    """Path to convert sample documentation files."""
    return SAMPLES_DIR
```

### Unit Tests

Unit tests are organized by module under each tool's test directory:

| Test File | Module Under Test | Coverage |
|-----------|------------------|----------|
| `tests/convert/unit/test_patterns.py` | `flutterdoc_gen.convert.patterns` | Pattern registry validation, regex compilation |
| `tests/convert/unit/test_paths.py` | `flutterdoc_gen.convert.paths` | Output path construction, directory helpers |
| `tests/convert/unit/test_transformations.py` | `flutterdoc_gen.convert.transformations` | All cleanup and link transformation functions |
| `tests/convert/unit/test_parsing.py` | `flutterdoc_gen.convert.parsing` | Section extraction, member link parsing |
| `tests/convert/unit/test_conversion.py` | `flutterdoc_gen.convert.conversion` | HTML-to-markdown conversion, Dart snippet wrapping |

### Integration Tests

Integration tests validate the full pipeline for each tool:

| Test File | Scope |
|-----------|-------|
| `tests/convert/integration/test_cli.py` | CLI argument parsing, error handling, help output |
| `tests/convert/integration/test_conversion_pipeline.py` | Full end-to-end conversion with sample files |

## Configuration Changes

### `pyproject.toml` Updates

```toml
[project]
name = "doc-gen"
version = "0.2.0"
requires-python = ">=3.12"
dependencies = [
    "html-to-markdown>=2.19.1",
]

[project.scripts]
convert = "flutterdoc_gen.convert.cli:main"
# Future scripts would be added here:
# index = "flutterdoc_gen.index.cli:main"

[dependency-groups]
dev = [
    "pytest>=9.0.2",
    "snakeviz>=2.2.2",
]

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

### Key Configuration Notes

1. **Source Layout**: Uses `src/` layout per PEP 517/518 best practices
2. **Parent Package**: `flutterdoc_gen` serves as namespace for all tools
3. **Entry Points**: The `[project.scripts]` section creates `convert` command for `uv run` and after installation
4. **pytest Configuration**: `pythonpath = ["src"]` ensures imports work correctly
5. **Build System**: Not needed - `uv` handles building automatically

## Migration Plan

### Phase 1: Create Package Structure

1. Create `src/flutterdoc_gen/` directory structure
2. Create `src/flutterdoc_gen/__init__.py` with version info
3. Create `src/flutterdoc_gen/convert/` directory
4. Create `__init__.py` and `__main__.py` files for convert
5. Move pattern definitions to `patterns.py`
6. Extract path construction logic to `paths.py`
7. Move template strings to `templates.py`

### Phase 2: Split Transformation and Parsing Logic

1. Move transformation functions to `transformations.py`
2. Move parsing functions to `parsing.py`
3. Update imports within the package to use `flutterdoc_gen.convert.*`
4. Ensure all cross-module dependencies are resolved

### Phase 3: Split Conversion and Processing Logic

1. Move conversion functions to `conversion.py`
2. Move processor functions to `processors.py`
3. Move CLI functions to `cli.py`
4. Update the `__init__.py` exports

### Phase 4: Reorganize Tests

1. Create new test directory structure under `tests/`
2. Create `tests/conftest.py` with top-level shared fixtures
3. Create `tests/convert/` directory with tool-specific structure
4. Create `tests/convert/conftest.py` with convert-specific fixtures
5. Split `test_transformations.py` into:
   - `tests/convert/unit/test_patterns.py`
   - `tests/convert/unit/test_transformations.py`
   - `tests/convert/unit/test_parsing.py`
6. Split `test_integration.py` into:
   - `tests/convert/integration/test_cli.py`
   - `tests/convert/integration/test_conversion_pipeline.py`
7. Move `samples/` directory to `tests/convert/integration/samples/`

### Phase 5: Update Configuration and Validation

1. Update `pyproject.toml` with new configuration
2. Add `[project.scripts]` entry point for `convert`
3. Run full test suite to verify functionality
4. Update any documentation or README files
5. Create placeholder `src/flutterdoc_gen/_shared/` directory for future shared utilities

## Import Structure Examples

### Internal Imports (within convert package)

```python
# In flutterdoc_gen/convert/processors.py
from flutterdoc_gen.convert.conversion import convert_html_to_markdown, convert_dart_snippet
from flutterdoc_gen.convert.parsing import extract_section_content, extract_member_links
from flutterdoc_gen.convert.templates import INHERITED_PROPERTY_TEMPLATE
from flutterdoc_gen.convert.paths import (
    get_constructor_file_path,
    get_native_property_file_path,
    ensure_constructors_directory,
)
```

### Cross-Tool Imports (future shared utilities)

```python
# In flutterdoc_gen/convert/cli.py (future, when shared utilities exist)
from flutterdoc_gen._shared.logging import configure_logging
```

### External Imports (in tests)

```python
# In tests/convert/unit/test_transformations.py
from flutterdoc_gen.convert.transformations import (
    remove_header,
    remove_footer,
    transform_class_links,
    apply_transformations,
)
from flutterdoc_gen.convert.patterns import LINK_PATTERNS

# In tests/convert/integration/test_conversion_pipeline.py
import subprocess
from pathlib import Path

def run_convert(doc_dir: Path, section: str, output_dir: Path) -> subprocess.CompletedProcess[str]:
    cmd = ["uv", "run", "convert", "-d", str(doc_dir), ...]
    return subprocess.run(cmd, capture_output=True, text=True)
```

## Backward Compatibility

The refactoring maintains full backward compatibility:

1. **CLI**: The command-line interface remains unchanged
2. **Output Format**: Generated markdown files are identical
3. **Behavior**: All transformation and processing logic is preserved

The command-line interface and behavior remain identical:

| Scenario | Before | After |
|----------|--------|-------|
| **Development** | `uv run convert.py -d ... -s ... -o ...` | `uv run convert -d ... -s ... -o ...` |
| **After install** | N/A | `convert -d ... -s ... -o ...` |
| **Module execution** | N/A | `python -m flutterdoc_gen.convert -d ...` |

## Success Criteria

The refactoring is considered complete when:

1. All existing tests pass with the new structure
2. The CLI works identically to the current implementation
3. Output files are byte-for-byte identical for the same input
4. Code coverage remains at or above current levels
5. All imports follow Python best practices (no circular imports)
6. The package can be installed in editable mode with `pip install -e .`

## Future Considerations

This refactored structure enables future enhancements:

1. **New Documentation Types**: Add new processor modules (e.g., `flutterdoc_gen/convert/processors/mixins.py`)
2. **Additional Tools**: Add sibling packages under `flutterdoc_gen/` (e.g., `flutterdoc_gen/index/`, `flutterdoc_gen/validate/`)
3. **Shared Utilities**: Common code in `flutterdoc_gen/_shared/` (logging, path utilities, etc.)
4. **Plugin Architecture**: Pattern definitions could be loaded from external files
5. **Async Processing**: Large documentation sets could benefit from async I/O
6. **Database Output**: Additional output formats beyond markdown files

### Example: Adding a New Tool

To add a new `index` tool for building a documentation search index:

1. Create the package structure:
   ```
   src/flutterdoc_gen/index/
   ├── __init__.py
   ├── __main__.py
   ├── cli.py
   └── indexer.py
   ```

2. Add the entry point to `pyproject.toml`:
   ```toml
   [project.scripts]
   convert = "flutterdoc_gen.convert.cli:main"
   index = "flutterdoc_gen.index.cli:main"
   ```

3. Create the test structure:
   ```
   tests/index/
   ├── conftest.py
   ├── unit/
   └── integration/
   ```

4. Run with: `uv run index ...` (development) or `index ...` (after install)
