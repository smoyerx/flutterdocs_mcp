"""Unit tests for conversion functions."""

from pathlib import Path

import pytest

from flutterdoc_gen.convert.conversion import convert_dart_snippet


class TestConvertDartSnippet:
    """Tests for convert_dart_snippet function."""

    def test_wraps_dart_code_in_code_block(self, tmp_path: Path) -> None:
        """Should wrap Dart code in markdown code block with dart language marker."""
        dart_file = tmp_path / "snippet.dart"
        dart_file.write_text("void main() {\n  print('Hello');\n}", encoding="utf-8")

        result = convert_dart_snippet(dart_file, "Widget", "widgets")

        assert result.startswith("# Code Snippet for Widget in widgets")
        assert "```dart" in result
        assert "void main() {" in result
        assert "print('Hello');" in result
        assert result.endswith("```")

    def test_includes_class_name_and_section_in_header(self, tmp_path: Path) -> None:
        """Header should include class name and section."""
        dart_file = tmp_path / "snippet.dart"
        dart_file.write_text("// Sample code", encoding="utf-8")

        result = convert_dart_snippet(dart_file, "ListTile", "material")

        assert "# Code Snippet for ListTile in material" in result

    def test_preserves_dart_code_unchanged(self, tmp_path: Path) -> None:
        """Dart code content should be preserved exactly as-is."""
        dart_code = (
            "import 'package:flutter/material.dart';\n\nvoid main() => runApp(MyApp());"
        )
        dart_file = tmp_path / "snippet.dart"
        dart_file.write_text(dart_code, encoding="utf-8")

        result = convert_dart_snippet(dart_file, "MyApp", "widgets")

        # Code should appear between ```dart and ```
        assert f"```dart\n{dart_code}\n```" in result

    def test_handles_empty_dart_file(self, tmp_path: Path) -> None:
        """Should handle empty Dart files correctly."""
        dart_file = tmp_path / "empty.dart"
        dart_file.write_text("", encoding="utf-8")

        result = convert_dart_snippet(dart_file, "Empty", "widgets")

        assert "# Code Snippet for Empty in widgets" in result
        assert "```dart\n\n```" in result

    def test_handles_multiline_dart_code(self, tmp_path: Path) -> None:
        """Should handle multiline Dart code correctly."""
        dart_code = """class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}"""
        dart_file = tmp_path / "widget.dart"
        dart_file.write_text(dart_code, encoding="utf-8")

        result = convert_dart_snippet(dart_file, "MyWidget", "widgets")

        assert "class MyWidget extends StatelessWidget {" in result
        assert "@override" in result
        assert "Widget build(BuildContext context) {" in result
        assert "return Container();" in result

    def test_raises_error_for_nonexistent_file(self, tmp_path: Path) -> None:
        """Should raise FileNotFoundError if Dart file doesn't exist."""
        dart_file = tmp_path / "nonexistent.dart"

        with pytest.raises(FileNotFoundError) as exc_info:
            convert_dart_snippet(dart_file, "Widget", "widgets")

        assert "Dart file not found" in str(exc_info.value)

    def test_handles_dart_code_with_special_characters(self, tmp_path: Path) -> None:
        """Should handle Dart code with special markdown characters."""
        dart_code = 'String msg = "Use `backticks` and *asterisks*";'
        dart_file = tmp_path / "special.dart"
        dart_file.write_text(dart_code, encoding="utf-8")

        result = convert_dart_snippet(dart_file, "Special", "widgets")

        # Special characters should be preserved within code block
        assert dart_code in result
        assert "```dart" in result

    def test_output_format(self, tmp_path: Path) -> None:
        """Should produce correct markdown format."""
        dart_file = tmp_path / "test.dart"
        dart_file.write_text("// test", encoding="utf-8")

        result = convert_dart_snippet(dart_file, "Test", "widgets")

        lines = result.split("\n")
        assert lines[0] == "# Code Snippet for Test in widgets"
        assert lines[1] == ""
        assert lines[2] == "```dart"
        assert lines[3] == "// test"
        assert lines[4] == "```"
