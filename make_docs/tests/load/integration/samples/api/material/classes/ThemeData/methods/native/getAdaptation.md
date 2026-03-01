# getAdaptation<T> method

[Adaptation](flutter-docs://api/material/Adaptation)<T>? getAdaptation<T>()

Used to obtain a particular [Adaptation](flutter-docs://api/material/Adaptation) from [adaptationMap](flutter-docs://api/material/ThemeData/adaptationMap).

To get an adaptation, use `Theme.of(context).getAdaptation<MyAdaptation>()`.

## Implementation

```dart
Adaptation<T>? getAdaptation<T>() => adaptationMap[T] as Adaptation<T>?;
```