# InkWell class

A rectangular area of a [Material](flutter-docs://api/material/Material) that responds to touch.

For a variant of this widget that does not clip splashes, see [InkResponse](flutter-docs://api/material/InkResponse).

The following diagram shows how an [InkWell](flutter-docs://api/material/InkWell) looks when tapped, when using
default values.

[Omitted image: The highlight is a rectangle the size of the box.]

The [InkWell](flutter-docs://api/material/InkWell) widget must have a [Material](flutter-docs://api/material/Material) widget as an ancestor. The [Material](flutter-docs://api/material/Material) widget is where the ink reactions are actually painted. This
matches the Material Design premise wherein the [Material](flutter-docs://api/material/Material) is what is
actually reacting to touches by spreading ink.

If a Widget uses this class directly, it should include the following line
at the top of its build function to call [debugCheckHasMaterial](flutter-docs://api/material/debugCheckHasMaterial):

```dart
assert(debugCheckHasMaterial(context));

```


## Troubleshooting

### The ink splashes aren't visible!

If there is an opaque graphic, e.g. painted using a [Container](flutter-docs://api/widgets/Container), [Image](flutter-docs://api/widgets/Image), or [DecoratedBox](flutter-docs://api/widgets/DecoratedBox), between the [Material](flutter-docs://api/material/Material) widget and the [InkWell](flutter-docs://api/material/InkWell) widget, then
the splash won't be visible because it will be under the opaque graphic.
This is because ink splashes draw on the underlying [Material](flutter-docs://api/material/Material) itself, as
if the ink was spreading inside the material.

The [Ink](flutter-docs://api/material/Ink) widget can be used as a replacement for [Image](flutter-docs://api/widgets/Image), [Container](flutter-docs://api/widgets/Container), or [DecoratedBox](flutter-docs://api/widgets/DecoratedBox) to ensure that the image or decoration also paints in the [Material](flutter-docs://api/material/Material) itself, below the ink.

If this is not possible for some reason, e.g. because you are using an
opaque [CustomPaint](flutter-docs://api/widgets/CustomPaint) widget, alternatively consider using a second [Material](flutter-docs://api/material/Material) above the opaque widget but below the [InkWell](flutter-docs://api/material/InkWell) (as an
ancestor to the ink well). The [MaterialType.transparency](flutter-docs://api/material/MaterialType) material
kind can be used for this purpose.

### InkWell isn't clipping properly

If you want to clip an InkWell or any [Ink](flutter-docs://api/material/Ink) widgets you need to keep in mind
that the [Material](flutter-docs://api/material/Material) that the Ink will be printed on is responsible for clipping.
This means you can't wrap the [Ink](flutter-docs://api/material/Ink) widget in a clipping widget directly,
since this will leave the [Material](flutter-docs://api/material/Material) not clipped (and by extension the printed [Ink](flutter-docs://api/material/Ink) widgets as well).

An easy solution is to deliberately wrap the [Ink](flutter-docs://api/material/Ink) widgets you want to clip
in a [Material](flutter-docs://api/material/Material), and wrap that in a clipping widget instead. See [Ink](flutter-docs://api/material/Ink) for
an example.

### The ink splashes don't track the size of an animated container

If the size of an InkWell's [Material](flutter-docs://api/material/Material) ancestor changes while the InkWell's
splashes are expanding, you may notice that the splashes aren't clipped
correctly. This can't be avoided.

An example of this situation is as follows:

Tap the container to cause it to grow. Then, tap it again and hold before
the widget reaches its maximum size to observe the clipped ink splash.


To create a local project with this code sample, run:  flutter create --sample=material.InkWell.1 mysample

[Omitted code: Interactive sample]

An InkWell's splashes will not properly update to conform to changes if the
size of its underlying [Material](flutter-docs://api/material/Material), where the splashes are rendered, changes
during animation. You should avoid using InkWells within [Material](flutter-docs://api/material/Material) widgets
that are changing size.

See also:

- [GestureDetector](flutter-docs://api/widgets/GestureDetector), for listening for gestures without ink splashes.
- [ElevatedButton](flutter-docs://api/material/ElevatedButton) and [TextButton](flutter-docs://api/material/TextButton), two kinds of buttons in Material Design.
- [InkResponse](flutter-docs://api/material/InkResponse), a variant of [InkWell](flutter-docs://api/material/InkWell) that doesn't force a rectangular
shape on the ink reaction.


Inheritance
- [Object](flutter-docs://api/dart-core/Object)
- [DiagnosticableTree](flutter-docs://api/foundation/DiagnosticableTree)
- [Widget](flutter-docs://api/widgets/Widget)
- [StatelessWidget](flutter-docs://api/widgets/StatelessWidget)
- [InkResponse](flutter-docs://api/material/InkResponse)
- InkWell

## Constructors

[InkWell](flutter-docs://api/material/InkWell/InkWell)({[Key](flutter-docs://api/foundation/Key)? key, [Widget](flutter-docs://api/widgets/Widget)? child, [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)? onTap, [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)? onDoubleTap, [GestureLongPressCallback](flutter-docs://api/gestures/GestureLongPressCallback)? onLongPress, [GestureLongPressUpCallback](flutter-docs://api/gestures/GestureLongPressUpCallback)? onLongPressUp, [GestureTapDownCallback](flutter-docs://api/gestures/GestureTapDownCallback)? onTapDown, [GestureTapUpCallback](flutter-docs://api/gestures/GestureTapUpCallback)? onTapUp, [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)? onTapCancel, [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)? onSecondaryTap, [GestureTapUpCallback](flutter-docs://api/gestures/GestureTapUpCallback)? onSecondaryTapUp, [GestureTapDownCallback](flutter-docs://api/gestures/GestureTapDownCallback)? onSecondaryTapDown, [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)? onSecondaryTapCancel, [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>? onHighlightChanged, [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>? onHover, [MouseCursor](flutter-docs://api/services/MouseCursor)? mouseCursor, [Color](flutter-docs://api/dart-ui/Color)? focusColor, [Color](flutter-docs://api/dart-ui/Color)? hoverColor, [Color](flutter-docs://api/dart-ui/Color)? highlightColor, [WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty)<[Color](flutter-docs://api/dart-ui/Color)?>? overlayColor, [Color](flutter-docs://api/dart-ui/Color)? splashColor, [InteractiveInkFeatureFactory](flutter-docs://api/material/InteractiveInkFeatureFactory)? splashFactory, [double](flutter-docs://api/dart-core/double)? radius, [BorderRadius](flutter-docs://api/painting/BorderRadius)? borderRadius, [ShapeBorder](flutter-docs://api/painting/ShapeBorder)? customBorder, [bool](flutter-docs://api/dart-core/bool) enableFeedback = true, [bool](flutter-docs://api/dart-core/bool) excludeFromSemantics = false, [FocusNode](flutter-docs://api/widgets/FocusNode)? focusNode, [bool](flutter-docs://api/dart-core/bool) canRequestFocus = true, [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>? onFocusChange, [bool](flutter-docs://api/dart-core/bool) autofocus = false, [MaterialStatesController](flutter-docs://api/material/MaterialStatesController)? statesController, [Duration](flutter-docs://api/dart-core/Duration)? hoverDuration})
Creates an ink well.


## Properties

[autofocus](flutter-docs://api/material/InkResponse/autofocus) → [bool](flutter-docs://api/dart-core/bool)
True if this widget will be selected as the initial focus when no other
node in its scope is currently focused.


[borderRadius](flutter-docs://api/material/InkResponse/borderRadius) → [BorderRadius](flutter-docs://api/painting/BorderRadius)?
The border radius of the containing rectangle. This is effective only if
[highlightShape](flutter-docs://api/material/InkResponse/highlightShape) is [BoxShape.rectangle](flutter-docs://api/painting/BoxShape).


[canRequestFocus](flutter-docs://api/material/InkResponse/canRequestFocus) → [bool](flutter-docs://api/dart-core/bool)
If true, this widget may request the primary focus.


[child](flutter-docs://api/material/InkResponse/child) → [Widget](flutter-docs://api/widgets/Widget)?
The widget below this widget in the tree.


[containedInkWell](flutter-docs://api/material/InkResponse/containedInkWell) → [bool](flutter-docs://api/dart-core/bool)
Whether this ink response should be clipped its bounds.


[customBorder](flutter-docs://api/material/InkResponse/customBorder) → [ShapeBorder](flutter-docs://api/painting/ShapeBorder)?
The custom clip border.


[enableFeedback](flutter-docs://api/material/InkResponse/enableFeedback) → [bool](flutter-docs://api/dart-core/bool)
Whether detected gestures should provide acoustic and/or haptic feedback.


[excludeFromSemantics](flutter-docs://api/material/InkResponse/excludeFromSemantics) → [bool](flutter-docs://api/dart-core/bool)
Whether to exclude the gestures introduced by this widget from the
semantics tree.


[focusColor](flutter-docs://api/material/InkResponse/focusColor) → [Color](flutter-docs://api/dart-ui/Color)?
The color of the ink response when the parent widget is focused. If this
property is null then the focus color of the theme,
[ThemeData.focusColor](flutter-docs://api/material/ThemeData/focusColor), will be used.


[focusNode](flutter-docs://api/material/InkResponse/focusNode) → [FocusNode](flutter-docs://api/widgets/FocusNode)?
An optional focus node to use as the focus node for this widget.


[hashCode](flutter-docs://api/widgets/Widget/hashCode) → [int](flutter-docs://api/dart-core/int)
The hash code for this object.


[highlightColor](flutter-docs://api/material/InkResponse/highlightColor) → [Color](flutter-docs://api/dart-ui/Color)?
The highlight color of the ink response when pressed. If this property is
null then the highlight color of the theme, [ThemeData.highlightColor](flutter-docs://api/material/ThemeData/highlightColor),
will be used.


[highlightShape](flutter-docs://api/material/InkResponse/highlightShape) → [BoxShape](flutter-docs://api/painting/BoxShape)
The shape (e.g., circle, rectangle) to use for the highlight drawn around
this part of the material when pressed, hovered over, or focused.


[hoverColor](flutter-docs://api/material/InkResponse/hoverColor) → [Color](flutter-docs://api/dart-ui/Color)?
The color of the ink response when a pointer is hovering over it. If this
property is null then the hover color of the theme,
[ThemeData.hoverColor](flutter-docs://api/material/ThemeData/hoverColor), will be used.


[hoverDuration](flutter-docs://api/material/InkResponse/hoverDuration) → [Duration](flutter-docs://api/dart-core/Duration)?
The duration of the animation that animates the hover effect.


[key](flutter-docs://api/widgets/Widget/key) → [Key](flutter-docs://api/foundation/Key)?
Controls how one widget replaces another widget in the tree.


[mouseCursor](flutter-docs://api/material/InkResponse/mouseCursor) → [MouseCursor](flutter-docs://api/services/MouseCursor)?
The cursor for a mouse pointer when it enters or is hovering over the
widget.


[onDoubleTap](flutter-docs://api/material/InkResponse/onDoubleTap) → [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)?
Called when the user double taps this part of the material.


[onFocusChange](flutter-docs://api/material/InkResponse/onFocusChange) → [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>?
Handler called when the focus changes.


[onHighlightChanged](flutter-docs://api/material/InkResponse/onHighlightChanged) → [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>?
Called when this part of the material either becomes highlighted or stops
being highlighted.


[onHover](flutter-docs://api/material/InkResponse/onHover) → [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>?
Called when a pointer enters or exits the ink response area.


[onLongPress](flutter-docs://api/material/InkResponse/onLongPress) → [GestureLongPressCallback](flutter-docs://api/gestures/GestureLongPressCallback)?
Called when the user long-presses on this part of the material.


[onLongPressUp](flutter-docs://api/material/InkResponse/onLongPressUp) → [GestureLongPressUpCallback](flutter-docs://api/gestures/GestureLongPressUpCallback)?
Called when the user lifts their finger after a long press on the button.


[onSecondaryTap](flutter-docs://api/material/InkResponse/onSecondaryTap) → [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)?
Called when the user taps this part of the material with a secondary button.


[onSecondaryTapCancel](flutter-docs://api/material/InkResponse/onSecondaryTapCancel) → [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)?
Called when the user cancels a secondary button tap that was started on
this part of the material.


[onSecondaryTapDown](flutter-docs://api/material/InkResponse/onSecondaryTapDown) → [GestureTapDownCallback](flutter-docs://api/gestures/GestureTapDownCallback)?
Called when the user taps down on this part of the material with a
secondary button.


[onSecondaryTapUp](flutter-docs://api/material/InkResponse/onSecondaryTapUp) → [GestureTapUpCallback](flutter-docs://api/gestures/GestureTapUpCallback)?
Called when the user releases a secondary button tap that was started on
this part of the material. [onSecondaryTap](flutter-docs://api/material/InkResponse/onSecondaryTap) is called immediately after.


[onTap](flutter-docs://api/material/InkResponse/onTap) → [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)?
Called when the user taps this part of the material.


[onTapCancel](flutter-docs://api/material/InkResponse/onTapCancel) → [GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback)?
Called when the user cancels a tap that was started on this part of the
material.


[onTapDown](flutter-docs://api/material/InkResponse/onTapDown) → [GestureTapDownCallback](flutter-docs://api/gestures/GestureTapDownCallback)?
Called when the user taps down this part of the material.


[onTapUp](flutter-docs://api/material/InkResponse/onTapUp) → [GestureTapUpCallback](flutter-docs://api/gestures/GestureTapUpCallback)?
Called when the user releases a tap that was started on this part of the
material. [onTap](flutter-docs://api/material/InkResponse/onTap) is called immediately after.


[overlayColor](flutter-docs://api/material/InkResponse/overlayColor) → [WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty)<[Color](flutter-docs://api/dart-ui/Color)?>?
Defines the ink response focus, hover, and splash colors.


[radius](flutter-docs://api/material/InkResponse/radius) → [double](flutter-docs://api/dart-core/double)?
The radius of the ink splash.


[runtimeType](flutter-docs://api/dart-core/Object/runtimeType) → [Type](flutter-docs://api/dart-core/Type)
A representation of the runtime type of the object.


[splashColor](flutter-docs://api/material/InkResponse/splashColor) → [Color](flutter-docs://api/dart-ui/Color)?
The splash color of the ink response. If this property is null then the
splash color of the theme, [ThemeData.splashColor](flutter-docs://api/material/ThemeData/splashColor), will be used.


[splashFactory](flutter-docs://api/material/InkResponse/splashFactory) → [InteractiveInkFeatureFactory](flutter-docs://api/material/InteractiveInkFeatureFactory)?
Defines the appearance of the splash.


[statesController](flutter-docs://api/material/InkResponse/statesController) → [MaterialStatesController](flutter-docs://api/material/MaterialStatesController)?
Represents the interactive "state" of this widget in terms of
a set of [WidgetState](flutter-docs://api/widgets/WidgetState) s, like [WidgetState.pressed](flutter-docs://api/widgets/WidgetState) and
[WidgetState.focused](flutter-docs://api/widgets/WidgetState).


## Methods

[build](flutter-docs://api/material/InkResponse/build)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [Widget](flutter-docs://api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[createElement](flutter-docs://api/widgets/StatelessWidget/createElement)() → [StatelessElement](flutter-docs://api/widgets/StatelessElement)
Creates a [StatelessElement](flutter-docs://api/widgets/StatelessElement) to manage this widget's location in the tree.


[debugCheckContext](flutter-docs://api/material/InkResponse/debugCheckContext)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context satisfies the prerequisites for
this class.


[debugDescribeChildren](flutter-docs://api/foundation/DiagnosticableTree/debugDescribeChildren)() → [List](flutter-docs://api/dart-core/List)<[DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)>
Returns a list of [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode) objects describing this node's
children.


[debugFillProperties](flutter-docs://api/widgets/Widget/debugFillProperties)([DiagnosticPropertiesBuilder](flutter-docs://api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[getRectCallback](flutter-docs://api/material/InkResponse/getRectCallback)([RenderBox](flutter-docs://api/rendering/RenderBox) referenceBox) → [RectCallback](flutter-docs://api/material/RectCallback)?
The rectangle to use for the highlight effect and for clipping
the splash effects if [containedInkWell](flutter-docs://api/material/InkResponse/containedInkWell) is true.


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
