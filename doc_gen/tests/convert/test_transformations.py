"""Unit tests for transformation functions in convert.py."""

from convert import (
    extract_member_links,
    extract_section_content,
    remove_footer,
    remove_header,
    remove_noise_lines,
    transform_class_links,
    transform_dartpad_links,
    transform_image_links,
    transform_member_links,
)


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


class TestRemoveNoiseLines:
    """Tests for remove_noise_lines transformation function."""

    def test_removes_const_line(self) -> None:
        """Line containing only 'const' should be removed."""
        content = "# Heading\nconst\nBody content"
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody content"

    def test_removes_final_line(self) -> None:
        """Line containing only 'final' should be removed."""
        content = "# Heading\nfinal\nBody content"
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody content"

    def test_removes_inherited_line(self) -> None:
        """Line containing only 'inherited' should be removed."""
        content = "# Heading\ninherited\nBody content"
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody content"

    def test_removes_no_setter_inherited_line(self) -> None:
        """Line containing only 'no setterinherited' should be removed."""
        content = "# Heading\nno setterinherited\nBody content"
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody content"

    def test_removes_final_inherited_line(self) -> None:
        """Line containing only 'finalinherited' should be removed."""
        content = "# Heading\nfinalinherited\nBody content"
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody content"

    def test_removes_copy_link_line(self) -> None:
        """Line containing only the copy link markdown should be removed."""
        content = '# Heading\n[*link*](# "Copy link to clipboard")\nBody content'
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody content"

    def test_removes_noise_with_whitespace(self) -> None:
        """Noise strings with leading/trailing whitespace should be removed."""
        content = "# Heading\n   const   \nBody content"
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody content"

    def test_preserves_noise_string_in_sentence(self) -> None:
        """Noise strings within sentences should be preserved."""
        content = "# Heading\nThis is a const variable.\nBody content"
        result = remove_noise_lines(content)
        assert result == "# Heading\nThis is a const variable.\nBody content"

    def test_preserves_normal_content(self) -> None:
        """Normal content without noise should be unchanged."""
        content = "# Heading\nBody content\nMore content"
        result = remove_noise_lines(content)
        assert result == content

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = remove_noise_lines("")
        assert result == ""

    def test_removes_multiple_noise_lines(self) -> None:
        """Multiple noise lines should all be removed."""
        content = "# Heading\nconst\nBody\nfinal\nMore"
        result = remove_noise_lines(content)
        assert result == "# Heading\nBody\nMore"


class TestTransformClassLinks:
    """Tests for transform_class_links transformation function."""

    def test_transforms_class_link(self) -> None:
        """Class link should be transformed to MCP URI."""
        content = "See [Widget](widgets/Widget-class.html) for details."
        result = transform_class_links(content)
        assert result == "See [Widget](mcp://flutter/api/widgets/Widget) for details."

    def test_transforms_multiple_class_links(self) -> None:
        """Multiple class links should all be transformed."""
        content = (
            "[Widget](widgets/Widget-class.html) and [Text](widgets/Text-class.html)"
        )
        result = transform_class_links(content)
        assert (
            result
            == "[Widget](mcp://flutter/api/widgets/Widget) and [Text](mcp://flutter/api/widgets/Text)"
        )

    def test_preserves_non_class_links(self) -> None:
        """Links that don't match class pattern should be preserved."""
        content = "[method](widgets/Widget/build.html)"
        result = transform_class_links(content)
        assert result == content

    def test_preserves_absolute_urls(self) -> None:
        """Absolute URLs should be preserved."""
        content = "[Flutter](https://flutter.dev/Widget-class.html)"
        result = transform_class_links(content)
        assert result == content

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_class_links("")
        assert result == ""


class TestTransformMemberLinks:
    """Tests for transform_member_links transformation function."""

    def test_transforms_member_link(self) -> None:
        """Member link should be transformed to MCP URI."""
        content = "See [build](widgets/Widget/build.html) method."
        result = transform_member_links(content)
        assert result == "See [build](mcp://flutter/api/widgets/Widget/build) method."

    def test_transforms_multiple_member_links(self) -> None:
        """Multiple member links should all be transformed."""
        content = (
            "[build](widgets/Widget/build.html) and [key](widgets/Widget/key.html)"
        )
        result = transform_member_links(content)
        assert (
            result
            == "[build](mcp://flutter/api/widgets/Widget/build) and [key](mcp://flutter/api/widgets/Widget/key)"
        )

    def test_preserves_non_member_links(self) -> None:
        """Links that don't match member pattern should be preserved."""
        content = "[Widget](widgets/Widget-class.html)"
        result = transform_member_links(content)
        assert result == content

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_member_links("")
        assert result == ""


class TestTransformImageLinks:
    """Tests for transform_image_links transformation function."""

    def test_transforms_image_link(self) -> None:
        """Image link should be transformed to placeholder text."""
        content = "See ![example image](images/example.png) here."
        result = transform_image_links(content)
        assert result == "See [Note: Image example image omitted] here."

    def test_transforms_image_with_url(self) -> None:
        """Image with absolute URL should be transformed."""
        content = "![logo](https://example.com/logo.png)"
        result = transform_image_links(content)
        assert result == "[Note: Image logo omitted]"

    def test_transforms_multiple_images(self) -> None:
        """Multiple images should all be transformed."""
        content = "![img1](a.png) and ![img2](b.jpg)"
        result = transform_image_links(content)
        assert result == "[Note: Image img1 omitted] and [Note: Image img2 omitted]"

    def test_preserves_regular_links(self) -> None:
        """Regular markdown links should be preserved."""
        content = "See [Flutter](https://flutter.dev) site."
        result = transform_image_links(content)
        assert result == content

    def test_handles_empty_alt_text(self) -> None:
        """Image with empty alt text should work."""
        content = "![](image.png)"
        result = transform_image_links(content)
        assert result == "[Note: Image  omitted]"

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_image_links("")
        assert result == ""


class TestTransformDartpadLinks:
    """Tests for transform_dartpad_links transformation function."""

    def test_transforms_dartpad_link(self) -> None:
        """DartPad link should be transformed to placeholder text."""
        content = "Try [this example](https://dartpad.dev/?id=123)."
        result = transform_dartpad_links(content)
        assert result == "Try [Note: Interactive sample omitted]."

    def test_transforms_multiple_dartpad_links(self) -> None:
        """Multiple DartPad links should all be transformed."""
        content = "[ex1](https://dartpad.dev/a) and [ex2](https://dartpad.dev/b)"
        result = transform_dartpad_links(content)
        assert (
            result
            == "[Note: Interactive sample omitted] and [Note: Interactive sample omitted]"
        )

    def test_preserves_non_dartpad_links(self) -> None:
        """Non-DartPad links should be preserved."""
        content = "See [Flutter](https://flutter.dev) site."
        result = transform_dartpad_links(content)
        assert result == content

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_dartpad_links("")
        assert result == ""


class TestExtractSectionContent:
    """Tests for extract_section_content function."""

    def test_extracts_section_content(self) -> None:
        """Should extract content between section heading and next section."""
        content = "# Title\n## Properties\nprop1\nprop2\n## Methods\nmethod1"
        result = extract_section_content(content, "Properties")
        assert result == "prop1\nprop2"

    def test_returns_none_for_missing_section(self) -> None:
        """Should return None if section is not found."""
        content = "# Title\n## Properties\ncontent"
        result = extract_section_content(content, "Methods")
        assert result is None

    def test_extracts_to_end_if_no_next_section(self) -> None:
        """Should extract to end if no following section."""
        content = "# Title\n## Properties\nprop1\nprop2"
        result = extract_section_content(content, "Properties")
        assert result == "prop1\nprop2"

    def test_handles_h1_as_section_terminator(self) -> None:
        """Should stop at h1 heading."""
        content = "## Properties\nprop1\n# New Doc\ncontent"
        result = extract_section_content(content, "Properties")
        assert result == "prop1"

    def test_includes_h3_subheadings(self) -> None:
        """Should include h3+ subheadings within section."""
        content = "## Properties\n### Subsection\ncontent\n## Methods"
        result = extract_section_content(content, "Properties")
        assert result == "### Subsection\ncontent"

    def test_handles_whitespace_in_heading(self) -> None:
        """Should handle whitespace around section name."""
        content = "##   Properties  \ncontent\n## Methods"
        result = extract_section_content(content, "Properties")
        assert result == "content"


class TestExtractMemberLinks:
    """Tests for extract_member_links function."""

    def test_extracts_member_link(self) -> None:
        """Should extract member link with all fields."""
        content = "[hashCode](mcp://flutter/api/dart-core/Object/hashCode)→ int\nThe hash code."
        result = extract_member_links(content)
        assert len(result) == 1
        assert result[0]["link_text"] == "hashCode"
        assert result[0]["section"] == "dart-core"
        assert result[0]["class_name"] == "Object"
        assert result[0]["member"] == "hashCode"
        assert result[0]["result_type"] == "int"
        assert result[0]["description"] == "The hash code."

    def test_extracts_multiple_members(self) -> None:
        """Should extract multiple member links."""
        content = (
            "[prop1](mcp://flutter/api/widgets/Widget/prop1)→ String\nDesc1\n\n"
            "[prop2](mcp://flutter/api/widgets/Widget/prop2)→ int\nDesc2"
        )
        result = extract_member_links(content)
        assert len(result) == 2
        assert result[0]["member"] == "prop1"
        assert result[1]["member"] == "prop2"

    def test_ignores_links_without_arrow(self) -> None:
        """Should ignore links that don't have type signature arrow."""
        content = "[method](mcp://flutter/api/widgets/Widget/method)\nDescription here."
        result = extract_member_links(content)
        # Links without arrow are inline references, not member definitions
        assert len(result) == 0

    def test_handles_multiline_description(self) -> None:
        """Should capture multiline description until blank line."""
        content = "[prop](mcp://flutter/api/s/C/prop)→ int\nLine 1\nLine 2\n\nNext"
        result = extract_member_links(content)
        assert result[0]["description"] == "Line 1\nLine 2"

    def test_handles_leading_whitespace(self) -> None:
        """Should handle leading whitespace before link."""
        content = "  [prop](mcp://flutter/api/s/C/prop)→ int\nDesc"
        result = extract_member_links(content)
        assert len(result) == 1
        assert result[0]["member"] == "prop"

    def test_returns_empty_for_no_links(self) -> None:
        """Should return empty list if no matching links."""
        content = "No links here, just text."
        result = extract_member_links(content)
        assert result == []

    def test_ignores_inline_references(self) -> None:
        """Should ignore links that appear as inline references within text."""
        content = (
            "[highlightShape](mcp://flutter/api/material/InkResponse/highlightShape) is BoxShape.\n\n"
            "[highlightShape](mcp://flutter/api/material/InkResponse/highlightShape)→ BoxShape\n"
            "The shape to use for highlights."
        )
        result = extract_member_links(content)
        # Only the second one with arrow should be extracted
        assert len(result) == 1
        assert result[0]["result_type"] == "BoxShape"

    def test_captures_full_result_type(self) -> None:
        """Should capture the full result type including links and generics."""
        content = "[prop](mcp://flutter/api/s/C/prop)→ [Widget](mcp://flutter/api/widgets/Widget)?\nDesc"
        result = extract_member_links(content)
        assert result[0]["result_type"] == "[Widget](mcp://flutter/api/widgets/Widget)?"
