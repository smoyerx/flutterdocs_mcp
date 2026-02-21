# isThreeLine property

[bool](flutter-docs://api/dart-core/bool)? isThreeLine


Whether this list tile is intended to display three lines of text.

If true, then [subtitle](flutter-docs://api/material/ListTile/subtitle) must be non-null (since it is expected to give
the second and third lines of text).

If false, the list tile is treated as having one line if the subtitle is
null and treated as having two lines if the subtitle is non-null.

When using a [Text](flutter-docs://api/widgets/Text) widget for [title](flutter-docs://api/material/ListTile/title) and [subtitle](flutter-docs://api/material/ListTile/subtitle), you can enforce
line limits using [Text.maxLines](flutter-docs://api/widgets/Text/maxLines).

See also:

- [ListTileTheme.of](flutter-docs://api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](flutter-docs://api/material/ListTileTheme)'s
[ListTileThemeData](flutter-docs://api/material/ListTileThemeData).


## Implementation

```dart
final bool? isThreeLine;
```