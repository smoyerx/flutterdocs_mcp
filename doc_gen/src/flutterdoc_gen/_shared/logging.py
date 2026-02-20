"""Shared logging utilities for flutterdoc_gen tools.

This module provides centralized logging configuration and utilities
for all flutterdoc_gen tools (convert, load, etc.).
"""

import logging
import sys
from pathlib import Path
from typing import NoReturn

# Logger names for different message types
_PROGRESS_LOGGER_NAME = "flutterdoc_gen.progress"
_NOTIFICATION_LOGGER_NAME = "flutterdoc_gen.notification"


def get_progress_logger() -> logging.Logger:
    """Get the logger for routine progress messages.

    Returns:
        Logger instance for progress messages like "Converting class: X".
    """
    return logging.getLogger(_PROGRESS_LOGGER_NAME)


def get_notification_logger() -> logging.Logger:
    """Get the logger for unexpected (but not erroneous) condition messages.

    Returns:
        Logger instance for messages like "Skipping transformation",
        "Uncategorizable file", "Unmatched patterns", etc.
    """
    return logging.getLogger(_NOTIFICATION_LOGGER_NAME)


def configure_logging(verbose: bool) -> None:
    """Configure logging for flutterdoc_gen tools.

    Sets up progress and notification loggers with appropriate levels and formatting.
    Both loggers honor the verbose flag. The format includes the logger name
    to enable filtering output by message type using grep or other tools.

    Args:
        verbose: If True, enables INFO level logging. If False, only WARNING
                 and above are logged.

    Examples:
        # Show all messages
        configure_logging(verbose=True)

        # Filter to only notification conditions
        $ tool --verbose 2>&1 | grep "\\[flutterdoc_gen.notification\\]"

        # Filter to only progress messages
        $ tool --verbose 2>&1 | grep "\\[flutterdoc_gen.progress\\]"
    """
    log_level = logging.INFO if verbose else logging.WARNING

    # Configure root logger for basic behavior (handles ERROR, WARNING, etc.)
    logging.basicConfig(
        level=log_level,
        format="[%(name)s] %(message)s",
        force=True,  # Override any existing configuration
    )

    # Configure progress logger
    progress_logger = get_progress_logger()
    progress_logger.setLevel(log_level)

    # Configure notification logger
    notification_logger = get_notification_logger()
    notification_logger.setLevel(log_level)


def log_processing_error(message: str, source_file: Path | None = None) -> NoReturn:
    """Log an error message with optional file context and exit with status 1.

    This function is used for fatal errors during processing. It logs the error
    and immediately exits the program with a non-zero exit code.

    Args:
        message: The error message to log.
        source_file: Optional path to the source file being processed.
                    If provided, the absolute path will be prefixed to the message.
    """
    if source_file:
        formatted_message = f"[{source_file.resolve()}] {message}"
    else:
        formatted_message = message

    logging.error(formatted_message)
    sys.exit(1)
