# addMaterialState method

@[protected](flutter-docs://api/meta/protected)
voidaddMaterialState(
[WidgetState](flutter-docs://api/widgets/WidgetState) state
)

Mutator to mark a [WidgetState](flutter-docs://api/widgets/WidgetState) value as active.

## Implementation

```dart
@protected
void addMaterialState(WidgetState state) {
  if (materialStates.add(state)) {
    setState(() {});
  }
}
```