# brightness property

[Brightness](mcp://flutter/api/dart-ui/Brightness) get brightness

The overall theme brightness.

The default [TextStyle](mcp://flutter/api/painting/TextStyle) color for the [textTheme](mcp://flutter/api/material/ThemeData/textTheme) is black if the
theme is constructed with [Brightness.light](mcp://flutter/api/dart-ui/Brightness) and white if the
theme is constructed with [Brightness.dark](mcp://flutter/api/dart-ui/Brightness).

## Implementation

```dart
Brightness get brightness => colorScheme.brightness;
```