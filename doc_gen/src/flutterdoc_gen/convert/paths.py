"""Path construction utilities for the convert tool.

This module centralizes all path construction logic for input and output files,
providing a consistent interface for building file paths throughout the
conversion process.
"""

from pathlib import Path
from flutterdoc_gen.convert.constants import CategoryType


# --- Output Directory Builders ---


def get_api_root_dir(output_dir: Path) -> Path:
    """Get the API root output directory path.

    Args:
        output_dir: The root output directory.

    Returns:
        Path to the api/ directory.
    """
    return output_dir / "api"


def get_api_section_dir(output_dir: Path, section: str) -> Path:
    """Get the API section output directory path.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.

    Returns:
        Path to the api/{section} directory.
    """
    return output_dir / "api" / section


def get_entity_dir(
    output_dir: Path,
    section: str,
    entity_name: str,
    entity_type: CategoryType,
) -> Path:
    """Get the entity output directory path.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        entity_name: The entity name.
        entity_type: The category type of the entity.

    Returns:
        Path to the api/{section}/{entity_type}/{entity_name} directory.
    """
    # Not using str(entity_type) to keep output directory structure indepdendent of enum value
    match entity_type:
        case CategoryType.CLASS:
            subdir = "classes"
        case CategoryType.MIXIN:
            subdir = "mixins"
        case CategoryType.ENUM:
            subdir = "enums"
        case CategoryType.CONSTANT:
            subdir = "constants"
        case CategoryType.LIBRARY:
            subdir = "libraries"
        case CategoryType.EXTENSION_TYPE:
            subdir = "extension_types"
        case CategoryType.EXTENSION:
            subdir = "extensions"
        case CategoryType.FUNCTION:
            subdir = "functions"
        case CategoryType.TYPEDEF:
            subdir = "typedefs"
        case _:
            subdir = "entities"
    return get_api_section_dir(output_dir, section) / subdir / entity_name


def get_entity_file(
    output_dir: Path, section: str, entity_name: str, entity_type: CategoryType
) -> Path:
    """Get the main entity markdown file path.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        entity_name: The entity name.
        entity_type: The category type of the entity.

    Returns:
        Path to the api/{section}/{entity_name}/{entity_name}.md file.
    """
    return (
        get_entity_dir(output_dir, section, entity_name, entity_type)
        / f"{entity_name}.md"
    )


# --- Member Directory Builders ---


def get_constructors_dir(entity_dir: Path) -> Path:
    """Get the constructors subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the constructors subdirectory.
    """
    return entity_dir / "constructors"


def get_properties_native_dir(entity_dir: Path) -> Path:
    """Get the native properties subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the properties/native subdirectory.
    """
    return entity_dir / "properties" / "native"


def get_properties_inherited_dir(entity_dir: Path) -> Path:
    """Get the inherited properties subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the properties/inherited subdirectory.
    """
    return entity_dir / "properties" / "inherited"


def get_methods_native_dir(entity_dir: Path) -> Path:
    """Get the native methods subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the methods/native subdirectory.
    """
    return entity_dir / "methods" / "native"


def get_methods_inherited_dir(entity_dir: Path) -> Path:
    """Get the inherited methods subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the methods/inherited subdirectory.
    """
    return entity_dir / "methods" / "inherited"


def get_operators_native_dir(entity_dir: Path) -> Path:
    """Get the native operators subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the operators/native subdirectory.
    """
    return entity_dir / "operators" / "native"


def get_operators_inherited_dir(entity_dir: Path) -> Path:
    """Get the inherited operators subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the operators/inherited subdirectory.
    """
    return entity_dir / "operators" / "inherited"


def get_statics_dir(entity_dir: Path) -> Path:
    """Get the static methods subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the statics subdirectory.
    """
    return entity_dir / "statics"


def get_snippets_output_dir(entity_dir: Path) -> Path:
    """Get the snippets subdirectory path.

    Args:
        entity_dir: The entity output directory.

    Returns:
        Path to the snippets subdirectory.
    """
    return entity_dir / "snippets"


# --- Output File Builders ---


def get_native_member_file(member_dir: Path, member_name: str) -> Path:
    """Get the path for a native member markdown file.

    Args:
        member_dir: The member type directory (e.g., constructors, properties/native).
        member_name: The member name.

    Returns:
        Path to the {member_name}.md file.
    """
    return member_dir / f"{member_name}.md"


def get_inherited_member_file(
    inherited_dir: Path, source_section: str, source_entity: str, member_name: str
) -> Path:
    """Get the path for an inherited member markdown file.

    Args:
        inherited_dir: The inherited member directory.
        source_section: The section where the member is defined.
        source_entity: The entity where the member is defined.
        member_name: The member name.

    Returns:
        Path to the {section}___{entity}___{member}.md file.
    """
    filename = f"{source_section}___{source_entity}___{member_name}.md"
    return inherited_dir / filename


def get_snippet_output_file(snippets_dir: Path, short_name: str) -> Path:
    """Get the path for a snippet markdown file.

    Args:
        snippets_dir: The snippets output directory.
        short_name: The short name of the snippet (without section/entity prefix).

    Returns:
        Path to the {short_name}.md file.
    """
    return snippets_dir / f"{short_name}.md"


# --- Convenience Functions (Compose Multiple Path Operations) ---


def get_entity_snippets_dir(
    output_dir: Path, section: str, entity_name: str, entity_type: CategoryType
) -> Path:
    """Get the snippets directory for an entity.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        entity_name: The entity name.
        entity_type: The category type of the entity.

    Returns:
        Path to the api/{section}/{entity_name}/snippets directory.
    """
    return get_snippets_output_dir(
        get_entity_dir(output_dir, section, entity_name, entity_type)
    )


def get_entity_properties_inherited_dir(
    output_dir: Path, section: str, entity_name: str, entity_type: CategoryType
) -> Path:
    """Get the inherited properties directory for an entity.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        entity_name: The entity name.
        entity_type: The category type of the entity.

    Returns:
        Path to the api/{section}/{entity_name}/properties/inherited directory.
    """
    return get_properties_inherited_dir(
        get_entity_dir(output_dir, section, entity_name, entity_type)
    )


def get_entity_methods_inherited_dir(
    output_dir: Path, section: str, entity_name: str, entity_type: CategoryType
) -> Path:
    """Get the inherited methods directory for an entity.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        entity_name: The entity name.
        entity_type: The category type of the entity.

    Returns:
        Path to the api/{section}/{entity_name}/methods/inherited directory.
    """
    return get_methods_inherited_dir(
        get_entity_dir(output_dir, section, entity_name, entity_type)
    )


def get_entity_operators_inherited_dir(
    output_dir: Path, section: str, entity_name: str, entity_type: CategoryType
) -> Path:
    """Get the inherited operators directory for an entity.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        entity_name: The entity name.
        entity_type: The category type of the entity.

    Returns:
        Path to the api/{section}/{entity_name}/operators/inherited directory.
    """
    return get_operators_inherited_dir(
        get_entity_dir(output_dir, section, entity_name, entity_type)
    )


def get_entity_inherited_member_file(
    output_dir: Path,
    section: str,
    entity_name: str,
    entity_type: CategoryType,
    member_type: str,
    source_section: str,
    source_entity: str,
    member_name: str,
) -> Path:
    """Get the path for an inherited member file for an entity.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        entity_name: The entity name.
        entity_type: The category type of the entity.
        member_type: The member type ('properties', 'methods', or 'operators').
        source_section: The section where the member is defined.
        source_entity: The entity where the member is defined.
        member_name: The member name.

    Returns:
        Path to the inherited member markdown file.
    """
    entity_dir = get_entity_dir(output_dir, section, entity_name, entity_type)
    inherited_dir = entity_dir / member_type / "inherited"
    return get_inherited_member_file(
        inherited_dir, source_section, source_entity, member_name
    )


# --- Input Path Builders ---


def get_input_flutter_dir(doc_dir: Path) -> Path:
    """Get the input Flutter documentation root directory path.

    Args:
        doc_dir: The root documentation directory.

    Returns:
        Path to the flutter/ directory.
    """
    return doc_dir / "flutter"


def get_input_section_dir(doc_dir: Path, section: str) -> Path:
    """Get the input section directory path.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.

    Returns:
        Path to the flutter/{section} directory.
    """
    return doc_dir / "flutter" / section


def get_input_class_file(doc_dir: Path, section: str, class_name: str) -> Path:
    """Get the input class HTML file path.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.
        class_name: The class name.

    Returns:
        Path to the flutter/{section}/{class_name}-class.html file.
    """
    return get_input_section_dir(doc_dir, section) / f"{class_name}-class.html"


def get_input_member_file(
    doc_dir: Path, section: str, entity_name: str, member_name: str
) -> Path:
    """Get the input member HTML file path.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.
        entity_name: The entity name.
        member_name: The member name.

    Returns:
        Path to the flutter/{section}/{entity_name}/{member_name}.html file.
    """
    return get_input_section_dir(doc_dir, section) / entity_name / f"{member_name}.html"


def get_input_snippets_dir(doc_dir: Path) -> Path:
    """Get the input snippets directory path.

    Args:
        doc_dir: The root documentation directory.

    Returns:
        Path to the snippets directory.
    """
    return doc_dir / "snippets"


# --- Directory Creation Helper ---


def ensure_dir_exists(dir_path: Path) -> Path:
    """Create directory if it doesn't exist.

    Args:
        dir_path: The directory path to create.

    Returns:
        The same directory path (for chaining).
    """
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path
