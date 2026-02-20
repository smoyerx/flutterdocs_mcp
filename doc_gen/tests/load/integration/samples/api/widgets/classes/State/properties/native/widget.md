# widget property

T get widget

The current configuration.

A [State](flutter-docs://api/widgets/State) object's configuration is the corresponding [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) instance. This property is initialized by the framework before calling [initState](flutter-docs://api/widgets/State/initState). If the parent updates this location in the tree to a new
widget with the same [runtimeType](flutter-docs://api/dart-core/Object/runtimeType) and [Widget.key](flutter-docs://api/widgets/Widget/key) as the current
configuration, the framework will update this property to refer to the new
widget and then call [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget), passing the old configuration as
an argument.

## Implementation

```dart
T get widget => _widget!;
```