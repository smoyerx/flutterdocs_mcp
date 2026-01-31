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

    # Extract just the noise strings from the tuples
    noise_strings = tuple(noise[0] for noise in NOISE_STRINGS)

    for line in lines:
        stripped = line.strip()
        # Skip noise strings
        if stripped in noise_strings:
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

    # Extract just the tracking domains from the tuples
    tracking_domains = tuple(domain[0] for domain in TRACKING_DOMAINS)

    for line in lines:
        if any(domain in line for domain in tracking_domains):
            continue
        result_lines.append(line)

    return "\n".join(result_lines)


# --- Link Transformation Functions ---


def transform_class_links(content: str) -> str:
    """Transform class links to MCP URI format.

    Replaces links of the form [CLASS_NAME](SECTION/CLASS_NAME-class.html)
    with [CLASS_NAME](mcp://flutter/api/SECTION/CLASS_NAME).

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with class links transformed.
    """
    class_pattern = next(p for p in LINK_PATTERNS if p.name == "class_link")
    return re.sub(class_pattern.pattern, class_pattern.replacement, content)


def transform_member_links(content: str) -> str:
    """Transform member links to MCP URI format.

    Replaces links of the form [MEMBER](SECTION/CLASS/MEMBER.html)
    with [MEMBER](mcp://flutter/api/SECTION/CLASS/MEMBER).

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with member links transformed.
    """
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


# --- Function Declaration Cleanup ---

# Pattern for ordered list markers (1. , 2. , etc.)
_ORDERED_LIST_MARKER = re.compile(r"^(\d+)\.\s")

# Pattern for unordered list markers (- , * , + )
_UNORDERED_LIST_MARKER = re.compile(r"^[-*+]\s")

# Pattern for closing parenthesis line with optional comments
_CLOSING_PAREN_PATTERN = re.compile(r"^\s*\)(\s*//.*)?$")

# Pattern for closing brace+paren line with optional comments
_CLOSING_BRACE_PAREN_PATTERN = re.compile(r"^\s*\}\)(\s*//.*)?$")


def cleanup_function_declaration(content: str, source_context: str = "") -> str:
    """Clean up function declaration formatting in markdown content.

    This transformation removes blank lines and list markers from function
    declarations (constructors, methods, operators, static methods).

    The transformation operates on content between:
    - Start: First non-blank line after the first header
    - End: First line containing only ')' or '})' (optionally with comments)

    Args:
        content: The markdown content to transform.
        source_context: Context string for error reporting (typically file path).

    Returns:
        The transformed content with clean function declarations.

    Note:
        Calls log_processing_error() and exits with status 1 for:
        - Mixed list markers (ordered and unordered in same declaration)
        - Nested/indented list markers
        - List markers mid-line
        - Missing closing pattern after start pattern
    """
    from flutterdoc_gen.convert.errors import log_processing_error
    from pathlib import Path

    lines = content.split("\n")

    # Find the first header line
    header_index = None
    for i, line in enumerate(lines):
        if line.startswith("#") and " " in line:
            header_index = i
            break

    # If no header found, return content unchanged
    if header_index is None:
        return content

    # Find the start pattern: first non-blank line after header
    start_index = None
    for i in range(header_index + 1, len(lines)):
        if lines[i].strip():  # Non-blank line
            start_index = i
            break

    # If no start pattern found, return content unchanged
    if start_index is None:
        return content

    # Find the end pattern: first line with only ) or }) possibly with comments
    end_index = None
    for i in range(start_index, len(lines)):
        line = lines[i]
        if _CLOSING_PAREN_PATTERN.match(line) or _CLOSING_BRACE_PAREN_PATTERN.match(
            line
        ):
            end_index = i
            break

    # If no end pattern found after start, the declaration is likely a single-line
    # signature (e.g., "ClassName()") that doesn't need cleanup. Return unchanged.
    if end_index is None:
        return content

    # If start and end are the same line, nothing to transform
    if start_index == end_index:
        return content

    # Process lines between start and end (inclusive)
    declaration_lines = lines[start_index : end_index + 1]

    # Validate and detect list marker types
    has_ordered = False
    has_unordered = False

    for line in declaration_lines:
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # Check for ordered list marker
        if _ORDERED_LIST_MARKER.match(stripped):
            if indent > 0:
                source_path = Path(source_context) if source_context else None
                log_processing_error(
                    "Nested/indented list marker found in function declaration",
                    source_path,
                )
            has_ordered = True

        # Check for unordered list marker
        if _UNORDERED_LIST_MARKER.match(stripped):
            if indent > 0:
                source_path = Path(source_context) if source_context else None
                log_processing_error(
                    "Nested/indented list marker found in function declaration",
                    source_path,
                )
            has_unordered = True

        # Check for mid-line list markers (marker not at start of content)
        # Only check non-blank lines that aren't entirely a list marker line
        if (
            stripped
            and not _ORDERED_LIST_MARKER.match(stripped)
            and not _UNORDERED_LIST_MARKER.match(stripped)
        ):
            # Look for list markers that appear after other content
            if re.search(r"\S\s+\d+\.\s", line) or re.search(r"\S\s+[-*+]\s", line):
                source_path = Path(source_context) if source_context else None
                log_processing_error(
                    "List marker found mid-line in function declaration",
                    source_path,
                )

    # Check for mixed markers
    if has_ordered and has_unordered:
        source_path = Path(source_context) if source_context else None
        log_processing_error(
            "Mixed list markers (ordered and unordered) in function declaration",
            source_path,
        )

    # Transform declaration lines: remove blank lines and list markers
    transformed_declaration = []
    for line in declaration_lines:
        # Skip blank lines
        if not line.strip():
            continue

        # Remove ordered list markers
        new_line = _ORDERED_LIST_MARKER.sub("", line)

        # Remove unordered list markers
        new_line = _UNORDERED_LIST_MARKER.sub("", new_line)

        transformed_declaration.append(new_line)

    # Reconstruct the content
    result_lines = (
        lines[:start_index] + transformed_declaration + lines[end_index + 1 :]
    )

    return "\n".join(result_lines)
