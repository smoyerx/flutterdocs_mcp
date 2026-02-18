# minTileHeight property

[double](mcp://flutter/api/dart-core/double)? minTileHeight


The minimum height allocated for the [ListTile](mcp://flutter/api/material/ListTile) widget.

If this is null, default tile heights are 56.0, 72.0, and 88.0 for one,
two, and three lines of text respectively. If `isDense` is true, these
defaults are changed to 48.0, 64.0, and 76.0. A visual density value or
a large title will also adjust the default tile heights.

## Implementation

```dart
final double? minTileHeight;
```