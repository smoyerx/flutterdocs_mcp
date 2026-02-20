# isSelected property

[bool](flutter-docs://api/dart-core/bool) get isSelected

Getter for whether this class considers [WidgetState.selected](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isSelected => materialStates.contains(WidgetState.selected);
```