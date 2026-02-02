"""Unit tests for path construction functions."""

from pathlib import Path

from flutterdoc_gen.convert.constants import CategoryType
from flutterdoc_gen.convert.paths import (
    ensure_dir_exists,
    get_api_root_dir,
    get_api_section_dir,
    get_entity_dir,
    get_entity_file,
    get_constructors_dir,
    get_inherited_member_file,
    get_input_class_file,
    get_input_member_file,
    get_input_section_dir,
    get_input_snippets_dir,
    get_methods_inherited_dir,
    get_methods_native_dir,
    get_native_member_file,
    get_operators_inherited_dir,
    get_operators_native_dir,
    get_properties_inherited_dir,
    get_properties_native_dir,
    get_snippet_output_file,
    get_snippets_output_dir,
    get_statics_dir,
)


class TestOutputDirectoryBuilders:
    """Test output directory path construction."""

    def test_get_api_root_dir(self):
        """Verify api root dir structure."""
        output_dir = Path("/output")
        result = get_api_root_dir(output_dir)
        assert result == Path("/output/api")
        assert str(result).endswith("/api")
        assert result.name == "api"

    def test_get_api_section_dir(self):
        """Verify api section dir structure."""
        output_dir = Path("/output")
        result = get_api_section_dir(output_dir, "material")
        assert result == Path("/output/api/material")
        assert "api" in result.parts
        assert result.name == "material"

    def test_get_api_section_dir_widgets(self):
        """Verify api section dir with different section."""
        output_dir = Path("/output")
        result = get_api_section_dir(output_dir, "widgets")
        assert result == Path("/output/api/widgets")
        assert result.parent == Path("/output/api")

    def test_get_entity_dir(self):
        """Verify class dir includes 'classes' subdirectory."""
        output_dir = Path("/output")
        result = get_entity_dir(output_dir, "material", "ListTile", CategoryType.CLASS)
        assert result == Path("/output/api/material/classes/ListTile")
        assert "classes" in result.parts
        assert result.name == "ListTile"

    def test_get_entity_dir_nested_structure(self):
        """Verify class dir maintains proper nesting."""
        output_dir = Path("/root/output")
        result = get_entity_dir(output_dir, "widgets", "Text", CategoryType.CLASS)
        assert result == Path("/root/output/api/widgets/classes/Text")
        assert result.parent.name == "classes"
        assert result.parent.parent.name == "widgets"

    def test_get_entity_file(self):
        """Verify class file path structure."""
        output_dir = Path("/output")
        result = get_entity_file(output_dir, "widgets", "Text", CategoryType.CLASS)
        assert result == Path("/output/api/widgets/classes/Text/Text.md")
        assert result.name == "Text.md"
        assert result.suffix == ".md"

    def test_get_entity_file_parent_is_class_dir(self):
        """Verify class file parent is the class directory."""
        output_dir = Path("/output")
        section = "material"
        class_name = "Button"

        class_dir = get_entity_dir(output_dir, section, class_name, CategoryType.CLASS)
        class_file = get_entity_file(
            output_dir, section, class_name, CategoryType.CLASS
        )

        assert class_file.parent == class_dir


class TestMemberDirectoryBuilders:
    """Test member directory path construction."""

    def test_get_constructors_dir(self):
        """Verify constructors directory structure."""
        class_dir = Path("/output/api/material/classes/ListTile")
        result = get_constructors_dir(class_dir)
        assert result == class_dir / "constructors"
        assert result.name == "constructors"

    def test_get_properties_native_dir(self):
        """Verify native properties use properties/native structure."""
        class_dir = Path("/output/api/material/classes/ListTile")
        result = get_properties_native_dir(class_dir)
        assert result == class_dir / "properties" / "native"
        assert "properties" in result.parts
        assert "native" in result.parts
        assert result.parent.name == "properties"

    def test_get_properties_inherited_dir(self):
        """Verify inherited properties use properties/inherited structure."""
        class_dir = Path("/output/api/material/classes/InkWell")
        result = get_properties_inherited_dir(class_dir)
        assert result == class_dir / "properties" / "inherited"
        assert "inherited" in result.parts
        assert result.name == "inherited"

    def test_get_methods_native_dir(self):
        """Verify native methods use methods/native structure."""
        class_dir = Path("/output/api/widgets/classes/State")
        result = get_methods_native_dir(class_dir)
        assert result == class_dir / "methods" / "native"
        assert result.parent.name == "methods"
        assert result.name == "native"

    def test_get_methods_inherited_dir(self):
        """Verify inherited methods use methods/inherited structure."""
        class_dir = Path("/output/api/widgets/classes/Text")
        result = get_methods_inherited_dir(class_dir)
        assert result == class_dir / "methods" / "inherited"
        assert "methods" in result.parts
        assert "inherited" in result.parts

    def test_get_operators_native_dir(self):
        """Verify native operators use operators/native structure."""
        class_dir = Path("/output/api/material/classes/Color")
        result = get_operators_native_dir(class_dir)
        assert result == class_dir / "operators" / "native"
        assert result.parent.name == "operators"

    def test_get_operators_inherited_dir(self):
        """Verify inherited operators use operators/inherited structure."""
        class_dir = Path("/output/api/material/classes/Color")
        result = get_operators_inherited_dir(class_dir)
        assert result == class_dir / "operators" / "inherited"
        assert result.name == "inherited"

    def test_get_statics_dir(self):
        """Verify statics directory structure."""
        class_dir = Path("/output/api/material/classes/Colors")
        result = get_statics_dir(class_dir)
        assert result == class_dir / "statics"
        assert result.name == "statics"

    def test_get_snippets_output_dir(self):
        """Verify snippets directory structure."""
        class_dir = Path("/output/api/widgets/classes/TextField")
        result = get_snippets_output_dir(class_dir)
        assert result == class_dir / "snippets"
        assert result.name == "snippets"


class TestMemberFileBuilders:
    """Test member file path construction."""

    def test_get_native_member_file(self):
        """Verify native member filename structure."""
        native_dir = Path("/output/api/material/classes/ListTile/properties/native")
        result = get_native_member_file(native_dir, "title")
        assert result == native_dir / "title.md"
        assert result.name == "title.md"
        assert result.suffix == ".md"

    def test_get_inherited_member_file_format(self):
        """Verify inherited member filename uses triple-underscore separator."""
        inherited_dir = Path(
            "/output/api/material/classes/InkWell/properties/inherited"
        )
        result = get_inherited_member_file(
            inherited_dir, "widgets", "Widget", "hashCode"
        )
        assert result.name == "widgets___Widget___hashCode.md"
        assert "___" in result.name
        assert result.suffix == ".md"

    def test_inherited_filename_parts_extractable(self):
        """Verify we can extract source section/class from inherited filename."""
        inherited_dir = Path("/any/path")
        result = get_inherited_member_file(
            inherited_dir, "dart-core", "Object", "toString"
        )
        parts = result.stem.split("___")
        assert parts == ["dart-core", "Object", "toString"]
        assert len(parts) == 3

    def test_get_snippet_output_file(self):
        """Verify snippet output filename structure."""
        snippets_dir = Path("/output/api/material/classes/Card/snippets")
        result = get_snippet_output_file(snippets_dir, "material.Card.1")
        assert result == snippets_dir / "material.Card.1.md"
        assert result.name == "material.Card.1.md"
        assert result.suffix == ".md"


class TestStructureChangePropagation:
    """Test that structure changes in paths.py propagate correctly."""

    def test_changing_classes_subdir_name_propagates(self):
        """If 'classes' subdir name changes, all class paths should reflect it."""
        output_dir = Path("/output")
        section = "material"
        class_name = "Button"

        class_dir = get_entity_dir(output_dir, section, class_name, CategoryType.CLASS)
        class_file = get_entity_file(
            output_dir, section, class_name, CategoryType.CLASS
        )

        # Both should include the 'classes' subdirectory
        assert "classes" in class_dir.parts
        assert "classes" in class_file.parts

        # class_file parent should equal class_dir
        assert class_file.parent == class_dir

    def test_changing_api_root_name_propagates(self):
        """If 'api' root dir name changes, all paths should reflect it."""
        output_dir = Path("/output")

        api_root = get_api_root_dir(output_dir)
        api_section = get_api_section_dir(output_dir, "widgets")
        class_dir = get_entity_dir(output_dir, "widgets", "Text", CategoryType.CLASS)

        # All should start with the same api root
        assert api_section.parts[: len(api_root.parts)] == api_root.parts
        assert class_dir.parts[: len(api_root.parts)] == api_root.parts

    def test_member_dirs_relative_to_class_dir(self):
        """Verify all member dirs are constructed relative to class_dir."""
        class_dir = Path("/output/api/material/classes/Widget")

        constructors = get_constructors_dir(class_dir)
        props_native = get_properties_native_dir(class_dir)
        props_inherited = get_properties_inherited_dir(class_dir)
        methods_native = get_methods_native_dir(class_dir)
        methods_inherited = get_methods_inherited_dir(class_dir)
        ops_native = get_operators_native_dir(class_dir)
        ops_inherited = get_operators_inherited_dir(class_dir)
        statics = get_statics_dir(class_dir)
        snippets = get_snippets_output_dir(class_dir)

        # All should be children of class_dir
        for member_dir in [
            constructors,
            props_native,
            props_inherited,
            methods_native,
            methods_inherited,
            ops_native,
            ops_inherited,
            statics,
            snippets,
        ]:
            assert class_dir in member_dir.parents


class TestInputPathBuilders:
    """Test input path construction."""

    def test_get_input_section_dir_uses_flutter_subdir(self):
        """Verify input paths include 'flutter' subdirectory."""
        doc_dir = Path("/docs")
        result = get_input_section_dir(doc_dir, "material")
        assert result == Path("/docs/flutter/material")
        assert "flutter" in result.parts

    def test_get_input_class_file_structure(self):
        """Verify input class file path structure."""
        doc_dir = Path("/docs")
        result = get_input_class_file(doc_dir, "widgets", "Text")
        assert result == Path("/docs/flutter/widgets/Text-class.html")
        assert result.suffix == ".html"
        assert result.name == "Text-class.html"

    def test_get_input_member_file_structure(self):
        """Verify input member file path structure."""
        doc_dir = Path("/docs")
        result = get_input_member_file(doc_dir, "widgets", "Text", "build")
        assert result == Path("/docs/flutter/widgets/Text/build.html")
        assert result.suffix == ".html"
        assert result.name == "build.html"

    def test_get_input_snippets_dir_structure(self):
        """Verify input snippets directory structure."""
        doc_dir = Path("/docs")
        result = get_input_snippets_dir(doc_dir)
        assert result == Path("/docs/snippets")
        assert result.name == "snippets"


class TestEnsureDirExists:
    """Test ensure_dir_exists utility function."""

    def test_ensure_dir_exists_creates_directory(self, tmp_path: Path):
        """Verify ensure_dir_exists creates directory."""
        new_dir = tmp_path / "test" / "nested" / "path"
        assert not new_dir.exists()

        result = ensure_dir_exists(new_dir)

        assert new_dir.exists()
        assert new_dir.is_dir()
        assert result == new_dir

    def test_ensure_dir_exists_with_existing_dir(self, tmp_path: Path):
        """Verify ensure_dir_exists works with existing directory."""
        existing_dir = tmp_path / "existing"
        existing_dir.mkdir()

        result = ensure_dir_exists(existing_dir)

        assert result == existing_dir
        assert existing_dir.exists()

    def test_ensure_dir_exists_creates_parents(self, tmp_path: Path):
        """Verify ensure_dir_exists creates parent directories."""
        deep_path = tmp_path / "a" / "b" / "c" / "d" / "e"
        result = ensure_dir_exists(deep_path)

        assert result == deep_path
        assert deep_path.exists()
        assert (tmp_path / "a").exists()
        assert (tmp_path / "a" / "b").exists()
        assert (tmp_path / "a" / "b" / "c").exists()


class TestPathConsistency:
    """Test consistency between related path functions."""

    def test_class_file_within_class_dir(self):
        """Verify class file is always within class directory."""
        test_cases = [
            ("/output", "material", "Button"),
            ("/root/output", "widgets", "Text"),
            ("/tmp/docs", "dart-core", "Object"),
        ]

        for output_dir, section, class_name in test_cases:
            output_path = Path(output_dir)
            class_dir = get_entity_dir(
                output_path, section, class_name, CategoryType.CLASS
            )
            class_file = get_entity_file(
                output_path, section, class_name, CategoryType.CLASS
            )

            assert class_file.parent == class_dir, (
                f"class_file parent {class_file.parent} != class_dir {class_dir}"
            )

    def test_section_within_api_root(self):
        """Verify section directory is always within api root."""
        output_dir = Path("/output")
        sections = ["material", "widgets", "dart-core", "dart-async"]

        api_root = get_api_root_dir(output_dir)

        for section in sections:
            section_dir = get_api_section_dir(output_dir, section)
            assert section_dir.parent == api_root

    def test_class_within_section(self):
        """Verify class directory is within section directory."""
        output_dir = Path("/output")
        section = "material"
        class_name = "Card"

        section_dir = get_api_section_dir(output_dir, section)
        class_dir = get_entity_dir(output_dir, section, class_name, CategoryType.CLASS)

        # class_dir should be descendant of section_dir
        assert section_dir in class_dir.parents
