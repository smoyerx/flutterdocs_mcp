"""Processing functions for root documentation files.

This module contains functions for processing different types of root documentation
files (classes, mixins, constants, libraries, enums, extensions, extension types,
functions, and typedefs).

Root documentation files are the main entry point files for each documented entity,
as opposed to member documentation files (constructors, methods, properties, etc.)
which are processed by the functions in the processors module.
"""

import re
from pathlib import Path

from html_to_markdown import ConversionOptionsHandle

from flutterdocs._shared.constants import CategoryType
from flutterdocs.convert.conversion import convert_html_to_markdown
from flutterdocs._shared.logging import get_progress_logger
from flutterdocs._shared.paths import PathBuilder, ensure_dir_exists
from flutterdocs.convert.processors import (
    process_constants,
    process_constructors,
    process_methods,
    process_operators,
    process_properties,
    process_snippets,
    process_static_methods,
)


def _process_all_sections(
    entity_markdown: str,
    builder: PathBuilder,
    options_handle: ConversionOptionsHandle,
) -> None:
    """Process all possible sections for a given root entity documentation file.

    Scans each possible section (constructors, properties, methods, etc.) and converts
    member documentation files referenced in those sections as well as any code snippets.
    Missing or empty sections are skipped without error.

    Used for all class-like entities (classes, mixins, enums, etc.) where all sections are
    applicable with few exceptions (e.g., mixins do not have constructors).

    Args:
        entity_markdown: The markdown content of the root entity documentation file.
        builder: The PathBuilder instance for constructing paths.
        options_handle: The ConversionOptionsHandle instance to use for conversion.
    """

    # Process constructor files (if applicable)
    process_constructors(entity_markdown, builder, options_handle)

    # Process property files
    process_properties(entity_markdown, builder, options_handle)

    # Process method files
    process_methods(entity_markdown, builder, options_handle)

    # Process operator files
    process_operators(entity_markdown, builder, options_handle)

    # Process static method files
    process_static_methods(entity_markdown, builder, options_handle)

    # Process constant files (if applicable, e.g., for enums)
    process_constants(entity_markdown, builder, options_handle)

    # Process code snippet files
    process_snippets(builder)


def process_class(
    options_handle: ConversionOptionsHandle,
    class_name: str,
    class_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process class documentation files.

    Process the root class documentation file and all associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        class_name: The name of the class being processed.
        class_file: Path to the main class HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=class_name,
        entity_type=CategoryType.CLASS,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create class output directory
    class_output_dir = builder.get_entity_dir()
    ensure_dir_exists(class_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root class file
    progress_logger.info(f"  Processing class file: {class_file}")
    class_markdown = convert_html_to_markdown(options_handle, class_file)
    class_output_file = builder.get_entity_file()
    class_output_file.write_text(class_markdown, encoding="utf-8")

    # Process all sections for the class documentation file
    _process_all_sections(class_markdown, builder, options_handle)


def process_mixin(
    options_handle: ConversionOptionsHandle,
    mixin_name: str,
    mixin_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process mixin documentation files.

    Process the root mixin documentation file and all associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        mixin_name: The name of the mixin being processed.
        mixin_file: Path to the main mixin HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=mixin_name,
        entity_type=CategoryType.MIXIN,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create mixin output directory
    mixin_output_dir = builder.get_entity_dir()
    ensure_dir_exists(mixin_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root mixin file
    progress_logger.info(f"  Processing mixin file: {mixin_file}")
    mixin_markdown = convert_html_to_markdown(options_handle, mixin_file)
    mixin_output_file = builder.get_entity_file()
    mixin_output_file.write_text(mixin_markdown, encoding="utf-8")

    # Process all sections for the mixin documentation file
    _process_all_sections(mixin_markdown, builder, options_handle)


def process_constant(
    options_handle: ConversionOptionsHandle,
    constant_name: str,
    constant_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process constant documentation files.

    Process the root constant documentation file; does not have associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        constant_name: The name of the constant being processed.
        constant_file: Path to the main constant HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=constant_name,
        entity_type=CategoryType.CONSTANT,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create constant output directory
    constant_output_dir = builder.get_entity_dir()
    ensure_dir_exists(constant_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root constant file
    progress_logger.info(f"  Processing constant file: {constant_file}")
    constant_markdown = convert_html_to_markdown(options_handle, constant_file)
    constant_output_file = builder.get_entity_file()
    constant_output_file.write_text(constant_markdown, encoding="utf-8")


def process_extension_type(
    options_handle: ConversionOptionsHandle,
    extension_type_name: str,
    extension_type_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process extension type documentation files.

    Process the root extension type documentation file and all associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        extension_type_name: The name of the extension type being processed.
        extension_type_file: Path to the main extension type HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=extension_type_name,
        entity_type=CategoryType.EXTENSION_TYPE,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create extension type output directory
    extension_type_output_dir = builder.get_entity_dir()
    ensure_dir_exists(extension_type_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root extension type file
    progress_logger.info(f"  Processing extension type file: {extension_type_file}")
    extension_type_markdown = convert_html_to_markdown(
        options_handle, extension_type_file, apply_function_declaration_cleanup=True
    )
    extension_type_output_file = builder.get_entity_file()
    extension_type_output_file.write_text(extension_type_markdown, encoding="utf-8")

    # Process all sections for the extension type documentation file
    _process_all_sections(extension_type_markdown, builder, options_handle)


def process_enum(
    options_handle: ConversionOptionsHandle,
    enum_name: str,
    enum_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process enum documentation files.

        Process the root enum documentation file and all associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        enum_name: The name of the enum being processed.
        enum_file: Path to the main enum HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=enum_name,
        entity_type=CategoryType.ENUM,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create enum output directory
    enum_output_dir = builder.get_entity_dir()
    ensure_dir_exists(enum_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root enum file
    progress_logger.info(f"  Processing enum file: {enum_file}")
    enum_markdown = convert_html_to_markdown(options_handle, enum_file)
    enum_output_file = builder.get_entity_file()
    enum_output_file.write_text(enum_markdown, encoding="utf-8")

    # Process all sections for the enum documentation file
    _process_all_sections(enum_markdown, builder, options_handle)


def process_extension(
    options_handle: ConversionOptionsHandle,
    extension_name: str,
    extension_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process extension documentation files.

    Process the root extension documentation file and all associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        extension_name: The name of the extension being processed.
        extension_file: Path to the main extension HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=extension_name,
        entity_type=CategoryType.EXTENSION,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create extension output directory
    extension_output_dir = builder.get_entity_dir()
    ensure_dir_exists(extension_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root extension file
    progress_logger.info(f"  Processing extension file: {extension_file}")
    extension_markdown = convert_html_to_markdown(options_handle, extension_file)
    extension_output_file = builder.get_entity_file()
    extension_output_file.write_text(extension_markdown, encoding="utf-8")

    # Process all sections for the extension documentation file
    _process_all_sections(extension_markdown, builder, options_handle)


def process_function(
    options_handle: ConversionOptionsHandle,
    function_name: str,
    function_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process function documentation files.

    Process the root function documentation file; does not have associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        function_name: The name of the function being processed.
        function_file: Path to the main function HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=function_name,
        entity_type=CategoryType.FUNCTION,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create function output directory
    function_output_dir = builder.get_entity_dir()
    ensure_dir_exists(function_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root function file
    progress_logger.info(f"  Processing function file: {function_file}")
    function_markdown = convert_html_to_markdown(
        options_handle, function_file, apply_function_declaration_cleanup=True
    )
    function_output_file = builder.get_entity_file()
    function_output_file.write_text(function_markdown, encoding="utf-8")


def process_typedef(
    options_handle: ConversionOptionsHandle,
    typedef_name: str,
    typedef_file: Path,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process typedef documentation files.

    Process the root typedef documentation file; does not have associated member documentation files.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        typedef_name: The name of the typedef being processed.
        typedef_file: Path to the main typedef HTML file.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """
    pass
    # Create PathBuilder with entity context
    builder = PathBuilder(
        section=section,
        entity_name=typedef_name,
        entity_type=CategoryType.TYPEDEF,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Create typedef output directory
    typedef_output_dir = builder.get_entity_dir()
    ensure_dir_exists(typedef_output_dir)

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root typedef file
    progress_logger.info(f"  Processing typedef file: {typedef_file}")
    typedef_markdown = convert_html_to_markdown(options_handle, typedef_file)
    typedef_output_file = builder.get_entity_file()
    typedef_output_file.write_text(typedef_markdown, encoding="utf-8")


def process_library(
    options_handle: ConversionOptionsHandle,
    section: str,
    doc_dir: Path,
    root_output_dir: Path,
) -> None:
    """Process library documentation files.

    Process the root library documentation file; does not have associated member
    documentation files. The library file is stored as a flat section-level file
    at api/{section}/{section}.md.

    Args:
        options_handle: The ConversionOptionsHandle instance to use for conversion.
        section: The documentation section name.
        doc_dir: The root documentation directory.
        root_output_dir: The root output directory.
    """

    # Create PathBuilder with section context only (no entity context)
    builder = PathBuilder(
        section=section,
        doc_dir=doc_dir,
        output_dir=root_output_dir,
    )

    # Ensure section output directory exists
    ensure_dir_exists(builder.get_api_section_dir())

    # Get logger for progress messages
    progress_logger = get_progress_logger()

    # Process the root library file
    library_input_file = builder.get_input_library_file()
    progress_logger.info(f"  Processing library file: {library_input_file}")
    library_markdown = convert_html_to_markdown(options_handle, library_input_file)
    library_output_file = builder.get_library_file()
    library_output_file.write_text(library_markdown, encoding="utf-8")

    # Extract display name from first header line: "# <name> library"
    first_line = library_markdown.split("\n", 1)[0]
    match = re.match(r"#\s+(.+?)\s+library\s*$", first_line)
    if match:
        display_name_file = builder.get_library_display_name_file()
        display_name_file.write_text(match.group(1), encoding="utf-8")
