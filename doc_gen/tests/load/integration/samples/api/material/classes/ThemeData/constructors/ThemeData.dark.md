# ThemeData.dark constructor

ThemeData.dark({
[bool](flutter-docs://api/dart-core/bool)? useMaterial3,
})

A default dark theme.

This theme does not contain text geometry. Instead, it is expected that
this theme is localized using text geometry using [ThemeData.localize](flutter-docs://api/material/ThemeData/localize).

## Implementation

```dart
factory ThemeData.dark({bool? useMaterial3}) =>
    ThemeData(brightness: Brightness.dark, useMaterial3: useMaterial3);
```