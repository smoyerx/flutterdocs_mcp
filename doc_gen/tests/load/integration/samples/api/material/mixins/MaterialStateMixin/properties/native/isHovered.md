# isHovered property

[bool](mcp://flutter/api/dart-core/bool) get isHovered

Getter for whether this class considers [WidgetState.hovered](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isHovered => materialStates.contains(WidgetState.hovered);
```