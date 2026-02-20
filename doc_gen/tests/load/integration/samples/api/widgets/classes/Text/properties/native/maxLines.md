# maxLines property

[int](flutter-docs://api/dart-core/int)? maxLines


An optional maximum number of lines for the text to span, wrapping if necessary.
If the text exceeds the given number of lines, it will be truncated according
to [overflow](flutter-docs://api/widgets/Text/overflow).

If this is 1, text will not wrap. Otherwise, text will be wrapped at the
edge of the box.

If this is null, but there is an ambient [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle) that specifies
an explicit number for its [DefaultTextStyle.maxLines](flutter-docs://api/widgets/DefaultTextStyle/maxLines), then the [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle) value will take precedence. You can use a [RichText](flutter-docs://api/widgets/RichText) widget directly to entirely override the [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle).

## Implementation

```dart
final int? maxLines;
```