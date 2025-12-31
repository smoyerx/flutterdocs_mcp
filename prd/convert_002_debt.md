# Technical Debt: convert.py

This document tracks technical debt identified during the convert_002 implementation that should be addressed in future iterations.

## Critical: Spec Violations

### TD-001: Unauthorized Link Transformations

**Severity:** High  
**Location:** `transform_class_links()`, `transform_member_links()`

**Problem:** The implementation added transformations for link patterns not specified in convert_002.md:
- `-mixin.html` suffix (e.g., `Diagnosticable-mixin.html`)
- `-constant.html` suffix for 2-part paths (e.g., `optionalTypeArgs-constant.html`)
- `-constant.html` suffix for 3-part paths (e.g., `Colors/transparent-constant.html`)

These were added to make integration tests pass rather than following the spec's requirement to log unmatched patterns as informational messages.

**Impact:** 
- Prevents discovery of all suffix patterns in the full documentation set
- Blocks future implementation of type-specific conversion strategies for mixins, constants, and libraries

**Resolution:**
1. Remove the unauthorized transformation patterns
2. Implement informational logging for unmatched relative URI patterns as specified in section 3.2
3. Update `test_output_files_have_no_html_links` to validate that unmatched patterns are logged rather than asserting zero HTML links remain

---

### TD-002: Missing Informational Logging for Unmatched Patterns

**Severity:** High  
**Location:** `transform_class_links()`, `transform_member_links()`

**Problem:** The spec requires:
> "Any relative URI that does not match one of the following patterns will be logged as an informational message..."

This logging was never implemented. Instead, unmatched patterns were either:
- Left untransformed (silent failure), or
- Had new transformations added (spec violation per TD-001)

**Resolution:**
1. Add a catch-all pattern at the end of `apply_transformations()` to detect remaining relative HTML links
2. Log each unmatched pattern with `logging.info()` including the full link and source context
3. Consider outputting a summary count at the end of processing

---

## Moderate: Fragile Implementation

### TD-003: Hardcoded Noise Strings

**Severity:** Medium  
**Location:** `remove_noise_lines()`

**Problem:** Noise strings are hardcoded:
```python
noise_strings = [
    "const",
    "final",
    "no setterinherited",
    "finalinherited",
    "inherited",
    '[*link*](# "Copy link to clipboard")',
]
```

These are artifacts of `html_to_markdown` conversion behavior. Changes to the library or Flutter documentation format will cause silent failures.

**Resolution:**
- Move noise patterns to a configuration constant at module level
- Consider pattern-based detection (regex) instead of exact string matching
- Add integration test that validates noise removal against known samples

---

### TD-004: Fragile Section Heading Detection

**Severity:** Medium  
**Location:** `extract_section_content()`

**Problem:** Section detection uses exact heading format matching:
```python
pattern = rf"^## {re.escape(section_name)}\s*$"
```

This fails for:
- Extra whitespace: `##  Constructors`
- Heading anchors: `## Constructors {#constructors}`
- Case variations: `## CONSTRUCTORS`

**Resolution:**
- Normalize whitespace before matching
- Strip trailing anchor syntax `{#...}`
- Consider case-insensitive matching with canonical form comparison

---

### TD-005: Member Link Extraction Depends on Arrow Character

**Severity:** Medium  
**Location:** `extract_member_links()`

**Problem:** The regex requires the arrow character `→` immediately after the link to distinguish member definitions from inline references:
```python
arrow = r"\s*→"
pattern = r"^\s*\[([^\]]+)\]\(mcp://flutter/api/...)\)" + arrow
```

This is brittle because:
- Depends on exact `html_to_markdown` output formatting
- Unicode arrow character may vary (`→`, `->`, `⟶`)
- Formatting changes break extraction silently

**Resolution:**
- Document the expected input format explicitly
- Consider alternative detection strategies (e.g., line position, surrounding context)
- Add defensive handling for arrow variations

---

### TD-006: Incomplete Operator Filename Mapping

**Severity:** Medium  
**Location:** `OPERATOR_FILENAME_MAP`

**Problem:** The operator-to-filename mapping only includes operators discovered during testing:
```python
OPERATOR_FILENAME_MAP = {
    "operator ==": "operator_equals",
    "operator []": "operator_get",
    ...
}
```

Dart has additional operators that may appear in Flutter documentation but aren't mapped, causing silent failures.

**Resolution:**
- Create exhaustive mapping from Dart language specification
- Add fallback handling that logs unmapped operators
- Consider algorithmic mapping based on operator character patterns

---

### TD-007: Scattered Regex Patterns

**Severity:** Low  
**Location:** Multiple `transform_*` functions

**Problem:** Each transformation function contains inline regex patterns with no central registry or validation. This makes it difficult to:
- Audit all patterns in one place
- Test patterns independently
- Ensure patterns don't conflict or overlap

**Resolution:**
- Define patterns in a central data structure:
  ```python
  @dataclass
  class LinkPattern:
      name: str
      regex: str
      replacement: str
      description: str
  
  LINK_PATTERNS: list[LinkPattern] = [...]
  ```
- Add unit tests for pattern coverage and non-overlap
- Generate transformation functions from pattern definitions

---

## Low Priority: Code Quality

### TD-008: Analytics URL Filtering in Noise Removal

**Severity:** Low  
**Location:** `remove_noise_lines()`

**Problem:** Google Tag Manager URL filtering was added as a special case:
```python
if "googletagmanager.com" in line:
    continue
```

This mixes concerns (noise string removal vs. tracking URL removal) and uses substring matching rather than proper URL detection.

**Resolution:**
- Separate tracking URL removal into its own function
- Use proper URL parsing to detect tracking/analytics domains
- Make the blocked domain list configurable

---

### TD-009: Integration Test Assertions Too Strict

**Severity:** Low  
**Location:** `test_integration.py::test_output_files_have_no_html_links`

**Problem:** The test was updated to use a regex that excludes HTTPS URLs, but the fundamental assertion (no local HTML links) conflicts with the spec's allowance for unmatched patterns.

**Resolution:**
- Rewrite test to validate:
  1. All spec-defined patterns ARE transformed
  2. Unmatched patterns ARE logged (capture logging output)
  3. No transformation errors occur
- Add separate test for logging output validation

---

## Summary

| ID | Severity | Category | Status |
|----|----------|----------|--------|
| TD-001 | High | Spec Violation | Open |
| TD-002 | High | Spec Violation | Open |
| TD-003 | Medium | Fragile | Open |
| TD-004 | Medium | Fragile | Open |
| TD-005 | Medium | Fragile | Open |
| TD-006 | Medium | Fragile | Open |
| TD-007 | Low | Code Quality | Open |
| TD-008 | Low | Code Quality | Open |
| TD-009 | Low | Code Quality | Open |

**Recommended Priority:** Address TD-001 and TD-002 first as they block the intended use of convert.py for documentation discovery.
