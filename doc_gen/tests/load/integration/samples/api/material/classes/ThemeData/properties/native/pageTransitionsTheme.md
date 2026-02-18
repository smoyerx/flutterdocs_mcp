# pageTransitionsTheme property

[PageTransitionsTheme](mcp://flutter/api/material/PageTransitionsTheme) pageTransitionsTheme


Default [MaterialPageRoute](mcp://flutter/api/material/MaterialPageRoute) transitions per [TargetPlatform](mcp://flutter/api/foundation/TargetPlatform).

[MaterialPageRoute.buildTransitions](mcp://flutter/api/material/MaterialRouteTransitionMixin/buildTransitions) delegates to a [platform](mcp://flutter/api/material/ThemeData/platform) specific [PageTransitionsBuilder](mcp://flutter/api/widgets/PageTransitionsBuilder). If a matching builder is not found, a builder
whose platform is null is used.

## Implementation

```dart
final PageTransitionsTheme pageTransitionsTheme;
```