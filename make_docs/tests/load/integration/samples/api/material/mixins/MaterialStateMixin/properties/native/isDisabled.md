# isDisabled property

[bool](flutter-docs://api/dart-core/bool) get isDisabled

Getter for whether this class considers [WidgetState.disabled](flutter-docs://api/widgets/WidgetState) to be active.

## Implementation

```dart
bool get isDisabled => materialStates.contains(WidgetState.disabled);
```