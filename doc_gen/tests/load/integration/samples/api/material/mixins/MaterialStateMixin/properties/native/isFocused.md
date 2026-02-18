# isFocused property

[bool](mcp://flutter/api/dart-core/bool) get isFocused

Getter for whether this class considers [WidgetState.focused](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isFocused => materialStates.contains(WidgetState.focused);
```