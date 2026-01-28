"""Command-line interface for the convert tool.

This module contains the CLI entry point and related functions for
running the Flutter documentation conversion tool.
"""

import argparse
import logging
import sys
from pathlib import Path

from html_to_markdown import (
    ConversionOptions,
    ConversionOptionsHandle,
    create_options_handle,
)

from flutterdoc_gen.convert.conversion import convert_html_to_markdown
from flutterdoc_gen.convert.paths import (
    ensure_dir_exists,
    get_api_section_dir,
    get_input_section_dir,
    get_input_snippets_dir,
)
from flutterdoc_gen.convert.processors import (
    process_constructors,
    process_methods,
    process_operators,
    process_properties,
    process_snippets,
    process_static_methods,
)
from flutterdoc_gen.convert.transformations import (
    log_unmatched_summary,
    reset_unmatched_patterns,
)


def find_class_files(doc_dir: Path, section: str) -> list[tuple[str, Path]]:
    """Find all class documentation files for a section.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Returns:
        A list of tuples, each containing:
        - class_name: The name of the class
        - class_file: Path to the main class HTML file
    """
    section_dir = get_input_section_dir(doc_dir, section)

    classes = []

    # Find all *-class.html files
    class_files = sorted(section_dir.glob("*-class.html"))

    for class_file in class_files:
        # Extract class name from filename (e.g., "ListTile" from "ListTile-class.html")
        class_name = class_file.stem.replace("-class", "")
        classes.append((class_name, class_file))

    return classes


def process_class(
    options_handle: ConversionOptionsHandle,
    class_name: str,
    class_file: Path,
    section: str,
    doc_dir: Path,
    output_dir: Path,
) -> None:
    """Process all documentation files for a class using the 7-step pipeline.

    Steps:
    1. Process the class file
    2. Process constructor files
    3. Process property files
    4. Process method files
    5. Process operator files
    6. Process static method files
    7. Process code snippet files

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        class_name: The name of the class being processed.
        class_file: Path to the main class HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        output_dir: The section output directory (api/{section}).
    """
    # Create class output directory
    # Note: output_dir is already api/{section}, so we just add class_name
    class_output_dir = output_dir / class_name
    ensure_dir_exists(class_output_dir)

    # Step 1: Process the class file
    logging.info(f"  Processing class file: {class_file}")
    class_markdown = convert_html_to_markdown(options_handle, class_file)
    class_output_file = class_output_dir / f"{class_name}.md"
    class_output_file.write_text(class_markdown, encoding="utf-8")

    # Step 2: Process constructor files
    logging.info(f"  Processing constructors for {class_name}")
    process_constructors(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 3: Process property files
    logging.info(f"  Processing properties for {class_name}")
    process_properties(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 4: Process method files
    logging.info(f"  Processing methods for {class_name}")
    process_methods(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 5: Process operator files
    logging.info(f"  Processing operators for {class_name}")
    process_operators(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 6: Process static method files
    logging.info(f"  Processing static methods for {class_name}")
    process_static_methods(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 7: Process code snippet files
    logging.info(f"  Processing snippets for {class_name}")
    process_snippets(doc_dir, class_output_dir, section, class_name)


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

    section_dir = get_input_section_dir(doc_dir, section)
    if not section_dir.exists() or not section_dir.is_dir():
        logging.error(f"Section directory does not exist: {section_dir}")
        sys.exit(1)

    snippets_dir = get_input_snippets_dir(doc_dir)
    if not snippets_dir.exists() or not snippets_dir.is_dir():
        logging.error(f"Snippets directory does not exist: {snippets_dir}")
        sys.exit(1)


def create_output_directory(output_dir: Path, section: str) -> Path:
    """Create the output directory for a section.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.

    Returns:
        The path to the section output directory (api/{section}).

    Raises:
        SystemExit: If the directory cannot be created.
    """
    section_output = get_api_section_dir(output_dir, section)
    try:
        ensure_dir_exists(section_output)
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

    # Reset unmatched pattern tracking
    reset_unmatched_patterns()

    # Validate directories
    validate_directories(args.documents, args.section)

    # Create output directory
    output_section_dir = create_output_directory(args.output, args.section)

    # Initialize html_to_markdown
    options_handle = create_options_handle(ConversionOptions())

    # Find and process class documentation files
    classes = find_class_files(args.documents, args.section)

    if not classes:
        print(f"No files found matching pattern in section '{args.section}'")
        sys.exit(0)

    for class_name, class_file in classes:
        logging.info(f"Converting class: {class_name}")

        try:
            # Process documentation files for the class
            process_class(
                options_handle,
                class_name,
                class_file,
                args.section,
                args.documents,
                output_section_dir,
            )
        except OSError as e:
            logging.error(f"Cannot write output file for {class_name}: {e}")
            sys.exit(1)

    # Log summary of unmatched HTML link patterns
    log_unmatched_summary()

    print(
        f"Successfully processed {len(classes)} classes from section '{args.section}'"
    )


if __name__ == "__main__":
    main()
