# selectionColor property

[Color](mcp://flutter/api/dart-ui/Color)? selectionColor


The color to use when painting the selection.

This is ignored if [SelectionContainer.maybeOf](mcp://flutter/api/widgets/SelectionContainer/maybeOf) returns null
in the [BuildContext](mcp://flutter/api/widgets/BuildContext) of the [Text](mcp://flutter/api/widgets/Text) widget.

If null, the ambient [DefaultSelectionStyle](mcp://flutter/api/widgets/DefaultSelectionStyle) is used (if any); failing
that, the selection color defaults to [DefaultSelectionStyle.defaultColor](mcp://flutter/api/widgets/DefaultSelectionStyle/defaultColor) (semi-transparent grey).

## Implementation

```dart
final Color? selectionColor;
```