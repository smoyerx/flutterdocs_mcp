"""Conversion functions for HTML to markdown.

This module contains functions for converting HTML files to markdown
and processing Dart code snippets.
"""

from pathlib import Path

from html_to_markdown import ConversionOptionsHandle, convert_with_handle

from flutterdoc_gen.convert.transformations import (
    apply_transformations,
    cleanup_function_declaration,
)


def convert_html_to_markdown(
    options_handle: ConversionOptionsHandle,
    html_path: Path,
    apply_function_declaration_cleanup: bool = False,
) -> str:
    """Convert an HTML file to markdown and apply transformations.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        html_path: Path to the HTML file to convert.
        apply_function_declaration_cleanup: If True, apply function declaration
            cleanup transformation after generic transformations. Use for
            constructor, native method, native operator, and static method files.

    Returns:
        The transformed markdown content.

    Raises:
        FileNotFoundError: If the HTML file does not exist.
        RuntimeError: If the HTML file cannot be read or converted.
    """
    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    try:
        md_text = convert_with_handle(
            html_path.read_text(encoding="utf-8"), options_handle
        )
    except Exception as e:
        raise RuntimeError(f"Error reading or converting HTML file {html_path}: {e}")

    content = apply_transformations(md_text, source_context=str(html_path))

    if apply_function_declaration_cleanup:
        content = cleanup_function_declaration(content, source_context=str(html_path))

    return content


def convert_dart_snippet(dart_path: Path, entity_name: str, section: str) -> str:
    """Convert a Dart snippet file to markdown.

    Wraps the Dart code in a markdown code block with a header.

    Args:
        dart_path: Path to the Dart file to convert.
        entity_name: The name of the entity the snippet belongs to.
        section: The documentation section name.

    Returns:
        The Dart code wrapped in markdown format.

    Raises:
        FileNotFoundError: If the Dart file does not exist.
    """
    if not dart_path.exists():
        raise FileNotFoundError(f"Dart file not found: {dart_path}")

    content = dart_path.read_text(encoding="utf-8")
    return f"# Code Snippet for {entity_name} in {section}\n\n```dart\n{content}\n```"
