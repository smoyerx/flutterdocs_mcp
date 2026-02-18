# subtitle property

[Widget](mcp://flutter/api/widgets/Widget)? subtitle


Additional content displayed below the title.

Typically a [Text](mcp://flutter/api/widgets/Text) widget.

If [isThreeLine](mcp://flutter/api/material/ListTile/isThreeLine) is false, this should not wrap.

If [isThreeLine](mcp://flutter/api/material/ListTile/isThreeLine) is true, this should be configured to take a maximum of
two lines. For example, you can use [Text.maxLines](mcp://flutter/api/widgets/Text/maxLines) to enforce the number
of lines.

The subtitle's default [TextStyle](mcp://flutter/api/painting/TextStyle) depends on [TextTheme.bodyMedium](mcp://flutter/api/material/TextTheme/bodyMedium) except [TextStyle.color](mcp://flutter/api/painting/TextStyle/color). The [TextStyle.color](mcp://flutter/api/painting/TextStyle/color) depends on the value of [enabled](mcp://flutter/api/material/ListTile/enabled) and [selected](mcp://flutter/api/material/ListTile/selected).

When [enabled](mcp://flutter/api/material/ListTile/enabled) is false, the text color is set to [ThemeData.disabledColor](mcp://flutter/api/material/ThemeData/disabledColor).

When [selected](mcp://flutter/api/material/ListTile/selected) is false, the text color is set to [ListTileTheme.textColor](mcp://flutter/api/material/ListTileTheme/textColor) if it's not null and to [TextTheme.bodySmall](mcp://flutter/api/material/TextTheme/bodySmall)'s color if [ListTileTheme.textColor](mcp://flutter/api/material/ListTileTheme/textColor) is null.

## Implementation

```dart
final Widget? subtitle;
```