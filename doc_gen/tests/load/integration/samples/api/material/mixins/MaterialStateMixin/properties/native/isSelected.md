# isSelected property

[bool](mcp://flutter/api/dart-core/bool) get isSelected

Getter for whether this class considers [WidgetState.selected](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isSelected => materialStates.contains(WidgetState.selected);
```