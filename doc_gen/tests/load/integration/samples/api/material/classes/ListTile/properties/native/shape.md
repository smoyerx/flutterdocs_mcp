# shape property

[ShapeBorder](mcp://flutter/api/painting/ShapeBorder)? shape


Defines the tile's [InkWell.customBorder](mcp://flutter/api/material/InkResponse/customBorder) and [Ink.decoration](mcp://flutter/api/material/Ink/decoration) shape.

If this property is null then [ListTileThemeData.shape](mcp://flutter/api/material/ListTileThemeData/shape) is used. If that
is also null then a rectangular [Border](mcp://flutter/api/painting/Border) will be used.

See also:

- [ListTileTheme.of](mcp://flutter/api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](mcp://flutter/api/material/ListTileTheme)'s
[ListTileThemeData](mcp://flutter/api/material/ListTileThemeData).


## Implementation

```dart
final ShapeBorder? shape;
```