# Text class

A run of text with a single style.

The [Text](mcp://flutter/api/widgets/Text) widget displays a string of text with single style. The string
might break across multiple lines or might all be displayed on the same line
depending on the layout constraints.

The [style](mcp://flutter/api/widgets/Text/style) argument is optional. When omitted, the text will use the style
from the closest enclosing [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle). If the given style's [TextStyle.inherit](mcp://flutter/api/painting/TextStyle/inherit) property is true (the default), the given style will
be merged with the closest enclosing [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle). This merging
behavior is useful, for example, to make the text bold while using the
default font family and size.

This example shows how to display text using the [Text](mcp://flutter/api/widgets/Text) widget with the
[overflow](mcp://flutter/api/widgets/Text/overflow) set to [TextOverflow.ellipsis](mcp://flutter/api/painting/TextOverflow).



[Omitted image: If the text overflows, the Text widget displays an ellipsis to trim the overflowing text]



```dart
Container(
  width: 100,
  decoration: BoxDecoration(border: Border.all()),
  child: const Text(
    'Hello, how are you?',
    overflow: TextOverflow.ellipsis,
  ),
)
```

Setting [maxLines](mcp://flutter/api/widgets/Text/maxLines) to `1` is not equivalent to disabling soft wrapping with
[softWrap](mcp://flutter/api/widgets/Text/softWrap). This is apparent when using [TextOverflow.fade](mcp://flutter/api/painting/TextOverflow) as the following
examples show.



[Omitted image: If a second line overflows the Text widget displays a horizontal fade]

Here soft wrapping is enabled and the [Text](mcp://flutter/api/widgets/Text) widget tries to wrap the words
"how are you?" to a second line. This is prevented by the [maxLines](mcp://flutter/api/widgets/Text/maxLines) value
of `1`. The result is that a second line overflows and the fade appears in a
horizontal direction at the bottom.

[Omitted image: If a single line overflows the Text widget displays a horizontal fade]

Here soft wrapping is disabled with `softWrap: false` and the [Text](mcp://flutter/api/widgets/Text) widget
attempts to display its text in a single unbroken line. The result is that
the single line overflows and the fade appears in a vertical direction at
the right.



```dart
const Text(
  'Hello, how are you?',
  overflow: TextOverflow.fade,
  maxLines: 1,
)

// ...

const Text(
  'Hello, how are you?',
  overflow: TextOverflow.fade,
  softWrap: false,
)
```

Using the [Text.rich](mcp://flutter/api/widgets/Text/Text.rich) constructor, the [Text](mcp://flutter/api/widgets/Text) widget can
display a paragraph with differently styled [TextSpan](mcp://flutter/api/painting/TextSpan) s. The sample
that follows displays "Hello beautiful world" with different styles
for each word.

[Omitted image: The word &quot;Hello&quot; is shown with the default text styles. The word &quot;beautiful&quot; is italicized. The word &quot;world&quot; is bold.]



```dart
const Text.rich(
  TextSpan(
    text: 'Hello', // default text style
    children: <TextSpan>[
      TextSpan(text: ' beautiful ', style: TextStyle(fontStyle: FontStyle.italic)),
      TextSpan(text: 'world', style: TextStyle(fontWeight: FontWeight.bold)),
    ],
  ),
)
```

## Interactivity

To make [Text](mcp://flutter/api/widgets/Text) react to touch events, wrap it in a [GestureDetector](mcp://flutter/api/widgets/GestureDetector) widget
with a [GestureDetector.onTap](mcp://flutter/api/widgets/GestureDetector/onTap) handler.

In a Material Design application, consider using a [TextButton](mcp://flutter/api/material/TextButton) instead, or
if that isn't appropriate, at least using an [InkWell](mcp://flutter/api/material/InkWell) instead of [GestureDetector](mcp://flutter/api/widgets/GestureDetector).

To make sections of the text interactive, use [RichText](mcp://flutter/api/widgets/RichText) and specify a [TapGestureRecognizer](mcp://flutter/api/gestures/TapGestureRecognizer) as the [TextSpan.recognizer](mcp://flutter/api/painting/TextSpan/recognizer) of the relevant part of
the text.

## Selection

[Text](mcp://flutter/api/widgets/Text) is not selectable by default. To make a [Text](mcp://flutter/api/widgets/Text) selectable, one can
wrap a subtree with a [SelectionArea](mcp://flutter/api/material/SelectionArea) widget. To exclude a part of a subtree
under [SelectionArea](mcp://flutter/api/material/SelectionArea) from selection, once can also wrap that part of the
subtree with [SelectionContainer.disabled](mcp://flutter/api/widgets/SelectionContainer/SelectionContainer.disabled).

This sample demonstrates how to disable selection for a Text under a
SelectionArea.


To create a local project with this code sample, run:  flutter create --sample=widgets.Text.4 mysample

[Omitted code: Interactive sample]

See also:

- [RichText](mcp://flutter/api/widgets/RichText), which gives you more control over the text styles.
- [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle), which sets default styles for [Text](mcp://flutter/api/widgets/Text) widgets.
- [SelectableRegion](mcp://flutter/api/widgets/SelectableRegion), which provides an overview of the selection system.


Inheritance
- [Object](mcp://flutter/api/dart-core/Object)
- [DiagnosticableTree](mcp://flutter/api/foundation/DiagnosticableTree)
- [Widget](mcp://flutter/api/widgets/Widget)
- [StatelessWidget](mcp://flutter/api/widgets/StatelessWidget)
- Text

## Constructors

[Text](mcp://flutter/api/widgets/Text/Text)([String](mcp://flutter/api/dart-core/String) data, {[Key](mcp://flutter/api/foundation/Key)? key, [TextStyle](mcp://flutter/api/painting/TextStyle)? style, [StrutStyle](mcp://flutter/api/painting/StrutStyle)? strutStyle, [TextAlign](mcp://flutter/api/dart-ui/TextAlign)? textAlign, [TextDirection](mcp://flutter/api/dart-ui/TextDirection)? textDirection, [Locale](mcp://flutter/api/dart-ui/Locale)? locale, [bool](mcp://flutter/api/dart-core/bool)? softWrap, [TextOverflow](mcp://flutter/api/painting/TextOverflow)? overflow, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.') [double](mcp://flutter/api/dart-core/double)? textScaleFactor, [TextScaler](mcp://flutter/api/painting/TextScaler)? textScaler, [int](mcp://flutter/api/dart-core/int)? maxLines, [String](mcp://flutter/api/dart-core/String)? semanticsLabel, [String](mcp://flutter/api/dart-core/String)? semanticsIdentifier, [TextWidthBasis](mcp://flutter/api/painting/TextWidthBasis)? textWidthBasis, [TextHeightBehavior](mcp://flutter/api/dart-ui/TextHeightBehavior)? textHeightBehavior, [Color](mcp://flutter/api/dart-ui/Color)? selectionColor})
Creates a text widget.


[Text.rich](mcp://flutter/api/widgets/Text/Text.rich)([InlineSpan](mcp://flutter/api/painting/InlineSpan) textSpan, {[Key](mcp://flutter/api/foundation/Key)? key, [TextStyle](mcp://flutter/api/painting/TextStyle)? style, [StrutStyle](mcp://flutter/api/painting/StrutStyle)? strutStyle, [TextAlign](mcp://flutter/api/dart-ui/TextAlign)? textAlign, [TextDirection](mcp://flutter/api/dart-ui/TextDirection)? textDirection, [Locale](mcp://flutter/api/dart-ui/Locale)? locale, [bool](mcp://flutter/api/dart-core/bool)? softWrap, [TextOverflow](mcp://flutter/api/painting/TextOverflow)? overflow, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.') [double](mcp://flutter/api/dart-core/double)? textScaleFactor, [TextScaler](mcp://flutter/api/painting/TextScaler)? textScaler, [int](mcp://flutter/api/dart-core/int)? maxLines, [String](mcp://flutter/api/dart-core/String)? semanticsLabel, [String](mcp://flutter/api/dart-core/String)? semanticsIdentifier, [TextWidthBasis](mcp://flutter/api/painting/TextWidthBasis)? textWidthBasis, [TextHeightBehavior](mcp://flutter/api/dart-ui/TextHeightBehavior)? textHeightBehavior, [Color](mcp://flutter/api/dart-ui/Color)? selectionColor})
Creates a text widget with a [InlineSpan](mcp://flutter/api/painting/InlineSpan).


## Properties

[data](mcp://flutter/api/widgets/Text/data) → [String](mcp://flutter/api/dart-core/String)?
The text to display.


[hashCode](mcp://flutter/api/widgets/Widget/hashCode) → [int](mcp://flutter/api/dart-core/int)
The hash code for this object.


[key](mcp://flutter/api/widgets/Widget/key) → [Key](mcp://flutter/api/foundation/Key)?
Controls how one widget replaces another widget in the tree.


[locale](mcp://flutter/api/widgets/Text/locale) → [Locale](mcp://flutter/api/dart-ui/Locale)?
Used to select a font when the same Unicode character can
be rendered differently, depending on the locale.


[maxLines](mcp://flutter/api/widgets/Text/maxLines) → [int](mcp://flutter/api/dart-core/int)?
An optional maximum number of lines for the text to span, wrapping if necessary.
If the text exceeds the given number of lines, it will be truncated according
to [overflow](mcp://flutter/api/widgets/Text/overflow).


[overflow](mcp://flutter/api/widgets/Text/overflow) → [TextOverflow](mcp://flutter/api/painting/TextOverflow)?
How visual overflow should be handled.


[runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) → [Type](mcp://flutter/api/dart-core/Type)
A representation of the runtime type of the object.


[selectionColor](mcp://flutter/api/widgets/Text/selectionColor) → [Color](mcp://flutter/api/dart-ui/Color)?
The color to use when painting the selection.


[semanticsIdentifier](mcp://flutter/api/widgets/Text/semanticsIdentifier) → [String](mcp://flutter/api/dart-core/String)?
A unique identifier for the semantics node for this widget.


[semanticsLabel](mcp://flutter/api/widgets/Text/semanticsLabel) → [String](mcp://flutter/api/dart-core/String)?
An alternative semantics label for this text.


[softWrap](mcp://flutter/api/widgets/Text/softWrap) → [bool](mcp://flutter/api/dart-core/bool)?
Whether the text should break at soft line breaks.


[strutStyle](mcp://flutter/api/widgets/Text/strutStyle) → [StrutStyle](mcp://flutter/api/painting/StrutStyle)?
The strut style to use. Strut style defines the strut, which sets minimum
vertical layout metrics.


[style](mcp://flutter/api/widgets/Text/style) → [TextStyle](mcp://flutter/api/painting/TextStyle)?
If non-null, the style to use for this text.


[textAlign](mcp://flutter/api/widgets/Text/textAlign) → [TextAlign](mcp://flutter/api/dart-ui/TextAlign)?
How the text should be aligned horizontally.


[textDirection](mcp://flutter/api/widgets/Text/textDirection) → [TextDirection](mcp://flutter/api/dart-ui/TextDirection)?
The directionality of the text.


[textHeightBehavior](mcp://flutter/api/widgets/Text/textHeightBehavior) → [TextHeightBehavior](mcp://flutter/api/dart-ui/TextHeightBehavior)?
Defines how to apply [TextStyle.height](mcp://flutter/api/painting/TextStyle/height) over and under text.


[textScaleFactor](mcp://flutter/api/widgets/Text/textScaleFactor) → [double](mcp://flutter/api/dart-core/double)?
Deprecated. Will be removed in a future version of Flutter. Use
[textScaler](mcp://flutter/api/widgets/Text/textScaler) instead.


[textScaler](mcp://flutter/api/widgets/Text/textScaler) → [TextScaler](mcp://flutter/api/painting/TextScaler)?
The font scaling strategy to use when laying out and rendering the text.


[textSpan](mcp://flutter/api/widgets/Text/textSpan) → [InlineSpan](mcp://flutter/api/painting/InlineSpan)?
The text to display as a [InlineSpan](mcp://flutter/api/painting/InlineSpan).


[textWidthBasis](mcp://flutter/api/widgets/Text/textWidthBasis) → [TextWidthBasis](mcp://flutter/api/painting/TextWidthBasis)?
Defines how to measure the width of the rendered text.


## Methods

[build](mcp://flutter/api/widgets/Text/build)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [Widget](mcp://flutter/api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[createElement](mcp://flutter/api/widgets/StatelessWidget/createElement)() → [StatelessElement](mcp://flutter/api/widgets/StatelessElement)
Creates a [StatelessElement](mcp://flutter/api/widgets/StatelessElement) to manage this widget's location in the tree.


[debugDescribeChildren](mcp://flutter/api/foundation/DiagnosticableTree/debugDescribeChildren)() → [List](mcp://flutter/api/dart-core/List)<[DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)>
Returns a list of [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode) objects describing this node's
children.


[debugFillProperties](mcp://flutter/api/widgets/Text/debugFillProperties)([DiagnosticPropertiesBuilder](mcp://flutter/api/foundation/DiagnosticPropertiesBuilder) properties) → void
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
