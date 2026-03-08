# toString method

[String](flutter-docs://api/dart-core/String) toString()


A string representation of this object.

Some classes have a default textual representation,
often paired with a static `parse` function (like [int.parse](flutter-docs://api/dart-core/int/parse)).
These classes will provide the textual representation as
their string representation.

Other classes have no meaningful textual representation
that a program will care about.
Such classes will typically override `toString` to provide
useful information when inspecting the object,
mainly for debugging or logging.

## Implementation

```dart
String toString() {
  StringBuffer sb = StringBuffer();
  sb.write(type);
  if (message.isNotEmpty) {
    sb.write(": $message");
    if (osError != null) {
      sb.write(" ($osError)");
    }
  } else if (osError != null) {
    sb.write(": $osError");
  }
  return sb.toString();
}
```