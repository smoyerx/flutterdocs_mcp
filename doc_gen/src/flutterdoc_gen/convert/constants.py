"""Constants for categorization in the convert module."""

from enum import Enum


class CategoryType(str, Enum):
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
