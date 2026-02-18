# mounted property

[bool](mcp://flutter/api/dart-core/bool) get mounted

Whether this [State](mcp://flutter/api/widgets/State) object is currently in a tree.

After creating a [State](mcp://flutter/api/widgets/State) object and before calling [initState](mcp://flutter/api/widgets/State/initState), the
framework "mounts" the [State](mcp://flutter/api/widgets/State) object by associating it with a [BuildContext](mcp://flutter/api/widgets/BuildContext). The [State](mcp://flutter/api/widgets/State) object remains mounted until the framework
calls [dispose](mcp://flutter/api/widgets/State/dispose), after which time the framework will never ask the [State](mcp://flutter/api/widgets/State) object to [build](mcp://flutter/api/widgets/State/build) again.

It is an error to call [setState](mcp://flutter/api/widgets/State/setState) unless [mounted](mcp://flutter/api/widgets/State/mounted) is true.

## Implementation

```dart
bool get mounted => _element != null;
```