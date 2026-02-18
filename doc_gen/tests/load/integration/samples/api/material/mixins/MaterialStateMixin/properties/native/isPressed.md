# isPressed property

[bool](mcp://flutter/api/dart-core/bool) get isPressed

Getter for whether this class considers [WidgetState.pressed](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isPressed => materialStates.contains(WidgetState.pressed);
```