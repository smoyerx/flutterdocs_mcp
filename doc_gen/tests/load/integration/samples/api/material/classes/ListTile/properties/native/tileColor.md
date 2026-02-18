# tileColor property

[Color](mcp://flutter/api/dart-ui/Color)? tileColor


Defines the background color of `ListTile` when [selected](mcp://flutter/api/material/ListTile/selected) is false.

If this property is null and [selected](mcp://flutter/api/material/ListTile/selected) is false then [ListTileThemeData.tileColor](mcp://flutter/api/material/ListTileThemeData/tileColor) is used. If that is also null and [selected](mcp://flutter/api/material/ListTile/selected) is true, [selectedTileColor](mcp://flutter/api/material/ListTile/selectedTileColor) is used.
When that is also null, the [ListTileTheme.selectedTileColor](mcp://flutter/api/material/ListTileTheme/selectedTileColor) is used, otherwise [Colors.transparent](mcp://flutter/api/material/Colors/transparent) is used.

## Implementation

```dart
final Color? tileColor;
```