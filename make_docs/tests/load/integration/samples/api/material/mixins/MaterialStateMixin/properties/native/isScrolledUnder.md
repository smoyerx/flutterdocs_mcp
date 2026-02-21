# isScrolledUnder property

[bool](flutter-docs://api/dart-core/bool) get isScrolledUnder

Getter for whether this class considers [WidgetState.scrolledUnder](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isScrolledUnder => materialStates.contains(WidgetState.scrolledUnder);
```