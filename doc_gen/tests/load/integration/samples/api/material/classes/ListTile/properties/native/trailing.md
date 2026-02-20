# trailing property

[Widget](flutter-docs://api/widgets/Widget)? trailing


A widget to display after the title.

Typically an [Icon](flutter-docs://api/widgets/Icon) widget.

To show right-aligned metadata (assuming left-to-right reading order;
left-aligned for right-to-left reading order), consider using a [Row](flutter-docs://api/widgets/Row) with [CrossAxisAlignment.baseline](flutter-docs://api/rendering/CrossAxisAlignment) alignment whose first item is [Expanded](flutter-docs://api/widgets/Expanded) and
whose second child is the metadata text, instead of using the [trailing](flutter-docs://api/material/ListTile/trailing) property.

## Implementation

```dart
final Widget? trailing;
```