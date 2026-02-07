"""Integration tests for entity type categorization and handling.

Tests file categorization, directory structure organization, and type-specific
processing for classes, mixins, enums, extensions, and standalone types.
"""

from pathlib import Path


from convert.conftest import (
    build_entity_path_builder,
    run_convert,
    SAMPLES_DIR,
)
from flutterdoc_gen.convert.constants import CategoryType
from flutterdoc_gen.convert.transformations import FOOTER_MARKER


class TestFileCategorization:
    """Integration tests for root documentation file categorization."""

    def test_categorize_material_section(self, output_dir: Path) -> None:
        """Test correct categorization of material section sample files."""
        from flutterdoc_gen.convert.categorization import find_and_categorize_root_files

        categorized = find_and_categorize_root_files(SAMPLES_DIR, "material")

        # Verify classes
        class_names = [name for name, _ in categorized[CategoryType.CLASS]]
        assert sorted(class_names) == ["InkWell", "ListTile"]

        # Verify mixins
        mixin_names = [name for name, _ in categorized[CategoryType.MIXIN]]
        assert sorted(mixin_names) == ["BaseSliderTrackShape", "MaterialStateMixin"]

        # Verify constants
        constant_names = [name for name, _ in categorized[CategoryType.CONSTANT]]
        assert sorted(constant_names) == [
            "accelerateEasing",
            "kBottomNavigationBarHeight",
        ]

        # Verify libraries
        library_names = [name for name, _ in categorized[CategoryType.LIBRARY]]
        assert library_names == ["material"]
        # Verify library file path is index.html
        library_paths = [path for _, path in categorized[CategoryType.LIBRARY]]
        assert len(library_paths) == 1
        assert library_paths[0].name == "index.html"

        # Verify enums
        enum_names = [name for name, _ in categorized[CategoryType.ENUM]]
        assert sorted(enum_names) == ["HourFormat", "StretchMode"]

        # Verify functions
        function_names = [name for name, _ in categorized[CategoryType.FUNCTION]]
        assert sorted(function_names) == ["showBottomSheet", "showMenu"]

        # Verify typedefs
        typedef_names = [name for name, _ in categorized[CategoryType.TYPEDEF]]
        assert sorted(typedef_names) == ["DrawerCallback", "MaterialState"]

        # Verify no extension types or extensions in material section
        assert len(categorized[CategoryType.EXTENSION_TYPE]) == 0
        assert len(categorized[CategoryType.EXTENSION]) == 0

    def test_categorize_widgets_section(self, output_dir: Path) -> None:
        """Test correct categorization of widgets section sample files."""
        from flutterdoc_gen.convert.categorization import find_and_categorize_root_files

        categorized = find_and_categorize_root_files(SAMPLES_DIR, "widgets")

        # Verify classes
        class_names = [name for name, _ in categorized[CategoryType.CLASS]]
        assert sorted(class_names) == ["State", "Text"]

        # Verify extensions
        extension_names = [name for name, _ in categorized[CategoryType.EXTENSION]]
        assert extension_names == ["WidgetStateOperators"]

        # Verify extension types
        extension_type_names = [
            name for name, _ in categorized[CategoryType.EXTENSION_TYPE]
        ]
        assert extension_type_names == ["OverlayChildLayoutInfo"]

        # Verify libraries
        library_names = [name for name, _ in categorized[CategoryType.LIBRARY]]
        assert library_names == ["widgets"]
        # Verify library file path is index.html
        library_paths = [path for _, path in categorized[CategoryType.LIBRARY]]
        assert len(library_paths) == 1
        assert library_paths[0].name == "index.html"

        # Verify no other types in widgets section
        assert len(categorized[CategoryType.MIXIN]) == 0
        assert len(categorized[CategoryType.CONSTANT]) == 0
        assert len(categorized[CategoryType.ENUM]) == 0
        assert len(categorized[CategoryType.FUNCTION]) == 0
        assert len(categorized["typedef"]) == 0

    def test_all_categories_processed(self, output_dir: Path) -> None:
        """Test that convert processes all categorized files without error."""
        result = run_convert(SAMPLES_DIR, "material", output_dir, verbose=True)

        assert result.returncode == 0
        assert "Successfully processed" in result.stdout

        # Verify that the output mentions processing different types
        # Classes are fully processed, others are just logged
        # Note: verbose logging goes to stderr
        assert "Converting class:" in result.stderr
        assert "Converting mixin:" in result.stderr
        assert "Converting constant:" in result.stderr
        assert "Converting library:" in result.stderr
        assert "Converting enum:" in result.stderr
        assert "Converting function:" in result.stderr
        assert "Converting typedef:" in result.stderr


class TestDirectoryStructureByType:
    """Tests for output directory structure organization by documentation type.

    Validates that PathBuilder generates correct directory structures for each
    entity type according to the categorization system.
    """

    def test_class_directory_structure(self, output_dir: Path) -> None:
        """Classes should be placed in api/{section}/classes/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        class_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        class_dir = class_builder.get_entity_dir()

        expected_path = output_dir / "api" / "material" / "classes" / "InkWell"
        assert class_dir == expected_path
        assert class_dir.exists()
        assert (class_dir / "InkWell.md").exists()

    def test_mixin_directory_structure(self, output_dir: Path) -> None:
        """Mixins should be placed in api/{section}/mixins/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "BaseSliderTrackShape", CategoryType.MIXIN
        )
        mixin_dir = mixin_builder.get_entity_dir()

        expected_path = (
            output_dir / "api" / "material" / "mixins" / "BaseSliderTrackShape"
        )
        assert mixin_dir == expected_path
        assert mixin_dir.exists()
        assert (mixin_dir / "BaseSliderTrackShape.md").exists()

    def test_enum_directory_structure(self, output_dir: Path) -> None:
        """Enums should be placed in api/{section}/enums/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        enum_builder = build_entity_path_builder(
            output_dir, "material", "HourFormat", CategoryType.ENUM
        )
        enum_dir = enum_builder.get_entity_dir()

        expected_path = output_dir / "api" / "material" / "enums" / "HourFormat"
        assert enum_dir == expected_path
        assert enum_dir.exists()
        assert (enum_dir / "HourFormat.md").exists()

    def test_extension_directory_structure(self, output_dir: Path) -> None:
        """Extensions should be placed in api/{section}/extensions/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        extension_builder = build_entity_path_builder(
            output_dir, "widgets", "WidgetStateOperators", CategoryType.EXTENSION
        )
        extension_dir = extension_builder.get_entity_dir()

        expected_path = (
            output_dir / "api" / "widgets" / "extensions" / "WidgetStateOperators"
        )
        assert extension_dir == expected_path
        assert extension_dir.exists()
        assert (extension_dir / "WidgetStateOperators.md").exists()

    def test_extension_type_directory_structure(self, output_dir: Path) -> None:
        """Extension types should be placed in api/{section}/extension_types/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        ext_type_builder = build_entity_path_builder(
            output_dir, "widgets", "OverlayChildLayoutInfo", CategoryType.EXTENSION_TYPE
        )
        ext_type_dir = ext_type_builder.get_entity_dir()

        expected_path = (
            output_dir
            / "api"
            / "widgets"
            / "extension_types"
            / "OverlayChildLayoutInfo"
        )
        assert ext_type_dir == expected_path
        assert ext_type_dir.exists()
        assert (ext_type_dir / "OverlayChildLayoutInfo.md").exists()

    def test_constant_file_structure(self, output_dir: Path) -> None:
        """Constants should be in api/{section}/constants/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        constant_builder = build_entity_path_builder(
            output_dir, "material", "accelerateEasing", CategoryType.CONSTANT
        )
        constant_file = constant_builder.get_entity_file()

        expected_path = (
            output_dir
            / "api"
            / "material"
            / "constants"
            / "accelerateEasing"
            / "accelerateEasing.md"
        )
        assert constant_file == expected_path
        assert constant_file.exists()
        assert constant_file.is_file()

    def test_function_file_structure(self, output_dir: Path) -> None:
        """Functions should be in api/{section}/functions/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        function_builder = build_entity_path_builder(
            output_dir, "material", "showBottomSheet", CategoryType.FUNCTION
        )
        function_file = function_builder.get_entity_file()

        expected_path = (
            output_dir
            / "api"
            / "material"
            / "functions"
            / "showBottomSheet"
            / "showBottomSheet.md"
        )
        assert function_file == expected_path
        assert function_file.exists()
        assert function_file.is_file()

    def test_typedef_file_structure(self, output_dir: Path) -> None:
        """Typedefs should be in api/{section}/typedefs/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        typedef_builder = build_entity_path_builder(
            output_dir, "material", "DrawerCallback", CategoryType.TYPEDEF
        )
        typedef_file = typedef_builder.get_entity_file()

        expected_path = (
            output_dir
            / "api"
            / "material"
            / "typedefs"
            / "DrawerCallback"
            / "DrawerCallback.md"
        )
        assert typedef_file == expected_path
        assert typedef_file.exists()
        assert typedef_file.is_file()

    def test_library_file_structure(self, output_dir: Path) -> None:
        """Libraries should be in api/{section}/library/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        library_builder = build_entity_path_builder(
            output_dir, "material", "material", CategoryType.LIBRARY
        )
        library_file = library_builder.get_entity_file()

        expected_path = (
            output_dir / "api" / "material" / "library" / "material" / "material.md"
        )
        assert library_file == expected_path
        assert library_file.exists()
        assert library_file.is_file()


class TestMixinProcessing:
    """Tests for mixin-specific processing behavior.

    Mixins have full member processing like classes, but should NOT have
    constructor sections (Dart language constraint).
    """

    def test_mixin_no_constructors_directory(self, output_dir: Path) -> None:
        """Mixins should NOT have a constructors directory.

        Mixins cannot have constructors in Dart, so the constructors
        subdirectory should not be created during processing.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "BaseSliderTrackShape", CategoryType.MIXIN
        )
        mixin_dir = mixin_builder.get_entity_dir()
        constructors_dir = mixin_dir / "constructors"

        assert not constructors_dir.exists(), (
            f"Mixin should not have constructors directory: {constructors_dir}"
        )

    def test_mixin_has_other_members(self, output_dir: Path) -> None:
        """Mixins should have other member types processed normally.

        While mixins can't have constructors, they can have properties,
        methods, and operators.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "BaseSliderTrackShape", CategoryType.MIXIN
        )

        # Check that root file exists
        mixin_file = mixin_builder.get_entity_file()
        assert mixin_file.exists(), "Mixin root file should exist"

    def test_material_state_mixin_processing(self, output_dir: Path) -> None:
        """MaterialStateMixin should be processed without constructors."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "MaterialStateMixin", CategoryType.MIXIN
        )

        # Verify mixin file exists
        mixin_file = mixin_builder.get_entity_file()
        assert mixin_file.exists()

        # Verify no constructors directory
        mixin_dir = mixin_builder.get_entity_dir()
        constructors_dir = mixin_dir / "constructors"
        assert not constructors_dir.exists()


class TestStandaloneTypeProcessing:
    """Tests for standalone documentation types (constant, function, typedef, library).

    These types should produce single markdown files without member subdirectories
    or complex processing beyond root file conversion.
    """

    def test_constant_no_subdirectories(self, output_dir: Path) -> None:
        """Constants should not create entity subdirectories.

        Constants are standalone files with no members.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        constant_builder = build_entity_path_builder(
            output_dir, "material", "accelerateEasing", CategoryType.CONSTANT
        )
        constant_file = constant_builder.get_entity_file()
        assert constant_file.exists()
        assert constant_file.is_file()

        # Verify this is a file, not a directory
        assert not constant_file.is_dir()

    def test_function_no_subdirectories(self, output_dir: Path) -> None:
        """Functions should not create member subdirectories.

        Functions have an entity directory but no member subdirectories.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        function_builder = build_entity_path_builder(
            output_dir, "material", "showBottomSheet", CategoryType.FUNCTION
        )
        function_file = function_builder.get_entity_file()
        assert function_file.exists()
        assert function_file.is_file()

        # Functions have an entity directory
        function_dir = function_builder.get_entity_dir()
        assert function_dir.exists()

        # But should not have member subdirectories (properties, methods, etc.)
        member_subdirs = [d for d in function_dir.iterdir() if d.is_dir()]
        assert len(member_subdirs) == 0, (
            f"Function should not have member subdirs: {member_subdirs}"
        )

    def test_typedef_no_subdirectories(self, output_dir: Path) -> None:
        """Typedefs should not create member subdirectories.

        Typedefs have an entity directory but no member subdirectories.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        typedef_builder = build_entity_path_builder(
            output_dir, "material", "DrawerCallback", CategoryType.TYPEDEF
        )
        typedef_file = typedef_builder.get_entity_file()
        assert typedef_file.exists()
        assert typedef_file.is_file()

        # Typedefs have an entity directory
        typedef_dir = typedef_builder.get_entity_dir()
        assert typedef_dir.exists()

        # But should not have member subdirectories (properties, methods, etc.)
        member_subdirs = [d for d in typedef_dir.iterdir() if d.is_dir()]
        assert len(member_subdirs) == 0, (
            f"Typedef should not have member subdirs: {member_subdirs}"
        )

    def test_library_no_subdirectories(self, output_dir: Path) -> None:
        """Libraries should not create member subdirectories.

        Libraries have an entity directory but no member subdirectories.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        library_builder = build_entity_path_builder(
            output_dir, "material", "material", CategoryType.LIBRARY
        )
        library_file = library_builder.get_entity_file()
        assert library_file.exists()
        assert library_file.is_file()

        # Libraries have an entity directory
        library_dir = library_builder.get_entity_dir()
        assert library_dir.exists()

        # But should not have member subdirectories (properties, methods, etc.)
        member_subdirs = [d for d in library_dir.iterdir() if d.is_dir()]
        assert len(member_subdirs) == 0, (
            f"Library should not have member subdirs: {member_subdirs}"
        )

    def test_all_standalone_types_converted(self, output_dir: Path) -> None:
        """All standalone type files should be converted to markdown."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Check one of each standalone type
        constant_file = build_entity_path_builder(
            output_dir, "material", "accelerateEasing", CategoryType.CONSTANT
        ).get_entity_file()
        function_file = build_entity_path_builder(
            output_dir, "material", "showBottomSheet", CategoryType.FUNCTION
        ).get_entity_file()
        typedef_file = build_entity_path_builder(
            output_dir, "material", "DrawerCallback", CategoryType.TYPEDEF
        ).get_entity_file()
        library_file = build_entity_path_builder(
            output_dir, "material", "material", CategoryType.LIBRARY
        ).get_entity_file()

        for file in [constant_file, function_file, typedef_file, library_file]:
            assert file.exists(), f"Standalone type file not found: {file}"
            content = file.read_text(encoding="utf-8")
            assert content.startswith("#"), f"File should start with heading: {file}"
            assert FOOTER_MARKER not in content, f"File should not have footer: {file}"
