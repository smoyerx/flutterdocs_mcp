"""Unit tests for the categorization module."""

from pathlib import Path
from typing import Any

import pytest

from flutterdoc_gen.convert.categorization import find_and_categorize_root_files


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

    assert len(result["class"]) == 3
    assert ("Widget", mock_section_dir / "Widget-class.html") in result["class"]
    assert ("State", mock_section_dir / "State-class.html") in result["class"]
    assert ("Text", mock_section_dir / "Text-class.html") in result["class"]


def test_categorize_mixin_files(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization of mixin documentation files."""
    create_test_files(
        mock_section_dir,
        ["BaseSliderTrackShape-mixin.html", "MaterialStateMixin-mixin.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result["mixin"]) == 2
    assert (
        "BaseSliderTrackShape",
        mock_section_dir / "BaseSliderTrackShape-mixin.html",
    ) in result["mixin"]
    assert (
        "MaterialStateMixin",
        mock_section_dir / "MaterialStateMixin-mixin.html",
    ) in result["mixin"]


def test_categorize_constant_files(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization of constant documentation files."""
    create_test_files(
        mock_section_dir,
        ["accelerateEasing-constant.html", "kBottomNavigationBarHeight-constant.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result["constant"]) == 2
    assert (
        "accelerateEasing",
        mock_section_dir / "accelerateEasing-constant.html",
    ) in result["constant"]
    assert (
        "kBottomNavigationBarHeight",
        mock_section_dir / "kBottomNavigationBarHeight-constant.html",
    ) in result["constant"]


def test_categorize_library_files(tmp_path: Path, mock_section_dir: Path) -> None:
    """Test categorization of library documentation files."""
    create_test_files(
        mock_section_dir, ["material-library.html", "widgets-library.html"]
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result["library"]) == 2
    assert ("material", mock_section_dir / "material-library.html") in result["library"]
    assert ("widgets", mock_section_dir / "widgets-library.html") in result["library"]


def test_categorize_extension_type_files(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of extension type documentation files."""
    create_test_files(
        mock_section_dir,
        ["OverlayChildLayoutInfo-extension-type.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result["extension_type"]) == 1
    assert (
        "OverlayChildLayoutInfo",
        mock_section_dir / "OverlayChildLayoutInfo-extension-type.html",
    ) in result["extension_type"]


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

    assert len(result["enum"]) == 2
    assert ("HourFormat", mock_section_dir / "HourFormat.html") in result["enum"]
    assert ("StretchMode", mock_section_dir / "StretchMode.html") in result["enum"]


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

    assert len(result["extension"]) == 1
    assert (
        "WidgetStateOperators",
        mock_section_dir / "WidgetStateOperators.html",
    ) in result["extension"]


def test_categorize_function_files_lowercase(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of function documentation files (lowercase first letter)."""
    create_test_files(
        mock_section_dir,
        ["showBottomSheet.html", "showMenu.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result["function"]) == 2
    assert (
        "showBottomSheet",
        mock_section_dir / "showBottomSheet.html",
    ) in result["function"]
    assert ("showMenu", mock_section_dir / "showMenu.html") in result["function"]


def test_categorize_typedef_files_uppercase(
    tmp_path: Path, mock_section_dir: Path
) -> None:
    """Test categorization of typedef documentation files (uppercase first letter)."""
    create_test_files(
        mock_section_dir,
        ["DrawerCallback.html", "WidgetBuilder.html"],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result["typedef"]) == 2
    assert (
        "DrawerCallback",
        mock_section_dir / "DrawerCallback.html",
    ) in result["typedef"]
    assert (
        "WidgetBuilder",
        mock_section_dir / "WidgetBuilder.html",
    ) in result["typedef"]


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
    assert len(result["class"]) == 1
    assert ("Widget", mock_section_dir / "Widget-class.html") in result["class"]

    # Enum should not be categorized without its main file
    assert len(result["enum"]) == 0


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
    assert len(result["enum"]) == 0
    assert len(result["typedef"]) == 1
    assert (
        "PotentialEnum",
        mock_section_dir / "PotentialEnum.html",
    ) in result["typedef"]


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
    assert len(result["extension"]) == 0
    assert len(result["typedef"]) == 1


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
            "material-library.html",
            "HourFormat.html",
            "HourFormat-enum-sidebar.html",
            "showBottomSheet.html",
            "DrawerCallback.html",
        ],
    )

    result = find_and_categorize_root_files(tmp_path, "test_section")

    assert len(result["class"]) == 2
    assert len(result["mixin"]) == 1
    assert len(result["constant"]) == 1
    assert len(result["library"]) == 1
    assert len(result["enum"]) == 1
    assert len(result["function"]) == 1
    assert len(result["typedef"]) == 1
    assert len(result["extension"]) == 0
    assert len(result["extension_type"]) == 0


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

    assert len(result["function"]) == 2
    assert ("lowerCaseStart", mock_section_dir / "lowerCaseStart.html") in result[
        "function"
    ]
    assert ("anotherFunction", mock_section_dir / "anotherFunction.html") in result[
        "function"
    ]

    assert len(result["typedef"]) == 2
    assert ("UpperCaseStart", mock_section_dir / "UpperCaseStart.html") in result[
        "typedef"
    ]
    assert ("AnotherTypedef", mock_section_dir / "AnotherTypedef.html") in result[
        "typedef"
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

    assert len(result["class"]) == 1
    assert len(result["typedef"]) == 0
    assert ("Widget", mock_section_dir / "Widget-class.html") in result["class"]


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
    class_names = [name for name, _ in result["class"]]
    assert class_names == ["Apple", "Mango", "Zebra"]
