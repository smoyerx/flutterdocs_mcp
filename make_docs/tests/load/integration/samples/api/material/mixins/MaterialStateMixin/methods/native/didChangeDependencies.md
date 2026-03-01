# didChangeDependencies method

1. @[protected](flutter-docs://api/meta/protected)
2. @[mustCallSuper](flutter-docs://api/meta/mustCallSuper)

void didChangeDependencies()


Called when a dependency of this [State](flutter-docs://api/widgets/State) object changes.

For example, if the previous call to [build](flutter-docs://api/widgets/State/build) referenced an [InheritedWidget](flutter-docs://api/widgets/InheritedWidget) that later changed, the framework would call this
method to notify this object about the change.

This method is also called immediately after [initState](flutter-docs://api/widgets/State/initState). It is safe to
call [BuildContext.dependOnInheritedWidgetOfExactType](flutter-docs://api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) from this method.

Subclasses rarely override this method because the framework always
calls [build](flutter-docs://api/widgets/State/build) after a dependency changes. Some subclasses do override
this method because they need to do some expensive work (e.g., network
fetches) when their dependencies change, and that work would be too
expensive to do for every build.

## Implementation

```dart
@protected
@mustCallSuper
void didChangeDependencies() {}
```