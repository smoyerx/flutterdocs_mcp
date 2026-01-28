"""Path construction utilities for the convert tool.

This module centralizes all path construction logic for input and output files,
providing a consistent interface for building file paths throughout the
conversion process.
"""

from pathlib import Path


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


def get_class_dir(output_dir: Path, section: str, class_name: str) -> Path:
    """Get the class output directory path.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        class_name: The class name.

    Returns:
        Path to the api/{section}/{class_name} directory.
    """
    return get_api_section_dir(output_dir, section) / class_name


def get_class_file(output_dir: Path, section: str, class_name: str) -> Path:
    """Get the main class markdown file path.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        class_name: The class name.

    Returns:
        Path to the api/{section}/{class_name}/{class_name}.md file.
    """
    return get_class_dir(output_dir, section, class_name) / f"{class_name}.md"


# --- Member Directory Builders ---


def get_constructors_dir(class_dir: Path) -> Path:
    """Get the constructors subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the constructors subdirectory.
    """
    return class_dir / "constructors"


def get_properties_native_dir(class_dir: Path) -> Path:
    """Get the native properties subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the properties/native subdirectory.
    """
    return class_dir / "properties" / "native"


def get_properties_inherited_dir(class_dir: Path) -> Path:
    """Get the inherited properties subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the properties/inherited subdirectory.
    """
    return class_dir / "properties" / "inherited"


def get_methods_native_dir(class_dir: Path) -> Path:
    """Get the native methods subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the methods/native subdirectory.
    """
    return class_dir / "methods" / "native"


def get_methods_inherited_dir(class_dir: Path) -> Path:
    """Get the inherited methods subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the methods/inherited subdirectory.
    """
    return class_dir / "methods" / "inherited"


def get_operators_native_dir(class_dir: Path) -> Path:
    """Get the native operators subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the operators/native subdirectory.
    """
    return class_dir / "operators" / "native"


def get_operators_inherited_dir(class_dir: Path) -> Path:
    """Get the inherited operators subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the operators/inherited subdirectory.
    """
    return class_dir / "operators" / "inherited"


def get_statics_dir(class_dir: Path) -> Path:
    """Get the static methods subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the statics subdirectory.
    """
    return class_dir / "statics"


def get_snippets_output_dir(class_dir: Path) -> Path:
    """Get the snippets subdirectory path.

    Args:
        class_dir: The class output directory.

    Returns:
        Path to the snippets subdirectory.
    """
    return class_dir / "snippets"


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
    inherited_dir: Path, source_section: str, source_class: str, member_name: str
) -> Path:
    """Get the path for an inherited member markdown file.

    Args:
        inherited_dir: The inherited member directory.
        source_section: The section where the member is defined.
        source_class: The class where the member is defined.
        member_name: The member name.

    Returns:
        Path to the {section}___{class}___{member}.md file.
    """
    filename = f"{source_section}___{source_class}___{member_name}.md"
    return inherited_dir / filename


def get_snippet_output_file(snippets_dir: Path, short_name: str) -> Path:
    """Get the path for a snippet markdown file.

    Args:
        snippets_dir: The snippets output directory.
        short_name: The short name of the snippet (without section/class prefix).

    Returns:
        Path to the {short_name}.md file.
    """
    return snippets_dir / f"{short_name}.md"


# --- Convenience Functions (Compose Multiple Path Operations) ---


def get_class_snippets_dir(output_dir: Path, section: str, class_name: str) -> Path:
    """Get the snippets directory for a class.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        class_name: The class name.

    Returns:
        Path to the api/{section}/{class_name}/snippets directory.
    """
    return get_snippets_output_dir(get_class_dir(output_dir, section, class_name))


def get_class_properties_inherited_dir(
    output_dir: Path, section: str, class_name: str
) -> Path:
    """Get the inherited properties directory for a class.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        class_name: The class name.

    Returns:
        Path to the api/{section}/{class_name}/properties/inherited directory.
    """
    return get_properties_inherited_dir(get_class_dir(output_dir, section, class_name))


def get_class_methods_inherited_dir(
    output_dir: Path, section: str, class_name: str
) -> Path:
    """Get the inherited methods directory for a class.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        class_name: The class name.

    Returns:
        Path to the api/{section}/{class_name}/methods/inherited directory.
    """
    return get_methods_inherited_dir(get_class_dir(output_dir, section, class_name))


def get_class_operators_inherited_dir(
    output_dir: Path, section: str, class_name: str
) -> Path:
    """Get the inherited operators directory for a class.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        class_name: The class name.

    Returns:
        Path to the api/{section}/{class_name}/operators/inherited directory.
    """
    return get_operators_inherited_dir(get_class_dir(output_dir, section, class_name))


def get_class_inherited_member_file(
    output_dir: Path,
    section: str,
    class_name: str,
    member_type: str,
    source_section: str,
    source_class: str,
    member_name: str,
) -> Path:
    """Get the path for an inherited member file for a class.

    Args:
        output_dir: The root output directory.
        section: The documentation section name.
        class_name: The class name.
        member_type: The member type ('properties', 'methods', or 'operators').
        source_section: The section where the member is defined.
        source_class: The class where the member is defined.
        member_name: The member name.

    Returns:
        Path to the inherited member markdown file.
    """
    class_dir = get_class_dir(output_dir, section, class_name)
    inherited_dir = class_dir / member_type / "inherited"
    return get_inherited_member_file(
        inherited_dir, source_section, source_class, member_name
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
    doc_dir: Path, section: str, class_name: str, member_name: str
) -> Path:
    """Get the input member HTML file path.

    Args:
        doc_dir: The root documentation directory.
        section: The documentation section name.
        class_name: The class name.
        member_name: The member name.

    Returns:
        Path to the flutter/{section}/{class_name}/{member_name}.html file.
    """
    return get_input_section_dir(doc_dir, section) / class_name / f"{member_name}.html"


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
