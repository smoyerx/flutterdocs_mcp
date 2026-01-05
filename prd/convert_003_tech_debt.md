# Technical Debt: convert.py

This document tracks technical debt identified during the convert_002 implementation that should be addressed in future iterations.

## Critical: Spec Violations

### TD-001: Unauthorized Link Transformations

**Severity:** High  
**Location:** `transform_class_links()`, `transform_member_links()`  
**Status:** RESOLVED (2025-12-31)

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
**Status:** RESOLVED (2025-12-31)

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
**Status:** RESOLVED (2025-12-31)

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
**Status:** RESOLVED (2025-12-31)

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
**Status:** RESOLVED (2025-12-31)

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
The arrow character is semantically important—it distinguishes member definitions (with type signatures) from inline references. Removing arrow detection would break this distinction.

Instead, robustness was improved by:
1. Supporting multiple arrow formats: `→` (U+2192), `->`, `=>`, `➜` (U+279C), `➔` (U+2794)
2. Allowing optional whitespace between the link closing `)` and the arrow
3. Using regex alternation pattern for arrow detection

This maintains correct semantic filtering while accommodating formatting variations.

---

### TD-006: Scattered Regex Patterns

**Severity:** Low  
**Location:** Multiple `transform_*` functions  
**Status:** RESOLVED (2025-12-31)

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

### TD-007: Analytics URL Filtering in Noise Removal

**Severity:** Low  
**Location:** `remove_noise_lines()`  
**Status:** RESOLVED (2025-12-31)

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

### TD-008: Integration Test Assertions Too Strict

**Severity:** Low  
**Location:** `test_integration.py::test_output_files_have_no_html_links`  
**Status:** RESOLVED (2025-12-31)

**Problem:** The test was updated to use a regex that excludes HTTPS URLs, but the fundamental assertion (no local HTML links) conflicts with the spec's allowance for unmatched patterns.

**Resolution:**
- Rewrite test to validate:
  1. All spec-defined patterns ARE transformed
  2. Unmatched patterns ARE logged (capture logging output)
  3. No transformation errors occur
- Add separate test for logging output validation

---

## Specification Gaps

### TD-009: Missing Static Methods Section Processing

**Severity:** Medium  
**Location:** `convert_002.md` specification  
**Status:** Closed (Implemented 2025-12-31)

**Problem:** The convert_002.md specification neglected to include processing for the `## Static Methods` section, which is present in some Flutter class documentation.

Static methods differ from instance methods:
- They are associated with the class itself, not instances of the class
- They are always **native** to the class (never inherited)
- They require a separate output directory to distinguish from instance methods

**Impact:**
- Static methods in Flutter documentation are not converted
- Classes with static methods have incomplete documentation output

**Resolution:**
Update the specification to add a new step (or sub-step of Step 4) for processing static methods:

1. Scan the static methods section (`## Static Methods`) of the {CLASS}.md content for lines that **start** with `[{METHOD}](mcp://flutter/api/{SECTION}/{CLASS}/{METHOD})`
2. For each such line found:
   - Convert {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html to markdown
   - Save the converted markdown file as {OUTPUT_DIR}/api/{SECTION}/{CLASS}/statics/{METHOD}.md
3. Continue without printing an informational or error message if:
   - No static methods section found
   - No lines matching the pattern in the static methods section
4. Print error and exit with non-zero status if:
   - HTML file for a static method does not exist
   - Link URI scheme does not match the specified pattern

**Note:** Static methods have no inherited variant since static members belong to the declaring class only.

---

### TD-010: Static Methods Processing Not Implemented

**Severity:** Medium  
**Location:** `convert.py` - missing implementation  
**Status:** RESOLVED (2025-12-31)

**Problem:** Following the resolution of TD-009, the convert_002.md specification now includes requirements for processing static methods (section `## Static Methods`). However, convert.py has not yet been updated to implement this functionality.

**Impact:**
- Static methods in Flutter class documentation are not converted
- Classes with static methods have incomplete documentation output
- Implementation is out of sync with updated specification

**Resolution:**
Implement static methods processing in convert.py following the specification in convert_002.md:

1. Add a new processing step (after operators, before snippets) to scan for `## Static Methods` section
2. Extract static method links matching pattern `[{METHOD}](mcp://flutter/api/{SECTION}/{CLASS}/{METHOD})`
3. Convert HTML files from `{DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html`
4. Save to `{OUTPUT_DIR}/api/{SECTION}/{CLASS}/statics/{METHOD}.md`
5. Handle informational cases (no section found, no methods) and error cases (missing HTML file) per spec
6. Add unit tests for static method extraction and processing
7. Add integration tests verifying static method output files

**Note:** This is a new feature implementation, not a bug fix. Since static methods have no inherited variant, the implementation is simpler than instance methods.

---

## Summary

| ID | Severity | Category | Status |
|----|----------|----------|--------|
| TD-001 | High | Spec Violation | Open |
| TD-002 | High | Spec Violation | Open |
| TD-003 | Medium | Fragile | Open |
| TD-004 | Medium | Fragile | Open |
| TD-005 | Medium | Fragile | Open |
| TD-006 | Low | Code Quality | Open |
| TD-007 | Low | Code Quality | Open |
| TD-008 | Low | Code Quality | Open |
| TD-009 | Medium | Spec Gap | **Closed** |
| TD-010 | Medium | Missing Feature | Open |

**Recommended Priority:** Address TD-001 and TD-002 first as they block the intended use of convert.py for documentation discovery. TD-010 should be implemented in the next development iteration to bring convert.py into compliance with the updated specification.
