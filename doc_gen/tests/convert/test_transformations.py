# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pytest>=8.0.0",
#     "markitdown>=0.1.4",
# ]
# ///
"""Unit tests for transformation functions in convert.py."""

import sys
from pathlib import Path

# Add parent directory to path to import convert module
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from convert import remove_header, remove_footer, remove_html_links



class TestRemoveHeader:
    """Tests for remove_header transformation function."""

    def test_removes_lines_before_first_heading(self) -> None:
        """Content before the first heading should be removed."""
        content = "Some preamble\nMore preamble\n# Heading\nBody content"
        result = remove_header(content)
        assert result == "# Heading\nBody content"

    def test_preserves_content_starting_with_heading(self) -> None:
        """Content that starts with a heading should be unchanged."""
        content = "# Heading\nBody content\n## Subheading"
        result = remove_header(content)
        assert result == content

    def test_handles_h2_as_first_heading(self) -> None:
        """Should work with any heading level as first heading."""
        content = "Preamble\n## H2 Heading\nContent"
        result = remove_header(content)
        assert result == "## H2 Heading\nContent"

    def test_handles_h6_as_first_heading(self) -> None:
        """Should work with h6 as first heading."""
        content = "Preamble\n###### H6 Heading\nContent"
        result = remove_header(content)
        assert result == "###### H6 Heading\nContent"

    def test_returns_original_when_no_heading(self) -> None:
        """Content without any heading should be returned unchanged."""
        content = "No headings here\nJust text"
        result = remove_header(content)
        assert result == content

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = remove_header("")
        assert result == ""

    def test_handles_heading_only(self) -> None:
        """Single heading with no other content."""
        content = "# Just a heading"
        result = remove_header(content)
        assert result == "# Just a heading"

    def test_preserves_multiple_headings(self) -> None:
        """All headings after the first should be preserved."""
        content = "Preamble\n# First\n## Second\n### Third"
        result = remove_header(content)
        assert result == "# First\n## Second\n### Third"

    def test_handles_hash_in_code_block_before_heading(self) -> None:
        """Hash symbols in code blocks should not be treated as headings."""
        # This tests a potential edge case - a # that's not at line start
        content = "Some text with a `#hash` tag\n# Real Heading\nContent"
        result = remove_header(content)
        # The # in `#hash` is not at line start, so # Real Heading is first
        assert result == "# Real Heading\nContent"


class TestRemoveFooter:
    """Tests for remove_footer transformation function."""

    def test_removes_footer_content(self) -> None:
        """Content from footer marker to end should be removed."""
        content = "# Heading\nBody\n1. [Flutter](index.html)\nFooter stuff"
        result = remove_footer(content)
        assert result == "# Heading\nBody"

    def test_preserves_content_without_footer_marker(self) -> None:
        """Content without footer marker should be unchanged."""
        content = "# Heading\nBody content\nMore content"
        result = remove_footer(content)
        assert result == content

    def test_handles_marker_at_start(self) -> None:
        """Footer marker at start of content removes everything."""
        content = "1. [Flutter](index.html)\nAll footer"
        result = remove_footer(content)
        assert result == ""

    def test_handles_marker_with_surrounding_whitespace(self) -> None:
        """Footer marker detection works with surrounding content on line."""
        content = "Body\n   1. [Flutter](index.html)   \nFooter"
        result = remove_footer(content)
        assert result == "Body"

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = remove_footer("")
        assert result == ""

    def test_removes_trailing_whitespace(self) -> None:
        """Trailing whitespace before footer should be stripped."""
        content = "# Heading\nBody\n\n\n1. [Flutter](index.html)"
        result = remove_footer(content)
        assert result == "# Heading\nBody"

    def test_handles_marker_as_only_content(self) -> None:
        """Just the footer marker should result in empty string."""
        content = "1. [Flutter](index.html)"
        result = remove_footer(content)
        assert result == ""


class TestRemoveHtmlLinks:
    """Tests for remove_html_links transformation function."""

    def test_removes_simple_html_link(self) -> None:
        """Simple HTML link should be replaced with just link text."""
        content = "See [SomeClass](SomeClass-class.html) for details."
        result = remove_html_links(content)
        assert result == "See SomeClass for details."

    def test_removes_link_with_path(self) -> None:
        """HTML link with path should be replaced."""
        content = "Check [Widget](widgets/Widget-class.html) here."
        result = remove_html_links(content)
        assert result == "Check Widget here."

    def test_removes_multiple_links(self) -> None:
        """Multiple HTML links should all be replaced."""
        content = "[Class1](a.html) and [Class2](b.html) are related."
        result = remove_html_links(content)
        assert result == "Class1 and Class2 are related."

    def test_preserves_non_html_links(self) -> None:
        """Links to non-HTML files should be preserved."""
        content = "See [image](picture.png) and [doc](file.pdf)."
        result = remove_html_links(content)
        assert result == "See [image](picture.png) and [doc](file.pdf)."

    def test_preserves_external_urls(self) -> None:
        """External URLs should be preserved."""
        content = "Visit [Flutter](https://flutter.dev) for more."
        result = remove_html_links(content)
        assert result == "Visit [Flutter](https://flutter.dev) for more."

    def test_handles_link_text_with_spaces(self) -> None:
        """Link text with spaces should be preserved."""
        content = "[Some Long Class Name](class.html)"
        result = remove_html_links(content)
        assert result == "Some Long Class Name"

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = remove_html_links("")
        assert result == ""

    def test_handles_no_links(self) -> None:
        """Content without links should be unchanged."""
        content = "Just plain text with no links."
        result = remove_html_links(content)
        assert result == content

    def test_handles_nested_brackets_in_link_text(self) -> None:
        """Link text with special characters."""
        content = "[List<Widget>](List.html)"
        result = remove_html_links(content)
        assert result == "List<Widget>"

    def test_handles_index_html_link(self) -> None:
        """The Flutter index link should be replaced."""
        content = "1. [Flutter](index.html)"
        result = remove_html_links(content)
        assert result == "1. Flutter"

    def test_handles_complex_path(self) -> None:
        """Links with complex paths should be handled."""
        content = "[BuildContext](dart-ui/BuildContext-class.html)"
        result = remove_html_links(content)
        assert result == "BuildContext"


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
