# mounted property

[bool](flutter-docs://api/dart-core/bool) get mounted


Whether this [State](flutter-docs://api/widgets/State) object is currently in a tree.

After creating a [State](flutter-docs://api/widgets/State) object and before calling [initState](flutter-docs://api/widgets/State/initState), the
framework "mounts" the [State](flutter-docs://api/widgets/State) object by associating it with a [BuildContext](flutter-docs://api/widgets/BuildContext). The [State](flutter-docs://api/widgets/State) object remains mounted until the framework
calls [dispose](flutter-docs://api/widgets/State/dispose), after which time the framework will never ask the [State](flutter-docs://api/widgets/State) object to [build](flutter-docs://api/widgets/State/build) again.

It is an error to call [setState](flutter-docs://api/widgets/State/setState) unless [mounted](flutter-docs://api/widgets/State/mounted) is true.

## Implementation

```dart
bool get mounted => _element != null;
```