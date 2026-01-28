"""Transformation functions for markdown content.

This module contains functions for cleaning up and transforming markdown
content during the HTML to markdown conversion process.
"""

import logging
import re

from flutterdoc_gen.convert.patterns import (
    LINK_PATTERNS,
    NOISE_STRINGS,
    TRACKING_DOMAINS,
    UNMATCHED_HTML_LINK_PATTERN,
)

# Footer marker for content removal - the start of Flutter doc footer navigation
FOOTER_MARKER = "1. [Flutter](index.html)"

# Module-level tracking of unmatched HTML link patterns
_unmatched_patterns: list[tuple[str, str]] = []  # List of (context, pattern)


def reset_unmatched_patterns() -> None:
    """Reset the unmatched patterns tracking list."""
    global _unmatched_patterns
    _unmatched_patterns = []


def get_unmatched_patterns() -> list[tuple[str, str]]:
    """Get the list of unmatched patterns collected during processing.

    Returns:
        List of tuples containing (source_context, pattern_string).
    """
    return _unmatched_patterns.copy()


def log_unmatched_summary() -> None:
    """Log a summary of all unmatched HTML link patterns found."""
    if _unmatched_patterns:
        unique_patterns = set(pattern for _, pattern in _unmatched_patterns)
        logging.info(
            "Found %d unmatched HTML link patterns (%d unique)",
            len(_unmatched_patterns),
            len(unique_patterns),
        )
        for pattern in sorted(unique_patterns):
            count = sum(1 for _, p in _unmatched_patterns if p == pattern)
            logging.info("  %dx: %s", count, pattern)


# --- Cleanup Transformation Functions ---


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

    Removes all content from the line containing FOOTER_MARKER
    to the end of the file.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with footer removed. If the footer marker is not found,
        returns the original content.
    """
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if FOOTER_MARKER in line:
            return "\n".join(lines[:i]).rstrip()
    return content


def remove_noise_lines(content: str) -> str:
    """Remove lines containing only specific noise strings.

    Removes lines that contain only whitespace and exactly one occurrence
    of exactly one of the strings defined in NOISE_STRINGS.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with noise lines removed.
    """
    lines = content.split("\n")
    result_lines = []

    for line in lines:
        stripped = line.strip()
        # Skip noise strings
        if stripped in NOISE_STRINGS:
            continue
        result_lines.append(line)

    return "\n".join(result_lines)


def remove_tracking_urls(content: str) -> str:
    """Remove lines containing analytics/tracking URLs.

    Removes lines containing any domain from TRACKING_DOMAINS.
    This separates tracking URL removal from general noise removal
    for better maintainability and testability.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with tracking URL lines removed.
    """
    lines = content.split("\n")
    result_lines = []

    for line in lines:
        if any(domain in line for domain in TRACKING_DOMAINS):
            continue
        result_lines.append(line)

    return "\n".join(result_lines)


# --- Link Transformation Functions ---


def transform_class_links(content: str) -> str:
    """Transform class links to MCP URI format.

    Replaces links of the form:
    - [CLASS_NAME](SECTION/CLASS_NAME-class.html)
    - [TYPE](SECTION/TYPE.html)
    with [NAME](mcp://flutter/api/SECTION/NAME).

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with class links transformed.
    """
    # Apply class_link pattern
    class_pattern = next(p for p in LINK_PATTERNS if p.name == "class_link")
    content = re.sub(class_pattern.pattern, class_pattern.replacement, content)

    # Apply type_link pattern
    type_pattern = next(p for p in LINK_PATTERNS if p.name == "type_link")
    return re.sub(type_pattern.pattern, type_pattern.replacement, content)


def transform_member_links(content: str) -> str:
    """Transform member links to MCP URI format.

    Replaces links of the form:
    - [MEMBER](SECTION/CLASS/MEMBER.html) -> mcp://flutter/api/SECTION/CLASS/MEMBER
    - [CLASS.MEMBER](SECTION/CLASS/CLASS.MEMBER.html) -> mcp://flutter/api/SECTION/CLASS/CLASS.MEMBER

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with member links transformed.
    """
    # Apply dotted_member_link pattern first (more specific)
    dotted_pattern = next(p for p in LINK_PATTERNS if p.name == "dotted_member_link")
    content = re.sub(dotted_pattern.pattern, dotted_pattern.replacement, content)

    # Apply member_link pattern
    member_pattern = next(p for p in LINK_PATTERNS if p.name == "member_link")
    return re.sub(member_pattern.pattern, member_pattern.replacement, content)


def transform_image_links(content: str) -> str:
    """Transform image links to placeholder text.

    Replaces image links of the form ![Link Text](IMAGE_PATH)
    with [Note: Image Link Text omitted].

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with image links replaced by placeholder text.
    """
    image_pattern = next(p for p in LINK_PATTERNS if p.name == "image_link")
    return re.sub(image_pattern.pattern, image_pattern.replacement, content)


def transform_dartpad_links(content: str) -> str:
    """Transform DartPad links to placeholder text.

    Replaces links containing "dartpad.dev" in the URI
    with [Note: Interactive sample omitted].

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with DartPad links replaced by placeholder text.
    """
    dartpad_pattern = next(p for p in LINK_PATTERNS if p.name == "dartpad_link")
    return re.sub(dartpad_pattern.pattern, dartpad_pattern.replacement, content)


def _collect_unmatched_patterns(content: str, source_context: str = "") -> None:
    """Detect and collect any remaining relative HTML links that weren't transformed.

    This function identifies HTML links that weren't matched by any transformation
    pattern, adding them to the module-level tracking list.

    Uses UNMATCHED_HTML_LINK_PATTERN for detection.

    Args:
        content: The markdown content to check for unmatched links.
        source_context: Optional context string to identify the source file.
    """
    global _unmatched_patterns
    matches = UNMATCHED_HTML_LINK_PATTERN.findall(content)

    for match in matches:
        _unmatched_patterns.append((source_context, match))


def apply_transformations(content: str, source_context: str = "") -> str:
    """Apply all markdown transformations in the specified order.

    Cleanup transformations (applied first):
    1. Remove header content before first heading
    2. Remove footer content from Flutter index link
    3. Remove noise lines (const, final, inherited markers, etc.)
    4. Remove tracking URL lines (analytics, etc.)

    Link transformations (applied second):
    1. Transform class links to MCP URI format
    2. Transform member links to MCP URI format
    3. Transform image links to placeholder text
    4. Transform DartPad links to placeholder text

    After transformations, any remaining relative HTML links are collected
    as unmatched patterns for summary reporting.

    Args:
        content: The markdown content to transform.
        source_context: Optional context string for identifying unmatched patterns.

    Returns:
        The fully transformed markdown content.
    """
    # Cleanup transformations
    content = remove_header(content)
    content = remove_footer(content)
    content = remove_noise_lines(content)
    content = remove_tracking_urls(content)

    # Link transformations
    content = transform_class_links(content)
    content = transform_member_links(content)
    content = transform_image_links(content)
    content = transform_dartpad_links(content)

    # Collect any remaining unmatched HTML links
    _collect_unmatched_patterns(content, source_context)

    return content
