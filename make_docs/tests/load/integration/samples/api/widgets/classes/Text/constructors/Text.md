# Text constructor

const Text(
[String](flutter-docs://api/dart-core/String) data, {
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

Creates a text widget.

If the `style` argument is null, the text will use the style from the
closest enclosing [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle).

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