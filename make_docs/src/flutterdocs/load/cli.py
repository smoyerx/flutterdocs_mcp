"""Command-line interface for the load tool.

Contains the CLI entry point, validation, and orchestration loop for
loading Flutter/Dart markdown documentation into a sqlite3 database.
"""

import argparse
import sys
from pathlib import Path

from flutterdocs._shared.constants import ALL_CATEGORIES
from flutterdocs._shared.logging import (
    configure_logging,
    get_notification_logger,
    get_progress_logger,
    log_processing_error,
)
from flutterdocs._shared.paths import PathBuilder, list_entity_names, read_section_list
from flutterdocs.load.db import open_or_create_db, upsert_library
from flutterdocs.load.loader import load_entity


def validate_global_inputs(doc_dir: Path, db_file: Path) -> None:
    """Validate CLI inputs that apply to the whole run (not per-section).

    Checks that doc_dir exists and is a directory and that the parent of
    db_file is writable when db_file does not yet exist.

    Args:
        doc_dir: Root markdown output directory from convert.py.
        db_file: Path for the sqlite3 output database.

    Raises:
        SystemExit: If any validation check fails.
    """
    if not doc_dir.exists() or not doc_dir.is_dir():
        log_processing_error(
            f"Documents directory does not exist or is not a directory: {doc_dir}"
        )

    if not db_file.exists():
        parent = db_file.parent
        if not parent.exists() or not parent.is_dir():
            log_processing_error(
                f"Parent directory of database file does not exist: {parent}"
            )
        if not _is_writable(parent):
            log_processing_error(
                f"Parent directory of database file is not writable: {parent}"
            )


def _check_section_dir(doc_dir: Path, section: str) -> bool:
    """Check that the section output directory exists.

    Unlike validate_global_inputs, this does *not* exit on failure. Instead it
    logs a notification and returns False so the caller can skip the section.

    Args:
        doc_dir: Root markdown output directory from convert.py.
        section: Documentation section name.

    Returns:
        True if the section directory exists, False otherwise.
    """
    notification_logger = get_notification_logger()
    temp_builder = PathBuilder(section=section, output_dir=doc_dir)
    section_dir = temp_builder.get_api_section_dir()
    if not section_dir.exists() or not section_dir.is_dir():
        notification_logger.info(
            f"Section directory does not exist, skipping: {section_dir}"
        )
        return False
    return True


def _is_writable(directory: Path) -> bool:
    """Check if a directory is writable by attempting a test file write.

    Args:
        directory: Directory path to check.

    Returns:
        True if writable, False otherwise.
    """
    test_file = directory / ".load_write_test"
    try:
        test_file.touch()
        test_file.unlink()
        return True
    except OSError:
        return False


def process_section(
    section: str,
    conn: object,
    doc_dir: Path,
    progress_logger: object,
    notification_logger: object,
) -> dict[str, int]:
    """Load all entities for a single section into the database.

    Args:
        section: Documentation section name (e.g. "material", "widgets").
        conn: Open sqlite3 database connection.
        doc_dir: Root markdown output directory from convert.py.
        progress_logger: Logger for per-entity progress messages.
        notification_logger: Logger for informational notices (skips, etc.).

    Returns:
        Dict mapping category string to number of entities loaded.
        Returns an empty dict if the library file is missing.
    """
    # Transaction: load library
    lib_builder = PathBuilder(section=section, output_dir=doc_dir)
    library_file = lib_builder.get_library_file()

    if not library_file.exists():
        notification_logger.info(  # type: ignore[union-attr]
            f"Library file not found, skipping section: {library_file}"
        )
        print(f"No library file found for section '{section}'")
        return {}

    library_content = library_file.read_text()
    display_name_file = lib_builder.get_library_display_name_file()
    display_name = (
        display_name_file.read_text().strip() if display_name_file.exists() else section
    )
    try:
        with conn:  # type: ignore[attr-defined]
            library_id = upsert_library(conn, section, display_name, library_content)  # type: ignore[arg-type]
    except Exception as e:
        log_processing_error(f"Failed to load library for section '{section}': {e}")

    # Enumerate and load all entities
    counts: dict[str, int] = {}

    for category_type in ALL_CATEGORIES:
        entity_names = list_entity_names(doc_dir, section, category_type)
        if not entity_names:
            continue

        category_str = str(category_type)
        loaded_count = 0

        for entity_name in entity_names:
            builder = PathBuilder(
                section=section,
                output_dir=doc_dir,
                entity_name=entity_name,
                entity_type=category_type,
            )

            entity_file = builder.get_entity_file()
            if not entity_file.exists():
                notification_logger.info(  # type: ignore[union-attr]
                    f"Entity file not found, skipping: {entity_file}"
                )
                continue

            try:
                member_count = load_entity(
                    conn,  # type: ignore[arg-type]
                    builder=builder,
                    library_id=library_id,
                    entity_name=entity_name,
                    category_type_str=category_str,
                )
            except Exception as e:
                log_processing_error(
                    f"Failed to load entity '{entity_name}' ({category_str}): {e}"
                )

            progress_logger.info(  # type: ignore[union-attr]
                f"Loading {category_str}: {entity_name} ({member_count} members)"
            )
            loaded_count += 1

        if loaded_count > 0:
            counts[category_str] = loaded_count

    return counts


def main() -> None:
    """Main entry point for the load script."""
    parser = argparse.ArgumentParser(
        description="Load Flutter/Dart markdown documentation into a sqlite3 database.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-d",
        "--documents",
        required=True,
        type=Path,
        help="Path to root markdown output directory produced by convert.py",
    )
    section_group = parser.add_mutually_exclusive_group(required=True)
    section_group.add_argument(
        "-s",
        "--section",
        help="Name of a single documentation section to load",
    )
    section_group.add_argument(
        "-S",
        "--section-list",
        type=Path,
        metavar="FILE",
        help=(
            "Path to a text file containing section names to load, one per line."
            " Blank lines and lines starting with '#' are ignored."
        ),
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="Path to the sqlite3 database file to create or add to",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging output",
    )

    args = parser.parse_args()

    configure_logging(args.verbose)
    progress_logger = get_progress_logger()
    notification_logger = get_notification_logger()

    doc_dir: Path = args.documents
    db_file: Path = args.output

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

    # Validate global inputs (once)
    validate_global_inputs(doc_dir, db_file)

    # Open (or create) the database once for the entire run
    try:
        conn = open_or_create_db(db_file)
    except Exception as e:
        log_processing_error(f"Failed to open or initialize database {db_file}: {e}")

    total_entities = 0
    all_counts: dict[str, int] = {}
    skipped = 0

    try:
        for section in sections:
            if not _check_section_dir(doc_dir, section):
                skipped += 1
                continue

            counts = process_section(
                section,
                conn,
                doc_dir,
                progress_logger,
                notification_logger,
            )
            if not counts:
                # Library file was missing; section was already reported
                skipped += 1
                continue

            section_total = sum(counts.values())
            total_entities += section_total
            summary_parts = [f"{cat}: {n}" for cat, n in counts.items()]
            print(f"Loaded section '{section}': {', '.join(summary_parts)}")

            for cat, n in counts.items():
                all_counts[cat] = all_counts.get(cat, 0) + n

    finally:
        conn.close()  # type: ignore[union-attr]

    if skipped:
        print(
            f"Skipped {skipped} section(s) due to missing directories or library files."
        )

    if total_entities == 0:
        print("No entities loaded.")
        sys.exit(0)
