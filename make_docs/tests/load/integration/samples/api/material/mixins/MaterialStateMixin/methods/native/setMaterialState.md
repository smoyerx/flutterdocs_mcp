# setMaterialState method

@[protected](flutter-docs://api/meta/protected)
voidsetMaterialState(
[WidgetState](flutter-docs://api/widgets/WidgetState) state,
[bool](flutter-docs://api/dart-core/bool) isSet
)

Mutator to mark a [WidgetState](flutter-docs://api/widgets/WidgetState) value as either active or inactive.

## Implementation

```dart
@protected
void setMaterialState(WidgetState state, bool isSet) {
  return isSet ? addMaterialState(state) : removeMaterialState(state);
}
```