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
        result = builder.get_inherited_property_file("key")
        assert result == Path(
            "/output/api/material/classes/ListTile/properties/inherited/key.md"
        )

    def test_get_constructors_dir(self):
        """Verify constructors directory construction (no native/inherited split)."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_constructors_dir()
        assert result == Path("/output/api/material/classes/ListTile/constructors")
        assert "constructors" in result.parts

    def test_get_methods_dir_native(self):
        """Verify native methods directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_methods_dir(inherited=False)
        assert result == Path("/output/api/material/classes/ListTile/methods/native")
        assert "methods" in result.parts
        assert "native" in result.parts

    def test_get_methods_dir_inherited(self):
        """Verify inherited methods directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_methods_dir(inherited=True)
        assert result == Path("/output/api/material/classes/ListTile/methods/inherited")
        assert "methods" in result.parts
        assert "inherited" in result.parts

    def test_get_operators_dir_native(self):
        """Verify native operators directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="InkWell",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_operators_dir(inherited=False)
        assert result == Path("/output/api/material/classes/InkWell/operators/native")
        assert "operators" in result.parts
        assert "native" in result.parts

    def test_get_operators_dir_inherited(self):
        """Verify inherited operators directory construction."""
        builder = PathBuilder(
            section="material",
            entity_name="InkWell",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_operators_dir(inherited=True)
        assert result == Path(
            "/output/api/material/classes/InkWell/operators/inherited"
        )
        assert "operators" in result.parts
        assert "inherited" in result.parts

    def test_get_statics_dir(self):
        """Verify statics directory construction (no native/inherited split)."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_statics_dir()
        assert result == Path("/output/api/material/classes/ListTile/statics")
        assert "statics" in result.parts

    def test_get_constants_dir(self):
        """Verify constants directory construction (no native/inherited split)."""
        builder = PathBuilder(
            section="material",
            entity_name="HourFormat",
            entity_type=CategoryType.ENUM,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_constants_dir()
        assert result == Path("/output/api/material/enums/HourFormat/constants")
        assert "constants" in result.parts

    def test_get_snippets_dir(self):
        """Verify snippets directory construction (no native/inherited split)."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_snippets_dir()
        assert result == Path("/output/api/material/classes/ListTile/snippets")
        assert "snippets" in result.parts

    def test_get_constructor_file(self):
        """Verify constructor file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="InkWell",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_constructor_file("InkWell")
        assert result == Path(
            "/output/api/material/classes/InkWell/constructors/InkWell.md"
        )
        assert result.suffix == ".md"

    def test_get_native_method_file(self):
        """Verify native method file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_native_method_file("build")
        assert result == Path(
            "/output/api/material/classes/ListTile/methods/native/build.md"
        )
        assert result.suffix == ".md"

    def test_get_native_operator_file(self):
        """Verify native operator file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="InkWell",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_native_operator_file("operator_equals")
        assert result == Path(
            "/output/api/material/classes/InkWell/operators/native/operator_equals.md"
        )
        assert result.suffix == ".md"

    def test_get_inherited_method_file(self):
        """Verify inherited method file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="InkWell",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_inherited_method_file("build")
        assert result == Path(
            "/output/api/material/classes/InkWell/methods/inherited/build.md"
        )

    def test_get_inherited_operator_file(self):
        """Verify inherited operator file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="InkWell",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_inherited_operator_file("operator_equals")
        assert result == Path(
            "/output/api/material/classes/InkWell/operators/inherited/operator_equals.md"
        )

    def test_get_static_file(self):
        """Verify static file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_static_file("staticMethod")
        assert result == Path(
            "/output/api/material/classes/ListTile/statics/staticMethod.md"
        )
        assert result.suffix == ".md"

    def test_get_constant_file(self):
        """Verify constant file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="HourFormat",
            entity_type=CategoryType.ENUM,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_constant_file("values")
        assert result == Path(
            "/output/api/material/enums/HourFormat/constants/values.md"
        )
        assert result.suffix == ".md"

    def test_get_snippet_file(self):
        """Verify snippet file path construction."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_snippet_file("2")
        assert result == Path("/output/api/material/classes/ListTile/snippets/2.md")
        assert result.suffix == ".md"

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

    def test_get_input_constant_file(self):
        """Verify input constant file path construction with -constant.html suffix."""
        builder = PathBuilder(
            section="material",
            entity_name="HourFormat",
            entity_type=CategoryType.ENUM,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        result = builder.get_input_constant_file("values")
        assert result == Path("/doc/flutter/material/HourFormat/values-constant.html")

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

    def test_entity_type_mapping_constant(self):
        """Verify CONSTANT type maps to 'constants' directory."""
        builder = PathBuilder(
            section="material",
            entity_name="kBottomNavigationBarHeight",
            entity_type=CategoryType.CONSTANT,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "constants" in entity_dir.parts

    def test_entity_type_mapping_library(self):
        """Verify LIBRARY type maps to 'libraries' directory."""
        builder = PathBuilder(
            section="material",
            entity_name="material",
            entity_type=CategoryType.LIBRARY,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "libraries" in entity_dir.parts

    def test_entity_type_mapping_extension_type(self):
        """Verify EXTENSION_TYPE type maps to 'extension_types' directory."""
        builder = PathBuilder(
            section="widgets",
            entity_name="OverlayChildLayoutInfo",
            entity_type=CategoryType.EXTENSION_TYPE,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "extension_types" in entity_dir.parts

    def test_entity_type_mapping_extension(self):
        """Verify EXTENSION type maps to 'extensions' directory."""
        builder = PathBuilder(
            section="widgets",
            entity_name="WidgetStateOperators",
            entity_type=CategoryType.EXTENSION,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "extensions" in entity_dir.parts

    def test_entity_type_mapping_function(self):
        """Verify FUNCTION type maps to 'functions' directory."""
        builder = PathBuilder(
            section="material",
            entity_name="showBottomSheet",
            entity_type=CategoryType.FUNCTION,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "functions" in entity_dir.parts

    def test_entity_type_mapping_typedef(self):
        """Verify TYPEDEF type maps to 'typedefs' directory."""
        builder = PathBuilder(
            section="material",
            entity_name="DrawerCallback",
            entity_type=CategoryType.TYPEDEF,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )
        entity_dir = builder.get_entity_dir()
        assert "typedefs" in entity_dir.parts

    def test_directory_only_pathbuilder(self):
        """Test PathBuilder without entity context for directory operations."""
        builder = PathBuilder(
            section="widgets",
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )

        # These should work without entity context
        assert builder.get_api_root_dir() == Path("/output/api")
        assert builder.get_api_section_dir() == Path("/output/api/widgets")
        assert builder.get_input_flutter_dir() == Path("/doc/flutter")
        assert builder.get_input_section_dir() == Path("/doc/flutter/widgets")
        assert builder.get_input_snippets_dir() == Path("/doc/snippets")

    def test_entity_methods_require_context(self):
        """Test that entity-dependent methods raise ValueError without context."""
        import pytest

        builder = PathBuilder(
            section="widgets",
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )

        # All these should raise ValueError
        with pytest.raises(ValueError, match="requires entity context"):
            builder.get_entity_dir()

        with pytest.raises(ValueError, match="requires entity context"):
            builder.get_entity_file()

        with pytest.raises(ValueError, match="requires entity context"):
            builder.get_constructors_dir()

        with pytest.raises(ValueError, match="requires entity context"):
            builder.get_properties_dir()

        with pytest.raises(ValueError, match="requires entity context"):
            builder.get_native_property_file("selected")

        with pytest.raises(ValueError, match="requires entity context"):
            builder.get_input_entity_file()

        with pytest.raises(ValueError, match="requires entity context"):
            builder.get_input_member_file("build")

    def test_partial_entity_context_validation(self):
        """Test that providing only entity_name or only entity_type raises ValueError."""
        import pytest

        # Only entity_name provided
        with pytest.raises(ValueError, match="must both be provided or both be None"):
            PathBuilder(
                section="widgets",
                doc_dir=Path("/doc"),
                output_dir=Path("/output"),
                entity_name="Text",
            )

        # Only entity_type provided
        with pytest.raises(ValueError, match="must both be provided or both be None"):
            PathBuilder(
                section="widgets",
                doc_dir=Path("/doc"),
                output_dir=Path("/output"),
                entity_type=CategoryType.CLASS,
            )

    def test_full_entity_context_works(self):
        """Test that all methods work when full entity context provided."""
        builder = PathBuilder(
            section="material",
            entity_name="ListTile",
            entity_type=CategoryType.CLASS,
            doc_dir=Path("/doc"),
            output_dir=Path("/output"),
        )

        # Directory methods still work
        assert builder.get_api_root_dir() == Path("/output/api")

        # Entity methods work
        assert builder.get_entity_dir() == Path("/output/api/material/classes/ListTile")
        assert builder.get_entity_file() == Path(
            "/output/api/material/classes/ListTile/ListTile.md"
        )
        assert builder.get_properties_dir() == Path(
            "/output/api/material/classes/ListTile/properties/native"
        )
