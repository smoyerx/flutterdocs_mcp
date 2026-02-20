# BaseSliderTrackShape mixin

Base track shape that provides an implementation of [getPreferredRect](flutter-docs://api/material/BaseSliderTrackShape/getPreferredRect) for
default sizing.

The height is set from [SliderThemeData.trackHeight](flutter-docs://api/material/SliderThemeData/trackHeight) and the width of the
parent box less the larger of the widths of [SliderThemeData.thumbShape](flutter-docs://api/material/SliderThemeData/thumbShape) and [SliderThemeData.overlayShape](flutter-docs://api/material/SliderThemeData/overlayShape).

See also:

- [RectangularSliderTrackShape](flutter-docs://api/material/RectangularSliderTrackShape), which is a track shape with sharp
rectangular edges
- [RoundedRectSliderTrackShape](flutter-docs://api/material/RoundedRectSliderTrackShape), which is a track shape with round
stadium-like edges.


Mixin applications
- [GappedSliderTrackShape](flutter-docs://api/material/GappedSliderTrackShape)
- [RectangularSliderTrackShape](flutter-docs://api/material/RectangularSliderTrackShape)
- [RoundedRectSliderTrackShape](flutter-docs://api/material/RoundedRectSliderTrackShape)

## Properties

[hashCode](flutter-docs://api/material/BaseSliderTrackShape/hashCode) → [int](flutter-docs://api/dart-core/int)
The hash code for this object.


[isRounded](flutter-docs://api/material/BaseSliderTrackShape/isRounded) → [bool](flutter-docs://api/dart-core/bool)
Whether the track shape is rounded. This is used to determine the correct
position of the thumb in relation to the track. Defaults to false.


[runtimeType](flutter-docs://api/material/BaseSliderTrackShape/runtimeType) → [Type](flutter-docs://api/dart-core/Type)
A representation of the runtime type of the object.


## Methods

[getPreferredRect](flutter-docs://api/material/BaseSliderTrackShape/getPreferredRect)({required [RenderBox](flutter-docs://api/rendering/RenderBox) parentBox, [Offset](flutter-docs://api/dart-ui/Offset) offset = Offset.zero, required [SliderThemeData](flutter-docs://api/material/SliderThemeData) sliderTheme, [bool](flutter-docs://api/dart-core/bool) isEnabled = false, [bool](flutter-docs://api/dart-core/bool) isDiscrete = false}) → [Rect](flutter-docs://api/dart-ui/Rect)
Returns a rect that represents the track bounds that fits within the
[Slider](flutter-docs://api/material/Slider).

[noSuchMethod](flutter-docs://api/material/BaseSliderTrackShape/noSuchMethod)([Invocation](flutter-docs://api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[toString](flutter-docs://api/material/BaseSliderTrackShape/toString)() → [String](flutter-docs://api/dart-core/String)
A string representation of this object.


## Operators

[operator ==](flutter-docs://api/material/BaseSliderTrackShape/operator_equals)([Object](flutter-docs://api/dart-core/Object) other) → [bool](flutter-docs://api/dart-core/bool)
The equality operator.
