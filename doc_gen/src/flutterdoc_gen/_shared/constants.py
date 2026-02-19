"""Shared constants for Flutter/Dart documentation workflows.

This module defines domain enums used across multiple flutterdoc_gen tools (convert, load).
CategoryType and MemberType represent the logical structure of Flutter/Dart documentation.
"""

from enum import StrEnum


class CategoryType(StrEnum):
    """Category types for Flutter/Dart documentation files.

    Each category corresponds to a specific documentation file pattern:
    - CLASS: Class documentation files (*-class.html)
    - MIXIN: Mixin documentation files (*-mixin.html)
    - ENUM: Enum documentation files (identified via *-enum-sidebar.html)
    - CONSTANT: Constant documentation files (*-constant.html)
    - LIBRARY: Library documentation files (*-library.html)
    - EXTENSION_TYPE: Extension type files (*-extension-type.html)
    - EXTENSION: Extension files (identified via *-extension-sidebar.html)
    - FUNCTION: Function documentation files (lowercase-starting names)
    - TYPEDEF: Typedef documentation files (uppercase-starting names)
    """

    CLASS = "class"
    MIXIN = "mixin"
    ENUM = "enum"
    CONSTANT = "constant"
    LIBRARY = "library"
    EXTENSION_TYPE = "extension_type"
    EXTENSION = "extension"
    FUNCTION = "function"
    TYPEDEF = "typedef"


# All category values in canonical order for iteration
ALL_CATEGORIES = [
    CategoryType.CLASS,
    CategoryType.MIXIN,
    CategoryType.CONSTANT,
    CategoryType.LIBRARY,
    CategoryType.EXTENSION_TYPE,
    CategoryType.ENUM,
    CategoryType.EXTENSION,
    CategoryType.FUNCTION,
    CategoryType.TYPEDEF,
]


class MemberType(StrEnum):
    """Logical member types for entity documentation.

    Maps to filesystem subdirectories via PathBuilder.

    Note: A snippet is not a member of an entity, but we include it here because we are
    grouping code snippets with the member documentation for an entity.
    """

    CONSTRUCTOR = "constructor"
    CONSTANT = "constant"
    PROPERTY = "property"
    METHOD = "method"
    OPERATOR = "operator"
    STATIC = "static_method"
    SNIPPET = "snippet"
