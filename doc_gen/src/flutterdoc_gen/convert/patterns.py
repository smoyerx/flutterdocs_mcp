"""Pattern definitions for HTML to markdown conversion.

This module contains all pattern definitions used for link transformation
and content filtering during the conversion process.
"""

import re
from dataclasses import dataclass


# Noise strings to remove from converted markdown
# These are artifacts from the HTML conversion that don't add value
NOISE_STRINGS: tuple[str, ...] = (
    "const",
    "final",
    "no setterinherited",
    "finalinherited",
    "inherited",
    '[*link*](# "Copy link to clipboard")',
)

# Analytics/tracking domains to filter from output
TRACKING_DOMAINS: tuple[str, ...] = ("googletagmanager.com",)


@dataclass(frozen=True)
class LinkPattern:
    """A pattern for transforming markdown links.

    Attributes:
        name: A human-readable name for the pattern.
        pattern: The regex pattern to match.
        replacement: The replacement string (can use capture groups).
        description: A description of what this pattern matches.
    """

    name: str
    pattern: str
    replacement: str
    description: str


# Centralized registry of link transformation patterns
# Order matters: more specific patterns should come before less specific ones
LINK_PATTERNS: tuple[LinkPattern, ...] = (
    # Class links
    LinkPattern(
        name="class_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-class\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3)",
        description="[ClassName](section/ClassName-class.html)",
    ),
    LinkPattern(
        name="type_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3)",
        description="[Type](section/Type.html) - types and references",
    ),
    # Member links (more specific patterns first)
    LinkPattern(
        name="dotted_member_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3/\4)",
        description="[Class.member](section/Class/Class.member.html) - named constructors/static methods",
    ),
    LinkPattern(
        name="member_link",
        pattern=r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)\.html\)",
        replacement=r"[\1](mcp://flutter/api/\2/\3/\4)",
        description="[member](section/Class/member.html)",
    ),
    # Special links
    LinkPattern(
        name="image_link",
        pattern=r"!\[([^\]]*)\]\([^)]+\)",
        replacement=r"[Note: Image \1 omitted]",
        description="![alt text](path) - image links",
    ),
    LinkPattern(
        name="dartpad_link",
        pattern=r"\[[^\]]+\]\([^)]*dartpad\.dev[^)]*\)",
        replacement="[Note: Interactive sample omitted]",
        description="[text](url with dartpad.dev) - DartPad links",
    ),
)

# Pattern for detecting unmatched relative HTML links
UNMATCHED_HTML_LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?!https?://)[^)]+\.html[^)]*\)")
