"""Unit tests for PathBuilder class."""

from pathlib import Path

from flutterdoc_gen.convert.constants import CategoryType
from flutterdoc_gen.convert.paths import PathBuilder


class TestPathBuilder:
    """Test PathBuilder construction and path generation."""

    def test_builder_creation(self):
        """Verify PathBuilder can be instantiated."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        assert builder.section == "material"
        assert builder.entity_name == "ListTile"
        assert builder.entity_type == CategoryType.CLASS

    def test_get_api_root_dir(self):
        """Verify API root directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_api_root_dir()
        assert result == Path("/output/api")

    def test_get_api_section_dir(self):
        """Verify API section directory construction."""
        builder = PathBuilder(
            section="widgets",
            entity_name="Text",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_api_section_dir()
        assert result == Path("/output/api/widgets")

    def test_get_entity_dir(self):
        """Verify entity directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_entity_dir()
        assert result == Path("/output/api/material/classes/ListTile")
        assert "classes" in result.parts

    def test_get_entity_file(self):
        """Verify entity file path construction."""
        builder = PathBuilder(
            section="widgets",
            entity_name="Text",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_entity_file()
        assert result == Path("/output/api/widgets/classes/Text/Text.md")
        assert result.suffix == ".md"

    def test_get_properties_dir_native(self):
        """Verify native properties directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_properties_dir(inherited=False)
        assert result == Path("/output/api/material/classes/ListTile/properties/native")

    def test_get_properties_dir_inherited(self):
        """Verify inherited properties directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_properties_dir(inherited=True)
        assert result == Path(
            "/output/api/material/classes/ListTile/properties/inherited"
        )

    def test_get_native_property_file(self):
        """Verify native property file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_native_property_file("selected")
        assert result == Path(
            "/output/api/material/classes/ListTile/properties/native/selected.md"
        )

    def test_get_inherited_property_file(self):
        """Verify inherited property file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_inherited_property_file("widgets", "Widget", "key")
        assert result == Path(
            "/output/api/material/classes/ListTile/properties/inherited/widgets___Widget___key.md"
        )
        assert "___" in result.name

    def test_get_input_section_dir(self):
        """Verify input section directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_input_section_dir()
        assert result == Path("/doc/flutter/material")

    def test_get_input_member_file(self):
        """Verify input member file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_input_member_file("build")
        assert result == Path("/doc/flutter/material/ListTile/build.html")

    def test_entity_type_mapping_class(self):
        """Verify CLASS type maps to 'classes' directory."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "classes" in entity_dir.parts

    def test_entity_type_mapping_mixin(self):
        """Verify MIXIN type maps to 'mixins' directory."""
        builder = PathBuilder(
            section="material",
            entity_name="SomeMixin",
            entity_type=CategoryType.MIXIN,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "mixins" in entity_dir.parts

    def test_entity_type_mapping_enum(self):
        """Verify ENUM type maps to 'enums' directory."""
        builder = PathBuilder(
            section="material",
            entity_name="HourFormat",
            entity_type=CategoryType.ENUM,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "enums" in entity_dir.parts
