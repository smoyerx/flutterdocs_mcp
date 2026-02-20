# operator ~ method

[WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) operator ~()

Takes a [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint) and applies the logical "not".

## Implementation

```dart
WidgetStatesConstraint operator ~() => _WidgetStateNot(this);
```