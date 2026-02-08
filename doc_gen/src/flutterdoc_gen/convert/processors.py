"""Processing functions for entity documentation files.

This module contains functions for processing different types of entity
documentation members (constructors, properties, methods, operators,
static methods, and snippets).
"""

from html_to_markdown import ConversionOptionsHandle

from flutterdoc_gen.convert.conversion import (
    convert_dart_snippet,
    convert_html_to_markdown,
)
from flutterdoc_gen._shared.logging import log_processing_error
from flutterdoc_gen.convert.parsing import (
    extract_constructor_links,
    extract_member_definitions,
    extract_section_content,
    extract_static_method_links,
)
from flutterdoc_gen._shared.paths import PathBuilder, ensure_dir_exists
from flutterdoc_gen.convert.templates import (
    INHERITED_METHOD_TEMPLATE,
    INHERITED_OPERATOR_TEMPLATE,
    INHERITED_PROPERTY_TEMPLATE,
)


def process_constructors(
    entity_markdown: str,
    builder: PathBuilder,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process constructor files for an entity.

    Scans the Constructors section and converts each constructor HTML file.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        builder: PathBuilder instance with entity context.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(entity_markdown, "Constructors")
    if section_content is None:
        return

    members = extract_constructor_links(section_content)
    if not members:
        return

    constructors_dir = builder.get_constructors_dir()

    for member in members:
        # Constructors must be in the same section/entity
        if (
            member["section"] != builder.section
            or member["entity_name"] != builder.entity_name
        ):
            log_processing_error(
                f"Constructor link has unexpected URI: "
                f"mcp://flutter/api/{member['section']}/{member['entity_name']}/{member['member']}"
            )

        # Try regular member file first (e.g., Widget/Widget.html for default constructor)
        html_path = builder.get_input_member_file(member["member"])
        if not html_path.exists():
            # Try named constructor pattern (e.g., Text/Text.rich.html)
            html_path = builder.get_input_named_constructor_file(member["member"])
            if not html_path.exists():
                log_processing_error(f"Constructor HTML file not found: {html_path}")
                continue

        ensure_dir_exists(constructors_dir)
        markdown_content = convert_html_to_markdown(
            options_handle, html_path, apply_function_declaration_cleanup=True
        )
        output_file = builder.get_constructor_file(member["member"])
        output_file.write_text(markdown_content, encoding="utf-8")


def process_properties(
    entity_markdown: str,
    builder: PathBuilder,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process property files for an entity.

    Scans the Properties section and either converts native property HTML files
    or generates inherited property markdown files.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        builder: PathBuilder instance with entity context.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(entity_markdown, "Properties")
    if section_content is None:
        return

    members = extract_member_definitions(section_content)
    if not members:
        return

    native_dir = builder.get_properties_dir(inherited=False)
    inherited_dir = builder.get_properties_dir(inherited=True)

    for member in members:
        is_native = (
            member["section"] == builder.section
            and member["entity_name"] == builder.entity_name
        )

        if is_native:
            html_path = builder.get_input_member_file(member["member"])
            if not html_path.exists():
                log_processing_error(f"Property HTML file not found: {html_path}")

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(options_handle, html_path)
            output_file = builder.get_native_property_file(member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited property
            if not member["result_type"] or not member["description"]:
                log_processing_error(
                    f"Unable to capture result_type or description for inherited property "
                    f"{member['member']} from {member['section']}/{member['entity_name']}"
                )

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_PROPERTY_TEMPLATE.format(
                property=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_entity=member["entity_name"],
            )
            output_file = builder.get_inherited_property_file(member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")


def process_methods(
    entity_markdown: str,
    builder: PathBuilder,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process method files for an entity.

    Scans the Methods section and either converts native method HTML files
    or generates inherited method markdown files.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        builder: PathBuilder instance with entity context.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(entity_markdown, "Methods")
    if section_content is None:
        return

    members = extract_member_definitions(section_content)
    if not members:
        return

    native_dir = builder.get_methods_dir(inherited=False)
    inherited_dir = builder.get_methods_dir(inherited=True)

    for member in members:
        is_native = (
            member["section"] == builder.section
            and member["entity_name"] == builder.entity_name
        )

        if is_native:
            html_path = builder.get_input_member_file(member["member"])
            if not html_path.exists():
                log_processing_error(f"Method HTML file not found: {html_path}")

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(
                options_handle, html_path, apply_function_declaration_cleanup=True
            )
            output_file = builder.get_native_method_file(member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited method
            if not member["result_type"] or not member["description"]:
                log_processing_error(
                    f"Unable to capture result_type or description for inherited method "
                    f"{member['member']} from {member['section']}/{member['entity_name']}"
                )

            ensure_dir_exists(inherited_dir)
            markdown_content = INHERITED_METHOD_TEMPLATE.format(
                method=member["member"],
                result_type=member["result_type"],
                description=member["description"],
                some_section=member["section"],
                some_entity=member["entity_name"],
            )
            output_file = builder.get_inherited_method_file(member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")


def process_operators(
    entity_markdown: str,
    builder: PathBuilder,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process operator files for an entity.

    Scans the Operators section and either converts native operator HTML files
    or generates inherited operator markdown files.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        builder: PathBuilder instance with entity context.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(entity_markdown, "Operators")
    if section_content is None:
        return

    members = extract_member_definitions(section_content)
    if not members:
        return

    native_dir = builder.get_operators_dir(inherited=False)
    inherited_dir = builder.get_operators_dir(inherited=True)

    for member in members:
        is_native = (
            member["section"] == builder.section
            and member["entity_name"] == builder.entity_name
        )

        if is_native:
            html_path = builder.get_input_member_file(member["member"])
            if not html_path.exists():
                log_processing_error(f"Operator HTML file not found: {html_path}")

            ensure_dir_exists(native_dir)
            markdown_content = convert_html_to_markdown(
                options_handle, html_path, apply_function_declaration_cleanup=True
            )
            output_file = builder.get_native_operator_file(member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")
        else:
            # Inherited operator
            if not member["result_type"] or not member["description"]:
                log_processing_error(
                    f"Unable to capture result_type or description for inherited operator "
                    f"{member['member']} from {member['section']}/{member['entity_name']}"
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
            output_file = builder.get_inherited_operator_file(member["member"])
            output_file.write_text(markdown_content, encoding="utf-8")


def process_constants(
    entity_markdown: str,
    builder: PathBuilder,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process constant files for an entity (typically enums).

    Scans the Constants section and converts native constant HTML files.
    Constants have no inherited variant - they belong to the declaring entity only.
    Enum constants (like `values`) use -constant.html suffix in the input.

    Silently returns if the Constants section is not found.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        builder: PathBuilder instance with entity context.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(entity_markdown, "Constants")
    if section_content is None:
        # Silent handling - not all entities have Constants sections
        return

    members = extract_member_definitions(section_content)
    if not members:
        # Silent handling - no matches found
        return

    constants_dir = builder.get_constants_dir()

    for member in members:
        # Validate that constant belongs to current entity
        is_native = (
            member["section"] == builder.section
            and member["entity_name"] == builder.entity_name
        )

        if not is_native:
            # Constants should only reference the current entity
            log_processing_error(
                f"Constant link has unexpected URI: "
                f"{member['section']}/{member['entity_name']}/{member['member']} "
                f"(expected {builder.section}/{builder.entity_name})"
            )

        # Enum constants use -constant.html suffix
        html_path = builder.get_input_constant_file(member["member"])
        if not html_path.exists():
            log_processing_error(f"Constant HTML file not found: {html_path}")

        ensure_dir_exists(constants_dir)
        markdown_content = convert_html_to_markdown(options_handle, html_path)
        output_file = builder.get_constant_file(member["member"])
        output_file.write_text(markdown_content, encoding="utf-8")


def process_static_methods(
    entity_markdown: str,
    builder: PathBuilder,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process static method files for an entity.

    Scans the Static Methods section and converts native static method HTML files.
    Static methods have no inherited variant since static members belong to the
    declaring entity only.

    Args:
        entity_markdown: The converted markdown content of the root entity file.
        builder: PathBuilder instance with entity context.
        options_handle: The ConversionOptionsHandle instance for conversion.
    """
    section_content = extract_section_content(entity_markdown, "Static Methods")
    if section_content is None:
        # Silent handling per spec - no message if section not found
        return

    members = extract_static_method_links(section_content)
    if not members:
        # Silent handling per spec - no message if no matches found
        return

    statics_dir = builder.get_statics_dir()

    for member in members:
        # Validate that static method belongs to current entity
        is_native = (
            member["section"] == builder.section
            and member["entity_name"] == builder.entity_name
        )

        if not is_native:
            # Static methods should only reference the current entity
            log_processing_error(
                f"Static method link has unexpected URI scheme: "
                f"{member['section']}/{member['entity_name']}/{member['member']} "
                f"(expected {builder.section}/{builder.entity_name})"
            )

        html_path = builder.get_input_member_file(member["member"])
        if not html_path.exists():
            log_processing_error(f"Static method HTML file not found: {html_path}")

        ensure_dir_exists(statics_dir)
        markdown_content = convert_html_to_markdown(
            options_handle, html_path, apply_function_declaration_cleanup=True
        )
        output_file = builder.get_static_file(member["member"])
        output_file.write_text(markdown_content, encoding="utf-8")


def process_snippets(builder: PathBuilder) -> None:
    """Process code snippet files for an entity.

    Converts Dart snippet files to markdown and saves them.

    Args:
        builder: PathBuilder instance with entity context.
    """
    snippets_dir = builder.get_input_snippets_dir()
    snippet_pattern = f"{builder.section}.{builder.entity_name}.*.dart"
    snippet_files = sorted(snippets_dir.glob(snippet_pattern))
    assert builder.entity_name is not None  # Type hint for mypy / Pylance

    if not snippet_files:
        return

    output_snippets_dir = builder.get_snippets_dir()
    ensure_dir_exists(output_snippets_dir)

    for snippet_file in snippet_files:
        # Extract SHORT_NAME: remove {section}.{entity_name}. prefix and .dart suffix
        prefix = f"{builder.section}.{builder.entity_name}."
        short_name = snippet_file.name[len(prefix) : -len(".dart")]

        markdown_content = convert_dart_snippet(
            snippet_file, builder.entity_name, builder.section
        )
        output_file = builder.get_snippet_file(short_name)
        output_file.write_text(markdown_content, encoding="utf-8")
