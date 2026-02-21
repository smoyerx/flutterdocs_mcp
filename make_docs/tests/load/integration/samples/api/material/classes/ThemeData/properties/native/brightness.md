# brightness property

[Brightness](flutter-docs://api/dart-ui/Brightness) get brightness

The overall theme brightness.

The default [TextStyle](flutter-docs://api/painting/TextStyle) color for the [textTheme](flutter-docs://api/material/ThemeData/textTheme) is black if the
theme is constructed with [Brightness.light](flutter-docs://api/dart-ui/Brightness) and white if the
theme is constructed with [Brightness.dark](flutter-docs://api/dart-ui/Brightness).

## Implementation

```dart
Brightness get brightness => colorScheme.brightness;
```