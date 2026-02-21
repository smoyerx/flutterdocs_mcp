# applyElevationOverlayColor property

[bool](flutter-docs://api/dart-core/bool) applyElevationOverlayColor


Apply a semi-transparent overlay color on Material surfaces to indicate
elevation for dark themes.

If [useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) is true, then this flag is ignored as there is a new [Material.surfaceTintColor](flutter-docs://api/material/Material/surfaceTintColor) used to create an overlay for Material 3.
This flag is meant only for the Material 2 elevation overlay for dark
themes.

Material drop shadows can be difficult to see in a dark theme, so the
elevation of a surface should be portrayed with an "overlay" in addition
to the shadow. As the elevation of the component increases, the
overlay increases in opacity. [applyElevationOverlayColor](flutter-docs://api/material/ThemeData/applyElevationOverlayColor) turns the
application of this overlay on or off for dark themes.

If true and [brightness](flutter-docs://api/material/ThemeData/brightness) is [Brightness.dark](flutter-docs://api/dart-ui/Brightness), a
semi-transparent version of [ColorScheme.onSurface](flutter-docs://api/material/ColorScheme/onSurface) will be
applied on top of [Material](flutter-docs://api/material/Material) widgets that have a [ColorScheme.surface](flutter-docs://api/material/ColorScheme/surface) color. The level of transparency is based on [Material.elevation](flutter-docs://api/material/Material/elevation) as
per the Material Dark theme specification.

If false the surface color will be used unmodified.

Defaults to false in order to maintain backwards compatibility with
apps that were built before the Material Dark theme specification
was published. New apps should set this to true for any themes
where [brightness](flutter-docs://api/material/ThemeData/brightness) is [Brightness.dark](flutter-docs://api/dart-ui/Brightness).

See also:

- [Material.elevation](flutter-docs://api/material/Material/elevation), which effects the level of transparency of the
overlay color.
- [ElevationOverlay.applyOverlay](flutter-docs://api/material/ElevationOverlay/applyOverlay), which is used by [Material](flutter-docs://api/material/Material) to apply
the overlay color to its surface color.
- [material.io/design/color/dark-theme.html](https://material.io/design/color/dark-theme.html), which specifies how
the overlay should be applied.


## Implementation

```dart
final bool applyElevationOverlayColor;
```