# statesController property

[MaterialStatesController](mcp://flutter/api/material/MaterialStatesController)? statesController


Represents the interactive "state" of this widget in terms of
a set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s, like [WidgetState.pressed](mcp://flutter/api/widgets/WidgetState) and [WidgetState.focused](mcp://flutter/api/widgets/WidgetState).

Classes based on this one can provide their own[WidgetStatesController](mcp://flutter/api/widgets/WidgetStatesController) to which they've added listeners.
They can also update the controller's [WidgetStatesController.value](mcp://flutter/api/foundation/ValueNotifier/value) however, this may only be done when it's safe to call [State.setState](mcp://flutter/api/widgets/State/setState), like in an event handler.

## Implementation

```dart
final MaterialStatesController? statesController;
```