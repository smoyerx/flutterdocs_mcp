"""Unit tests for transformation functions in convert.py."""

import re

from convert import (
    LINK_PATTERNS,
    apply_transformations,
    extract_member_links,
    extract_section_content,
    extract_static_method_links,
    get_unmatched_patterns,
    remove_footer,
    remove_header,
    remove_noise_lines,
    remove_tracking_urls,
    reset_unmatched_patterns,
    transform_class_links,
    transform_dartpad_links,
    transform_image_links,
    transform_member_links,
)


class TestLinkPatternRegistry:
    """Tests for the centralized LINK_PATTERNS registry."""

    def test_all_patterns_have_required_fields(self) -> None:
        """All patterns should have name, pattern, replacement, and description."""
        for p in LINK_PATTERNS:
            assert p.name, "Pattern must have a name"
            assert p.pattern, "Pattern must have a regex pattern"
            assert p.replacement is not None, "Pattern must have a replacement"
            assert p.description, "Pattern must have a description"

    def test_all_patterns_compile(self) -> None:
        """All patterns should be valid regex patterns."""
        for p in LINK_PATTERNS:
            try:
                re.compile(p.pattern)
            except re.error as e:
                raise AssertionError(f"Pattern '{p.name}' has invalid regex: {e}")

    def test_pattern_names_are_unique(self) -> None:
        """All pattern names should be unique."""
        names = [p.name for p in LINK_PATTERNS]
        assert len(names) == len(set(names)), "Pattern names must be unique"

    def test_expected_patterns_exist(self) -> None:
        """Expected patterns should be present in registry."""
        expected_names = {
            "class_link",
            "type_link",
            "dotted_member_link",
            "member_link",
            "image_link",
            "dartpad_link",
        }
        actual_names = {p.name for p in LINK_PATTERNS}
        assert expected_names == actual_names, (
            f"Missing patterns: {expected_names - actual_names}"
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


class TestRemoveTrackingUrls:
    """Tests for remove_tracking_urls transformation function."""

    def test_removes_googletagmanager_line(self) -> None:
        """Line containing googletagmanager.com should be removed."""
        content = "# Heading\n<script>googletagmanager.com/abc</script>\nBody content"
        result = remove_tracking_urls(content)
        assert result == "# Heading\nBody content"

    def test_removes_multiple_tracking_lines(self) -> None:
        """Multiple tracking lines should all be removed."""
        content = (
            "# Heading\ngoogletagmanager.com line1\nBody\ngoogletagmanager.com line2"
        )
        result = remove_tracking_urls(content)
        assert result == "# Heading\nBody"

    def test_preserves_normal_content(self) -> None:
        """Normal content without tracking URLs should be unchanged."""
        content = "# Heading\nBody content\nMore content"
        result = remove_tracking_urls(content)
        assert result == content

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = remove_tracking_urls("")
        assert result == ""


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


class TestUnmatchedPatternTracking:
    """Tests for unmatched HTML link pattern tracking."""

    def setup_method(self) -> None:
        """Reset unmatched patterns before each test."""
        reset_unmatched_patterns()

    def test_collects_mixin_patterns(self) -> None:
        """Mixin link patterns should be collected as unmatched."""
        content = (
            "See [Diagnosticable](foundation/Diagnosticable-mixin.html) for details."
        )
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 1
        assert "Diagnosticable-mixin.html" in patterns[0][1]
        assert patterns[0][0] == "test.html"

    def test_collects_constant_patterns_2_part(self) -> None:
        """Two-part constant link patterns should be collected as unmatched."""
        content = "Use [optionalTypeArgs](meta/optionalTypeArgs-constant.html)."
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 1
        assert "optionalTypeArgs-constant.html" in patterns[0][1]

    def test_collects_constant_patterns_3_part(self) -> None:
        """Three-part constant link patterns should be collected as unmatched."""
        content = "Color is [transparent](material/Colors/transparent-constant.html)."
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 1
        assert "transparent-constant.html" in patterns[0][1]

    def test_does_not_collect_transformed_class_links(self) -> None:
        """Transformed class links should not be collected."""
        content = "See [Widget](widgets/Widget-class.html) for details."
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 0

    def test_does_not_collect_transformed_member_links(self) -> None:
        """Transformed member links should not be collected."""
        content = "See [build](widgets/Widget/build.html) method."
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 0

    def test_does_not_collect_absolute_urls(self) -> None:
        """Absolute URLs should not be collected as unmatched."""
        content = "See [Flutter](https://flutter.dev/docs/index.html) for details."
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 0

    def test_collects_multiple_patterns(self) -> None:
        """Multiple unmatched patterns should all be collected."""
        content = (
            "[Diagnosticable](foundation/Diagnosticable-mixin.html) and "
            "[optionalTypeArgs](meta/optionalTypeArgs-constant.html)"
        )
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 2

    def test_reset_clears_patterns(self) -> None:
        """Reset should clear all collected patterns."""
        content = "[Diagnosticable](foundation/Diagnosticable-mixin.html)"
        apply_transformations(content)
        reset_unmatched_patterns()
        patterns = get_unmatched_patterns()
        assert len(patterns) == 0


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
