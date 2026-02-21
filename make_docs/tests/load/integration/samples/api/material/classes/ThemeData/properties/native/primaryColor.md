# primaryColor property

[Color](flutter-docs://api/dart-ui/Color) primaryColor


The background color for major parts of the app (toolbars, tab bars, etc)

The theme's [colorScheme](flutter-docs://api/material/ThemeData/colorScheme) property contains [ColorScheme.primary](flutter-docs://api/material/ColorScheme/primary), as
well as a color that contrasts well with the primary color called [ColorScheme.onPrimary](flutter-docs://api/material/ColorScheme/onPrimary). It might be simpler to just configure an app's
visuals in terms of the theme's [colorScheme](flutter-docs://api/material/ThemeData/colorScheme).

## Implementation

```dart
final Color primaryColor;
```