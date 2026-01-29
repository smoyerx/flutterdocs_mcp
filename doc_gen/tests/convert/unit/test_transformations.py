"""Unit tests for transformation functions."""

import pytest

from flutterdoc_gen.convert.patterns import NOISE_STRINGS, TRACKING_DOMAINS
from flutterdoc_gen.convert.transformations import (
    FOOTER_MARKER,
    apply_transformations,
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
        content = f"# Heading\nBody\n{FOOTER_MARKER}\nFooter stuff"
        result = remove_footer(content)
        assert result == "# Heading\nBody"

    def test_preserves_content_without_footer_marker(self) -> None:
        """Content without footer marker should be unchanged."""
        content = "# Heading\nBody content\nMore content"
        result = remove_footer(content)
        assert result == content

    def test_handles_marker_at_start(self) -> None:
        """Footer marker at start of content removes everything."""
        content = f"{FOOTER_MARKER}\nAll footer"
        result = remove_footer(content)
        assert result == ""

    def test_handles_marker_with_surrounding_whitespace(self) -> None:
        """Footer marker detection works with surrounding content on line."""
        content = f"Body\n   {FOOTER_MARKER}   \nFooter"
        result = remove_footer(content)
        assert result == "Body"

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = remove_footer("")
        assert result == ""

    def test_removes_trailing_whitespace(self) -> None:
        """Trailing whitespace before footer should be stripped."""
        content = f"# Heading\nBody\n\n\n{FOOTER_MARKER}"
        result = remove_footer(content)
        assert result == "# Heading\nBody"

    def test_handles_marker_as_only_content(self) -> None:
        """Just the footer marker should result in empty string."""
        content = FOOTER_MARKER
        result = remove_footer(content)
        assert result == ""


class TestRemoveNoiseLines:
    """Tests for remove_noise_lines transformation function."""

    @pytest.mark.parametrize(
        ("noise_string", "test_input", "expected_output"), NOISE_STRINGS
    )
    def test_removes_noise_string(
        self, noise_string: str, test_input: str, expected_output: str
    ) -> None:
        """Each noise string should be removed from content."""
        result = remove_noise_lines(test_input)
        assert result == expected_output

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

    @pytest.mark.parametrize(
        ("tracking_domain", "test_input", "expected_output"), TRACKING_DOMAINS
    )
    def test_removes_tracking_domain(
        self, tracking_domain: str, test_input: str, expected_output: str
    ) -> None:
        """Each tracking domain should be removed from content."""
        result = remove_tracking_urls(test_input)
        assert result == expected_output

    def test_removes_multiple_tracking_lines(self) -> None:
        """Multiple tracking lines should all be removed."""
        # Extract first tracking domain for testing multiple occurrences
        tracking_domain = TRACKING_DOMAINS[0][0]
        content = f"# Heading\n{tracking_domain} line1\nBody\n{tracking_domain} line2"
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
        assert result == "See [Omitted image: example image] here."

    def test_transforms_image_with_url(self) -> None:
        """Image with absolute URL should be transformed."""
        content = "![logo](https://example.com/logo.png)"
        result = transform_image_links(content)
        assert result == "[Omitted image: logo]"

    def test_transforms_multiple_images(self) -> None:
        """Multiple images should all be transformed."""
        content = "![img1](a.png) and ![img2](b.jpg)"
        result = transform_image_links(content)
        assert result == "[Omitted image: img1] and [Omitted image: img2]"

    def test_preserves_regular_links(self) -> None:
        """Regular markdown links should be preserved."""
        content = "See [Flutter](https://flutter.dev) site."
        result = transform_image_links(content)
        assert result == content

    def test_handles_empty_alt_text(self) -> None:
        """Image with empty alt text should work."""
        content = "![](image.png)"
        result = transform_image_links(content)
        assert result == "[Omitted image: ]"

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
        assert result == "Try [Omitted code: Interactive sample]."

    def test_transforms_multiple_dartpad_links(self) -> None:
        """Multiple DartPad links should all be transformed."""
        content = "[ex1](https://dartpad.dev/a) and [ex2](https://dartpad.dev/b)"
        result = transform_dartpad_links(content)
        assert (
            result
            == "[Omitted code: Interactive sample] and [Omitted code: Interactive sample]"
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
