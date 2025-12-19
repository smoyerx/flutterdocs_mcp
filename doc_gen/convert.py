# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "markitdown>=0.1.4",
# ]
# ///
"""Convert Flutter/Dart HTML documentation to markdown.

This script converts HTML documentation files to markdown format using the
markitdown package, applies transformations to clean up the output, and
concatenates related files into single entity documentation files.
"""

import argparse
import logging
import re
import sys
from pathlib import Path

from markitdown import MarkItDown


# --- Transformation Functions ---


def remove_header(content: str) -> str:
    """Remove all lines before the first markdown heading.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with all lines before the first heading removed.
        If no heading is found, returns the original content.
    """
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("#"):
            return "\n".join(lines[i:])
    return content


def remove_footer(content: str) -> str:
    """Remove footer content starting from the Flutter index link.

    Removes all content from the line containing "1. [Flutter](index.html)"
    to the end of the file.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with footer removed. If the footer marker is not found,
        returns the original content.
    """
    marker = "1. [Flutter](index.html)"
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if marker in line:
            return "\n".join(lines[:i]).rstrip()
    return content


def remove_html_links(content: str) -> str:
    """Remove HTML file links, keeping only the link text.

    Replaces markdown links to HTML files (e.g., [SomeClass](SomeClass-class.html))
    with just the link text (e.g., SomeClass).

    Args:
        content: The markdown content to transform.

    Returns:
        The content with HTML links replaced by their link text.
    """
    # Match [link text](anything.html) or [link text](path/to/file.html)
    pattern = r"\[([^\]]+)\]\([^)]+\.html\)"
    return re.sub(pattern, r"\1", content)


def apply_transformations(content: str) -> str:
    """Apply all markdown transformations in the specified order.

    Transformations are applied in order:
    1. Remove header content before first heading
    2. Remove footer content from Flutter index link
    3. Remove HTML file links

    Args:
        content: The markdown content to transform.

    Returns:
        The fully transformed markdown content.
    """
    content = remove_header(content)
    content = remove_footer(content)
    content = remove_html_links(content)
    return content


# --- Conversion Functions ---


def convert_html_to_markdown(md: MarkItDown, html_path: Path) -> str:
    """Convert an HTML file to markdown and apply transformations.

    Args:
        md: The MarkItDown instance to use for conversion.
        html_path: Path to the HTML file to convert.

    Returns:
        The transformed markdown content.

    Raises:
        FileNotFoundError: If the HTML file does not exist.
    """
    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    result = md.convert(str(html_path))
    return apply_transformations(result.text_content)


def convert_dart_snippet(dart_path: Path) -> str:
    """Convert a Dart snippet file to markdown.

    Wraps the Dart code in a markdown code block with a header.

    Args:
        dart_path: Path to the Dart file to convert.

    Returns:
        The Dart code wrapped in markdown format.

    Raises:
        FileNotFoundError: If the Dart file does not exist.
    """
    if not dart_path.exists():
        raise FileNotFoundError(f"Dart file not found: {dart_path}")

    content = dart_path.read_text(encoding="utf-8")
    return f"# Code Snippet\n\n```dart\n{content}\n```"


# --- File Discovery Functions ---


def find_entity_files(
    doc_dir: Path, section: str
) -> list[tuple[str, Path, list[Path], list[Path]]]:
    """Find all entity documentation files for a section.

    Discovers entity class files and their related property/method files
    and code snippets.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Returns:
        A list of tuples, each containing:
        - entity_name: The name of the entity
        - class_file: Path to the main class HTML file
        - member_files: List of paths to member HTML files (sorted alphabetically)
        - snippet_files: List of paths to snippet Dart files (sorted alphabetically)
    """
    section_dir = doc_dir / "flutter" / section
    snippets_dir = doc_dir / "snippets"

    entities = []

    # Find all *-class.html files
    class_files = sorted(section_dir.glob("*-class.html"))

    for class_file in class_files:
        # Extract entity name from filename (e.g., "ListTile" from "ListTile-class.html")
        entity_name = class_file.stem.replace("-class", "")

        # Find member files in entity subdirectory
        entity_subdir = section_dir / entity_name
        member_files: list[Path] = []
        if entity_subdir.is_dir():
            member_files = sorted(entity_subdir.glob("*.html"))

        # Find snippet files
        snippet_pattern = f"{section}.{entity_name}.*.dart"
        snippet_files = sorted(snippets_dir.glob(snippet_pattern))

        entities.append((entity_name, class_file, member_files, snippet_files))

    return entities


# --- Main Processing Functions ---


def process_entity(
    md: MarkItDown,
    entity_name: str,
    class_file: Path,
    member_files: list[Path],
    snippet_files: list[Path],
    verbose: bool = False,
) -> str:
    """Process all files for an entity and return concatenated markdown.

    Args:
        md: The MarkItDown instance to use for conversion.
        entity_name: The name of the entity being processed.
        class_file: Path to the main class HTML file.
        member_files: List of paths to member HTML files.
        snippet_files: List of paths to snippet Dart files.
        verbose: Whether to log file processing details.

    Returns:
        The concatenated markdown content for the entity.
    """
    parts: list[str] = []

    # Convert main class file
    if verbose:
        logging.info(f"  Processing: {class_file}")
    parts.append(convert_html_to_markdown(md, class_file))

    # Convert member files
    for member_file in member_files:
        if verbose:
            logging.info(f"  Processing: {member_file}")
        parts.append(convert_html_to_markdown(md, member_file))

    # Convert snippet files
    for snippet_file in snippet_files:
        if verbose:
            logging.info(f"  Processing: {snippet_file}")
        parts.append(convert_dart_snippet(snippet_file))

    return "\n\n".join(parts)


def validate_directories(doc_dir: Path, section: str) -> None:
    """Validate that required directories exist.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Raises:
        SystemExit: If any required directory does not exist.
    """
    if not doc_dir.exists() or not doc_dir.is_dir():
        logging.error(f"Documentation directory does not exist: {doc_dir}")
        sys.exit(1)

    section_dir = doc_dir / "flutter" / section
    if not section_dir.exists() or not section_dir.is_dir():
        logging.error(f"Section directory does not exist: {section_dir}")
        sys.exit(1)

    snippets_dir = doc_dir / "snippets"
    if not snippets_dir.exists() or not snippets_dir.is_dir():
        logging.error(f"Snippets directory does not exist: {snippets_dir}")
        sys.exit(1)


def create_output_directory(output_dir: Path, section: str) -> Path:
    """Create the output directory for a section.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.

    Returns:
        The path to the section output directory.

    Raises:
        SystemExit: If the directory cannot be created.
    """
    section_output = output_dir / section
    try:
        section_output.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logging.error(f"Cannot create output directory {section_output}: {e}")
        sys.exit(1)

    return section_output


def main() -> None:
    """Main entry point for the convert script."""
    parser = argparse.ArgumentParser(
        description="Convert Flutter/Dart HTML documentation to markdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-d",
        "--documents",
        required=True,
        type=Path,
        help="Path to directory containing HTML documentation",
    )
    parser.add_argument(
        "-s",
        "--section",
        required=True,
        help="Name of the documentation section to convert",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="Path to directory for converted markdown files",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging output",
    )

    args = parser.parse_args()

    # Configure logging
    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
    )

    # Validate directories
    validate_directories(args.documents, args.section)

    # Create output directory
    output_section_dir = create_output_directory(args.output, args.section)

    # Initialize MarkItDown
    md = MarkItDown(enable_plugins=False)

    # Find and process entities
    entities = find_entity_files(args.documents, args.section)

    if not entities:
        print(f"No files found matching pattern in section '{args.section}'")
        sys.exit(0)

    total_files = 0
    for entity_name, class_file, member_files, snippet_files in entities:
        if args.verbose:
            logging.info(f"Converting entity: {entity_name}")

        # Process entity
        markdown_content = process_entity(
            md,
            entity_name,
            class_file,
            member_files,
            snippet_files,
            verbose=args.verbose,
        )

        # Write output file
        output_file = output_section_dir / f"{entity_name}.md"
        try:
            output_file.write_text(markdown_content, encoding="utf-8")
        except OSError as e:
            logging.error(f"Cannot write output file {output_file}: {e}")
            sys.exit(1)

        # Count files processed
        entity_file_count = 1 + len(member_files) + len(snippet_files)
        total_files += entity_file_count

    # Print summary
    if args.verbose:
        logging.info(f"\nSection '{args.section}': {total_files} files processed")

    print(f"Successfully processed {len(entities)} entities from section '{args.section}'")


if __name__ == "__main__":
    main()
