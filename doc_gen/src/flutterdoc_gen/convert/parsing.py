"""Parsing functions for extracting content from markdown.

This module contains functions for parsing and extracting structured
information from markdown content, such as section content and member links.
"""

import re

from flutterdoc_gen.convert.patterns import MCP_URI_PREFIX


def split_into_paragraphs(section_content: str) -> list[str]:
    """Split section content into paragraphs.

    A paragraph is a block of non-empty lines bounded by blank lines or section
    headers. Section headers act as paragraph boundaries but are not included
    in the resulting paragraphs.

    This approach is robust to markdown formatting variations - it works whether
    or not there are blank lines after section headers or before the next section.

    Args:
        section_content: The markdown content of a section.

    Returns:
        A list of paragraph strings, where each paragraph is the concatenated
        lines of that paragraph (preserving internal newlines).
    """
    lines = section_content.split("\n")
    paragraphs: list[str] = []
    current_paragraph: list[str] = []

    for line in lines:
        # Section header terminates current paragraph (but is not included)
        if line.strip().startswith("#"):
            if current_paragraph:
                paragraphs.append("\n".join(current_paragraph))
                current_paragraph = []
            continue

        # Blank line terminates current paragraph
        if line.strip() == "":
            if current_paragraph:
                paragraphs.append("\n".join(current_paragraph))
                current_paragraph = []
            continue

        # Content line - add to current paragraph
        current_paragraph.append(line)

    # Don't forget the last paragraph
    if current_paragraph:
        paragraphs.append("\n".join(current_paragraph))

    return paragraphs


def extract_member_definitions(section_content: str) -> list[dict[str, str]]:
    """Extract member definitions from section content.

    Works for Properties, Methods, and Operators sections. Uses paragraph-based
    parsing for robustness: each member definition is a paragraph where the first
    line contains the member link with an arrow, and remaining lines are the
    description.

    This unified approach handles all member types (properties, methods, operators)
    consistently, regardless of where the arrow appears on the first line.

    Args:
        section_content: The markdown content of a section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - entity_name: The entity from the URI
        - member: The member name from the URI
        - result_type: The result type (text after arrow on first line), stripped
        - description: Lines following the first line, or empty string
    """
    members: list[dict[str, str]] = []
    paragraphs = split_into_paragraphs(section_content)

    # Pattern to match [text](mcp://flutter/api/section/entity/member)
    link_pattern = re.compile(
        rf"^\s*\[([^\]]+)\]\({MCP_URI_PREFIX}([^/]+)/([^/]+)/([^)]+)\)"
    )

    # Arrow pattern: Unicode rightwards arrow, left-right arrow, ASCII arrow variants
    # Supported: → (U+2192), ↔ (U+2194), -> , => , <-> , <=> , ➜ (U+279C), ➔ (U+2794)
    arrow_pattern = re.compile(r"(?:\u2192|\u2194|\u279C|\u2794|<->|<=>|->|=>)")

    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        if not lines:
            continue

        first_line = lines[0]
        description_lines = lines[1:] if len(lines) > 1 else []

        # Check if first line has an MCP link
        match = link_pattern.match(first_line)
        if not match:
            continue

        # Check if first line has an arrow (distinguishes definitions from inline refs)
        arrow_match = arrow_pattern.search(first_line)
        if not arrow_match:
            continue

        # Extract link components
        link_text = match.group(1)
        section = match.group(2)
        entity_name = match.group(3)
        member = match.group(4)

        # Extract result type: everything after arrow on first line, stripped
        result_type = first_line[arrow_match.end() :].strip()

        # Extract description: remaining lines of paragraph
        description = "\n".join(description_lines).strip()

        members.append(
            {
                "link_text": link_text,
                "section": section,
                "entity_name": entity_name,
                "member": member,
                "result_type": result_type,
                "description": description,
            }
        )

    return members


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

    Parses lines that start with [MEMBER](mcp://flutter/api/SECTION/ENTITY/MEMBER)
    followed by a type signature arrow (→, ->, etc.), and captures the link text,
    section, entity, member name, result type, and description.

    Args:
        section_content: The markdown content of a section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - entity_name: The entity from the URI
        - member: The member name from the URI
        - result_type: The result type (text after arrow on the same line), or empty string
        - description: Lines following the link until a blank line, or empty string
    """
    members: list[dict[str, str]] = []
    lines = section_content.split("\n")

    # Arrow patterns: Unicode rightwards arrow, left-right arrow, ASCII arrow variants
    # Supported: → (U+2192), ↔ (U+2194), -> , => , <-> , <=> , ➜ (U+279C), ➔ (U+2794)
    arrow_pattern = r"(?:\u2192|\u2194|\u279C|\u2794|<->|<=>|->|=>)"

    # Pattern to match [text](mcp://flutter/api/section/entity/member) followed by
    # optional whitespace and an arrow (type signature).
    # This distinguishes property definitions from inline references
    link_pattern = re.compile(
        rf"^\s*\[([^\]]+)\]\({MCP_URI_PREFIX}([^/]+)/([^/]+)/([^)]+)\)\s*"
        + arrow_pattern
    )

    i = 0
    while i < len(lines):
        line = lines[i]
        match = link_pattern.match(line)

        if match:
            link_text = match.group(1)
            section = match.group(2)
            entity_name = match.group(3)
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
                    "entity_name": entity_name,
                    "member": member,
                    "result_type": result_type,
                    "description": "\n".join(description_lines),
                }
            )

        i += 1

    return members


def extract_constructor_links(
    section_content: str,
) -> list[dict[str, str]]:
    """Extract constructor links from section content.

    Uses paragraph-based parsing per spec: only the **first line** of each paragraph
    is checked for the constructor link pattern. This prevents false positives from
    MCP links that appear in description text.

    Parses paragraphs where the first line starts with
    [CONSTRUCTOR](mcp://flutter/api/SECTION/ENTITY/CONSTRUCTOR).
    Constructors are followed by parameter lists, not arrows.

    Args:
        section_content: The markdown content of the Constructors section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - entity_name: The entity from the URI
        - member: The member name from the URI
    """
    members: list[dict[str, str]] = []
    paragraphs = split_into_paragraphs(section_content)

    # Pattern to match [text](mcp://flutter/api/section/entity/member)
    # For constructors, we don't require the arrow - just the MCP link at line start
    link_pattern = re.compile(
        rf"^\s*\[([^\]]+)\]\({MCP_URI_PREFIX}([^/]+)/([^/]+)/([^)]+)\)"
    )

    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        if not lines:
            continue

        # Per spec: only check the FIRST line of each paragraph
        first_line = lines[0]
        match = link_pattern.match(first_line)

        if match:
            link_text = match.group(1)
            section = match.group(2)
            entity_name = match.group(3)
            member = match.group(4)

            members.append(
                {
                    "link_text": link_text,
                    "section": section,
                    "entity_name": entity_name,
                    "member": member,
                }
            )

    return members


def extract_method_links(
    section_content: str,
) -> list[dict[str, str]]:
    """Extract method links from section content.

    Parses lines that start with [METHOD](mcp://flutter/api/SECTION/ENTITY/METHOD)
    for methods. Methods have parameters followed by an arrow and return type.
    The arrow may appear after the parameters, not immediately after the link.

    For inherited methods, captures the result_type and description.

    Only links with arrows are considered method definitions. Links without
    arrows are treated as inline references and ignored.

    Args:
        section_content: The markdown content of the Methods section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - entity_name: The entity from the URI
        - member: The member name from the URI
        - result_type: The result type (text after arrow), or empty string
        - description: Lines following the link until a blank line, or empty string
    """
    members: list[dict[str, str]] = []
    lines = section_content.split("\n")

    # Arrow patterns: Unicode rightwards arrow, left-right arrow, ASCII arrow variants
    # Supported: → (U+2192), ↔ (U+2194), -> , => , <-> , <=> , ➜ (U+279C), ➔ (U+2794)
    arrow_pattern = r"(?:\u2192|\u2194|\u279C|\u2794|<->|<=>|->|=>)"

    # Pattern to match [text](mcp://flutter/api/section/entity/member)
    # For methods, the link is at the start of the line, but the arrow comes after parameters
    link_pattern = re.compile(
        rf"^\s*\[([^\]]+)\]\({MCP_URI_PREFIX}([^/]+)/([^/]+)/([^)]+)\)"
    )

    i = 0
    while i < len(lines):
        line = lines[i]
        match = link_pattern.match(line)

        if match:
            # Check if this line has an arrow - only then is it a method definition
            arrow_search = re.search(arrow_pattern, line)
            if not arrow_search:
                # No arrow means this is just an inline reference, not a method definition
                i += 1
                continue

            link_text = match.group(1)
            section = match.group(2)
            entity_name = match.group(3)
            member = match.group(4)

            # Extract result type (after arrow on same line)
            result_type = ""
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
                    "entity_name": entity_name,
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

    Uses paragraph-based parsing per spec: only the **first line** of each paragraph
    is checked for the static method link pattern. This prevents false positives from
    MCP links that appear in description text (e.g., cross-references to other entities).

    Parses paragraphs where the first line starts with
    [METHOD](mcp://flutter/api/SECTION/ENTITY/METHOD)( for static methods.
    The opening parenthesis after the link is required as static methods always have
    parameter lists.

    Args:
        section_content: The markdown content of the Static Methods section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - entity_name: The entity from the URI
        - member: The member name from the URI
    """
    members: list[dict[str, str]] = []
    paragraphs = split_into_paragraphs(section_content)

    # Pattern to match [text](mcp://flutter/api/section/entity/member)(
    # The opening parenthesis after the link is required because static methods
    # always have parameter lists following the link.
    link_pattern = re.compile(
        rf"^\s*\[([^\]]+)\]\({MCP_URI_PREFIX}([^/]+)/([^/]+)/([^)]+)\)\("
    )

    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        if not lines:
            continue

        # Per spec: only check the FIRST line of each paragraph
        first_line = lines[0]
        match = link_pattern.match(first_line)

        if match:
            link_text = match.group(1)
            section = match.group(2)
            entity_name = match.group(3)
            member = match.group(4)

            members.append(
                {
                    "link_text": link_text,
                    "section": section,
                    "entity_name": entity_name,
                    "member": member,
                }
            )

    return members
