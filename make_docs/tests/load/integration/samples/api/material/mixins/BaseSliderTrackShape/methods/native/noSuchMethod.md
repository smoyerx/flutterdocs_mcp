# noSuchMethod method

dynamic noSuchMethod(
[Invocation](flutter-docs://api/dart-core/Invocation) invocation
)


Invoked when a nonexistent method or property is accessed.

A dynamic member invocation can attempt to call a member which
doesn't exist on the receiving object. Example:

```dart
dynamic object = 1;
object.add(42); // Statically allowed, run-time error

```
This invalid code will invoke the `noSuchMethod` method
of the integer `1` with an [Invocation](flutter-docs://api/dart-core/Invocation) representing the `.add(42)` call and arguments (which then throws).

Classes can override [noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod) to provide custom behavior
for such invalid dynamic invocations.

A class with a non-default [noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod) invocation can also
omit implementations for members of its interface.
Example:

```dart
class MockList<T> implements List<T> {
  noSuchMethod(Invocation invocation) {
    log(invocation);
    super.noSuchMethod(invocation); // Will throw.
  }
}
void main() {
  MockList().add(42);
}

```
This code has no compile-time warnings or errors even though
the `MockList` class has no concrete implementation of
any of the `List` interface methods.
Calls to `List` methods are forwarded to `noSuchMethod`,
so this code will `log` an invocation similar to `Invocation.method(#add, [42])` and then throw.

If a value is returned from `noSuchMethod`,
it becomes the result of the original invocation.
If the value is not of a type that can be returned by the original
invocation, a type error occurs at the invocation.

The default behavior is to throw a [NoSuchMethodError](flutter-docs://api/dart-core/NoSuchMethodError).

## Implementation

```dart
@pragma("vm:entry-point")
@pragma("wasm:entry-point")
external dynamic noSuchMethod(Invocation invocation);
```