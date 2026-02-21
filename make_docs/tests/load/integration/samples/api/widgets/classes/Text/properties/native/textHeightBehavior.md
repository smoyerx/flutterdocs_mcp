# textHeightBehavior property

[TextHeightBehavior](flutter-docs://api/dart-ui/TextHeightBehavior)? textHeightBehavior


Defines how to apply [TextStyle.height](flutter-docs://api/painting/TextStyle/height) over and under text.

[TextHeightBehavior.applyHeightToFirstAscent](flutter-docs://api/dart-ui/TextHeightBehavior/applyHeightToFirstAscent) and [TextHeightBehavior.applyHeightToLastDescent](flutter-docs://api/dart-ui/TextHeightBehavior/applyHeightToLastDescent) represent whether the [TextStyle.height](flutter-docs://api/painting/TextStyle/height) modifier will be applied to the corresponding metric. By
default both properties are true, and [TextStyle.height](flutter-docs://api/painting/TextStyle/height) is applied as
normal. When set to false, the font's default ascent will be used.

[TextHeightBehavior.leadingDistribution](flutter-docs://api/dart-ui/TextHeightBehavior/leadingDistribution) determines how the
leading is distributed over and under text. This
property applies before [TextHeightBehavior.applyHeightToFirstAscent](flutter-docs://api/dart-ui/TextHeightBehavior/applyHeightToFirstAscent) and [TextHeightBehavior.applyHeightToLastDescent](flutter-docs://api/dart-ui/TextHeightBehavior/applyHeightToLastDescent).

## Implementation

```dart
final ui.TextHeightBehavior? textHeightBehavior;
```