"""Convert Flutter/Dart HTML documentation to markdown.

This script converts HTML documentation files to markdown format using the
html_to_markdown package, applies transformations to clean up the output, and
concatenates related files into single class documentation files.
"""

import argparse
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from html_to_markdown import (
    ConversionOptions,
    ConversionOptionsHandle,
    convert_with_handle,
    create_options_handle,
)


# Module-level tracking of unmatched HTML link patterns
_unmatched_patterns: list[tuple[str, str]] = []  # List of (context, pattern)

# Noise strings to remove from converted markdown
# These are artifacts from the HTML conversion that don't add value
NOISE_STRINGS: tuple[str, ...] = (
    "const",
    "final",
    "no setterinherited",
    "finalinherited",
    "inherited",
    '[*link*](# "Copy link to clipboard")',
)

# Analytics/tracking domains to filter from output
TRACKING_DOMAINS: tuple[str, ...] = ("googletagmanager.com",)


# --- Link Transformation Pattern Registry ---


@dataclass(frozen=True)
class LinkPattern:
    """A pattern for transforming markdown links.

    Attributes:
        name: A human-readable name for the pattern.
        pattern: The regex pattern to match.
        replacement: The replacement string (can use capture groups).
        description: A description of what this pattern matches.
    """

    name: str
    pattern: str
    replacement: str
    description: str


# Centralized registry of link transformation patterns
# Order matters: more specific patterns should come before less specific ones
LINK_PATTERNS: tuple[LinkPattern, ...] = (
    # Class links
    LinkPattern(
        name="class_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-class\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3)",
        description="[ClassName](section/ClassName-class.html)",
    ),
    LinkPattern(
        name="type_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3)",
        description="[Type](section/Type.html) - types and references",
    ),
    # Member links (more specific patterns first)
    LinkPattern(
        name="dotted_member_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3/\4)",
        description="[Class.member](section/Class/Class.member.html) - named constructors/static methods",
    ),
    LinkPattern(
        name="member_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3/\4)",
        description="[member](section/Class/member.html)",
    ),
    # Special links
    LinkPattern(
        name="image_link",
        pattern=r"!\[([^\]]*)\]\([^)]+\)",
        replacement=r"[Note: Image \1 omitted]",
        description="![alt text](path) - image links",
    ),
    LinkPattern(
        name="dartpad_link",
        pattern=r"\[[^\]]+\]\([^)]*dartpad\.dev[^)]*\)",
        replacement="[Note: Interactive sample omitted]",
        description="[text](url with dartpad.dev) - DartPad links",
    ),
)

# Pattern for detecting unmatched relative HTML links
UNMATCHED_HTML_LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?!https?://)[^)]+\.html[^)]*\)")


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


# --- Transformation Functions ---


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

    Removes all content from the line containing "1. [Flutter](index.html)"
    to the end of the file.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with footer removed. If the footer marker is not found,
        returns the original content.
    """
    marker = "1. [Flutter](index.html)"
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if marker in line:
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


# --- Section Parsing Functions ---


def _normalize_heading_text(heading_text: str) -> str:
    """Normalize heading text for comparison.

    Removes anchor syntax ({#id}), normalizes whitespace, and converts to lowercase.

    Args:
        heading_text: The raw heading text (after ## prefix).

    Returns:
        Normalized heading text for case-insensitive comparison.
    """
    # Remove anchor syntax like {#constructors}
    anchor_pattern = re.compile(r"\s*\{#[^}]+\}\s*")
    text = anchor_pattern.sub("", heading_text)
    # Normalize whitespace and lowercase
    return " ".join(text.split()).lower()


def extract_section_content(markdown: str, section_name: str) -> str | None:
    """Extract content from a specific section of markdown.

    Extracts all content between a section heading (## section_name) and the
    next heading of the same or higher level. Handles variations in heading
    format including extra whitespace, anchor syntax ({#id}), and is
    case-insensitive.

    Args:
        markdown: The markdown content to search.
        section_name: The name of the section to extract (without ##).

    Returns:
        The content of the section, or None if the section is not found.
    """
    lines = markdown.split("\n")
    in_section = False
    section_lines: list[str] = []
    normalized_target = _normalize_heading_text(section_name)

    for line in lines:
        stripped = line.lstrip()

        # Check if this is the target section heading
        if stripped.startswith("## "):
            heading_text = stripped[3:]
            if _normalize_heading_text(heading_text) == normalized_target:
                in_section = True
                continue

        # Check if we've hit the next section (same or higher level heading)
        if in_section and stripped.startswith("#"):
            # Count the heading level
            heading_level = 0
            for char in stripped:
                if char == "#":
                    heading_level += 1
                else:
                    break
            # Stop if we hit a heading of level 1 or 2
            if heading_level <= 2:
                break

        if in_section:
            section_lines.append(line)

    if not section_lines:
        return None

    return "\n".join(section_lines)


def extract_member_links(
    section_content: str,
) -> list[dict[str, str]]:
    """Extract member links from section content.

    Parses lines that start with [MEMBER](mcp://flutter/api/SECTION/CLASS/MEMBER)
    followed by a type signature arrow (→, ->, etc.), and captures the link text,
    section, class, member name, result type, and description.

    Args:
        section_content: The markdown content of a section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - class_name: The class from the URI
        - member: The member name from the URI
        - result_type: The result type (text after arrow on the same line), or empty string
        - description: Lines following the link until a blank line, or empty string
    """
    members: list[dict[str, str]] = []
    lines = section_content.split("\n")

    # Arrow patterns: Unicode rightwards arrow, ASCII arrow variants
    # Supported: → (U+2192), -> , => , ➜ (U+279C), ➔ (U+2794)
    arrow_pattern = r"(?:\u2192|\u279C|\u2794|->|=>)"

    # Pattern to match [text](mcp://flutter/api/section/class/member) followed by
    # optional whitespace and an arrow (type signature).
    # This distinguishes property definitions from inline references
    link_pattern = re.compile(
        r"^\s*\[([^\]]+)\]\(mcp://flutter/api/([^/]+)/([^/]+)/([^)]+)\)\s*"
        + arrow_pattern
    )

    i = 0
    while i < len(lines):
        line = lines[i]
        match = link_pattern.match(line)

        if match:
            link_text = match.group(1)
            section = match.group(2)
            class_name = match.group(3)
            member = match.group(4)

            # Extract result type (after arrow on same line)
            # Use regex to find the arrow and extract what follows
            result_type = ""
            arrow_search = re.search(arrow_pattern, line)
            if arrow_search:
                after_arrow = line[arrow_search.end() :].strip()
                # Result type is everything after the arrow on the same line
                if after_arrow:
                    result_type = after_arrow

            # Extract description (lines until blank line)
            description_lines: list[str] = []
            j = i + 1
            while j < len(lines):
                desc_line = lines[j]
                if desc_line.strip() == "":
                    break
                description_lines.append(desc_line)
                j += 1

            members.append(
                {
                    "link_text": link_text,
                    "section": section,
                    "class_name": class_name,
                    "member": member,
                    "result_type": result_type,
                    "description": "\n".join(description_lines),
                }
            )

        i += 1

    return members


def extract_static_method_links(
    section_content: str,
) -> list[dict[str, str]]:
    """Extract static method links from section content.

    Parses lines that start with [METHOD](mcp://flutter/api/SECTION/CLASS/METHOD)
    for static methods. Unlike properties/methods, static methods don't require
    capturing result_type or description - we just need the link information.

    Args:
        section_content: The markdown content of the Static Methods section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - class_name: The class from the URI
        - member: The member name from the URI
    """
    members: list[dict[str, str]] = []
    lines = section_content.split("\n")

    # Pattern to match [text](mcp://flutter/api/section/class/member)
    # For static methods, we don't require the arrow - just the MCP link at line start
    link_pattern = re.compile(
        r"^\s*\[([^\]]+)\]\(mcp://flutter/api/([^/]+)/([^/]+)/([^)]+)\)"
    )

    for line in lines:
        match = link_pattern.match(line)

        if match:
            link_text = match.group(1)
            section = match.group(2)
            class_name = match.group(3)
            member = match.group(4)

            members.append(
                {
                    "link_text": link_text,
                    "section": section,
                    "class_name": class_name,
                    "member": member,
                }
            )

    return members


# --- Inherited Member Templates ---

INHERITED_PROPERTY_TEMPLATE = """# {property} property

{result_type} {property}

{description}

This property is inherited from [{some_class}](mcp://flutter/api/{some_section}/{some_class}).
See further details at [{property}](mcp://flutter/api/{some_section}/{some_class}/{property}).
"""

INHERITED_METHOD_TEMPLATE = """# {method} method

{result_type} {method}(/* See {some_class} documentation for parameters */)

{description}

This method is inherited from [{some_class}](mcp://flutter/api/{some_section}/{some_class}).
See further details at [{method}](mcp://flutter/api/{some_section}/{some_class}/{method}).
"""

INHERITED_OPERATOR_TEMPLATE = """# {operator_symbol} ({operator}) method

{result_type} {operator_symbol}(/* See {some_class} documentation for parameters */)

{description}

This operator is inherited from [{some_class}](mcp://flutter/api/{some_section}/{some_class}).
See further details at [{operator_symbol}](mcp://flutter/api/{some_section}/{some_class}/{operator}).
"""


# --- Conversion Functions ---


def convert_html_to_markdown(
    options_handle: ConversionOptionsHandle, html_path: Path
) -> str:
    """Convert an HTML file to markdown and apply transformations.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        html_path: Path to the HTML file to convert.

    Returns:
        The transformed markdown content.

    Raises:
        FileNotFoundError: If the HTML file does not exist.
    """
    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    try:
        md_text = convert_with_handle(
            html_path.read_text(encoding="utf-8"), options_handle
        )
    except Exception as e:
        raise RuntimeError(f"Error reading or converting HTML file {html_path}: {e}")

    return apply_transformations(md_text, source_context=str(html_path))


def convert_dart_snippet(dart_path: Path, class_name: str, section: str) -> str:
    """Convert a Dart snippet file to markdown.

    Wraps the Dart code in a markdown code block with a header.

    Args:
        dart_path: Path to the Dart file to convert.
        class_name: The name of the class the snippet belongs to.
        section: The documentation section name.

    Returns:
        The Dart code wrapped in markdown format.

    Raises:
        FileNotFoundError: If the Dart file does not exist.
    """
    if not dart_path.exists():
        raise FileNotFoundError(f"Dart file not found: {dart_path}")

    content = dart_path.read_text(encoding="utf-8")
    return f"# Code Snippet for {class_name} in {section}\n\n```dart\n{content}\n```"


# --- Member Processing Functions ---


def process_constructors(
    class_markdown: str,
    current_section: str,
    current_class: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process constructor files for a class.

    Scans the Constructors section and converts each constructor HTML file.

    Args:
        class_markdown: The converted markdown content of the main class file.
        current_section: The current documentation section name.
        current_class: The current class name.
        doc_dir: The root documentation directory.
        output_dir: The class output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(class_markdown, "Constructors")
    if section_content is None:
        logging.info(f"No Constructors section found in {current_class}")
        return

    members = extract_member_links(section_content)
    if not members:
        logging.info(f"No constructor links found in {current_class}")
        return

    constructors_dir = output_dir / "constructors"
    constructors_dir.mkdir(parents=True, exist_ok=True)

    for member in members:
        # Constructors must be in the same section/class
        if (
            member["section"] != current_section
            or member["class_name"] != current_class
        ):
            logging.error(
                f"Constructor link has unexpected URI: "
                f"mcp://flutter/api/{member['section']}/{member['class_name']}/{member['member']}"
            )
            sys.exit(1)

        html_path = (
            doc_dir
            / "flutter"
            / current_section
            / current_class
            / f"{member['member']}.html"
        )
        if not html_path.exists():
            logging.error(f"Constructor HTML file not found: {html_path}")
            sys.exit(1)

        markdown_content = convert_html_to_markdown(options_handle, html_path)
        output_file = constructors_dir / f"{member['member']}.md"
        output_file.write_text(markdown_content, encoding="utf-8")


def process_properties(
    class_markdown: str,
    current_section: str,
    current_class: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process property files for a class.

    Scans the Properties section and either converts native property HTML files
    or generates inherited property markdown files.

    Args:
        class_markdown: The converted markdown content of the main class file.
        current_section: The current documentation section name.
        current_class: The current class name.
        doc_dir: The root documentation directory.
        output_dir: The class output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(class_markdown, "Properties")
    if section_content is None:
        logging.info(f"No Properties section found in {current_class}")
        return

    members = extract_member_links(section_content)
    if not members:
        logging.info(f"No property links found in {current_class}")
        return

    native_dir = output_dir / "properties" / "native"
    inherited_dir = output_dir / "properties" / "inherited"

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["class_name"] == current_class
        )

        if is_native:
            native_dir.mkdir(parents=True, exist_ok=True)
            html_path = (
                doc_dir
                / "flutter"
                / current_section
                / current_class
                / f"{member['member']}.html"
            )
            if not html_path.exists():
                logging.error(f"Property HTML file not found: {html_path}")
                sys.exit(1)

            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = native_dir / f"{member['member']}.md"
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited property
            if not member["result_type"] or not member["description"]:
                logging.error(
                    f"Unable to capture result_type or description for inherited property "
                    f"{member['member']} from {member['section']}/{member['class_name']}"
                )
                sys.exit(1)

            inherited_dir.mkdir(parents=True, exist_ok=True)
            markdown_content = INHERITED_PROPERTY_TEMPLATE.format(
                property=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_class=member["class_name"],
            )
            filename = (
                f"{member['section']}-{member['class_name']}-{member['member']}.md"
            )
            output_file = inherited_dir / filename
            output_file.write_text(markdown_content, encoding="utf-8")


def process_methods(
    class_markdown: str,
    current_section: str,
    current_class: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process method files for a class.

    Scans the Methods section and either converts native method HTML files
    or generates inherited method markdown files.

    Args:
        class_markdown: The converted markdown content of the main class file.
        current_section: The current documentation section name.
        current_class: The current class name.
        doc_dir: The root documentation directory.
        output_dir: The class output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(class_markdown, "Methods")
    if section_content is None:
        logging.info(f"No Methods section found in {current_class}")
        return

    members = extract_member_links(section_content)
    if not members:
        logging.info(f"No method links found in {current_class}")
        return

    native_dir = output_dir / "methods" / "native"
    inherited_dir = output_dir / "methods" / "inherited"

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["class_name"] == current_class
        )

        if is_native:
            native_dir.mkdir(parents=True, exist_ok=True)
            html_path = (
                doc_dir
                / "flutter"
                / current_section
                / current_class
                / f"{member['member']}.html"
            )
            if not html_path.exists():
                logging.error(f"Method HTML file not found: {html_path}")
                sys.exit(1)

            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = native_dir / f"{member['member']}.md"
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited method
            if not member["result_type"] or not member["description"]:
                logging.error(
                    f"Unable to capture result_type or description for inherited method "
                    f"{member['member']} from {member['section']}/{member['class_name']}"
                )
                sys.exit(1)

            inherited_dir.mkdir(parents=True, exist_ok=True)
            markdown_content = INHERITED_METHOD_TEMPLATE.format(
                method=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_class=member["class_name"],
            )
            filename = (
                f"{member['section']}-{member['class_name']}-{member['member']}.md"
            )
            output_file = inherited_dir / filename
            output_file.write_text(markdown_content, encoding="utf-8")


def process_operators(
    class_markdown: str,
    current_section: str,
    current_class: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process operator files for a class.

    Scans the Operators section and either converts native operator HTML files
    or generates inherited operator markdown files.

    Args:
        class_markdown: The converted markdown content of the main class file.
        current_section: The current documentation section name.
        current_class: The current class name.
        doc_dir: The root documentation directory.
        output_dir: The class output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(class_markdown, "Operators")
    if section_content is None:
        logging.info(f"No Operators section found in {current_class}")
        return

    members = extract_member_links(section_content)
    if not members:
        logging.info(f"No operator links found in {current_class}")
        return

    native_dir = output_dir / "operators" / "native"
    inherited_dir = output_dir / "operators" / "inherited"

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["class_name"] == current_class
        )

        if is_native:
            native_dir.mkdir(parents=True, exist_ok=True)
            html_path = (
                doc_dir
                / "flutter"
                / current_section
                / current_class
                / f"{member['member']}.html"
            )
            if not html_path.exists():
                logging.error(f"Operator HTML file not found: {html_path}")
                sys.exit(1)

            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = native_dir / f"{member['member']}.md"
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited operator
            if not member["result_type"] or not member["description"]:
                logging.error(
                    f"Unable to capture result_type or description for inherited operator "
                    f"{member['member']} from {member['section']}/{member['class_name']}"
                )
                sys.exit(1)

            inherited_dir.mkdir(parents=True, exist_ok=True)
            markdown_content = INHERITED_OPERATOR_TEMPLATE.format(
                operator_symbol=member["link_text"],
                operator=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_class=member["class_name"],
            )
            filename = (
                f"{member['section']}-{member['class_name']}-{member['member']}.md"
            )
            output_file = inherited_dir / filename
            output_file.write_text(markdown_content, encoding="utf-8")


def process_static_methods(
    class_markdown: str,
    current_section: str,
    current_class: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process static method files for a class.

    Scans the Static Methods section and converts native static method HTML files.
    Static methods have no inherited variant since static members belong to the
    declaring class only.

    Args:
        class_markdown: The converted markdown content of the main class file.
        current_section: The current documentation section name.
        current_class: The current class name.
        doc_dir: The root documentation directory.
        output_dir: The class output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(class_markdown, "Static Methods")
    if section_content is None:
        # Silent handling per spec - no message if section not found
        return

    members = extract_static_method_links(section_content)
    if not members:
        # Silent handling per spec - no message if no matches found
        return

    statics_dir = output_dir / "statics"

    for member in members:
        # Validate that static method belongs to current class
        is_native = (
            member["section"] == current_section
            and member["class_name"] == current_class
        )

        if not is_native:
            # Static methods should only reference the current class
            logging.error(
                f"Static method link has unexpected URI scheme: "
                f"{member['section']}/{member['class_name']}/{member['member']} "
                f"(expected {current_section}/{current_class})"
            )
            sys.exit(1)

        statics_dir.mkdir(parents=True, exist_ok=True)
        html_path = (
            doc_dir
            / "flutter"
            / current_section
            / current_class
            / f"{member['member']}.html"
        )
        if not html_path.exists():
            logging.error(f"Static method HTML file not found: {html_path}")
            sys.exit(1)

        markdown_content = convert_html_to_markdown(options_handle, html_path)
        output_file = statics_dir / f"{member['member']}.md"
        output_file.write_text(markdown_content, encoding="utf-8")


def process_snippets(
    doc_dir: Path,
    output_dir: Path,
    section: str,
    class_name: str,
) -> None:
    """Process code snippet files for a class.

    Converts Dart snippet files to markdown and saves them.

    Args:
        doc_dir: The root documentation directory.
        output_dir: The class output directory.
        section: The documentation section name.
        class_name: The class name.
    """
    snippets_dir = doc_dir / "snippets"
    snippet_pattern = f"{section}.{class_name}.*.dart"
    snippet_files = sorted(snippets_dir.glob(snippet_pattern))

    if not snippet_files:
        return

    output_snippets_dir = output_dir / "snippets"
    output_snippets_dir.mkdir(parents=True, exist_ok=True)

    for snippet_file in snippet_files:
        # Extract SHORT_NAME: remove {section}.{class_name}. prefix and .dart suffix
        prefix = f"{section}.{class_name}."
        short_name = snippet_file.name[len(prefix) : -len(".dart")]

        markdown_content = convert_dart_snippet(snippet_file, class_name, section)
        output_file = output_snippets_dir / f"{short_name}.md"
        output_file.write_text(markdown_content, encoding="utf-8")


# --- File Discovery Functions ---


def find_class_files(doc_dir: Path, section: str) -> list[tuple[str, Path]]:
    """Find all class documentation files for a section.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Returns:
        A list of tuples, each containing:
        - class_name: The name of the class
        - class_file: Path to the main class HTML file
    """
    section_dir = doc_dir / "flutter" / section

    classes = []

    # Find all *-class.html files
    class_files = sorted(section_dir.glob("*-class.html"))

    for class_file in class_files:
        # Extract class name from filename (e.g., "ListTile" from "ListTile-class.html")
        class_name = class_file.stem.replace("-class", "")
        classes.append((class_name, class_file))

    return classes


# --- Main Processing Functions ---


def process_class(
    options_handle: ConversionOptionsHandle,
    class_name: str,
    class_file: Path,
    section: str,
    doc_dir: Path,
    output_dir: Path,
) -> None:
    """Process all documentation files for a class using the 7-step pipeline.

    Steps:
    1. Process the class file
    2. Process constructor files
    3. Process property files
    4. Process method files
    5. Process operator files
    6. Process static method files
    7. Process code snippet files

    Args:
        options_handle: The ConversionOptionsHandle instance for conversion.
        class_name: The name of the class being processed.
        class_file: Path to the main class HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        output_dir: The section output directory (api/{section}).
    """
    # Create class output directory
    class_output_dir = output_dir / class_name
    class_output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Process the class file
    logging.info(f"  Processing class file: {class_file}")
    class_markdown = convert_html_to_markdown(options_handle, class_file)
    class_output_file = class_output_dir / f"{class_name}.md"
    class_output_file.write_text(class_markdown, encoding="utf-8")

    # Step 2: Process constructor files
    logging.info(f"  Processing constructors for {class_name}")
    process_constructors(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 3: Process property files
    logging.info(f"  Processing properties for {class_name}")
    process_properties(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 4: Process method files
    logging.info(f"  Processing methods for {class_name}")
    process_methods(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 5: Process operator files
    logging.info(f"  Processing operators for {class_name}")
    process_operators(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 6: Process static method files
    logging.info(f"  Processing static methods for {class_name}")
    process_static_methods(
        class_markdown, section, class_name, doc_dir, class_output_dir, options_handle
    )

    # Step 7: Process code snippet files
    logging.info(f"  Processing snippets for {class_name}")
    process_snippets(doc_dir, class_output_dir, section, class_name)


def validate_directories(doc_dir: Path, section: str) -> None:
    """Validate that required directories exist.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Raises:
        SystemExit: If any required directory does not exist.
    """
    if not doc_dir.exists() or not doc_dir.is_dir():
        logging.error(f"Documentation directory does not exist: {doc_dir}")
        sys.exit(1)

    section_dir = doc_dir / "flutter" / section
    if not section_dir.exists() or not section_dir.is_dir():
        logging.error(f"Section directory does not exist: {section_dir}")
        sys.exit(1)

    snippets_dir = doc_dir / "snippets"
    if not snippets_dir.exists() or not snippets_dir.is_dir():
        logging.error(f"Snippets directory does not exist: {snippets_dir}")
        sys.exit(1)


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
    section_output = output_dir / "api" / section
    try:
        section_output.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logging.error(f"Cannot create output directory {section_output}: {e}")
        sys.exit(1)

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
    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
    )

    # Reset unmatched pattern tracking
    reset_unmatched_patterns()

    # Validate directories
    validate_directories(args.documents, args.section)

    # Create output directory
    output_section_dir = create_output_directory(args.output, args.section)

    # Initialize html_to_markdown
    options_handle = create_options_handle(ConversionOptions())

    # Find and process class documentation files
    classes = find_class_files(args.documents, args.section)

    if not classes:
        print(f"No files found matching pattern in section '{args.section}'")
        sys.exit(0)

    for class_name, class_file in classes:
        logging.info(f"Converting class: {class_name}")

        try:
            # Process documentation files for the class
            process_class(
                options_handle,
                class_name,
                class_file,
                args.section,
                args.documents,
                output_section_dir,
            )
        except OSError as e:
            logging.error(f"Cannot write output file for {class_name}: {e}")
            sys.exit(1)

    # Log summary of unmatched HTML link patterns
    log_unmatched_summary()

    print(
        f"Successfully processed {len(classes)} classes from section '{args.section}'"
    )


if __name__ == "__main__":
    main()
