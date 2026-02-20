# style property

[TextStyle](flutter-docs://api/painting/TextStyle)? style


If non-null, the style to use for this text.

If the style's "inherit" property is true, the style will be merged with
the closest enclosing [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle). Otherwise, the style will
replace the closest enclosing [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle).

## Implementation

```dart
final TextStyle? style;
```