# divideTiles static method

[Iterable](mcp://flutter/api/dart-core/Iterable)<[Widget](mcp://flutter/api/widgets/Widget)>divideTiles({
[BuildContext](mcp://flutter/api/widgets/BuildContext)? context,
required [Iterable](mcp://flutter/api/dart-core/Iterable)<[Widget](mcp://flutter/api/widgets/Widget)> tiles,
[Color](mcp://flutter/api/dart-ui/Color)? color,
})

Add a one pixel border in between each tile. If color isn't specified the[ThemeData.dividerColor](mcp://flutter/api/material/ThemeData/dividerColor) of the context's [Theme](mcp://flutter/api/material/Theme) is used.

See also:

- [Divider](mcp://flutter/api/material/Divider), which you can use to obtain this effect manually.


## Implementation

```dart
static Iterable<Widget> divideTiles({
  BuildContext? context,
  required Iterable<Widget> tiles,
  Color? color,
}) {
  assert(color != null || context != null);
  tiles = tiles.toList();

  if (tiles.isEmpty || tiles.length == 1) {
    return tiles;
  }

  Widget wrapTile(Widget tile) {
    return DecoratedBox(
      position: DecorationPosition.foreground,
      decoration: BoxDecoration(
        border: Border(bottom: Divider.createBorderSide(context, color: color)),
      ),
      child: tile,
    );
  }

  return <Widget>[...tiles.take(tiles.length - 1).map(wrapTile), tiles.last];
}
```