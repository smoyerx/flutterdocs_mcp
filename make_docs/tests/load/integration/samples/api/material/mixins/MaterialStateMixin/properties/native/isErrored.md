# isErrored property

[bool](flutter-docs://api/dart-core/bool) get isErrored

Getter for whether this class considers [WidgetState.error](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isErrored => materialStates.contains(WidgetState.error);
```