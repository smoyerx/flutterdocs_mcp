# removeMaterialState method

@[protected](mcp://flutter/api/meta/protected)
voidremoveMaterialState(
[WidgetState](mcp://flutter/api/widgets/WidgetState) state
)

Mutator to mark a [WidgetState](mcp://flutter/api/widgets/WidgetState) value as inactive.

## Implementation

```dart
@protected
void removeMaterialState(WidgetState state) {
  if (materialStates.remove(state)) {
    setState(() {});
  }
}
```