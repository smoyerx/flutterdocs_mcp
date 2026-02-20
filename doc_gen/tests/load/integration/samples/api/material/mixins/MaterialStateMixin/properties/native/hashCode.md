# hashCode property

[int](flutter-docs://api/dart-core/int) get hashCode


The hash code for this object.

A hash code is a single integer which represents the state of the object
that affects [operator ==](flutter-docs://api/dart-core/Object/operator_equals) comparisons.

All objects have hash codes.
The default hash code implemented by [Object](flutter-docs://api/dart-core/Object) represents only the identity of the object,
the same way as the default [operator ==](flutter-docs://api/dart-core/Object/operator_equals) implementation only considers objects
equal if they are identical (see [identityHashCode](flutter-docs://api/dart-core/identityHashCode)).

If [operator ==](flutter-docs://api/dart-core/Object/operator_equals) is overridden to use the object state instead,
the hash code must also be changed to represent that state,
otherwise the object cannot be used in hash based data structures
like the default [Set](flutter-docs://api/dart-core/Set) and [Map](flutter-docs://api/dart-core/Map) implementations.

Hash codes must be the same for objects that are equal to each other
according to [operator ==](flutter-docs://api/dart-core/Object/operator_equals).
The hash code of an object should only change if the object changes
in a way that affects equality.
There are no further requirements for the hash codes.
They need not be consistent between executions of the same program
and there are no distribution guarantees.

Objects that are not equal are allowed to have the same hash code.
It is even technically allowed that all instances have the same hash code,
but if clashes happen too often,
it may reduce the efficiency of hash-based data structures
like [HashSet](flutter-docs://api/dart-collection/HashSet) or [HashMap](flutter-docs://api/dart-collection/HashMap).

If a subclass overrides [hashCode](flutter-docs://api/dart-core/Object/hashCode), it should override the [operator ==](flutter-docs://api/dart-core/Object/operator_equals) operator as well to maintain consistency.

## Implementation

```dart
external int get hashCode;
```