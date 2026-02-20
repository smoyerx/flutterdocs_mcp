# operator & method

[WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) operator &(
[WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) other
)

Combines two [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) values using logical "and".

## Implementation

```dart
WidgetStatesConstraint operator &(WidgetStatesConstraint other) => _WidgetStateAnd(this, other);
```