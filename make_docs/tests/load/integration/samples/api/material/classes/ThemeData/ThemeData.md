# ThemeData class

Defines the configuration of the overall visual [Theme](flutter-docs://api/material/Theme) for a [MaterialApp](flutter-docs://api/material/MaterialApp) or a widget subtree within the app.

The [MaterialApp](flutter-docs://api/material/MaterialApp) theme property can be used to configure the appearance
of the entire app. Widget subtrees within an app can override the app's
theme by including a [Theme](flutter-docs://api/material/Theme) widget at the top of the subtree.

Widgets whose appearance should align with the overall theme can obtain the
current theme's configuration with [Theme.of](flutter-docs://api/material/Theme/of). Material components typically
depend exclusively on the [colorScheme](flutter-docs://api/material/ThemeData/colorScheme) and [textTheme](flutter-docs://api/material/ThemeData/textTheme). These properties
are guaranteed to have non-null values.

The static [Theme.of](flutter-docs://api/material/Theme/of) method finds the [ThemeData](flutter-docs://api/material/ThemeData) value specified for the
nearest [BuildContext](flutter-docs://api/widgets/BuildContext) ancestor. This lookup is inexpensive, essentially
just a single HashMap access. It can sometimes be a little confusing
because [Theme.of](flutter-docs://api/material/Theme/of) can not see a [Theme](flutter-docs://api/material/Theme) widget that is defined in the
current build method's context. To overcome that, create a new custom widget
for the subtree that appears below the new [Theme](flutter-docs://api/material/Theme), or insert a widget
that creates a new BuildContext, like [Builder](flutter-docs://api/widgets/Builder).

This example demonstrates how a typical [MaterialApp](flutter-docs://api/material/MaterialApp) specifies
and uses a custom [Theme](flutter-docs://api/material/Theme). The theme's [ColorScheme](flutter-docs://api/material/ColorScheme) is based on a
single "seed" color and configures itself to match the platform's
current light or dark color configuration. The theme overrides the
default configuration of [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) to show how to
customize the appearance a class of components.


To create a local project with this code sample, run:  flutter create --sample=material.ThemeData.1 mysample

[Omitted code: Interactive sample]

See [material.io/design/color/](https://material.io/design/color/) for
more discussion on how to pick the right colors.

Mixed-in types
- [Diagnosticable](flutter-docs://api/foundation/Diagnosticable)

Annotations
- @[immutable](flutter-docs://api/meta/immutable)

## Constructors

[ThemeData](flutter-docs://api/material/ThemeData/ThemeData)({[Iterable](flutter-docs://api/dart-core/Iterable)<[Adaptation](flutter-docs://api/material/Adaptation)<[Object](flutter-docs://api/dart-core/Object)>>? adaptations, [bool](flutter-docs://api/dart-core/bool)? applyElevationOverlayColor, [NoDefaultCupertinoThemeData](flutter-docs://api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme, [Iterable](flutter-docs://api/dart-core/Iterable)<[ThemeExtension](flutter-docs://api/material/ThemeExtension)>? extensions, [Object](flutter-docs://api/dart-core/Object)? inputDecorationTheme, [MaterialTapTargetSize](flutter-docs://api/material/MaterialTapTargetSize)? materialTapTargetSize, [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme)? pageTransitionsTheme, [TargetPlatform](flutter-docs://api/foundation/TargetPlatform)? platform, [ScrollbarThemeData](flutter-docs://api/material/ScrollbarThemeData)? scrollbarTheme, [InteractiveInkFeatureFactory](flutter-docs://api/material/InteractiveInkFeatureFactory)? splashFactory, [bool](flutter-docs://api/dart-core/bool)? useMaterial3, [bool](flutter-docs://api/dart-core/bool)? useSystemColors, [VisualDensity](flutter-docs://api/material/VisualDensity)? visualDensity, [ColorScheme](flutter-docs://api/material/ColorScheme)? colorScheme, [Brightness](flutter-docs://api/dart-ui/Brightness)? brightness, [Color](flutter-docs://api/dart-ui/Color)? colorSchemeSeed, [Color](flutter-docs://api/dart-ui/Color)? canvasColor, [Color](flutter-docs://api/dart-ui/Color)? cardColor, [Color](flutter-docs://api/dart-ui/Color)? disabledColor, [Color](flutter-docs://api/dart-ui/Color)? dividerColor, [Color](flutter-docs://api/dart-ui/Color)? focusColor, [Color](flutter-docs://api/dart-ui/Color)? highlightColor, [Color](flutter-docs://api/dart-ui/Color)? hintColor, [Color](flutter-docs://api/dart-ui/Color)? hoverColor, [Color](flutter-docs://api/dart-ui/Color)? primaryColor, [Color](flutter-docs://api/dart-ui/Color)? primaryColorDark, [Color](flutter-docs://api/dart-ui/Color)? primaryColorLight, [MaterialColor](flutter-docs://api/material/MaterialColor)? primarySwatch, [Color](flutter-docs://api/dart-ui/Color)? scaffoldBackgroundColor, [Color](flutter-docs://api/dart-ui/Color)? secondaryHeaderColor, [Color](flutter-docs://api/dart-ui/Color)? shadowColor, [Color](flutter-docs://api/dart-ui/Color)? splashColor, [Color](flutter-docs://api/dart-ui/Color)? unselectedWidgetColor, [String](flutter-docs://api/dart-core/String)? fontFamily, [List](flutter-docs://api/dart-core/List)<[String](flutter-docs://api/dart-core/String)>? fontFamilyFallback, [String](flutter-docs://api/dart-core/String)? package, [IconThemeData](flutter-docs://api/widgets/IconThemeData)? iconTheme, [IconThemeData](flutter-docs://api/widgets/IconThemeData)? primaryIconTheme, [TextTheme](flutter-docs://api/material/TextTheme)? primaryTextTheme, [TextTheme](flutter-docs://api/material/TextTheme)? textTheme, [Typography](flutter-docs://api/material/Typography)? typography, [ActionIconThemeData](flutter-docs://api/material/ActionIconThemeData)? actionIconTheme, [Object](flutter-docs://api/dart-core/Object)? appBarTheme, [BadgeThemeData](flutter-docs://api/material/BadgeThemeData)? badgeTheme, [MaterialBannerThemeData](flutter-docs://api/material/MaterialBannerThemeData)? bannerTheme, [BottomAppBarThemeData](flutter-docs://api/material/BottomAppBarThemeData)? bottomAppBarTheme, [BottomNavigationBarThemeData](flutter-docs://api/material/BottomNavigationBarThemeData)? bottomNavigationBarTheme, [BottomSheetThemeData](flutter-docs://api/material/BottomSheetThemeData)? bottomSheetTheme, [ButtonThemeData](flutter-docs://api/material/ButtonThemeData)? buttonTheme, [CardThemeData](flutter-docs://api/material/CardThemeData)? cardTheme, [CarouselViewThemeData](flutter-docs://api/material/CarouselViewThemeData)? carouselViewTheme, [CheckboxThemeData](flutter-docs://api/material/CheckboxThemeData)? checkboxTheme, [ChipThemeData](flutter-docs://api/material/ChipThemeData)? chipTheme, [DataTableThemeData](flutter-docs://api/material/DataTableThemeData)? dataTableTheme, [DatePickerThemeData](flutter-docs://api/material/DatePickerThemeData)? datePickerTheme, [DialogThemeData](flutter-docs://api/material/DialogThemeData)? dialogTheme, [DividerThemeData](flutter-docs://api/material/DividerThemeData)? dividerTheme, [DrawerThemeData](flutter-docs://api/material/DrawerThemeData)? drawerTheme, [DropdownMenuThemeData](flutter-docs://api/material/DropdownMenuThemeData)? dropdownMenuTheme, [ElevatedButtonThemeData](flutter-docs://api/material/ElevatedButtonThemeData)? elevatedButtonTheme, [ExpansionTileThemeData](flutter-docs://api/material/ExpansionTileThemeData)? expansionTileTheme, [FilledButtonThemeData](flutter-docs://api/material/FilledButtonThemeData)? filledButtonTheme, [FloatingActionButtonThemeData](flutter-docs://api/material/FloatingActionButtonThemeData)? floatingActionButtonTheme, [IconButtonThemeData](flutter-docs://api/material/IconButtonThemeData)? iconButtonTheme, [ListTileThemeData](flutter-docs://api/material/ListTileThemeData)? listTileTheme, [MenuBarThemeData](flutter-docs://api/material/MenuBarThemeData)? menuBarTheme, [MenuButtonThemeData](flutter-docs://api/material/MenuButtonThemeData)? menuButtonTheme, [MenuThemeData](flutter-docs://api/material/MenuThemeData)? menuTheme, [NavigationBarThemeData](flutter-docs://api/material/NavigationBarThemeData)? navigationBarTheme, [NavigationDrawerThemeData](flutter-docs://api/material/NavigationDrawerThemeData)? navigationDrawerTheme, [NavigationRailThemeData](flutter-docs://api/material/NavigationRailThemeData)? navigationRailTheme, [OutlinedButtonThemeData](flutter-docs://api/material/OutlinedButtonThemeData)? outlinedButtonTheme, [PopupMenuThemeData](flutter-docs://api/material/PopupMenuThemeData)? popupMenuTheme, [ProgressIndicatorThemeData](flutter-docs://api/material/ProgressIndicatorThemeData)? progressIndicatorTheme, [RadioThemeData](flutter-docs://api/material/RadioThemeData)? radioTheme, [SearchBarThemeData](flutter-docs://api/material/SearchBarThemeData)? searchBarTheme, [SearchViewThemeData](flutter-docs://api/material/SearchViewThemeData)? searchViewTheme, [SegmentedButtonThemeData](flutter-docs://api/material/SegmentedButtonThemeData)? segmentedButtonTheme, [SliderThemeData](flutter-docs://api/material/SliderThemeData)? sliderTheme, [SnackBarThemeData](flutter-docs://api/material/SnackBarThemeData)? snackBarTheme, [SwitchThemeData](flutter-docs://api/material/SwitchThemeData)? switchTheme, [TabBarThemeData](flutter-docs://api/material/TabBarThemeData)? tabBarTheme, [TextButtonThemeData](flutter-docs://api/material/TextButtonThemeData)? textButtonTheme, [TextSelectionThemeData](flutter-docs://api/material/TextSelectionThemeData)? textSelectionTheme, [TimePickerThemeData](flutter-docs://api/material/TimePickerThemeData)? timePickerTheme, [ToggleButtonsThemeData](flutter-docs://api/material/ToggleButtonsThemeData)? toggleButtonsTheme, [TooltipThemeData](flutter-docs://api/material/TooltipThemeData)? tooltipTheme, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use OverflowBar instead. ' 'This feature was deprecated after v3.21.0-10.0.pre.') [ButtonBarThemeData](flutter-docs://api/material/ButtonBarThemeData)? buttonBarTheme, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use DialogThemeData.backgroundColor instead. ' 'This feature was deprecated after v3.27.0-0.1.pre.') [Color](flutter-docs://api/dart-ui/Color)? dialogBackgroundColor, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use TabBarThemeData.indicatorColor instead. ' 'This feature was deprecated after v3.28.0-1.0.pre.') [Color](flutter-docs://api/dart-ui/Color)? indicatorColor})
Create a [ThemeData](flutter-docs://api/material/ThemeData) that's used to configure a [Theme](flutter-docs://api/material/Theme).


[ThemeData.dark](flutter-docs://api/material/ThemeData/ThemeData.dark)({[bool](flutter-docs://api/dart-core/bool)? useMaterial3})
A default dark theme.


[ThemeData.fallback](flutter-docs://api/material/ThemeData/ThemeData.fallback)({[bool](flutter-docs://api/dart-core/bool)? useMaterial3})
The default color theme. Same as [ThemeData.light](flutter-docs://api/material/ThemeData/ThemeData.light).


[ThemeData.from](flutter-docs://api/material/ThemeData/ThemeData.from)({required [ColorScheme](flutter-docs://api/material/ColorScheme) colorScheme, [TextTheme](flutter-docs://api/material/TextTheme)? textTheme, [bool](flutter-docs://api/dart-core/bool)? useMaterial3})
Create a [ThemeData](flutter-docs://api/material/ThemeData) based on the colors in the given `colorScheme` and
text styles of the optional `textTheme`.


[ThemeData.light](flutter-docs://api/material/ThemeData/ThemeData.light)({[bool](flutter-docs://api/dart-core/bool)? useMaterial3})
A default light theme.


[ThemeData.raw](flutter-docs://api/material/ThemeData/ThemeData.raw)({required [Map](flutter-docs://api/dart-core/Map)<[Type](flutter-docs://api/dart-core/Type), [Adaptation](flutter-docs://api/material/Adaptation)<[Object](flutter-docs://api/dart-core/Object)>> adaptationMap, required [bool](flutter-docs://api/dart-core/bool) applyElevationOverlayColor, required [NoDefaultCupertinoThemeData](flutter-docs://api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme, required [Map](flutter-docs://api/dart-core/Map)<[Object](flutter-docs://api/dart-core/Object), [ThemeExtension](flutter-docs://api/material/ThemeExtension)> extensions, required [InputDecorationThemeData](flutter-docs://api/material/InputDecorationThemeData) inputDecorationTheme, required [MaterialTapTargetSize](flutter-docs://api/material/MaterialTapTargetSize) materialTapTargetSize, required [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) pageTransitionsTheme, required [TargetPlatform](flutter-docs://api/foundation/TargetPlatform) platform, required [ScrollbarThemeData](flutter-docs://api/material/ScrollbarThemeData) scrollbarTheme, required [InteractiveInkFeatureFactory](flutter-docs://api/material/InteractiveInkFeatureFactory) splashFactory, required [bool](flutter-docs://api/dart-core/bool) useMaterial3, required [VisualDensity](flutter-docs://api/material/VisualDensity) visualDensity, required [ColorScheme](flutter-docs://api/material/ColorScheme) colorScheme, required [Color](flutter-docs://api/dart-ui/Color) canvasColor, required [Color](flutter-docs://api/dart-ui/Color) cardColor, required [Color](flutter-docs://api/dart-ui/Color) disabledColor, required [Color](flutter-docs://api/dart-ui/Color) dividerColor, required [Color](flutter-docs://api/dart-ui/Color) focusColor, required [Color](flutter-docs://api/dart-ui/Color) highlightColor, required [Color](flutter-docs://api/dart-ui/Color) hintColor, required [Color](flutter-docs://api/dart-ui/Color) hoverColor, required [Color](flutter-docs://api/dart-ui/Color) primaryColor, required [Color](flutter-docs://api/dart-ui/Color) primaryColorDark, required [Color](flutter-docs://api/dart-ui/Color) primaryColorLight, required [Color](flutter-docs://api/dart-ui/Color) scaffoldBackgroundColor, required [Color](flutter-docs://api/dart-ui/Color) secondaryHeaderColor, required [Color](flutter-docs://api/dart-ui/Color) shadowColor, required [Color](flutter-docs://api/dart-ui/Color) splashColor, required [Color](flutter-docs://api/dart-ui/Color) unselectedWidgetColor, required [IconThemeData](flutter-docs://api/widgets/IconThemeData) iconTheme, required [IconThemeData](flutter-docs://api/widgets/IconThemeData) primaryIconTheme, required [TextTheme](flutter-docs://api/material/TextTheme) primaryTextTheme, required [TextTheme](flutter-docs://api/material/TextTheme) textTheme, required [Typography](flutter-docs://api/material/Typography) typography, required [ActionIconThemeData](flutter-docs://api/material/ActionIconThemeData)? actionIconTheme, required [AppBarThemeData](flutter-docs://api/material/AppBarThemeData) appBarTheme, required [BadgeThemeData](flutter-docs://api/material/BadgeThemeData) badgeTheme, required [MaterialBannerThemeData](flutter-docs://api/material/MaterialBannerThemeData) bannerTheme, required [BottomAppBarThemeData](flutter-docs://api/material/BottomAppBarThemeData) bottomAppBarTheme, required [BottomNavigationBarThemeData](flutter-docs://api/material/BottomNavigationBarThemeData) bottomNavigationBarTheme, required [BottomSheetThemeData](flutter-docs://api/material/BottomSheetThemeData) bottomSheetTheme, required [ButtonThemeData](flutter-docs://api/material/ButtonThemeData) buttonTheme, required [CardThemeData](flutter-docs://api/material/CardThemeData) cardTheme, required [CarouselViewThemeData](flutter-docs://api/material/CarouselViewThemeData) carouselViewTheme, required [CheckboxThemeData](flutter-docs://api/material/CheckboxThemeData) checkboxTheme, required [ChipThemeData](flutter-docs://api/material/ChipThemeData) chipTheme, required [DataTableThemeData](flutter-docs://api/material/DataTableThemeData) dataTableTheme, required [DatePickerThemeData](flutter-docs://api/material/DatePickerThemeData) datePickerTheme, required [DialogThemeData](flutter-docs://api/material/DialogThemeData) dialogTheme, required [DividerThemeData](flutter-docs://api/material/DividerThemeData) dividerTheme, required [DrawerThemeData](flutter-docs://api/material/DrawerThemeData) drawerTheme, required [DropdownMenuThemeData](flutter-docs://api/material/DropdownMenuThemeData) dropdownMenuTheme, required [ElevatedButtonThemeData](flutter-docs://api/material/ElevatedButtonThemeData) elevatedButtonTheme, required [ExpansionTileThemeData](flutter-docs://api/material/ExpansionTileThemeData) expansionTileTheme, required [FilledButtonThemeData](flutter-docs://api/material/FilledButtonThemeData) filledButtonTheme, required [FloatingActionButtonThemeData](flutter-docs://api/material/FloatingActionButtonThemeData) floatingActionButtonTheme, required [IconButtonThemeData](flutter-docs://api/material/IconButtonThemeData) iconButtonTheme, required [ListTileThemeData](flutter-docs://api/material/ListTileThemeData) listTileTheme, required [MenuBarThemeData](flutter-docs://api/material/MenuBarThemeData) menuBarTheme, required [MenuButtonThemeData](flutter-docs://api/material/MenuButtonThemeData) menuButtonTheme, required [MenuThemeData](flutter-docs://api/material/MenuThemeData) menuTheme, required [NavigationBarThemeData](flutter-docs://api/material/NavigationBarThemeData) navigationBarTheme, required [NavigationDrawerThemeData](flutter-docs://api/material/NavigationDrawerThemeData) navigationDrawerTheme, required [NavigationRailThemeData](flutter-docs://api/material/NavigationRailThemeData) navigationRailTheme, required [OutlinedButtonThemeData](flutter-docs://api/material/OutlinedButtonThemeData) outlinedButtonTheme, required [PopupMenuThemeData](flutter-docs://api/material/PopupMenuThemeData) popupMenuTheme, required [ProgressIndicatorThemeData](flutter-docs://api/material/ProgressIndicatorThemeData) progressIndicatorTheme, required [RadioThemeData](flutter-docs://api/material/RadioThemeData) radioTheme, required [SearchBarThemeData](flutter-docs://api/material/SearchBarThemeData) searchBarTheme, required [SearchViewThemeData](flutter-docs://api/material/SearchViewThemeData) searchViewTheme, required [SegmentedButtonThemeData](flutter-docs://api/material/SegmentedButtonThemeData) segmentedButtonTheme, required [SliderThemeData](flutter-docs://api/material/SliderThemeData) sliderTheme, required [SnackBarThemeData](flutter-docs://api/material/SnackBarThemeData) snackBarTheme, required [SwitchThemeData](flutter-docs://api/material/SwitchThemeData) switchTheme, required [TabBarThemeData](flutter-docs://api/material/TabBarThemeData) tabBarTheme, required [TextButtonThemeData](flutter-docs://api/material/TextButtonThemeData) textButtonTheme, required [TextSelectionThemeData](flutter-docs://api/material/TextSelectionThemeData) textSelectionTheme, required [TimePickerThemeData](flutter-docs://api/material/TimePickerThemeData) timePickerTheme, required [ToggleButtonsThemeData](flutter-docs://api/material/ToggleButtonsThemeData) toggleButtonsTheme, required [TooltipThemeData](flutter-docs://api/material/TooltipThemeData) tooltipTheme, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use OverflowBar instead. ' 'This feature was deprecated after v3.21.0-10.0.pre.') [ButtonBarThemeData](flutter-docs://api/material/ButtonBarThemeData)? buttonBarTheme, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use DialogThemeData.backgroundColor instead. ' 'This feature was deprecated after v3.27.0-0.1.pre.') required [Color](flutter-docs://api/dart-ui/Color) dialogBackgroundColor, @[Deprecated](flutter-docs://api/dart-core/Deprecated/Deprecated)('Use TabBarThemeData.indicatorColor instead. ' 'This feature was deprecated after v3.28.0-1.0.pre.') required [Color](flutter-docs://api/dart-ui/Color) indicatorColor})
Create a [ThemeData](flutter-docs://api/material/ThemeData) given a set of exact values. Most values must be
specified. They all must also be non-null except for
`cupertinoOverrideTheme`, and deprecated members.


## Properties

[actionIconTheme](flutter-docs://api/material/ThemeData/actionIconTheme) → [ActionIconThemeData](flutter-docs://api/material/ActionIconThemeData)?
A theme for customizing icons of [BackButtonIcon](flutter-docs://api/material/BackButtonIcon), [CloseButtonIcon](flutter-docs://api/material/CloseButtonIcon),
[DrawerButtonIcon](flutter-docs://api/material/DrawerButtonIcon), or [EndDrawerButtonIcon](flutter-docs://api/material/EndDrawerButtonIcon).


[adaptationMap](flutter-docs://api/material/ThemeData/adaptationMap) → [Map](flutter-docs://api/dart-core/Map)<[Type](flutter-docs://api/dart-core/Type), [Adaptation](flutter-docs://api/material/Adaptation)<[Object](flutter-docs://api/dart-core/Object)>>
A map which contains the adaptations for the theme. The entry's key is the
type of the adaptation; the value is the adaptation itself.


[appBarTheme](flutter-docs://api/material/ThemeData/appBarTheme) → [AppBarThemeData](flutter-docs://api/material/AppBarThemeData)
A theme for customizing the color, elevation, brightness, iconTheme and
textTheme of [AppBar](flutter-docs://api/material/AppBar) s.


[applyElevationOverlayColor](flutter-docs://api/material/ThemeData/applyElevationOverlayColor) → [bool](flutter-docs://api/dart-core/bool)
Apply a semi-transparent overlay color on Material surfaces to indicate
elevation for dark themes.


[badgeTheme](flutter-docs://api/material/ThemeData/badgeTheme) → [BadgeThemeData](flutter-docs://api/material/BadgeThemeData)
A theme for customizing the color of [Badge](flutter-docs://api/material/Badge) s.


[bannerTheme](flutter-docs://api/material/ThemeData/bannerTheme) → [MaterialBannerThemeData](flutter-docs://api/material/MaterialBannerThemeData)
A theme for customizing the color and text style of a [MaterialBanner](flutter-docs://api/material/MaterialBanner).


[bottomAppBarTheme](flutter-docs://api/material/ThemeData/bottomAppBarTheme) → [BottomAppBarThemeData](flutter-docs://api/material/BottomAppBarThemeData)
A theme for customizing the shape, elevation, and color of a [BottomAppBar](flutter-docs://api/material/BottomAppBar).


[bottomNavigationBarTheme](flutter-docs://api/material/ThemeData/bottomNavigationBarTheme) → [BottomNavigationBarThemeData](flutter-docs://api/material/BottomNavigationBarThemeData)
A theme for customizing the appearance and layout of [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar) widgets.


[bottomSheetTheme](flutter-docs://api/material/ThemeData/bottomSheetTheme) → [BottomSheetThemeData](flutter-docs://api/material/BottomSheetThemeData)
A theme for customizing the color, elevation, and shape of a bottom sheet.


[brightness](flutter-docs://api/material/ThemeData/brightness) → [Brightness](flutter-docs://api/dart-ui/Brightness)
The overall theme brightness.


[buttonBarTheme](flutter-docs://api/material/ThemeData/buttonBarTheme) → [ButtonBarThemeData](flutter-docs://api/material/ButtonBarThemeData)
A theme for customizing the appearance and layout of [ButtonBar](flutter-docs://api/material/ButtonBar) widgets.


[buttonTheme](flutter-docs://api/material/ThemeData/buttonTheme) → [ButtonThemeData](flutter-docs://api/material/ButtonThemeData)
Defines the default configuration of button widgets, like [DropdownButton](flutter-docs://api/material/DropdownButton) and [ButtonBar](flutter-docs://api/material/ButtonBar).


[canvasColor](flutter-docs://api/material/ThemeData/canvasColor) → [Color](flutter-docs://api/dart-ui/Color)
The default color of [MaterialType.canvas](flutter-docs://api/material/MaterialType) [Material](flutter-docs://api/material/Material).


[cardColor](flutter-docs://api/material/ThemeData/cardColor) → [Color](flutter-docs://api/dart-ui/Color)
The color of [Material](flutter-docs://api/material/Material) when it is used as a [Card](flutter-docs://api/material/Card).


[cardTheme](flutter-docs://api/material/ThemeData/cardTheme) → [CardThemeData](flutter-docs://api/material/CardThemeData)
The colors and styles used to render [Card](flutter-docs://api/material/Card).


[carouselViewTheme](flutter-docs://api/material/ThemeData/carouselViewTheme) → [CarouselViewThemeData](flutter-docs://api/material/CarouselViewThemeData)
A theme for customizing the appearance and layout of [CarouselView](flutter-docs://api/material/CarouselView) widgets.


[checkboxTheme](flutter-docs://api/material/ThemeData/checkboxTheme) → [CheckboxThemeData](flutter-docs://api/material/CheckboxThemeData)
A theme for customizing the appearance and layout of [Checkbox](flutter-docs://api/material/Checkbox) widgets.


[chipTheme](flutter-docs://api/material/ThemeData/chipTheme) → [ChipThemeData](flutter-docs://api/material/ChipThemeData)
The colors and styles used to render [Chip](flutter-docs://api/material/Chip) s.


[colorScheme](flutter-docs://api/material/ThemeData/colorScheme) → [ColorScheme](flutter-docs://api/material/ColorScheme)
A set of 45 colors based on the
[Material spec](https://m3.material.io/styles/color/the-color-system/color-roles) that can be used to configure the color properties of most components.


[cupertinoOverrideTheme](flutter-docs://api/material/ThemeData/cupertinoOverrideTheme) → [NoDefaultCupertinoThemeData](flutter-docs://api/cupertino/NoDefaultCupertinoThemeData)?
Components of the [CupertinoThemeData](flutter-docs://api/cupertino/CupertinoThemeData) to override from the Material
[ThemeData](flutter-docs://api/material/ThemeData) adaptation.


[dataTableTheme](flutter-docs://api/material/ThemeData/dataTableTheme) → [DataTableThemeData](flutter-docs://api/material/DataTableThemeData)
A theme for customizing the appearance and layout of [DataTable](flutter-docs://api/material/DataTable) widgets.


[datePickerTheme](flutter-docs://api/material/ThemeData/datePickerTheme) → [DatePickerThemeData](flutter-docs://api/material/DatePickerThemeData)
A theme for customizing the appearance and layout of [DatePickerDialog](flutter-docs://api/material/DatePickerDialog) widgets.


[dialogBackgroundColor](flutter-docs://api/material/ThemeData/dialogBackgroundColor) → [Color](flutter-docs://api/dart-ui/Color)
The background color of [Dialog](flutter-docs://api/material/Dialog) elements.


[dialogTheme](flutter-docs://api/material/ThemeData/dialogTheme) → [DialogThemeData](flutter-docs://api/material/DialogThemeData)
A theme for customizing the shape of a dialog.


[disabledColor](flutter-docs://api/material/ThemeData/disabledColor) → [Color](flutter-docs://api/dart-ui/Color)
The color used for widgets that are inoperative, regardless of
their state. For example, a disabled checkbox (which may be
checked or unchecked).


[dividerColor](flutter-docs://api/material/ThemeData/dividerColor) → [Color](flutter-docs://api/dart-ui/Color)
The color of [Divider](flutter-docs://api/material/Divider) s and [PopupMenuDivider](flutter-docs://api/material/PopupMenuDivider) s, also used
between [ListTile](flutter-docs://api/material/ListTile) s, between rows in [DataTable](flutter-docs://api/material/DataTable) s, and so forth.


[dividerTheme](flutter-docs://api/material/ThemeData/dividerTheme) → [DividerThemeData](flutter-docs://api/material/DividerThemeData)
A theme for customizing the color, thickness, and indents of [Divider](flutter-docs://api/material/Divider) s,
[VerticalDivider](flutter-docs://api/material/VerticalDivider) s, etc.


[drawerTheme](flutter-docs://api/material/ThemeData/drawerTheme) → [DrawerThemeData](flutter-docs://api/material/DrawerThemeData)
A theme for customizing the appearance and layout of [Drawer](flutter-docs://api/material/Drawer) widgets.


[dropdownMenuTheme](flutter-docs://api/material/ThemeData/dropdownMenuTheme) → [DropdownMenuThemeData](flutter-docs://api/material/DropdownMenuThemeData)
A theme for customizing the appearance and layout of [DropdownMenu](flutter-docs://api/material/DropdownMenu) widgets.


[elevatedButtonTheme](flutter-docs://api/material/ThemeData/elevatedButtonTheme) → [ElevatedButtonThemeData](flutter-docs://api/material/ElevatedButtonThemeData)
A theme for customizing the appearance and internal layout of
[ElevatedButton](flutter-docs://api/material/ElevatedButton) s.


[expansionTileTheme](flutter-docs://api/material/ThemeData/expansionTileTheme) → [ExpansionTileThemeData](flutter-docs://api/material/ExpansionTileThemeData)
A theme for customizing the visual properties of [ExpansionTile](flutter-docs://api/material/ExpansionTile) s.


[extensions](flutter-docs://api/material/ThemeData/extensions) → [Map](flutter-docs://api/dart-core/Map)<[Object](flutter-docs://api/dart-core/Object), [ThemeExtension](flutter-docs://api/material/ThemeExtension)>
Arbitrary additions to this theme.


[filledButtonTheme](flutter-docs://api/material/ThemeData/filledButtonTheme) → [FilledButtonThemeData](flutter-docs://api/material/FilledButtonThemeData)
A theme for customizing the appearance and internal layout of
[FilledButton](flutter-docs://api/material/FilledButton) s.


[floatingActionButtonTheme](flutter-docs://api/material/ThemeData/floatingActionButtonTheme) → [FloatingActionButtonThemeData](flutter-docs://api/material/FloatingActionButtonThemeData)
A theme for customizing the shape, elevation, and color of a
[FloatingActionButton](flutter-docs://api/material/FloatingActionButton).


[focusColor](flutter-docs://api/material/ThemeData/focusColor) → [Color](flutter-docs://api/dart-ui/Color)
The focus color used indicate that a component has the input focus.


[hashCode](flutter-docs://api/material/ThemeData/hashCode) → [int](flutter-docs://api/dart-core/int)
The hash code for this object.

no setteroverride

[highlightColor](flutter-docs://api/material/ThemeData/highlightColor) → [Color](flutter-docs://api/dart-ui/Color)
The highlight color used during ink splash animations or to
indicate an item in a menu is selected.


[hintColor](flutter-docs://api/material/ThemeData/hintColor) → [Color](flutter-docs://api/dart-ui/Color)
The color to use for hint text or placeholder text, e.g. in
[TextField](flutter-docs://api/material/TextField) fields.


[hoverColor](flutter-docs://api/material/ThemeData/hoverColor) → [Color](flutter-docs://api/dart-ui/Color)
The hover color used to indicate when a pointer is hovering over a
component.


[iconButtonTheme](flutter-docs://api/material/ThemeData/iconButtonTheme) → [IconButtonThemeData](flutter-docs://api/material/IconButtonThemeData)
A theme for customizing the appearance and internal layout of
[IconButton](flutter-docs://api/material/IconButton) s.


[iconTheme](flutter-docs://api/material/ThemeData/iconTheme) → [IconThemeData](flutter-docs://api/widgets/IconThemeData)
An icon theme that contrasts with the card and canvas colors.


[indicatorColor](flutter-docs://api/material/ThemeData/indicatorColor) → [Color](flutter-docs://api/dart-ui/Color)
The color of the selected tab indicator in a tab bar.


[inputDecorationTheme](flutter-docs://api/material/ThemeData/inputDecorationTheme) → [InputDecorationThemeData](flutter-docs://api/material/InputDecorationThemeData)
The default [InputDecoration](flutter-docs://api/material/InputDecoration) values for [InputDecorator](flutter-docs://api/material/InputDecorator), [TextField](flutter-docs://api/material/TextField),
and [TextFormField](flutter-docs://api/material/TextFormField) are based on this theme.


[listTileTheme](flutter-docs://api/material/ThemeData/listTileTheme) → [ListTileThemeData](flutter-docs://api/material/ListTileThemeData)
A theme for customizing the appearance of [ListTile](flutter-docs://api/material/ListTile) widgets.


[materialTapTargetSize](flutter-docs://api/material/ThemeData/materialTapTargetSize) → [MaterialTapTargetSize](flutter-docs://api/material/MaterialTapTargetSize)
Configures the hit test size of certain Material widgets.


[menuBarTheme](flutter-docs://api/material/ThemeData/menuBarTheme) → [MenuBarThemeData](flutter-docs://api/material/MenuBarThemeData)
A theme for customizing the color, shape, elevation, and other [MenuStyle](flutter-docs://api/material/MenuStyle) aspects of the menu bar created by the [MenuBar](flutter-docs://api/material/MenuBar) widget.


[menuButtonTheme](flutter-docs://api/material/ThemeData/menuButtonTheme) → [MenuButtonThemeData](flutter-docs://api/material/MenuButtonThemeData)
A theme for customizing the color, shape, elevation, and text style of
cascading menu buttons created by [SubmenuButton](flutter-docs://api/material/SubmenuButton) or [MenuItemButton](flutter-docs://api/material/MenuItemButton).


[menuTheme](flutter-docs://api/material/ThemeData/menuTheme) → [MenuThemeData](flutter-docs://api/material/MenuThemeData)
A theme for customizing the color, shape, elevation, and other [MenuStyle](flutter-docs://api/material/MenuStyle) attributes of menus created by the [SubmenuButton](flutter-docs://api/material/SubmenuButton) widget.


[navigationBarTheme](flutter-docs://api/material/ThemeData/navigationBarTheme) → [NavigationBarThemeData](flutter-docs://api/material/NavigationBarThemeData)
A theme for customizing the background color, text style, and icon themes
of a [NavigationBar](flutter-docs://api/material/NavigationBar).


[navigationDrawerTheme](flutter-docs://api/material/ThemeData/navigationDrawerTheme) → [NavigationDrawerThemeData](flutter-docs://api/material/NavigationDrawerThemeData)
A theme for customizing the background color, text style, and icon themes
of a [NavigationDrawer](flutter-docs://api/material/NavigationDrawer).


[navigationRailTheme](flutter-docs://api/material/ThemeData/navigationRailTheme) → [NavigationRailThemeData](flutter-docs://api/material/NavigationRailThemeData)
A theme for customizing the background color, elevation, text style, and
icon themes of a [NavigationRail](flutter-docs://api/material/NavigationRail).


[outlinedButtonTheme](flutter-docs://api/material/ThemeData/outlinedButtonTheme) → [OutlinedButtonThemeData](flutter-docs://api/material/OutlinedButtonThemeData)
A theme for customizing the appearance and internal layout of
[OutlinedButton](flutter-docs://api/material/OutlinedButton) s.


[pageTransitionsTheme](flutter-docs://api/material/ThemeData/pageTransitionsTheme) → [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme)
Default [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) transitions per [TargetPlatform](flutter-docs://api/foundation/TargetPlatform).


[platform](flutter-docs://api/material/ThemeData/platform) → [TargetPlatform](flutter-docs://api/foundation/TargetPlatform)
The platform the material widgets should adapt to target.


[popupMenuTheme](flutter-docs://api/material/ThemeData/popupMenuTheme) → [PopupMenuThemeData](flutter-docs://api/material/PopupMenuThemeData)
A theme for customizing the color, shape, elevation, and text style of
popup menus.


[primaryColor](flutter-docs://api/material/ThemeData/primaryColor) → [Color](flutter-docs://api/dart-ui/Color)
The background color for major parts of the app (toolbars, tab bars, etc)


[primaryColorDark](flutter-docs://api/material/ThemeData/primaryColorDark) → [Color](flutter-docs://api/dart-ui/Color)
A darker version of the [primaryColor](flutter-docs://api/material/ThemeData/primaryColor).


[primaryColorLight](flutter-docs://api/material/ThemeData/primaryColorLight) → [Color](flutter-docs://api/dart-ui/Color)
A lighter version of the [primaryColor](flutter-docs://api/material/ThemeData/primaryColor).


[primaryIconTheme](flutter-docs://api/material/ThemeData/primaryIconTheme) → [IconThemeData](flutter-docs://api/widgets/IconThemeData)
An icon theme that contrasts with the primary color.


[primaryTextTheme](flutter-docs://api/material/ThemeData/primaryTextTheme) → [TextTheme](flutter-docs://api/material/TextTheme)
A text theme that contrasts with the primary color.


[progressIndicatorTheme](flutter-docs://api/material/ThemeData/progressIndicatorTheme) → [ProgressIndicatorThemeData](flutter-docs://api/material/ProgressIndicatorThemeData)
A theme for customizing the appearance and layout of [ProgressIndicator](flutter-docs://api/material/ProgressIndicator) widgets.


[radioTheme](flutter-docs://api/material/ThemeData/radioTheme) → [RadioThemeData](flutter-docs://api/material/RadioThemeData)
A theme for customizing the appearance and layout of [Radio](flutter-docs://api/material/Radio) widgets.


[runtimeType](flutter-docs://api/dart-core/Object/runtimeType) → [Type](flutter-docs://api/dart-core/Type)
A representation of the runtime type of the object.


[scaffoldBackgroundColor](flutter-docs://api/material/ThemeData/scaffoldBackgroundColor) → [Color](flutter-docs://api/dart-ui/Color)
The default color of the [Material](flutter-docs://api/material/Material) that underlies the [Scaffold](flutter-docs://api/material/Scaffold). The
background color for a typical material app or a page within the app.


[scrollbarTheme](flutter-docs://api/material/ThemeData/scrollbarTheme) → [ScrollbarThemeData](flutter-docs://api/material/ScrollbarThemeData)
A theme for customizing the colors, thickness, and shape of [Scrollbar](flutter-docs://api/material/Scrollbar) s.


[searchBarTheme](flutter-docs://api/material/ThemeData/searchBarTheme) → [SearchBarThemeData](flutter-docs://api/material/SearchBarThemeData)
A theme for customizing the appearance and layout of [SearchBar](flutter-docs://api/material/SearchBar) widgets.


[searchViewTheme](flutter-docs://api/material/ThemeData/searchViewTheme) → [SearchViewThemeData](flutter-docs://api/material/SearchViewThemeData)
A theme for customizing the appearance and layout of search views created by [SearchAnchor](flutter-docs://api/material/SearchAnchor) widgets.


[secondaryHeaderColor](flutter-docs://api/material/ThemeData/secondaryHeaderColor) → [Color](flutter-docs://api/dart-ui/Color)
The color of the header of a [PaginatedDataTable](flutter-docs://api/material/PaginatedDataTable) when there are selected rows.


[segmentedButtonTheme](flutter-docs://api/material/ThemeData/segmentedButtonTheme) → [SegmentedButtonThemeData](flutter-docs://api/material/SegmentedButtonThemeData)
A theme for customizing the appearance and layout of [SegmentedButton](flutter-docs://api/material/SegmentedButton) widgets.


[shadowColor](flutter-docs://api/material/ThemeData/shadowColor) → [Color](flutter-docs://api/dart-ui/Color)
The color that the [Material](flutter-docs://api/material/Material) widget uses to draw elevation shadows.


[sliderTheme](flutter-docs://api/material/ThemeData/sliderTheme) → [SliderThemeData](flutter-docs://api/material/SliderThemeData)
The colors and shapes used to render [Slider](flutter-docs://api/material/Slider).


[snackBarTheme](flutter-docs://api/material/ThemeData/snackBarTheme) → [SnackBarThemeData](flutter-docs://api/material/SnackBarThemeData)
A theme for customizing colors, shape, elevation, and behavior of a [SnackBar](flutter-docs://api/material/SnackBar).


[splashColor](flutter-docs://api/material/ThemeData/splashColor) → [Color](flutter-docs://api/dart-ui/Color)
The color of ink splashes.


[splashFactory](flutter-docs://api/material/ThemeData/splashFactory) → [InteractiveInkFeatureFactory](flutter-docs://api/material/InteractiveInkFeatureFactory)
Defines the appearance of ink splashes produces by [InkWell](flutter-docs://api/material/InkWell) and [InkResponse](flutter-docs://api/material/InkResponse).


[switchTheme](flutter-docs://api/material/ThemeData/switchTheme) → [SwitchThemeData](flutter-docs://api/material/SwitchThemeData)
A theme for customizing the appearance and layout of [Switch](flutter-docs://api/material/Switch) widgets.


[tabBarTheme](flutter-docs://api/material/ThemeData/tabBarTheme) → [TabBarThemeData](flutter-docs://api/material/TabBarThemeData)
A theme for customizing the size, shape, and color of the tab bar indicator.


[textButtonTheme](flutter-docs://api/material/ThemeData/textButtonTheme) → [TextButtonThemeData](flutter-docs://api/material/TextButtonThemeData)
A theme for customizing the appearance and internal layout of
[TextButton](flutter-docs://api/material/TextButton) s.


[textSelectionTheme](flutter-docs://api/material/ThemeData/textSelectionTheme) → [TextSelectionThemeData](flutter-docs://api/material/TextSelectionThemeData)
A theme for customizing the appearance and layout of [TextField](flutter-docs://api/material/TextField) widgets.


[textTheme](flutter-docs://api/material/ThemeData/textTheme) → [TextTheme](flutter-docs://api/material/TextTheme)
Text with a color that contrasts with the card and canvas colors.


[timePickerTheme](flutter-docs://api/material/ThemeData/timePickerTheme) → [TimePickerThemeData](flutter-docs://api/material/TimePickerThemeData)
A theme for customizing the appearance and layout of time picker widgets.


[toggleButtonsTheme](flutter-docs://api/material/ThemeData/toggleButtonsTheme) → [ToggleButtonsThemeData](flutter-docs://api/material/ToggleButtonsThemeData)
Defines the default configuration of [ToggleButtons](flutter-docs://api/material/ToggleButtons) widgets.


[tooltipTheme](flutter-docs://api/material/ThemeData/tooltipTheme) → [TooltipThemeData](flutter-docs://api/material/TooltipThemeData)
A theme for customizing the visual properties of [Tooltip](flutter-docs://api/material/Tooltip) s.


[typography](flutter-docs://api/material/ThemeData/typography) → [Typography](flutter-docs://api/material/Typography)
The color and geometry [TextTheme](flutter-docs://api/material/TextTheme) values used to configure [textTheme](flutter-docs://api/material/ThemeData/textTheme).


[unselectedWidgetColor](flutter-docs://api/material/ThemeData/unselectedWidgetColor) → [Color](flutter-docs://api/dart-ui/Color)
The color used for widgets in their inactive (but enabled)
state. For example, an unchecked checkbox. See also [disabledColor](flutter-docs://api/material/ThemeData/disabledColor).


[useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) → [bool](flutter-docs://api/dart-core/bool)
A temporary flag that can be used to opt-out of Material 3 features.


[visualDensity](flutter-docs://api/material/ThemeData/visualDensity) → [VisualDensity](flutter-docs://api/material/VisualDensity)
The density value for specifying the compactness of various UI components.


## Methods

[copyWith](flutter-docs://api/material/ThemeData/copyWith)({[Iterable](flutter-docs://api/dart-core/Iterable)<[Adaptation](flutter-docs://api/material/Adaptation)<[Object](flutter-docs://api/dart-core/Object)>>? adaptations, [bool](flutter-docs://api/dart-core/bool)? applyElevationOverlayColor, [NoDefaultCupertinoThemeData](flutter-docs://api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme, [Iterable](flutter-docs://api/dart-core/Iterable)<[ThemeExtension](flutter-docs://api/material/ThemeExtension)>? extensions, [Object](flutter-docs://api/dart-core/Object)? inputDecorationTheme, [MaterialTapTargetSize](flutter-docs://api/material/MaterialTapTargetSize)? materialTapTargetSize, [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme)? pageTransitionsTheme, [TargetPlatform](flutter-docs://api/foundation/TargetPlatform)? platform, [ScrollbarThemeData](flutter-docs://api/material/ScrollbarThemeData)? scrollbarTheme, [InteractiveInkFeatureFactory](flutter-docs://api/material/InteractiveInkFeatureFactory)? splashFactory, [VisualDensity](flutter-docs://api/material/VisualDensity)? visualDensity, [ColorScheme](flutter-docs://api/material/ColorScheme)? colorScheme, [Brightness](flutter-docs://api/dart-ui/Brightness)? brightness, [Color](flutter-docs://api/dart-ui/Color)? canvasColor, [Color](flutter-docs://api/dart-ui/Color)? cardColor, [Color](flutter-docs://api/dart-ui/Color)? disabledColor, [Color](flutter-docs://api/dart-ui/Color)? dividerColor, [Color](flutter-docs://api/dart-ui/Color)? focusColor, [Color](flutter-docs://api/dart-ui/Color)? highlightColor, [Color](flutter-docs://api/dart-ui/Color)? hintColor, [Color](flutter-docs://api/dart-ui/Color)? hoverColor, [Color](flutter-docs://api/dart-ui/Color)? primaryColor, [Color](flutter-docs://api/dart-ui/Color)? primaryColorDark, [Color](flutter-docs://api/dart-ui/Color)? primaryColorLight, [Color](flutter-docs://api/dart-ui/Color)? scaffoldBackgroundColor, [Color](flutter-docs://api/dart-ui/Color)? secondaryHeaderColor, [Color](flutter-docs://api/dart-ui/Color)? shadowColor, [Color](flutter-docs://api/dart-ui/Color)? splashColor, [Color](flutter-docs://api/dart-ui/Color)? unselectedWidgetColor, [IconThemeData](flutter-docs://api/widgets/IconThemeData)? iconTheme, [IconThemeData](flutter-docs://api/widgets/IconThemeData)? primaryIconTheme, [TextTheme](flutter-docs://api/material/TextTheme)? primaryTextTheme, [TextTheme](flutter-docs://api/material/TextTheme)? textTheme, [Typography](flutter-docs://api/material/Typography)? typography, [ActionIconThemeData](flutter-docs://api/material/ActionIconThemeData)? actionIconTheme, [Object](flutter-docs://api/dart-core/Object)? appBarTheme, [BadgeThemeData](flutter-docs://api/material/BadgeThemeData)? badgeTheme, [MaterialBannerThemeData](flutter-docs://api/material/MaterialBannerThemeData)? bannerTheme, [BottomAppBarThemeData](flutter-docs://api/material/BottomAppBarThemeData)? bottomAppBarTheme, [BottomNavigationBarThemeData](flutter-docs://api/material/BottomNavigationBarThemeData)? bottomNavigationBarTheme, [BottomSheetThemeData](flutter-docs://api/material/BottomSheetThemeData)? bottomSheetTheme, [ButtonThemeData](flutter-docs://api/material/ButtonThemeData)? buttonTheme, [CardThemeData](flutter-docs://api/material/CardThemeData)? cardTheme, [CarouselViewThemeData](flutter-docs://api/material/CarouselViewThemeData)? carouselViewTheme, [CheckboxThemeData](flutter-docs://api/material/CheckboxThemeData)? checkboxTheme, [ChipThemeData](flutter-docs://api/material/ChipThemeData)? chipTheme, [DataTableThemeData](flutter-docs://api/material/DataTableThemeData)? dataTableTheme, [DatePickerThemeData](flutter-docs://api/material/DatePickerThemeData)? datePickerTheme, [DialogThemeData](flutter-docs://api/material/DialogThemeData)? dialogTheme, [DividerThemeData](flutter-docs://api/material/DividerThemeData)? dividerTheme, [DrawerThemeData](flutter-docs://api/material/DrawerThemeData)? drawerTheme, [DropdownMenuThemeData](flutter-docs://api/material/DropdownMenuThemeData)? dropdownMenuTheme, [ElevatedButtonThemeData](flutter-docs://api/material/ElevatedButtonThemeData)? elevatedButtonTheme, [ExpansionTileThemeData](flutter-docs://api/material/ExpansionTileThemeData)? expansionTileTheme, [FilledButtonThemeData](flutter-docs://api/material/FilledButtonThemeData)? filledButtonTheme, [FloatingActionButtonThemeData](flutter-docs://api/material/FloatingActionButtonThemeData)? floatingActionButtonTheme, [IconButtonThemeData](flutter-docs://api/material/IconButtonThemeData)? iconButtonTheme, [ListTileThemeData](flutter-docs://api/material/ListTileThemeData)? listTileTheme, [MenuBarThemeData](flutter-docs://api/material/MenuBarThemeData)? menuBarTheme, [MenuButtonThemeData](flutter-docs://api/material/MenuButtonThemeData)? menuButtonTheme, [MenuThemeData](flutter-docs://api/material/MenuThemeData)? menuTheme, [NavigationBarThemeData](flutter-docs://api/material/NavigationBarThemeData)? navigationBarTheme, [NavigationDrawerThemeData](flutter-docs://api/material/NavigationDrawerThemeData)? navigationDrawerTheme, [NavigationRailThemeData](flutter-docs://api/material/NavigationRailThemeData)? navigationRailTheme, [OutlinedButtonThemeData](flutter-docs://api/material/OutlinedButtonThemeData)? outlinedButtonTheme, [PopupMenuThemeData](flutter-docs://api/material/PopupMenuThemeData)? popupMenuTheme, [ProgressIndicatorThemeData](flutter-docs://api/material/ProgressIndicatorThemeData)? progressIndicatorTheme, [RadioThemeData](flutter-docs://api/material/RadioThemeData)? radioTheme, [SearchBarThemeData](flutter-docs://api/material/SearchBarThemeData)? searchBarTheme, [SearchViewThemeData](flutter-docs://api/material/SearchViewThemeData)? searchViewTheme, [SegmentedButtonThemeData](flutter-docs://api/material/SegmentedButtonThemeData)? segmentedButtonTheme, [SliderThemeData](flutter-docs://api/material/SliderThemeData)? sliderTheme, [SnackBarThemeData](flutter-docs://api/material/SnackBarThemeData)? snackBarTheme, [SwitchThemeData](flutter-docs://api/material/SwitchThemeData)? switchTheme, [TabBarThemeData](flutter-docs://api/material/TabBarThemeData)? tabBarTheme, [TextButtonThemeData](flutter-docs://api/material/TextButtonThemeData)? textButtonTheme, [TextSelectionThemeData](flutter-docs://api/material/TextSelectionThemeData)? textSelectionTheme, [TimePickerThemeData](flutter-docs://api/material/TimePickerThemeData)? timePickerTheme, [ToggleButtonsThemeData](flutter-docs://api/material/ToggleButtonsThemeData)? toggleButtonsTheme, [TooltipThemeData](flutter-docs://api/material/TooltipThemeData)? tooltipTheme, [bool](flutter-docs://api/dart-core/bool)? useMaterial3, [ButtonBarThemeData](flutter-docs://api/material/ButtonBarThemeData)? buttonBarTheme, [Color](flutter-docs://api/dart-ui/Color)? dialogBackgroundColor, [Color](flutter-docs://api/dart-ui/Color)? indicatorColor}) → [ThemeData](flutter-docs://api/material/ThemeData)
Creates a copy of this theme but with the given fields replaced with the new values.

[debugFillProperties](flutter-docs://api/material/ThemeData/debugFillProperties)([DiagnosticPropertiesBuilder](flutter-docs://api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[extension](flutter-docs://api/material/ThemeData/extension)<T>() → T?
Used to obtain a particular [ThemeExtension](flutter-docs://api/material/ThemeExtension) from [extensions](flutter-docs://api/material/ThemeData/extensions).

[getAdaptation](flutter-docs://api/material/ThemeData/getAdaptation)<T>() → [Adaptation](flutter-docs://api/material/Adaptation)<T>?
Used to obtain a particular [Adaptation](flutter-docs://api/material/Adaptation) from [adaptationMap](flutter-docs://api/material/ThemeData/adaptationMap).

[noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod)([Invocation](flutter-docs://api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[toDiagnosticsNode](flutter-docs://api/foundation/Diagnosticable/toDiagnosticsNode)({[String](flutter-docs://api/dart-core/String)? name, [DiagnosticsTreeStyle](flutter-docs://api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](flutter-docs://api/foundation/DiagnosticsNode/toStringDeep).


[toString](flutter-docs://api/foundation/Diagnosticable/toString)({[DiagnosticLevel](flutter-docs://api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](flutter-docs://api/dart-core/String)
A string representation of this object.


[toStringShort](flutter-docs://api/foundation/Diagnosticable/toStringShort)() → [String](flutter-docs://api/dart-core/String)
A brief description of this object, usually just the [runtimeType](flutter-docs://api/dart-core/Object/runtimeType) and the
[hashCode](flutter-docs://api/dart-core/Object/hashCode).


## Operators

[operator ==](flutter-docs://api/material/ThemeData/operator_equals)([Object](flutter-docs://api/dart-core/Object) other) → [bool](flutter-docs://api/dart-core/bool)
The equality operator.


## Static Methods

[estimateBrightnessForColor](flutter-docs://api/material/ThemeData/estimateBrightnessForColor)([Color](flutter-docs://api/dart-ui/Color) color) → [Brightness](flutter-docs://api/dart-ui/Brightness)
Determines whether the given [Color](flutter-docs://api/dart-ui/Color) is [Brightness.light](flutter-docs://api/dart-ui/Brightness) or
[Brightness.dark](flutter-docs://api/dart-ui/Brightness).

[lerp](flutter-docs://api/material/ThemeData/lerp)([ThemeData](flutter-docs://api/material/ThemeData) a, [ThemeData](flutter-docs://api/material/ThemeData) b, [double](flutter-docs://api/dart-core/double) t) → [ThemeData](flutter-docs://api/material/ThemeData)
Linearly interpolate between two themes.

[localize](flutter-docs://api/material/ThemeData/localize)([ThemeData](flutter-docs://api/material/ThemeData) baseTheme, [TextTheme](flutter-docs://api/material/TextTheme) localTextGeometry) → [ThemeData](flutter-docs://api/material/ThemeData)
Returns a new theme built by merging the text geometry provided by the
`localTextGeometry` theme with the `baseTheme`.