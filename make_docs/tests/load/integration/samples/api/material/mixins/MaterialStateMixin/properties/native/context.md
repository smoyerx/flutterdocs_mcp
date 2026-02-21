# context property

[BuildContext](flutter-docs://api/widgets/BuildContext) get context


The location in the tree where this widget builds.

The framework associates [State](flutter-docs://api/widgets/State) objects with a [BuildContext](flutter-docs://api/widgets/BuildContext) after
creating them with [StatefulWidget.createState](flutter-docs://api/widgets/StatefulWidget/createState) and before calling [initState](flutter-docs://api/widgets/State/initState). The association is permanent: the [State](flutter-docs://api/widgets/State) object will never
change its [BuildContext](flutter-docs://api/widgets/BuildContext). However, the [BuildContext](flutter-docs://api/widgets/BuildContext) itself can be moved
around the tree.

After calling [dispose](flutter-docs://api/widgets/State/dispose), the framework severs the [State](flutter-docs://api/widgets/State) object's
connection with the [BuildContext](flutter-docs://api/widgets/BuildContext).

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