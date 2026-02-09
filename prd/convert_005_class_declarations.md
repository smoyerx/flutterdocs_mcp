# convert.py Class Documentation Function Declaration Cleanup Transformations

This document specifies updates to the convert.py script for processing class documentation files in Flutter and Dart documentation. Specifically, it details a new multi-line function declaration cleanup transformation.

## Definitions

- {DOC_DIR}: The root directory containing the HTML documentation files to be converted. Specified as a command line argument to convert.py.
- {SECTION}: The specific documentation section to convert (e.g., "widgets", "foundation", etc.). Specified as a command line argument to convert.py.
- {CLASS}: The name of the class whose documentation is being processed. Derived from the filename of the class HTML file being converted.
- A **blank line** in markdown content is a line comprising only whitespace
- A **header** in markdown content is a line starting with one or more `#` characters followed by a space (e.g., `# Header 1`, `## Header 2`, etc.)

## Current Transformations

convert.py CURRENTLY processes class documentation files by:
- Converting HTML files to markdown using the html-to-markdown library
- Calling the function flutterdoc_gen.convert.transformations.apply_transformations to clean up the resulting markdown content

## New Multi-Line Function Declaration Cleanup Transformation

This document defines a new multi-line function declaration cleanup transformation that must be applied to specific markdown content, defined below, *after* the generic transformations currently applied. This new transformation should be implemented as a separate function in flutterdoc_gen.convert.transformations.py.

### Transformation Definition

The markdown content to be transformed has the following characteristics.

#### Start Pattern

The content starts with the **first** non-blank line **after** the **first** header line.

**Important**: The search for the start pattern MUST halt if a subsequent header line is encountered.

#### End Pattern

The content ends with the **first** line containing **only**:
- Whitespace and the character `)`, excluding the quotes, with no other characters on the line excepting comments (i.e., lines that contain only whitespace and the character `)` possibly followed by whitespace and comments), or
- Whitespace and the characters `})`, excluding the quotes, with no other characters on the line excepting comments (i.e., lines that contain only whitespace and the characters `})` possibly followed by whitespace and comments)

**Important**: The search for the end pattern MUST begin **after** the identified start pattern line and halt if a subsequent header line is encountered before finding a valid end pattern.

#### Transformation Rules

The transformation MUST modify this markdown content as follows:
- Remove all blank lines between the start and end patterns
- Remove all markdown ordered list markers that are the first non-whitespace at the start of a line (i.e., `1. `, `2. `, etc.) while **retaining** all text following the marker
- Remove all markdown unordered list markers that are the first non-whitespace at the start of a line (i.e., `- `, `* `, or `+ `) while **retaining** all text following the marker
- Preserve all other whitespace and formatting on non-blank lines

**Important**:
- No markdown content outside the defined start and end patterns should be modified by this transformation.
- If no start pattern is found then no transformation should be applied.
- If a start pattern is found but no valid end pattern is found then no transformation should be applied. This is common in the case of single-line function declarations.

#### Transformation Edge Cases

convert.py MUST print an informational message (when in verbose mode) and continue processing **without** applying any transformation if one of the following edge cases is encountered:
- List markers mid-line (i.e., list markers that do not appear at the start of a line)
- The start pattern is found and it also matches the end pattern (i.e., the header is immediately followed by a line with only `)` or `})` possibly with comments)
- The end pattern line contains additional text beyond whitespace and comments (i.e., a line with `)` or `})` plus characters other than comments)

No other edge cases are expected.


### Markdown Content Subject to the New Transformation

This new transformation MUST be applied to the following markdown content when processing class documentation files:
- Constructor declarations: included in markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{CONSTRUCTOR}.html
- Native method declarations (not inherited): included in markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html
- Native operator declarations (not inherited): included in markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{OPERATOR}.html
- Static method declarations: included in markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{STATIC_METHOD}.html

Constructor declarations, method declarations, and operator declarations are all considered function declarations for the purposes of this transformation.

### Transformation Example: Native Method

#### Before Transformation

```markdown
# build method

1. @[override](dart-core/override-constant.html)

[Widget](mcp://flutter/api/widgets/Widget)build(

1. [BuildContext](mcp://flutter/api/widgets/BuildContext) context
)


Describes the part of the user interface represented by this widget.
```

#### After Transformation

```markdown
# build method

@[override](dart-core/override-constant.html)
[Widget](mcp://flutter/api/widgets/Widget)build(
[BuildContext](mcp://flutter/api/widgets/BuildContext) context
)


Describes the part of the user interface represented by this widget.
```

### Transformation Example: Constructor

#### Before Transformation

```markdown
# InkWell constructor

const InkWell({

1. [Key](mcp://flutter/api/foundation/Key)? key,
2. [Widget](mcp://flutter/api/widgets/Widget)? child,
3. [GestureTapCallback](gestures/GestureTapCallback.html)? onTap,
4. [GestureTapCallback](gestures/GestureTapCallback.html)? onDoubleTap,
5. [GestureLongPressCallback](gestures/GestureLongPressCallback.html)? onLongPress,
6. [GestureLongPressUpCallback](gestures/GestureLongPressUpCallback.html)? onLongPressUp,
7. [GestureTapDownCallback](gestures/GestureTapDownCallback.html)? onTapDown,
8. [GestureTapUpCallback](gestures/GestureTapUpCallback.html)? onTapUp,
9. [GestureTapCallback](gestures/GestureTapCallback.html)? onTapCancel,
10. [GestureTapCallback](gestures/GestureTapCallback.html)? onSecondaryTap,
11. [GestureTapUpCallback](gestures/GestureTapUpCallback.html)? onSecondaryTapUp,
12. [GestureTapDownCallback](gestures/GestureTapDownCallback.html)? onSecondaryTapDown,
13. [GestureTapCallback](gestures/GestureTapCallback.html)? onSecondaryTapCancel,
14. [ValueChanged](foundation/ValueChanged.html)<[bool](mcp://flutter/api/dart-core/bool)>? onHighlightChanged,
15. [ValueChanged](foundation/ValueChanged.html)<[bool](mcp://flutter/api/dart-core/bool)>? onHover,
16. [MouseCursor](mcp://flutter/api/services/MouseCursor)? mouseCursor,
17. [Color](mcp://flutter/api/dart-ui/Color)? focusColor,
18. [Color](mcp://flutter/api/dart-ui/Color)? hoverColor,
19. [Color](mcp://flutter/api/dart-ui/Color)? highlightColor,
20. [WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty)<[Color](mcp://flutter/api/dart-ui/Color)?>? overlayColor,
21. [Color](mcp://flutter/api/dart-ui/Color)? splashColor,
22. [InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)? splashFactory,
23. [double](mcp://flutter/api/dart-core/double)? radius,
24. [BorderRadius](mcp://flutter/api/painting/BorderRadius)? borderRadius,
25. [ShapeBorder](mcp://flutter/api/painting/ShapeBorder)? customBorder,
26. [bool](mcp://flutter/api/dart-core/bool) enableFeedback = true,
27. [bool](mcp://flutter/api/dart-core/bool) excludeFromSemantics = false,
28. [FocusNode](mcp://flutter/api/widgets/FocusNode)? focusNode,
29. [bool](mcp://flutter/api/dart-core/bool) canRequestFocus = true,
30. [ValueChanged](foundation/ValueChanged.html)<[bool](mcp://flutter/api/dart-core/bool)>? onFocusChange,
31. [bool](mcp://flutter/api/dart-core/bool) autofocus = false,
32. [MaterialStatesController](material/MaterialStatesController.html)? statesController,
33. [Duration](mcp://flutter/api/dart-core/Duration)? hoverDuration,
})

Creates an ink well.
```

#### After Transformation

```markdown
# InkWell constructor

const InkWell({
[Key](mcp://flutter/api/foundation/Key)? key,
[Widget](mcp://flutter/api/widgets/Widget)? child,
[GestureTapCallback](gestures/GestureTapCallback.html)? onTap,
[GestureTapCallback](gestures/GestureTapCallback.html)? onDoubleTap,
[GestureLongPressCallback](gestures/GestureLongPressCallback.html)? onLongPress,
[GestureLongPressUpCallback](gestures/GestureLongPressUpCallback.html)? onLongPressUp,
[GestureTapDownCallback](gestures/GestureTapDownCallback.html)? onTapDown,
[GestureTapUpCallback](gestures/GestureTapUpCallback.html)? onTapUp,
[GestureTapCallback](gestures/GestureTapCallback.html)? onTapCancel,
[GestureTapCallback](gestures/GestureTapCallback.html)? onSecondaryTap,
[GestureTapUpCallback](gestures/GestureTapUpCallback.html)? onSecondaryTapUp,
[GestureTapDownCallback](gestures/GestureTapDownCallback.html)? onSecondaryTapDown,
[GestureTapCallback](gestures/GestureTapCallback.html)? onSecondaryTapCancel,
[ValueChanged](foundation/ValueChanged.html)<[bool](mcp://flutter/api/dart-core/bool)>? onHighlightChanged,
[ValueChanged](foundation/ValueChanged.html)<[bool](mcp://flutter/api/dart-core/bool)>? onHover,
[MouseCursor](mcp://flutter/api/services/MouseCursor)? mouseCursor,
[Color](mcp://flutter/api/dart-ui/Color)? focusColor,
[Color](mcp://flutter/api/dart-ui/Color)? hoverColor,
[Color](mcp://flutter/api/dart-ui/Color)? highlightColor,
[WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty)<[Color](mcp://flutter/api/dart-ui/Color)?>? overlayColor,
[Color](mcp://flutter/api/dart-ui/Color)? splashColor,
[InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)? splashFactory,
[double](mcp://flutter/api/dart-core/double)? radius,
[BorderRadius](mcp://flutter/api/painting/BorderRadius)? borderRadius,
[ShapeBorder](mcp://flutter/api/painting/ShapeBorder)? customBorder,
[bool](mcp://flutter/api/dart-core/bool) enableFeedback = true,
[bool](mcp://flutter/api/dart-core/bool) excludeFromSemantics = false,
[FocusNode](mcp://flutter/api/widgets/FocusNode)? focusNode,
[bool](mcp://flutter/api/dart-core/bool) canRequestFocus = true,
[ValueChanged](foundation/ValueChanged.html)<[bool](mcp://flutter/api/dart-core/bool)>? onFocusChange,
[bool](mcp://flutter/api/dart-core/bool) autofocus = false,
[MaterialStatesController](material/MaterialStatesController.html)? statesController,
[Duration](mcp://flutter/api/dart-core/Duration)? hoverDuration,
})

Creates an ink well.
```

## Testing Requirements

Extend the existing test suite for convert.py to include tests for the new function declaration cleanup transformation.

Required Test Cases:
- Basic ordered list removal: Multi-line declaration with numbered parameters (as shown in examples above)
- Basic unordered list removal: Multi-line declaration with unordered list markers
- No blank lines or list markers present: Verify no-op on multi-line declarations without blank lines or list markers
- Multiple blank lines: Verify all blank lines are removed from multi-line declaration
- No header present: Verify no transformation when header is missing
- No end pattern: Verify no transformation is applied an no informational message is printed in verbose mode
- Multiple headers: Verify only the first header triggers transformation
- Content after the end pattern: Verify content after the end pattern is not transformed
- Edge cases: Verify an informational message is printed in verbose mode and no transformation is applied for each of the edge cases in the section [Transformation Edge Cases](#transformation-edge-cases)
- Mixed whitespace: Declarations with tabs, spaces, and mixed whitespace
- End pattern with comments: Line with `)` or `})` followed by comments must be accepted
- Different header levels: Test with ##, ###, etc.
- Whitespace preservation: Leading/trailing whitespace on non-blank lines should be preserved (excluding markers removed)

Other test cases may be added as necessary to ensure comprehensive coverage of the new transformation.
