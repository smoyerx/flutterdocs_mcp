# Text.rich constructor

const Text.rich(
[InlineSpan](flutter-docs://api/painting/InlineSpan) textSpan, {
[Key](flutter-docs://api/foundation/Key)? key,
[TextStyle](flutter-docs://api/painting/TextStyle)? style,
[StrutStyle](flutter-docs://api/painting/StrutStyle)? strutStyle,
[TextAlign](flutter-docs://api/dart-ui/TextAlign)? textAlign,
[TextDirection](flutter-docs://api/dart-ui/TextDirection)? textDirection,
[Locale](flutter-docs://api/dart-ui/Locale)? locale,
[bool](flutter-docs://api/dart-core/bool)? softWrap,
[TextOverflow](flutter-docs://api/painting/TextOverflow)? overflow,
@[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.') [double](flutter-docs://api/dart-core/double)? textScaleFactor,
[TextScaler](flutter-docs://api/painting/TextScaler)? textScaler,
[int](flutter-docs://api/dart-core/int)? maxLines,
[String](flutter-docs://api/dart-core/String)? semanticsLabel,
[String](flutter-docs://api/dart-core/String)? semanticsIdentifier,
[TextWidthBasis](flutter-docs://api/painting/TextWidthBasis)? textWidthBasis,
[TextHeightBehavior](flutter-docs://api/dart-ui/TextHeightBehavior)? textHeightBehavior,
[Color](flutter-docs://api/dart-ui/Color)? selectionColor,
})

Creates a text widget with a [InlineSpan](flutter-docs://api/painting/InlineSpan).

The following subclasses of [InlineSpan](flutter-docs://api/painting/InlineSpan) may be used to build rich text:

- [TextSpan](flutter-docs://api/painting/TextSpan) s define text and children [InlineSpan](flutter-docs://api/painting/InlineSpan) s.
- [WidgetSpan](flutter-docs://api/widgets/WidgetSpan) s define embedded inline widgets.


See [RichText](flutter-docs://api/widgets/RichText) which provides a lower-level way to draw text.

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