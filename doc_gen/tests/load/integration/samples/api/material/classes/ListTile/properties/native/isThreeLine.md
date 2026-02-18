# isThreeLine property

[bool](mcp://flutter/api/dart-core/bool)? isThreeLine


Whether this list tile is intended to display three lines of text.

If true, then [subtitle](mcp://flutter/api/material/ListTile/subtitle) must be non-null (since it is expected to give
the second and third lines of text).

If false, the list tile is treated as having one line if the subtitle is
null and treated as having two lines if the subtitle is non-null.

When using a [Text](mcp://flutter/api/widgets/Text) widget for [title](mcp://flutter/api/material/ListTile/title) and [subtitle](mcp://flutter/api/material/ListTile/subtitle), you can enforce
line limits using [Text.maxLines](mcp://flutter/api/widgets/Text/maxLines).

See also:

- [ListTileTheme.of](mcp://flutter/api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](mcp://flutter/api/material/ListTileTheme)'s
[ListTileThemeData](mcp://flutter/api/material/ListTileThemeData).


## Implementation

```dart
final bool? isThreeLine;
```