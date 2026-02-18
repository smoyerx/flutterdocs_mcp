# MaterialState typedef

1. @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use WidgetState instead. ' 'Moved to the Widgets layer to make code available outside of Material. ' 'This feature was deprecated after v3.19.0-0.3.pre.')

MaterialState = [WidgetState](mcp://flutter/api/widgets/WidgetState)

Interactive states that some of the Material widgets can take on when
receiving input from the user.

States are defined by <https://material.io/design/interaction/states.html#usage>.

Some Material widgets track their current state in a `Set<MaterialState>`.

See also:

- [WidgetState](mcp://flutter/api/widgets/WidgetState), a general non-Material version that can be used
interchangeably with `MaterialState`. They functionally work the same,
except [WidgetState](mcp://flutter/api/widgets/WidgetState) can be used outside of Material.
- [MaterialStateProperty](mcp://flutter/api/material/MaterialStateProperty), an interface for objects that "resolve" to
different values depending on a widget's material state.
- [MaterialStateColor](mcp://flutter/api/material/MaterialStateColor), a [Color](mcp://flutter/api/dart-ui/Color) that implements `MaterialStateProperty` which is used in APIs that need to accept either a [Color](mcp://flutter/api/dart-ui/Color) or a `MaterialStateProperty<Color>`.
- [MaterialStateMouseCursor](mcp://flutter/api/material/MaterialStateMouseCursor), a [MouseCursor](mcp://flutter/api/services/MouseCursor) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
a [MouseCursor](mcp://flutter/api/services/MouseCursor) or a [MaterialStateProperty<MouseCursor>](mcp://flutter/api/material/MaterialStateProperty).
- [MaterialStateOutlinedBorder](mcp://flutter/api/material/MaterialStateOutlinedBorder), an [OutlinedBorder](mcp://flutter/api/painting/OutlinedBorder) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
an [OutlinedBorder](mcp://flutter/api/painting/OutlinedBorder) or a [MaterialStateProperty<OutlinedBorder>](mcp://flutter/api/material/MaterialStateProperty).
- [MaterialStateOutlineInputBorder](mcp://flutter/api/material/MaterialStateOutlineInputBorder), an [OutlineInputBorder](mcp://flutter/api/material/OutlineInputBorder) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
an [OutlineInputBorder](mcp://flutter/api/material/OutlineInputBorder) or a [MaterialStateProperty<OutlineInputBorder>](mcp://flutter/api/material/MaterialStateProperty).
- [MaterialStateUnderlineInputBorder](mcp://flutter/api/material/MaterialStateUnderlineInputBorder), an [UnderlineInputBorder](mcp://flutter/api/material/UnderlineInputBorder) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
an [UnderlineInputBorder](mcp://flutter/api/material/UnderlineInputBorder) or a [MaterialStateProperty<UnderlineInputBorder>](mcp://flutter/api/material/MaterialStateProperty).
- [MaterialStateBorderSide](mcp://flutter/api/material/MaterialStateBorderSide), a [BorderSide](mcp://flutter/api/painting/BorderSide) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
a [BorderSide](mcp://flutter/api/painting/BorderSide) or a [MaterialStateProperty<BorderSide>](mcp://flutter/api/material/MaterialStateProperty).
- [MaterialStateTextStyle](mcp://flutter/api/material/MaterialStateTextStyle), a [TextStyle](mcp://flutter/api/painting/TextStyle) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
a [TextStyle](mcp://flutter/api/painting/TextStyle) or a [MaterialStateProperty<TextStyle>](mcp://flutter/api/material/MaterialStateProperty).


## Implementation

```dart
@Deprecated(
  'Use WidgetState instead. '
  'Moved to the Widgets layer to make code available outside of Material. '
  'This feature was deprecated after v3.19.0-0.3.pre.',
)
typedef MaterialState = WidgetState;
```