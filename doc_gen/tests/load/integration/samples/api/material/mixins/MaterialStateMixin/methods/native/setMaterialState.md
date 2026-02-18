# setMaterialState method

@[protected](mcp://flutter/api/meta/protected)
voidsetMaterialState(
[WidgetState](mcp://flutter/api/widgets/WidgetState) state,
[bool](mcp://flutter/api/dart-core/bool) isSet
)

Mutator to mark a [WidgetState](mcp://flutter/api/widgets/WidgetState) value as either active or inactive.

## Implementation

```dart
@protected
void setMaterialState(WidgetState state, bool isSet) {
  return isSet ? addMaterialState(state) : removeMaterialState(state);
}
```