# titleAlignment property

[ListTileTitleAlignment](mcp://flutter/api/material/ListTileTitleAlignment)? titleAlignment


Defines how [ListTile.leading](mcp://flutter/api/material/ListTile/leading) and [ListTile.trailing](mcp://flutter/api/material/ListTile/trailing) are
vertically aligned relative to the [ListTile](mcp://flutter/api/material/ListTile)'s titles
([ListTile.title](mcp://flutter/api/material/ListTile/title) and [ListTile.subtitle](mcp://flutter/api/material/ListTile/subtitle)).

If this property is null then [ListTileThemeData.titleAlignment](mcp://flutter/api/material/ListTileThemeData/titleAlignment) is used. If that is also null then [ListTileTitleAlignment.threeLine](mcp://flutter/api/material/ListTileTitleAlignment) is used.

See also:

- [ListTileTheme.of](mcp://flutter/api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](mcp://flutter/api/material/ListTileTheme)'s
[ListTileThemeData](mcp://flutter/api/material/ListTileThemeData).


## Implementation

```dart
final ListTileTitleAlignment? titleAlignment;
```