# leadingAndTrailingTextStyle property

[TextStyle](flutter-docs://api/painting/TextStyle)? leadingAndTrailingTextStyle


The text style for ListTile's [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing).

If this property is null, then [ListTileThemeData.leadingAndTrailingTextStyle](flutter-docs://api/material/ListTileThemeData/leadingAndTrailingTextStyle) is used.
If that is also null and [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is true, [TextTheme.labelSmall](flutter-docs://api/material/TextTheme/labelSmall) with [ColorScheme.onSurfaceVariant](flutter-docs://api/material/ColorScheme/onSurfaceVariant) will be used, otherwise [TextTheme.bodyMedium](flutter-docs://api/material/TextTheme/bodyMedium) will be used.

## Implementation

```dart
final TextStyle? leadingAndTrailingTextStyle;
```