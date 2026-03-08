"""Unit tests for processor functions.

Tests that inherited properties, methods, and operators with empty descriptions
are handled gracefully without fatal exit.
"""

from pathlib import Path


from flutterdocs._shared.constants import CategoryType
from flutterdocs._shared.paths import PathBuilder
from flutterdocs.convert.processors import (
    process_methods,
    process_operators,
    process_properties,
)


def _make_builder(tmp_path: Path) -> PathBuilder:
    """Create a PathBuilder for TlsException in dart-io."""
    return PathBuilder(
        section="dart-io",
        output_dir=tmp_path,
        entity_name="TlsException",
        entity_type=CategoryType.CLASS,
    )


class TestProcessPropertiesEmptyDescription:
    """Tests for process_properties with an inherited property that has no description."""

    def test_does_not_exit(self, tmp_path: Path) -> None:
        """Inherited property with empty description should not cause fatal exit."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Properties\n"
            "\n"
            "[hashCode](flutter-docs://api/dart-core/Object/hashCode) → int\n"
        )
        # Should complete without raising SystemExit
        process_properties(entity_markdown, builder, None)  # type: ignore[arg-type]

    def test_output_file_created(self, tmp_path: Path) -> None:
        """Inherited property with empty description should produce an output file."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Properties\n"
            "\n"
            "[hashCode](flutter-docs://api/dart-core/Object/hashCode) → int\n"
        )
        process_properties(entity_markdown, builder, None)  # type: ignore[arg-type]
        output_file = builder.get_inherited_property_file("hashCode")
        assert output_file.exists()

    def test_output_file_content(self, tmp_path: Path) -> None:
        """Inherited property file with empty description should have valid markdown."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Properties\n"
            "\n"
            "[hashCode](flutter-docs://api/dart-core/Object/hashCode) → int\n"
        )
        process_properties(entity_markdown, builder, None)  # type: ignore[arg-type]
        content = builder.get_inherited_property_file("hashCode").read_text(
            encoding="utf-8"
        )
        assert content.startswith("# hashCode property")
        assert "This property is inherited from" in content


class TestProcessMethodsEmptyDescription:
    """Tests for process_methods with an inherited method that has no description."""

    def test_does_not_exit(self, tmp_path: Path) -> None:
        """Inherited method with empty description should not cause fatal exit."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Methods\n"
            "\n"
            "[noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod) → dynamic\n"
        )
        process_methods(entity_markdown, builder, None)  # type: ignore[arg-type]

    def test_output_file_created(self, tmp_path: Path) -> None:
        """Inherited method with empty description should produce an output file."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Methods\n"
            "\n"
            "[noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod) → dynamic\n"
        )
        process_methods(entity_markdown, builder, None)  # type: ignore[arg-type]
        output_file = builder.get_inherited_method_file("noSuchMethod")
        assert output_file.exists()

    def test_output_file_content(self, tmp_path: Path) -> None:
        """Inherited method file with empty description should have valid markdown."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Methods\n"
            "\n"
            "[noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod) → dynamic\n"
        )
        process_methods(entity_markdown, builder, None)  # type: ignore[arg-type]
        content = builder.get_inherited_method_file("noSuchMethod").read_text(
            encoding="utf-8"
        )
        assert content.startswith("# noSuchMethod method")
        assert "This method is inherited from" in content


class TestProcessOperatorsEmptyDescription:
    """Tests for process_operators with an inherited operator that has no description."""

    def test_does_not_exit(self, tmp_path: Path) -> None:
        """Inherited operator with empty description should not cause fatal exit."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Operators\n"
            "\n"
            "[operator ==](flutter-docs://api/dart-core/Object/operator_equals) → bool\n"
        )
        process_operators(entity_markdown, builder, None)  # type: ignore[arg-type]

    def test_output_file_created(self, tmp_path: Path) -> None:
        """Inherited operator with empty description should produce an output file."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Operators\n"
            "\n"
            "[operator ==](flutter-docs://api/dart-core/Object/operator_equals) → bool\n"
        )
        process_operators(entity_markdown, builder, None)  # type: ignore[arg-type]
        output_file = builder.get_inherited_operator_file("operator_equals")
        assert output_file.exists()

    def test_output_file_content(self, tmp_path: Path) -> None:
        """Inherited operator file with empty description should have valid markdown."""
        builder = _make_builder(tmp_path)
        entity_markdown = (
            "## Operators\n"
            "\n"
            "[operator ==](flutter-docs://api/dart-core/Object/operator_equals) → bool\n"
        )
        process_operators(entity_markdown, builder, None)  # type: ignore[arg-type]
        content = builder.get_inherited_operator_file("operator_equals").read_text(
            encoding="utf-8"
        )
        assert content.startswith("# operator == (operator_equals)")
        assert "This operator is inherited from" in content
