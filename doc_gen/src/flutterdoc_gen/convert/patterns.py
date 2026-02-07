"""Pattern definitions for HTML to markdown conversion.

This module contains all pattern definitions used for link transformation
and content filtering during the conversion process.
"""

import re
from dataclasses import dataclass


# MCP URI scheme prefix for Flutter API documentation
MCP_URI_PREFIX = "mcp://flutter/api/"

# Noise strings to remove from converted markdown
# These are artifacts from the HTML conversion that don't add value
# Each entry: (noise_string, test_input_with_noise, expected_output_without_noise)
#
# An argument could be made that some of these belong in the converted markdown.
# Will make adjustments based on user feedback.
NOISE_STRINGS: tuple[tuple[str, str, str], ...] = (
    ("const", "# Heading\nconst\nBody content", "# Heading\nBody content"),
    ("final", "# Heading\nfinal\nBody content", "# Heading\nBody content"),
    ("override", "# Heading\noverride\nBody content", "# Heading\nBody content"),
    ("no setter", "# Heading\nno setter\nBody content", "# Heading\nBody content"),
    (
        "getter/setter pair",
        "# Heading\ngetter/setter pair\nBody content",
        "# Heading\nBody content",
    ),
    (
        "no setterinherited",
        "# Heading\nno setterinherited\nBody content",
        "# Heading\nBody content",
    ),
    (
        "finalinherited",
        "# Heading\nfinalinherited\nBody content",
        "# Heading\nBody content",
    ),
    ("inherited", "# Heading\ninherited\nBody content", "# Heading\nBody content"),
    (
        '[*link*](# "Copy link to clipboard")',
        '# Heading\n[*link*](# "Copy link to clipboard")\nBody content',
        "# Heading\nBody content",
    ),
    (
        "*content_copy*",
        "# Heading\n*content_copy*\nBody content",
        "# Heading\nBody content",
    ),
)

# Analytics/tracking domains to filter from output
# Each entry: (tracking_domain, test_input_with_domain, expected_output_without_domain)
TRACKING_DOMAINS: tuple[tuple[str, str, str], ...] = (
    (
        "googletagmanager.com",
        "# Heading\n<script>googletagmanager.com/abc</script>\nBody content",
        "# Heading\nBody content",
    ),
)


@dataclass(frozen=True)
class LinkPattern:
    """A pattern for transforming markdown links.

    Attributes:
        name: A human-readable name for the pattern.
        pattern: The regex pattern to match.
        replacement: The replacement string (can use capture groups).
        description: A description of what this pattern matches.
        test_input: Example input markdown to test the pattern.
        test_output: Expected output after applying the pattern.
    """

    name: str
    pattern: str
    replacement: str
    description: str
    test_input: str
    test_output: str


# Centralized registry of link transformation patterns
# Order matters: more specific patterns should come before less specific ones.
# In particular, enum_constant_link (3-part with -constant.html) must come
# BEFORE member_link (3-part with .html) to avoid incorrect matches.
LINK_PATTERNS: tuple[LinkPattern, ...] = (
    # Class links
    LinkPattern(
        name="class_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-class\.html\)",
        replacement=rf"[\1]({MCP_URI_PREFIX}\2/\3)",
        description="[ClassName](section/ClassName-class.html)",
        test_input="See [Widget](widgets/Widget-class.html) for details.",
        test_output="See [Widget](mcp://flutter/api/widgets/Widget) for details.",
    ),
    # Mixin links
    LinkPattern(
        name="mixin_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-mixin\.html\)",
        replacement=rf"[\1]({MCP_URI_PREFIX}\2/\3)",
        description="[MixinName](section/MixinName-mixin.html)",
        test_input="See [BaseSliderTrackShape](material/BaseSliderTrackShape-mixin.html) for details.",
        test_output="See [BaseSliderTrackShape](mcp://flutter/api/material/BaseSliderTrackShape) for details.",
    ),
    # Constant links (2-part root constants, not enum member constants)
    LinkPattern(
        name="constant_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-constant\.html\)",
        replacement=rf"[\1]({MCP_URI_PREFIX}\2/\3)",
        description="[constantName](section/constantName-constant.html)",
        test_input="See [kBottomNavigationBarHeight](material/kBottomNavigationBarHeight-constant.html) for value.",
        test_output="See [kBottomNavigationBarHeight](mcp://flutter/api/material/kBottomNavigationBarHeight) for value.",
    ),
    # Extension type links
    LinkPattern(
        name="extension_type_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-extension-type\.html\)",
        replacement=rf"[\1]({MCP_URI_PREFIX}\2/\3)",
        description="[ExtensionTypeName](section/ExtensionTypeName-extension-type.html)",
        test_input="See [OverlayChildLayoutInfo](widgets/OverlayChildLayoutInfo-extension-type.html) for info.",
        test_output="See [OverlayChildLayoutInfo](mcp://flutter/api/widgets/OverlayChildLayoutInfo) for info.",
    ),
    # Other root documentation links (catch-all for remaining root docs)
    # Must come AFTER more specific 2-part patterns (class, mixin, constant, extension-type)
    LinkPattern(
        name="other_root_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)\.html\)",
        replacement=rf"[\1]({MCP_URI_PREFIX}\2/\3)",
        description="[EntityName](section/EntityName.html)",
        test_input="See [MyFunction](dart-core/MyFunction.html) for details.",
        test_output="See [MyFunction](mcp://flutter/api/dart-core/MyFunction) for details.",
    ),
    # Enum constant links (3-part with -constant.html suffix)
    # Must come BEFORE member_link to match the more specific pattern first.
    LinkPattern(
        name="enum_constant_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)-constant\.html\)",
        replacement=rf"[\1]({MCP_URI_PREFIX}\2/\3/\4)",
        description="[constant](section/Enum/constant-constant.html)",
        test_input="See [values](material/HourFormat/values-constant.html) for list.",
        test_output="See [values](mcp://flutter/api/material/HourFormat/values) for list.",
    ),
    # Member links
    LinkPattern(
        name="member_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)\.html\)",
        replacement=rf"[\1]({MCP_URI_PREFIX}\2/\3/\4)",
        description="[member](section/entity/member.html)",
        test_input="[build](widgets/Widget/build.html) method",
        test_output="[build](mcp://flutter/api/widgets/Widget/build) method",
    ),
    # Special links
    LinkPattern(
        name="image_link",
        pattern=r"!\[([^\]]*)\]\([^)]+\)",
        replacement=r"[Omitted image: \1]",
        description="![alt text](path) - image links",
        test_input="![diagram](assets/diagram.png)",
        test_output="[Omitted image: diagram]",
    ),
    LinkPattern(
        name="dartpad_link",
        pattern=r"\[[^\]]+\]\([^)]*dartpad\.dev[^)]*\)",
        replacement="[Omitted code: Interactive sample]",
        description="[text](url with dartpad.dev) - DartPad links",
        test_input="[Open in DartPad](https://dartpad.dev/?id=abc123)",
        test_output="[Omitted code: Interactive sample]",
    ),
)

# Pattern for detecting unmatched relative HTML links
UNMATCHED_HTML_LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?!https?://)[^)]+\.html[^)]*\)")
