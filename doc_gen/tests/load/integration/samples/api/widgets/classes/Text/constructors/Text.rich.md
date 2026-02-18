# Text.rich constructor

const Text.rich(
[InlineSpan](mcp://flutter/api/painting/InlineSpan) textSpan, {
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

Creates a text widget with a [InlineSpan](mcp://flutter/api/painting/InlineSpan).

The following subclasses of [InlineSpan](mcp://flutter/api/painting/InlineSpan) may be used to build rich text:

- [TextSpan](mcp://flutter/api/painting/TextSpan) s define text and children [InlineSpan](mcp://flutter/api/painting/InlineSpan) s.
- [WidgetSpan](mcp://flutter/api/widgets/WidgetSpan) s define embedded inline widgets.


See [RichText](mcp://flutter/api/widgets/RichText) which provides a lower-level way to draw text.

## Implementation

```dart
const Text.rich(
  InlineSpan this.textSpan, {
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
}) : data = null,
     assert(
       textScaler == null || textScaleFactor == null,
       'textScaleFactor is deprecated and cannot be specified when textScaler is specified.',
     );
```