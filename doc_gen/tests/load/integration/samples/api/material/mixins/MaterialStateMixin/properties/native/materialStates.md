# materialStates property

1. @[protected](mcp://flutter/api/meta/protected)

[Set](mcp://flutter/api/dart-core/Set)<[WidgetState](mcp://flutter/api/widgets/WidgetState)>materialStates


Managed set of active [WidgetState](mcp://flutter/api/widgets/WidgetState) values; designed to be passed to [WidgetStateProperty.resolve](mcp://flutter/api/widgets/WidgetStateProperty/resolve) methods.

To mutate and have [setState](mcp://flutter/api/widgets/State/setState) called automatically for you, use [setMaterialState](mcp://flutter/api/material/MaterialStateMixin/setMaterialState), [addMaterialState](mcp://flutter/api/material/MaterialStateMixin/addMaterialState), or [removeMaterialState](mcp://flutter/api/material/MaterialStateMixin/removeMaterialState). Directly
mutating the set is possible, and may be necessary if you need to alter its
list without calling [setState](mcp://flutter/api/widgets/State/setState) (and thus triggering a re-render).

To check for a single condition, convenience getters [isPressed](mcp://flutter/api/material/MaterialStateMixin/isPressed), [isHovered](mcp://flutter/api/material/MaterialStateMixin/isHovered), [isFocused](mcp://flutter/api/material/MaterialStateMixin/isFocused), etc, are available for each [WidgetState](mcp://flutter/api/widgets/WidgetState) value.

## Implementation

```dart
@protected
Set<WidgetState> materialStates = <WidgetState>{};
```