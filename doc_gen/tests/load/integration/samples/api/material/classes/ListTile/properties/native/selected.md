# selected property

[bool](mcp://flutter/api/dart-core/bool) selected


If this tile is also [enabled](mcp://flutter/api/material/ListTile/enabled) then icons and text are rendered with the same color.

By default the selected color is the theme's primary color. The selected color
can be overridden with a [ListTileTheme](mcp://flutter/api/material/ListTileTheme).

Here is an example of using a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) to keep track of the
selected index, and using that to set the [selected](mcp://flutter/api/material/ListTile/selected) property on the
corresponding [ListTile](mcp://flutter/api/material/ListTile).


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.selected.1 mysample

[Omitted code: Interactive sample]

## Implementation

```dart
final bool selected;
```