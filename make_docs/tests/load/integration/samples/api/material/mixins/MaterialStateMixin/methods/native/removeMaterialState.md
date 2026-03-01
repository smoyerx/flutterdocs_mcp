# removeMaterialState method

@[protected](flutter-docs://api/meta/protected)
void removeMaterialState(
[WidgetState](flutter-docs://api/widgets/WidgetState) state
)

Mutator to mark a [WidgetState](flutter-docs://api/widgets/WidgetState) value as inactive.

## Implementation

```dart
@protected
void removeMaterialState(WidgetState state) {
  if (materialStates.remove(state)) {
    setState(() {});
  }
}
```