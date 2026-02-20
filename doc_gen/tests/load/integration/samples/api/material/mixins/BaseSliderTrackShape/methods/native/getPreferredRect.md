# getPreferredRect method

[Rect](flutter-docs://api/dart-ui/Rect) getPreferredRect({
required [RenderBox](flutter-docs://api/rendering/RenderBox) parentBox,
[Offset](flutter-docs://api/dart-ui/Offset) offset = Offset.zero,
required [SliderThemeData](flutter-docs://api/material/SliderThemeData) sliderTheme,
[bool](flutter-docs://api/dart-core/bool) isEnabled = false,
[bool](flutter-docs://api/dart-core/bool) isDiscrete = false,
})

Returns a rect that represents the track bounds that fits within the[Slider](flutter-docs://api/material/Slider).

The width is the width of the [Slider](flutter-docs://api/material/Slider) or [RangeSlider](flutter-docs://api/material/RangeSlider), but padded by
the max of the overlay and thumb radius. The height is defined by the [SliderThemeData.trackHeight](flutter-docs://api/material/SliderThemeData/trackHeight).

The [Rect](flutter-docs://api/dart-ui/Rect) is centered both horizontally and vertically within the slider
bounds.

## Implementation

```dart
Rect getPreferredRect({
  required RenderBox parentBox,
  Offset offset = Offset.zero,
  required SliderThemeData sliderTheme,
  bool isEnabled = false,
  bool isDiscrete = false,
}) {
  final double thumbWidth = sliderTheme.thumbShape!.getPreferredSize(isEnabled, isDiscrete).width;
  final double overlayWidth = sliderTheme.overlayShape!
      .getPreferredSize(isEnabled, isDiscrete)
      .width;
  double trackHeight = sliderTheme.trackHeight!;
  assert(overlayWidth >= 0);
  assert(trackHeight >= 0);

  // If the track colors are transparent, then override only the track height
  // to maintain overall Slider width.
  if (sliderTheme.activeTrackColor == Colors.transparent &&
      sliderTheme.inactiveTrackColor == Colors.transparent) {
    trackHeight = 0;
  }

  final double trackLeft =
      offset.dx + (sliderTheme.padding == null ? math.max(overlayWidth / 2, thumbWidth / 2) : 0);
  final double trackTop = offset.dy + (parentBox.size.height - trackHeight) / 2;
  final double trackRight =
      trackLeft +
      parentBox.size.width -
      (sliderTheme.padding == null ? math.max(thumbWidth, overlayWidth) : 0);
  final double trackBottom = trackTop + trackHeight;
  // If the parentBox's size less than slider's size the trackRight will be less than trackLeft, so switch them.
  return Rect.fromLTRB(
    math.min(trackLeft, trackRight),
    trackTop,
    math.max(trackLeft, trackRight),
    trackBottom,
  );
}
```