"""Processing functions for class documentation files.

This module contains functions for processing different types of class
documentation members (constructors, properties, methods, operators,
static methods, and snippets).
"""

import logging
import sys
from pathlib import Path

from html_to_markdown import ConversionOptionsHandle

from flutterdoc_gen.convert.conversion import (
    convert_dart_snippet,
    convert_html_to_markdown,
)
from flutterdoc_gen.convert.parsing import (
    extract_constructor_links,
    extract_member_links,
    extract_method_links,
    extract_section_content,
    extract_static_method_links,
)
from flutterdoc_gen.convert.paths import (
    ensure_dir_exists,
    get_constructors_dir,
    get_inherited_member_file,
    get_input_member_file,
    get_input_snippets_dir,
    get_methods_inherited_dir,
    get_methods_native_dir,
    get_native_member_file,
    get_operators_inherited_dir,
    get_operators_native_dir,
    get_properties_inherited_dir,
    get_properties_native_dir,
    get_snippet_output_file,
    get_snippets_output_dir,
    get_statics_dir,
)
from flutterdoc_gen.convert.templates import (
    INHERITED_METHOD_TEMPLATE,
    INHERITED_OPERATOR_TEMPLATE,
    INHERITED_PROPERTY_TEMPLATE,
)


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

    members = extract_constructor_links(section_content)
    if not members:
        logging.info(f"No constructor links found in {current_class}")
        return

    constructors_dir = get_constructors_dir(output_dir)

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

        html_path = get_input_member_file(
            doc_dir, current_section, current_class, member["member"]
        )
        if not html_path.exists():
            logging.error(f"Constructor HTML file not found: {html_path}")
            sys.exit(1)

        ensure_dir_exists(constructors_dir)
        markdown_content = convert_html_to_markdown(options_handle, html_path)
        output_file = get_native_member_file(constructors_dir, member["member"])
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

    native_dir = get_properties_native_dir(output_dir)
    inherited_dir = get_properties_inherited_dir(output_dir)

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["class_name"] == current_class
        )

        if is_native:
            html_path = get_input_member_file(
                doc_dir, current_section, current_class, member["member"]
            )
            if not html_path.exists():
                logging.error(f"Property HTML file not found: {html_path}")
                sys.exit(1)

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = get_native_member_file(native_dir, member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited property
            if not member["result_type"] or not member["description"]:
                logging.error(
                    f"Unable to capture result_type or description for inherited property "
                    f"{member['member']} from {member['section']}/{member['class_name']}"
                )
                sys.exit(1)

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_PROPERTY_TEMPLATE.format(
                property=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_class=member["class_name"],
            )
            output_file = get_inherited_member_file(
                inherited_dir,
                member["section"],
                member["class_name"],
                member["member"],
            )
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

    members = extract_method_links(section_content)
    if not members:
        logging.info(f"No method links found in {current_class}")
        return

    native_dir = get_methods_native_dir(output_dir)
    inherited_dir = get_methods_inherited_dir(output_dir)

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["class_name"] == current_class
        )

        if is_native:
            html_path = get_input_member_file(
                doc_dir, current_section, current_class, member["member"]
            )
            if not html_path.exists():
                logging.error(f"Method HTML file not found: {html_path}")
                sys.exit(1)

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = get_native_member_file(native_dir, member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited method
            if not member["result_type"] or not member["description"]:
                logging.error(
                    f"Unable to capture result_type or description for inherited method "
                    f"{member['member']} from {member['section']}/{member['class_name']}"
                )
                sys.exit(1)

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_METHOD_TEMPLATE.format(
                method=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_class=member["class_name"],
            )
            output_file = get_inherited_member_file(
                inherited_dir,
                member["section"],
                member["class_name"],
                member["member"],
            )
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

    native_dir = get_operators_native_dir(output_dir)
    inherited_dir = get_operators_inherited_dir(output_dir)

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["class_name"] == current_class
        )

        if is_native:
            html_path = get_input_member_file(
                doc_dir, current_section, current_class, member["member"]
            )
            if not html_path.exists():
                logging.error(f"Operator HTML file not found: {html_path}")
                sys.exit(1)

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = get_native_member_file(native_dir, member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited operator
            if not member["result_type"] or not member["description"]:
                logging.error(
                    f"Unable to capture result_type or description for inherited operator "
                    f"{member['member']} from {member['section']}/{member['class_name']}"
                )
                sys.exit(1)

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_OPERATOR_TEMPLATE.format(
                operator_symbol=member["link_text"],
                operator=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_class=member["class_name"],
            )
            output_file = get_inherited_member_file(
                inherited_dir,
                member["section"],
                member["class_name"],
                member["member"],
            )
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

    statics_dir = get_statics_dir(output_dir)

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

        html_path = get_input_member_file(
            doc_dir, current_section, current_class, member["member"]
        )
        if not html_path.exists():
            logging.error(f"Static method HTML file not found: {html_path}")
            sys.exit(1)

        ensure_dir_exists(statics_dir)
        markdown_content = convert_html_to_markdown(options_handle, html_path)
        output_file = get_native_member_file(statics_dir, member["member"])
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
    snippets_dir = get_input_snippets_dir(doc_dir)
    snippet_pattern = f"{section}.{class_name}.*.dart"
    snippet_files = sorted(snippets_dir.glob(snippet_pattern))

    if not snippet_files:
        return

    output_snippets_dir = get_snippets_output_dir(output_dir)
    ensure_dir_exists(output_snippets_dir)

    for snippet_file in snippet_files:
        # Extract SHORT_NAME: remove {section}.{class_name}. prefix and .dart suffix
        prefix = f"{section}.{class_name}."
        short_name = snippet_file.name[len(prefix) : -len(".dart")]

        markdown_content = convert_dart_snippet(snippet_file, class_name, section)
        output_file = get_snippet_output_file(output_snippets_dir, short_name)
        output_file.write_text(markdown_content, encoding="utf-8")
