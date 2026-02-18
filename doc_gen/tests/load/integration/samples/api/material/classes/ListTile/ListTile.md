# ListTile class

A single fixed-height row that typically contains some text as well as
a leading or trailing icon.

[https://www.youtube.com/embed/l8dj0yPBvgQ?rel=0](https://www.youtube.com/embed/l8dj0yPBvgQ?rel=0)

A list tile contains one to three lines of text optionally flanked by icons or
other widgets, such as check boxes. The icons (or other widgets) for the
tile are defined with the [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) parameters. The first
line of text is not optional and is specified with [title](mcp://flutter/api/material/ListTile/title). The value of [subtitle](mcp://flutter/api/material/ListTile/subtitle), which *is* optional, will occupy the space allocated for an
additional line of text, or two lines if [isThreeLine](mcp://flutter/api/material/ListTile/isThreeLine) is true. If [dense](mcp://flutter/api/material/ListTile/dense) is true then the overall height of this tile and the size of the [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle) s that wrap the [title](mcp://flutter/api/material/ListTile/title) and [subtitle](mcp://flutter/api/material/ListTile/subtitle) widget are reduced.

It is the responsibility of the caller to ensure that [title](mcp://flutter/api/material/ListTile/title) does not wrap,
and to ensure that [subtitle](mcp://flutter/api/material/ListTile/subtitle) doesn't wrap (if [isThreeLine](mcp://flutter/api/material/ListTile/isThreeLine) is false) or
wraps to two lines (if it is true).

The heights of the [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) widgets are constrained
according to the [Material spec](https://material.io/design/components/lists.html).
An exception is made for one-line ListTiles for accessibility. Please
see the example below to see how to adhere to both Material spec and
accessibility requirements.

The [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) widgets can expand as far as they wish
horizontally, so ensure that they are properly constrained.

List tiles are typically used in [ListView](mcp://flutter/api/widgets/ListView) s, or arranged in [Column](mcp://flutter/api/widgets/Column) s in [Drawer](mcp://flutter/api/material/Drawer) s and [Card](mcp://flutter/api/material/Card) s.

This widget requires a [Material](mcp://flutter/api/material/Material) widget ancestor in the tree to paint
itself on, which is typically provided by the app's [Scaffold](mcp://flutter/api/material/Scaffold).
The [tileColor](mcp://flutter/api/material/ListTile/tileColor), [selectedTileColor](mcp://flutter/api/material/ListTile/selectedTileColor), [focusColor](mcp://flutter/api/material/ListTile/focusColor), and [hoverColor](mcp://flutter/api/material/ListTile/hoverColor) are not painted by the [ListTile](mcp://flutter/api/material/ListTile) itself but by the [Material](mcp://flutter/api/material/Material) widget
ancestor. In this case, one can wrap a [Material](mcp://flutter/api/material/Material) widget around the [ListTile](mcp://flutter/api/material/ListTile), e.g.:



```dart
const ColoredBox(
  color: Colors.green,
  child: Material(
    child: ListTile(
      title: Text('ListTile with red background'),
      tileColor: Colors.red,
    ),
  ),
)
```

## Performance considerations when wrapping [ListTile](mcp://flutter/api/material/ListTile) with [Material](mcp://flutter/api/material/Material)

Wrapping a large number of [ListTile](mcp://flutter/api/material/ListTile) s individually with [Material](mcp://flutter/api/material/Material) s
is expensive. Consider only wrapping the [ListTile](mcp://flutter/api/material/ListTile) s that require it
or include a common [Material](mcp://flutter/api/material/Material) ancestor where possible.

[ListTile](mcp://flutter/api/material/ListTile) must be wrapped in a [Material](mcp://flutter/api/material/Material) widget to animate [tileColor](mcp://flutter/api/material/ListTile/tileColor), [selectedTileColor](mcp://flutter/api/material/ListTile/selectedTileColor), [focusColor](mcp://flutter/api/material/ListTile/focusColor), and [hoverColor](mcp://flutter/api/material/ListTile/hoverColor) as these colors
are not drawn by the list tile itself but by the material widget ancestor.

This example showcases how [ListTile](mcp://flutter/api/material/ListTile) needs to be wrapped in a [Material](mcp://flutter/api/material/Material) widget to animate colors.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.2 mysample

[Omitted code: Interactive sample]

This example uses a [ListView](mcp://flutter/api/widgets/ListView) to demonstrate different configurations of
[ListTile](mcp://flutter/api/material/ListTile) s in [Card](mcp://flutter/api/material/Card) s.



[Omitted image: Different variations of ListTile]


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.3 mysample

[Omitted code: Interactive sample]

This sample shows the creation of a [ListTile](mcp://flutter/api/material/ListTile) using [ThemeData.useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) flag,
as described in: <https://m3.material.io/components/lists/overview>.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.4 mysample

[Omitted code: Interactive sample]

This sample shows [ListTile](mcp://flutter/api/material/ListTile)'s [textColor](mcp://flutter/api/material/ListTile/textColor) and [iconColor](mcp://flutter/api/material/ListTile/iconColor) can use
[WidgetStateColor](mcp://flutter/api/widgets/WidgetStateColor) color to change the color of the text and icon
when the [ListTile](mcp://flutter/api/material/ListTile) is enabled, selected, or disabled.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.5 mysample

[Omitted code: Interactive sample]

This sample shows [ListTile.titleAlignment](mcp://flutter/api/material/ListTile/titleAlignment) can be used to configure the
[leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) widgets alignment relative to the [title](mcp://flutter/api/material/ListTile/title) and
[subtitle](mcp://flutter/api/material/ListTile/subtitle) widgets.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.6 mysample

[Omitted code: Interactive sample]

To use a [ListTile](mcp://flutter/api/material/ListTile) within a [Row](mcp://flutter/api/widgets/Row), it needs to be wrapped in an
[Expanded](mcp://flutter/api/widgets/Expanded) widget. [ListTile](mcp://flutter/api/material/ListTile) requires fixed width constraints,
whereas a [Row](mcp://flutter/api/widgets/Row) does not constrain its children.



```dart
const Row(
  children: <Widget>[
    Expanded(
      child: ListTile(
        leading: FlutterLogo(),
        title: Text('These ListTiles are expanded '),
      ),
    ),
    Expanded(
      child: ListTile(
        trailing: FlutterLogo(),
        title: Text('to fill the available space.'),
      ),
    ),
  ],
)
```

Tiles can be much more elaborate. Here is a tile which can be tapped, but
which is disabled when the `_act` variable is not 2. When the tile is
tapped, the whole row has an ink splash effect (see [InkWell](mcp://flutter/api/material/InkWell)).



```dart
ListTile(
  leading: const Icon(Icons.flight_land),
  title: const Text("Trix's airplane"),
  subtitle: _act != 2 ? const Text('The airplane is only in Act II.') : null,
  enabled: _act == 2,
  onTap: () { /* react to the tile being tapped */ }
)
```

To be accessible, tappable [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) widgets have to
be at least 48x48 in size. However, to adhere to the Material spec, [trailing](mcp://flutter/api/material/ListTile/trailing) and [leading](mcp://flutter/api/material/ListTile/leading) widgets in one-line ListTiles should visually be
at most 32 ([dense](mcp://flutter/api/material/ListTile/dense): true) or 40 ([dense](mcp://flutter/api/material/ListTile/dense): false) in height, which may
conflict with the accessibility requirement.

For this reason, a one-line ListTile allows the height of [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) widgets to be constrained by the height of the ListTile.
This allows for the creation of tappable [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) widgets
that are large enough, but it is up to the developer to ensure that
their widgets follow the Material spec.

Here is an example of a one-line, non-[dense](mcp://flutter/api/material/ListTile/dense) ListTile with a
tappable leading widget that adheres to accessibility requirements and
the Material spec. To adjust the use case below for a one-line, [dense](mcp://flutter/api/material/ListTile/dense) ListTile, adjust the vertical padding to 8.0.



```dart
ListTile(
  leading: GestureDetector(
    behavior: HitTestBehavior.translucent,
    onTap: () {},
    child: Container(
      width: 48,
      height: 48,
      padding: const EdgeInsets.symmetric(vertical: 4.0),
      alignment: Alignment.center,
      child: const CircleAvatar(),
    ),
  ),
  title: const Text('title'),
  dense: false,
)
```

## The ListTile layout isn't exactly what I want

If the way ListTile pads and positions its elements isn't quite what
you're looking for, it's easy to create custom list items with a
combination of other widgets, such as [Row](mcp://flutter/api/widgets/Row) s and [Column](mcp://flutter/api/widgets/Column) s.

Here is an example of a custom list item that resembles a YouTube-related
video list item created with [Expanded](mcp://flutter/api/widgets/Expanded) and [Container](mcp://flutter/api/widgets/Container) widgets.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.10 mysample

[Omitted code: Interactive sample]

Here is an example of an article list item with multiline titles and
subtitles. It utilizes [Row](mcp://flutter/api/widgets/Row) s and [Column](mcp://flutter/api/widgets/Column) s, as well as [Expanded](mcp://flutter/api/widgets/Expanded) and
[AspectRatio](mcp://flutter/api/widgets/AspectRatio) widgets to organize its layout.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.11 mysample

[Omitted code: Interactive sample]

See also:

- [ListTileTheme](mcp://flutter/api/material/ListTileTheme), which defines visual properties for [ListTile](mcp://flutter/api/material/ListTile) s.
- [ListView](mcp://flutter/api/widgets/ListView), which can display an arbitrary number of [ListTile](mcp://flutter/api/material/ListTile) s
in a scrolling list.
- [CircleAvatar](mcp://flutter/api/material/CircleAvatar), which shows an icon representing a person and is often
used as the [leading](mcp://flutter/api/material/ListTile/leading) element of a ListTile.
- [Card](mcp://flutter/api/material/Card), which can be used with [Column](mcp://flutter/api/widgets/Column) to show a few [ListTile](mcp://flutter/api/material/ListTile) s.
- [Divider](mcp://flutter/api/material/Divider), which can be used to separate [ListTile](mcp://flutter/api/material/ListTile) s.
- [ListTile.divideTiles](mcp://flutter/api/material/ListTile/divideTiles), a utility for inserting [Divider](mcp://flutter/api/material/Divider) s in between [ListTile](mcp://flutter/api/material/ListTile) s.
- [CheckboxListTile](mcp://flutter/api/material/CheckboxListTile), [RadioListTile](mcp://flutter/api/material/RadioListTile), and [SwitchListTile](mcp://flutter/api/material/SwitchListTile), widgets
that combine [ListTile](mcp://flutter/api/material/ListTile) with other controls.
- Material 3 [ListTile](mcp://flutter/api/material/ListTile) specifications are referenced from [m3.material.io/components/lists/specs](https://m3.material.io/components/lists/specs) and Material 2 [ListTile](mcp://flutter/api/material/ListTile) specifications are referenced from [material.io/design/components/lists.html](https://material.io/design/components/lists.html)
- Cookbook: [Use lists](https://docs.flutter.dev/cookbook/lists/basic-list)
- Cookbook: [Implement swipe to dismiss](https://docs.flutter.dev/cookbook/gestures/dismissible)


Inheritance
- [Object](mcp://flutter/api/dart-core/Object)
- [DiagnosticableTree](mcp://flutter/api/foundation/DiagnosticableTree)
- [Widget](mcp://flutter/api/widgets/Widget)
- [StatelessWidget](mcp://flutter/api/widgets/StatelessWidget)
- ListTile

## Constructors

[ListTile](mcp://flutter/api/material/ListTile/ListTile)({[Key](mcp://flutter/api/foundation/Key)? key, [Widget](mcp://flutter/api/widgets/Widget)? leading, [Widget](mcp://flutter/api/widgets/Widget)? title, [Widget](mcp://flutter/api/widgets/Widget)? subtitle, [Widget](mcp://flutter/api/widgets/Widget)? trailing, [bool](mcp://flutter/api/dart-core/bool)? isThreeLine, [bool](mcp://flutter/api/dart-core/bool)? dense, [VisualDensity](mcp://flutter/api/material/VisualDensity)? visualDensity, [ShapeBorder](mcp://flutter/api/painting/ShapeBorder)? shape, [ListTileStyle](mcp://flutter/api/material/ListTileStyle)? style, [Color](mcp://flutter/api/dart-ui/Color)? selectedColor, [Color](mcp://flutter/api/dart-ui/Color)? iconColor, [Color](mcp://flutter/api/dart-ui/Color)? textColor, [TextStyle](mcp://flutter/api/painting/TextStyle)? titleTextStyle, [TextStyle](mcp://flutter/api/painting/TextStyle)? subtitleTextStyle, [TextStyle](mcp://flutter/api/painting/TextStyle)? leadingAndTrailingTextStyle, [EdgeInsetsGeometry](mcp://flutter/api/painting/EdgeInsetsGeometry)? contentPadding, [bool](mcp://flutter/api/dart-core/bool) enabled = true, [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)? onTap, [GestureLongPressCallback](mcp://flutter/api/gestures/GestureLongPressCallback)? onLongPress, [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>? onFocusChange, [MouseCursor](mcp://flutter/api/services/MouseCursor)? mouseCursor, [bool](mcp://flutter/api/dart-core/bool) selected = false, [Color](mcp://flutter/api/dart-ui/Color)? focusColor, [Color](mcp://flutter/api/dart-ui/Color)? hoverColor, [Color](mcp://flutter/api/dart-ui/Color)? splashColor, [FocusNode](mcp://flutter/api/widgets/FocusNode)? focusNode, [bool](mcp://flutter/api/dart-core/bool) autofocus = false, [Color](mcp://flutter/api/dart-ui/Color)? tileColor, [Color](mcp://flutter/api/dart-ui/Color)? selectedTileColor, [bool](mcp://flutter/api/dart-core/bool)? enableFeedback, [double](mcp://flutter/api/dart-core/double)? horizontalTitleGap, [double](mcp://flutter/api/dart-core/double)? minVerticalPadding, [double](mcp://flutter/api/dart-core/double)? minLeadingWidth, [double](mcp://flutter/api/dart-core/double)? minTileHeight, [ListTileTitleAlignment](mcp://flutter/api/material/ListTileTitleAlignment)? titleAlignment, [bool](mcp://flutter/api/dart-core/bool) internalAddSemanticForOnTap = true, [MaterialStatesController](mcp://flutter/api/material/MaterialStatesController)? statesController})
Creates a list tile.


## Properties

[autofocus](mcp://flutter/api/material/ListTile/autofocus) → [bool](mcp://flutter/api/dart-core/bool)
True if this widget will be selected as the initial focus when no other
node in its scope is currently focused.


[contentPadding](mcp://flutter/api/material/ListTile/contentPadding) → [EdgeInsetsGeometry](mcp://flutter/api/painting/EdgeInsetsGeometry)?
The tile's internal padding.


[dense](mcp://flutter/api/material/ListTile/dense) → [bool](mcp://flutter/api/dart-core/bool)?
Whether this list tile is part of a vertically dense list.


[enabled](mcp://flutter/api/material/ListTile/enabled) → [bool](mcp://flutter/api/dart-core/bool)
Whether this list tile is interactive.


[enableFeedback](mcp://flutter/api/material/ListTile/enableFeedback) → [bool](mcp://flutter/api/dart-core/bool)?
Whether detected gestures should provide acoustic and/or haptic feedback.


[focusColor](mcp://flutter/api/material/ListTile/focusColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The color for the tile's [Material](mcp://flutter/api/material/Material) when it has the input focus.


[focusNode](mcp://flutter/api/material/ListTile/focusNode) → [FocusNode](mcp://flutter/api/widgets/FocusNode)?
An optional focus node to use as the focus node for this widget.


[hashCode](mcp://flutter/api/widgets/Widget/hashCode) → [int](mcp://flutter/api/dart-core/int)
The hash code for this object.


[horizontalTitleGap](mcp://flutter/api/material/ListTile/horizontalTitleGap) → [double](mcp://flutter/api/dart-core/double)?
The horizontal gap between the titles and the leading/trailing widgets.


[hoverColor](mcp://flutter/api/material/ListTile/hoverColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The color for the tile's [Material](mcp://flutter/api/material/Material) when a pointer is hovering over it.


[iconColor](mcp://flutter/api/material/ListTile/iconColor) → [Color](mcp://flutter/api/dart-ui/Color)?
Defines the default color for [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing) icons.


[internalAddSemanticForOnTap](mcp://flutter/api/material/ListTile/internalAddSemanticForOnTap) → [bool](mcp://flutter/api/dart-core/bool)
Whether to add button:true to the semantics if onTap is provided.
This is a temporary flag to help changing the behavior of ListTile onTap semantics.


[isThreeLine](mcp://flutter/api/material/ListTile/isThreeLine) → [bool](mcp://flutter/api/dart-core/bool)?
Whether this list tile is intended to display three lines of text.


[key](mcp://flutter/api/widgets/Widget/key) → [Key](mcp://flutter/api/foundation/Key)?
Controls how one widget replaces another widget in the tree.


[leading](mcp://flutter/api/material/ListTile/leading) → [Widget](mcp://flutter/api/widgets/Widget)?
A widget to display before the title.


[leadingAndTrailingTextStyle](mcp://flutter/api/material/ListTile/leadingAndTrailingTextStyle) → [TextStyle](mcp://flutter/api/painting/TextStyle)?
The text style for ListTile's [leading](mcp://flutter/api/material/ListTile/leading) and [trailing](mcp://flutter/api/material/ListTile/trailing).


[minLeadingWidth](mcp://flutter/api/material/ListTile/minLeadingWidth) → [double](mcp://flutter/api/dart-core/double)?
The minimum width allocated for the [ListTile.leading](mcp://flutter/api/material/ListTile/leading) widget.


[minTileHeight](mcp://flutter/api/material/ListTile/minTileHeight) → [double](mcp://flutter/api/dart-core/double)?
The minimum height allocated for the [ListTile](mcp://flutter/api/material/ListTile) widget.


[minVerticalPadding](mcp://flutter/api/material/ListTile/minVerticalPadding) → [double](mcp://flutter/api/dart-core/double)?
The minimum padding on the top and bottom of the title and subtitle widgets.


[mouseCursor](mcp://flutter/api/material/ListTile/mouseCursor) → [MouseCursor](mcp://flutter/api/services/MouseCursor)?
The cursor for a mouse pointer when it enters or is hovering over the
widget.


[onFocusChange](mcp://flutter/api/material/ListTile/onFocusChange) → [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>?
Handler called when the focus changes.


[onLongPress](mcp://flutter/api/material/ListTile/onLongPress) → [GestureLongPressCallback](mcp://flutter/api/gestures/GestureLongPressCallback)?
Called when the user long-presses on this list tile.


[onTap](mcp://flutter/api/material/ListTile/onTap) → [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)?
Called when the user taps this list tile.


[runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) → [Type](mcp://flutter/api/dart-core/Type)
A representation of the runtime type of the object.


[selected](mcp://flutter/api/material/ListTile/selected) → [bool](mcp://flutter/api/dart-core/bool)
If this tile is also [enabled](mcp://flutter/api/material/ListTile/enabled) then icons and text are rendered with the same color.


[selectedColor](mcp://flutter/api/material/ListTile/selectedColor) → [Color](mcp://flutter/api/dart-ui/Color)?
Defines the color used for icons and text when the list tile is selected.


[selectedTileColor](mcp://flutter/api/material/ListTile/selectedTileColor) → [Color](mcp://flutter/api/dart-ui/Color)?
Defines the background color of `ListTile` when [selected](mcp://flutter/api/material/ListTile/selected) is true.


[shape](mcp://flutter/api/material/ListTile/shape) → [ShapeBorder](mcp://flutter/api/painting/ShapeBorder)?
Defines the tile's [InkWell.customBorder](mcp://flutter/api/material/InkResponse/customBorder) and [Ink.decoration](mcp://flutter/api/material/Ink/decoration) shape.


[splashColor](mcp://flutter/api/material/ListTile/splashColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The color of splash for the tile's [Material](mcp://flutter/api/material/Material).


[statesController](mcp://flutter/api/material/ListTile/statesController) → [MaterialStatesController](mcp://flutter/api/material/MaterialStatesController)?
Represents the interactive "state" of this widget in terms of
a set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s, like [WidgetState.pressed](mcp://flutter/api/widgets/WidgetState) and
[WidgetState.focused](mcp://flutter/api/widgets/WidgetState).


[style](mcp://flutter/api/material/ListTile/style) → [ListTileStyle](mcp://flutter/api/material/ListTileStyle)?
Defines the font used for the [title](mcp://flutter/api/material/ListTile/title).


[subtitle](mcp://flutter/api/material/ListTile/subtitle) → [Widget](mcp://flutter/api/widgets/Widget)?
Additional content displayed below the title.


[subtitleTextStyle](mcp://flutter/api/material/ListTile/subtitleTextStyle) → [TextStyle](mcp://flutter/api/painting/TextStyle)?
The text style for ListTile's [subtitle](mcp://flutter/api/material/ListTile/subtitle).


[textColor](mcp://flutter/api/material/ListTile/textColor) → [Color](mcp://flutter/api/dart-ui/Color)?
Defines the text color for the [title](mcp://flutter/api/material/ListTile/title), [subtitle](mcp://flutter/api/material/ListTile/subtitle), [leading](mcp://flutter/api/material/ListTile/leading), and [trailing](mcp://flutter/api/material/ListTile/trailing).


[tileColor](mcp://flutter/api/material/ListTile/tileColor) → [Color](mcp://flutter/api/dart-ui/Color)?
Defines the background color of `ListTile` when [selected](mcp://flutter/api/material/ListTile/selected) is false.


[title](mcp://flutter/api/material/ListTile/title) → [Widget](mcp://flutter/api/widgets/Widget)?
The primary content of the list tile.


[titleAlignment](mcp://flutter/api/material/ListTile/titleAlignment) → [ListTileTitleAlignment](mcp://flutter/api/material/ListTileTitleAlignment)?
Defines how [ListTile.leading](mcp://flutter/api/material/ListTile/leading) and [ListTile.trailing](mcp://flutter/api/material/ListTile/trailing) are
vertically aligned relative to the [ListTile](mcp://flutter/api/material/ListTile)'s titles
([ListTile.title](mcp://flutter/api/material/ListTile/title) and [ListTile.subtitle](mcp://flutter/api/material/ListTile/subtitle)).


[titleTextStyle](mcp://flutter/api/material/ListTile/titleTextStyle) → [TextStyle](mcp://flutter/api/painting/TextStyle)?
The text style for ListTile's [title](mcp://flutter/api/material/ListTile/title).


[trailing](mcp://flutter/api/material/ListTile/trailing) → [Widget](mcp://flutter/api/widgets/Widget)?
A widget to display after the title.


[visualDensity](mcp://flutter/api/material/ListTile/visualDensity) → [VisualDensity](mcp://flutter/api/material/VisualDensity)?
Defines how compact the list tile's layout will be.


## Methods

[build](mcp://flutter/api/material/ListTile/build)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [Widget](mcp://flutter/api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[createElement](mcp://flutter/api/widgets/StatelessWidget/createElement)() → [StatelessElement](mcp://flutter/api/widgets/StatelessElement)
Creates a [StatelessElement](mcp://flutter/api/widgets/StatelessElement) to manage this widget's location in the tree.


[debugDescribeChildren](mcp://flutter/api/foundation/DiagnosticableTree/debugDescribeChildren)() → [List](mcp://flutter/api/dart-core/List)<[DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)>
Returns a list of [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode) objects describing this node's
children.


[debugFillProperties](mcp://flutter/api/material/ListTile/debugFillProperties)([DiagnosticPropertiesBuilder](mcp://flutter/api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[noSuchMethod](mcp://flutter/api/dart-core/Object/noSuchMethod)([Invocation](mcp://flutter/api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[toDiagnosticsNode](mcp://flutter/api/foundation/DiagnosticableTree/toDiagnosticsNode)({[String](mcp://flutter/api/dart-core/String)? name, [DiagnosticsTreeStyle](mcp://flutter/api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](mcp://flutter/api/foundation/DiagnosticsNode/toStringDeep).


[toString](mcp://flutter/api/foundation/Diagnosticable/toString)({[DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](mcp://flutter/api/dart-core/String)
A string representation of this object.


[toStringDeep](mcp://flutter/api/foundation/DiagnosticableTree/toStringDeep)({[String](mcp://flutter/api/dart-core/String) prefixLineOne = '', [String](mcp://flutter/api/dart-core/String)? prefixOtherLines, [DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.debug, [int](mcp://flutter/api/dart-core/int) wrapWidth = 65}) → [String](mcp://flutter/api/dart-core/String)
Returns a string representation of this node and its descendants.


[toStringShallow](mcp://flutter/api/foundation/DiagnosticableTree/toStringShallow)({[String](mcp://flutter/api/dart-core/String) joiner = ', ', [DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.debug}) → [String](mcp://flutter/api/dart-core/String)
Returns a one-line detailed description of the object.


[toStringShort](mcp://flutter/api/widgets/Widget/toStringShort)() → [String](mcp://flutter/api/dart-core/String)
A short, textual description of this widget.


## Operators

[operator ==](mcp://flutter/api/widgets/Widget/operator_equals)([Object](mcp://flutter/api/dart-core/Object) other) → [bool](mcp://flutter/api/dart-core/bool)
The equality operator.


## Static Methods

[divideTiles](mcp://flutter/api/material/ListTile/divideTiles)({[BuildContext](mcp://flutter/api/widgets/BuildContext)? context, required [Iterable](mcp://flutter/api/dart-core/Iterable)<[Widget](mcp://flutter/api/widgets/Widget)> tiles, [Color](mcp://flutter/api/dart-ui/Color)? color}) → [Iterable](mcp://flutter/api/dart-core/Iterable)<[Widget](mcp://flutter/api/widgets/Widget)>
Add a one pixel border in between each tile. If color isn't specified the
[ThemeData.dividerColor](mcp://flutter/api/material/ThemeData/dividerColor) of the context's [Theme](mcp://flutter/api/material/Theme) is used.