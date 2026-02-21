# textDirection property

[TextDirection](flutter-docs://api/dart-ui/TextDirection)? textDirection


The directionality of the text.

This decides how [textAlign](flutter-docs://api/widgets/Text/textAlign) values like [TextAlign.start](flutter-docs://api/dart-ui/TextAlign) and [TextAlign.end](flutter-docs://api/dart-ui/TextAlign) are interpreted.

This is also used to disambiguate how to render bidirectional text. For
example, if the [data](flutter-docs://api/widgets/Text/data) is an English phrase followed by a Hebrew phrase,
in a [TextDirection.ltr](flutter-docs://api/dart-ui/TextDirection) context the English phrase will be on the left
and the Hebrew phrase to its right, while in a [TextDirection.rtl](flutter-docs://api/dart-ui/TextDirection) context, the English phrase will be on the right and the Hebrew phrase on
its left.

Defaults to the ambient [Directionality](flutter-docs://api/widgets/Directionality), if any.

## Implementation

```dart
final TextDirection? textDirection;
```