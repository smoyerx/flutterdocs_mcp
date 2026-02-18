# initState method

1. @[protected](mcp://flutter/api/meta/protected)
2. @[mustCallSuper](mcp://flutter/api/meta/mustCallSuper)

voidinitState()


Called when this object is inserted into the tree.

The framework will call this method exactly once for each [State](mcp://flutter/api/widgets/State) object
it creates.

Override this method to perform initialization that depends on the
location at which this object was inserted into the tree (i.e., [context](mcp://flutter/api/widgets/State/context))
or on the widget used to configure this object (i.e., [widget](mcp://flutter/api/widgets/State/widget)).

If a [State](mcp://flutter/api/widgets/State)'s [build](mcp://flutter/api/widgets/State/build) method depends on an object that can itself
change state, for example a [ChangeNotifier](mcp://flutter/api/foundation/ChangeNotifier) or [Stream](mcp://flutter/api/dart-async/Stream), or some
other object to which one can subscribe to receive notifications, then
be sure to subscribe and unsubscribe properly in [initState](mcp://flutter/api/widgets/State/initState), [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget), and [dispose](mcp://flutter/api/widgets/State/dispose):

- In [initState](mcp://flutter/api/widgets/State/initState), subscribe to the object.
- In [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget) unsubscribe from the old object and subscribe
to the new one if the updated widget configuration requires
replacing the object.
- In [dispose](mcp://flutter/api/widgets/State/dispose), unsubscribe from the object.


You should not use [BuildContext.dependOnInheritedWidgetOfExactType](mcp://flutter/api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) from this
method. However, [didChangeDependencies](mcp://flutter/api/widgets/State/didChangeDependencies) will be called immediately
following this method, and [BuildContext.dependOnInheritedWidgetOfExactType](mcp://flutter/api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) can
be used there.

Implementations of this method should start with a call to the inherited
method, as in `super.initState()`.

## Implementation

```dart
@protected
@mustCallSuper
void initState() {
  assert(_debugLifecycleState == _StateLifecycle.created);
  assert(debugMaybeDispatchCreated('widgets', 'State', this));
}
```