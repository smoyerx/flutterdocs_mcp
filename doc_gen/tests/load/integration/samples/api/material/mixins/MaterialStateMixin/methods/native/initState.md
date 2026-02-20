# initState method

1. @[protected](flutter-docs://api/meta/protected)
2. @[mustCallSuper](flutter-docs://api/meta/mustCallSuper)

voidinitState()


Called when this object is inserted into the tree.

The framework will call this method exactly once for each [State](flutter-docs://api/widgets/State) object
it creates.

Override this method to perform initialization that depends on the
location at which this object was inserted into the tree (i.e., [context](flutter-docs://api/widgets/State/context))
or on the widget used to configure this object (i.e., [widget](flutter-docs://api/widgets/State/widget)).

If a [State](flutter-docs://api/widgets/State)'s [build](flutter-docs://api/widgets/State/build) method depends on an object that can itself
change state, for example a [ChangeNotifier](flutter-docs://api/foundation/ChangeNotifier) or [Stream](flutter-docs://api/dart-async/Stream), or some
other object to which one can subscribe to receive notifications, then
be sure to subscribe and unsubscribe properly in [initState](flutter-docs://api/widgets/State/initState), [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget), and [dispose](flutter-docs://api/widgets/State/dispose):

- In [initState](flutter-docs://api/widgets/State/initState), subscribe to the object.
- In [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget) unsubscribe from the old object and subscribe
to the new one if the updated widget configuration requires
replacing the object.
- In [dispose](flutter-docs://api/widgets/State/dispose), unsubscribe from the object.


You should not use [BuildContext.dependOnInheritedWidgetOfExactType](flutter-docs://api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) from this
method. However, [didChangeDependencies](flutter-docs://api/widgets/State/didChangeDependencies) will be called immediately
following this method, and [BuildContext.dependOnInheritedWidgetOfExactType](flutter-docs://api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) can
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