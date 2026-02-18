# extensions property

[Map](mcp://flutter/api/dart-core/Map)<[Object](mcp://flutter/api/dart-core/Object), [ThemeExtension](mcp://flutter/api/material/ThemeExtension)>extensions


Arbitrary additions to this theme.

To define extensions, pass an [Iterable](mcp://flutter/api/dart-core/Iterable) containing one or more [ThemeExtension](mcp://flutter/api/material/ThemeExtension) subclasses to [ThemeData.new](mcp://flutter/api/material/ThemeData/ThemeData) or [copyWith](mcp://flutter/api/material/ThemeData/copyWith).

To obtain an extension, use [extension](mcp://flutter/api/material/ThemeData/extension).

This sample shows how to create and use a subclass of [ThemeExtension](mcp://flutter/api/material/ThemeExtension) that
defines two colors.


To create a local project with this code sample, run:  flutter create --sample=material.ThemeData.extensions.1 mysample

[Omitted code: Interactive sample]

See also:

- [extension](mcp://flutter/api/material/ThemeData/extension), a convenience function for obtaining a specific extension.


## Implementation

```dart
final Map<Object, ThemeExtension<dynamic>> extensions;
```