# accelerateEasing top-level constant

1. @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use Easing.legacyAccelerate (M2) or Easing.standardAccelerate (M3) instead. ' 'This curve is updated in M3. ' 'This feature was deprecated after v3.18.0-0.1.pre.')

[Curve](flutter-docs://api/animation/Curve) const accelerateEasing

The accelerate easing curve in the Material 2 specification.

Elements exiting a screen use acceleration easing,
where they start at rest and end at peak velocity.

See also:

- [material.io/design/motion/speed.html#easing](https://material.io/design/motion/speed.html#easing)


## Implementation

```dart
@Deprecated(
  'Use Easing.legacyAccelerate (M2) or Easing.standardAccelerate (M3) instead. '
  'This curve is updated in M3. '
  'This feature was deprecated after v3.18.0-0.1.pre.',
)
const Curve accelerateEasing = Cubic(0.4, 0.0, 1.0, 1.0);
```