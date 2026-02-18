# WidgetStateOperators extension

These operators can be used inside a [WidgetStateMap](mcp://flutter/api/widgets/WidgetStateMap) to combine states
and find a match.

Example:

```dart
final WidgetStatesConstraint constraint = WidgetState.focused | WidgetState.hovered;

```
In the above case, `constraint.isSatisfiedBy(states)` is equivalent to:

```dart
states.contains(WidgetState.focused) || states.contains(WidgetState.hovered);

```
Since enums can't extend other classes, [WidgetState](mcp://flutter/api/widgets/WidgetState) instead `implements` the [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) interface. This `extension` ensures that
the operators can be used without being directly inherited.

on
- [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint)

## Operators

[operator &](mcp://flutter/api/widgets/WidgetStateOperators/operator_bitwise_and)([WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) other) → [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint)
Available on [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint),
 provided by the [WidgetStateOperators](mcp://flutter/api/widgets/WidgetStateOperators) extension

Combines two [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) values using logical "and".

[operator |](mcp://flutter/api/widgets/WidgetStateOperators/operator_bitwise_or)([WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) other) → [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint)
Available on [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint),
 provided by the [WidgetStateOperators](mcp://flutter/api/widgets/WidgetStateOperators) extension

Combines two [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) values using logical "or".

[operator ~](mcp://flutter/api/widgets/WidgetStateOperators/operator_bitwise_negate)() → [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint)
Available on [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint),
 provided by the [WidgetStateOperators](mcp://flutter/api/widgets/WidgetStateOperators) extension

Takes a [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) and applies the logical "not".