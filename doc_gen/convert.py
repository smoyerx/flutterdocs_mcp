"""Convert Flutter/Dart HTML documentation to markdown.

This script converts HTML documentation files to markdown format using the
html_to_markdown package, applies transformations to clean up the output, and
concatenates related files into single class documentation files.
"""

import argparse
import logging
import re
import sys
from pathlib import Path

from html_to_markdown import (
    ConversionOptions,
    ConversionOptionsHandle,
    convert_with_handle,
    create_options_handle,
)


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
    """Remove lines containing only whitespace and specific noise strings.

    Removes lines that contain only whitespace and exactly one occurrence
    of exactly one of the following strings:
    - "const"
    - "final"
    - "no setterinherited"
    - "finalinherited"
    - "inherited"
    - '[*link*](# "Copy link to clipboard")'

    Also removes lines containing analytics/tracking URLs.

    Args:
        content: The markdown content to transform.

    Returns:
        The content with noise lines removed.
    """
    noise_strings = [
        "const",
        "final",
        "no setterinherited",
        "finalinherited",
        "inherited",
        '[*link*](# "Copy link to clipboard")',
    ]

    lines = content.split("\n")
    result_lines = []

    for line in lines:
        stripped = line.strip()
        # Skip noise strings
        if stripped in noise_strings:
            continue
        # Skip analytics/tracking lines
        if "googletagmanager.com" in line:
            continue
        result_lines.append(line)

    return "\n".join(result_lines)


# --- Link Transformation Functions ---


def transform_class_links(content: str) -> str:
    """Transform class and mixin links to MCP URI format.

    Replaces links of the form:
    - [CLASS_NAME](SECTION/CLASS_NAME-class.html)
    - [MIXIN_NAME](SECTION/MIXIN_NAME-mixin.html)
    - [CONSTANT](SECTION/CONSTANT-constant.html)
    - [TYPE](SECTION/TYPE.html)
    with [NAME](mcp://flutter/api/SECTION/NAME).

    Args:
        content: The markdown content to transform.

    Returns:
        The content with class/mixin/constant links transformed.
    """
    # Match [ClassName](section/ClassName-class.html) - relative URI only
    pattern = r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-class\.html\)"
    content = re.sub(pattern, r"[\1](mcp://flutter/api/\2/\3)", content)

    # Match [MixinName](section/MixinName-mixin.html)
    pattern_mixin = r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-mixin\.html\)"
    content = re.sub(pattern_mixin, r"[\1](mcp://flutter/api/\2/\3)", content)

    # Match [ConstantName](section/ConstantName-constant.html)
    pattern_const = r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-constant\.html\)"
    content = re.sub(pattern_const, r"[\1](mcp://flutter/api/\2/\3)", content)

    # Match [ClassName](section/ClassName.html) - types and other references
    # Avoid matching 3-part member paths and external URLs
    pattern2 = r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)\.html\)"
    return re.sub(pattern2, r"[\1](mcp://flutter/api/\2/\3)", content)


def transform_member_links(content: str) -> str:
    """Transform member links to MCP URI format.

    Replaces links of the form:
    - [MEMBER](SECTION/CLASS/MEMBER.html) -> mcp://flutter/api/SECTION/CLASS/MEMBER
    - [CLASS.MEMBER](SECTION/CLASS/CLASS.MEMBER.html) -> mcp://flutter/api/SECTION/CLASS/CLASS.MEMBER
    - [MEMBER](SECTION/CLASS/MEMBER-constant.html) -> mcp://flutter/api/SECTION/CLASS/MEMBER

    Args:
        content: The markdown content to transform.

    Returns:
        The content with member links transformed.
    """
    # Match [Class.member](section/Class/Class.member.html) - named constructors/static methods
    pattern4 = r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)\.html\)"
    content = re.sub(pattern4, r"[\1](mcp://flutter/api/\2/\3/\4)", content)

    # Match [member](section/Class/member-constant.html) - class constants
    pattern_const = r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)-constant\.html\)"
    content = re.sub(pattern_const, r"[\1](mcp://flutter/api/\2/\3/\4)", content)

    # Match [member](section/Class/member.html) - relative URI only
    pattern3 = r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)\.html\)"
    return re.sub(pattern3, r"[\1](mcp://flutter/api/\2/\3/\4)", content)


def transform_image_links(content: str) -> str:
    """Transform image links to placeholder text.

    Replaces image links of the form ![Link Text](IMAGE_PATH)
    with [Note: Image Link Text omitted].

    Args:
        content: The markdown content to transform.

    Returns:
        The content with image links replaced by placeholder text.
    """
    # Match ![alt text](any/path/or/url)
    pattern = r"!\[([^\]]*)\]\([^)]+\)"
    return re.sub(pattern, r"[Note: Image \1 omitted]", content)


def transform_dartpad_links(content: str) -> str:
    """Transform DartPad links to placeholder text.

    Replaces links containing "dartpad.dev" in the URI
    with [Note: Interactive sample omitted].

    Args:
        content: The markdown content to transform.

    Returns:
        The content with DartPad links replaced by placeholder text.
    """
    # Match [text](url containing dartpad.dev)
    pattern = r"\[[^\]]+\]\([^)]*dartpad\.dev[^)]*\)"
    return re.sub(pattern, "[Note: Interactive sample omitted]", content)


def apply_transformations(content: str) -> str:
    """Apply all markdown transformations in the specified order.

    Cleanup transformations (applied first):
    1. Remove header content before first heading
    2. Remove footer content from Flutter index link
    3. Remove noise lines (const, final, inherited markers, etc.)

    Link transformations (applied second):
    1. Transform class links to MCP URI format
    2. Transform member links to MCP URI format
    3. Transform image links to placeholder text
    4. Transform DartPad links to placeholder text

    Args:
        content: The markdown content to transform.

    Returns:
        The fully transformed markdown content.
    """
    # Cleanup transformations
    content = remove_header(content)
    content = remove_footer(content)
    content = remove_noise_lines(content)

    # Link transformations
    content = transform_class_links(content)
    content = transform_member_links(content)
    content = transform_image_links(content)
    content = transform_dartpad_links(content)

    return content


# --- Section Parsing Functions ---


def extract_section_content(markdown: str, section_name: str) -> str | None:
    """Extract content from a specific section of markdown.

    Extracts all content between a section heading (## section_name) and the
    next heading of the same or higher level.

    Args:
        markdown: The markdown content to search.
        section_name: The name of the section to extract (without ##).

    Returns:
        The content of the section, or None if the section is not found.
    """
    lines = markdown.split("\n")
    in_section = False
    section_lines: list[str] = []

    for line in lines:
        stripped = line.lstrip()

        # Check if this is the target section heading
        if stripped.startswith("## ") and stripped[3:].strip() == section_name:
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
    followed by a type signature arrow (→), and captures the link text, section,
    class, member name, result type, and description.

    Args:
        section_content: The markdown content of a section.

    Returns:
        A list of dictionaries, each containing:
        - link_text: The text of the link
        - section: The section from the URI
        - class_name: The class from the URI
        - member: The member name from the URI
        - result_type: The result type (text after → on the same line), or empty string
        - description: Lines following the link until a blank line, or empty string
    """
    members: list[dict[str, str]] = []
    lines = section_content.split("\n")

    # Unicode rightwards arrow
    arrow = "\u2192"

    # Pattern to match [text](mcp://flutter/api/section/class/member) followed by → (type signature)
    # This distinguishes property definitions from inline references
    link_pattern = re.compile(
        r"^\s*\[([^\]]+)\]\(mcp://flutter/api/([^/]+)/([^/]+)/([^)]+)\)" + arrow
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

            # Extract result type (after → on same line)
            result_type = ""
            arrow_pos = line.find(arrow)
            if arrow_pos != -1:
                after_arrow = line[arrow_pos + 1 :].strip()
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

    return apply_transformations(md_text)


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
    """Process all documentation files for a class using the 6-step pipeline.

    Steps:
    1. Process the class file
    2. Process constructor files
    3. Process property files
    4. Process method files
    5. Process operator files
    6. Process code snippet files

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

    # Step 6: Process code snippet files
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

    print(
        f"Successfully processed {len(classes)} classes from section '{args.section}'"
    )


if __name__ == "__main__":
    main()
