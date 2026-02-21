# titleAlignment property

[ListTileTitleAlignment](flutter-docs://api/material/ListTileTitleAlignment)? titleAlignment


Defines how [ListTile.leading](flutter-docs://api/material/ListTile/leading) and [ListTile.trailing](flutter-docs://api/material/ListTile/trailing) are
vertically aligned relative to the [ListTile](flutter-docs://api/material/ListTile)'s titles
([ListTile.title](flutter-docs://api/material/ListTile/title) and [ListTile.subtitle](flutter-docs://api/material/ListTile/subtitle)).

If this property is null then [ListTileThemeData.titleAlignment](flutter-docs://api/material/ListTileThemeData/titleAlignment) is used. If that is also null then [ListTileTitleAlignment.threeLine](flutter-docs://api/material/ListTileTitleAlignment) is used.

See also:

- [ListTileTheme.of](flutter-docs://api/material/ListTileTheme/of), which returns the nearest [ListTileTheme](flutter-docs://api/material/ListTileTheme)'s
[ListTileThemeData](flutter-docs://api/material/ListTileThemeData).


## Implementation

```dart
final ListTileTitleAlignment? titleAlignment;
```