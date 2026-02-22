"""Unit tests for _shared/paths.py standalone helper functions."""

from pathlib import Path

import pytest

from flutterdocs._shared.paths import read_section_list


class TestReadSectionList:
    """Tests for the read_section_list helper."""

    def test_returns_section_names(self, tmp_path: Path) -> None:
        """Valid lines are returned in order."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\nwidgets\n", encoding="utf-8")
        result = read_section_list(section_file)
        assert result == ["material", "widgets"]

    def test_blank_lines_are_ignored(self, tmp_path: Path) -> None:
        """Blank lines between or around section names are stripped."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("\nmaterial\n\nwidgets\n\n", encoding="utf-8")
        result = read_section_list(section_file)
        assert result == ["material", "widgets"]

    def test_comment_lines_are_ignored(self, tmp_path: Path) -> None:
        """Lines whose first non-whitespace character is '#' are ignored."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text(
            "# This is a comment\nmaterial\n# another comment\nwidgets\n",
            encoding="utf-8",
        )
        result = read_section_list(section_file)
        assert result == ["material", "widgets"]

    def test_mixed_blanks_and_comments(self, tmp_path: Path) -> None:
        """Blank lines AND comment lines are both ignored together."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text(
            "\n# header\n\nmaterial\n\n# divider\nwidgets\n",
            encoding="utf-8",
        )
        result = read_section_list(section_file)
        assert result == ["material", "widgets"]

    def test_all_blanks_and_comments_returns_empty(self, tmp_path: Path) -> None:
        """A file with only blanks/comments returns an empty list."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text(
            "# only comments\n\n# more comments\n", encoding="utf-8"
        )
        result = read_section_list(section_file)
        assert result == []

    def test_empty_file_returns_empty(self, tmp_path: Path) -> None:
        """An entirely empty file returns an empty list."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("", encoding="utf-8")
        result = read_section_list(section_file)
        assert result == []

    def test_single_section_returned(self, tmp_path: Path) -> None:
        """A file with exactly one section returns a one-element list."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\n", encoding="utf-8")
        result = read_section_list(section_file)
        assert result == ["material"]

    def test_whitespace_stripped_from_names(self, tmp_path: Path) -> None:
        """Leading/trailing whitespace on section names is stripped."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("  material  \n\twidgets\t\n", encoding="utf-8")
        result = read_section_list(section_file)
        assert result == ["material", "widgets"]

    def test_nonexistent_file_raises_file_not_found(self, tmp_path: Path) -> None:
        """FileNotFoundError is raised when the path does not exist."""
        missing = tmp_path / "does_not_exist.txt"
        with pytest.raises(FileNotFoundError):
            read_section_list(missing)

    def test_preserves_order(self, tmp_path: Path) -> None:
        """Section names are returned in the same order as the file."""
        names = ["animation", "cupertino", "material", "painting", "widgets"]
        section_file = tmp_path / "sections.txt"
        section_file.write_text("\n".join(names) + "\n", encoding="utf-8")
        result = read_section_list(section_file)
        assert result == names
