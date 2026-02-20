"""Transformation functions for markdown content.

This module contains functions for cleaning up and transforming markdown
content during the HTML to markdown conversion process.
"""

import re

from flutterdoc_gen._shared.logging import get_notification_logger
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
        notification_logger = get_notification_logger()
        unique_patterns = set(pattern for _, pattern in _unmatched_patterns)
        notification_logger.info(
            "Found %d unmatched HTML link patterns (%d unique)",
            len(_unmatched_patterns),
            len(unique_patterns),
        )
        for pattern in sorted(unique_patterns):
            count = sum(1 for _, p in _unmatched_patterns if p == pattern)
            notification_logger.info("  %dx: %s", count, pattern)


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


def fix_arrow_spacing(content: str) -> str:
    """Ensure arrow patterns have proper spacing.

    Ensures that arrow patterns (→, ↔, ->, =>, <->, <=>, ➜, ➔) are:
    - Preceded by a space, unless at the start of a line
    - Followed by a space, unless at the end of a line

    Args:
        content: The markdown content to transform.

    Returns:
        The content with proper spacing around arrow patterns.
    """
    # Arrow patterns in order: longer patterns first to avoid partial matches
    # Supported: <-> , <=> , -> , => , → (U+2192), ↔ (U+2194), ➜ (U+279C), ➔ (U+2794)
    arrow_pattern = r"(<->|<=>|->|=>|\u2192|\u2194|\u279C|\u2794)"

    def fix_line(line: str) -> str:
        """Fix arrow spacing for a single line."""
        # Pattern to find arrows that need space before (not at line start, not preceded by space)
        # Negative lookbehind for start-of-string or space
        line = re.sub(r"(?<!^)(?<! )" + arrow_pattern, r" \1", line)

        # Pattern to find arrows that need space after (not at line end, not followed by space)
        # Negative lookahead for end-of-string or space
        line = re.sub(arrow_pattern + r"(?! )(?!$)", r"\1 ", line)

        return line

    lines = content.split("\n")
    result_lines = [fix_line(line) for line in lines]
    return "\n".join(result_lines)


# --- Link Transformation Functions ---


def transform_class_links(content: str) -> str:
    """Transform class links to MCP URI format.

    Replaces links of the form [CLASS_NAME](SECTION/CLASS_NAME-class.html)
    with [CLASS_NAME](flutter-docs://api/SECTION/CLASS_NAME).

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with class links transformed.
    """
    class_pattern = next(p for p in LINK_PATTERNS if p.name == "class_link")
    return re.sub(class_pattern.pattern, class_pattern.replacement, content)


def transform_mixin_links(content: str) -> str:
    """Transform mixin links to MCP URI format.

    Replaces links of the form [MIXIN_NAME](SECTION/MIXIN_NAME-mixin.html)
    with [MIXIN_NAME](flutter-docs://api/SECTION/MIXIN_NAME).

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with mixin links transformed.
    """
    mixin_pattern = next(p for p in LINK_PATTERNS if p.name == "mixin_link")
    return re.sub(mixin_pattern.pattern, mixin_pattern.replacement, content)


def transform_constant_links(content: str) -> str:
    """Transform constant links to MCP URI format.

    Replaces links of the form [CONSTANT_NAME](SECTION/CONSTANT_NAME-constant.html)
    with [CONSTANT_NAME](flutter-docs://api/SECTION/CONSTANT_NAME).

    This handles 2-part paths for root-level constant entities. This is distinct
    from 3-part paths for enum member constants (handled by transform_enum_constant_links).

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with constant links transformed.
    """
    constant_pattern = next(p for p in LINK_PATTERNS if p.name == "constant_link")
    return re.sub(constant_pattern.pattern, constant_pattern.replacement, content)


def transform_extension_type_links(content: str) -> str:
    """Transform extension type links to MCP URI format.

    Replaces links of the form [EXTENSION_TYPE_NAME](SECTION/EXTENSION_TYPE_NAME-extension-type.html)
    with [EXTENSION_TYPE_NAME](flutter-docs://api/SECTION/EXTENSION_TYPE_NAME).

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with extension type links transformed.
    """
    extension_type_pattern = next(
        p for p in LINK_PATTERNS if p.name == "extension_type_link"
    )
    return re.sub(
        extension_type_pattern.pattern, extension_type_pattern.replacement, content
    )


def transform_other_root_links(content: str) -> str:
    """Transform other root documentation links to MCP URI format.

    Replaces links of the form [ROOT_DOC_NAME](SECTION/ROOT_DOC_NAME.html)
    with [ROOT_DOC_NAME](flutter-docs://api/SECTION/ROOT_DOC_NAME).

    This handles all root documentation files EXCEPT those with specific suffixes
    (-class, -mixin, -constant, -extension-type) which are handled by other
    transformation functions. This must be called after those more specific
    transformations to avoid premature matching.

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with other root links transformed.
    """
    other_root_pattern = next(p for p in LINK_PATTERNS if p.name == "other_root_link")
    return re.sub(other_root_pattern.pattern, other_root_pattern.replacement, content)


def transform_named_constructor_links(content: str) -> str:
    """Transform named constructor links to MCP URI format.

    Replaces links of the form [ENTITY_NAME.MEMBER_NAME](SECTION/ENTITY_NAME/ENTITY_NAME.MEMBER_NAME.html)
    with [ENTITY_NAME.MEMBER_NAME](flutter-docs://api/SECTION/ENTITY_NAME/ENTITY_NAME.MEMBER_NAME).

    This handles 3-part paths where the entity name is repeated in the filename,
    which is the pattern used for named constructors and static factory methods
    (e.g., ThemeData.from, Text.rich, IconButton.filled). This is distinct from
    regular member links which use the pattern ENTITY/MEMBER.html without repetition.

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with named constructor links transformed.
    """
    named_constructor_pattern = next(
        p for p in LINK_PATTERNS if p.name == "named_constructor_link"
    )
    return re.sub(
        named_constructor_pattern.pattern,
        named_constructor_pattern.replacement,
        content,
    )


def transform_enum_constant_links(content: str) -> str:
    """Transform enum constant links to MCP URI format.

    Replaces links of the form [CONSTANT](SECTION/ENUM/CONSTANT-constant.html)
    with [CONSTANT](flutter-docs://api/SECTION/ENUM/CONSTANT).

    This handles 3-part paths with -constant.html suffix, which are enum member
    constants (like the `values` constant on enums). This is distinct from
    2-part paths for root-level CategoryType.CONSTANT entities.

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with enum constant links transformed.
    """
    enum_constant_pattern = next(
        p for p in LINK_PATTERNS if p.name == "enum_constant_link"
    )
    return re.sub(
        enum_constant_pattern.pattern, enum_constant_pattern.replacement, content
    )


def transform_member_links(content: str) -> str:
    """Transform member links to MCP URI format.

    Replaces links of the form [MEMBER](SECTION/ENTITY/MEMBER.html)
    with [MEMBER](flutter-docs://api/SECTION/ENTITY/MEMBER).

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


def transform_unmapped_links(content: str) -> str:
    """Transform unmapped relative links to placeholder text.

    Replaces links of the form [LINK_TEXT](URI) with [Omitted link: LINK_TEXT]
    where URI does not start with http://, https://, flutter-docs://, or #.

    This transformation acts as a catch-all for any relative links that were
    not transformed by other more specific transformation functions. It excludes:
    - http:// and https:// URLs (external websites)
    - flutter-docs:// URIs (already transformed Flutter docs links)
    - # anchors (in-document navigation)

    Uses patterns from LINK_PATTERNS registry.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with unmapped relative links replaced by placeholder text.
    """
    unmapped_pattern = next(p for p in LINK_PATTERNS if p.name == "unmapped_link")
    return re.sub(unmapped_pattern.pattern, unmapped_pattern.replacement, content)


def fix_link_spacing(content: str) -> str:
    """Add missing space after markdown links followed by text.

    Fixes patterns where html-to-markdown produces links immediately followed
    by text due to HTML span handling. This commonly occurs with Dart type
    annotations where a type link is followed by an identifier.

    Fixes patterns like:
    - [Widget](url)foo -> [Widget](url) foo
    - [Widget](url)?bar -> [Widget](url)? bar
    - [Widget](url)_baz -> [Widget](url) _baz

    Args:
        content: The markdown content to transform.

    Returns:
        The content with proper spacing after links.
    """
    # Pattern: link closing paren, optional nullable marker, then identifier start
    # Captures: 1=closing bracket and paren with URL, 2=optional ?, 3=identifier char
    pattern = r"(\]\([^)]+\))(\??)([a-zA-Z_])"
    replacement = r"\1\2 \3"
    return re.sub(pattern, replacement, content)


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
    2. Transform mixin links to MCP URI format
    3. Transform constant links to MCP URI format (2-part root constants)
    4. Transform extension type links to MCP URI format
    5. Transform other root links to MCP URI format (catch-all for remaining 2-part)
    6. Transform named constructor links to MCP URI format (3-part with entity.member pattern)
    7. Transform enum constant links to MCP URI format (3-part enum members)
    8. Transform member links to MCP URI format (3-part entity members)
    9. Transform image links to placeholder text
    10. Transform DartPad links to placeholder text
    11. Transform unmapped links to placeholder text (catch-all for remaining relative links)
    12. Fix link spacing issues after markdown links

    Note: More specific 2-part patterns (class, mixin, constant, extension-type)
    must come before the catch-all other_root pattern. The 3-part patterns
    (named_constructor, enum_constant, member) follow after all 2-part patterns,
    with more specific patterns (named_constructor, enum_constant) before the
    general member pattern.

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
    content = fix_arrow_spacing(content)

    # Link transformations
    # 2-part root documentation patterns (most specific first, catch-all last)
    content = transform_class_links(content)
    content = transform_mixin_links(content)
    content = transform_constant_links(content)
    content = transform_extension_type_links(content)
    content = transform_other_root_links(content)
    # 3-part member patterns (more specific patterns before general member pattern)
    content = transform_named_constructor_links(content)
    content = transform_enum_constant_links(content)
    content = transform_member_links(content)
    # Special link handling
    content = transform_image_links(content)
    content = transform_dartpad_links(content)
    content = transform_unmapped_links(content)
    content = fix_link_spacing(content)

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


def _is_header_line(line: str) -> bool:
    """Check if a line is a markdown header.

    Args:
        line: The line to check.

    Returns:
        True if the line starts with '#' followed by a space.
    """
    return line.startswith("#") and " " in line


def cleanup_function_declaration(content: str, source_context: str = "") -> str:
    """Clean up multi-line function declaration formatting in markdown content.

    This transformation removes blank lines and list markers from function
    declarations (constructors, methods, operators, static methods).

    The transformation operates on content between:
    - Start: First non-blank line after the first header (halts on subsequent header)
    - End: First line containing only ')' or '})' (optionally with comments),
           searched after start line (halts on subsequent header)

    Args:
        content: The markdown content to transform.
        source_context: Context string for logging (typically file path).

    Returns:
        The transformed content with clean function declarations, or the
        original content unchanged if no transformation is applicable or
        an edge case is encountered.

    Note:
        Logs an informational message and returns unchanged for edge cases:
        - List markers mid-line
    """
    lines = content.split("\n")

    # Find the first header line
    header_index = None
    for i, line in enumerate(lines):
        if _is_header_line(line):
            header_index = i
            break

    # If no header found, return content unchanged
    if header_index is None:
        return content

    # Find the start pattern: first non-blank line after header
    # Halt if a subsequent header is encountered
    start_index = None
    for i in range(header_index + 1, len(lines)):
        line = lines[i]
        if _is_header_line(line):
            # Halt: encountered another header before finding start
            break
        if line.strip():  # Non-blank line
            start_index = i
            break

    # If no start pattern found, return content unchanged
    if start_index is None:
        return content

    # Find the end pattern: first line with only ) or }) possibly with comments
    # Search starts AFTER the start line and halts on header
    end_index = None
    for i in range(start_index + 1, len(lines)):
        line = lines[i]
        if _is_header_line(line):
            # Halt: encountered header before finding end pattern
            break
        if _CLOSING_PAREN_PATTERN.match(line) or _CLOSING_BRACE_PAREN_PATTERN.match(
            line
        ):
            end_index = i
            break

    # If no end pattern found, likely a single-line signature. Return unchanged.
    if end_index is None:
        return content

    # Process lines between start and end (inclusive)
    declaration_lines = lines[start_index : end_index + 1]

    for line in declaration_lines:
        stripped = line.lstrip()

        # Check for mid-line list markers (marker not at start of content)
        # Only check non-blank lines that aren't entirely a list marker line
        if (
            stripped
            and not _ORDERED_LIST_MARKER.match(stripped)
            and not _UNORDERED_LIST_MARKER.match(stripped)
        ):
            # Look for list markers that appear after other content
            if re.search(r"\S\s+\d+\.\s", line) or re.search(r"\S\s+[-*+]\s", line):
                notification_logger = get_notification_logger()
                notification_logger.info(
                    "Skipping transformation: list marker found mid-line "
                    "in function declaration (%s)",
                    source_context or "unknown",
                )
                return content

    # Transform declaration lines: remove blank lines and list markers
    transformed_declaration = []
    for line in declaration_lines:
        stripped = line.lstrip()
        # Skip blank lines. Capture indent for non-blank lines.
        if not stripped:
            continue
        indent = len(line) - len(stripped)

        # Remove ordered list markers
        new_line = _ORDERED_LIST_MARKER.sub("", stripped)

        # Remove unordered list markers
        new_line = _UNORDERED_LIST_MARKER.sub("", new_line)

        # Add indentation back to preserve readability
        new_line = " " * indent + new_line

        transformed_declaration.append(new_line)

    # Reconstruct the content
    result_lines = (
        lines[:start_index] + transformed_declaration + lines[end_index + 1 :]
    )

    return "\n".join(result_lines)
