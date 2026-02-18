# adaptationMap property

[Map](mcp://flutter/api/dart-core/Map)<[Type](mcp://flutter/api/dart-core/Type), [Adaptation](mcp://flutter/api/material/Adaptation)<[Object](mcp://flutter/api/dart-core/Object)>>adaptationMap


A map which contains the adaptations for the theme. The entry's key is the
type of the adaptation; the value is the adaptation itself.

To obtain an adaptation, use [getAdaptation](mcp://flutter/api/material/ThemeData/getAdaptation).

## Implementation

```dart
final Map<Type, Adaptation<Object>> adaptationMap;
```