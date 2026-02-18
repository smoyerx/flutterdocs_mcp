# focusNode property

[FocusNode](mcp://flutter/api/widgets/FocusNode)? focusNode


An optional focus node to use as the focus node for this widget.

If one is not supplied, then one will be automatically allocated, owned,
and managed by this widget. The widget will be focusable even if a[focusNode](mcp://flutter/api/material/ListTile/focusNode) is not supplied. If supplied, the given [focusNode](mcp://flutter/api/material/ListTile/focusNode) will be *hosted* by this widget, but not owned. See [FocusNode](mcp://flutter/api/widgets/FocusNode) for more
information on what being hosted and/or owned implies.

Supplying a focus node is sometimes useful if an ancestor to this widget
wants to control when this widget has the focus. The owner will be
responsible for calling [FocusNode.dispose](mcp://flutter/api/widgets/FocusNode/dispose) on the focus node when it is
done with it, but this widget will attach/detach and reparent the node
when needed.

## Implementation

```dart
final FocusNode? focusNode;
```