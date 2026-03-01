# statesController property

[MaterialStatesController](flutter-docs://api/material/MaterialStatesController)? statesController


Represents the interactive "state" of this widget in terms of
a set of [WidgetState](flutter-docs://api/widgets/WidgetState) s, like [WidgetState.pressed](flutter-docs://api/widgets/WidgetState) and [WidgetState.focused](flutter-docs://api/widgets/WidgetState).

Classes based on this one can provide their own [WidgetStatesController](flutter-docs://api/widgets/WidgetStatesController) to which they've added listeners.
They can also update the controller's [WidgetStatesController.value](flutter-docs://api/foundation/ValueNotifier/value) however, this may only be done when it's safe to call [State.setState](flutter-docs://api/widgets/State/setState), like in an event handler.

## Implementation

```dart
final MaterialStatesController? statesController;
```