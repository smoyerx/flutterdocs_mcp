# PathBuilder Usage Examples

## load.py Usage (No doc_dir needed)

```python
from pathlib import Path
from flutterdoc_gen._shared.constants import CategoryType
from flutterdoc_gen._shared.paths import PathBuilder, list_entity_names

# load.py receives convert.py's output directory from command line
output_dir = Path("/path/to/output")
section = "material"

# 1. Discover entities (no PathBuilder needed)
class_names = list_entity_names(output_dir, section, CategoryType.CLASS)

# 2. Create PathBuilder only for file reading (no doc_dir!)
for name in class_names:
    builder = PathBuilder(
        section=section,
        output_dir=output_dir,  # Needed for reading markdown output by convert.py
        entity_name=name,
        entity_type=CategoryType.CLASS,
    )
    
    # Read markdown files
    entity_file = builder.get_entity_file()
    content = entity_file.read_text()
    
    # Load into database...
```

## convert.py Usage (doc_dir required for reading HTML)

```python
from pathlib import Path
from flutterdoc_gen._shared.constants import CategoryType
from flutterdoc_gen._shared.paths import PathBuilder

# convert.py needs both input (doc_dir) and output (output_dir)
doc_dir = Path("/path/to/flutter_docs")
output_dir = Path("/path/to/output")
section = "material"

# Create PathBuilder with BOTH doc_dir and output_dir
builder = PathBuilder(
    section=section,
    doc_dir=doc_dir,        # Needed for reading HTML
    output_dir=output_dir,   # Needed for writing markdown
    entity_name="ListTile",
    entity_type=CategoryType.CLASS,
)

# Read input HTML files
html_file = builder.get_input_entity_file()
html_content = html_file.read_text()

# ... convert to markdown ...

# Write output markdown files
output_file = builder.get_entity_file()
output_file.write_text(markdown_content)
```

## Key Differences

| Aspect | load.py | convert.py |
|--------|---------|------------|
| **doc_dir** | ❌ Not needed | ✅ Required |
| **Purpose** | Read markdown files | Read HTML, write markdown |
| **Input methods** | ❌ Cannot use | ✅ Can use |
| **Output methods** | ✅ Can use | ✅ Can use |

## Validation

PathBuilder properly validates usage:

```python
# ✅ This works - load.py usage
builder = PathBuilder(section="material", output_dir=Path("/output"))
builder.get_entity_file()  # OK

# ❌ This fails with clear error
builder.get_input_entity_file()
# ValueError: This operation requires doc_dir (input documentation directory),
# but PathBuilder was created without doc_dir.
```
