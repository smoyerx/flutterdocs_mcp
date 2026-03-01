# materialStates property

1. @[protected](flutter-docs://api/meta/protected)

[Set](flutter-docs://api/dart-core/Set)<[WidgetState](flutter-docs://api/widgets/WidgetState)> materialStates


Managed set of active [WidgetState](flutter-docs://api/widgets/WidgetState) values; designed to be passed to [WidgetStateProperty.resolve](flutter-docs://api/widgets/WidgetStateProperty/resolve) methods.

To mutate and have [setState](flutter-docs://api/widgets/State/setState) called automatically for you, use [setMaterialState](flutter-docs://api/material/MaterialStateMixin/setMaterialState), [addMaterialState](flutter-docs://api/material/MaterialStateMixin/addMaterialState), or [removeMaterialState](flutter-docs://api/material/MaterialStateMixin/removeMaterialState). Directly
mutating the set is possible, and may be necessary if you need to alter its
list without calling [setState](flutter-docs://api/widgets/State/setState) (and thus triggering a re-render).

To check for a single condition, convenience getters [isPressed](flutter-docs://api/material/MaterialStateMixin/isPressed), [isHovered](flutter-docs://api/material/MaterialStateMixin/isHovered), [isFocused](flutter-docs://api/material/MaterialStateMixin/isFocused), etc, are available for each [WidgetState](flutter-docs://api/widgets/WidgetState) value.

## Implementation

```dart
@protected
Set<WidgetState> materialStates = <WidgetState>{};
```