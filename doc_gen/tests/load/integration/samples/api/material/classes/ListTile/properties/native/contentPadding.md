# contentPadding property

[EdgeInsetsGeometry](mcp://flutter/api/painting/EdgeInsetsGeometry)? contentPadding


The tile's internal padding.

Insets a [ListTile](mcp://flutter/api/material/ListTile)'s contents: its [leading](mcp://flutter/api/material/ListTile/leading), [title](mcp://flutter/api/material/ListTile/title), [subtitle](mcp://flutter/api/material/ListTile/subtitle), and [trailing](mcp://flutter/api/material/ListTile/trailing) widgets.

If this property is null, then [ListTileThemeData.contentPadding](mcp://flutter/api/material/ListTileThemeData/contentPadding) is used. If that is also
null and [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) is true, then a default value of `EdgeInsetsDirectional.only(start: 16.0, end: 24.0)` will be used. Otherwise, a default value
of `EdgeInsets.symmetric(horizontal: 16.0)` will be used.

## Implementation

```dart
final EdgeInsetsGeometry? contentPadding;
```