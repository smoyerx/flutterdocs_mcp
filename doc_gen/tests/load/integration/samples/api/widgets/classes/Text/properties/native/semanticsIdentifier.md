# semanticsIdentifier property

[String](mcp://flutter/api/dart-core/String)? semanticsIdentifier


A unique identifier for the semantics node for this widget.

This is useful for cases where the text widget needs to have a uniquely
identifiable ID that is recognized through the automation tools without
having a dependency on the actual content of the text that can possibly be
dynamic in nature.

## Implementation

```dart
final String? semanticsIdentifier;
```