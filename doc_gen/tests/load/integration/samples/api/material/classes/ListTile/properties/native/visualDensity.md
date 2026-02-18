# visualDensity property

[VisualDensity](mcp://flutter/api/material/VisualDensity)? visualDensity


Defines how compact the list tile's layout will be.

Density, in the context of a UI, is the vertical and horizontal
"compactness" of the elements in the UI. It is unitless, since it means
different things to different UI elements. For buttons, it affects the
spacing around the centered label of the button. For lists, it affects the
distance between baselines of entries in the list.

Typically, density values are integral, but any value in range may be
used. The range includes values from [VisualDensity.minimumDensity](mcp://flutter/api/material/VisualDensity/minimumDensity) (which
is -4), to [VisualDensity.maximumDensity](mcp://flutter/api/material/VisualDensity/maximumDensity) (which is 4), inclusive, where
negative values indicate a denser, more compact, UI, and positive values
indicate a less dense, more expanded, UI. If a component doesn't support
the value given, it will clamp to the nearest supported value.

The default for visual densities is zero for both vertical and horizontal
densities, which corresponds to the default visual density of components
in the Material Design specification.

As a rule of thumb, a change of 1 or -1 in density corresponds to 4
logical pixels. However, this is not a strict relationship since
components interpret the density values appropriately for their needs.

A larger value translates to a spacing increase (less dense), and a
smaller value translates to a spacing decrease (more dense).

In Material Design 3, the [visualDensity](mcp://flutter/api/material/ListTile/visualDensity) does not override the default
visual for the following components which are set to [VisualDensity.standard](mcp://flutter/api/material/VisualDensity/standard) for all platforms:

- [IconButton](mcp://flutter/api/material/IconButton) - To override the default value of [IconButton.visualDensity](mcp://flutter/api/material/IconButton/visualDensity),
use [ThemeData.iconButtonTheme](mcp://flutter/api/material/ThemeData/iconButtonTheme) instead.
- [Checkbox](mcp://flutter/api/material/Checkbox) - To override the default value of [Checkbox.visualDensity](mcp://flutter/api/material/Checkbox/visualDensity),
use [ThemeData.checkboxTheme](mcp://flutter/api/material/ThemeData/checkboxTheme) instead.


See also:

- [ThemeData.visualDensity](mcp://flutter/api/material/ThemeData/visualDensity), which specifies the [visualDensity](mcp://flutter/api/material/ListTile/visualDensity) for all
widgets within a [Theme](mcp://flutter/api/material/Theme).


## Implementation

```dart
final VisualDensity? visualDensity;
```