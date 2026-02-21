# ThemeData.light constructor

ThemeData.light({
[bool](flutter-docs://api/dart-core/bool)? useMaterial3,
})

A default light theme.

This theme does not contain text geometry. Instead, it is expected that
this theme is localized using text geometry using [ThemeData.localize](flutter-docs://api/material/ThemeData/localize).

## Implementation

```dart
factory ThemeData.light({bool? useMaterial3}) =>
    ThemeData(brightness: Brightness.light, useMaterial3: useMaterial3);
```