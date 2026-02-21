# shape property

[ShapeBorder](flutter-docs://api/painting/ShapeBorder)? shape


Defines the tile's [InkWell.customBorder](flutter-docs://api/material/InkResponse/customBorder) and [Ink.decoration](flutter-docs://api/material/Ink/decoration) shape.

If this property is null then [ListTileThemeData.shape](flutter-docs://api/material/ListTileThemeData/shape) is used. If that
is also null then a rectangular [Border](flutter-docs://api/painting/Border) will be used.

See also:

- [ListTileTheme.of](flutter-docs://api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](flutter-docs://api/material/ListTileTheme)'s
[ListTileThemeData](flutter-docs://api/material/ListTileThemeData).


## Implementation

```dart
final ShapeBorder? shape;
```