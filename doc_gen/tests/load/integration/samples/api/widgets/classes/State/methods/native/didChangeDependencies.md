# didChangeDependencies method

1. @[protected](mcp://flutter/api/meta/protected)
2. @[mustCallSuper](mcp://flutter/api/meta/mustCallSuper)

voiddidChangeDependencies()

Called when a dependency of this [State](mcp://flutter/api/widgets/State) object changes.

For example, if the previous call to [build](mcp://flutter/api/widgets/State/build) referenced an [InheritedWidget](mcp://flutter/api/widgets/InheritedWidget) that later changed, the framework would call this
method to notify this object about the change.

This method is also called immediately after [initState](mcp://flutter/api/widgets/State/initState). It is safe to
call [BuildContext.dependOnInheritedWidgetOfExactType](mcp://flutter/api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) from this method.

Subclasses rarely override this method because the framework always
calls [build](mcp://flutter/api/widgets/State/build) after a dependency changes. Some subclasses do override
this method because they need to do some expensive work (e.g., network
fetches) when their dependencies change, and that work would be too
expensive to do for every build.

## Implementation

```dart
@protected
@mustCallSuper
void didChangeDependencies() {}
```