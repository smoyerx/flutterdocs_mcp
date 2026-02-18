# toStringShort method

[String](mcp://flutter/api/dart-core/String) toStringShort()


A brief description of this object, usually just the [runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) and the [hashCode](mcp://flutter/api/dart-core/Object/hashCode).

See also:

- [toString](mcp://flutter/api/foundation/Diagnosticable/toString), for a detailed description of the object.


## Implementation

```dart
String toStringShort() => describeIdentity(this);
```