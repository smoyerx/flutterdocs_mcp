# extension<T> method

T? extension<T>()

Used to obtain a particular [ThemeExtension](flutter-docs://api/material/ThemeExtension) from [extensions](flutter-docs://api/material/ThemeData/extensions).

Obtain with `Theme.of(context).extension<MyThemeExtension>()`.

See [extensions](flutter-docs://api/material/ThemeData/extensions) for an interactive example.

## Implementation

```dart
T? extension<T>() => extensions[T] as T?;
```