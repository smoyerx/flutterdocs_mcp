# Text class

A run of text with a single style.

The [Text](flutter-docs://api/widgets/Text) widget displays a string of text with single style. The string
might break across multiple lines or might all be displayed on the same line
depending on the layout constraints.

The [style](flutter-docs://api/widgets/Text/style) argument is optional. When omitted, the text will use the style
from the closest enclosing [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle). If the given style's [TextStyle.inherit](flutter-docs://api/painting/TextStyle/inherit) property is true (the default), the given style will
be merged with the closest enclosing [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle). This merging
behavior is useful, for example, to make the text bold while using the
default font family and size.

This example shows how to display text using the [Text](flutter-docs://api/widgets/Text) widget with the
[overflow](flutter-docs://api/widgets/Text/overflow) set to [TextOverflow.ellipsis](flutter-docs://api/painting/TextOverflow).



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

Setting [maxLines](flutter-docs://api/widgets/Text/maxLines) to `1` is not equivalent to disabling soft wrapping with
[softWrap](flutter-docs://api/widgets/Text/softWrap). This is apparent when using [TextOverflow.fade](flutter-docs://api/painting/TextOverflow) as the following
examples show.



[Omitted image: If a second line overflows the Text widget displays a horizontal fade]

Here soft wrapping is enabled and the [Text](flutter-docs://api/widgets/Text) widget tries to wrap the words
"how are you?" to a second line. This is prevented by the [maxLines](flutter-docs://api/widgets/Text/maxLines) value
of `1`. The result is that a second line overflows and the fade appears in a
horizontal direction at the bottom.

[Omitted image: If a single line overflows the Text widget displays a horizontal fade]

Here soft wrapping is disabled with `softWrap: false` and the [Text](flutter-docs://api/widgets/Text) widget
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

Using the [Text.rich](flutter-docs://api/widgets/Text/Text.rich) constructor, the [Text](flutter-docs://api/widgets/Text) widget can
display a paragraph with differently styled [TextSpan](flutter-docs://api/painting/TextSpan) s. The sample
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

To make [Text](flutter-docs://api/widgets/Text) react to touch events, wrap it in a [GestureDetector](flutter-docs://api/widgets/GestureDetector) widget
with a [GestureDetector.onTap](flutter-docs://api/widgets/GestureDetector/onTap) handler.

In a Material Design application, consider using a [TextButton](flutter-docs://api/material/TextButton) instead, or
if that isn't appropriate, at least using an [InkWell](flutter-docs://api/material/InkWell) instead of [GestureDetector](flutter-docs://api/widgets/GestureDetector).

To make sections of the text interactive, use [RichText](flutter-docs://api/widgets/RichText) and specify a [TapGestureRecognizer](flutter-docs://api/gestures/TapGestureRecognizer) as the [TextSpan.recognizer](flutter-docs://api/painting/TextSpan/recognizer) of the relevant part of
the text.

## Selection

[Text](flutter-docs://api/widgets/Text) is not selectable by default. To make a [Text](flutter-docs://api/widgets/Text) selectable, one can
wrap a subtree with a [SelectionArea](flutter-docs://api/material/SelectionArea) widget. To exclude a part of a subtree
under [SelectionArea](flutter-docs://api/material/SelectionArea) from selection, once can also wrap that part of the
subtree with [SelectionContainer.disabled](flutter-docs://api/widgets/SelectionContainer/SelectionContainer.disabled).

This sample demonstrates how to disable selection for a Text under a
SelectionArea.


To create a local project with this code sample, run:  flutter create --sample=widgets.Text.4 mysample

[Omitted code: Interactive sample]

See also:

- [RichText](flutter-docs://api/widgets/RichText), which gives you more control over the text styles.
- [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle), which sets default styles for [Text](flutter-docs://api/widgets/Text) widgets.
- [SelectableRegion](flutter-docs://api/widgets/SelectableRegion), which provides an overview of the selection system.


Inheritance
- [Object](flutter-docs://api/dart-core/Object)
- [DiagnosticableTree](flutter-docs://api/foundation/DiagnosticableTree)
- [Widget](flutter-docs://api/widgets/Widget)
- [StatelessWidget](flutter-docs://api/widgets/StatelessWidget)
- Text

## Constructors

[Text](flutter-docs://api/widgets/Text/Text)([String](flutter-docs://api/dart-core/String) data, {[Key](flutter-docs://api/foundation/Key)? key, [TextStyle](flutter-docs://api/painting/TextStyle)? style, [StrutStyle](flutter-docs://api/painting/StrutStyle)? strutStyle, [TextAlign](flutter-docs://api/dart-ui/TextAlign)? textAlign, [TextDirection](flutter-docs://api/dart-ui/TextDirection)? textDirection, [Locale](flutter-docs://api/dart-ui/Locale)? locale, [bool](flutter-docs://api/dart-core/bool)? softWrap, [TextOverflow](flutter-docs://api/painting/TextOverflow)? overflow, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.') [double](flutter-docs://api/dart-core/double)? textScaleFactor, [TextScaler](flutter-docs://api/painting/TextScaler)? textScaler, [int](flutter-docs://api/dart-core/int)? maxLines, [String](flutter-docs://api/dart-core/String)? semanticsLabel, [String](flutter-docs://api/dart-core/String)? semanticsIdentifier, [TextWidthBasis](flutter-docs://api/painting/TextWidthBasis)? textWidthBasis, [TextHeightBehavior](flutter-docs://api/dart-ui/TextHeightBehavior)? textHeightBehavior, [Color](flutter-docs://api/dart-ui/Color)? selectionColor})
Creates a text widget.


[Text.rich](flutter-docs://api/widgets/Text/Text.rich)([InlineSpan](flutter-docs://api/painting/InlineSpan) textSpan, {[Key](flutter-docs://api/foundation/Key)? key, [TextStyle](flutter-docs://api/painting/TextStyle)? style, [StrutStyle](flutter-docs://api/painting/StrutStyle)? strutStyle, [TextAlign](flutter-docs://api/dart-ui/TextAlign)? textAlign, [TextDirection](flutter-docs://api/dart-ui/TextDirection)? textDirection, [Locale](flutter-docs://api/dart-ui/Locale)? locale, [bool](flutter-docs://api/dart-core/bool)? softWrap, [TextOverflow](flutter-docs://api/painting/TextOverflow)? overflow, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use textScaler instead. ' 'Use of textScaleFactor was deprecated in preparation for the upcoming nonlinear text scaling support. ' 'This feature was deprecated after v3.12.0-2.0.pre.') [double](flutter-docs://api/dart-core/double)? textScaleFactor, [TextScaler](flutter-docs://api/painting/TextScaler)? textScaler, [int](flutter-docs://api/dart-core/int)? maxLines, [String](flutter-docs://api/dart-core/String)? semanticsLabel, [String](flutter-docs://api/dart-core/String)? semanticsIdentifier, [TextWidthBasis](flutter-docs://api/painting/TextWidthBasis)? textWidthBasis, [TextHeightBehavior](flutter-docs://api/dart-ui/TextHeightBehavior)? textHeightBehavior, [Color](flutter-docs://api/dart-ui/Color)? selectionColor})
Creates a text widget with a [InlineSpan](flutter-docs://api/painting/InlineSpan).


## Properties

[data](flutter-docs://api/widgets/Text/data) → [String](flutter-docs://api/dart-core/String)?
The text to display.


[hashCode](flutter-docs://api/widgets/Widget/hashCode) → [int](flutter-docs://api/dart-core/int)
The hash code for this object.


[key](flutter-docs://api/widgets/Widget/key) → [Key](flutter-docs://api/foundation/Key)?
Controls how one widget replaces another widget in the tree.


[locale](flutter-docs://api/widgets/Text/locale) → [Locale](flutter-docs://api/dart-ui/Locale)?
Used to select a font when the same Unicode character can
be rendered differently, depending on the locale.


[maxLines](flutter-docs://api/widgets/Text/maxLines) → [int](flutter-docs://api/dart-core/int)?
An optional maximum number of lines for the text to span, wrapping if necessary.
If the text exceeds the given number of lines, it will be truncated according
to [overflow](flutter-docs://api/widgets/Text/overflow).


[overflow](flutter-docs://api/widgets/Text/overflow) → [TextOverflow](flutter-docs://api/painting/TextOverflow)?
How visual overflow should be handled.


[runtimeType](flutter-docs://api/dart-core/Object/runtimeType) → [Type](flutter-docs://api/dart-core/Type)
A representation of the runtime type of the object.


[selectionColor](flutter-docs://api/widgets/Text/selectionColor) → [Color](flutter-docs://api/dart-ui/Color)?
The color to use when painting the selection.


[semanticsIdentifier](flutter-docs://api/widgets/Text/semanticsIdentifier) → [String](flutter-docs://api/dart-core/String)?
A unique identifier for the semantics node for this widget.


[semanticsLabel](flutter-docs://api/widgets/Text/semanticsLabel) → [String](flutter-docs://api/dart-core/String)?
An alternative semantics label for this text.


[softWrap](flutter-docs://api/widgets/Text/softWrap) → [bool](flutter-docs://api/dart-core/bool)?
Whether the text should break at soft line breaks.


[strutStyle](flutter-docs://api/widgets/Text/strutStyle) → [StrutStyle](flutter-docs://api/painting/StrutStyle)?
The strut style to use. Strut style defines the strut, which sets minimum
vertical layout metrics.


[style](flutter-docs://api/widgets/Text/style) → [TextStyle](flutter-docs://api/painting/TextStyle)?
If non-null, the style to use for this text.


[textAlign](flutter-docs://api/widgets/Text/textAlign) → [TextAlign](flutter-docs://api/dart-ui/TextAlign)?
How the text should be aligned horizontally.


[textDirection](flutter-docs://api/widgets/Text/textDirection) → [TextDirection](flutter-docs://api/dart-ui/TextDirection)?
The directionality of the text.


[textHeightBehavior](flutter-docs://api/widgets/Text/textHeightBehavior) → [TextHeightBehavior](flutter-docs://api/dart-ui/TextHeightBehavior)?
Defines how to apply [TextStyle.height](flutter-docs://api/painting/TextStyle/height) over and under text.


[textScaleFactor](flutter-docs://api/widgets/Text/textScaleFactor) → [double](flutter-docs://api/dart-core/double)?
Deprecated. Will be removed in a future version of Flutter. Use
[textScaler](flutter-docs://api/widgets/Text/textScaler) instead.


[textScaler](flutter-docs://api/widgets/Text/textScaler) → [TextScaler](flutter-docs://api/painting/TextScaler)?
The font scaling strategy to use when laying out and rendering the text.


[textSpan](flutter-docs://api/widgets/Text/textSpan) → [InlineSpan](flutter-docs://api/painting/InlineSpan)?
The text to display as a [InlineSpan](flutter-docs://api/painting/InlineSpan).


[textWidthBasis](flutter-docs://api/widgets/Text/textWidthBasis) → [TextWidthBasis](flutter-docs://api/painting/TextWidthBasis)?
Defines how to measure the width of the rendered text.


## Methods

[build](flutter-docs://api/widgets/Text/build)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [Widget](flutter-docs://api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[createElement](flutter-docs://api/widgets/StatelessWidget/createElement)() → [StatelessElement](flutter-docs://api/widgets/StatelessElement)
Creates a [StatelessElement](flutter-docs://api/widgets/StatelessElement) to manage this widget's location in the tree.


[debugDescribeChildren](flutter-docs://api/foundation/DiagnosticableTree/debugDescribeChildren)() → [List](flutter-docs://api/dart-core/List)<[DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)>
Returns a list of [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode) objects describing this node's
children.


[debugFillProperties](flutter-docs://api/widgets/Text/debugFillProperties)([DiagnosticPropertiesBuilder](flutter-docs://api/foundation/DiagnosticPropertiesBuilder) properties) → void
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
