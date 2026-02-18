# textColor property

[Color](mcp://flutter/api/dart-ui/Color)? textColor


Defines the text color for the [title](mcp://flutter/api/material/ListTile/title), [subtitle](mcp://flutter/api/material/ListTile/subtitle), [leading](mcp://flutter/api/material/ListTile/leading), and [trailing](mcp://flutter/api/material/ListTile/trailing).

If this property is null and [selected](mcp://flutter/api/material/ListTile/selected) is false then [ListTileThemeData.textColor](mcp://flutter/api/material/ListTileThemeData/textColor) is used. If that is also null then default text color is used for the [title](mcp://flutter/api/material/ListTile/title), [subtitle](mcp://flutter/api/material/ListTile/subtitle)[leading](mcp://flutter/api/material/ListTile/leading), and [trailing](mcp://flutter/api/material/ListTile/trailing). Except for [subtitle](mcp://flutter/api/material/ListTile/subtitle), if [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) is false, [TextTheme.bodySmall](mcp://flutter/api/material/TextTheme/bodySmall) is used.

If this property is null and [selected](mcp://flutter/api/material/ListTile/selected) is true then [ListTileThemeData.selectedColor](mcp://flutter/api/material/ListTileThemeData/selectedColor) is used. If that is also null then [ColorScheme.primary](mcp://flutter/api/material/ColorScheme/primary) is used.

If this color is a [WidgetStateColor](mcp://flutter/api/widgets/WidgetStateColor) it will be resolved against [WidgetState.selected](mcp://flutter/api/widgets/WidgetState) and [WidgetState.disabled](mcp://flutter/api/widgets/WidgetState) states.

See also:

- [ListTileTheme.of](mcp://flutter/api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](mcp://flutter/api/material/ListTileTheme)'s
[ListTileThemeData](mcp://flutter/api/material/ListTileThemeData).


## Implementation

```dart
final Color? textColor;
```