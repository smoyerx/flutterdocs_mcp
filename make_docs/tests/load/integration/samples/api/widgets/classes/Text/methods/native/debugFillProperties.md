# debugFillProperties method

@[override](flutter-docs://api/dart-core/override)
voiddebugFillProperties(
[DiagnosticPropertiesBuilder](flutter-docs://api/foundation/DiagnosticPropertiesBuilder) properties
)


Add additional properties associated with the node.

[https://www.youtube.com/embed/DnC7eT-vh1k?rel=0](https://www.youtube.com/embed/DnC7eT-vh1k?rel=0)

Use the most specific [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) existing subclass to describe
each property instead of the [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) base class. There are
only a small number of [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) subclasses each covering a
common use case. Consider what values a property is relevant for users
debugging as users debugging large trees are overloaded with information.
Common named parameters in [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode) subclasses help filter when
and how properties are displayed.

`defaultValue`, `showName`, `showSeparator`, and `level` keep string
representations of diagnostics terse and hide properties when they are not
very useful.

- Use `defaultValue` any time the default value of a property is
uninteresting. For example, specify a default value of null any time
a property being null does not indicate an error.
- Avoid specifying the `level` parameter unless the result you want
cannot be achieved by using the `defaultValue` parameter or using
the [ObjectFlagProperty](flutter-docs://api/foundation/ObjectFlagProperty) class to conditionally display the property
as a flag.
- Specify `showName` and `showSeparator` in rare cases where the string
output would look clumsy if they were not set.

```dart
DiagnosticsProperty<Object>('child(3, 4)', null, ifNull: 'is null', showSeparator: false).toString()

```
Shows using `showSeparator` to get output `child(3, 4) is null` which
is more polished than `child(3, 4): is null`.

```dart
DiagnosticsProperty<IconData>('icon', icon, ifNull: '<empty>', showName: false).toString()

```
Shows using `showName` to omit the property name as in this context the
property name does not add useful information.

`ifNull`, `ifEmpty`, `unit`, and `tooltip` make property
descriptions clearer. The examples in the code sample below illustrate
good uses of all of these parameters.

## DiagnosticsProperty subclasses for primitive types

- [StringProperty](flutter-docs://api/foundation/StringProperty), which supports automatically enclosing a [String](flutter-docs://api/dart-core/String) value in quotes.
- [DoubleProperty](flutter-docs://api/foundation/DoubleProperty), which supports specifying a unit of measurement for
a [double](flutter-docs://api/dart-core/double) value.
- [PercentProperty](flutter-docs://api/foundation/PercentProperty), which clamps a [double](flutter-docs://api/dart-core/double) to between 0 and 1 and
formats it as a percentage.
- [IntProperty](flutter-docs://api/foundation/IntProperty), which supports specifying a unit of measurement for an
[int](flutter-docs://api/dart-core/int) value.
- [FlagProperty](flutter-docs://api/foundation/FlagProperty), which formats a [bool](flutter-docs://api/dart-core/bool) value as one or more flags.
Depending on the use case it is better to format a bool as
`DiagnosticsProperty<bool>` instead of using [FlagProperty](flutter-docs://api/foundation/FlagProperty) as the
output is more verbose but unambiguous.


## Other important [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) variants

- [EnumProperty](flutter-docs://api/foundation/EnumProperty), which provides terse descriptions of enum values
working around limitations of the `toString` implementation for Dart
enum types.
- [IterableProperty](flutter-docs://api/foundation/IterableProperty), which handles iterable values with display
customizable depending on the [DiagnosticsTreeStyle](flutter-docs://api/foundation/DiagnosticsTreeStyle) used.
- [ObjectFlagProperty](flutter-docs://api/foundation/ObjectFlagProperty), which provides terse descriptions of whether a
property value is present or not. For example, whether an `onClick` callback is specified or an animation is in progress.
- [ColorProperty](flutter-docs://api/painting/ColorProperty), which must be used if the property value is
a [Color](flutter-docs://api/dart-ui/Color) or one of its subclasses.
- [IconDataProperty](flutter-docs://api/widgets/IconDataProperty), which must be used if the property value
is of type [IconData](flutter-docs://api/widgets/IconData).


If none of these subclasses apply, use the [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) constructor or in rare cases create your own [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) subclass as in the case for [TransformProperty](flutter-docs://api/painting/TransformProperty) which handles [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4) that represent transforms. Generally any property value with a good `toString` method implementation works fine using [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) directly.

This example shows best practices for implementing [debugFillProperties](flutter-docs://api/widgets/Text/debugFillProperties) illustrating use of all common [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) subclasses and all
common [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) parameters.



```dart
class ExampleObject extends ExampleSuperclass {

  // ...various members and properties...

  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    // Always add properties from the base class first.
    super.debugFillProperties(properties);

    // Omit the property name 'message' when displaying this String property
    // as it would just add visual noise.
    properties.add(StringProperty('message', message, showName: false));

    properties.add(DoubleProperty('stepWidth', stepWidth));

    // A scale of 1.0 does nothing so should be hidden.
    properties.add(DoubleProperty('scale', scale, defaultValue: 1.0));

    // If the hitTestExtent matches the paintExtent, it is just set to its
    // default value so is not relevant.
    properties.add(DoubleProperty('hitTestExtent', hitTestExtent, defaultValue: paintExtent));

    // maxWidth of double.infinity indicates the width is unconstrained and
    // so maxWidth has no impact.
    properties.add(DoubleProperty('maxWidth', maxWidth, defaultValue: double.infinity));

    // Progress is a value between 0 and 1 or null. Showing it as a
    // percentage makes the meaning clear enough that the name can be
    // hidden.
    properties.add(PercentProperty(
      'progress',
      progress,
      showName: false,
      ifNull: '<indeterminate>',
    ));

    // Most text fields have maxLines set to 1.
    properties.add(IntProperty('maxLines', maxLines, defaultValue: 1));

    // Specify the unit as otherwise it would be unclear that time is in
    // milliseconds.
    properties.add(IntProperty('duration', duration.inMilliseconds, unit: 'ms'));

    // Tooltip is used instead of unit for this case as a unit should be a
    // terse description appropriate to display directly after a number
    // without a space.
    properties.add(DoubleProperty(
      'device pixel ratio',
      devicePixelRatio,
      tooltip: 'physical pixels per logical pixel',
    ));

    // Displaying the depth value would be distracting. Instead only display
    // if the depth value is missing.
    properties.add(ObjectFlagProperty<int>('depth', depth, ifNull: 'no depth'));

    // bool flag that is only shown when the value is true.
    properties.add(FlagProperty('using primary controller', value: primary));

    properties.add(FlagProperty(
      'isCurrent',
      value: isCurrent,
      ifTrue: 'active',
      ifFalse: 'inactive',
    ));

    properties.add(DiagnosticsProperty<bool>('keepAlive', keepAlive));

    // FlagProperty could have also been used in this case.
    // This option results in the text "obscureText: true" instead
    // of "obscureText" which is a bit more verbose but a bit clearer.
    properties.add(DiagnosticsProperty<bool>('obscureText', obscureText, defaultValue: false));

    properties.add(EnumProperty<TextAlign>('textAlign', textAlign, defaultValue: null));
    properties.add(EnumProperty<ImageRepeat>('repeat', repeat, defaultValue: ImageRepeat.noRepeat));

    // Warn users when the widget is missing but do not show the value.
    properties.add(ObjectFlagProperty<Widget>('widget', widget, ifNull: 'no widget'));

    properties.add(IterableProperty<BoxShadow>(
      'boxShadow',
      boxShadow,
      defaultValue: null,
      style: style,
    ));

    // Getting the value of size throws an exception unless hasSize is true.
    properties.add(DiagnosticsProperty<Size>.lazy(
      'size',
      () => size,
      description: '${ hasSize ? size : "MISSING" }',
    ));

    // If the `toString` method for the property value does not provide a
    // good terse description, write a DiagnosticsProperty subclass as in
    // the case of TransformProperty which displays a nice debugging view
    // of a Matrix4 that represents a transform.
    properties.add(TransformProperty('transform', transform));

    // If the value class has a good `toString` method, use
    // DiagnosticsProperty<YourValueType>. Specifying the value type ensures
    // that debugging tools always know the type of the field and so can
    // provide the right UI affordances. For example, in this case even
    // if color is null, a debugging tool still knows the value is a Color
    // and can display relevant color related UI.
    properties.add(DiagnosticsProperty<Color>('color', color));

    // Use a custom description to generate a more terse summary than the
    // `toString` method on the map class.
    properties.add(DiagnosticsProperty<Map<Listenable, VoidCallback>>(
      'handles',
      handles,
      description: handles != null
        ? '${handles!.length} active client${ handles!.length == 1 ? "" : "s" }'
        : null,
      ifNull: 'no notifications ever received',
      showName: false,
    ));
  }
}
```

Used by [toDiagnosticsNode](flutter-docs://api/foundation/DiagnosticableTree/toDiagnosticsNode) and [toString](flutter-docs://api/foundation/Diagnosticable/toString).

Do not add values that have lifetime shorter than the object.

## Implementation

```dart
@override
void debugFillProperties(DiagnosticPropertiesBuilder properties) {
  super.debugFillProperties(properties);
  properties.add(StringProperty('data', data, showName: false));
  if (textSpan != null) {
    properties.add(
      textSpan!.toDiagnosticsNode(name: 'textSpan', style: DiagnosticsTreeStyle.transition),
    );
  }
  style?.debugFillProperties(properties);
  properties.add(EnumProperty<TextAlign>('textAlign', textAlign, defaultValue: null));
  properties.add(EnumProperty<TextDirection>('textDirection', textDirection, defaultValue: null));
  properties.add(DiagnosticsProperty<Locale>('locale', locale, defaultValue: null));
  properties.add(
    FlagProperty(
      'softWrap',
      value: softWrap,
      ifTrue: 'wrapping at box width',
      ifFalse: 'no wrapping except at line break characters',
      showName: true,
    ),
  );
  properties.add(EnumProperty<TextOverflow>('overflow', overflow, defaultValue: null));
  properties.add(DoubleProperty('textScaleFactor', textScaleFactor, defaultValue: null));
  properties.add(IntProperty('maxLines', maxLines, defaultValue: null));
  properties.add(
    EnumProperty<TextWidthBasis>('textWidthBasis', textWidthBasis, defaultValue: null),
  );
  properties.add(
    DiagnosticsProperty<ui.TextHeightBehavior>(
      'textHeightBehavior',
      textHeightBehavior,
      defaultValue: null,
    ),
  );
  if (semanticsLabel != null) {
    properties.add(StringProperty('semanticsLabel', semanticsLabel));
  }
  if (semanticsIdentifier != null) {
    properties.add(StringProperty('semanticsIdentifier', semanticsIdentifier));
  }
}
```