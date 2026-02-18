# textScaler property

[TextScaler](mcp://flutter/api/painting/TextScaler)? textScaler


The font scaling strategy to use when laying out and rendering the text.

The value usually comes from [MediaQuery.textScalerOf](mcp://flutter/api/widgets/MediaQuery/textScalerOf), which typically
reflects the user-specified text scaling value in the platform's
accessibility settings. The [TextStyle.fontSize](mcp://flutter/api/painting/TextStyle/fontSize) of the text will be
adjusted by the [TextScaler](mcp://flutter/api/painting/TextScaler) before the text is laid out and rendered.

## Implementation

```dart
final TextScaler? textScaler;
```