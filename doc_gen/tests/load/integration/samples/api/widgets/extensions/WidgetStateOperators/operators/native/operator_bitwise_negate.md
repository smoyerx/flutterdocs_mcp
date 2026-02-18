# operator ~ method

[WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) operator ~()

Takes a [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint) and applies the logical "not".

## Implementation

```dart
WidgetStatesConstraint operator ~() => _WidgetStateNot(this);
```