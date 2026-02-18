# leadingAndTrailingTextStyle property

[TextStyle](mcp://flutter/api/painting/TextStyle)? leadingAndTrailingTextStyle


The text style for ListTile's [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing).

If this property is null, then [ListTileThemeData.leadingAndTrailingTextStyle](mcp://flutter/api/material/ListTileThemeData/leadingAndTrailingTextStyle) is used.
If that is also null and [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) is true, [TextTheme.labelSmall](mcp://flutter/api/material/TextTheme/labelSmall) with [ColorScheme.onSurfaceVariant](mcp://flutter/api/material/ColorScheme/onSurfaceVariant) will be used, otherwise [TextTheme.bodyMedium](mcp://flutter/api/material/TextTheme/bodyMedium) will be used.

## Implementation

```dart
final TextStyle? leadingAndTrailingTextStyle;
```