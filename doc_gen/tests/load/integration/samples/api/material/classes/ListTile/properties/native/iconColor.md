# iconColor property

[Color](mcp://flutter/api/dart-ui/Color)? iconColor


Defines the default color for [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) icons.

If this property is null and [selected](mcp://flutter/api/material/ListTile/selected) is false then [ListTileThemeData.iconColor](mcp://flutter/api/material/ListTileThemeData/iconColor) is used. If that is also null and [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) is true, [ColorScheme.onSurfaceVariant](mcp://flutter/api/material/ColorScheme/onSurfaceVariant) is used, otherwise if [ThemeData.brightness](mcp://flutter/api/material/ThemeData/brightness) is [Brightness.light](mcp://flutter/api/dart-ui/Brightness), [Colors.black54](mcp://flutter/api/material/Colors/black54) is used,
and if [ThemeData.brightness](mcp://flutter/api/material/ThemeData/brightness) is [Brightness.dark](mcp://flutter/api/dart-ui/Brightness), the value is null.

If this property is null and [selected](mcp://flutter/api/material/ListTile/selected) is true then [ListTileThemeData.selectedColor](mcp://flutter/api/material/ListTileThemeData/selectedColor) is used. If that is also null then [ColorScheme.primary](mcp://flutter/api/material/ColorScheme/primary) is used.

If this color is a [WidgetStateColor](mcp://flutter/api/widgets/WidgetStateColor) it will be resolved against [WidgetState.selected](mcp://flutter/api/widgets/WidgetState) and [WidgetState.disabled](mcp://flutter/api/widgets/WidgetState) states.

See also:

- [ListTileTheme.of](mcp://flutter/api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](mcp://flutter/api/material/ListTileTheme)'s
[ListTileThemeData](mcp://flutter/api/material/ListTileThemeData).


## Implementation

```dart
final Color? iconColor;
```