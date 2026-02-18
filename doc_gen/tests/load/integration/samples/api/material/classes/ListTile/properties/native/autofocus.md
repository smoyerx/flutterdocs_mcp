# autofocus property

[bool](mcp://flutter/api/dart-core/bool) autofocus


True if this widget will be selected as the initial focus when no other
node in its scope is currently focused.

Ideally, there is only one widget with autofocus set in each [FocusScope](mcp://flutter/api/widgets/FocusScope).
If there is more than one widget with autofocus set, then the first one
added to the tree will get focus.

Defaults to false.

## Implementation

```dart
final bool autofocus;
```