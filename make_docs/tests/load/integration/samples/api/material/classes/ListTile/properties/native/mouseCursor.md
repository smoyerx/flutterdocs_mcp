# mouseCursor property

[MouseCursor](flutter-docs://api/services/MouseCursor)? mouseCursor


The cursor for a mouse pointer when it enters or is hovering over the
widget.

If [mouseCursor](flutter-docs://api/material/ListTile/mouseCursor) is a [WidgetStateMouseCursor](flutter-docs://api/widgets/WidgetStateMouseCursor), [WidgetStateProperty.resolve](flutter-docs://api/widgets/WidgetStateProperty/resolve) is used for the following [WidgetState](flutter-docs://api/widgets/WidgetState) s:

- [WidgetState.selected](flutter-docs://api/widgets/WidgetState).
- [WidgetState.disabled](flutter-docs://api/widgets/WidgetState).


If null, then the value of [ListTileThemeData.mouseCursor](flutter-docs://api/material/ListTileThemeData/mouseCursor) is used. If
that is also null, then [WidgetStateMouseCursor.clickable](flutter-docs://api/widgets/WidgetStateMouseCursor/clickable) is used.

## Implementation

```dart
final MouseCursor? mouseCursor;
```