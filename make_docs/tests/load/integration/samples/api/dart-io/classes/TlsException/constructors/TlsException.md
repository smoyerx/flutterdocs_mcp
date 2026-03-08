# TlsException constructor

const TlsException([

1. [String](flutter-docs://api/dart-core/String) message = "",
2. [OSError](flutter-docs://api/dart-io/OSError)? osError
])

## Implementation

```dart
@pragma("vm:entry-point")
const TlsException([String message = "", OSError? osError])
  : this._("TlsException", message, osError);
```