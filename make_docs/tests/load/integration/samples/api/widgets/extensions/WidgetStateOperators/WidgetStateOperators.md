# WidgetStateOperators extension

These operators can be used inside a [WidgetStateMap](flutter-docs://api/widgets/WidgetStateMap) to combine states
and find a match.

Example:

```dart
final WidgetStatesConstraint constraint = WidgetState.focused | WidgetState.hovered;

```
In the above case, `constraint.isSatisfiedBy(states)` is equivalent to:

```dart
states.contains(WidgetState.focused) || states.contains(WidgetState.hovered);

```
Since enums can't extend other classes, [WidgetState](flutter-docs://api/widgets/WidgetState) instead `implements` the [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) interface. This `extension` ensures that
the operators can be used without being directly inherited.

on
- [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint)

## Operators

[operator &](flutter-docs://api/widgets/WidgetStateOperators/operator_bitwise_and)([WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) other) → [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint)
Available on [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint),
 provided by the [WidgetStateOperators](flutter-docs://api/widgets/WidgetStateOperators) extension

Combines two [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) values using logical "and".

[operator |](flutter-docs://api/widgets/WidgetStateOperators/operator_bitwise_or)([WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) other) → [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint)
Available on [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint),
 provided by the [WidgetStateOperators](flutter-docs://api/widgets/WidgetStateOperators) extension

Combines two [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) values using logical "or".

[operator ~](flutter-docs://api/widgets/WidgetStateOperators/operator_bitwise_negate)() → [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint)
Available on [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint),
 provided by the [WidgetStateOperators](flutter-docs://api/widgets/WidgetStateOperators) extension

Takes a [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) and applies the logical "not".