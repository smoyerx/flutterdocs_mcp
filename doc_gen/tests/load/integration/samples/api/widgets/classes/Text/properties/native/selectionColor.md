# selectionColor property

[Color](flutter-docs://api/dart-ui/Color)? selectionColor


The color to use when painting the selection.

This is ignored if [SelectionContainer.maybeOf](flutter-docs://api/widgets/SelectionContainer/maybeOf) returns null
in the [BuildContext](flutter-docs://api/widgets/BuildContext) of the [Text](flutter-docs://api/widgets/Text) widget.

If null, the ambient [DefaultSelectionStyle](flutter-docs://api/widgets/DefaultSelectionStyle) is used (if any); failing
that, the selection color defaults to [DefaultSelectionStyle.defaultColor](flutter-docs://api/widgets/DefaultSelectionStyle/defaultColor) (semi-transparent grey).

## Implementation

```dart
final Color? selectionColor;
```