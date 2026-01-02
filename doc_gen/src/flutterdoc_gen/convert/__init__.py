"""Convert Flutter/Dart HTML documentation to markdown.

This package provides functionality to convert HTML documentation files
to markdown format, applying transformations and organizing output files.
"""

from flutterdoc_gen.convert.cli import main
from flutterdoc_gen.convert.conversion import (
    convert_dart_snippet,
    convert_html_to_markdown,
)
from flutterdoc_gen.convert.patterns import (
    LINK_PATTERNS,
    NOISE_STRINGS,
    TRACKING_DOMAINS,
    UNMATCHED_HTML_LINK_PATTERN,
    LinkPattern,
)
from flutterdoc_gen.convert.templates import (
    INHERITED_METHOD_TEMPLATE,
    INHERITED_OPERATOR_TEMPLATE,
    INHERITED_PROPERTY_TEMPLATE,
)
from flutterdoc_gen.convert.transformations import (
    apply_transformations,
    get_unmatched_patterns,
    log_unmatched_summary,
    reset_unmatched_patterns,
)

__all__ = [
    # CLI
    "main",
    # Patterns
    "LinkPattern",
    "LINK_PATTERNS",
    "NOISE_STRINGS",
    "TRACKING_DOMAINS",
    "UNMATCHED_HTML_LINK_PATTERN",
    # Templates
    "INHERITED_METHOD_TEMPLATE",
    "INHERITED_OPERATOR_TEMPLATE",
    "INHERITED_PROPERTY_TEMPLATE",
    # Conversion
    "convert_dart_snippet",
    "convert_html_to_markdown",
    # Transformations
    "apply_transformations",
    "get_unmatched_patterns",
    "log_unmatched_summary",
    "reset_unmatched_patterns",
]
