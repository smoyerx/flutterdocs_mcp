# cupertinoOverrideTheme property

[NoDefaultCupertinoThemeData](flutter-docs://api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme


Components of the [CupertinoThemeData](flutter-docs://api/cupertino/CupertinoThemeData) to override from the Material [ThemeData](flutter-docs://api/material/ThemeData) adaptation.

By default, [cupertinoOverrideTheme](flutter-docs://api/material/ThemeData/cupertinoOverrideTheme) is null and Cupertino widgets
descendant to the Material [Theme](flutter-docs://api/material/Theme) will adhere to a [CupertinoTheme](flutter-docs://api/cupertino/CupertinoTheme) derived from the Material [ThemeData](flutter-docs://api/material/ThemeData). e.g. [ThemeData](flutter-docs://api/material/ThemeData)'s [ColorScheme](flutter-docs://api/material/ColorScheme) will also inform the [CupertinoThemeData](flutter-docs://api/cupertino/CupertinoThemeData)'s `primaryColor` etc.

This cascading effect for individual attributes of the [CupertinoThemeData](flutter-docs://api/cupertino/CupertinoThemeData) can be overridden using attributes of this [cupertinoOverrideTheme](flutter-docs://api/material/ThemeData/cupertinoOverrideTheme).

## Implementation

```dart
final NoDefaultCupertinoThemeData? cupertinoOverrideTheme;
```