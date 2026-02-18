# cupertinoOverrideTheme property

[NoDefaultCupertinoThemeData](mcp://flutter/api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme


Components of the [CupertinoThemeData](mcp://flutter/api/cupertino/CupertinoThemeData) to override from the Material [ThemeData](mcp://flutter/api/material/ThemeData) adaptation.

By default, [cupertinoOverrideTheme](mcp://flutter/api/material/ThemeData/cupertinoOverrideTheme) is null and Cupertino widgets
descendant to the Material [Theme](mcp://flutter/api/material/Theme) will adhere to a [CupertinoTheme](mcp://flutter/api/cupertino/CupertinoTheme) derived from the Material [ThemeData](mcp://flutter/api/material/ThemeData). e.g. [ThemeData](mcp://flutter/api/material/ThemeData)'s [ColorScheme](mcp://flutter/api/material/ColorScheme) will also inform the [CupertinoThemeData](mcp://flutter/api/cupertino/CupertinoThemeData)'s `primaryColor` etc.

This cascading effect for individual attributes of the [CupertinoThemeData](mcp://flutter/api/cupertino/CupertinoThemeData) can be overridden using attributes of this [cupertinoOverrideTheme](mcp://flutter/api/material/ThemeData/cupertinoOverrideTheme).

## Implementation

```dart
final NoDefaultCupertinoThemeData? cupertinoOverrideTheme;
```