# overflow property

[TextOverflow](mcp://flutter/api/painting/TextOverflow)? overflow


How visual overflow should be handled.

If this is null [TextStyle.overflow](mcp://flutter/api/painting/TextStyle/overflow) will be used, otherwise the value
from the nearest [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle) ancestor will be used.

## Implementation

```dart
final TextOverflow? overflow;
```