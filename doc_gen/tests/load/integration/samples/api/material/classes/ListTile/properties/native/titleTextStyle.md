# titleTextStyle property

[TextStyle](mcp://flutter/api/painting/TextStyle)? titleTextStyle


The text style for ListTile's [title](mcp://flutter/api/material/ListTile/title).

If this property is null, then [ListTileThemeData.titleTextStyle](mcp://flutter/api/material/ListTileThemeData/titleTextStyle) is used.
If that is also null and [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) is true, [TextTheme.bodyLarge](mcp://flutter/api/material/TextTheme/bodyLarge) with [ColorScheme.onSurface](mcp://flutter/api/material/ColorScheme/onSurface) will be used. Otherwise, If ListTile style is [ListTileStyle.list](mcp://flutter/api/material/ListTileStyle), [TextTheme.titleMedium](mcp://flutter/api/material/TextTheme/titleMedium) will be used and if ListTile style
is [ListTileStyle.drawer](mcp://flutter/api/material/ListTileStyle), [TextTheme.bodyLarge](mcp://flutter/api/material/TextTheme/bodyLarge) will be used.

## Implementation

```dart
final TextStyle? titleTextStyle;
```