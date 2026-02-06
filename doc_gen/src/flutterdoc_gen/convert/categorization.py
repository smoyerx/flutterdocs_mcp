"""Categorization logic for Flutter documentation files.

This module contains functions for identifying and categorizing different types
of root documentation files (classes, mixins, constants, libraries, enums,
extensions, extension types, functions, and typedefs).
"""

import logging
from pathlib import Path

from flutterdoc_gen.convert.constants import CategoryType
from flutterdoc_gen.convert.paths import PathBuilder


def find_and_categorize_root_files(
    doc_dir: Path, section: str
) -> dict[str, list[tuple[str, Path]]]:
    """Find and categorize all root documentation files for a section.

    Categorizes files according to the following logic:
    1. Directly identified by filename pattern (class, mixin, constant, library, extension-type)
    2. Indirectly identified via sidebar files (enum, extension)
    3. Complex identification by name case (function, typedef)

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Returns:
        A dictionary mapping category names to lists of (name, path) tuples.
        Categories: 'class', 'mixin', 'constant', 'library', 'extension_type',
                   'enum', 'extension', 'function', 'typedef'
    """
    # Use temporary PathBuilder to construct path
    temp_builder = PathBuilder(
        section=section,
        doc_dir=doc_dir,
        output_dir=Path(),
    )
    section_dir = temp_builder.get_input_section_dir()

    # Initialize category dictionary
    categories: dict[str, list[tuple[str, Path]]] = {
        CategoryType.CLASS: [],
        CategoryType.MIXIN: [],
        CategoryType.CONSTANT: [],
        CategoryType.LIBRARY: [],
        CategoryType.EXTENSION_TYPE: [],
        CategoryType.ENUM: [],
        CategoryType.EXTENSION: [],
        CategoryType.FUNCTION: [],
        CategoryType.TYPEDEF: [],
    }

    # Get all HTML files in the section directory
    all_html_files = sorted(section_dir.glob("*.html"))

    # First pass: Categorize files with direct patterns and collect sidebar info
    sidebar_files = set()
    categorized_files = set()

    for html_file in all_html_files:
        filename = html_file.name

        # Skip sidebar files but track them for indirect identification
        if filename.endswith("-sidebar.html"):
            sidebar_files.add(filename)
            continue

        # Extract base name and check direct patterns
        name = html_file.stem

        # Direct identification by suffix pattern
        if filename.endswith("-class.html"):
            class_name = name.replace("-class", "")
            categories[CategoryType.CLASS].append((class_name, html_file))
            categorized_files.add(filename)
        elif filename.endswith("-mixin.html"):
            mixin_name = name.replace("-mixin", "")
            categories[CategoryType.MIXIN].append((mixin_name, html_file))
            categorized_files.add(filename)
        elif filename.endswith("-constant.html"):
            constant_name = name.replace("-constant", "")
            categories[CategoryType.CONSTANT].append((constant_name, html_file))
            categorized_files.add(filename)
        elif filename.endswith("-extension-type.html"):
            extension_type_name = name.replace("-extension-type", "")
            categories[CategoryType.EXTENSION_TYPE].append(
                (extension_type_name, html_file)
            )
            categorized_files.add(filename)

    # Second pass: Indirect identification via sidebar files and library check
    # Check for library: index.html exists and {section}-library.html exists
    library_marker = f"{section}-library.html"
    index_file = section_dir / "index.html"
    if index_file.exists() and library_marker in {f.name for f in all_html_files}:
        categories[CategoryType.LIBRARY].append((section, index_file))
        categorized_files.add("index.html")
        categorized_files.add(library_marker)  # Mark marker file as categorized too

    for html_file in all_html_files:
        filename = html_file.name

        # Skip already categorized files and sidebar files
        if filename in categorized_files or filename.endswith("-sidebar.html"):
            continue

        name = html_file.stem

        # Check for enum via sidebar
        enum_sidebar = f"{name}-enum-sidebar.html"
        if enum_sidebar in sidebar_files:
            categories[CategoryType.ENUM].append((name, html_file))
            categorized_files.add(filename)
            continue

        # Check for extension via sidebar
        extension_sidebar = f"{name}-extension-sidebar.html"
        if extension_sidebar in sidebar_files:
            categories[CategoryType.EXTENSION].append((name, html_file))
            categorized_files.add(filename)
            continue

    # Third pass: Complex identification by case (function vs typedef)
    for html_file in all_html_files:
        filename = html_file.name

        # Skip already categorized files and sidebar files
        if filename in categorized_files or filename.endswith("-sidebar.html"):
            continue

        name = html_file.stem

        # Check if name starts with a letter (not number or special char)
        if name and name[0].isalpha():
            if name[0].islower():
                # Function: starts with lowercase
                categories[CategoryType.FUNCTION].append((name, html_file))
                categorized_files.add(filename)
            elif name[0].isupper():
                # Typedef: starts with uppercase
                categories[CategoryType.TYPEDEF].append((name, html_file))
                categorized_files.add(filename)
        else:
            # Uncategorizable file - log in verbose mode
            logging.info(f"Uncategorizable file (skipping): {filename}")

    return categories
