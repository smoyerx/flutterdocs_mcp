# context property

[BuildContext](mcp://flutter/api/widgets/BuildContext) get context


The location in the tree where this widget builds.

The framework associates [State](mcp://flutter/api/widgets/State) objects with a [BuildContext](mcp://flutter/api/widgets/BuildContext) after
creating them with [StatefulWidget.createState](mcp://flutter/api/widgets/StatefulWidget/createState) and before calling [initState](mcp://flutter/api/widgets/State/initState). The association is permanent: the [State](mcp://flutter/api/widgets/State) object will never
change its [BuildContext](mcp://flutter/api/widgets/BuildContext). However, the [BuildContext](mcp://flutter/api/widgets/BuildContext) itself can be moved
around the tree.

After calling [dispose](mcp://flutter/api/widgets/State/dispose), the framework severs the [State](mcp://flutter/api/widgets/State) object's
connection with the [BuildContext](mcp://flutter/api/widgets/BuildContext).

## Implementation

```dart
BuildContext get context {
  assert(() {
    if (_element == null) {
      throw FlutterError(
        'This widget has been unmounted, so the State no longer has a context (and should be considered defunct). \n'
        'Consider canceling any active work during "dispose" or using the "mounted" getter to determine if the State is still active.',
      );
    }
    return true;
  }());
  return _element!;
}
```