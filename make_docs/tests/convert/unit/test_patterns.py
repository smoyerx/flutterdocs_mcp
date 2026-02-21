"""Unit tests for pattern definitions."""

import re

from flutterdocs.convert.patterns import LINK_PATTERNS


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
            "mixin_link",
            "constant_link",
            "extension_type_link",
            "other_root_link",
            "named_constructor_link",
            "enum_constant_link",
            "member_link",
            "image_link",
            "dartpad_link",
            "unmapped_link",
        }
        actual_names = {p.name for p in LINK_PATTERNS}
        assert expected_names == actual_names, (
            f"Missing patterns: {expected_names - actual_names}"
        )

    def test_enum_constant_link_pattern_before_member_link(self) -> None:
        """enum_constant_link must come before member_link in registry.

        This is critical because enum_constant_link is more specific
        (-constant.html vs .html). If member_link comes first, it would
        incorrectly match enum constant links.
        """
        names = [p.name for p in LINK_PATTERNS]
        enum_constant_idx = names.index("enum_constant_link")
        member_idx = names.index("member_link")
        assert enum_constant_idx < member_idx, (
            "enum_constant_link must come before member_link in LINK_PATTERNS"
        )
