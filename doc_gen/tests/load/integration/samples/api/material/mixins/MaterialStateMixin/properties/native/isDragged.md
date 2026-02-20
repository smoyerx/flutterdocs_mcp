# isDragged property

[bool](flutter-docs://api/dart-core/bool) get isDragged

Getter for whether this class considers [WidgetState.dragged](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isDragged => materialStates.contains(WidgetState.dragged);
```