"""Command-line interface for the load tool.

Contains the CLI entry point, validation, and orchestration loop for
loading Flutter/Dart markdown documentation into a sqlite3 database.
"""

import argparse
import sys
from pathlib import Path

from flutterdoc_gen._shared.constants import ALL_CATEGORIES
from flutterdoc_gen._shared.logging import (
    configure_logging,
    get_notification_logger,
    get_progress_logger,
    log_processing_error,
)
from flutterdoc_gen._shared.paths import PathBuilder, list_entity_names
from flutterdoc_gen.load.db import open_or_create_db, upsert_library
from flutterdoc_gen.load.loader import load_entity


def validate_inputs(doc_dir: Path, section: str, db_file: Path) -> None:
    """Validate CLI inputs before loading.

    Checks that doc_dir exists and is a directory, that the section directory
    within it exists, and that the parent of db_file is writable (when db_file
    does not yet exist).

    Args:
        doc_dir: Root markdown output directory from convert.py.
        section: Documentation section name.
        db_file: Path for the sqlite3 output database.

    Raises:
        SystemExit: If any validation check fails.
    """
    if not doc_dir.exists() or not doc_dir.is_dir():
        log_processing_error(
            f"Documents directory does not exist or is not a directory: {doc_dir}"
        )

    temp_builder = PathBuilder(section=section, output_dir=doc_dir)
    section_dir = temp_builder.get_api_section_dir()
    if not section_dir.exists() or not section_dir.is_dir():
        log_processing_error(
            f"Section directory does not exist or is not a directory: {section_dir}"
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
    parser.add_argument(
        "-s",
        "--section",
        required=True,
        help="Name of the documentation section to load (e.g., material, widgets)",
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
    section: str = args.section
    db_file: Path = args.output

    validate_inputs(doc_dir, section, db_file)

    # Open (or create) the database
    try:
        conn = open_or_create_db(db_file)
    except Exception as e:
        log_processing_error(f"Failed to open or initialize database {db_file}: {e}")

    # Transaction 2: load library
    lib_builder = PathBuilder(section=section, output_dir=doc_dir)
    library_file = lib_builder.get_library_file()

    if not library_file.exists():
        notification_logger.info(
            f"Library file not found, skipping section: {library_file}"
        )
        print(f"No library file found for section '{section}'")
        sys.exit(0)

    library_content = library_file.read_text()
    try:
        with conn:
            library_id = upsert_library(conn, section, library_content)
    except Exception as e:
        log_processing_error(f"Failed to load library for section '{section}': {e}")

    # Enumerate and load all entities
    counts: dict[str, int] = {}
    total_entities = 0

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
                notification_logger.info(
                    f"Entity file not found, skipping: {entity_file}"
                )
                continue

            try:
                member_count = load_entity(
                    conn,
                    builder=builder,
                    library_id=library_id,
                    entity_name=entity_name,
                    category_type_str=category_str,
                )
            except Exception as e:
                log_processing_error(
                    f"Failed to load entity '{entity_name}' ({category_str}): {e}"
                )

            progress_logger.info(
                f"Loading {category_str}: {entity_name} ({member_count} members)"
            )
            loaded_count += 1
            total_entities += 1

        if loaded_count > 0:
            counts[category_str] = loaded_count

    if total_entities == 0:
        print(f"No entities found for section '{section}'")
        sys.exit(0)

    # Print summary
    summary_parts = [f"{cat}: {n}" for cat, n in counts.items()]
    print(f"Loaded section '{section}': {', '.join(summary_parts)}")
