# extensions property

[Map](flutter-docs://api/dart-core/Map)<[Object](flutter-docs://api/dart-core/Object), [ThemeExtension](flutter-docs://api/material/ThemeExtension)> extensions


Arbitrary additions to this theme.

To define extensions, pass an [Iterable](flutter-docs://api/dart-core/Iterable) containing one or more [ThemeExtension](flutter-docs://api/material/ThemeExtension) subclasses to [ThemeData.new](flutter-docs://api/material/ThemeData/ThemeData) or [copyWith](flutter-docs://api/material/ThemeData/copyWith).

To obtain an extension, use [extension](flutter-docs://api/material/ThemeData/extension).

This sample shows how to create and use a subclass of [ThemeExtension](flutter-docs://api/material/ThemeExtension) that
defines two colors.


To create a local project with this code sample, run:  flutter create --sample=material.ThemeData.extensions.1 mysample

[Omitted code: Interactive sample]

See also:

- [extension](flutter-docs://api/material/ThemeData/extension), a convenience function for obtaining a specific extension.


## Implementation

```dart
final Map<Object, ThemeExtension<dynamic>> extensions;
```