"""Unit tests for transformation functions."""

import pytest

from flutterdocs.convert.patterns import NOISE_STRINGS, TRACKING_DOMAINS
from flutterdocs.convert.transformations import (
    FOOTER_MARKER,
    apply_transformations,
    cleanup_function_declaration,
    fix_link_spacing,
    get_unmatched_patterns,
    remove_footer,
    remove_header,
    remove_noise_lines,
    remove_tracking_urls,
    reset_unmatched_patterns,
    transform_class_links,
    transform_constant_links,
    transform_dartpad_links,
    transform_enum_constant_links,
    transform_extension_type_links,
    transform_image_links,
    transform_member_links,
    transform_mixin_links,
    transform_named_constructor_links,
    transform_other_root_links,
    transform_unmapped_links,
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
        assert result == "See [Widget](flutter-docs://api/widgets/Widget) for details."

    def test_transforms_multiple_class_links(self) -> None:
        """Multiple class links should all be transformed."""
        content = (
            "[Widget](widgets/Widget-class.html) and [Text](widgets/Text-class.html)"
        )
        result = transform_class_links(content)
        assert (
            result
            == "[Widget](flutter-docs://api/widgets/Widget) and [Text](flutter-docs://api/widgets/Text)"
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


class TestTransformMixinLinks:
    """Tests for transform_mixin_links transformation function."""

    def test_transforms_mixin_link(self) -> None:
        """Mixin link should be transformed to MCP URI."""
        content = "See [BaseSliderTrackShape](material/BaseSliderTrackShape-mixin.html) for details."
        result = transform_mixin_links(content)
        assert (
            result
            == "See [BaseSliderTrackShape](flutter-docs://api/material/BaseSliderTrackShape) for details."
        )

    def test_transforms_multiple_mixin_links(self) -> None:
        """Multiple mixin links should all be transformed."""
        content = "[Mixin1](widgets/Mixin1-mixin.html) and [Mixin2](material/Mixin2-mixin.html)"
        result = transform_mixin_links(content)
        assert (
            result
            == "[Mixin1](flutter-docs://api/widgets/Mixin1) and [Mixin2](flutter-docs://api/material/Mixin2)"
        )

    def test_preserves_non_mixin_links(self) -> None:
        """Links that don't match mixin pattern should be preserved."""
        content = "[Widget](widgets/Widget-class.html)"
        result = transform_mixin_links(content)
        assert result == content

    def test_preserves_links_with_path_separators(self) -> None:
        """Links with path separators in names should not be transformed."""
        content = "[Mixin](section/sub/path/Mixin-mixin.html)"
        result = transform_mixin_links(content)
        assert result == content  # Should not match due to path separators

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_mixin_links("")
        assert result == ""


class TestTransformConstantLinks:
    """Tests for transform_constant_links transformation function."""

    def test_transforms_constant_link(self) -> None:
        """Constant link should be transformed to MCP URI."""
        content = "See [kBottomNavigationBarHeight](material/kBottomNavigationBarHeight-constant.html) for value."
        result = transform_constant_links(content)
        assert (
            result
            == "See [kBottomNavigationBarHeight](flutter-docs://api/material/kBottomNavigationBarHeight) for value."
        )

    def test_transforms_multiple_constant_links(self) -> None:
        """Multiple constant links should all be transformed."""
        content = (
            "[kHeight](material/kHeight-constant.html) and "
            "[kWidth](widgets/kWidth-constant.html)"
        )
        result = transform_constant_links(content)
        assert result == (
            "[kHeight](flutter-docs://api/material/kHeight) and "
            "[kWidth](flutter-docs://api/widgets/kWidth)"
        )

    def test_preserves_enum_constant_links(self) -> None:
        """3-part enum constant links should be preserved for other transformer."""
        content = "[values](material/HourFormat/values-constant.html)"
        result = transform_constant_links(content)
        assert result == content  # 3-part, not 2-part, so not matched

    def test_preserves_non_constant_links(self) -> None:
        """Links that don't match constant pattern should be preserved."""
        content = "[Widget](widgets/Widget-class.html)"
        result = transform_constant_links(content)
        assert result == content

    def test_preserves_links_with_path_separators(self) -> None:
        """Links with path separators in names should not be transformed."""
        content = "[kConstant](section/sub/path/kConstant-constant.html)"
        result = transform_constant_links(content)
        assert result == content  # Should not match due to path separators

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_constant_links("")
        assert result == ""


class TestTransformExtensionTypeLinks:
    """Tests for transform_extension_type_links transformation function."""

    def test_transforms_extension_type_link(self) -> None:
        """Extension type link should be transformed to MCP URI."""
        content = "See [OverlayChildLayoutInfo](widgets/OverlayChildLayoutInfo-extension-type.html) for info."
        result = transform_extension_type_links(content)
        assert (
            result
            == "See [OverlayChildLayoutInfo](flutter-docs://api/widgets/OverlayChildLayoutInfo) for info."
        )

    def test_transforms_multiple_extension_type_links(self) -> None:
        """Multiple extension type links should all be transformed."""
        content = (
            "[ExtType1](widgets/ExtType1-extension-type.html) and "
            "[ExtType2](material/ExtType2-extension-type.html)"
        )
        result = transform_extension_type_links(content)
        assert result == (
            "[ExtType1](flutter-docs://api/widgets/ExtType1) and "
            "[ExtType2](flutter-docs://api/material/ExtType2)"
        )

    def test_preserves_non_extension_type_links(self) -> None:
        """Links that don't match extension type pattern should be preserved."""
        content = "[Widget](widgets/Widget-class.html)"
        result = transform_extension_type_links(content)
        assert result == content

    def test_preserves_links_with_path_separators(self) -> None:
        """Links with path separators in names should not be transformed."""
        content = "[ExtType](section/sub/path/ExtType-extension-type.html)"
        result = transform_extension_type_links(content)
        assert result == content  # Should not match due to path separators

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_extension_type_links("")
        assert result == ""


class TestTransformOtherRootLinks:
    """Tests for transform_other_root_links transformation function."""

    def test_transforms_other_root_link(self) -> None:
        """Other root documentation link should be transformed to MCP URI."""
        content = "See [MyFunction](dart-core/MyFunction.html) for details."
        result = transform_other_root_links(content)
        assert (
            result
            == "See [MyFunction](flutter-docs://api/dart-core/MyFunction) for details."
        )

    def test_transforms_multiple_other_root_links(self) -> None:
        """Multiple other root links should all be transformed."""
        content = (
            "[Function1](dart-core/Function1.html) and "
            "[Function2](widgets/Function2.html)"
        )
        result = transform_other_root_links(content)
        assert result == (
            "[Function1](flutter-docs://api/dart-core/Function1) and "
            "[Function2](flutter-docs://api/widgets/Function2)"
        )

    def test_preserves_member_links(self) -> None:
        """3-part member links should be preserved for other transformer."""
        content = "[build](widgets/Widget/build.html)"
        result = transform_other_root_links(content)
        assert result == content  # 3-part, not 2-part, so not matched

    def test_preserves_class_links_already_transformed(self) -> None:
        """Class links with -class.html suffix should not be matched."""
        # This tests that other_root_links doesn't interfere with class links
        # In actual pipeline, class links are transformed first
        content = "[Widget](widgets/Widget-class.html)"
        result = transform_other_root_links(content)
        assert result == content  # Suffix doesn't match plain .html

    def test_preserves_mixin_links_already_transformed(self) -> None:
        """Mixin links with -mixin.html suffix should not be matched."""
        content = "[Mixin](material/Mixin-mixin.html)"
        result = transform_other_root_links(content)
        assert result == content  # Suffix doesn't match plain .html

    def test_preserves_constant_links_already_transformed(self) -> None:
        """Constant links with -constant.html suffix should not be matched."""
        content = "[kConstant](material/kConstant-constant.html)"
        result = transform_other_root_links(content)
        assert result == content  # Suffix doesn't match plain .html

    def test_preserves_extension_type_links_already_transformed(self) -> None:
        """Extension type links with -extension-type.html suffix should not be matched."""
        content = "[ExtType](widgets/ExtType-extension-type.html)"
        result = transform_other_root_links(content)
        assert result == content  # Suffix doesn't match plain .html

    def test_preserves_links_with_path_separators(self) -> None:
        """Links with path separators in names should not be transformed."""
        content = "[Function](section/sub/path/Function.html)"
        result = transform_other_root_links(content)
        assert result == content  # Should not match due to path separators

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_other_root_links("")
        assert result == ""


class TestTransformMemberLinks:
    """Tests for transform_member_links transformation function."""

    def test_transforms_member_link(self) -> None:
        """Member link should be transformed to MCP URI."""
        content = "See [build](widgets/Widget/build.html) method."
        result = transform_member_links(content)
        assert result == "See [build](flutter-docs://api/widgets/Widget/build) method."

    def test_transforms_multiple_member_links(self) -> None:
        """Multiple member links should all be transformed."""
        content = (
            "[build](widgets/Widget/build.html) and [key](widgets/Widget/key.html)"
        )
        result = transform_member_links(content)
        assert (
            result
            == "[build](flutter-docs://api/widgets/Widget/build) and [key](flutter-docs://api/widgets/Widget/key)"
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


class TestTransformNamedConstructorLinks:
    """Tests for transform_named_constructor_links transformation function."""

    def test_transforms_named_constructor_link(self) -> None:
        """Named constructor link should be transformed to MCP URI."""
        content = "See [Text.rich](widgets/Text/Text.rich.html) constructor."
        result = transform_named_constructor_links(content)
        assert (
            result
            == "See [Text.rich](flutter-docs://api/widgets/Text/Text.rich) constructor."
        )

    def test_transforms_multiple_named_constructor_links(self) -> None:
        """Multiple named constructor links should all be transformed."""
        content = (
            "Use [ThemeData.from](material/ThemeData/ThemeData.from.html) or "
            "[IconButton.filled](material/IconButton/IconButton.filled.html)"
        )
        result = transform_named_constructor_links(content)
        assert result == (
            "Use [ThemeData.from](flutter-docs://api/material/ThemeData/ThemeData.from) or "
            "[IconButton.filled](flutter-docs://api/material/IconButton/IconButton.filled)"
        )

    def test_preserves_regular_member_links(self) -> None:
        """Regular member links without entity repetition should be preserved."""
        content = "[build](widgets/Widget/build.html)"
        result = transform_named_constructor_links(content)
        assert result == content  # No entity repetition, so not matched

    def test_preserves_links_with_path_separators(self) -> None:
        """Links with path separators in names should not be transformed."""
        content = "[Text.rich](section/sub/Text/Text.rich.html)"
        result = transform_named_constructor_links(content)
        assert result == content  # Should not match due to path separators

    def test_preserves_absolute_urls(self) -> None:
        """Absolute URLs should be preserved."""
        content = "[Text.rich](https://example.com/Text/Text.rich.html)"
        result = transform_named_constructor_links(content)
        assert result == content  # Absolute URL, not transformed

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_named_constructor_links("")
        assert result == ""

    def test_transforms_various_named_constructors(self) -> None:
        """Various real-world named constructor patterns should be transformed."""
        content = (
            "[ColorScheme.fromSeed](material/ColorScheme/ColorScheme.fromSeed.html) and "
            "[Transform.rotate](widgets/Transform/Transform.rotate.html) and "
            "[FloatingActionButton.extended](material/FloatingActionButton/FloatingActionButton.extended.html)"
        )
        result = transform_named_constructor_links(content)
        assert result == (
            "[ColorScheme.fromSeed](flutter-docs://api/material/ColorScheme/ColorScheme.fromSeed) and "
            "[Transform.rotate](flutter-docs://api/widgets/Transform/Transform.rotate) and "
            "[FloatingActionButton.extended](flutter-docs://api/material/FloatingActionButton/FloatingActionButton.extended)"
        )


class TestTransformEnumConstantLinks:
    """Tests for transform_enum_constant_links transformation function."""

    def test_transforms_enum_constant_link(self) -> None:
        """Enum constant link should be transformed to MCP URI."""
        content = "See [values](material/HourFormat/values-constant.html) for list."
        result = transform_enum_constant_links(content)
        assert (
            result
            == "See [values](flutter-docs://api/material/HourFormat/values) for list."
        )

    def test_transforms_multiple_enum_constant_links(self) -> None:
        """Multiple enum constant links should all be transformed."""
        content = (
            "[values](material/HourFormat/values-constant.html) and "
            "[values](widgets/SomeEnum/values-constant.html)"
        )
        result = transform_enum_constant_links(content)
        assert result == (
            "[values](flutter-docs://api/material/HourFormat/values) and "
            "[values](flutter-docs://api/widgets/SomeEnum/values)"
        )

    def test_preserves_non_constant_member_links(self) -> None:
        """Links without -constant.html suffix should be preserved."""
        content = "[build](widgets/Widget/build.html)"
        result = transform_enum_constant_links(content)
        assert result == content

    def test_preserves_root_constant_links(self) -> None:
        """2-part constant links (root constants) should be preserved."""
        # These are CategoryType.CONSTANT entities, not enum member constants
        content = "[kBottomNavigationBarHeight](material/kBottomNavigationBarHeight-constant.html)"
        result = transform_enum_constant_links(content)
        assert result == content  # 2-part, not 3-part, so not matched

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_enum_constant_links("")
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


class TestTransformUnmappedLinks:
    """Tests for transform_unmapped_links transformation function."""

    def test_transforms_relative_html_link(self) -> None:
        """Relative HTML link should be transformed to placeholder text."""
        content = "See [documentation](../docs/guide.html) for details."
        result = transform_unmapped_links(content)
        assert result == "See [Omitted link: documentation] for details."

    def test_transforms_multiple_unmapped_links(self) -> None:
        """Multiple unmapped links should all be transformed."""
        content = "[link1](path/file.html) and [link2](other/doc.md)"
        result = transform_unmapped_links(content)
        assert result == "[Omitted link: link1] and [Omitted link: link2]"

    def test_preserves_http_links(self) -> None:
        """HTTP links should be preserved."""
        content = "See [Flutter](http://flutter.dev) site."
        result = transform_unmapped_links(content)
        assert result == content

    def test_preserves_https_links(self) -> None:
        """HTTPS links should be preserved."""
        content = "See [Flutter](https://flutter.dev) site."
        result = transform_unmapped_links(content)
        assert result == content

    def test_preserves_mcp_uris(self) -> None:
        """MCP URIs (already transformed links) should be preserved."""
        content = "See [Widget](flutter-docs://api/widgets/Widget) class."
        result = transform_unmapped_links(content)
        assert result == content

    def test_preserves_anchor_links(self) -> None:
        """Anchor links should be preserved for in-document navigation."""
        content = "Jump to [section](#heading) below."
        result = transform_unmapped_links(content)
        assert result == content

    def test_transforms_parent_relative_path(self) -> None:
        """Parent relative path should be transformed."""
        content = "See [parent doc](../README.md) for more."
        result = transform_unmapped_links(content)
        assert result == "See [Omitted link: parent doc] for more."

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = transform_unmapped_links("")
        assert result == ""

    def test_mixed_content_with_preserved_and_transformed(self) -> None:
        """Mixed links: some preserved, some transformed."""
        content = "[http link](https://example.com), [relative](file.html), and [anchor](#top)"
        result = transform_unmapped_links(content)
        assert (
            result
            == "[http link](https://example.com), [Omitted link: relative], and [anchor](#top)"
        )

    def test_already_transformed_links_not_affected(self) -> None:
        """Links already transformed to MCP URIs should not match."""
        content = "[Text](flutter-docs://api/widgets/Text) widget"
        result = transform_unmapped_links(content)
        assert result == content


class TestFixLinkSpacing:
    """Tests for fix_link_spacing transformation function."""

    def test_adds_space_after_link_followed_by_text(self) -> None:
        """Link immediately followed by text should get a space."""
        content = "[Widget](url)foo"
        result = fix_link_spacing(content)
        assert result == "[Widget](url) foo"

    def test_adds_space_after_link_followed_by_underscore(self) -> None:
        """Link immediately followed by underscore identifier should get a space."""
        content = "[Widget](url)_bar"
        result = fix_link_spacing(content)
        assert result == "[Widget](url) _bar"

    def test_adds_space_after_nullable_link_followed_by_text(self) -> None:
        """Nullable link immediately followed by text should get a space after ?."""
        content = "[Widget](url)?foo"
        result = fix_link_spacing(content)
        assert result == "[Widget](url)? foo"

    def test_adds_space_after_nullable_link_followed_by_underscore(self) -> None:
        """Nullable link immediately followed by underscore should get a space."""
        content = "[Widget](url)?_bar"
        result = fix_link_spacing(content)
        assert result == "[Widget](url)? _bar"

    def test_preserves_already_spaced_link(self) -> None:
        """Link already followed by space should be unchanged."""
        content = "[Widget](url) foo"
        result = fix_link_spacing(content)
        assert result == "[Widget](url) foo"

    def test_preserves_already_spaced_nullable_link(self) -> None:
        """Nullable link already followed by space should be unchanged."""
        content = "[Widget](url)? foo"
        result = fix_link_spacing(content)
        assert result == "[Widget](url)? foo"

    def test_preserves_link_without_following_text(self) -> None:
        """Link at end of line should be unchanged."""
        content = "[Widget](url)"
        result = fix_link_spacing(content)
        assert result == "[Widget](url)"

    def test_preserves_link_followed_by_punctuation(self) -> None:
        """Link followed by punctuation should be unchanged."""
        content = "[Widget](url)."
        result = fix_link_spacing(content)
        assert result == "[Widget](url)."

    def test_preserves_link_followed_by_digit(self) -> None:
        """Link followed by digit should be unchanged (not valid Dart identifier start)."""
        content = "[Widget](url)123"
        result = fix_link_spacing(content)
        assert result == "[Widget](url)123"

    def test_fixes_multiple_links_on_same_line(self) -> None:
        """Multiple links with missing spaces should all be fixed."""
        content = "[Widget](url1)foo and [Text](url2)bar"
        result = fix_link_spacing(content)
        assert result == "[Widget](url1) foo and [Text](url2) bar"

    def test_fixes_multiple_nullable_links(self) -> None:
        """Multiple nullable links with missing spaces should all be fixed."""
        content = "[Widget](url1)?foo, [Text](url2)?bar"
        result = fix_link_spacing(content)
        assert result == "[Widget](url1)? foo, [Text](url2)? bar"

    def test_handles_empty_string(self) -> None:
        """Empty string should return empty string."""
        result = fix_link_spacing("")
        assert result == ""

    def test_realistic_dart_type_annotation(self) -> None:
        """Realistic Dart type annotation pattern should be fixed."""
        content = "Returns [Future](dart-async/Future-class.html)<[Widget](widgets/Widget-class.html)?>"
        result = fix_link_spacing(content)
        # The < after ) is not a letter, so no change there
        # The ? followed by > is not followed by a letter, so no change
        assert result == content

    def test_realistic_dart_parameter(self) -> None:
        """Realistic Dart parameter pattern should be fixed."""
        content = "[BuildContext](widgets/BuildContext-class.html)context"
        result = fix_link_spacing(content)
        assert result == "[BuildContext](widgets/BuildContext-class.html) context"

    def test_realistic_nullable_parameter(self) -> None:
        """Realistic nullable Dart parameter pattern should be fixed."""
        content = "[Key](foundation/Key-class.html)?key"
        result = fix_link_spacing(content)
        assert result == "[Key](foundation/Key-class.html)? key"


class TestUnmatchedPatternTracking:
    """Tests for unmatched HTML link pattern tracking."""

    def setup_method(self) -> None:
        """Reset unmatched patterns before each test."""
        reset_unmatched_patterns()

    def test_does_not_collect_transformed_mixin_links(self) -> None:
        """Transformed mixin links should not be collected."""
        content = (
            "See [Diagnosticable](foundation/Diagnosticable-mixin.html) for details."
        )
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 0

    def test_does_not_collect_transformed_constant_links(self) -> None:
        """Transformed two-part constant links should not be collected."""
        content = "Use [optionalTypeArgs](meta/optionalTypeArgs-constant.html)."
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        assert len(patterns) == 0

    def test_does_not_collect_transformed_enum_constant_links(self) -> None:
        """Three-part constant link patterns are now transformed and not collected."""
        content = "Color is [transparent](material/Colors/transparent-constant.html)."
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        # 3-part -constant.html links are now transformed by enum_constant_link pattern
        assert len(patterns) == 0

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
        """With unmapped_link transformation, no patterns should be unmatched."""
        # These patterns are now caught by transform_unmapped_links()
        content = (
            "[Unknown](foundation/some/nested/Unknown.html) and "
            "[Other](meta/path/to/Other.html)"
        )
        apply_transformations(content, source_context="test.html")
        patterns = get_unmatched_patterns()
        # The unmapped_link transformation catches all relative links now
        assert len(patterns) == 0

    def test_reset_clears_patterns(self) -> None:
        """Reset should clear all collected patterns."""
        # Use a pattern that isn't matched by any transformer
        content = "[Unknown](foundation/some/nested/Unknown.html)"
        apply_transformations(content)
        reset_unmatched_patterns()
        patterns = get_unmatched_patterns()
        assert len(patterns) == 0


class TestCleanupFunctionDeclaration:
    """Tests for cleanup_function_declaration transformation function."""

    def test_basic_ordered_list_removal(self) -> None:
        """Ordered list markers should be removed from function parameters."""
        content = """\
# build method

1. @[override](dart-core/override-constant.html)

[Widget](flutter-docs://api/widgets/Widget)build(

1. [BuildContext](flutter-docs://api/widgets/BuildContext) context
)


Describes the part of the user interface represented by this widget."""
        expected = """\
# build method

@[override](dart-core/override-constant.html)
[Widget](flutter-docs://api/widgets/Widget)build(
[BuildContext](flutter-docs://api/widgets/BuildContext) context
)


Describes the part of the user interface represented by this widget."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_basic_unordered_list_removal(self) -> None:
        """Unordered list markers should be removed from function parameters."""
        content = """\
# MyClass constructor

MyClass({
- [int](flutter-docs://api/dart-core/int) value,
- [String](flutter-docs://api/dart-core/String)? name,
})

Creates a new MyClass instance."""
        expected = """\
# MyClass constructor

MyClass({
[int](flutter-docs://api/dart-core/int) value,
[String](flutter-docs://api/dart-core/String)? name,
})

Creates a new MyClass instance."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_asterisk_unordered_list_removal(self) -> None:
        """Asterisk unordered list markers should be removed."""
        content = """\
# test method

void test(
* int a,
* int b
)

Test method."""
        expected = """\
# test method

void test(
int a,
int b
)

Test method."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_plus_unordered_list_removal(self) -> None:
        """Plus unordered list markers should be removed."""
        content = """\
# test method

void test(
+ int a,
+ int b
)

Test method."""
        expected = """\
# test method

void test(
int a,
int b
)

Test method."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_no_blank_lines_or_markers_noop(self) -> None:
        """Declaration without blank lines or markers should be unchanged."""
        content = """\
# simple method

void simple(
int x
)

Does something simple."""
        result = cleanup_function_declaration(content)
        assert result == content

    def test_multiple_blank_lines_removed(self) -> None:
        """Multiple blank lines within declaration should all be removed."""
        content = """\
# method with blanks

void method(


int a,


int b


)

Description."""
        expected = """\
# method with blanks

void method(
int a,
int b
)

Description."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_no_header_returns_unchanged(self) -> None:
        """Content without a header should be returned unchanged."""
        content = """\
void method(
1. int a
)

No header here."""
        result = cleanup_function_declaration(content)
        assert result == content

    def test_missing_closing_pattern_returns_unchanged(self) -> None:
        """Missing closing pattern means single-line signature, return unchanged."""
        content = """\
# simple method

void method(int a, int b)

Single line signature, no closing paren on its own line."""
        result = cleanup_function_declaration(content, source_context="test.html")
        assert result == content

    def test_multiple_headers_only_first_triggers(self) -> None:
        """Only the first header should trigger the transformation."""
        content = """\
# first header

void method(
1. int a
)

## second header

This should not be transformed.
1. This is a list item."""
        expected = """\
# first header

void method(
int a
)

## second header

This should not be transformed.
1. This is a list item."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_content_after_closing_pattern_unchanged(self) -> None:
        """Content after closing pattern should not be modified."""
        content = """\
# method

void method(
1. int a
)

1. First item in description list
2. Second item in description list"""
        expected = """\
# method

void method(
int a
)

1. First item in description list
2. Second item in description list"""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_mixed_list_markers_transforms(self) -> None:
        """Mixed ordered and unordered markers should be transformed."""
        content = """\
# mixed method

void method(
1. int a,
- int b
)

Description."""
        expected = """\
# mixed method

void method(
int a,
int b
)

Description."""
        result = cleanup_function_declaration(content, source_context="test.html")
        assert result == expected

    def test_nested_indented_markers_transforms(self) -> None:
        """Indented/nested list markers should be transformed with indent preserved."""
        content = """\
# nested method

void method(
  1. int a
)

Description."""
        expected = """\
# nested method

void method(
  int a
)

Description."""
        result = cleanup_function_declaration(content, source_context="test.html")
        assert result == expected

    def test_different_header_levels(self) -> None:
        """Different header levels should work (##, ###, etc.)."""
        content = """\
## h2 method

void method(
1. int a
)

Description."""
        expected = """\
## h2 method

void method(
int a
)

Description."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_h3_header_level(self) -> None:
        """H3 header level should work."""
        content = """\
### h3 method

void method(
1. int a
)

Description."""
        expected = """\
### h3 method

void method(
int a
)

Description."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_whitespace_preservation(self) -> None:
        """Leading/trailing whitespace on non-blank lines should be preserved."""
        content = """\
# method

  void method(
1.   int a,
2.   int b
  )

Description."""
        expected = """\
# method

  void method(
  int a,
  int b
  )

Description."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_end_pattern_with_paren_and_comment(self) -> None:
        """Closing ) with trailing comment should be accepted."""
        content = """\
# method

void method(
1. int a
) // end of parameters

Description."""
        expected = """\
# method

void method(
int a
) // end of parameters

Description."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_end_pattern_with_brace_paren_and_comment(self) -> None:
        """Closing }) with trailing comment should be accepted."""
        content = """\
# constructor

MyClass({
1. int a
}) // end of constructor

Description."""
        expected = """\
# constructor

MyClass({
int a
}) // end of constructor

Description."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_brace_paren_closing(self) -> None:
        """}) closing pattern should work for named parameters."""
        content = """\
# InkWell constructor

const InkWell({

1. [Key](flutter-docs://api/foundation/Key)? key,
2. [Widget](flutter-docs://api/widgets/Widget)? child,
})

Creates an ink well."""
        expected = """\
# InkWell constructor

const InkWell({
[Key](flutter-docs://api/foundation/Key)? key,
[Widget](flutter-docs://api/widgets/Widget)? child,
})

Creates an ink well."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_constructor_with_many_parameters(self) -> None:
        """Large constructor with many numbered parameters."""
        content = """\
# BigClass constructor

BigClass({
1. int a,
2. int b,
3. int c,
4. int d,
5. int e,
6. int f,
7. int g,
8. int h,
9. int i,
10. int j,
})

Creates a BigClass."""
        expected = """\
# BigClass constructor

BigClass({
int a,
int b,
int c,
int d,
int e,
int f,
int g,
int h,
int i,
int j,
})

Creates a BigClass."""
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_tabs_and_spaces_mixed_whitespace(self) -> None:
        """Declarations with tabs and spaces should be handled."""
        # Tab after marker is part of the marker separator and gets removed
        content = "# method\n\nvoid method(\n1.\tint a\n)\n\nDescription."
        expected = "# method\n\nvoid method(\nint a\n)\n\nDescription."
        result = cleanup_function_declaration(content)
        assert result == expected

    def test_start_pattern_halts_on_header(self) -> None:
        """Start pattern search should halt on subsequent header."""
        content = """\
# first header

## second header

void method(
1. int a
)

Description."""
        result = cleanup_function_declaration(content)
        assert result == content

    def test_end_pattern_halts_on_header(self) -> None:
        """End pattern search should halt on subsequent header."""
        content = """\
# method

void method(
1. int a

## another header

)

Description."""
        result = cleanup_function_declaration(content)
        assert result == content

    def test_mid_line_markers_returns_unchanged(self) -> None:
        """List markers mid-line should return unchanged."""
        content = """\
# method

void method(
some text 1. int a
)

Description."""
        result = cleanup_function_declaration(content, source_context="test.html")
        assert result == content
