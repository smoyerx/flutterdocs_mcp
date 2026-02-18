# getAdaptation<T> method

[Adaptation](mcp://flutter/api/material/Adaptation)<T>?getAdaptation<T>()

Used to obtain a particular [Adaptation](mcp://flutter/api/material/Adaptation) from [adaptationMap](mcp://flutter/api/material/ThemeData/adaptationMap).

To get an adaptation, use `Theme.of(context).getAdaptation<MyAdaptation>()`.

## Implementation

```dart
Adaptation<T>? getAdaptation<T>() => adaptationMap[T] as Adaptation<T>?;
```