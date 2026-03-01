# textColor property

[Color](flutter-docs://api/dart-ui/Color)? textColor


Defines the text color for the [title](flutter-docs://api/material/ListTile/title), [subtitle](flutter-docs://api/material/ListTile/subtitle), [leading](flutter-docs://api/material/ListTile/leading), and [trailing](flutter-docs://api/material/ListTile/trailing).

If this property is null and [selected](flutter-docs://api/material/ListTile/selected) is false then [ListTileThemeData.textColor](flutter-docs://api/material/ListTileThemeData/textColor) is used. If that is also null then default text color is used for the [title](flutter-docs://api/material/ListTile/title), [subtitle](flutter-docs://api/material/ListTile/subtitle) [leading](flutter-docs://api/material/ListTile/leading), and [trailing](flutter-docs://api/material/ListTile/trailing). Except for [subtitle](flutter-docs://api/material/ListTile/subtitle), if [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is false, [TextTheme.bodySmall](flutter-docs://api/material/TextTheme/bodySmall) is used.

If this property is null and [selected](flutter-docs://api/material/ListTile/selected) is true then [ListTileThemeData.selectedColor](flutter-docs://api/material/ListTileThemeData/selectedColor) is used. If that is also null then [ColorScheme.primary](flutter-docs://api/material/ColorScheme/primary) is used.

If this color is a [WidgetStateColor](flutter-docs://api/widgets/WidgetStateColor) it will be resolved against [WidgetState.selected](flutter-docs://api/widgets/WidgetState) and [WidgetState.disabled](flutter-docs://api/widgets/WidgetState) states.

See also:

- [ListTileTheme.of](flutter-docs://api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](flutter-docs://api/material/ListTileTheme)'s
[ListTileThemeData](flutter-docs://api/material/ListTileThemeData).


## Implementation

```dart
final Color? textColor;
```