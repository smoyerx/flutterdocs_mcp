# reassemble method

1. @[protected](flutter-docs://api/meta/protected)
2. @[mustCallSuper](flutter-docs://api/meta/mustCallSuper)

voidreassemble()

Called whenever the application is reassembled during debugging, for
example during hot reload.

This method should rerun any initialization logic that depends on global
state, for example, image loading from asset bundles (since the asset
bundle may have changed).

This function will only be called during development. In release builds,
the `ext.flutter.reassemble` hook is not available, and so this code will
never execute.

Implementers should not rely on any ordering for hot reload source update,
reassemble, and build methods after a hot reload has been initiated. It is
possible that a [Timer](flutter-docs://api/dart-async/Timer) (e.g. an [Animation](flutter-docs://api/animation/Animation)) or a debugging session
attached to the isolate could trigger a build with reloaded code *before* reassemble is called. Code that expects preconditions to be set by
reassemble after a hot reload must be resilient to being called out of
order, e.g. by fizzling instead of throwing. That said, once reassemble is
called, build will be called after it at least once.

In addition to this method being invoked, it is guaranteed that the[build](flutter-docs://api/widgets/State/build) method will be invoked when a reassemble is signaled. Most
widgets therefore do not need to do anything in the [reassemble](flutter-docs://api/widgets/State/reassemble) method.

See also:

- [Element.reassemble](flutter-docs://api/widgets/Element/reassemble)
- [BindingBase.reassembleApplication](flutter-docs://api/foundation/BindingBase/reassembleApplication)
- [Image](flutter-docs://api/dart-ui/Image), which uses this to reload images.


## Implementation

```dart
@protected
@mustCallSuper
void reassemble() {}
```