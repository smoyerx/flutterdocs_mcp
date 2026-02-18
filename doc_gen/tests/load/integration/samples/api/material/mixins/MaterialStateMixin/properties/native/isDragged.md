# isDragged property

[bool](mcp://flutter/api/dart-core/bool) get isDragged

Getter for whether this class considers [WidgetState.dragged](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isDragged => materialStates.contains(WidgetState.dragged);
```