# ThemeData.fallback constructor

ThemeData.fallback({
[bool](mcp://flutter/api/dart-core/bool)? useMaterial3,
})

The default color theme. Same as [ThemeData.light](mcp://flutter/api/material/ThemeData/ThemeData.light).

This is used by [Theme.of](mcp://flutter/api/material/Theme/of) when no theme has been specified.

This theme does not contain text geometry. Instead, it is expected that
this theme is localized using text geometry using [ThemeData.localize](mcp://flutter/api/material/ThemeData/localize).

Most applications would use [Theme.of](mcp://flutter/api/material/Theme/of), which provides correct localized
text geometry.

## Implementation

```dart
factory ThemeData.fallback({bool? useMaterial3}) => ThemeData.light(useMaterial3: useMaterial3);
```