# trailing property

[Widget](mcp://flutter/api/widgets/Widget)? trailing


A widget to display after the title.

Typically an [Icon](mcp://flutter/api/widgets/Icon) widget.

To show right-aligned metadata (assuming left-to-right reading order;
left-aligned for right-to-left reading order), consider using a [Row](mcp://flutter/api/widgets/Row) with [CrossAxisAlignment.baseline](mcp://flutter/api/rendering/CrossAxisAlignment) alignment whose first item is [Expanded](mcp://flutter/api/widgets/Expanded) and
whose second child is the metadata text, instead of using the [trailing](mcp://flutter/api/material/ListTile/trailing) property.

## Implementation

```dart
final Widget? trailing;
```