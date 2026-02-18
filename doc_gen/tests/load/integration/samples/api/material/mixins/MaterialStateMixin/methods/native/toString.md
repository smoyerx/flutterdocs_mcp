# toString method

@[override](mcp://flutter/api/dart-core/override)
[String](mcp://flutter/api/dart-core/String) toString({
[DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info,
})


A string representation of this object.

Some classes have a default textual representation,
often paired with a static `parse` function (like [int.parse](mcp://flutter/api/dart-core/int/parse)).
These classes will provide the textual representation as
their string representation.

Other classes have no meaningful textual representation
that a program will care about.
Such classes will typically override `toString` to provide
useful information when inspecting the object,
mainly for debugging or logging.

## Implementation

```dart
@override
String toString({DiagnosticLevel minLevel = DiagnosticLevel.info}) {
  String? fullString;
  assert(() {
    fullString = toDiagnosticsNode(
      style: DiagnosticsTreeStyle.singleLine,
    ).toString(minLevel: minLevel);
    return true;
  }());
  return fullString ?? toStringShort();
}
```