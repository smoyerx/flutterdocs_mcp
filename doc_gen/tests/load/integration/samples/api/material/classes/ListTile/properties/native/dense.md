# dense property

[bool](mcp://flutter/api/dart-core/bool)? dense


Whether this list tile is part of a vertically dense list.

If this property is null then its value is based on [ListTileTheme.dense](mcp://flutter/api/material/ListTileTheme/dense).

Dense list tiles default to a smaller height.

It is not recommended to set [dense](mcp://flutter/api/material/ListTile/dense) to true when [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) is true.

## Implementation

```dart
final bool? dense;
```