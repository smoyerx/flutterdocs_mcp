"""Processing functions for entity documentation files.

This module contains functions for processing different types of entity
documentation members (constructors, properties, methods, operators,
static methods, and snippets).
"""

import logging
from pathlib import Path

from html_to_markdown import ConversionOptionsHandle

from flutterdoc_gen.convert.conversion import (
    convert_dart_snippet,
    convert_html_to_markdown,
)
from flutterdoc_gen.convert.errors import log_processing_error
from flutterdoc_gen.convert.parsing import (
    extract_constructor_links,
    extract_member_definitions,
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
    entity_markdown: str,
    current_section: str,
    current_entity: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
    source_file: Path,
) -> None:
    """Process constructor files for an entity.

    Scans the Constructors section and converts each constructor HTML file.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        current_section: The current documentation section name.
        current_entity: The current entity name.
        doc_dir: The root documentation directory.
        output_dir: The entity output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
        source_file: Path to the source HTML file being processed.
    """
    section_content = extract_section_content(entity_markdown, "Constructors")
    if section_content is None:
        logging.info(f"No Constructors section found in {current_entity}")
        return

    members = extract_constructor_links(section_content)
    if not members:
        logging.info(f"No constructor links found in {current_entity}")
        return

    constructors_dir = get_constructors_dir(output_dir)

    for member in members:
        # Constructors must be in the same section/entity
        if (
            member["section"] != current_section
            or member["entity_name"] != current_entity
        ):
            log_processing_error(
                f"Constructor link has unexpected URI: "
                f"mcp://flutter/api/{member['section']}/{member['entity_name']}/{member['member']}",
                source_file,
            )

        html_path = get_input_member_file(
            doc_dir, current_section, current_entity, member["member"]
        )
        if not html_path.exists():
            log_processing_error(
                f"Constructor HTML file not found: {html_path}", source_file
            )

        ensure_dir_exists(constructors_dir)
        markdown_content = convert_html_to_markdown(
            options_handle, html_path, apply_function_declaration_cleanup=True
        )
        output_file = get_native_member_file(constructors_dir, member["member"])
        output_file.write_text(markdown_content, encoding="utf-8")


def process_properties(
    entity_markdown: str,
    current_section: str,
    current_entity: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
    source_file: Path,
) -> None:
    """Process property files for an entity.

    Scans the Properties section and either converts native property HTML files
    or generates inherited property markdown files.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        current_section: The current documentation section name.
        current_entity: The current entity name.
        doc_dir: The root documentation directory.
        output_dir: The entity output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
        source_file: Path to the source HTML file being processed.
    """
    section_content = extract_section_content(entity_markdown, "Properties")
    if section_content is None:
        logging.info(f"No Properties section found in {current_entity}")
        return

    members = extract_member_definitions(section_content)
    if not members:
        logging.info(f"No property links found in {current_entity}")
        return

    native_dir = get_properties_native_dir(output_dir)
    inherited_dir = get_properties_inherited_dir(output_dir)

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["entity_name"] == current_entity
        )

        if is_native:
            html_path = get_input_member_file(
                doc_dir, current_section, current_entity, member["member"]
            )
            if not html_path.exists():
                log_processing_error(
                    f"Property HTML file not found: {html_path}", source_file
                )

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = get_native_member_file(native_dir, member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited property
            if not member["result_type"] or not member["description"]:
                log_processing_error(
                    f"Unable to capture result_type or description for inherited property "
                    f"{member['member']} from {member['section']}/{member['entity_name']}",
                    source_file,
                )

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_PROPERTY_TEMPLATE.format(
                property=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_entity=member["entity_name"],
            )
            output_file = get_inherited_member_file(
                inherited_dir,
                member["section"],
                member["entity_name"],
                member["member"],
            )
            output_file.write_text(markdown_content, encoding="utf-8")


def process_methods(
    entity_markdown: str,
    current_section: str,
    current_entity: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
    source_file: Path,
) -> None:
    """Process method files for an entity.

    Scans the Methods section and either converts native method HTML files
    or generates inherited method markdown files.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        current_section: The current documentation section name.
        current_entity: The current entity name.
        doc_dir: The root documentation directory.
        output_dir: The entity output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
        source_file: Path to the source HTML file being processed.
    """
    section_content = extract_section_content(entity_markdown, "Methods")
    if section_content is None:
        logging.info(f"No Methods section found in {current_entity}")
        return

    members = extract_member_definitions(section_content)
    if not members:
        logging.info(f"No method links found in {current_entity}")
        return

    native_dir = get_methods_native_dir(output_dir)
    inherited_dir = get_methods_inherited_dir(output_dir)

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["entity_name"] == current_entity
        )

        if is_native:
            html_path = get_input_member_file(
                doc_dir, current_section, current_entity, member["member"]
            )
            if not html_path.exists():
                log_processing_error(
                    f"Method HTML file not found: {html_path}", source_file
                )

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(
                options_handle, html_path, apply_function_declaration_cleanup=True
            )
            output_file = get_native_member_file(native_dir, member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited method
            if not member["result_type"] or not member["description"]:
                log_processing_error(
                    f"Unable to capture result_type or description for inherited method "
                    f"{member['member']} from {member['section']}/{member['entity_name']}",
                    source_file,
                )

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_METHOD_TEMPLATE.format(
                method=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_entity=member["entity_name"],
            )
            output_file = get_inherited_member_file(
                inherited_dir,
                member["section"],
                member["entity_name"],
                member["member"],
            )
            output_file.write_text(markdown_content, encoding="utf-8")


def process_operators(
    entity_markdown: str,
    current_section: str,
    current_entity: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
    source_file: Path,
) -> None:
    """Process operator files for an entity.

    Scans the Operators section and either converts native operator HTML files
    or generates inherited operator markdown files.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        current_section: The current documentation section name.
        current_entity: The current entity name.
        doc_dir: The root documentation directory.
        output_dir: The entity output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
        source_file: Path to the source HTML file being processed.
    """
    section_content = extract_section_content(entity_markdown, "Operators")
    if section_content is None:
        logging.info(f"No Operators section found in {current_entity}")
        return

    members = extract_member_definitions(section_content)
    if not members:
        logging.info(f"No operator links found in {current_entity}")
        return

    native_dir = get_operators_native_dir(output_dir)
    inherited_dir = get_operators_inherited_dir(output_dir)

    for member in members:
        is_native = (
            member["section"] == current_section
            and member["entity_name"] == current_entity
        )

        if is_native:
            html_path = get_input_member_file(
                doc_dir, current_section, current_entity, member["member"]
            )
            if not html_path.exists():
                log_processing_error(
                    f"Operator HTML file not found: {html_path}", source_file
                )

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(
                options_handle, html_path, apply_function_declaration_cleanup=True
            )
            output_file = get_native_member_file(native_dir, member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited operator
            if not member["result_type"] or not member["description"]:
                log_processing_error(
                    f"Unable to capture result_type or description for inherited operator "
                    f"{member['member']} from {member['section']}/{member['entity_name']}",
                    source_file,
                )

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_OPERATOR_TEMPLATE.format(
                operator_symbol=member["link_text"],
                operator=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_entity=member["entity_name"],
            )
            output_file = get_inherited_member_file(
                inherited_dir,
                member["section"],
                member["entity_name"],
                member["member"],
            )
            output_file.write_text(markdown_content, encoding="utf-8")


def process_static_methods(
    entity_markdown: str,
    current_section: str,
    current_entity: str,
    doc_dir: Path,
    output_dir: Path,
    options_handle: ConversionOptionsHandle,
    source_file: Path,
) -> None:
    """Process static method files for an entity.

    Scans the Static Methods section and converts native static method HTML files.
    Static methods have no inherited variant since static members belong to the
    declaring entity only.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        current_section: The current documentation section name.
        current_entity: The current entity name.
        doc_dir: The root documentation directory.
        output_dir: The entity output directory.
        options_handle: The ConversionOptionsHandle instance for conversion.
        source_file: Path to the source HTML file being processed.
    """
    section_content = extract_section_content(entity_markdown, "Static Methods")
    if section_content is None:
        # Silent handling per spec - no message if section not found
        return

    members = extract_static_method_links(section_content)
    if not members:
        # Silent handling per spec - no message if no matches found
        return

    statics_dir = get_statics_dir(output_dir)

    for member in members:
        # Validate that static method belongs to current entity
        is_native = (
            member["section"] == current_section
            and member["entity_name"] == current_entity
        )

        if not is_native:
            # Static methods should only reference the current entity
            log_processing_error(
                f"Static method link has unexpected URI scheme: "
                f"{member['section']}/{member['entity_name']}/{member['member']} "
                f"(expected {current_section}/{current_entity})",
                source_file,
            )

        html_path = get_input_member_file(
            doc_dir, current_section, current_entity, member["member"]
        )
        if not html_path.exists():
            log_processing_error(
                f"Static method HTML file not found: {html_path}", source_file
            )

        ensure_dir_exists(statics_dir)
        markdown_content = convert_html_to_markdown(
            options_handle, html_path, apply_function_declaration_cleanup=True
        )
        output_file = get_native_member_file(statics_dir, member["member"])
        output_file.write_text(markdown_content, encoding="utf-8")


def process_snippets(
    doc_dir: Path,
    output_dir: Path,
    section: str,
    entity_name: str,
) -> None:
    """Process code snippet files for an entity.

    Converts Dart snippet files to markdown and saves them.

    Args:
        doc_dir: The root documentation directory.
        output_dir: The entity output directory.
        section: The documentation section name.
        entity_name: The entity name.
    """
    snippets_dir = get_input_snippets_dir(doc_dir)
    snippet_pattern = f"{section}.{entity_name}.*.dart"
    snippet_files = sorted(snippets_dir.glob(snippet_pattern))

    if not snippet_files:
        return

    output_snippets_dir = get_snippets_output_dir(output_dir)
    ensure_dir_exists(output_snippets_dir)

    for snippet_file in snippet_files:
        # Extract SHORT_NAME: remove {section}.{entity_name}. prefix and .dart suffix
        prefix = f"{section}.{entity_name}."
        short_name = snippet_file.name[len(prefix) : -len(".dart")]

        markdown_content = convert_dart_snippet(snippet_file, entity_name, section)
        output_file = get_snippet_output_file(output_snippets_dir, short_name)
        output_file.write_text(markdown_content, encoding="utf-8")
