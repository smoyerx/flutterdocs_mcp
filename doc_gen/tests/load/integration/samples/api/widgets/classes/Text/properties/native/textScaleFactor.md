# textScaleFactor property

1. @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.')

[double](mcp://flutter/api/dart-core/double)? textScaleFactor


Deprecated. Will be removed in a future version of Flutter. Use[textScaler](mcp://flutter/api/widgets/Text/textScaler) instead.

The number of font pixels for each logical pixel.

For example, if the text scale factor is 1.5, text will be 50% larger than
the specified font size.

The value given to the constructor as textScaleFactor. If null, will
use the [MediaQueryData.textScaleFactor](mcp://flutter/api/widgets/MediaQueryData/textScaleFactor) obtained from the ambient [MediaQuery](mcp://flutter/api/widgets/MediaQuery), or 1.0 if there is no [MediaQuery](mcp://flutter/api/widgets/MediaQuery) in scope.

## Implementation

```dart
@Deprecated(
  'Use textScaler instead. '
  'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. '
  'This feature was deprecated after v3.12.0-2.0.pre.',
)
final double? textScaleFactor;
```