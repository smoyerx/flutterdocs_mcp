"""Unit tests for pattern definitions."""

import re

from flutterdoc_gen.convert.patterns import LINK_PATTERNS


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
            "member_link",
            "image_link",
            "dartpad_link",
        }
        actual_names = {p.name for p in LINK_PATTERNS}
        assert expected_names == actual_names, (
            f"Missing patterns: {expected_names - actual_names}"
        )
