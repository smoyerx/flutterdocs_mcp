# platform property

[TargetPlatform](mcp://flutter/api/foundation/TargetPlatform) platform


The platform the material widgets should adapt to target.

Defaults to the current platform, as exposed by [defaultTargetPlatform](mcp://flutter/api/foundation/defaultTargetPlatform).
This should be used in order to style UI elements according to platform
conventions.

Widgets from the material library should use this getter (via [Theme.of](mcp://flutter/api/material/Theme/of))
to determine the current platform for the purpose of emulating the
platform behavior (e.g. scrolling or haptic effects). Widgets and render
objects at lower layers that try to emulate the underlying platform
can depend on [defaultTargetPlatform](mcp://flutter/api/foundation/defaultTargetPlatform) directly, or may require
that the target platform be provided as an argument. The [dart:io.Platform](mcp://flutter/api/dart-io/Platform) object should only be used directly when it's critical
to actually know the current platform, without any overrides possible (for
example, when a system API is about to be called).

In a test environment, the platform returned is [TargetPlatform.android](mcp://flutter/api/foundation/TargetPlatform) regardless of the host platform. (Android was chosen because the tests
were originally written assuming Android-like behavior, and we added
platform adaptations for other platforms later). Tests can check behavior
for other platforms by setting the [platform](mcp://flutter/api/material/ThemeData/platform) of the [Theme](mcp://flutter/api/material/Theme) explicitly to
another [TargetPlatform](mcp://flutter/api/foundation/TargetPlatform) value, or by setting [debugDefaultTargetPlatformOverride](mcp://flutter/api/foundation/debugDefaultTargetPlatformOverride).

Determines the defaults for [typography](mcp://flutter/api/material/ThemeData/typography) and [materialTapTargetSize](mcp://flutter/api/material/ThemeData/materialTapTargetSize).

## Implementation

```dart
final TargetPlatform platform;
```