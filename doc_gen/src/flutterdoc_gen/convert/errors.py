"""Error handling utilities for conversion processes.

This module provides standardized error logging and exit functions
for the documentation conversion pipeline.
"""

import logging
import sys
from pathlib import Path


def log_processing_error(message: str, source_file: Path | None = None) -> None:
    """Log an error message with optional file context and exit with status 1.

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
