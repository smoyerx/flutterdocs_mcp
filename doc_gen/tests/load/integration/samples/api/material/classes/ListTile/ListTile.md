# ListTile class

A single fixed-height row that typically contains some text as well as
a leading or trailing icon.

[https://www.youtube.com/embed/l8dj0yPBvgQ?rel=0](https://www.youtube.com/embed/l8dj0yPBvgQ?rel=0)

A list tile contains one to three lines of text optionally flanked by icons or
other widgets, such as check boxes. The icons (or other widgets) for the
tile are defined with the [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) parameters. The first
line of text is not optional and is specified with [title](flutter-docs://api/material/ListTile/title). The value of [subtitle](flutter-docs://api/material/ListTile/subtitle), which *is* optional, will occupy the space allocated for an
additional line of text, or two lines if [isThreeLine](flutter-docs://api/material/ListTile/isThreeLine) is true. If [dense](flutter-docs://api/material/ListTile/dense) is true then the overall height of this tile and the size of the [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle) s that wrap the [title](flutter-docs://api/material/ListTile/title) and [subtitle](flutter-docs://api/material/ListTile/subtitle) widget are reduced.

It is the responsibility of the caller to ensure that [title](flutter-docs://api/material/ListTile/title) does not wrap,
and to ensure that [subtitle](flutter-docs://api/material/ListTile/subtitle) doesn't wrap (if [isThreeLine](flutter-docs://api/material/ListTile/isThreeLine) is false) or
wraps to two lines (if it is true).

The heights of the [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) widgets are constrained
according to the [Material spec](https://material.io/design/components/lists.html).
An exception is made for one-line ListTiles for accessibility. Please
see the example below to see how to adhere to both Material spec and
accessibility requirements.

The [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) widgets can expand as far as they wish
horizontally, so ensure that they are properly constrained.

List tiles are typically used in [ListView](flutter-docs://api/widgets/ListView) s, or arranged in [Column](flutter-docs://api/widgets/Column) s in [Drawer](flutter-docs://api/material/Drawer) s and [Card](flutter-docs://api/material/Card) s.

This widget requires a [Material](flutter-docs://api/material/Material) widget ancestor in the tree to paint
itself on, which is typically provided by the app's [Scaffold](flutter-docs://api/material/Scaffold).
The [tileColor](flutter-docs://api/material/ListTile/tileColor), [selectedTileColor](flutter-docs://api/material/ListTile/selectedTileColor), [focusColor](flutter-docs://api/material/ListTile/focusColor), and [hoverColor](flutter-docs://api/material/ListTile/hoverColor) are not painted by the [ListTile](flutter-docs://api/material/ListTile) itself but by the [Material](flutter-docs://api/material/Material) widget
ancestor. In this case, one can wrap a [Material](flutter-docs://api/material/Material) widget around the [ListTile](flutter-docs://api/material/ListTile), e.g.:



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

## Performance considerations when wrapping [ListTile](flutter-docs://api/material/ListTile) with [Material](flutter-docs://api/material/Material)

Wrapping a large number of [ListTile](flutter-docs://api/material/ListTile) s individually with [Material](flutter-docs://api/material/Material) s
is expensive. Consider only wrapping the [ListTile](flutter-docs://api/material/ListTile) s that require it
or include a common [Material](flutter-docs://api/material/Material) ancestor where possible.

[ListTile](flutter-docs://api/material/ListTile) must be wrapped in a [Material](flutter-docs://api/material/Material) widget to animate [tileColor](flutter-docs://api/material/ListTile/tileColor), [selectedTileColor](flutter-docs://api/material/ListTile/selectedTileColor), [focusColor](flutter-docs://api/material/ListTile/focusColor), and [hoverColor](flutter-docs://api/material/ListTile/hoverColor) as these colors
are not drawn by the list tile itself but by the material widget ancestor.

This example showcases how [ListTile](flutter-docs://api/material/ListTile) needs to be wrapped in a [Material](flutter-docs://api/material/Material) widget to animate colors.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.2 mysample

[Omitted code: Interactive sample]

This example uses a [ListView](flutter-docs://api/widgets/ListView) to demonstrate different configurations of
[ListTile](flutter-docs://api/material/ListTile) s in [Card](flutter-docs://api/material/Card) s.



[Omitted image: Different variations of ListTile]


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.3 mysample

[Omitted code: Interactive sample]

This sample shows the creation of a [ListTile](flutter-docs://api/material/ListTile) using [ThemeData.useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) flag,
as described in: <https://m3.material.io/components/lists/overview>.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.4 mysample

[Omitted code: Interactive sample]

This sample shows [ListTile](flutter-docs://api/material/ListTile)'s [textColor](flutter-docs://api/material/ListTile/textColor) and [iconColor](flutter-docs://api/material/ListTile/iconColor) can use
[WidgetStateColor](flutter-docs://api/widgets/WidgetStateColor) color to change the color of the text and icon
when the [ListTile](flutter-docs://api/material/ListTile) is enabled, selected, or disabled.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.5 mysample

[Omitted code: Interactive sample]

This sample shows [ListTile.titleAlignment](flutter-docs://api/material/ListTile/titleAlignment) can be used to configure the
[leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) widgets alignment relative to the [title](flutter-docs://api/material/ListTile/title) and
[subtitle](flutter-docs://api/material/ListTile/subtitle) widgets.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.6 mysample

[Omitted code: Interactive sample]

To use a [ListTile](flutter-docs://api/material/ListTile) within a [Row](flutter-docs://api/widgets/Row), it needs to be wrapped in an
[Expanded](flutter-docs://api/widgets/Expanded) widget. [ListTile](flutter-docs://api/material/ListTile) requires fixed width constraints,
whereas a [Row](flutter-docs://api/widgets/Row) does not constrain its children.



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
tapped, the whole row has an ink splash effect (see [InkWell](flutter-docs://api/material/InkWell)).



```dart
ListTile(
  leading: const Icon(Icons.flight_land),
  title: const Text("Trix's airplane"),
  subtitle: _act != 2 ? const Text('The airplane is only in Act II.') : null,
  enabled: _act == 2,
  onTap: () { /* react to the tile being tapped */ }
)
```

To be accessible, tappable [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) widgets have to
be at least 48x48 in size. However, to adhere to the Material spec, [trailing](flutter-docs://api/material/ListTile/trailing) and [leading](flutter-docs://api/material/ListTile/leading) widgets in one-line ListTiles should visually be
at most 32 ([dense](flutter-docs://api/material/ListTile/dense): true) or 40 ([dense](flutter-docs://api/material/ListTile/dense): false) in height, which may
conflict with the accessibility requirement.

For this reason, a one-line ListTile allows the height of [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) widgets to be constrained by the height of the ListTile.
This allows for the creation of tappable [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) widgets
that are large enough, but it is up to the developer to ensure that
their widgets follow the Material spec.

Here is an example of a one-line, non-[dense](flutter-docs://api/material/ListTile/dense) ListTile with a
tappable leading widget that adheres to accessibility requirements and
the Material spec. To adjust the use case below for a one-line, [dense](flutter-docs://api/material/ListTile/dense) ListTile, adjust the vertical padding to 8.0.



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
combination of other widgets, such as [Row](flutter-docs://api/widgets/Row) s and [Column](flutter-docs://api/widgets/Column) s.

Here is an example of a custom list item that resembles a YouTube-related
video list item created with [Expanded](flutter-docs://api/widgets/Expanded) and [Container](flutter-docs://api/widgets/Container) widgets.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.10 mysample

[Omitted code: Interactive sample]

Here is an example of an article list item with multiline titles and
subtitles. It utilizes [Row](flutter-docs://api/widgets/Row) s and [Column](flutter-docs://api/widgets/Column) s, as well as [Expanded](flutter-docs://api/widgets/Expanded) and
[AspectRatio](flutter-docs://api/widgets/AspectRatio) widgets to organize its layout.


To create a local project with this code sample, run:  flutter create --sample=material.ListTile.11 mysample

[Omitted code: Interactive sample]

See also:

- [ListTileTheme](flutter-docs://api/material/ListTileTheme), which defines visual properties for [ListTile](flutter-docs://api/material/ListTile) s.
- [ListView](flutter-docs://api/widgets/ListView), which can display an arbitrary number of [ListTile](flutter-docs://api/material/ListTile) s
in a scrolling list.
- [CircleAvatar](flutter-docs://api/material/CircleAvatar), which shows an icon representing a person and is often
used as the [leading](flutter-docs://api/material/ListTile/leading) element of a ListTile.
- [Card](flutter-docs://api/material/Card), which can be used with [Column](flutter-docs://api/widgets/Column) to show a few [ListTile](flutter-docs://api/material/ListTile) s.
- [Divider](flutter-docs://api/material/Divider), which can be used to separate [ListTile](flutter-docs://api/material/ListTile) s.
- [ListTile.divideTiles](flutter-docs://api/material/ListTile/divideTiles), a utility for inserting [Divider](flutter-docs://api/material/Divider) s in between [ListTile](flutter-docs://api/material/ListTile) s.
- [CheckboxListTile](flutter-docs://api/material/CheckboxListTile), [RadioListTile](flutter-docs://api/material/RadioListTile), and [SwitchListTile](flutter-docs://api/material/SwitchListTile), widgets
that combine [ListTile](flutter-docs://api/material/ListTile) with other controls.
- Material 3 [ListTile](flutter-docs://api/material/ListTile) specifications are referenced from [m3.material.io/components/lists/specs](https://m3.material.io/components/lists/specs) and Material 2 [ListTile](flutter-docs://api/material/ListTile) specifications are referenced from [material.io/design/components/lists.html](https://material.io/design/components/lists.html)
- Cookbook: [Use lists](https://docs.flutter.dev/cookbook/lists/basic-list)
- Cookbook: [Implement swipe to dismiss](https://docs.flutter.dev/cookbook/gestures/dismissible)


Inheritance
- [Object](flutter-docs://api/dart-core/Object)
- [DiagnosticableTree](flutter-docs://api/foundation/DiagnosticableTree)
- [Widget](flutter-docs://api/widgets/Widget)
- [StatelessWidget](flutter-docs://api/widgets/StatelessWidget)
- ListTile

## Constructors

[ListTile](flutter-docs://api/material/ListTile/ListTile)({[Key](flutter-docs://api/foundation/Key)? key, [Widget](flutter-docs://api/widgets/Widget)? leading, [Widget](flutter-docs://api/widgets/Widget)? title, [Widget](flutter-docs://api/widgets/Widget)? subtitle, [Widget](flutter-docs://api/widgets/Widget)? trailing, [bool](flutter-docs://api/dart-core/bool)? isThreeLine, [bool](flutter-docs://api/dart-core/bool)? dense, [VisualDensity](flutter-docs://api/material/VisualDensity)? visualDensity, [ShapeBorder](flutter-docs://api/painting/ShapeBorder)? shape, [ListTileStyle](flutter-docs://api/material/ListTileStyle)? style, [Color](flutter-docs://api/dart-ui/Color)? selectedColor, [Color](flutter-docs://api/dart-ui/Color)? iconColor, [Color](flutter-docs://api/dart-ui/Color)? textColor, [TextStyle](flutter-docs://api/painting/TextStyle)? titleTextStyle, [TextStyle](flutter-docs://api/painting/TextStyle)? subtitleTextStyle, [TextStyle](flutter-docs://api/painting/TextStyle)? leadingAndTrailingTextStyle, [EdgeInsetsGeometry](flutter-docs://api/painting/EdgeInsetsGeometry)? contentPadding, [bool](flutter-docs://api/dart-core/bool) enabled = true, [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)? onTap, [GestureLongPressCallback](flutter-docs://api/gestures/GestureLongPressCallback)? onLongPress, [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>? onFocusChange, [MouseCursor](flutter-docs://api/services/MouseCursor)? mouseCursor, [bool](flutter-docs://api/dart-core/bool) selected = false, [Color](flutter-docs://api/dart-ui/Color)? focusColor, [Color](flutter-docs://api/dart-ui/Color)? hoverColor, [Color](flutter-docs://api/dart-ui/Color)? splashColor, [FocusNode](flutter-docs://api/widgets/FocusNode)? focusNode, [bool](flutter-docs://api/dart-core/bool) autofocus = false, [Color](flutter-docs://api/dart-ui/Color)? tileColor, [Color](flutter-docs://api/dart-ui/Color)? selectedTileColor, [bool](flutter-docs://api/dart-core/bool)? enableFeedback, [double](flutter-docs://api/dart-core/double)? horizontalTitleGap, [double](flutter-docs://api/dart-core/double)? minVerticalPadding, [double](flutter-docs://api/dart-core/double)? minLeadingWidth, [double](flutter-docs://api/dart-core/double)? minTileHeight, [ListTileTitleAlignment](flutter-docs://api/material/ListTileTitleAlignment)? titleAlignment, [bool](flutter-docs://api/dart-core/bool) internalAddSemanticForOnTap = true, [MaterialStatesController](flutter-docs://api/material/MaterialStatesController)? statesController})
Creates a list tile.


## Properties

[autofocus](flutter-docs://api/material/ListTile/autofocus) → [bool](flutter-docs://api/dart-core/bool)
True if this widget will be selected as the initial focus when no other
node in its scope is currently focused.


[contentPadding](flutter-docs://api/material/ListTile/contentPadding) → [EdgeInsetsGeometry](flutter-docs://api/painting/EdgeInsetsGeometry)?
The tile's internal padding.


[dense](flutter-docs://api/material/ListTile/dense) → [bool](flutter-docs://api/dart-core/bool)?
Whether this list tile is part of a vertically dense list.


[enabled](flutter-docs://api/material/ListTile/enabled) → [bool](flutter-docs://api/dart-core/bool)
Whether this list tile is interactive.


[enableFeedback](flutter-docs://api/material/ListTile/enableFeedback) → [bool](flutter-docs://api/dart-core/bool)?
Whether detected gestures should provide acoustic and/or haptic feedback.


[focusColor](flutter-docs://api/material/ListTile/focusColor) → [Color](flutter-docs://api/dart-ui/Color)?
The color for the tile's [Material](flutter-docs://api/material/Material) when it has the input focus.


[focusNode](flutter-docs://api/material/ListTile/focusNode) → [FocusNode](flutter-docs://api/widgets/FocusNode)?
An optional focus node to use as the focus node for this widget.


[hashCode](flutter-docs://api/widgets/Widget/hashCode) → [int](flutter-docs://api/dart-core/int)
The hash code for this object.


[horizontalTitleGap](flutter-docs://api/material/ListTile/horizontalTitleGap) → [double](flutter-docs://api/dart-core/double)?
The horizontal gap between the titles and the leading/trailing widgets.


[hoverColor](flutter-docs://api/material/ListTile/hoverColor) → [Color](flutter-docs://api/dart-ui/Color)?
The color for the tile's [Material](flutter-docs://api/material/Material) when a pointer is hovering over it.


[iconColor](flutter-docs://api/material/ListTile/iconColor) → [Color](flutter-docs://api/dart-ui/Color)?
Defines the default color for [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing) icons.


[internalAddSemanticForOnTap](flutter-docs://api/material/ListTile/internalAddSemanticForOnTap) → [bool](flutter-docs://api/dart-core/bool)
Whether to add button:true to the semantics if onTap is provided.
This is a temporary flag to help changing the behavior of ListTile onTap semantics.


[isThreeLine](flutter-docs://api/material/ListTile/isThreeLine) → [bool](flutter-docs://api/dart-core/bool)?
Whether this list tile is intended to display three lines of text.


[key](flutter-docs://api/widgets/Widget/key) → [Key](flutter-docs://api/foundation/Key)?
Controls how one widget replaces another widget in the tree.


[leading](flutter-docs://api/material/ListTile/leading) → [Widget](flutter-docs://api/widgets/Widget)?
A widget to display before the title.


[leadingAndTrailingTextStyle](flutter-docs://api/material/ListTile/leadingAndTrailingTextStyle) → [TextStyle](flutter-docs://api/painting/TextStyle)?
The text style for ListTile's [leading](flutter-docs://api/material/ListTile/leading) and [trailing](flutter-docs://api/material/ListTile/trailing).


[minLeadingWidth](flutter-docs://api/material/ListTile/minLeadingWidth) → [double](flutter-docs://api/dart-core/double)?
The minimum width allocated for the [ListTile.leading](flutter-docs://api/material/ListTile/leading) widget.


[minTileHeight](flutter-docs://api/material/ListTile/minTileHeight) → [double](flutter-docs://api/dart-core/double)?
The minimum height allocated for the [ListTile](flutter-docs://api/material/ListTile) widget.


[minVerticalPadding](flutter-docs://api/material/ListTile/minVerticalPadding) → [double](flutter-docs://api/dart-core/double)?
The minimum padding on the top and bottom of the title and subtitle widgets.


[mouseCursor](flutter-docs://api/material/ListTile/mouseCursor) → [MouseCursor](flutter-docs://api/services/MouseCursor)?
The cursor for a mouse pointer when it enters or is hovering over the
widget.


[onFocusChange](flutter-docs://api/material/ListTile/onFocusChange) → [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>?
Handler called when the focus changes.


[onLongPress](flutter-docs://api/material/ListTile/onLongPress) → [GestureLongPressCallback](flutter-docs://api/gestures/GestureLongPressCallback)?
Called when the user long-presses on this list tile.


[onTap](flutter-docs://api/material/ListTile/onTap) → [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)?
Called when the user taps this list tile.


[runtimeType](flutter-docs://api/dart-core/Object/runtimeType) → [Type](flutter-docs://api/dart-core/Type)
A representation of the runtime type of the object.


[selected](flutter-docs://api/material/ListTile/selected) → [bool](flutter-docs://api/dart-core/bool)
If this tile is also [enabled](flutter-docs://api/material/ListTile/enabled) then icons and text are rendered with the same color.


[selectedColor](flutter-docs://api/material/ListTile/selectedColor) → [Color](flutter-docs://api/dart-ui/Color)?
Defines the color used for icons and text when the list tile is selected.


[selectedTileColor](flutter-docs://api/material/ListTile/selectedTileColor) → [Color](flutter-docs://api/dart-ui/Color)?
Defines the background color of `ListTile` when [selected](flutter-docs://api/material/ListTile/selected) is true.


[shape](flutter-docs://api/material/ListTile/shape) → [ShapeBorder](flutter-docs://api/painting/ShapeBorder)?
Defines the tile's [InkWell.customBorder](flutter-docs://api/material/InkResponse/customBorder) and [Ink.decoration](flutter-docs://api/material/Ink/decoration) shape.


[splashColor](flutter-docs://api/material/ListTile/splashColor) → [Color](flutter-docs://api/dart-ui/Color)?
The color of splash for the tile's [Material](flutter-docs://api/material/Material).


[statesController](flutter-docs://api/material/ListTile/statesController) → [MaterialStatesController](flutter-docs://api/material/MaterialStatesController)?
Represents the interactive "state" of this widget in terms of
a set of [WidgetState](flutter-docs://api/widgets/WidgetState) s, like [WidgetState.pressed](flutter-docs://api/widgets/WidgetState) and
[WidgetState.focused](flutter-docs://api/widgets/WidgetState).


[style](flutter-docs://api/material/ListTile/style) → [ListTileStyle](flutter-docs://api/material/ListTileStyle)?
Defines the font used for the [title](flutter-docs://api/material/ListTile/title).


[subtitle](flutter-docs://api/material/ListTile/subtitle) → [Widget](flutter-docs://api/widgets/Widget)?
Additional content displayed below the title.


[subtitleTextStyle](flutter-docs://api/material/ListTile/subtitleTextStyle) → [TextStyle](flutter-docs://api/painting/TextStyle)?
The text style for ListTile's [subtitle](flutter-docs://api/material/ListTile/subtitle).


[textColor](flutter-docs://api/material/ListTile/textColor) → [Color](flutter-docs://api/dart-ui/Color)?
Defines the text color for the [title](flutter-docs://api/material/ListTile/title), [subtitle](flutter-docs://api/material/ListTile/subtitle), [leading](flutter-docs://api/material/ListTile/leading), and [trailing](flutter-docs://api/material/ListTile/trailing).


[tileColor](flutter-docs://api/material/ListTile/tileColor) → [Color](flutter-docs://api/dart-ui/Color)?
Defines the background color of `ListTile` when [selected](flutter-docs://api/material/ListTile/selected) is false.


[title](flutter-docs://api/material/ListTile/title) → [Widget](flutter-docs://api/widgets/Widget)?
The primary content of the list tile.


[titleAlignment](flutter-docs://api/material/ListTile/titleAlignment) → [ListTileTitleAlignment](flutter-docs://api/material/ListTileTitleAlignment)?
Defines how [ListTile.leading](flutter-docs://api/material/ListTile/leading) and [ListTile.trailing](flutter-docs://api/material/ListTile/trailing) are
vertically aligned relative to the [ListTile](flutter-docs://api/material/ListTile)'s titles
([ListTile.title](flutter-docs://api/material/ListTile/title) and [ListTile.subtitle](flutter-docs://api/material/ListTile/subtitle)).


[titleTextStyle](flutter-docs://api/material/ListTile/titleTextStyle) → [TextStyle](flutter-docs://api/painting/TextStyle)?
The text style for ListTile's [title](flutter-docs://api/material/ListTile/title).


[trailing](flutter-docs://api/material/ListTile/trailing) → [Widget](flutter-docs://api/widgets/Widget)?
A widget to display after the title.


[visualDensity](flutter-docs://api/material/ListTile/visualDensity) → [VisualDensity](flutter-docs://api/material/VisualDensity)?
Defines how compact the list tile's layout will be.


## Methods

[build](flutter-docs://api/material/ListTile/build)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [Widget](flutter-docs://api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[createElement](flutter-docs://api/widgets/StatelessWidget/createElement)() → [StatelessElement](flutter-docs://api/widgets/StatelessElement)
Creates a [StatelessElement](flutter-docs://api/widgets/StatelessElement) to manage this widget's location in the tree.


[debugDescribeChildren](flutter-docs://api/foundation/DiagnosticableTree/debugDescribeChildren)() → [List](flutter-docs://api/dart-core/List)<[DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)>
Returns a list of [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode) objects describing this node's
children.


[debugFillProperties](flutter-docs://api/material/ListTile/debugFillProperties)([DiagnosticPropertiesBuilder](flutter-docs://api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod)([Invocation](flutter-docs://api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[toDiagnosticsNode](flutter-docs://api/foundation/DiagnosticableTree/toDiagnosticsNode)({[String](flutter-docs://api/dart-core/String)? name, [DiagnosticsTreeStyle](flutter-docs://api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](flutter-docs://api/foundation/DiagnosticsNode/toStringDeep).


[toString](flutter-docs://api/foundation/Diagnosticable/toString)({[DiagnosticLevel](flutter-docs://api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](flutter-docs://api/dart-core/String)
A string representation of this object.


[toStringDeep](flutter-docs://api/foundation/DiagnosticableTree/toStringDeep)({[String](flutter-docs://api/dart-core/String) prefixLineOne = '', [String](flutter-docs://api/dart-core/String)? prefixOtherLines, [DiagnosticLevel](flutter-docs://api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.debug, [int](flutter-docs://api/dart-core/int) wrapWidth = 65}) → [String](flutter-docs://api/dart-core/String)
Returns a string representation of this node and its descendants.


[toStringShallow](flutter-docs://api/foundation/DiagnosticableTree/toStringShallow)({[String](flutter-docs://api/dart-core/String) joiner = ', ', [DiagnosticLevel](flutter-docs://api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.debug}) → [String](flutter-docs://api/dart-core/String)
Returns a one-line detailed description of the object.


[toStringShort](flutter-docs://api/widgets/Widget/toStringShort)() → [String](flutter-docs://api/dart-core/String)
A short, textual description of this widget.


## Operators

[operator ==](flutter-docs://api/widgets/Widget/operator_equals)([Object](flutter-docs://api/dart-core/Object) other) → [bool](flutter-docs://api/dart-core/bool)
The equality operator.


## Static Methods

[divideTiles](flutter-docs://api/material/ListTile/divideTiles)({[BuildContext](flutter-docs://api/widgets/BuildContext)? context, required [Iterable](flutter-docs://api/dart-core/Iterable)<[Widget](flutter-docs://api/widgets/Widget)> tiles, [Color](flutter-docs://api/dart-ui/Color)? color}) → [Iterable](flutter-docs://api/dart-core/Iterable)<[Widget](flutter-docs://api/widgets/Widget)>
Add a one pixel border in between each tile. If color isn't specified the
[ThemeData.dividerColor](flutter-docs://api/material/ThemeData/dividerColor) of the context's [Theme](flutter-docs://api/material/Theme) is used.