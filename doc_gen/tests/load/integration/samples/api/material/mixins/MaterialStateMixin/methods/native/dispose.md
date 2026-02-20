# dispose method

1. @[protected](flutter-docs://api/meta/protected)
2. @[mustCallSuper](flutter-docs://api/meta/mustCallSuper)

voiddispose()


Called when this object is removed from the tree permanently.

The framework calls this method when this [State](flutter-docs://api/widgets/State) object will never
build again. After the framework calls [dispose](flutter-docs://api/widgets/State/dispose), the [State](flutter-docs://api/widgets/State) object is
considered unmounted and the [mounted](flutter-docs://api/widgets/State/mounted) property is false. It is an error
to call [setState](flutter-docs://api/widgets/State/setState) at this point. This stage of the lifecycle is terminal:
there is no way to remount a [State](flutter-docs://api/widgets/State) object that has been disposed.

Subclasses should override this method to release any resources retained
by this object (e.g., stop any active animations).

If a [State](flutter-docs://api/widgets/State)'s [build](flutter-docs://api/material/MaterialStateMixin/build) method depends on an object that can itself
change state, for example a [ChangeNotifier](flutter-docs://api/foundation/ChangeNotifier) or [Stream](flutter-docs://api/dart-async/Stream), or some
other object to which one can subscribe to receive notifications, then
be sure to subscribe and unsubscribe properly in [initState](flutter-docs://api/material/MaterialStateMixin/initState), [didUpdateWidget](flutter-docs://api/material/MaterialStateMixin/didUpdateWidget), and [dispose](flutter-docs://api/widgets/State/dispose):

- In [initState](flutter-docs://api/material/MaterialStateMixin/initState), subscribe to the object.
- In [didUpdateWidget](flutter-docs://api/material/MaterialStateMixin/didUpdateWidget) unsubscribe from the old object and subscribe
to the new one if the updated widget configuration requires
replacing the object.
- In [dispose](flutter-docs://api/widgets/State/dispose), unsubscribe from the object.


Implementations of this method should end with a call to the inherited
method, as in `super.dispose()`.

## Caveats

This method is *not* invoked at times where a developer might otherwise
expect it, such as application shutdown or dismissal via platform
native methods.

### Application shutdown

There is no way to predict when application shutdown will happen. For
example, a user's battery could catch fire, or the user could drop the
device into a swimming pool, or the operating system could unilaterally
terminate the application process due to memory pressure.

Applications are responsible for ensuring that they are well-behaved
even in the face of a rapid unscheduled termination.

To artificially cause the entire widget tree to be disposed, consider
calling [runApp](flutter-docs://api/widgets/runApp) with a widget such as [SizedBox.shrink](flutter-docs://api/widgets/SizedBox/SizedBox.shrink).

To listen for platform shutdown messages (and other lifecycle changes),
consider the [AppLifecycleListener](flutter-docs://api/widgets/AppLifecycleListener) API.

## Dismissing Flutter UI via platform native methods

An application may have both Flutter and non-Flutter UI in it. If the
application calls non-Flutter methods to remove Flutter based UI such as
platform native API to manipulate the platform native navigation stack,
the framework does not know if the developer intends to eagerly free
resources or not. The widget tree remains mounted and ready to render
as soon as it is displayed again.

See the method used to bootstrap the app (e.g. [runApp](flutter-docs://api/widgets/runApp) or [runWidget](flutter-docs://api/widgets/runWidget))
for suggestions on how to release resources more eagerly.

See also:

- [deactivate](flutter-docs://api/widgets/State/deactivate), which is called prior to [dispose](flutter-docs://api/widgets/State/dispose).


## Implementation

```dart
@protected
@mustCallSuper
void dispose() {
  assert(_debugLifecycleState == _StateLifecycle.ready);
  assert(() {
    _debugLifecycleState = _StateLifecycle.defunct;
    return true;
  }());
  assert(debugMaybeDispatchDisposed(this));
}
```