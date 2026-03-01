# textScaleFactor property

1. @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.')

[double](flutter-docs://api/dart-core/double)? textScaleFactor


Deprecated. Will be removed in a future version of Flutter. Use [textScaler](flutter-docs://api/widgets/Text/textScaler) instead.

The number of font pixels for each logical pixel.

For example, if the text scale factor is 1.5, text will be 50% larger than
the specified font size.

The value given to the constructor as textScaleFactor. If null, will
use the [MediaQueryData.textScaleFactor](flutter-docs://api/widgets/MediaQueryData/textScaleFactor) obtained from the ambient [MediaQuery](flutter-docs://api/widgets/MediaQuery), or 1.0 if there is no [MediaQuery](flutter-docs://api/widgets/MediaQuery) in scope.

## Implementation

```dart
@Deprecated(
  'Use textScaler instead. '
  'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. '
  'This feature was deprecated after v3.12.0-2.0.pre.',
)
final double? textScaleFactor;
```