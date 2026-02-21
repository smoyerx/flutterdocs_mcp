# dense property

[bool](flutter-docs://api/dart-core/bool)? dense


Whether this list tile is part of a vertically dense list.

If this property is null then its value is based on [ListTileTheme.dense](flutter-docs://api/material/ListTileTheme/dense).

Dense list tiles default to a smaller height.

It is not recommended to set [dense](flutter-docs://api/material/ListTile/dense) to true when [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is true.

## Implementation

```dart
final bool? dense;
```