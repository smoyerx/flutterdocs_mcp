# isErrored property

[bool](mcp://flutter/api/dart-core/bool) get isErrored

Getter for whether this class considers [WidgetState.error](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isErrored => materialStates.contains(WidgetState.error);
```