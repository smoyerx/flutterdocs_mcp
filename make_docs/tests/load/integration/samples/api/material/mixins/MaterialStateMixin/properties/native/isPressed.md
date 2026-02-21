# isPressed property

[bool](flutter-docs://api/dart-core/bool) get isPressed

Getter for whether this class considers [WidgetState.pressed](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isPressed => materialStates.contains(WidgetState.pressed);
```