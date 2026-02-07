"""Unit tests for the categorization module."""

from pathlib import Path
from typing import Any

import pytest

from flutterdoc_gen.convert.categorization import find_and_categorize_root_files
from flutterdoc_gen._shared.constants import CategoryType


@pytest.fixture
def mock_section_dir(tmp_path: Path) -> Path:
    """Create a temporary section directory for testing."""
    section_dir = tmp_path / "flutter" / "test_section"
    section_dir.mkdir(parents=True)
    return section_dir


def create_test_files(section_dir: Path, filenames: list[str]) -> None:
    """Create test HTML files in the section directory."""
    for filename in filenames:
        (section_dir / filename).write_text("<html></html>", encoding="utf-8")


def test_categorize_class_files(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization of class documentation files."""
    create_test_files(
        mock_section_dir,
        ["Widget-class.html", "State-class.html", "Text-class.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.CLASS]) == 3
    assert ("Widget", mock_section_dir / "Widget-class.html") in result[
        CategoryType.CLASS
    ]
    assert ("State", mock_section_dir / "State-class.html") in result[
        CategoryType.CLASS
    ]
    assert ("Text", mock_section_dir / "Text-class.html") in result[CategoryType.CLASS]


def test_categorize_mixin_files(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization of mixin documentation files."""
    create_test_files(
        mock_section_dir,
        ["BaseSliderTrackShape-mixin.html", "MaterialStateMixin-mixin.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.MIXIN]) == 2
    assert (
        "BaseSliderTrackShape",
        mock_section_dir / "BaseSliderTrackShape-mixin.html",
    ) in result[CategoryType.MIXIN]
    assert (
        "MaterialStateMixin",
        mock_section_dir / "MaterialStateMixin-mixin.html",
    ) in result[CategoryType.MIXIN]


def test_categorize_constant_files(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization of constant documentation files."""
    create_test_files(
        mock_section_dir,
        ["accelerateEasing-constant.html", "kBottomNavigationBarHeight-constant.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.CONSTANT]) == 2
    assert (
        "accelerateEasing",
        mock_section_dir / "accelerateEasing-constant.html",
    ) in result[CategoryType.CONSTANT]
    assert (
        "kBottomNavigationBarHeight",
        mock_section_dir / "kBottomNavigationBarHeight-constant.html",
    ) in result[CategoryType.CONSTANT]


def test_categorize_library_files(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization of library documentation files."""
    # Library identification requires both index.html and test_section-library.html
    create_test_files(mock_section_dir, ["index.html", "test_section-library.html"])

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.LIBRARY]) == 1
    assert ("test_section", mock_section_dir / "index.html") in result[
        CategoryType.LIBRARY
    ]


def test_categorize_extension_type_files(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of extension type documentation files."""
    create_test_files(
        mock_section_dir,
        ["OverlayChildLayoutInfo-extension-type.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.EXTENSION_TYPE]) == 1
    assert (
        "OverlayChildLayoutInfo",
        mock_section_dir / "OverlayChildLayoutInfo-extension-type.html",
    ) in result[CategoryType.EXTENSION_TYPE]


def test_categorize_enum_files_with_sidebar(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of enum documentation files (requires sidebar)."""
    create_test_files(
        mock_section_dir,
        [
            "HourFormat.html",
            "HourFormat-enum-sidebar.html",
            "StretchMode.html",
            "StretchMode-enum-sidebar.html",
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.ENUM]) == 2
    assert ("HourFormat", mock_section_dir / "HourFormat.html") in result[
        CategoryType.ENUM
    ]
    assert ("StretchMode", mock_section_dir / "StretchMode.html") in result[
        CategoryType.ENUM
    ]


def test_categorize_extension_files_with_sidebar(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of extension documentation files (requires sidebar)."""
    create_test_files(
        mock_section_dir,
        [
            "WidgetStateOperators.html",
            "WidgetStateOperators-extension-sidebar.html",
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.EXTENSION]) == 1
    assert (
        "WidgetStateOperators",
        mock_section_dir / "WidgetStateOperators.html",
    ) in result[CategoryType.EXTENSION]


def test_categorize_function_files_lowercase(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of function documentation files (lowercase first letter)."""
    create_test_files(
        mock_section_dir,
        ["showBottomSheet.html", "showMenu.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.FUNCTION]) == 2
    assert (
        "showBottomSheet",
        mock_section_dir / "showBottomSheet.html",
    ) in result[CategoryType.FUNCTION]
    assert ("showMenu", mock_section_dir / "showMenu.html") in result[
        CategoryType.FUNCTION
    ]


def test_categorize_typedef_files_uppercase(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of typedef documentation files (uppercase first letter)."""
    create_test_files(
        mock_section_dir,
        ["DrawerCallback.html", "WidgetBuilder.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.TYPEDEF]) == 2
    assert (
        "DrawerCallback",
        mock_section_dir / "DrawerCallback.html",
    ) in result[CategoryType.TYPEDEF]
    assert (
        "WidgetBuilder",
        mock_section_dir / "WidgetBuilder.html",
    ) in result[CategoryType.TYPEDEF]


def test_sidebar_files_are_ignored(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test that sidebar files themselves are not categorized as root files."""
    create_test_files(
        mock_section_dir,
        [
            "Widget-class.html",
            "Widget-class-sidebar.html",
            "HourFormat-enum-sidebar.html",
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    # Should only have the class, not the sidebar files
    assert len(result[CategoryType.CLASS]) == 1
    assert ("Widget", mock_section_dir / "Widget-class.html") in result[
        CategoryType.CLASS
    ]

    # Enum should not be categorized without its main file
    assert len(result[CategoryType.ENUM]) == 0


def test_enum_without_sidebar_not_categorized(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test that files matching enum pattern are not categorized without sidebar."""
    create_test_files(
        mock_section_dir,
        ["PotentialEnum.html"],  # No sidebar file
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    # Should be categorized as typedef (uppercase), not enum (no sidebar)
    assert len(result[CategoryType.ENUM]) == 0
    assert len(result[CategoryType.TYPEDEF]) == 1
    assert (
        "PotentialEnum",
        mock_section_dir / "PotentialEnum.html",
    ) in result[CategoryType.TYPEDEF]


def test_extension_without_sidebar_not_categorized(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test that files matching extension pattern are not categorized without sidebar."""
    create_test_files(
        mock_section_dir,
        ["PotentialExtension.html"],  # No sidebar file
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    # Should be categorized as typedef (uppercase), not extension (no sidebar)
    assert len(result[CategoryType.EXTENSION]) == 0
    assert len(result[CategoryType.TYPEDEF]) == 1


def test_empty_section_directory(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test handling of empty section directory."""
    result = find_and_categorize_root_files(tmp_path, "test_section")

    # All categories should be empty lists
    for category in result.values():
        assert len(category) == 0


def test_mixed_categories(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization with multiple file types in the same section."""
    create_test_files(
        mock_section_dir,
        [
            "InkWell-class.html",
            "ListTile-class.html",
            "BaseSliderTrackShape-mixin.html",
            "accelerateEasing-constant.html",
            "index.html",
            "test_section-library.html",
            "HourFormat.html",
            "HourFormat-enum-sidebar.html",
            "showBottomSheet.html",
            "DrawerCallback.html",
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.CLASS]) == 2
    assert len(result[CategoryType.MIXIN]) == 1
    assert len(result[CategoryType.CONSTANT]) == 1
    assert len(result[CategoryType.LIBRARY]) == 1
    assert len(result[CategoryType.ENUM]) == 1
    assert len(result[CategoryType.FUNCTION]) == 1
    assert len(result[CategoryType.TYPEDEF]) == 1
    assert len(result[CategoryType.EXTENSION]) == 0
    assert len(result[CategoryType.EXTENSION_TYPE]) == 0


def test_uncategorizable_file_starting_with_number(
    tmp_path: Path, mock_section_dir: Path, caplog: Any
) -> None:
    """Test that files starting with numbers are logged as uncategorizable."""
    create_test_files(mock_section_dir, ["123test.html"])

    result = find_and_categorize_root_files(tmp_path, "test_section")

    # Should not be in any category
    for category in result.values():
        assert len(category) == 0


def test_case_sensitivity_function_vs_typedef(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test that case sensitivity correctly distinguishes functions from typedefs."""
    create_test_files(
        mock_section_dir,
        [
            "lowerCaseStart.html",  # function
            "UpperCaseStart.html",  # typedef
            "anotherFunction.html",  # function
            "AnotherTypedef.html",  # typedef
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.FUNCTION]) == 2
    assert ("lowerCaseStart", mock_section_dir / "lowerCaseStart.html") in result[
        CategoryType.FUNCTION
    ]
    assert ("anotherFunction", mock_section_dir / "anotherFunction.html") in result[
        CategoryType.FUNCTION
    ]

    assert len(result[CategoryType.TYPEDEF]) == 2
    assert ("UpperCaseStart", mock_section_dir / "UpperCaseStart.html") in result[
        CategoryType.TYPEDEF
    ]
    assert ("AnotherTypedef", mock_section_dir / "AnotherTypedef.html") in result[
        CategoryType.TYPEDEF
    ]


def test_direct_identification_takes_precedence(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test that directly identified patterns take precedence over indirect ones."""
    # Create a file that could match both class and typedef patterns
    # but should be categorized as class because of the -class suffix
    create_test_files(
        mock_section_dir,
        [
            "Widget-class.html",  # Should be class, not typedef
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result[CategoryType.CLASS]) == 1
    assert len(result[CategoryType.TYPEDEF]) == 0
    assert ("Widget", mock_section_dir / "Widget-class.html") in result[
        CategoryType.CLASS
    ]


def test_alphabetical_sorting(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test that results are returned in alphabetical order."""
    create_test_files(
        mock_section_dir,
        [
            "Zebra-class.html",
            "Apple-class.html",
            "Mango-class.html",
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    # Files should be in sorted order (by full filename)
    class_names = [name for name, _ in result[CategoryType.CLASS]]
    assert class_names == ["Apple", "Mango", "Zebra"]
