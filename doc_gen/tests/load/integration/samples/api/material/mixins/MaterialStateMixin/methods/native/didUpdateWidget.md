# didUpdateWidget method

@[mustCallSuper](mcp://flutter/api/meta/mustCallSuper)
@[protected](mcp://flutter/api/meta/protected)
voiddidUpdateWidget(
covariant T oldWidget
)


Called whenever the widget configuration changes.

If the parent widget rebuilds and requests that this location in the tree
update to display a new widget with the same [runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) and [Widget.key](mcp://flutter/api/widgets/Widget/key), the framework will update the [widget](mcp://flutter/api/widgets/State/widget) property of this [State](mcp://flutter/api/widgets/State) object to refer to the new widget and then call this method
with the previous widget as an argument.

Override this method to respond when the [widget](mcp://flutter/api/widgets/State/widget) changes (e.g., to start
implicit animations).

The framework always calls [build](mcp://flutter/api/widgets/State/build) after calling [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget), which
means any calls to [setState](mcp://flutter/api/widgets/State/setState) in [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget) are redundant.

If a [State](mcp://flutter/api/widgets/State)'s [build](mcp://flutter/api/widgets/State/build) method depends on an object that can itself
change state, for example a [ChangeNotifier](mcp://flutter/api/foundation/ChangeNotifier) or [Stream](mcp://flutter/api/dart-async/Stream), or some
other object to which one can subscribe to receive notifications, then
be sure to subscribe and unsubscribe properly in [initState](mcp://flutter/api/material/MaterialStateMixin/initState), [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget), and [dispose](mcp://flutter/api/material/MaterialStateMixin/dispose):

- In [initState](mcp://flutter/api/material/MaterialStateMixin/initState), subscribe to the object.
- In [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget) unsubscribe from the old object and subscribe
to the new one if the updated widget configuration requires
replacing the object.
- In [dispose](mcp://flutter/api/material/MaterialStateMixin/dispose), unsubscribe from the object.


Implementations of this method should start with a call to the inherited
method, as in `super.didUpdateWidget(oldWidget)`.

*See the discussion at [Element.rebuild](mcp://flutter/api/widgets/Element/rebuild) for more information on when this
method is called.*

## Implementation

```dart
@mustCallSuper
@protected
void didUpdateWidget(covariant T oldWidget) {}
```