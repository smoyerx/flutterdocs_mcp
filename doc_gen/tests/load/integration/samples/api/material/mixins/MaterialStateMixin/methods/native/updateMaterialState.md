# updateMaterialState method

@[protected](mcp://flutter/api/meta/protected)
[ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>updateMaterialState(
[WidgetState](mcp://flutter/api/widgets/WidgetState) key, {
[ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>? onChanged,
})

Callback factory which accepts a [WidgetState](mcp://flutter/api/widgets/WidgetState) value and returns a
closure to mutate [materialStates](mcp://flutter/api/material/MaterialStateMixin/materialStates) and call [setState](mcp://flutter/api/widgets/State/setState).

Accepts an optional second named parameter, `onChanged`, which allows
arbitrary functionality to be wired through the [MaterialStateMixin](mcp://flutter/api/material/MaterialStateMixin).
If supplied, the `onChanged` function is only called when child widgets
report events that make changes to the current set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s.

This example shows how to use the [updateMaterialState](mcp://flutter/api/material/MaterialStateMixin/updateMaterialState) callback factory
in other widgets, including the optional `onChanged` callback.



```dart
class MyWidget extends StatefulWidget {
  const MyWidget({super.key, this.onPressed});

  /// Something important this widget must do when pressed.
  final VoidCallback? onPressed;

  @override
  State<MyWidget> createState() => MyWidgetState();
}

class MyWidgetState extends State<MyWidget> with MaterialStateMixin<MyWidget> {
  @override
  Widget build(BuildContext context) {
    return ColoredBox(
      color: isPressed ? Colors.black : Colors.white,
      child: InkWell(
        onHighlightChanged: updateMaterialState(
          WidgetState.pressed,
          onChanged: (bool val) {
            if (val) {
              widget.onPressed?.call();
            }
          },
        ),
      ),
    );
  }
}
```

## Implementation

```dart
@protected
ValueChanged<bool> updateMaterialState(WidgetState key, {ValueChanged<bool>? onChanged}) {
  return (bool value) {
    if (materialStates.contains(key) == value) {
      return;
    }
    setMaterialState(key, value);
    onChanged?.call(value);
  };
}
```