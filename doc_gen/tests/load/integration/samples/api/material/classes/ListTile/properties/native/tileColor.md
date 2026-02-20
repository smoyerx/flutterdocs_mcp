# tileColor property

[Color](flutter-docs://api/dart-ui/Color)? tileColor


Defines the background color of `ListTile` when [selected](flutter-docs://api/material/ListTile/selected) is false.

If this property is null and [selected](flutter-docs://api/material/ListTile/selected) is false then [ListTileThemeData.tileColor](flutter-docs://api/material/ListTileThemeData/tileColor) is used. If that is also null and [selected](flutter-docs://api/material/ListTile/selected) is true, [selectedTileColor](flutter-docs://api/material/ListTile/selectedTileColor) is used.
When that is also null, the [ListTileTheme.selectedTileColor](flutter-docs://api/material/ListTileTheme/selectedTileColor) is used, otherwise [Colors.transparent](flutter-docs://api/material/Colors/transparent) is used.

## Implementation

```dart
final Color? tileColor;
```