# isFocused property

[bool](flutter-docs://api/dart-core/bool) get isFocused

Getter for whether this class considers [WidgetState.focused](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isFocused => materialStates.contains(WidgetState.focused);
```