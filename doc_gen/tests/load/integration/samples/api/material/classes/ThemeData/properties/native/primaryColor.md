# primaryColor property

[Color](mcp://flutter/api/dart-ui/Color) primaryColor


The background color for major parts of the app (toolbars, tab bars, etc)

The theme's [colorScheme](mcp://flutter/api/material/ThemeData/colorScheme) property contains [ColorScheme.primary](mcp://flutter/api/material/ColorScheme/primary), as
well as a color that contrasts well with the primary color called [ColorScheme.onPrimary](mcp://flutter/api/material/ColorScheme/onPrimary). It might be simpler to just configure an app's
visuals in terms of the theme's [colorScheme](mcp://flutter/api/material/ThemeData/colorScheme).

## Implementation

```dart
final Color primaryColor;
```