# addMaterialState method

@[protected](mcp://flutter/api/meta/protected)
voidaddMaterialState(
[WidgetState](mcp://flutter/api/widgets/WidgetState) state
)

Mutator to mark a [WidgetState](mcp://flutter/api/widgets/WidgetState) value as active.

## Implementation

```dart
@protected
void addMaterialState(WidgetState state) {
  if (materialStates.add(state)) {
    setState(() {});
  }
}
```