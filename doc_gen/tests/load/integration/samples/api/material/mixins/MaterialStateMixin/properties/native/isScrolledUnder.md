# isScrolledUnder property

[bool](mcp://flutter/api/dart-core/bool) get isScrolledUnder

Getter for whether this class considers [WidgetState.scrolledUnder](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isScrolledUnder => materialStates.contains(WidgetState.scrolledUnder);
```