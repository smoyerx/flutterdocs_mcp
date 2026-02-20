# updateMaterialState method

@[protected](flutter-docs://api/meta/protected)
[ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>updateMaterialState(
[WidgetState](flutter-docs://api/widgets/WidgetState) key, {
[ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>? onChanged,
})

Callback factory which accepts a [WidgetState](flutter-docs://api/widgets/WidgetState) value and returns a
closure to mutate [materialStates](flutter-docs://api/material/MaterialStateMixin/materialStates) and call [setState](flutter-docs://api/widgets/State/setState).

Accepts an optional second named parameter, `onChanged`, which allows
arbitrary functionality to be wired through the [MaterialStateMixin](flutter-docs://api/material/MaterialStateMixin).
If supplied, the `onChanged` function is only called when child widgets
report events that make changes to the current set of [WidgetState](flutter-docs://api/widgets/WidgetState) s.

This example shows how to use the [updateMaterialState](flutter-docs://api/material/MaterialStateMixin/updateMaterialState) callback factory
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