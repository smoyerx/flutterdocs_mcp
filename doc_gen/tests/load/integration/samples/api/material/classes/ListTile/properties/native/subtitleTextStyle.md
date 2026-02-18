# subtitleTextStyle property

[TextStyle](mcp://flutter/api/painting/TextStyle)? subtitleTextStyle


The text style for ListTile's [subtitle](mcp://flutter/api/material/ListTile/subtitle).

If this property is null, then [ListTileThemeData.subtitleTextStyle](mcp://flutter/api/material/ListTileThemeData/subtitleTextStyle) is used.
If that is also null and [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) is true, [TextTheme.bodyMedium](mcp://flutter/api/material/TextTheme/bodyMedium) with [ColorScheme.onSurfaceVariant](mcp://flutter/api/material/ColorScheme/onSurfaceVariant) will be used, otherwise [TextTheme.bodyMedium](mcp://flutter/api/material/TextTheme/bodyMedium) with [TextTheme.bodySmall](mcp://flutter/api/material/TextTheme/bodySmall) color will be used.

## Implementation

```dart
final TextStyle? subtitleTextStyle;
```