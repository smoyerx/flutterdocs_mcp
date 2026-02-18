# BaseSliderTrackShape mixin

Base track shape that provides an implementation of [getPreferredRect](mcp://flutter/api/material/BaseSliderTrackShape/getPreferredRect) for
default sizing.

The height is set from [SliderThemeData.trackHeight](mcp://flutter/api/material/SliderThemeData/trackHeight) and the width of the
parent box less the larger of the widths of [SliderThemeData.thumbShape](mcp://flutter/api/material/SliderThemeData/thumbShape) and [SliderThemeData.overlayShape](mcp://flutter/api/material/SliderThemeData/overlayShape).

See also:

- [RectangularSliderTrackShape](mcp://flutter/api/material/RectangularSliderTrackShape), which is a track shape with sharp
rectangular edges
- [RoundedRectSliderTrackShape](mcp://flutter/api/material/RoundedRectSliderTrackShape), which is a track shape with round
stadium-like edges.


Mixin applications
- [GappedSliderTrackShape](mcp://flutter/api/material/GappedSliderTrackShape)
- [RectangularSliderTrackShape](mcp://flutter/api/material/RectangularSliderTrackShape)
- [RoundedRectSliderTrackShape](mcp://flutter/api/material/RoundedRectSliderTrackShape)

## Properties

[hashCode](mcp://flutter/api/material/BaseSliderTrackShape/hashCode) → [int](mcp://flutter/api/dart-core/int)
The hash code for this object.


[isRounded](mcp://flutter/api/material/BaseSliderTrackShape/isRounded) → [bool](mcp://flutter/api/dart-core/bool)
Whether the track shape is rounded. This is used to determine the correct
position of the thumb in relation to the track. Defaults to false.


[runtimeType](mcp://flutter/api/material/BaseSliderTrackShape/runtimeType) → [Type](mcp://flutter/api/dart-core/Type)
A representation of the runtime type of the object.


## Methods

[getPreferredRect](mcp://flutter/api/material/BaseSliderTrackShape/getPreferredRect)({required [RenderBox](mcp://flutter/api/rendering/RenderBox) parentBox, [Offset](mcp://flutter/api/dart-ui/Offset) offset = Offset.zero, required [SliderThemeData](mcp://flutter/api/material/SliderThemeData) sliderTheme, [bool](mcp://flutter/api/dart-core/bool) isEnabled = false, [bool](mcp://flutter/api/dart-core/bool) isDiscrete = false}) → [Rect](mcp://flutter/api/dart-ui/Rect)
Returns a rect that represents the track bounds that fits within the
[Slider](mcp://flutter/api/material/Slider).

[noSuchMethod](mcp://flutter/api/material/BaseSliderTrackShape/noSuchMethod)([Invocation](mcp://flutter/api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[toString](mcp://flutter/api/material/BaseSliderTrackShape/toString)() → [String](mcp://flutter/api/dart-core/String)
A string representation of this object.


## Operators

[operator ==](mcp://flutter/api/material/BaseSliderTrackShape/operator_equals)([Object](mcp://flutter/api/dart-core/Object) other) → [bool](mcp://flutter/api/dart-core/bool)
The equality operator.
