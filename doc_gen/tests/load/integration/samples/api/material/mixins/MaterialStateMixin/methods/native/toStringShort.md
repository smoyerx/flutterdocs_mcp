# toStringShort method

[String](flutter-docs://api/dart-core/String) toStringShort()


A brief description of this object, usually just the [runtimeType](flutter-docs://api/dart-core/Object/runtimeType) and the [hashCode](flutter-docs://api/dart-core/Object/hashCode).

See also:

- [toString](flutter-docs://api/foundation/Diagnosticable/toString), for a detailed description of the object.


## Implementation

```dart
String toStringShort() => describeIdentity(this);
```