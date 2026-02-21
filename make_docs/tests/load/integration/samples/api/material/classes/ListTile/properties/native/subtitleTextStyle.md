# subtitleTextStyle property

[TextStyle](flutter-docs://api/painting/TextStyle)? subtitleTextStyle


The text style for ListTile's [subtitle](flutter-docs://api/material/ListTile/subtitle).

If this property is null, then [ListTileThemeData.subtitleTextStyle](flutter-docs://api/material/ListTileThemeData/subtitleTextStyle) is used.
If that is also null and [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is true, [TextTheme.bodyMedium](flutter-docs://api/material/TextTheme/bodyMedium) with [ColorScheme.onSurfaceVariant](flutter-docs://api/material/ColorScheme/onSurfaceVariant) will be used, otherwise [TextTheme.bodyMedium](flutter-docs://api/material/TextTheme/bodyMedium) with [TextTheme.bodySmall](flutter-docs://api/material/TextTheme/bodySmall) color will be used.

## Implementation

```dart
final TextStyle? subtitleTextStyle;
```