# InkWell class

A rectangular area of a [Material](mcp://flutter/api/material/Material) that responds to touch.

For a variant of this widget that does not clip splashes, see [InkResponse](mcp://flutter/api/material/InkResponse).

The following diagram shows how an [InkWell](mcp://flutter/api/material/InkWell) looks when tapped, when using
default values.

[Omitted image: The highlight is a rectangle the size of the box.]

The [InkWell](mcp://flutter/api/material/InkWell) widget must have a [Material](mcp://flutter/api/material/Material) widget as an ancestor. The [Material](mcp://flutter/api/material/Material) widget is where the ink reactions are actually painted. This
matches the Material Design premise wherein the [Material](mcp://flutter/api/material/Material) is what is
actually reacting to touches by spreading ink.

If a Widget uses this class directly, it should include the following line
at the top of its build function to call [debugCheckHasMaterial](mcp://flutter/api/material/debugCheckHasMaterial):

```dart
assert(debugCheckHasMaterial(context));

```


## Troubleshooting

### The ink splashes aren't visible!

If there is an opaque graphic, e.g. painted using a [Container](mcp://flutter/api/widgets/Container), [Image](mcp://flutter/api/widgets/Image), or [DecoratedBox](mcp://flutter/api/widgets/DecoratedBox), between the [Material](mcp://flutter/api/material/Material) widget and the [InkWell](mcp://flutter/api/material/InkWell) widget, then
the splash won't be visible because it will be under the opaque graphic.
This is because ink splashes draw on the underlying [Material](mcp://flutter/api/material/Material) itself, as
if the ink was spreading inside the material.

The [Ink](mcp://flutter/api/material/Ink) widget can be used as a replacement for [Image](mcp://flutter/api/widgets/Image), [Container](mcp://flutter/api/widgets/Container), or [DecoratedBox](mcp://flutter/api/widgets/DecoratedBox) to ensure that the image or decoration also paints in the [Material](mcp://flutter/api/material/Material) itself, below the ink.

If this is not possible for some reason, e.g. because you are using an
opaque [CustomPaint](mcp://flutter/api/widgets/CustomPaint) widget, alternatively consider using a second [Material](mcp://flutter/api/material/Material) above the opaque widget but below the [InkWell](mcp://flutter/api/material/InkWell) (as an
ancestor to the ink well). The [MaterialType.transparency](mcp://flutter/api/material/MaterialType) material
kind can be used for this purpose.

### InkWell isn't clipping properly

If you want to clip an InkWell or any [Ink](mcp://flutter/api/material/Ink) widgets you need to keep in mind
that the [Material](mcp://flutter/api/material/Material) that the Ink will be printed on is responsible for clipping.
This means you can't wrap the [Ink](mcp://flutter/api/material/Ink) widget in a clipping widget directly,
since this will leave the [Material](mcp://flutter/api/material/Material) not clipped (and by extension the printed [Ink](mcp://flutter/api/material/Ink) widgets as well).

An easy solution is to deliberately wrap the [Ink](mcp://flutter/api/material/Ink) widgets you want to clip
in a [Material](mcp://flutter/api/material/Material), and wrap that in a clipping widget instead. See [Ink](mcp://flutter/api/material/Ink) for
an example.

### The ink splashes don't track the size of an animated container

If the size of an InkWell's [Material](mcp://flutter/api/material/Material) ancestor changes while the InkWell's
splashes are expanding, you may notice that the splashes aren't clipped
correctly. This can't be avoided.

An example of this situation is as follows:

Tap the container to cause it to grow. Then, tap it again and hold before
the widget reaches its maximum size to observe the clipped ink splash.


To create a local project with this code sample, run:  flutter create --sample=material.InkWell.1 mysample

[Omitted code: Interactive sample]

An InkWell's splashes will not properly update to conform to changes if the
size of its underlying [Material](mcp://flutter/api/material/Material), where the splashes are rendered, changes
during animation. You should avoid using InkWells within [Material](mcp://flutter/api/material/Material) widgets
that are changing size.

See also:

- [GestureDetector](mcp://flutter/api/widgets/GestureDetector), for listening for gestures without ink splashes.
- [ElevatedButton](mcp://flutter/api/material/ElevatedButton) and [TextButton](mcp://flutter/api/material/TextButton), two kinds of buttons in Material Design.
- [InkResponse](mcp://flutter/api/material/InkResponse), a variant of [InkWell](mcp://flutter/api/material/InkWell) that doesn't force a rectangular
shape on the ink reaction.


Inheritance
- [Object](mcp://flutter/api/dart-core/Object)
- [DiagnosticableTree](mcp://flutter/api/foundation/DiagnosticableTree)
- [Widget](mcp://flutter/api/widgets/Widget)
- [StatelessWidget](mcp://flutter/api/widgets/StatelessWidget)
- [InkResponse](mcp://flutter/api/material/InkResponse)
- InkWell

## Constructors

[InkWell](mcp://flutter/api/material/InkWell/InkWell)({[Key](mcp://flutter/api/foundation/Key)? key, [Widget](mcp://flutter/api/widgets/Widget)? child, [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)? onTap, [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)? onDoubleTap, [GestureLongPressCallback](mcp://flutter/api/gestures/GestureLongPressCallback)? onLongPress, [GestureLongPressUpCallback](mcp://flutter/api/gestures/GestureLongPressUpCallback)? onLongPressUp, [GestureTapDownCallback](mcp://flutter/api/gestures/GestureTapDownCallback)? onTapDown, [GestureTapUpCallback](mcp://flutter/api/gestures/GestureTapUpCallback)? onTapUp, [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)? onTapCancel, [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)? onSecondaryTap, [GestureTapUpCallback](mcp://flutter/api/gestures/GestureTapUpCallback)? onSecondaryTapUp, [GestureTapDownCallback](mcp://flutter/api/gestures/GestureTapDownCallback)? onSecondaryTapDown, [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)? onSecondaryTapCancel, [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>? onHighlightChanged, [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>? onHover, [MouseCursor](mcp://flutter/api/services/MouseCursor)? mouseCursor, [Color](mcp://flutter/api/dart-ui/Color)? focusColor, [Color](mcp://flutter/api/dart-ui/Color)? hoverColor, [Color](mcp://flutter/api/dart-ui/Color)? highlightColor, [WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty)<[Color](mcp://flutter/api/dart-ui/Color)?>? overlayColor, [Color](mcp://flutter/api/dart-ui/Color)? splashColor, [InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)? splashFactory, [double](mcp://flutter/api/dart-core/double)? radius, [BorderRadius](mcp://flutter/api/painting/BorderRadius)? borderRadius, [ShapeBorder](mcp://flutter/api/painting/ShapeBorder)? customBorder, [bool](mcp://flutter/api/dart-core/bool) enableFeedback = true, [bool](mcp://flutter/api/dart-core/bool) excludeFromSemantics = false, [FocusNode](mcp://flutter/api/widgets/FocusNode)? focusNode, [bool](mcp://flutter/api/dart-core/bool) canRequestFocus = true, [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>? onFocusChange, [bool](mcp://flutter/api/dart-core/bool) autofocus = false, [MaterialStatesController](mcp://flutter/api/material/MaterialStatesController)? statesController, [Duration](mcp://flutter/api/dart-core/Duration)? hoverDuration})
Creates an ink well.


## Properties

[autofocus](mcp://flutter/api/material/InkResponse/autofocus) → [bool](mcp://flutter/api/dart-core/bool)
True if this widget will be selected as the initial focus when no other
node in its scope is currently focused.


[borderRadius](mcp://flutter/api/material/InkResponse/borderRadius) → [BorderRadius](mcp://flutter/api/painting/BorderRadius)?
The border radius of the containing rectangle. This is effective only if
[highlightShape](mcp://flutter/api/material/InkResponse/highlightShape) is [BoxShape.rectangle](mcp://flutter/api/painting/BoxShape).


[canRequestFocus](mcp://flutter/api/material/InkResponse/canRequestFocus) → [bool](mcp://flutter/api/dart-core/bool)
If true, this widget may request the primary focus.


[child](mcp://flutter/api/material/InkResponse/child) → [Widget](mcp://flutter/api/widgets/Widget)?
The widget below this widget in the tree.


[containedInkWell](mcp://flutter/api/material/InkResponse/containedInkWell) → [bool](mcp://flutter/api/dart-core/bool)
Whether this ink response should be clipped its bounds.


[customBorder](mcp://flutter/api/material/InkResponse/customBorder) → [ShapeBorder](mcp://flutter/api/painting/ShapeBorder)?
The custom clip border.


[enableFeedback](mcp://flutter/api/material/InkResponse/enableFeedback) → [bool](mcp://flutter/api/dart-core/bool)
Whether detected gestures should provide acoustic and/or haptic feedback.


[excludeFromSemantics](mcp://flutter/api/material/InkResponse/excludeFromSemantics) → [bool](mcp://flutter/api/dart-core/bool)
Whether to exclude the gestures introduced by this widget from the
semantics tree.


[focusColor](mcp://flutter/api/material/InkResponse/focusColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The color of the ink response when the parent widget is focused. If this
property is null then the focus color of the theme,
[ThemeData.focusColor](mcp://flutter/api/material/ThemeData/focusColor), will be used.


[focusNode](mcp://flutter/api/material/InkResponse/focusNode) → [FocusNode](mcp://flutter/api/widgets/FocusNode)?
An optional focus node to use as the focus node for this widget.


[hashCode](mcp://flutter/api/widgets/Widget/hashCode) → [int](mcp://flutter/api/dart-core/int)
The hash code for this object.


[highlightColor](mcp://flutter/api/material/InkResponse/highlightColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The highlight color of the ink response when pressed. If this property is
null then the highlight color of the theme, [ThemeData.highlightColor](mcp://flutter/api/material/ThemeData/highlightColor),
will be used.


[highlightShape](mcp://flutter/api/material/InkResponse/highlightShape) → [BoxShape](mcp://flutter/api/painting/BoxShape)
The shape (e.g., circle, rectangle) to use for the highlight drawn around
this part of the material when pressed, hovered over, or focused.


[hoverColor](mcp://flutter/api/material/InkResponse/hoverColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The color of the ink response when a pointer is hovering over it. If this
property is null then the hover color of the theme,
[ThemeData.hoverColor](mcp://flutter/api/material/ThemeData/hoverColor), will be used.


[hoverDuration](mcp://flutter/api/material/InkResponse/hoverDuration) → [Duration](mcp://flutter/api/dart-core/Duration)?
The duration of the animation that animates the hover effect.


[key](mcp://flutter/api/widgets/Widget/key) → [Key](mcp://flutter/api/foundation/Key)?
Controls how one widget replaces another widget in the tree.


[mouseCursor](mcp://flutter/api/material/InkResponse/mouseCursor) → [MouseCursor](mcp://flutter/api/services/MouseCursor)?
The cursor for a mouse pointer when it enters or is hovering over the
widget.


[onDoubleTap](mcp://flutter/api/material/InkResponse/onDoubleTap) → [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)?
Called when the user double taps this part of the material.


[onFocusChange](mcp://flutter/api/material/InkResponse/onFocusChange) → [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>?
Handler called when the focus changes.


[onHighlightChanged](mcp://flutter/api/material/InkResponse/onHighlightChanged) → [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>?
Called when this part of the material either becomes highlighted or stops
being highlighted.


[onHover](mcp://flutter/api/material/InkResponse/onHover) → [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>?
Called when a pointer enters or exits the ink response area.


[onLongPress](mcp://flutter/api/material/InkResponse/onLongPress) → [GestureLongPressCallback](mcp://flutter/api/gestures/GestureLongPressCallback)?
Called when the user long-presses on this part of the material.


[onLongPressUp](mcp://flutter/api/material/InkResponse/onLongPressUp) → [GestureLongPressUpCallback](mcp://flutter/api/gestures/GestureLongPressUpCallback)?
Called when the user lifts their finger after a long press on the button.


[onSecondaryTap](mcp://flutter/api/material/InkResponse/onSecondaryTap) → [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)?
Called when the user taps this part of the material with a secondary button.


[onSecondaryTapCancel](mcp://flutter/api/material/InkResponse/onSecondaryTapCancel) → [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)?
Called when the user cancels a secondary button tap that was started on
this part of the material.


[onSecondaryTapDown](mcp://flutter/api/material/InkResponse/onSecondaryTapDown) → [GestureTapDownCallback](mcp://flutter/api/gestures/GestureTapDownCallback)?
Called when the user taps down on this part of the material with a
secondary button.


[onSecondaryTapUp](mcp://flutter/api/material/InkResponse/onSecondaryTapUp) → [GestureTapUpCallback](mcp://flutter/api/gestures/GestureTapUpCallback)?
Called when the user releases a secondary button tap that was started on
this part of the material. [onSecondaryTap](mcp://flutter/api/material/InkResponse/onSecondaryTap) is called immediately after.


[onTap](mcp://flutter/api/material/InkResponse/onTap) → [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)?
Called when the user taps this part of the material.


[onTapCancel](mcp://flutter/api/material/InkResponse/onTapCancel) → [GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)?
Called when the user cancels a tap that was started on this part of the
material.


[onTapDown](mcp://flutter/api/material/InkResponse/onTapDown) → [GestureTapDownCallback](mcp://flutter/api/gestures/GestureTapDownCallback)?
Called when the user taps down this part of the material.


[onTapUp](mcp://flutter/api/material/InkResponse/onTapUp) → [GestureTapUpCallback](mcp://flutter/api/gestures/GestureTapUpCallback)?
Called when the user releases a tap that was started on this part of the
material. [onTap](mcp://flutter/api/material/InkResponse/onTap) is called immediately after.


[overlayColor](mcp://flutter/api/material/InkResponse/overlayColor) → [WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty)<[Color](mcp://flutter/api/dart-ui/Color)?>?
Defines the ink response focus, hover, and splash colors.


[radius](mcp://flutter/api/material/InkResponse/radius) → [double](mcp://flutter/api/dart-core/double)?
The radius of the ink splash.


[runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) → [Type](mcp://flutter/api/dart-core/Type)
A representation of the runtime type of the object.


[splashColor](mcp://flutter/api/material/InkResponse/splashColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The splash color of the ink response. If this property is null then the
splash color of the theme, [ThemeData.splashColor](mcp://flutter/api/material/ThemeData/splashColor), will be used.


[splashFactory](mcp://flutter/api/material/InkResponse/splashFactory) → [InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)?
Defines the appearance of the splash.


[statesController](mcp://flutter/api/material/InkResponse/statesController) → [MaterialStatesController](mcp://flutter/api/material/MaterialStatesController)?
Represents the interactive "state" of this widget in terms of
a set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s, like [WidgetState.pressed](mcp://flutter/api/widgets/WidgetState) and
[WidgetState.focused](mcp://flutter/api/widgets/WidgetState).


## Methods

[build](mcp://flutter/api/material/InkResponse/build)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [Widget](mcp://flutter/api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[createElement](mcp://flutter/api/widgets/StatelessWidget/createElement)() → [StatelessElement](mcp://flutter/api/widgets/StatelessElement)
Creates a [StatelessElement](mcp://flutter/api/widgets/StatelessElement) to manage this widget's location in the tree.


[debugCheckContext](mcp://flutter/api/material/InkResponse/debugCheckContext)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [bool](mcp://flutter/api/dart-core/bool)
Asserts that the given context satisfies the prerequisites for
this class.


[debugDescribeChildren](mcp://flutter/api/foundation/DiagnosticableTree/debugDescribeChildren)() → [List](mcp://flutter/api/dart-core/List)<[DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)>
Returns a list of [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode) objects describing this node's
children.


[debugFillProperties](mcp://flutter/api/widgets/Widget/debugFillProperties)([DiagnosticPropertiesBuilder](mcp://flutter/api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[getRectCallback](mcp://flutter/api/material/InkResponse/getRectCallback)([RenderBox](mcp://flutter/api/rendering/RenderBox) referenceBox) → [RectCallback](mcp://flutter/api/material/RectCallback)?
The rectangle to use for the highlight effect and for clipping
the splash effects if [containedInkWell](mcp://flutter/api/material/InkResponse/containedInkWell) is true.


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
