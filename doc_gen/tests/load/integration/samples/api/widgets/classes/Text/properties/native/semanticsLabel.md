# semanticsLabel property

[String](flutter-docs://api/dart-core/String)? semanticsLabel


An alternative semantics label for this text.

If present, the semantics of this widget will contain this value instead
of the actual text. This will overwrite any of the semantics labels applied
directly to the [TextSpan](flutter-docs://api/painting/TextSpan) s.

This is useful for replacing abbreviations or shorthands with the full
text value:

```dart
const Text(r'$$', semanticsLabel: 'Double dollars')

```


## Implementation

```dart
final String? semanticsLabel;
```