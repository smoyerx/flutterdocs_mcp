# iconColor property

[Color](flutter-docs://api/dart-ui/Color)? iconColor


Defines the default color for [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) icons.

If this property is null and [selected](flutter-docs://api/material/ListTile/selected) is false then [ListTileThemeData.iconColor](flutter-docs://api/material/ListTileThemeData/iconColor) is used. If that is also null and [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is true, [ColorScheme.onSurfaceVariant](flutter-docs://api/material/ColorScheme/onSurfaceVariant) is used, otherwise if [ThemeData.brightness](flutter-docs://api/material/ThemeData/brightness) is [Brightness.light](flutter-docs://api/dart-ui/Brightness), [Colors.black54](flutter-docs://api/material/Colors/black54) is used,
and if [ThemeData.brightness](flutter-docs://api/material/ThemeData/brightness) is [Brightness.dark](flutter-docs://api/dart-ui/Brightness), the value is null.

If this property is null and [selected](flutter-docs://api/material/ListTile/selected) is true then [ListTileThemeData.selectedColor](flutter-docs://api/material/ListTileThemeData/selectedColor) is used. If that is also null then [ColorScheme.primary](flutter-docs://api/material/ColorScheme/primary) is used.

If this color is a [WidgetStateColor](flutter-docs://api/widgets/WidgetStateColor) it will be resolved against [WidgetState.selected](flutter-docs://api/widgets/WidgetState) and [WidgetState.disabled](flutter-docs://api/widgets/WidgetState) states.

See also:

- [ListTileTheme.of](flutter-docs://api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](flutter-docs://api/material/ListTileTheme)'s
[ListTileThemeData](flutter-docs://api/material/ListTileThemeData).


## Implementation

```dart
final Color? iconColor;
```