# subtitle property

[Widget](flutter-docs://api/widgets/Widget)? subtitle


Additional content displayed below the title.

Typically a [Text](flutter-docs://api/widgets/Text) widget.

If [isThreeLine](flutter-docs://api/material/ListTile/isThreeLine) is false, this should not wrap.

If [isThreeLine](flutter-docs://api/material/ListTile/isThreeLine) is true, this should be configured to take a maximum of
two lines. For example, you can use [Text.maxLines](flutter-docs://api/widgets/Text/maxLines) to enforce the number
of lines.

The subtitle's default [TextStyle](flutter-docs://api/painting/TextStyle) depends on [TextTheme.bodyMedium](flutter-docs://api/material/TextTheme/bodyMedium) except [TextStyle.color](flutter-docs://api/painting/TextStyle/color). The [TextStyle.color](flutter-docs://api/painting/TextStyle/color) depends on the value of [enabled](flutter-docs://api/material/ListTile/enabled) and [selected](flutter-docs://api/material/ListTile/selected).

When [enabled](flutter-docs://api/material/ListTile/enabled) is false, the text color is set to [ThemeData.disabledColor](flutter-docs://api/material/ThemeData/disabledColor).

When [selected](flutter-docs://api/material/ListTile/selected) is false, the text color is set to [ListTileTheme.textColor](flutter-docs://api/material/ListTileTheme/textColor) if it's not null and to [TextTheme.bodySmall](flutter-docs://api/material/TextTheme/bodySmall)'s color if [ListTileTheme.textColor](flutter-docs://api/material/ListTileTheme/textColor) is null.

## Implementation

```dart
final Widget? subtitle;
```