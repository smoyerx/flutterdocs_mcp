# debugFillProperties method

@[override](mcp://flutter/api/dart-core/override)
voiddebugFillProperties(
[DiagnosticPropertiesBuilder](mcp://flutter/api/foundation/DiagnosticPropertiesBuilder) properties
)


Add additional properties associated with the node.

[https://www.youtube.com/embed/DnC7eT-vh1k?rel=0](https://www.youtube.com/embed/DnC7eT-vh1k?rel=0)

Use the most specific [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) existing subclass to describe
each property instead of the [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) base class. There are
only a small number of [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) subclasses each covering a
common use case. Consider what values a property is relevant for users
debugging as users debugging large trees are overloaded with information.
Common named parameters in [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode) subclasses help filter when
and how properties are displayed.

`defaultValue`, `showName`, `showSeparator`, and `level` keep string
representations of diagnostics terse and hide properties when they are not
very useful.

- Use `defaultValue` any time the default value of a property is
uninteresting. For example, specify a default value of null any time
a property being null does not indicate an error.
- Avoid specifying the `level` parameter unless the result you want
cannot be achieved by using the `defaultValue` parameter or using
the [ObjectFlagProperty](mcp://flutter/api/foundation/ObjectFlagProperty) class to conditionally display the property
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

- [StringProperty](mcp://flutter/api/foundation/StringProperty), which supports automatically enclosing a [String](mcp://flutter/api/dart-core/String) value in quotes.
- [DoubleProperty](mcp://flutter/api/foundation/DoubleProperty), which supports specifying a unit of measurement for
a [double](mcp://flutter/api/dart-core/double) value.
- [PercentProperty](mcp://flutter/api/foundation/PercentProperty), which clamps a [double](mcp://flutter/api/dart-core/double) to between 0 and 1 and
formats it as a percentage.
- [IntProperty](mcp://flutter/api/foundation/IntProperty), which supports specifying a unit of measurement for an
[int](mcp://flutter/api/dart-core/int) value.
- [FlagProperty](mcp://flutter/api/foundation/FlagProperty), which formats a [bool](mcp://flutter/api/dart-core/bool) value as one or more flags.
Depending on the use case it is better to format a bool as
`DiagnosticsProperty<bool>` instead of using [FlagProperty](mcp://flutter/api/foundation/FlagProperty) as the
output is more verbose but unambiguous.


## Other important [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) variants

- [EnumProperty](mcp://flutter/api/foundation/EnumProperty), which provides terse descriptions of enum values
working around limitations of the `toString` implementation for Dart
enum types.
- [IterableProperty](mcp://flutter/api/foundation/IterableProperty), which handles iterable values with display
customizable depending on the [DiagnosticsTreeStyle](mcp://flutter/api/foundation/DiagnosticsTreeStyle) used.
- [ObjectFlagProperty](mcp://flutter/api/foundation/ObjectFlagProperty), which provides terse descriptions of whether a
property value is present or not. For example, whether an `onClick` callback is specified or an animation is in progress.
- [ColorProperty](mcp://flutter/api/painting/ColorProperty), which must be used if the property value is
a [Color](mcp://flutter/api/dart-ui/Color) or one of its subclasses.
- [IconDataProperty](mcp://flutter/api/widgets/IconDataProperty), which must be used if the property value
is of type [IconData](mcp://flutter/api/widgets/IconData).


If none of these subclasses apply, use the [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) constructor or in rare cases create your own [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) subclass as in the case for [TransformProperty](mcp://flutter/api/painting/TransformProperty) which handles [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4) that represent transforms. Generally any property value with a good `toString` method implementation works fine using [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) directly.

This example shows best practices for implementing [debugFillProperties](mcp://flutter/api/material/ThemeData/debugFillProperties) illustrating use of all common [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) subclasses and all
common [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) parameters.



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

Used by [toDiagnosticsNode](mcp://flutter/api/foundation/Diagnosticable/toDiagnosticsNode) and [toString](mcp://flutter/api/foundation/Diagnosticable/toString).

Do not add values that have lifetime shorter than the object.

## Implementation

```dart
@override
void debugFillProperties(DiagnosticPropertiesBuilder properties) {
  super.debugFillProperties(properties);
  final ThemeData defaultData = ThemeData.fallback();
  // For the sanity of the reader, make sure these properties are in the same
  // order in every place that they are separated by section comments (e.g.
  // GENERAL CONFIGURATION). Each section except for deprecations should be
  // alphabetical by symbol name.

  // GENERAL CONFIGURATION
  properties.add(
    IterableProperty<Adaptation<dynamic>>(
      'adaptations',
      adaptationMap.values,
      defaultValue: defaultData.adaptationMap.values,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<bool>(
      'applyElevationOverlayColor',
      applyElevationOverlayColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<NoDefaultCupertinoThemeData>(
      'cupertinoOverrideTheme',
      cupertinoOverrideTheme,
      defaultValue: defaultData.cupertinoOverrideTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    IterableProperty<ThemeExtension<dynamic>>(
      'extensions',
      extensions.values,
      defaultValue: defaultData.extensions.values,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<InputDecorationThemeData>(
      'inputDecorationTheme',
      inputDecorationTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<MaterialTapTargetSize>(
      'materialTapTargetSize',
      materialTapTargetSize,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<PageTransitionsTheme>(
      'pageTransitionsTheme',
      pageTransitionsTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    EnumProperty<TargetPlatform>(
      'platform',
      platform,
      defaultValue: defaultTargetPlatform,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ScrollbarThemeData>(
      'scrollbarTheme',
      scrollbarTheme,
      defaultValue: defaultData.scrollbarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<InteractiveInkFeatureFactory>(
      'splashFactory',
      splashFactory,
      defaultValue: defaultData.splashFactory,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<bool>(
      'useMaterial3',
      useMaterial3,
      defaultValue: defaultData.useMaterial3,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<VisualDensity>(
      'visualDensity',
      visualDensity,
      defaultValue: defaultData.visualDensity,
      level: DiagnosticLevel.debug,
    ),
  );
  // COLORS
  properties.add(
    ColorProperty(
      'canvasColor',
      canvasColor,
      defaultValue: defaultData.canvasColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'cardColor',
      cardColor,
      defaultValue: defaultData.cardColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ColorScheme>(
      'colorScheme',
      colorScheme,
      defaultValue: defaultData.colorScheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'disabledColor',
      disabledColor,
      defaultValue: defaultData.disabledColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'dividerColor',
      dividerColor,
      defaultValue: defaultData.dividerColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'focusColor',
      focusColor,
      defaultValue: defaultData.focusColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'highlightColor',
      highlightColor,
      defaultValue: defaultData.highlightColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'hintColor',
      hintColor,
      defaultValue: defaultData.hintColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'hoverColor',
      hoverColor,
      defaultValue: defaultData.hoverColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'primaryColorDark',
      primaryColorDark,
      defaultValue: defaultData.primaryColorDark,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'primaryColorLight',
      primaryColorLight,
      defaultValue: defaultData.primaryColorLight,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'primaryColor',
      primaryColor,
      defaultValue: defaultData.primaryColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'scaffoldBackgroundColor',
      scaffoldBackgroundColor,
      defaultValue: defaultData.scaffoldBackgroundColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'secondaryHeaderColor',
      secondaryHeaderColor,
      defaultValue: defaultData.secondaryHeaderColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'shadowColor',
      shadowColor,
      defaultValue: defaultData.shadowColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'splashColor',
      splashColor,
      defaultValue: defaultData.splashColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'unselectedWidgetColor',
      unselectedWidgetColor,
      defaultValue: defaultData.unselectedWidgetColor,
      level: DiagnosticLevel.debug,
    ),
  );
  // TYPOGRAPHY & ICONOGRAPHY
  properties.add(
    DiagnosticsProperty<IconThemeData>('iconTheme', iconTheme, level: DiagnosticLevel.debug),
  );
  properties.add(
    DiagnosticsProperty<IconThemeData>(
      'primaryIconTheme',
      primaryIconTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<TextTheme>(
      'primaryTextTheme',
      primaryTextTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<TextTheme>('textTheme', textTheme, level: DiagnosticLevel.debug),
  );
  properties.add(
    DiagnosticsProperty<Typography>(
      'typography',
      typography,
      defaultValue: defaultData.typography,
      level: DiagnosticLevel.debug,
    ),
  );
  // COMPONENT THEMES
  properties.add(
    DiagnosticsProperty<ActionIconThemeData>(
      'actionIconTheme',
      actionIconTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<AppBarThemeData>(
      'appBarTheme',
      appBarTheme,
      defaultValue: defaultData.appBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<BadgeThemeData>(
      'badgeTheme',
      badgeTheme,
      defaultValue: defaultData.badgeTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<MaterialBannerThemeData>(
      'bannerTheme',
      bannerTheme,
      defaultValue: defaultData.bannerTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<BottomAppBarThemeData>(
      'bottomAppBarTheme',
      bottomAppBarTheme,
      defaultValue: defaultData.bottomAppBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<BottomNavigationBarThemeData>(
      'bottomNavigationBarTheme',
      bottomNavigationBarTheme,
      defaultValue: defaultData.bottomNavigationBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<BottomSheetThemeData>(
      'bottomSheetTheme',
      bottomSheetTheme,
      defaultValue: defaultData.bottomSheetTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ButtonThemeData>(
      'buttonTheme',
      buttonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<CardThemeData>('cardTheme', cardTheme, level: DiagnosticLevel.debug),
  );
  properties.add(
    DiagnosticsProperty<CarouselViewThemeData>(
      'carouselViewTheme',
      carouselViewTheme,
      defaultValue: defaultData.carouselViewTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<CheckboxThemeData>(
      'checkboxTheme',
      checkboxTheme,
      defaultValue: defaultData.checkboxTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ChipThemeData>('chipTheme', chipTheme, level: DiagnosticLevel.debug),
  );
  properties.add(
    DiagnosticsProperty<DataTableThemeData>(
      'dataTableTheme',
      dataTableTheme,
      defaultValue: defaultData.dataTableTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<DatePickerThemeData>(
      'datePickerTheme',
      datePickerTheme,
      defaultValue: defaultData.datePickerTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<DialogThemeData>(
      'dialogTheme',
      dialogTheme,
      defaultValue: defaultData.dialogTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<DividerThemeData>(
      'dividerTheme',
      dividerTheme,
      defaultValue: defaultData.dividerTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<DrawerThemeData>(
      'drawerTheme',
      drawerTheme,
      defaultValue: defaultData.drawerTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<DropdownMenuThemeData>(
      'dropdownMenuTheme',
      dropdownMenuTheme,
      defaultValue: defaultData.dropdownMenuTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ElevatedButtonThemeData>(
      'elevatedButtonTheme',
      elevatedButtonTheme,
      defaultValue: defaultData.elevatedButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ExpansionTileThemeData>(
      'expansionTileTheme',
      expansionTileTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<FilledButtonThemeData>(
      'filledButtonTheme',
      filledButtonTheme,
      defaultValue: defaultData.filledButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<FloatingActionButtonThemeData>(
      'floatingActionButtonTheme',
      floatingActionButtonTheme,
      defaultValue: defaultData.floatingActionButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<IconButtonThemeData>(
      'iconButtonTheme',
      iconButtonTheme,
      defaultValue: defaultData.iconButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ListTileThemeData>(
      'listTileTheme',
      listTileTheme,
      defaultValue: defaultData.listTileTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<MenuBarThemeData>(
      'menuBarTheme',
      menuBarTheme,
      defaultValue: defaultData.menuBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<MenuButtonThemeData>(
      'menuButtonTheme',
      menuButtonTheme,
      defaultValue: defaultData.menuButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<MenuThemeData>(
      'menuTheme',
      menuTheme,
      defaultValue: defaultData.menuTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<NavigationBarThemeData>(
      'navigationBarTheme',
      navigationBarTheme,
      defaultValue: defaultData.navigationBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<NavigationDrawerThemeData>(
      'navigationDrawerTheme',
      navigationDrawerTheme,
      defaultValue: defaultData.navigationDrawerTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<NavigationRailThemeData>(
      'navigationRailTheme',
      navigationRailTheme,
      defaultValue: defaultData.navigationRailTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<OutlinedButtonThemeData>(
      'outlinedButtonTheme',
      outlinedButtonTheme,
      defaultValue: defaultData.outlinedButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<PopupMenuThemeData>(
      'popupMenuTheme',
      popupMenuTheme,
      defaultValue: defaultData.popupMenuTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ProgressIndicatorThemeData>(
      'progressIndicatorTheme',
      progressIndicatorTheme,
      defaultValue: defaultData.progressIndicatorTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<RadioThemeData>(
      'radioTheme',
      radioTheme,
      defaultValue: defaultData.radioTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<SearchBarThemeData>(
      'searchBarTheme',
      searchBarTheme,
      defaultValue: defaultData.searchBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<SearchViewThemeData>(
      'searchViewTheme',
      searchViewTheme,
      defaultValue: defaultData.searchViewTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<SegmentedButtonThemeData>(
      'segmentedButtonTheme',
      segmentedButtonTheme,
      defaultValue: defaultData.segmentedButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<SliderThemeData>(
      'sliderTheme',
      sliderTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<SnackBarThemeData>(
      'snackBarTheme',
      snackBarTheme,
      defaultValue: defaultData.snackBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<SwitchThemeData>(
      'switchTheme',
      switchTheme,
      defaultValue: defaultData.switchTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<TabBarThemeData>(
      'tabBarTheme',
      tabBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<TextButtonThemeData>(
      'textButtonTheme',
      textButtonTheme,
      defaultValue: defaultData.textButtonTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<TextSelectionThemeData>(
      'textSelectionTheme',
      textSelectionTheme,
      defaultValue: defaultData.textSelectionTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<TimePickerThemeData>(
      'timePickerTheme',
      timePickerTheme,
      defaultValue: defaultData.timePickerTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<ToggleButtonsThemeData>(
      'toggleButtonsTheme',
      toggleButtonsTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    DiagnosticsProperty<TooltipThemeData>(
      'tooltipTheme',
      tooltipTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  // DEPRECATED (newest deprecations at the bottom)
  properties.add(
    DiagnosticsProperty<ButtonBarThemeData>(
      'buttonBarTheme',
      buttonBarTheme,
      defaultValue: defaultData.buttonBarTheme,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'dialogBackgroundColor',
      dialogBackgroundColor,
      defaultValue: defaultData.dialogBackgroundColor,
      level: DiagnosticLevel.debug,
    ),
  );
  properties.add(
    ColorProperty(
      'indicatorColor',
      indicatorColor,
      defaultValue: defaultData.indicatorColor,
      level: DiagnosticLevel.debug,
    ),
  );
}
```