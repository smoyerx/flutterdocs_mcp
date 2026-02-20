# MaterialState typedef

1. @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use WidgetState instead. ' 'Moved to the Widgets layer to make code available outside of Material. ' 'This feature was deprecated after v3.19.0-0.3.pre.')

MaterialState = [WidgetState](flutter-docs://api/widgets/WidgetState)

Interactive states that some of the Material widgets can take on when
receiving input from the user.

States are defined by <https://material.io/design/interaction/states.html#usage>.

Some Material widgets track their current state in a `Set<MaterialState>`.

See also:

- [WidgetState](flutter-docs://api/widgets/WidgetState), a general non-Material version that can be used
interchangeably with `MaterialState`. They functionally work the same,
except [WidgetState](flutter-docs://api/widgets/WidgetState) can be used outside of Material.
- [MaterialStateProperty](flutter-docs://api/material/MaterialStateProperty), an interface for objects that "resolve" to
different values depending on a widget's material state.
- [MaterialStateColor](flutter-docs://api/material/MaterialStateColor), a [Color](flutter-docs://api/dart-ui/Color) that implements `MaterialStateProperty` which is used in APIs that need to accept either a [Color](flutter-docs://api/dart-ui/Color) or a `MaterialStateProperty<Color>`.
- [MaterialStateMouseCursor](flutter-docs://api/material/MaterialStateMouseCursor), a [MouseCursor](flutter-docs://api/services/MouseCursor) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
a [MouseCursor](flutter-docs://api/services/MouseCursor) or a [MaterialStateProperty<MouseCursor>](flutter-docs://api/material/MaterialStateProperty).
- [MaterialStateOutlinedBorder](flutter-docs://api/material/MaterialStateOutlinedBorder), an [OutlinedBorder](flutter-docs://api/painting/OutlinedBorder) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
an [OutlinedBorder](flutter-docs://api/painting/OutlinedBorder) or a [MaterialStateProperty<OutlinedBorder>](flutter-docs://api/material/MaterialStateProperty).
- [MaterialStateOutlineInputBorder](flutter-docs://api/material/MaterialStateOutlineInputBorder), an [OutlineInputBorder](flutter-docs://api/material/OutlineInputBorder) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
an [OutlineInputBorder](flutter-docs://api/material/OutlineInputBorder) or a [MaterialStateProperty<OutlineInputBorder>](flutter-docs://api/material/MaterialStateProperty).
- [MaterialStateUnderlineInputBorder](flutter-docs://api/material/MaterialStateUnderlineInputBorder), an [UnderlineInputBorder](flutter-docs://api/material/UnderlineInputBorder) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
an [UnderlineInputBorder](flutter-docs://api/material/UnderlineInputBorder) or a [MaterialStateProperty<UnderlineInputBorder>](flutter-docs://api/material/MaterialStateProperty).
- [MaterialStateBorderSide](flutter-docs://api/material/MaterialStateBorderSide), a [BorderSide](flutter-docs://api/painting/BorderSide) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
a [BorderSide](flutter-docs://api/painting/BorderSide) or a [MaterialStateProperty<BorderSide>](flutter-docs://api/material/MaterialStateProperty).
- [MaterialStateTextStyle](flutter-docs://api/material/MaterialStateTextStyle), a [TextStyle](flutter-docs://api/painting/TextStyle) that implements
`MaterialStateProperty` which is used in APIs that need to accept either
a [TextStyle](flutter-docs://api/painting/TextStyle) or a [MaterialStateProperty<TextStyle>](flutter-docs://api/material/MaterialStateProperty).


## Implementation

```dart
@Deprecated(
  'Use WidgetState instead. '
  'Moved to the Widgets layer to make code available outside of Material. '
  'This feature was deprecated after v3.19.0-0.3.pre.',
)
typedef MaterialState = WidgetState;
```