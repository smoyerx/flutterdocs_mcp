# colorScheme property

[ColorScheme](flutter-docs://api/material/ColorScheme) colorScheme


A set of 45 colors based on the [Material spec](https://m3.material.io/styles/color/the-color-system/color-roles) that can be used to configure the color properties of most components.

This property was added much later than the theme's set of highly specific
colors, like [cardColor](flutter-docs://api/material/ThemeData/cardColor), [canvasColor](flutter-docs://api/material/ThemeData/canvasColor) etc. New components can be defined
exclusively in terms of [colorScheme](flutter-docs://api/material/ThemeData/colorScheme). Existing components will gradually
migrate to it, to the extent that is possible without significant
backwards compatibility breaks.

## Implementation

```dart
final ColorScheme colorScheme;
```