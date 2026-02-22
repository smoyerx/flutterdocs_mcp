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

from flutterdocs.convert.categorization import find_and_categorize_root_files
from flutterdocs._shared.constants import CategoryType
from flutterdocs._shared.logging import (
    configure_logging,
    get_notification_logger,
    get_progress_logger,
    log_processing_error,
)
from flutterdocs._shared.paths import PathBuilder, ensure_dir_exists, read_section_list
from flutterdocs.convert.rootdocs import (
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
from flutterdocs.convert.transformations import (
    log_unmatched_summary,
    reset_unmatched_patterns,
)


def validate_doc_dir(doc_dir: Path) -> None:
    """Validate that the root documentation directory exists.

    Called once before processing any sections.

    Args:
        doc_dir: The root documentation directory.

    Raises:
        SystemExit: If the directory does not exist.
    """
    if not doc_dir.exists() or not doc_dir.is_dir():
        log_processing_error(f"Documentation directory does not exist: {doc_dir}")


def _check_section_dirs(doc_dir: Path, section: str) -> bool:
    """Check that the section and snippets directories exist.

    Unlike validate_doc_dir, this does *not* exit on failure. Instead it logs
    a notification and returns False so the caller can skip the section.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Returns:
        True if both directories exist, False otherwise.
    """
    notification_logger = get_notification_logger()
    temp_builder = PathBuilder(
        section=section,
        doc_dir=doc_dir,
        output_dir=Path(),
    )

    section_dir = temp_builder.get_input_section_dir()
    if not section_dir.exists() or not section_dir.is_dir():
        notification_logger.info(
            f"Section directory does not exist, skipping: {section_dir}"
        )
        return False

    snippets_dir = temp_builder.get_input_snippets_dir()
    if not snippets_dir.exists() or not snippets_dir.is_dir():
        notification_logger.info(
            f"Snippets directory does not exist, skipping section '{section}': {snippets_dir}"
        )
        return False

    return True


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


def process_section(
    section: str,
    options_handle: object,
    doc_dir: Path,
    output_dir: Path,
) -> None:
    """Convert all documentation files for a single section.

    Creates the output directory, finds/categorises root files, processes the
    library and every entity category, then prints a per-section summary.

    Args:
        section: Documentation section name (e.g. "material", "widgets").
        options_handle: Pre-created html_to_markdown options handle.
        doc_dir: Root HTML documentation directory.
        output_dir: Root output directory for converted markdown files.
    """
    progress_logger = get_progress_logger()

    # Create output directory for this section
    create_output_directory(output_dir, section)

    # Find and categorize all root documentation files
    categorized_files = find_and_categorize_root_files(doc_dir, section)

    # Count total files
    total_files = sum(len(files) for files in categorized_files.values())

    if total_files == 0:
        print(f"No files found matching pattern in section '{section}'")
        return

    # Process library file first if it exists
    library_input_file = PathBuilder(
        section=section,
        output_dir=output_dir,
        doc_dir=doc_dir,
    ).get_input_library_file()
    if library_input_file.exists():
        progress_logger.info(f"Converting library: {section}")
        try:
            process_library(
                options_handle,
                section,
                doc_dir,
                output_dir,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {section}: {e}",
                library_input_file,
            )

    for class_name, class_file in categorized_files[CategoryType.CLASS]:
        progress_logger.info(f"Converting class: {class_name}")
        try:
            process_class(
                options_handle,
                class_name,
                class_file,
                section,
                doc_dir,
                output_dir,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {class_name}: {e}", class_file
            )

    for mixin_name, mixin_file in categorized_files[CategoryType.MIXIN]:
        progress_logger.info(f"Converting mixin: {mixin_name}")
        try:
            process_mixin(
                options_handle,
                mixin_name,
                mixin_file,
                section,
                doc_dir,
                output_dir,
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
                section,
                doc_dir,
                output_dir,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {constant_name}: {e}", constant_file
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
                section,
                doc_dir,
                output_dir,
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
                section,
                doc_dir,
                output_dir,
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
                section,
                doc_dir,
                output_dir,
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
                section,
                doc_dir,
                output_dir,
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
                section,
                doc_dir,
                output_dir,
            )
        except OSError as e:
            log_processing_error(
                f"Cannot write output file for {typedef_name}: {e}", typedef_file
            )

    print(f"Successfully processed {total_files} files from section '{section}'")


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
    section_group = parser.add_mutually_exclusive_group(required=True)
    section_group.add_argument(
        "-s",
        "--section",
        help="Name of a single documentation section to convert",
    )
    section_group.add_argument(
        "-S",
        "--section-list",
        type=Path,
        metavar="FILE",
        help=(
            "Path to a text file containing section names to convert, one per line."
            " Blank lines and lines starting with '#' are ignored."
        ),
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

    # Configure logging (once)
    configure_logging(args.verbose)

    # Resolve the list of sections to process
    if args.section is not None:
        sections: list[str] = [args.section]
    else:
        try:
            sections = read_section_list(args.section_list)
        except OSError as e:
            log_processing_error(f"Cannot read section list file: {e}")
        if not sections:
            log_processing_error(
                f"Section list file contains no sections: {args.section_list}"
            )

    # Validate the root documentation directory (once)
    validate_doc_dir(args.documents)

    # Reset unmatched pattern tracking (once, summarised after all sections)
    reset_unmatched_patterns()

    # Initialize html_to_markdown (once)
    options_handle = create_options_handle(ConversionOptions())

    processed = 0
    skipped = 0
    for section in sections:
        if not _check_section_dirs(args.documents, section):
            skipped += 1
            continue
        process_section(section, options_handle, args.documents, args.output)
        processed += 1

    # Log summary of unmatched HTML link patterns (once, across all sections)
    log_unmatched_summary()

    if skipped:
        print(f"Skipped {skipped} section(s) due to missing directories.")
    if processed == 0:
        print("No sections were processed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
