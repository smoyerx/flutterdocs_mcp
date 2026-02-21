# toDiagnosticsNode method

[DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode) toDiagnosticsNode({
[String](flutter-docs://api/dart-core/String)? name,
[DiagnosticsTreeStyle](flutter-docs://api/foundation/DiagnosticsTreeStyle)? style,
})


Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](flutter-docs://api/foundation/DiagnosticsNode/toStringDeep).

Leave `name` as null if there is not a meaningful description of the
relationship between the this node and its parent.

Typically the `style` argument is only specified to indicate an atypical
relationship between the parent and the node. For example, pass [DiagnosticsTreeStyle.offstage](flutter-docs://api/foundation/DiagnosticsTreeStyle) to indicate that a node is offstage.

## Implementation

```dart
DiagnosticsNode toDiagnosticsNode({String? name, DiagnosticsTreeStyle? style}) {
  return DiagnosticableNode<Diagnosticable>(name: name, value: this, style: style);
}
```