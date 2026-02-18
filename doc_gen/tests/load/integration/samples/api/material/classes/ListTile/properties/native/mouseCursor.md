# mouseCursor property

[MouseCursor](mcp://flutter/api/services/MouseCursor)? mouseCursor


The cursor for a mouse pointer when it enters or is hovering over the
widget.

If [mouseCursor](mcp://flutter/api/material/ListTile/mouseCursor) is a [WidgetStateMouseCursor](mcp://flutter/api/widgets/WidgetStateMouseCursor), [WidgetStateProperty.resolve](mcp://flutter/api/widgets/WidgetStateProperty/resolve) is used for the following [WidgetState](mcp://flutter/api/widgets/WidgetState) s:

- [WidgetState.selected](mcp://flutter/api/widgets/WidgetState).
- [WidgetState.disabled](mcp://flutter/api/widgets/WidgetState).


If null, then the value of [ListTileThemeData.mouseCursor](mcp://flutter/api/material/ListTileThemeData/mouseCursor) is used. If
that is also null, then [WidgetStateMouseCursor.clickable](mcp://flutter/api/widgets/WidgetStateMouseCursor/clickable) is used.

## Implementation

```dart
final MouseCursor? mouseCursor;
```