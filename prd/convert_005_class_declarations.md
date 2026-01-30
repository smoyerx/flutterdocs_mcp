# convert.py Class Documentation Function Declaration Cleanup Transformations

This document specifies updates to the convert.py script for processing class documentation files in Flutter and Dart documentation. Specifically, it details a new function declaration cleanup transformation.

## Definitions

- {DOC_DIR}: The root directory containing the HTML documentation files to be converted. Specified as a command line argument to convert.py.
- {SECTION}: The specific documentation section to convert (e.g., "widgets", "foundation", etc.). Specified as a command line argument to convert.py.
- {CLASS}: The name of the class whose documentation is being processed. Derived from the filename of the class HTML file being converted.
- A **blank line** in markdown content is a line comprising only whitespace

## Current Transformations

convert.py CURRENTLY processes class documentation files by:
- Converting HTML files to markdown using the html-to-markdown library
- Calling the function flutterdoc_gen.convert.transformations.apply_transformations to clean up the resulting markdown content

## New Function Declaration Cleanup Transformation

This document defines a new function declaration cleanup transformation that must be applied to specific markdown content, defined below, *after* the generic transformations currently applied. This new transformation should be implemented as a separate function in flutterdoc_gen.convert.transformations.py.

### Transformation Definition

The markdown content to be transformed has the following characteristics:
- It starts with the **first** non-blank line **after** the **first** header (i.e., a line starting with `# `)
- It ends with the **first** line containing **only**:
   - Whitespace and the character ')', excluding the quotes, or
   - Whitespace and the characters '})', excluding the quotes
- There *may* be lines containing only whitespace between the start and end lines defined above

These lines represent the declaration for a constructor, method, or operator which are types of functions.

The transformation MUST modify this markdown content as follows:
- Remove all blank lines
- Remove all markdown ordered list markers (i.e., lines starting with `1. `, `2. `, etc.) while **retaining** the text following the marker
- Remove all markdown unordered list markers (i.e., lines starting with `- `, `* `, or `+ `) while **retaining** the text following the marker

### Markdown Content Subject to the New Transformation

This new transformation MUST be applied to the following markdown content when processing class documentation files:
- Constructors: markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{CONSTRUCTOR}.html
- Native methods (not inherited): markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{METHOD}.html
- Native operators (not inherited): markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{OPERATOR}.html
- Static methods: markdown generated from files {DOC_DIR}/flutter/{SECTION}/{CLASS}/{STATIC_METHOD}.html

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
