"""Command-line interface for the convert tool.

This module contains the CLI entry point and related functions for
running the Flutter documentation conversion tool.
"""

import argparse
import sys
from pathlib import Path

from html_to_markdown import (
    ConversionOptions,
    create_options_handle,
)

from flutterdoc_gen.convert.categorization import find_and_categorize_root_files
from flutterdoc_gen._shared.constants import CategoryType
from flutterdoc_gen._shared.logging import (
    configure_logging,
    get_progress_logger,
    log_processing_error,
)
from flutterdoc_gen._shared.paths import PathBuilder, ensure_dir_exists
from flutterdoc_gen.convert.rootdocs import (
    process_class,
    process_constant,
    process_enum,
    process_extension,
    process_extension_type,
    process_function,
    process_library,
    process_mixin,
    process_typedef,
)
from flutterdoc_gen.convert.transformations import (
    log_unmatched_summary,
    reset_unmatched_patterns,
)


def validate_directories(doc_dir: Path, section: str) -> None:
    """Validate that required directories exist.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Raises:
        SystemExit: If any required directory does not exist.
    """
    if not doc_dir.exists() or not doc_dir.is_dir():
        log_processing_error(f"Documentation directory does not exist: {doc_dir}")

    # Use temporary PathBuilder to construct paths for validation
    temp_builder = PathBuilder(
        section=section,
        doc_dir=doc_dir,
        output_dir=Path(),
    )

    section_dir = temp_builder.get_input_section_dir()
    if not section_dir.exists() or not section_dir.is_dir():
        log_processing_error(f"Section directory does not exist: {section_dir}")

    snippets_dir = temp_builder.get_input_snippets_dir()
    if not snippets_dir.exists() or not snippets_dir.is_dir():
        log_processing_error(f"Snippets directory does not exist: {snippets_dir}")


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
    # Use temporary PathBuilder to construct path
    temp_builder = PathBuilder(
        section=section,
        doc_dir=Path(),
        output_dir=output_dir,
    )

    section_output = temp_builder.get_api_section_dir()
    try:
        ensure_dir_exists(section_output)
    except OSError as e:
        log_processing_error(f"Cannot create output directory {section_output}: {e}")

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
    configure_logging(args.verbose)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Reset unmatched pattern tracking
    reset_unmatched_patterns()

    # Validate directories
    validate_directories(args.documents, args.section)

    # Create output directory
    create_output_directory(args.output, args.section)

    # Initialize html_to_markdown
    options_handle = create_options_handle(ConversionOptions())

    # Find and categorize all root documentation files
    categorized_files = find_and_categorize_root_files(args.documents, args.section)

    # Count total files
    total_files = sum(len(files) for files in categorized_files.values())

    if total_files == 0:
        print(f"No files found matching pattern in section '{args.section}'")
        sys.exit(0)

    # Process classes (existing functionality)
    for class_name, class_file in categorized_files[CategoryType.CLASS]:
        progress_logger.info(f"Converting class: {class_name}")

        try:
            # Process documentation files for the class
            process_class(
                options_handle,
                class_name,
                class_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {class_name}: {e}", class_file
            )

    # Process other categories with stub processors
    for mixin_name, mixin_file in categorized_files[CategoryType.MIXIN]:
        progress_logger.info(f"Converting mixin: {mixin_name}")
        try:
            process_mixin(
                options_handle,
                mixin_name,
                mixin_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {mixin_name}: {e}", mixin_file
            )

    for constant_name, constant_file in categorized_files[CategoryType.CONSTANT]:
        progress_logger.info(f"Converting constant: {constant_name}")
        try:
            process_constant(
                options_handle,
                constant_name,
                constant_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {constant_name}: {e}", constant_file
            )

    for library_name, library_file in categorized_files[CategoryType.LIBRARY]:
        progress_logger.info(f"Converting library: {library_name}")
        try:
            process_library(
                options_handle,
                library_name,
                library_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {library_name}: {e}", library_file
            )

    for extension_type_name, extension_type_file in categorized_files[
        CategoryType.EXTENSION_TYPE
    ]:
        progress_logger.info(f"Converting extension type: {extension_type_name}")
        try:
            process_extension_type(
                options_handle,
                extension_type_name,
                extension_type_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {extension_type_name}: {e}",
                extension_type_file,
            )

    for enum_name, enum_file in categorized_files[CategoryType.ENUM]:
        progress_logger.info(f"Converting enum: {enum_name}")
        try:
            process_enum(
                options_handle,
                enum_name,
                enum_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {enum_name}: {e}", enum_file
            )

    for extension_name, extension_file in categorized_files[CategoryType.EXTENSION]:
        progress_logger.info(f"Converting extension: {extension_name}")
        try:
            process_extension(
                options_handle,
                extension_name,
                extension_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {extension_name}: {e}", extension_file
            )

    for function_name, function_file in categorized_files[CategoryType.FUNCTION]:
        progress_logger.info(f"Converting function: {function_name}")
        try:
            process_function(
                options_handle,
                function_name,
                function_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {function_name}: {e}", function_file
            )

    for typedef_name, typedef_file in categorized_files[CategoryType.TYPEDEF]:
        progress_logger.info(f"Converting typedef: {typedef_name}")
        try:
            process_typedef(
                options_handle,
                typedef_name,
                typedef_file,
                args.section,
                args.documents,
                args.output,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {typedef_name}: {e}", typedef_file
            )

    # Log summary of unmatched HTML link patterns
    log_unmatched_summary()

    print(f"Successfully processed {total_files} files from section '{args.section}'")


if __name__ == "__main__":
    main()
