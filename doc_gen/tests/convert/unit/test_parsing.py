"""Unit tests for parsing functions."""

from flutterdoc_gen.convert.parsing import (
    extract_member_links,
    extract_section_content,
    extract_static_method_links,
)


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

    def test_handles_anchor_syntax(self) -> None:
        """Should strip anchor syntax like {#constructors} from heading."""
        content = "## Constructors {#constructors}\nconstructor content\n## Properties"
        result = extract_section_content(content, "Constructors")
        assert result == "constructor content"

    def test_case_insensitive_matching(self) -> None:
        """Should match section names case-insensitively."""
        content = "## PROPERTIES\nprop1\n## Methods"
        result = extract_section_content(content, "Properties")
        assert result == "prop1"

    def test_case_insensitive_matching_lowercase(self) -> None:
        """Should match lowercase heading with titlecase search."""
        content = "## properties\nprop1\n## Methods"
        result = extract_section_content(content, "Properties")
        assert result == "prop1"

    def test_handles_multiple_whitespace(self) -> None:
        """Should normalize multiple whitespace in heading."""
        content = "## Static   Methods\nmethod1\n## Other"
        result = extract_section_content(content, "Static Methods")
        assert result == "method1"

    def test_anchor_with_extra_whitespace(self) -> None:
        """Should handle anchor with whitespace."""
        content = "##  Methods  {#methods}  \nmethod content\n## Properties"
        result = extract_section_content(content, "Methods")
        assert result == "method content"


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

    def test_handles_ascii_arrow(self) -> None:
        """Should handle ASCII arrow (->) format."""
        content = "[prop](mcp://flutter/api/s/C/prop)-> int\nDesc"
        result = extract_member_links(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "int"

    def test_handles_fat_arrow(self) -> None:
        """Should handle fat arrow (=>) format."""
        content = "[prop](mcp://flutter/api/s/C/prop)=> int\nDesc"
        result = extract_member_links(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "int"

    def test_handles_whitespace_before_arrow(self) -> None:
        """Should handle whitespace between link and arrow."""
        content = "[prop](mcp://flutter/api/s/C/prop) → int\nDesc"
        result = extract_member_links(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "int"

    def test_handles_multiple_whitespace_before_arrow(self) -> None:
        """Should handle multiple whitespace characters before arrow."""
        content = "[prop](mcp://flutter/api/s/C/prop)   →   int\nDesc"
        result = extract_member_links(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "int"

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


class TestExtractStaticMethodLinks:
    """Tests for extract_static_method_links function."""

    def test_extracts_static_method_link(self) -> None:
        """Should extract static method link with parameters."""
        content = (
            "[divideTiles](mcp://flutter/api/material/ListTile/divideTiles)"
            "({BuildContext? context, required Iterable<Widget> tiles}) → Iterable<Widget>"
        )
        result = extract_static_method_links(content)
        assert len(result) == 1
        assert result[0]["link_text"] == "divideTiles"
        assert result[0]["section"] == "material"
        assert result[0]["class_name"] == "ListTile"
        assert result[0]["member"] == "divideTiles"

    def test_extracts_multiple_static_methods(self) -> None:
        """Should extract multiple static method links."""
        content = (
            "[method1](mcp://flutter/api/section/Class/method1)() → void\n"
            "[method2](mcp://flutter/api/section/Class/method2)() → int\n"
        )
        result = extract_static_method_links(content)
        assert len(result) == 2
        assert result[0]["member"] == "method1"
        assert result[1]["member"] == "method2"

    def test_ignores_non_link_lines(self) -> None:
        """Should ignore lines that don't start with MCP links."""
        content = (
            "Some description text\n"
            "[divideTiles](mcp://flutter/api/material/ListTile/divideTiles)() → void\n"
            "More text here"
        )
        result = extract_static_method_links(content)
        assert len(result) == 1
        assert result[0]["member"] == "divideTiles"

    def test_handles_leading_whitespace(self) -> None:
        """Should handle leading whitespace on link lines."""
        content = "  [method](mcp://flutter/api/section/Class/method)() → void"
        result = extract_static_method_links(content)
        assert len(result) == 1
        assert result[0]["member"] == "method"

    def test_returns_empty_for_no_links(self) -> None:
        """Should return empty list if no matching links."""
        content = "No links here, just text."
        result = extract_static_method_links(content)
        assert result == []

    def test_returns_empty_for_empty_content(self) -> None:
        """Should return empty list for empty content."""
        result = extract_static_method_links("")
        assert result == []
