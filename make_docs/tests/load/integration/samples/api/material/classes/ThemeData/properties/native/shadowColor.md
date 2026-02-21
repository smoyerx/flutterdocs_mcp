# shadowColor property

[Color](flutter-docs://api/dart-ui/Color) shadowColor


The color that the [Material](flutter-docs://api/material/Material) widget uses to draw elevation shadows.

Defaults to fully opaque black.

Shadows can be difficult to see in a dark theme, so the elevation of a
surface should be rendered with an "overlay" in addition to the shadow.
As the elevation of the component increases, the overlay increases in
opacity. The [applyElevationOverlayColor](flutter-docs://api/material/ThemeData/applyElevationOverlayColor) property turns the elevation
overlay on or off for dark themes.

## Implementation

```dart
final Color shadowColor;
```