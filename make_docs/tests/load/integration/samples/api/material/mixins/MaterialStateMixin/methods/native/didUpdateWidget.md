# didUpdateWidget method

@[mustCallSuper](flutter-docs://api/meta/mustCallSuper)
@[protected](flutter-docs://api/meta/protected)
void didUpdateWidget(
covariant T oldWidget
)


Called whenever the widget configuration changes.

If the parent widget rebuilds and requests that this location in the tree
update to display a new widget with the same [runtimeType](flutter-docs://api/dart-core/Object/runtimeType) and [Widget.key](flutter-docs://api/widgets/Widget/key), the framework will update the [widget](flutter-docs://api/widgets/State/widget) property of this [State](flutter-docs://api/widgets/State) object to refer to the new widget and then call this method
with the previous widget as an argument.

Override this method to respond when the [widget](flutter-docs://api/widgets/State/widget) changes (e.g., to start
implicit animations).

The framework always calls [build](flutter-docs://api/widgets/State/build) after calling [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget), which
means any calls to [setState](flutter-docs://api/widgets/State/setState) in [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget) are redundant.

If a [State](flutter-docs://api/widgets/State)'s [build](flutter-docs://api/widgets/State/build) method depends on an object that can itself
change state, for example a [ChangeNotifier](flutter-docs://api/foundation/ChangeNotifier) or [Stream](flutter-docs://api/dart-async/Stream), or some
other object to which one can subscribe to receive notifications, then
be sure to subscribe and unsubscribe properly in [initState](flutter-docs://api/material/MaterialStateMixin/initState), [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget), and [dispose](flutter-docs://api/material/MaterialStateMixin/dispose):

- In [initState](flutter-docs://api/material/MaterialStateMixin/initState), subscribe to the object.
- In [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget) unsubscribe from the old object and subscribe
to the new one if the updated widget configuration requires
replacing the object.
- In [dispose](flutter-docs://api/material/MaterialStateMixin/dispose), unsubscribe from the object.


Implementations of this method should start with a call to the inherited
method, as in `super.didUpdateWidget(oldWidget)`.

*See the discussion at [Element.rebuild](flutter-docs://api/widgets/Element/rebuild) for more information on when this
method is called.*

## Implementation

```dart
@mustCallSuper
@protected
void didUpdateWidget(covariant T oldWidget) {}
```