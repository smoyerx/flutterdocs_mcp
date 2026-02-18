# dispose method

1. @[protected](mcp://flutter/api/meta/protected)
2. @[mustCallSuper](mcp://flutter/api/meta/mustCallSuper)

voiddispose()


Called when this object is removed from the tree permanently.

The framework calls this method when this [State](mcp://flutter/api/widgets/State) object will never
build again. After the framework calls [dispose](mcp://flutter/api/widgets/State/dispose), the [State](mcp://flutter/api/widgets/State) object is
considered unmounted and the [mounted](mcp://flutter/api/widgets/State/mounted) property is false. It is an error
to call [setState](mcp://flutter/api/widgets/State/setState) at this point. This stage of the lifecycle is terminal:
there is no way to remount a [State](mcp://flutter/api/widgets/State) object that has been disposed.

Subclasses should override this method to release any resources retained
by this object (e.g., stop any active animations).

If a [State](mcp://flutter/api/widgets/State)'s [build](mcp://flutter/api/material/MaterialStateMixin/build) method depends on an object that can itself
change state, for example a [ChangeNotifier](mcp://flutter/api/foundation/ChangeNotifier) or [Stream](mcp://flutter/api/dart-async/Stream), or some
other object to which one can subscribe to receive notifications, then
be sure to subscribe and unsubscribe properly in [initState](mcp://flutter/api/material/MaterialStateMixin/initState), [didUpdateWidget](mcp://flutter/api/material/MaterialStateMixin/didUpdateWidget), and [dispose](mcp://flutter/api/widgets/State/dispose):

- In [initState](mcp://flutter/api/material/MaterialStateMixin/initState), subscribe to the object.
- In [didUpdateWidget](mcp://flutter/api/material/MaterialStateMixin/didUpdateWidget) unsubscribe from the old object and subscribe
to the new one if the updated widget configuration requires
replacing the object.
- In [dispose](mcp://flutter/api/widgets/State/dispose), unsubscribe from the object.


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
calling [runApp](mcp://flutter/api/widgets/runApp) with a widget such as [SizedBox.shrink](mcp://flutter/api/widgets/SizedBox/SizedBox.shrink).

To listen for platform shutdown messages (and other lifecycle changes),
consider the [AppLifecycleListener](mcp://flutter/api/widgets/AppLifecycleListener) API.

## Dismissing Flutter UI via platform native methods

An application may have both Flutter and non-Flutter UI in it. If the
application calls non-Flutter methods to remove Flutter based UI such as
platform native API to manipulate the platform native navigation stack,
the framework does not know if the developer intends to eagerly free
resources or not. The widget tree remains mounted and ready to render
as soon as it is displayed again.

See the method used to bootstrap the app (e.g. [runApp](mcp://flutter/api/widgets/runApp) or [runWidget](mcp://flutter/api/widgets/runWidget))
for suggestions on how to release resources more eagerly.

See also:

- [deactivate](mcp://flutter/api/widgets/State/deactivate), which is called prior to [dispose](mcp://flutter/api/widgets/State/dispose).


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