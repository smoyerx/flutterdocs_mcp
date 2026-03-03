"""Unit tests for conversion functions."""

from pathlib import Path

import pytest

from flutterdocs.convert.conversion import convert_dart_snippet


class TestConvertDartSnippet:
    """Tests for convert_dart_snippet function."""

    def test_wraps_dart_code_in_code_fence(self, tmp_path: Path) -> None:
        """Should produce exactly ```dart\\n{content}\\n```."""
        dart_code = "void main() {\n  print('Hello');\n}"
        dart_file = tmp_path / "snippet.dart"
        dart_file.write_text(dart_code, encoding="utf-8")

        result = convert_dart_snippet(dart_file)

        assert result == f"```dart\n{dart_code}\n```\n"

    def test_raises_error_for_nonexistent_file(self, tmp_path: Path) -> None:
        """Should raise FileNotFoundError if Dart file doesn't exist."""
        dart_file = tmp_path / "nonexistent.dart"

        with pytest.raises(FileNotFoundError) as exc_info:
            convert_dart_snippet(dart_file)

        assert "Dart file not found" in str(exc_info.value)
