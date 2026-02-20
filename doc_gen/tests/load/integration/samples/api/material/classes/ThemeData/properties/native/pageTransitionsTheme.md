# pageTransitionsTheme property

[PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) pageTransitionsTheme


Default [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) transitions per [TargetPlatform](flutter-docs://api/foundation/TargetPlatform).

[MaterialPageRoute.buildTransitions](flutter-docs://api/material/MaterialRouteTransitionMixin/buildTransitions) delegates to a [platform](flutter-docs://api/material/ThemeData/platform) specific [PageTransitionsBuilder](flutter-docs://api/widgets/PageTransitionsBuilder). If a matching builder is not found, a builder
whose platform is null is used.

## Implementation

```dart
final PageTransitionsTheme pageTransitionsTheme;
```