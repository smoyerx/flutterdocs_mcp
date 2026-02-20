# titleTextStyle property

[TextStyle](flutter-docs://api/painting/TextStyle)? titleTextStyle


The text style for ListTile's [title](flutter-docs://api/material/ListTile/title).

If this property is null, then [ListTileThemeData.titleTextStyle](flutter-docs://api/material/ListTileThemeData/titleTextStyle) is used.
If that is also null and [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is true, [TextTheme.bodyLarge](flutter-docs://api/material/TextTheme/bodyLarge) with [ColorScheme.onSurface](flutter-docs://api/material/ColorScheme/onSurface) will be used. Otherwise, If ListTile style is [ListTileStyle.list](flutter-docs://api/material/ListTileStyle), [TextTheme.titleMedium](flutter-docs://api/material/TextTheme/titleMedium) will be used and if ListTile style
is [ListTileStyle.drawer](flutter-docs://api/material/ListTileStyle), [TextTheme.bodyLarge](flutter-docs://api/material/TextTheme/bodyLarge) will be used.

## Implementation

```dart
final TextStyle? titleTextStyle;
```