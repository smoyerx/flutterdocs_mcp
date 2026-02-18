# Text constructor

const Text(
[String](mcp://flutter/api/dart-core/String) data, {
[Key](mcp://flutter/api/foundation/Key)? key,
[TextStyle](mcp://flutter/api/painting/TextStyle)? style,
[StrutStyle](mcp://flutter/api/painting/StrutStyle)? strutStyle,
[TextAlign](mcp://flutter/api/dart-ui/TextAlign)? textAlign,
[TextDirection](mcp://flutter/api/dart-ui/TextDirection)? textDirection,
[Locale](mcp://flutter/api/dart-ui/Locale)? locale,
[bool](mcp://flutter/api/dart-core/bool)? softWrap,
[TextOverflow](mcp://flutter/api/painting/TextOverflow)? overflow,
@[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.') [double](mcp://flutter/api/dart-core/double)? textScaleFactor,
[TextScaler](mcp://flutter/api/painting/TextScaler)? textScaler,
[int](mcp://flutter/api/dart-core/int)? maxLines,
[String](mcp://flutter/api/dart-core/String)? semanticsLabel,
[String](mcp://flutter/api/dart-core/String)? semanticsIdentifier,
[TextWidthBasis](mcp://flutter/api/painting/TextWidthBasis)? textWidthBasis,
[TextHeightBehavior](mcp://flutter/api/dart-ui/TextHeightBehavior)? textHeightBehavior,
[Color](mcp://flutter/api/dart-ui/Color)? selectionColor,
})

Creates a text widget.

If the `style` argument is null, the text will use the style from the
closest enclosing [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle).

The `overflow` property's behavior is affected by the `softWrap` argument.
If the `softWrap` is true or null, the glyph causing overflow, and those
that follow, will not be rendered. Otherwise, it will be shown with the
given overflow option.

## Implementation

```dart
const Text(
  String this.data, {
  super.key,
  this.style,
  this.strutStyle,
  this.textAlign,
  this.textDirection,
  this.locale,
  this.softWrap,
  this.overflow,
  @Deprecated(
    'Use textScaler instead. '
    'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. '
    'This feature was deprecated after v3.12.0-2.0.pre.',
  )
  this.textScaleFactor,
  this.textScaler,
  this.maxLines,
  this.semanticsLabel,
  this.semanticsIdentifier,
  this.textWidthBasis,
  this.textHeightBehavior,
  this.selectionColor,
}) : textSpan = null,
     assert(
       textScaler == null || textScaleFactor == null,
       'textScaleFactor is deprecated and cannot be specified when textScaler is specified.',
     );
```