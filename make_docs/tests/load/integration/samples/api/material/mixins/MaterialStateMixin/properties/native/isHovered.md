# isHovered property

[bool](flutter-docs://api/dart-core/bool) get isHovered

Getter for whether this class considers [WidgetState.hovered](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isHovered => materialStates.contains(WidgetState.hovered);
```