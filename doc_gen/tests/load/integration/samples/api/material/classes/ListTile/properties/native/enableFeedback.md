# enableFeedback property

[bool](flutter-docs://api/dart-core/bool)? enableFeedback


Whether detected gestures should provide acoustic and/or haptic feedback.

For example, on Android a tap will produce a clicking sound and a
long-press will produce a short vibration, when feedback is enabled.

When null, the default value is true.

See also:

- [Feedback](flutter-docs://api/widgets/Feedback) for providing platform-specific feedback to certain actions.


## Implementation

```dart
final bool? enableFeedback;
```