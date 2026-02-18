# operator & method

[WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) operator &(
[WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) other
)

Combines two [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) values using logical "and".

## Implementation

```dart
WidgetStatesConstraint operator &(WidgetStatesConstraint other) => _WidgetStateAnd(this, other);
```