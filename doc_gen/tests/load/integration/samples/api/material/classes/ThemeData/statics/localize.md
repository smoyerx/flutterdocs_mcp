# localize static method

[ThemeData](mcp://flutter/api/material/ThemeData) localize(
[ThemeData](mcp://flutter/api/material/ThemeData) baseTheme,
[TextTheme](mcp://flutter/api/material/TextTheme) localTextGeometry
)

Returns a new theme built by merging the text geometry provided by the`localTextGeometry` theme with the `baseTheme`.

For those text styles in the `baseTheme` whose [TextStyle.inherit](mcp://flutter/api/painting/TextStyle/inherit) is set
to true, the returned theme's text styles inherit the geometric properties
of `localTextGeometry`. The resulting text styles' [TextStyle.inherit](mcp://flutter/api/painting/TextStyle/inherit) is
set to those provided by `localTextGeometry`.

## Implementation

```dart
static ThemeData localize(ThemeData baseTheme, TextTheme localTextGeometry) {
  // WARNING: this method memoizes the result in a cache based on the
  // previously seen baseTheme and localTextGeometry. Memoization is safe
  // because all inputs and outputs of this function are deeply immutable, and
  // the computations are referentially transparent. It only short-circuits
  // the computation if the new inputs are identical() to the previous ones.
  // It does not use the == operator, which performs a costly deep comparison.
  //
  // When changing this method, make sure the memoization logic is correct.
  // Remember:
  //
  // There are only two hard things in Computer Science: cache invalidation
  // and naming things. -- Phil Karlton

  return _localizedThemeDataCache.putIfAbsent(
    _IdentityThemeDataCacheKey(baseTheme, localTextGeometry),
    () {
      return baseTheme.copyWith(
        primaryTextTheme: localTextGeometry.merge(baseTheme.primaryTextTheme),
        textTheme: localTextGeometry.merge(baseTheme.textTheme),
      );
    },
  );
}
```