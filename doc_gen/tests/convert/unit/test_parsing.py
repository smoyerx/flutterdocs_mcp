"""Unit tests for parsing functions."""

from flutterdoc_gen.convert.parsing import (
    extract_member_definitions,
    extract_member_links,
    extract_method_links,
    extract_section_content,
    extract_static_method_links,
    split_into_paragraphs,
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


class TestSplitIntoParagraphs:
    """Tests for split_into_paragraphs function."""

    def test_splits_by_blank_lines(self) -> None:
        """Should split content into paragraphs separated by blank lines."""
        content = "Line 1\nLine 2\n\nLine 3\nLine 4"
        result = split_into_paragraphs(content)
        assert len(result) == 2
        assert result[0] == "Line 1\nLine 2"
        assert result[1] == "Line 3\nLine 4"

    def test_splits_by_section_headers(self) -> None:
        """Should treat section headers as paragraph boundaries."""
        content = "Line 1\n## Header\nLine 2"
        result = split_into_paragraphs(content)
        assert len(result) == 2
        assert result[0] == "Line 1"
        assert result[1] == "Line 2"

    def test_excludes_section_headers_from_paragraphs(self) -> None:
        """Should not include section headers in paragraph content."""
        content = "## Header 1\nContent\n## Header 2"
        result = split_into_paragraphs(content)
        assert len(result) == 1
        assert result[0] == "Content"
        assert "##" not in result[0]

    def test_handles_consecutive_blank_lines(self) -> None:
        """Should handle multiple consecutive blank lines."""
        content = "Para 1\n\n\n\nPara 2"
        result = split_into_paragraphs(content)
        assert len(result) == 2
        assert result[0] == "Para 1"
        assert result[1] == "Para 2"

    def test_handles_no_blank_line_after_header(self) -> None:
        """Should work when member follows immediately after section header."""
        content = "## Properties\n[prop](mcp://link)→ Type"
        result = split_into_paragraphs(content)
        assert len(result) == 1
        assert result[0] == "[prop](mcp://link)→ Type"

    def test_handles_header_before_next_section(self) -> None:
        """Should work when paragraph is followed immediately by section header."""
        content = "[prop](mcp://link)→ Type\nDesc\n## Methods"
        result = split_into_paragraphs(content)
        assert len(result) == 1
        assert result[0] == "[prop](mcp://link)→ Type\nDesc"

    def test_preserves_internal_newlines(self) -> None:
        """Should preserve newlines within paragraphs."""
        content = "Line 1\nLine 2\nLine 3\n\nNext para"
        result = split_into_paragraphs(content)
        assert result[0] == "Line 1\nLine 2\nLine 3"

    def test_handles_empty_content(self) -> None:
        """Should return empty list for empty content."""
        assert split_into_paragraphs("") == []

    def test_handles_only_blank_lines(self) -> None:
        """Should return empty list for content with only blank lines."""
        assert split_into_paragraphs("\n\n\n") == []


class TestExtractMemberDefinitions:
    """Tests for extract_member_definitions function."""

    def test_extracts_property_definition(self) -> None:
        """Should extract property with arrow immediately after link."""
        content = (
            "[hashCode](mcp://flutter/api/dart-core/Object/hashCode)→ int\n"
            "The hash code."
        )
        result = extract_member_definitions(content)
        assert len(result) == 1
        assert result[0]["link_text"] == "hashCode"
        assert result[0]["section"] == "dart-core"
        assert result[0]["class_name"] == "Object"
        assert result[0]["member"] == "hashCode"
        assert result[0]["result_type"] == "int"
        assert result[0]["description"] == "The hash code."

    def test_extracts_method_definition(self) -> None:
        """Should extract method with arrow after parameters."""
        content = (
            "[build](mcp://flutter/api/widgets/StatelessWidget/build)"
            "(BuildContext context) → Widget\n"
            "Describes the part of the user interface."
        )
        result = extract_member_definitions(content)
        assert len(result) == 1
        assert result[0]["link_text"] == "build"
        assert result[0]["section"] == "widgets"
        assert result[0]["class_name"] == "StatelessWidget"
        assert result[0]["member"] == "build"
        assert result[0]["result_type"] == "Widget"
        assert result[0]["description"] == "Describes the part of the user interface."

    def test_extracts_operator_definition(self) -> None:
        """Should extract operator with arrow after parameters."""
        content = (
            "[operator ==](mcp://flutter/api/widgets/Widget/operator_equals)"
            "([Object](mcp://flutter/api/dart-core/Object) other) → "
            "[bool](mcp://flutter/api/dart-core/bool)\n"
            "The equality operator."
        )
        result = extract_member_definitions(content)
        assert len(result) == 1
        assert result[0]["link_text"] == "operator =="
        assert result[0]["section"] == "widgets"
        assert result[0]["class_name"] == "Widget"
        assert result[0]["member"] == "operator_equals"
        assert result[0]["result_type"] == "[bool](mcp://flutter/api/dart-core/bool)"
        assert result[0]["description"] == "The equality operator."

    def test_extracts_multiple_members(self) -> None:
        """Should extract multiple member definitions."""
        content = (
            "[prop1](mcp://flutter/api/widgets/Widget/prop1)→ String\n"
            "Description 1\n\n"
            "[prop2](mcp://flutter/api/widgets/Widget/prop2)→ int\n"
            "Description 2"
        )
        result = extract_member_definitions(content)
        assert len(result) == 2
        assert result[0]["member"] == "prop1"
        assert result[1]["member"] == "prop2"

    def test_ignores_links_without_arrow(self) -> None:
        """Should ignore inline references without arrows."""
        content = (
            "[highlightShape](mcp://flutter/api/material/InkResponse/highlightShape) "
            "is BoxShape.\n\n"
            "[highlightShape](mcp://flutter/api/material/InkResponse/highlightShape)→ BoxShape\n"
            "The shape to use."
        )
        result = extract_member_definitions(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "BoxShape"

    def test_handles_multiline_description(self) -> None:
        """Should capture multiline descriptions within paragraph."""
        content = (
            "[prop](mcp://flutter/api/s/C/prop)→ int\nLine 1\nLine 2\n\nNext member"
        )
        result = extract_member_definitions(content)
        assert result[0]["description"] == "Line 1\nLine 2"

    def test_handles_complex_result_types(self) -> None:
        """Should capture full result type including links and generics."""
        content = (
            "[prop](mcp://flutter/api/s/C/prop)→ "
            "[List](link)<[Widget](link)>?\n"
            "Description"
        )
        result = extract_member_definitions(content)
        assert result[0]["result_type"] == "[List](link)<[Widget](link)>?"

    def test_handles_ascii_arrow(self) -> None:
        """Should handle ASCII arrow (->) format."""
        content = "[prop](mcp://flutter/api/s/C/prop)-> int\nDesc"
        result = extract_member_definitions(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "int"

    def test_handles_fat_arrow(self) -> None:
        """Should handle fat arrow (=>) format."""
        content = "[prop](mcp://flutter/api/s/C/prop)=> int\nDesc"
        result = extract_member_definitions(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "int"

    def test_strips_result_type_whitespace(self) -> None:
        """Should strip leading and trailing whitespace from result type."""
        content = "[prop](mcp://flutter/api/s/C/prop)→   int  \nDesc"
        result = extract_member_definitions(content)
        assert result[0]["result_type"] == "int"

    def test_returns_empty_for_no_definitions(self) -> None:
        """Should return empty list if no matching definitions."""
        content = "No member definitions here."
        result = extract_member_definitions(content)
        assert result == []


class TestExtractMemberLinks:
    """Tests for extract_member_links function (legacy - for backward compatibility)."""

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


class TestExtractMethodLinks:
    """Tests for extract_method_links function."""

    def test_extracts_method_with_parameters(self) -> None:
        """Should extract method link with parameters before arrow."""
        content = "[build](mcp://flutter/api/widgets/StatelessWidget/build)(BuildContext context) → Widget\nDesc"
        result = extract_method_links(content)
        assert len(result) == 1
        assert result[0]["link_text"] == "build"
        assert result[0]["section"] == "widgets"
        assert result[0]["class_name"] == "StatelessWidget"
        assert result[0]["member"] == "build"
        assert result[0]["result_type"] == "Widget"
        assert result[0]["description"] == "Desc"

    def test_extracts_operator_with_parameters(self) -> None:
        """Should extract operator link with parameters before arrow."""
        content = "[operator ==](mcp://flutter/api/widgets/Widget/operator_equals)([Object](mcp://flutter/api/dart-core/Object) other) → [bool](mcp://flutter/api/dart-core/bool)\nThe equality operator."
        result = extract_method_links(content)
        assert len(result) == 1
        assert result[0]["link_text"] == "operator =="
        assert result[0]["section"] == "widgets"
        assert result[0]["class_name"] == "Widget"
        assert result[0]["member"] == "operator_equals"
        assert result[0]["result_type"] == "[bool](mcp://flutter/api/dart-core/bool)"
        assert result[0]["description"] == "The equality operator."

    def test_ignores_links_without_arrow(self) -> None:
        """Should ignore method links that don't have return type arrow."""
        content = "[method](mcp://flutter/api/widgets/Widget/method)(int param)\nDescription here."
        result = extract_method_links(content)
        assert len(result) == 0

    def test_extracts_multiple_methods(self) -> None:
        """Should extract multiple method links."""
        content = (
            "[method1](mcp://flutter/api/section/Class/method1)() → void\nDesc1\n\n"
            "[method2](mcp://flutter/api/section/Class/method2)(int x) → int\nDesc2"
        )
        result = extract_method_links(content)
        assert len(result) == 2
        assert result[0]["member"] == "method1"
        assert result[1]["member"] == "method2"

    def test_handles_complex_parameters(self) -> None:
        """Should handle methods with complex parameter types."""
        content = "[method](mcp://flutter/api/s/C/method)([Map<String, dynamic>](link) data) → Future<void>\nAsync method."
        result = extract_method_links(content)
        assert len(result) == 1
        assert result[0]["result_type"] == "Future<void>"
        assert result[0]["description"] == "Async method."

    def test_handles_multiline_description(self) -> None:
        """Should capture multiline description until blank line."""
        content = (
            "[method](mcp://flutter/api/s/C/method)() → void\nLine 1\nLine 2\n\nNext"
        )
        result = extract_method_links(content)
        assert result[0]["description"] == "Line 1\nLine 2"

    def test_handles_leading_whitespace(self) -> None:
        """Should handle leading whitespace before link."""
        content = "  [method](mcp://flutter/api/s/C/method)() → void\nDesc"
        result = extract_method_links(content)
        assert len(result) == 1
        assert result[0]["member"] == "method"

    def test_returns_empty_for_no_links(self) -> None:
        """Should return empty list if no matching links."""
        content = "No links here, just text."
        result = extract_method_links(content)
        assert result == []
