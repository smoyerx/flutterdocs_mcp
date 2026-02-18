# ThemeData.from constructor

ThemeData.from({
required [ColorScheme](mcp://flutter/api/material/ColorScheme) colorScheme,
[TextTheme](mcp://flutter/api/material/TextTheme)? textTheme,
[bool](mcp://flutter/api/dart-core/bool)? useMaterial3,
})

Create a [ThemeData](mcp://flutter/api/material/ThemeData) based on the colors in the given `colorScheme` and
text styles of the optional `textTheme`.

If `colorScheme`.brightness is [Brightness.dark](mcp://flutter/api/dart-ui/Brightness) then [ThemeData.applyElevationOverlayColor](mcp://flutter/api/material/ThemeData/applyElevationOverlayColor) will be set to true to support
the Material dark theme method for indicating elevation by applying
a semi-transparent onSurface color on top of the surface color.

This is the recommended method to theme your application. As we move
forward we will be converting all the widget implementations to only use
colors or colors derived from those in [ColorScheme](mcp://flutter/api/material/ColorScheme).

This example will set up an application to use the baseline Material
Design light and dark themes.



```dart
MaterialApp(
  theme: ThemeData.from(colorScheme: const ColorScheme.light()),
  darkTheme: ThemeData.from(colorScheme: const ColorScheme.dark()),
)
```

See [material.io/design/color/](https://material.io/design/color/) for
more discussion on how to pick the right colors.

## Implementation

```dart
factory ThemeData.from({
  required ColorScheme colorScheme,
  TextTheme? textTheme,
  bool? useMaterial3,
}) {
  final bool isDark = colorScheme.brightness == Brightness.dark;

  // For surfaces that use primary color in light themes and surface color in dark
  final Color primarySurfaceColor = isDark ? colorScheme.surface : colorScheme.primary;
  final Color onPrimarySurfaceColor = isDark ? colorScheme.onSurface : colorScheme.onPrimary;

  return ThemeData(
    colorScheme: colorScheme,
    brightness: colorScheme.brightness,
    primaryColor: primarySurfaceColor,
    canvasColor: colorScheme.surface,
    scaffoldBackgroundColor: colorScheme.surface,
    cardColor: colorScheme.surface,
    dividerColor: colorScheme.onSurface.withOpacity(0.12),
    dialogBackgroundColor: colorScheme.surface,
    indicatorColor: onPrimarySurfaceColor,
    textTheme: textTheme,
    applyElevationOverlayColor: isDark,
    useMaterial3: useMaterial3,
  );
}
```