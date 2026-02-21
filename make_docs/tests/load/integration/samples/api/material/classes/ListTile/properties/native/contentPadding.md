# contentPadding property

[EdgeInsetsGeometry](flutter-docs://api/painting/EdgeInsetsGeometry)? contentPadding


The tile's internal padding.

Insets a [ListTile](flutter-docs://api/material/ListTile)'s contents: its [leading](flutter-docs://api/material/ListTile/leading), [title](flutter-docs://api/material/ListTile/title), [subtitle](flutter-docs://api/material/ListTile/subtitle), and [trailing](flutter-docs://api/material/ListTile/trailing) widgets.

If this property is null, then [ListTileThemeData.contentPadding](flutter-docs://api/material/ListTileThemeData/contentPadding) is used. If that is also
null and [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is true, then a default value of `EdgeInsetsDirectional.only(start: 16.0, end: 24.0)` will be used. Otherwise, a default value
of `EdgeInsets.symmetric(horizontal: 16.0)` will be used.

## Implementation

```dart
final EdgeInsetsGeometry? contentPadding;
```