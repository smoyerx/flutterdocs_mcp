# isDisabled property

[bool](mcp://flutter/api/dart-core/bool) get isDisabled

Getter for whether this class considers [WidgetState.disabled](mcp://flutter/api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isDisabled => materialStates.contains(WidgetState.disabled);
```