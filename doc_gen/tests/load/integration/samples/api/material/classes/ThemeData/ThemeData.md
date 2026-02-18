# ThemeData class

Defines the configuration of the overall visual [Theme](mcp://flutter/api/material/Theme) for a [MaterialApp](mcp://flutter/api/material/MaterialApp) or a widget subtree within the app.

The [MaterialApp](mcp://flutter/api/material/MaterialApp) theme property can be used to configure the appearance
of the entire app. Widget subtrees within an app can override the app's
theme by including a [Theme](mcp://flutter/api/material/Theme) widget at the top of the subtree.

Widgets whose appearance should align with the overall theme can obtain the
current theme's configuration with [Theme.of](mcp://flutter/api/material/Theme/of). Material components typically
depend exclusively on the [colorScheme](mcp://flutter/api/material/ThemeData/colorScheme) and [textTheme](mcp://flutter/api/material/ThemeData/textTheme). These properties
are guaranteed to have non-null values.

The static [Theme.of](mcp://flutter/api/material/Theme/of) method finds the [ThemeData](mcp://flutter/api/material/ThemeData) value specified for the
nearest [BuildContext](mcp://flutter/api/widgets/BuildContext) ancestor. This lookup is inexpensive, essentially
just a single HashMap access. It can sometimes be a little confusing
because [Theme.of](mcp://flutter/api/material/Theme/of) can not see a [Theme](mcp://flutter/api/material/Theme) widget that is defined in the
current build method's context. To overcome that, create a new custom widget
for the subtree that appears below the new [Theme](mcp://flutter/api/material/Theme), or insert a widget
that creates a new BuildContext, like [Builder](mcp://flutter/api/widgets/Builder).

This example demonstrates how a typical [MaterialApp](mcp://flutter/api/material/MaterialApp) specifies
and uses a custom [Theme](mcp://flutter/api/material/Theme). The theme's [ColorScheme](mcp://flutter/api/material/ColorScheme) is based on a
single "seed" color and configures itself to match the platform's
current light or dark color configuration. The theme overrides the
default configuration of [FloatingActionButton](mcp://flutter/api/material/FloatingActionButton) to show how to
customize the appearance a class of components.


To create a local project with this code sample, run:  flutter create --sample=material.ThemeData.1 mysample

[Omitted code: Interactive sample]

See [material.io/design/color/](https://material.io/design/color/) for
more discussion on how to pick the right colors.

Mixed-in types
- [Diagnosticable](mcp://flutter/api/foundation/Diagnosticable)

Annotations
- @[immutable](mcp://flutter/api/meta/immutable)

## Constructors

[ThemeData](mcp://flutter/api/material/ThemeData/ThemeData)({[Iterable](mcp://flutter/api/dart-core/Iterable)<[Adaptation](mcp://flutter/api/material/Adaptation)<[Object](mcp://flutter/api/dart-core/Object)>>? adaptations, [bool](mcp://flutter/api/dart-core/bool)? applyElevationOverlayColor, [NoDefaultCupertinoThemeData](mcp://flutter/api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme, [Iterable](mcp://flutter/api/dart-core/Iterable)<[ThemeExtension](mcp://flutter/api/material/ThemeExtension)>? extensions, [Object](mcp://flutter/api/dart-core/Object)? inputDecorationTheme, [MaterialTapTargetSize](mcp://flutter/api/material/MaterialTapTargetSize)? materialTapTargetSize, [PageTransitionsTheme](mcp://flutter/api/material/PageTransitionsTheme)? pageTransitionsTheme, [TargetPlatform](mcp://flutter/api/foundation/TargetPlatform)? platform, [ScrollbarThemeData](mcp://flutter/api/material/ScrollbarThemeData)? scrollbarTheme, [InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)? splashFactory, [bool](mcp://flutter/api/dart-core/bool)? useMaterial3, [bool](mcp://flutter/api/dart-core/bool)? useSystemColors, [VisualDensity](mcp://flutter/api/material/VisualDensity)? visualDensity, [ColorScheme](mcp://flutter/api/material/ColorScheme)? colorScheme, [Brightness](mcp://flutter/api/dart-ui/Brightness)? brightness, [Color](mcp://flutter/api/dart-ui/Color)? colorSchemeSeed, [Color](mcp://flutter/api/dart-ui/Color)? canvasColor, [Color](mcp://flutter/api/dart-ui/Color)? cardColor, [Color](mcp://flutter/api/dart-ui/Color)? disabledColor, [Color](mcp://flutter/api/dart-ui/Color)? dividerColor, [Color](mcp://flutter/api/dart-ui/Color)? focusColor, [Color](mcp://flutter/api/dart-ui/Color)? highlightColor, [Color](mcp://flutter/api/dart-ui/Color)? hintColor, [Color](mcp://flutter/api/dart-ui/Color)? hoverColor, [Color](mcp://flutter/api/dart-ui/Color)? primaryColor, [Color](mcp://flutter/api/dart-ui/Color)? primaryColorDark, [Color](mcp://flutter/api/dart-ui/Color)? primaryColorLight, [MaterialColor](mcp://flutter/api/material/MaterialColor)? primarySwatch, [Color](mcp://flutter/api/dart-ui/Color)? scaffoldBackgroundColor, [Color](mcp://flutter/api/dart-ui/Color)? secondaryHeaderColor, [Color](mcp://flutter/api/dart-ui/Color)? shadowColor, [Color](mcp://flutter/api/dart-ui/Color)? splashColor, [Color](mcp://flutter/api/dart-ui/Color)? unselectedWidgetColor, [String](mcp://flutter/api/dart-core/String)? fontFamily, [List](mcp://flutter/api/dart-core/List)<[String](mcp://flutter/api/dart-core/String)>? fontFamilyFallback, [String](mcp://flutter/api/dart-core/String)? package, [IconThemeData](mcp://flutter/api/widgets/IconThemeData)? iconTheme, [IconThemeData](mcp://flutter/api/widgets/IconThemeData)? primaryIconTheme, [TextTheme](mcp://flutter/api/material/TextTheme)? primaryTextTheme, [TextTheme](mcp://flutter/api/material/TextTheme)? textTheme, [Typography](mcp://flutter/api/material/Typography)? typography, [ActionIconThemeData](mcp://flutter/api/material/ActionIconThemeData)? actionIconTheme, [Object](mcp://flutter/api/dart-core/Object)? appBarTheme, [BadgeThemeData](mcp://flutter/api/material/BadgeThemeData)? badgeTheme, [MaterialBannerThemeData](mcp://flutter/api/material/MaterialBannerThemeData)? bannerTheme, [BottomAppBarThemeData](mcp://flutter/api/material/BottomAppBarThemeData)? bottomAppBarTheme, [BottomNavigationBarThemeData](mcp://flutter/api/material/BottomNavigationBarThemeData)? bottomNavigationBarTheme, [BottomSheetThemeData](mcp://flutter/api/material/BottomSheetThemeData)? bottomSheetTheme, [ButtonThemeData](mcp://flutter/api/material/ButtonThemeData)? buttonTheme, [CardThemeData](mcp://flutter/api/material/CardThemeData)? cardTheme, [CarouselViewThemeData](mcp://flutter/api/material/CarouselViewThemeData)? carouselViewTheme, [CheckboxThemeData](mcp://flutter/api/material/CheckboxThemeData)? checkboxTheme, [ChipThemeData](mcp://flutter/api/material/ChipThemeData)? chipTheme, [DataTableThemeData](mcp://flutter/api/material/DataTableThemeData)? dataTableTheme, [DatePickerThemeData](mcp://flutter/api/material/DatePickerThemeData)? datePickerTheme, [DialogThemeData](mcp://flutter/api/material/DialogThemeData)? dialogTheme, [DividerThemeData](mcp://flutter/api/material/DividerThemeData)? dividerTheme, [DrawerThemeData](mcp://flutter/api/material/DrawerThemeData)? drawerTheme, [DropdownMenuThemeData](mcp://flutter/api/material/DropdownMenuThemeData)? dropdownMenuTheme, [ElevatedButtonThemeData](mcp://flutter/api/material/ElevatedButtonThemeData)? elevatedButtonTheme, [ExpansionTileThemeData](mcp://flutter/api/material/ExpansionTileThemeData)? expansionTileTheme, [FilledButtonThemeData](mcp://flutter/api/material/FilledButtonThemeData)? filledButtonTheme, [FloatingActionButtonThemeData](mcp://flutter/api/material/FloatingActionButtonThemeData)? floatingActionButtonTheme, [IconButtonThemeData](mcp://flutter/api/material/IconButtonThemeData)? iconButtonTheme, [ListTileThemeData](mcp://flutter/api/material/ListTileThemeData)? listTileTheme, [MenuBarThemeData](mcp://flutter/api/material/MenuBarThemeData)? menuBarTheme, [MenuButtonThemeData](mcp://flutter/api/material/MenuButtonThemeData)? menuButtonTheme, [MenuThemeData](mcp://flutter/api/material/MenuThemeData)? menuTheme, [NavigationBarThemeData](mcp://flutter/api/material/NavigationBarThemeData)? navigationBarTheme, [NavigationDrawerThemeData](mcp://flutter/api/material/NavigationDrawerThemeData)? navigationDrawerTheme, [NavigationRailThemeData](mcp://flutter/api/material/NavigationRailThemeData)? navigationRailTheme, [OutlinedButtonThemeData](mcp://flutter/api/material/OutlinedButtonThemeData)? outlinedButtonTheme, [PopupMenuThemeData](mcp://flutter/api/material/PopupMenuThemeData)? popupMenuTheme, [ProgressIndicatorThemeData](mcp://flutter/api/material/ProgressIndicatorThemeData)? progressIndicatorTheme, [RadioThemeData](mcp://flutter/api/material/RadioThemeData)? radioTheme, [SearchBarThemeData](mcp://flutter/api/material/SearchBarThemeData)? searchBarTheme, [SearchViewThemeData](mcp://flutter/api/material/SearchViewThemeData)? searchViewTheme, [SegmentedButtonThemeData](mcp://flutter/api/material/SegmentedButtonThemeData)? segmentedButtonTheme, [SliderThemeData](mcp://flutter/api/material/SliderThemeData)? sliderTheme, [SnackBarThemeData](mcp://flutter/api/material/SnackBarThemeData)? snackBarTheme, [SwitchThemeData](mcp://flutter/api/material/SwitchThemeData)? switchTheme, [TabBarThemeData](mcp://flutter/api/material/TabBarThemeData)? tabBarTheme, [TextButtonThemeData](mcp://flutter/api/material/TextButtonThemeData)? textButtonTheme, [TextSelectionThemeData](mcp://flutter/api/material/TextSelectionThemeData)? textSelectionTheme, [TimePickerThemeData](mcp://flutter/api/material/TimePickerThemeData)? timePickerTheme, [ToggleButtonsThemeData](mcp://flutter/api/material/ToggleButtonsThemeData)? toggleButtonsTheme, [TooltipThemeData](mcp://flutter/api/material/TooltipThemeData)? tooltipTheme, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use OverflowBar instead. ' 'This feature was deprecated after v3.21.0-10.0.pre.') [ButtonBarThemeData](mcp://flutter/api/material/ButtonBarThemeData)? buttonBarTheme, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use DialogThemeData.backgroundColor instead. ' 'This feature was deprecated after v3.27.0-0.1.pre.') [Color](mcp://flutter/api/dart-ui/Color)? dialogBackgroundColor, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use TabBarThemeData.indicatorColor instead. ' 'This feature was deprecated after v3.28.0-1.0.pre.') [Color](mcp://flutter/api/dart-ui/Color)? indicatorColor})
Create a [ThemeData](mcp://flutter/api/material/ThemeData) that's used to configure a [Theme](mcp://flutter/api/material/Theme).


[ThemeData.dark](mcp://flutter/api/material/ThemeData/ThemeData.dark)({[bool](mcp://flutter/api/dart-core/bool)? useMaterial3})
A default dark theme.


[ThemeData.fallback](mcp://flutter/api/material/ThemeData/ThemeData.fallback)({[bool](mcp://flutter/api/dart-core/bool)? useMaterial3})
The default color theme. Same as [ThemeData.light](mcp://flutter/api/material/ThemeData/ThemeData.light).


[ThemeData.from](mcp://flutter/api/material/ThemeData/ThemeData.from)({required [ColorScheme](mcp://flutter/api/material/ColorScheme) colorScheme, [TextTheme](mcp://flutter/api/material/TextTheme)? textTheme, [bool](mcp://flutter/api/dart-core/bool)? useMaterial3})
Create a [ThemeData](mcp://flutter/api/material/ThemeData) based on the colors in the given `colorScheme` and
text styles of the optional `textTheme`.


[ThemeData.light](mcp://flutter/api/material/ThemeData/ThemeData.light)({[bool](mcp://flutter/api/dart-core/bool)? useMaterial3})
A default light theme.


[ThemeData.raw](mcp://flutter/api/material/ThemeData/ThemeData.raw)({required [Map](mcp://flutter/api/dart-core/Map)<[Type](mcp://flutter/api/dart-core/Type), [Adaptation](mcp://flutter/api/material/Adaptation)<[Object](mcp://flutter/api/dart-core/Object)>> adaptationMap, required [bool](mcp://flutter/api/dart-core/bool) applyElevationOverlayColor, required [NoDefaultCupertinoThemeData](mcp://flutter/api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme, required [Map](mcp://flutter/api/dart-core/Map)<[Object](mcp://flutter/api/dart-core/Object), [ThemeExtension](mcp://flutter/api/material/ThemeExtension)> extensions, required [InputDecorationThemeData](mcp://flutter/api/material/InputDecorationThemeData) inputDecorationTheme, required [MaterialTapTargetSize](mcp://flutter/api/material/MaterialTapTargetSize) materialTapTargetSize, required [PageTransitionsTheme](mcp://flutter/api/material/PageTransitionsTheme) pageTransitionsTheme, required [TargetPlatform](mcp://flutter/api/foundation/TargetPlatform) platform, required [ScrollbarThemeData](mcp://flutter/api/material/ScrollbarThemeData) scrollbarTheme, required [InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory) splashFactory, required [bool](mcp://flutter/api/dart-core/bool) useMaterial3, required [VisualDensity](mcp://flutter/api/material/VisualDensity) visualDensity, required [ColorScheme](mcp://flutter/api/material/ColorScheme) colorScheme, required [Color](mcp://flutter/api/dart-ui/Color) canvasColor, required [Color](mcp://flutter/api/dart-ui/Color) cardColor, required [Color](mcp://flutter/api/dart-ui/Color) disabledColor, required [Color](mcp://flutter/api/dart-ui/Color) dividerColor, required [Color](mcp://flutter/api/dart-ui/Color) focusColor, required [Color](mcp://flutter/api/dart-ui/Color) highlightColor, required [Color](mcp://flutter/api/dart-ui/Color) hintColor, required [Color](mcp://flutter/api/dart-ui/Color) hoverColor, required [Color](mcp://flutter/api/dart-ui/Color) primaryColor, required [Color](mcp://flutter/api/dart-ui/Color) primaryColorDark, required [Color](mcp://flutter/api/dart-ui/Color) primaryColorLight, required [Color](mcp://flutter/api/dart-ui/Color) scaffoldBackgroundColor, required [Color](mcp://flutter/api/dart-ui/Color) secondaryHeaderColor, required [Color](mcp://flutter/api/dart-ui/Color) shadowColor, required [Color](mcp://flutter/api/dart-ui/Color) splashColor, required [Color](mcp://flutter/api/dart-ui/Color) unselectedWidgetColor, required [IconThemeData](mcp://flutter/api/widgets/IconThemeData) iconTheme, required [IconThemeData](mcp://flutter/api/widgets/IconThemeData) primaryIconTheme, required [TextTheme](mcp://flutter/api/material/TextTheme) primaryTextTheme, required [TextTheme](mcp://flutter/api/material/TextTheme) textTheme, required [Typography](mcp://flutter/api/material/Typography) typography, required [ActionIconThemeData](mcp://flutter/api/material/ActionIconThemeData)? actionIconTheme, required [AppBarThemeData](mcp://flutter/api/material/AppBarThemeData) appBarTheme, required [BadgeThemeData](mcp://flutter/api/material/BadgeThemeData) badgeTheme, required [MaterialBannerThemeData](mcp://flutter/api/material/MaterialBannerThemeData) bannerTheme, required [BottomAppBarThemeData](mcp://flutter/api/material/BottomAppBarThemeData) bottomAppBarTheme, required [BottomNavigationBarThemeData](mcp://flutter/api/material/BottomNavigationBarThemeData) bottomNavigationBarTheme, required [BottomSheetThemeData](mcp://flutter/api/material/BottomSheetThemeData) bottomSheetTheme, required [ButtonThemeData](mcp://flutter/api/material/ButtonThemeData) buttonTheme, required [CardThemeData](mcp://flutter/api/material/CardThemeData) cardTheme, required [CarouselViewThemeData](mcp://flutter/api/material/CarouselViewThemeData) carouselViewTheme, required [CheckboxThemeData](mcp://flutter/api/material/CheckboxThemeData) checkboxTheme, required [ChipThemeData](mcp://flutter/api/material/ChipThemeData) chipTheme, required [DataTableThemeData](mcp://flutter/api/material/DataTableThemeData) dataTableTheme, required [DatePickerThemeData](mcp://flutter/api/material/DatePickerThemeData) datePickerTheme, required [DialogThemeData](mcp://flutter/api/material/DialogThemeData) dialogTheme, required [DividerThemeData](mcp://flutter/api/material/DividerThemeData) dividerTheme, required [DrawerThemeData](mcp://flutter/api/material/DrawerThemeData) drawerTheme, required [DropdownMenuThemeData](mcp://flutter/api/material/DropdownMenuThemeData) dropdownMenuTheme, required [ElevatedButtonThemeData](mcp://flutter/api/material/ElevatedButtonThemeData) elevatedButtonTheme, required [ExpansionTileThemeData](mcp://flutter/api/material/ExpansionTileThemeData) expansionTileTheme, required [FilledButtonThemeData](mcp://flutter/api/material/FilledButtonThemeData) filledButtonTheme, required [FloatingActionButtonThemeData](mcp://flutter/api/material/FloatingActionButtonThemeData) floatingActionButtonTheme, required [IconButtonThemeData](mcp://flutter/api/material/IconButtonThemeData) iconButtonTheme, required [ListTileThemeData](mcp://flutter/api/material/ListTileThemeData) listTileTheme, required [MenuBarThemeData](mcp://flutter/api/material/MenuBarThemeData) menuBarTheme, required [MenuButtonThemeData](mcp://flutter/api/material/MenuButtonThemeData) menuButtonTheme, required [MenuThemeData](mcp://flutter/api/material/MenuThemeData) menuTheme, required [NavigationBarThemeData](mcp://flutter/api/material/NavigationBarThemeData) navigationBarTheme, required [NavigationDrawerThemeData](mcp://flutter/api/material/NavigationDrawerThemeData) navigationDrawerTheme, required [NavigationRailThemeData](mcp://flutter/api/material/NavigationRailThemeData) navigationRailTheme, required [OutlinedButtonThemeData](mcp://flutter/api/material/OutlinedButtonThemeData) outlinedButtonTheme, required [PopupMenuThemeData](mcp://flutter/api/material/PopupMenuThemeData) popupMenuTheme, required [ProgressIndicatorThemeData](mcp://flutter/api/material/ProgressIndicatorThemeData) progressIndicatorTheme, required [RadioThemeData](mcp://flutter/api/material/RadioThemeData) radioTheme, required [SearchBarThemeData](mcp://flutter/api/material/SearchBarThemeData) searchBarTheme, required [SearchViewThemeData](mcp://flutter/api/material/SearchViewThemeData) searchViewTheme, required [SegmentedButtonThemeData](mcp://flutter/api/material/SegmentedButtonThemeData) segmentedButtonTheme, required [SliderThemeData](mcp://flutter/api/material/SliderThemeData) sliderTheme, required [SnackBarThemeData](mcp://flutter/api/material/SnackBarThemeData) snackBarTheme, required [SwitchThemeData](mcp://flutter/api/material/SwitchThemeData) switchTheme, required [TabBarThemeData](mcp://flutter/api/material/TabBarThemeData) tabBarTheme, required [TextButtonThemeData](mcp://flutter/api/material/TextButtonThemeData) textButtonTheme, required [TextSelectionThemeData](mcp://flutter/api/material/TextSelectionThemeData) textSelectionTheme, required [TimePickerThemeData](mcp://flutter/api/material/TimePickerThemeData) timePickerTheme, required [ToggleButtonsThemeData](mcp://flutter/api/material/ToggleButtonsThemeData) toggleButtonsTheme, required [TooltipThemeData](mcp://flutter/api/material/TooltipThemeData) tooltipTheme, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use OverflowBar instead. ' 'This feature was deprecated after v3.21.0-10.0.pre.') [ButtonBarThemeData](mcp://flutter/api/material/ButtonBarThemeData)? buttonBarTheme, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use DialogThemeData.backgroundColor instead. ' 'This feature was deprecated after v3.27.0-0.1.pre.') required [Color](mcp://flutter/api/dart-ui/Color) dialogBackgroundColor, @[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use TabBarThemeData.indicatorColor instead. ' 'This feature was deprecated after v3.28.0-1.0.pre.') required [Color](mcp://flutter/api/dart-ui/Color) indicatorColor})
Create a [ThemeData](mcp://flutter/api/material/ThemeData) given a set of exact values. Most values must be
specified. They all must also be non-null except for
`cupertinoOverrideTheme`, and deprecated members.


## Properties

[actionIconTheme](mcp://flutter/api/material/ThemeData/actionIconTheme) → [ActionIconThemeData](mcp://flutter/api/material/ActionIconThemeData)?
A theme for customizing icons of [BackButtonIcon](mcp://flutter/api/material/BackButtonIcon), [CloseButtonIcon](mcp://flutter/api/material/CloseButtonIcon),
[DrawerButtonIcon](mcp://flutter/api/material/DrawerButtonIcon), or [EndDrawerButtonIcon](mcp://flutter/api/material/EndDrawerButtonIcon).


[adaptationMap](mcp://flutter/api/material/ThemeData/adaptationMap) → [Map](mcp://flutter/api/dart-core/Map)<[Type](mcp://flutter/api/dart-core/Type), [Adaptation](mcp://flutter/api/material/Adaptation)<[Object](mcp://flutter/api/dart-core/Object)>>
A map which contains the adaptations for the theme. The entry's key is the
type of the adaptation; the value is the adaptation itself.


[appBarTheme](mcp://flutter/api/material/ThemeData/appBarTheme) → [AppBarThemeData](mcp://flutter/api/material/AppBarThemeData)
A theme for customizing the color, elevation, brightness, iconTheme and
textTheme of [AppBar](mcp://flutter/api/material/AppBar) s.


[applyElevationOverlayColor](mcp://flutter/api/material/ThemeData/applyElevationOverlayColor) → [bool](mcp://flutter/api/dart-core/bool)
Apply a semi-transparent overlay color on Material surfaces to indicate
elevation for dark themes.


[badgeTheme](mcp://flutter/api/material/ThemeData/badgeTheme) → [BadgeThemeData](mcp://flutter/api/material/BadgeThemeData)
A theme for customizing the color of [Badge](mcp://flutter/api/material/Badge) s.


[bannerTheme](mcp://flutter/api/material/ThemeData/bannerTheme) → [MaterialBannerThemeData](mcp://flutter/api/material/MaterialBannerThemeData)
A theme for customizing the color and text style of a [MaterialBanner](mcp://flutter/api/material/MaterialBanner).


[bottomAppBarTheme](mcp://flutter/api/material/ThemeData/bottomAppBarTheme) → [BottomAppBarThemeData](mcp://flutter/api/material/BottomAppBarThemeData)
A theme for customizing the shape, elevation, and color of a [BottomAppBar](mcp://flutter/api/material/BottomAppBar).


[bottomNavigationBarTheme](mcp://flutter/api/material/ThemeData/bottomNavigationBarTheme) → [BottomNavigationBarThemeData](mcp://flutter/api/material/BottomNavigationBarThemeData)
A theme for customizing the appearance and layout of [BottomNavigationBar](mcp://flutter/api/material/BottomNavigationBar) widgets.


[bottomSheetTheme](mcp://flutter/api/material/ThemeData/bottomSheetTheme) → [BottomSheetThemeData](mcp://flutter/api/material/BottomSheetThemeData)
A theme for customizing the color, elevation, and shape of a bottom sheet.


[brightness](mcp://flutter/api/material/ThemeData/brightness) → [Brightness](mcp://flutter/api/dart-ui/Brightness)
The overall theme brightness.


[buttonBarTheme](mcp://flutter/api/material/ThemeData/buttonBarTheme) → [ButtonBarThemeData](mcp://flutter/api/material/ButtonBarThemeData)
A theme for customizing the appearance and layout of [ButtonBar](mcp://flutter/api/material/ButtonBar) widgets.


[buttonTheme](mcp://flutter/api/material/ThemeData/buttonTheme) → [ButtonThemeData](mcp://flutter/api/material/ButtonThemeData)
Defines the default configuration of button widgets, like [DropdownButton](mcp://flutter/api/material/DropdownButton) and [ButtonBar](mcp://flutter/api/material/ButtonBar).


[canvasColor](mcp://flutter/api/material/ThemeData/canvasColor) → [Color](mcp://flutter/api/dart-ui/Color)
The default color of [MaterialType.canvas](mcp://flutter/api/material/MaterialType) [Material](mcp://flutter/api/material/Material).


[cardColor](mcp://flutter/api/material/ThemeData/cardColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color of [Material](mcp://flutter/api/material/Material) when it is used as a [Card](mcp://flutter/api/material/Card).


[cardTheme](mcp://flutter/api/material/ThemeData/cardTheme) → [CardThemeData](mcp://flutter/api/material/CardThemeData)
The colors and styles used to render [Card](mcp://flutter/api/material/Card).


[carouselViewTheme](mcp://flutter/api/material/ThemeData/carouselViewTheme) → [CarouselViewThemeData](mcp://flutter/api/material/CarouselViewThemeData)
A theme for customizing the appearance and layout of [CarouselView](mcp://flutter/api/material/CarouselView) widgets.


[checkboxTheme](mcp://flutter/api/material/ThemeData/checkboxTheme) → [CheckboxThemeData](mcp://flutter/api/material/CheckboxThemeData)
A theme for customizing the appearance and layout of [Checkbox](mcp://flutter/api/material/Checkbox) widgets.


[chipTheme](mcp://flutter/api/material/ThemeData/chipTheme) → [ChipThemeData](mcp://flutter/api/material/ChipThemeData)
The colors and styles used to render [Chip](mcp://flutter/api/material/Chip) s.


[colorScheme](mcp://flutter/api/material/ThemeData/colorScheme) → [ColorScheme](mcp://flutter/api/material/ColorScheme)
A set of 45 colors based on the
[Material spec](https://m3.material.io/styles/color/the-color-system/color-roles) that can be used to configure the color properties of most components.


[cupertinoOverrideTheme](mcp://flutter/api/material/ThemeData/cupertinoOverrideTheme) → [NoDefaultCupertinoThemeData](mcp://flutter/api/cupertino/NoDefaultCupertinoThemeData)?
Components of the [CupertinoThemeData](mcp://flutter/api/cupertino/CupertinoThemeData) to override from the Material
[ThemeData](mcp://flutter/api/material/ThemeData) adaptation.


[dataTableTheme](mcp://flutter/api/material/ThemeData/dataTableTheme) → [DataTableThemeData](mcp://flutter/api/material/DataTableThemeData)
A theme for customizing the appearance and layout of [DataTable](mcp://flutter/api/material/DataTable) widgets.


[datePickerTheme](mcp://flutter/api/material/ThemeData/datePickerTheme) → [DatePickerThemeData](mcp://flutter/api/material/DatePickerThemeData)
A theme for customizing the appearance and layout of [DatePickerDialog](mcp://flutter/api/material/DatePickerDialog) widgets.


[dialogBackgroundColor](mcp://flutter/api/material/ThemeData/dialogBackgroundColor) → [Color](mcp://flutter/api/dart-ui/Color)
The background color of [Dialog](mcp://flutter/api/material/Dialog) elements.


[dialogTheme](mcp://flutter/api/material/ThemeData/dialogTheme) → [DialogThemeData](mcp://flutter/api/material/DialogThemeData)
A theme for customizing the shape of a dialog.


[disabledColor](mcp://flutter/api/material/ThemeData/disabledColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color used for widgets that are inoperative, regardless of
their state. For example, a disabled checkbox (which may be
checked or unchecked).


[dividerColor](mcp://flutter/api/material/ThemeData/dividerColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color of [Divider](mcp://flutter/api/material/Divider) s and [PopupMenuDivider](mcp://flutter/api/material/PopupMenuDivider) s, also used
between [ListTile](mcp://flutter/api/material/ListTile) s, between rows in [DataTable](mcp://flutter/api/material/DataTable) s, and so forth.


[dividerTheme](mcp://flutter/api/material/ThemeData/dividerTheme) → [DividerThemeData](mcp://flutter/api/material/DividerThemeData)
A theme for customizing the color, thickness, and indents of [Divider](mcp://flutter/api/material/Divider) s,
[VerticalDivider](mcp://flutter/api/material/VerticalDivider) s, etc.


[drawerTheme](mcp://flutter/api/material/ThemeData/drawerTheme) → [DrawerThemeData](mcp://flutter/api/material/DrawerThemeData)
A theme for customizing the appearance and layout of [Drawer](mcp://flutter/api/material/Drawer) widgets.


[dropdownMenuTheme](mcp://flutter/api/material/ThemeData/dropdownMenuTheme) → [DropdownMenuThemeData](mcp://flutter/api/material/DropdownMenuThemeData)
A theme for customizing the appearance and layout of [DropdownMenu](mcp://flutter/api/material/DropdownMenu) widgets.


[elevatedButtonTheme](mcp://flutter/api/material/ThemeData/elevatedButtonTheme) → [ElevatedButtonThemeData](mcp://flutter/api/material/ElevatedButtonThemeData)
A theme for customizing the appearance and internal layout of
[ElevatedButton](mcp://flutter/api/material/ElevatedButton) s.


[expansionTileTheme](mcp://flutter/api/material/ThemeData/expansionTileTheme) → [ExpansionTileThemeData](mcp://flutter/api/material/ExpansionTileThemeData)
A theme for customizing the visual properties of [ExpansionTile](mcp://flutter/api/material/ExpansionTile) s.


[extensions](mcp://flutter/api/material/ThemeData/extensions) → [Map](mcp://flutter/api/dart-core/Map)<[Object](mcp://flutter/api/dart-core/Object), [ThemeExtension](mcp://flutter/api/material/ThemeExtension)>
Arbitrary additions to this theme.


[filledButtonTheme](mcp://flutter/api/material/ThemeData/filledButtonTheme) → [FilledButtonThemeData](mcp://flutter/api/material/FilledButtonThemeData)
A theme for customizing the appearance and internal layout of
[FilledButton](mcp://flutter/api/material/FilledButton) s.


[floatingActionButtonTheme](mcp://flutter/api/material/ThemeData/floatingActionButtonTheme) → [FloatingActionButtonThemeData](mcp://flutter/api/material/FloatingActionButtonThemeData)
A theme for customizing the shape, elevation, and color of a
[FloatingActionButton](mcp://flutter/api/material/FloatingActionButton).


[focusColor](mcp://flutter/api/material/ThemeData/focusColor) → [Color](mcp://flutter/api/dart-ui/Color)
The focus color used indicate that a component has the input focus.


[hashCode](mcp://flutter/api/material/ThemeData/hashCode) → [int](mcp://flutter/api/dart-core/int)
The hash code for this object.

no setteroverride

[highlightColor](mcp://flutter/api/material/ThemeData/highlightColor) → [Color](mcp://flutter/api/dart-ui/Color)
The highlight color used during ink splash animations or to
indicate an item in a menu is selected.


[hintColor](mcp://flutter/api/material/ThemeData/hintColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color to use for hint text or placeholder text, e.g. in
[TextField](mcp://flutter/api/material/TextField) fields.


[hoverColor](mcp://flutter/api/material/ThemeData/hoverColor) → [Color](mcp://flutter/api/dart-ui/Color)
The hover color used to indicate when a pointer is hovering over a
component.


[iconButtonTheme](mcp://flutter/api/material/ThemeData/iconButtonTheme) → [IconButtonThemeData](mcp://flutter/api/material/IconButtonThemeData)
A theme for customizing the appearance and internal layout of
[IconButton](mcp://flutter/api/material/IconButton) s.


[iconTheme](mcp://flutter/api/material/ThemeData/iconTheme) → [IconThemeData](mcp://flutter/api/widgets/IconThemeData)
An icon theme that contrasts with the card and canvas colors.


[indicatorColor](mcp://flutter/api/material/ThemeData/indicatorColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color of the selected tab indicator in a tab bar.


[inputDecorationTheme](mcp://flutter/api/material/ThemeData/inputDecorationTheme) → [InputDecorationThemeData](mcp://flutter/api/material/InputDecorationThemeData)
The default [InputDecoration](mcp://flutter/api/material/InputDecoration) values for [InputDecorator](mcp://flutter/api/material/InputDecorator), [TextField](mcp://flutter/api/material/TextField),
and [TextFormField](mcp://flutter/api/material/TextFormField) are based on this theme.


[listTileTheme](mcp://flutter/api/material/ThemeData/listTileTheme) → [ListTileThemeData](mcp://flutter/api/material/ListTileThemeData)
A theme for customizing the appearance of [ListTile](mcp://flutter/api/material/ListTile) widgets.


[materialTapTargetSize](mcp://flutter/api/material/ThemeData/materialTapTargetSize) → [MaterialTapTargetSize](mcp://flutter/api/material/MaterialTapTargetSize)
Configures the hit test size of certain Material widgets.


[menuBarTheme](mcp://flutter/api/material/ThemeData/menuBarTheme) → [MenuBarThemeData](mcp://flutter/api/material/MenuBarThemeData)
A theme for customizing the color, shape, elevation, and other [MenuStyle](mcp://flutter/api/material/MenuStyle) aspects of the menu bar created by the [MenuBar](mcp://flutter/api/material/MenuBar) widget.


[menuButtonTheme](mcp://flutter/api/material/ThemeData/menuButtonTheme) → [MenuButtonThemeData](mcp://flutter/api/material/MenuButtonThemeData)
A theme for customizing the color, shape, elevation, and text style of
cascading menu buttons created by [SubmenuButton](mcp://flutter/api/material/SubmenuButton) or [MenuItemButton](mcp://flutter/api/material/MenuItemButton).


[menuTheme](mcp://flutter/api/material/ThemeData/menuTheme) → [MenuThemeData](mcp://flutter/api/material/MenuThemeData)
A theme for customizing the color, shape, elevation, and other [MenuStyle](mcp://flutter/api/material/MenuStyle) attributes of menus created by the [SubmenuButton](mcp://flutter/api/material/SubmenuButton) widget.


[navigationBarTheme](mcp://flutter/api/material/ThemeData/navigationBarTheme) → [NavigationBarThemeData](mcp://flutter/api/material/NavigationBarThemeData)
A theme for customizing the background color, text style, and icon themes
of a [NavigationBar](mcp://flutter/api/material/NavigationBar).


[navigationDrawerTheme](mcp://flutter/api/material/ThemeData/navigationDrawerTheme) → [NavigationDrawerThemeData](mcp://flutter/api/material/NavigationDrawerThemeData)
A theme for customizing the background color, text style, and icon themes
of a [NavigationDrawer](mcp://flutter/api/material/NavigationDrawer).


[navigationRailTheme](mcp://flutter/api/material/ThemeData/navigationRailTheme) → [NavigationRailThemeData](mcp://flutter/api/material/NavigationRailThemeData)
A theme for customizing the background color, elevation, text style, and
icon themes of a [NavigationRail](mcp://flutter/api/material/NavigationRail).


[outlinedButtonTheme](mcp://flutter/api/material/ThemeData/outlinedButtonTheme) → [OutlinedButtonThemeData](mcp://flutter/api/material/OutlinedButtonThemeData)
A theme for customizing the appearance and internal layout of
[OutlinedButton](mcp://flutter/api/material/OutlinedButton) s.


[pageTransitionsTheme](mcp://flutter/api/material/ThemeData/pageTransitionsTheme) → [PageTransitionsTheme](mcp://flutter/api/material/PageTransitionsTheme)
Default [MaterialPageRoute](mcp://flutter/api/material/MaterialPageRoute) transitions per [TargetPlatform](mcp://flutter/api/foundation/TargetPlatform).


[platform](mcp://flutter/api/material/ThemeData/platform) → [TargetPlatform](mcp://flutter/api/foundation/TargetPlatform)
The platform the material widgets should adapt to target.


[popupMenuTheme](mcp://flutter/api/material/ThemeData/popupMenuTheme) → [PopupMenuThemeData](mcp://flutter/api/material/PopupMenuThemeData)
A theme for customizing the color, shape, elevation, and text style of
popup menus.


[primaryColor](mcp://flutter/api/material/ThemeData/primaryColor) → [Color](mcp://flutter/api/dart-ui/Color)
The background color for major parts of the app (toolbars, tab bars, etc)


[primaryColorDark](mcp://flutter/api/material/ThemeData/primaryColorDark) → [Color](mcp://flutter/api/dart-ui/Color)
A darker version of the [primaryColor](mcp://flutter/api/material/ThemeData/primaryColor).


[primaryColorLight](mcp://flutter/api/material/ThemeData/primaryColorLight) → [Color](mcp://flutter/api/dart-ui/Color)
A lighter version of the [primaryColor](mcp://flutter/api/material/ThemeData/primaryColor).


[primaryIconTheme](mcp://flutter/api/material/ThemeData/primaryIconTheme) → [IconThemeData](mcp://flutter/api/widgets/IconThemeData)
An icon theme that contrasts with the primary color.


[primaryTextTheme](mcp://flutter/api/material/ThemeData/primaryTextTheme) → [TextTheme](mcp://flutter/api/material/TextTheme)
A text theme that contrasts with the primary color.


[progressIndicatorTheme](mcp://flutter/api/material/ThemeData/progressIndicatorTheme) → [ProgressIndicatorThemeData](mcp://flutter/api/material/ProgressIndicatorThemeData)
A theme for customizing the appearance and layout of [ProgressIndicator](mcp://flutter/api/material/ProgressIndicator) widgets.


[radioTheme](mcp://flutter/api/material/ThemeData/radioTheme) → [RadioThemeData](mcp://flutter/api/material/RadioThemeData)
A theme for customizing the appearance and layout of [Radio](mcp://flutter/api/material/Radio) widgets.


[runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) → [Type](mcp://flutter/api/dart-core/Type)
A representation of the runtime type of the object.


[scaffoldBackgroundColor](mcp://flutter/api/material/ThemeData/scaffoldBackgroundColor) → [Color](mcp://flutter/api/dart-ui/Color)
The default color of the [Material](mcp://flutter/api/material/Material) that underlies the [Scaffold](mcp://flutter/api/material/Scaffold). The
background color for a typical material app or a page within the app.


[scrollbarTheme](mcp://flutter/api/material/ThemeData/scrollbarTheme) → [ScrollbarThemeData](mcp://flutter/api/material/ScrollbarThemeData)
A theme for customizing the colors, thickness, and shape of [Scrollbar](mcp://flutter/api/material/Scrollbar) s.


[searchBarTheme](mcp://flutter/api/material/ThemeData/searchBarTheme) → [SearchBarThemeData](mcp://flutter/api/material/SearchBarThemeData)
A theme for customizing the appearance and layout of [SearchBar](mcp://flutter/api/material/SearchBar) widgets.


[searchViewTheme](mcp://flutter/api/material/ThemeData/searchViewTheme) → [SearchViewThemeData](mcp://flutter/api/material/SearchViewThemeData)
A theme for customizing the appearance and layout of search views created by [SearchAnchor](mcp://flutter/api/material/SearchAnchor) widgets.


[secondaryHeaderColor](mcp://flutter/api/material/ThemeData/secondaryHeaderColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color of the header of a [PaginatedDataTable](mcp://flutter/api/material/PaginatedDataTable) when there are selected rows.


[segmentedButtonTheme](mcp://flutter/api/material/ThemeData/segmentedButtonTheme) → [SegmentedButtonThemeData](mcp://flutter/api/material/SegmentedButtonThemeData)
A theme for customizing the appearance and layout of [SegmentedButton](mcp://flutter/api/material/SegmentedButton) widgets.


[shadowColor](mcp://flutter/api/material/ThemeData/shadowColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color that the [Material](mcp://flutter/api/material/Material) widget uses to draw elevation shadows.


[sliderTheme](mcp://flutter/api/material/ThemeData/sliderTheme) → [SliderThemeData](mcp://flutter/api/material/SliderThemeData)
The colors and shapes used to render [Slider](mcp://flutter/api/material/Slider).


[snackBarTheme](mcp://flutter/api/material/ThemeData/snackBarTheme) → [SnackBarThemeData](mcp://flutter/api/material/SnackBarThemeData)
A theme for customizing colors, shape, elevation, and behavior of a [SnackBar](mcp://flutter/api/material/SnackBar).


[splashColor](mcp://flutter/api/material/ThemeData/splashColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color of ink splashes.


[splashFactory](mcp://flutter/api/material/ThemeData/splashFactory) → [InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)
Defines the appearance of ink splashes produces by [InkWell](mcp://flutter/api/material/InkWell) and [InkResponse](mcp://flutter/api/material/InkResponse).


[switchTheme](mcp://flutter/api/material/ThemeData/switchTheme) → [SwitchThemeData](mcp://flutter/api/material/SwitchThemeData)
A theme for customizing the appearance and layout of [Switch](mcp://flutter/api/material/Switch) widgets.


[tabBarTheme](mcp://flutter/api/material/ThemeData/tabBarTheme) → [TabBarThemeData](mcp://flutter/api/material/TabBarThemeData)
A theme for customizing the size, shape, and color of the tab bar indicator.


[textButtonTheme](mcp://flutter/api/material/ThemeData/textButtonTheme) → [TextButtonThemeData](mcp://flutter/api/material/TextButtonThemeData)
A theme for customizing the appearance and internal layout of
[TextButton](mcp://flutter/api/material/TextButton) s.


[textSelectionTheme](mcp://flutter/api/material/ThemeData/textSelectionTheme) → [TextSelectionThemeData](mcp://flutter/api/material/TextSelectionThemeData)
A theme for customizing the appearance and layout of [TextField](mcp://flutter/api/material/TextField) widgets.


[textTheme](mcp://flutter/api/material/ThemeData/textTheme) → [TextTheme](mcp://flutter/api/material/TextTheme)
Text with a color that contrasts with the card and canvas colors.


[timePickerTheme](mcp://flutter/api/material/ThemeData/timePickerTheme) → [TimePickerThemeData](mcp://flutter/api/material/TimePickerThemeData)
A theme for customizing the appearance and layout of time picker widgets.


[toggleButtonsTheme](mcp://flutter/api/material/ThemeData/toggleButtonsTheme) → [ToggleButtonsThemeData](mcp://flutter/api/material/ToggleButtonsThemeData)
Defines the default configuration of [ToggleButtons](mcp://flutter/api/material/ToggleButtons) widgets.


[tooltipTheme](mcp://flutter/api/material/ThemeData/tooltipTheme) → [TooltipThemeData](mcp://flutter/api/material/TooltipThemeData)
A theme for customizing the visual properties of [Tooltip](mcp://flutter/api/material/Tooltip) s.


[typography](mcp://flutter/api/material/ThemeData/typography) → [Typography](mcp://flutter/api/material/Typography)
The color and geometry [TextTheme](mcp://flutter/api/material/TextTheme) values used to configure [textTheme](mcp://flutter/api/material/ThemeData/textTheme).


[unselectedWidgetColor](mcp://flutter/api/material/ThemeData/unselectedWidgetColor) → [Color](mcp://flutter/api/dart-ui/Color)
The color used for widgets in their inactive (but enabled)
state. For example, an unchecked checkbox. See also [disabledColor](mcp://flutter/api/material/ThemeData/disabledColor).


[useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) → [bool](mcp://flutter/api/dart-core/bool)
A temporary flag that can be used to opt-out of Material 3 features.


[visualDensity](mcp://flutter/api/material/ThemeData/visualDensity) → [VisualDensity](mcp://flutter/api/material/VisualDensity)
The density value for specifying the compactness of various UI components.


## Methods

[copyWith](mcp://flutter/api/material/ThemeData/copyWith)({[Iterable](mcp://flutter/api/dart-core/Iterable)<[Adaptation](mcp://flutter/api/material/Adaptation)<[Object](mcp://flutter/api/dart-core/Object)>>? adaptations, [bool](mcp://flutter/api/dart-core/bool)? applyElevationOverlayColor, [NoDefaultCupertinoThemeData](mcp://flutter/api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme, [Iterable](mcp://flutter/api/dart-core/Iterable)<[ThemeExtension](mcp://flutter/api/material/ThemeExtension)>? extensions, [Object](mcp://flutter/api/dart-core/Object)? inputDecorationTheme, [MaterialTapTargetSize](mcp://flutter/api/material/MaterialTapTargetSize)? materialTapTargetSize, [PageTransitionsTheme](mcp://flutter/api/material/PageTransitionsTheme)? pageTransitionsTheme, [TargetPlatform](mcp://flutter/api/foundation/TargetPlatform)? platform, [ScrollbarThemeData](mcp://flutter/api/material/ScrollbarThemeData)? scrollbarTheme, [InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)? splashFactory, [VisualDensity](mcp://flutter/api/material/VisualDensity)? visualDensity, [ColorScheme](mcp://flutter/api/material/ColorScheme)? colorScheme, [Brightness](mcp://flutter/api/dart-ui/Brightness)? brightness, [Color](mcp://flutter/api/dart-ui/Color)? canvasColor, [Color](mcp://flutter/api/dart-ui/Color)? cardColor, [Color](mcp://flutter/api/dart-ui/Color)? disabledColor, [Color](mcp://flutter/api/dart-ui/Color)? dividerColor, [Color](mcp://flutter/api/dart-ui/Color)? focusColor, [Color](mcp://flutter/api/dart-ui/Color)? highlightColor, [Color](mcp://flutter/api/dart-ui/Color)? hintColor, [Color](mcp://flutter/api/dart-ui/Color)? hoverColor, [Color](mcp://flutter/api/dart-ui/Color)? primaryColor, [Color](mcp://flutter/api/dart-ui/Color)? primaryColorDark, [Color](mcp://flutter/api/dart-ui/Color)? primaryColorLight, [Color](mcp://flutter/api/dart-ui/Color)? scaffoldBackgroundColor, [Color](mcp://flutter/api/dart-ui/Color)? secondaryHeaderColor, [Color](mcp://flutter/api/dart-ui/Color)? shadowColor, [Color](mcp://flutter/api/dart-ui/Color)? splashColor, [Color](mcp://flutter/api/dart-ui/Color)? unselectedWidgetColor, [IconThemeData](mcp://flutter/api/widgets/IconThemeData)? iconTheme, [IconThemeData](mcp://flutter/api/widgets/IconThemeData)? primaryIconTheme, [TextTheme](mcp://flutter/api/material/TextTheme)? primaryTextTheme, [TextTheme](mcp://flutter/api/material/TextTheme)? textTheme, [Typography](mcp://flutter/api/material/Typography)? typography, [ActionIconThemeData](mcp://flutter/api/material/ActionIconThemeData)? actionIconTheme, [Object](mcp://flutter/api/dart-core/Object)? appBarTheme, [BadgeThemeData](mcp://flutter/api/material/BadgeThemeData)? badgeTheme, [MaterialBannerThemeData](mcp://flutter/api/material/MaterialBannerThemeData)? bannerTheme, [BottomAppBarThemeData](mcp://flutter/api/material/BottomAppBarThemeData)? bottomAppBarTheme, [BottomNavigationBarThemeData](mcp://flutter/api/material/BottomNavigationBarThemeData)? bottomNavigationBarTheme, [BottomSheetThemeData](mcp://flutter/api/material/BottomSheetThemeData)? bottomSheetTheme, [ButtonThemeData](mcp://flutter/api/material/ButtonThemeData)? buttonTheme, [CardThemeData](mcp://flutter/api/material/CardThemeData)? cardTheme, [CarouselViewThemeData](mcp://flutter/api/material/CarouselViewThemeData)? carouselViewTheme, [CheckboxThemeData](mcp://flutter/api/material/CheckboxThemeData)? checkboxTheme, [ChipThemeData](mcp://flutter/api/material/ChipThemeData)? chipTheme, [DataTableThemeData](mcp://flutter/api/material/DataTableThemeData)? dataTableTheme, [DatePickerThemeData](mcp://flutter/api/material/DatePickerThemeData)? datePickerTheme, [DialogThemeData](mcp://flutter/api/material/DialogThemeData)? dialogTheme, [DividerThemeData](mcp://flutter/api/material/DividerThemeData)? dividerTheme, [DrawerThemeData](mcp://flutter/api/material/DrawerThemeData)? drawerTheme, [DropdownMenuThemeData](mcp://flutter/api/material/DropdownMenuThemeData)? dropdownMenuTheme, [ElevatedButtonThemeData](mcp://flutter/api/material/ElevatedButtonThemeData)? elevatedButtonTheme, [ExpansionTileThemeData](mcp://flutter/api/material/ExpansionTileThemeData)? expansionTileTheme, [FilledButtonThemeData](mcp://flutter/api/material/FilledButtonThemeData)? filledButtonTheme, [FloatingActionButtonThemeData](mcp://flutter/api/material/FloatingActionButtonThemeData)? floatingActionButtonTheme, [IconButtonThemeData](mcp://flutter/api/material/IconButtonThemeData)? iconButtonTheme, [ListTileThemeData](mcp://flutter/api/material/ListTileThemeData)? listTileTheme, [MenuBarThemeData](mcp://flutter/api/material/MenuBarThemeData)? menuBarTheme, [MenuButtonThemeData](mcp://flutter/api/material/MenuButtonThemeData)? menuButtonTheme, [MenuThemeData](mcp://flutter/api/material/MenuThemeData)? menuTheme, [NavigationBarThemeData](mcp://flutter/api/material/NavigationBarThemeData)? navigationBarTheme, [NavigationDrawerThemeData](mcp://flutter/api/material/NavigationDrawerThemeData)? navigationDrawerTheme, [NavigationRailThemeData](mcp://flutter/api/material/NavigationRailThemeData)? navigationRailTheme, [OutlinedButtonThemeData](mcp://flutter/api/material/OutlinedButtonThemeData)? outlinedButtonTheme, [PopupMenuThemeData](mcp://flutter/api/material/PopupMenuThemeData)? popupMenuTheme, [ProgressIndicatorThemeData](mcp://flutter/api/material/ProgressIndicatorThemeData)? progressIndicatorTheme, [RadioThemeData](mcp://flutter/api/material/RadioThemeData)? radioTheme, [SearchBarThemeData](mcp://flutter/api/material/SearchBarThemeData)? searchBarTheme, [SearchViewThemeData](mcp://flutter/api/material/SearchViewThemeData)? searchViewTheme, [SegmentedButtonThemeData](mcp://flutter/api/material/SegmentedButtonThemeData)? segmentedButtonTheme, [SliderThemeData](mcp://flutter/api/material/SliderThemeData)? sliderTheme, [SnackBarThemeData](mcp://flutter/api/material/SnackBarThemeData)? snackBarTheme, [SwitchThemeData](mcp://flutter/api/material/SwitchThemeData)? switchTheme, [TabBarThemeData](mcp://flutter/api/material/TabBarThemeData)? tabBarTheme, [TextButtonThemeData](mcp://flutter/api/material/TextButtonThemeData)? textButtonTheme, [TextSelectionThemeData](mcp://flutter/api/material/TextSelectionThemeData)? textSelectionTheme, [TimePickerThemeData](mcp://flutter/api/material/TimePickerThemeData)? timePickerTheme, [ToggleButtonsThemeData](mcp://flutter/api/material/ToggleButtonsThemeData)? toggleButtonsTheme, [TooltipThemeData](mcp://flutter/api/material/TooltipThemeData)? tooltipTheme, [bool](mcp://flutter/api/dart-core/bool)? useMaterial3, [ButtonBarThemeData](mcp://flutter/api/material/ButtonBarThemeData)? buttonBarTheme, [Color](mcp://flutter/api/dart-ui/Color)? dialogBackgroundColor, [Color](mcp://flutter/api/dart-ui/Color)? indicatorColor}) → [ThemeData](mcp://flutter/api/material/ThemeData)
Creates a copy of this theme but with the given fields replaced with the new values.

[debugFillProperties](mcp://flutter/api/material/ThemeData/debugFillProperties)([DiagnosticPropertiesBuilder](mcp://flutter/api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[extension](mcp://flutter/api/material/ThemeData/extension)<T>() → T?
Used to obtain a particular [ThemeExtension](mcp://flutter/api/material/ThemeExtension) from [extensions](mcp://flutter/api/material/ThemeData/extensions).

[getAdaptation](mcp://flutter/api/material/ThemeData/getAdaptation)<T>() → [Adaptation](mcp://flutter/api/material/Adaptation)<T>?
Used to obtain a particular [Adaptation](mcp://flutter/api/material/Adaptation) from [adaptationMap](mcp://flutter/api/material/ThemeData/adaptationMap).

[noSuchMethod](mcp://flutter/api/dart-core/Object/noSuchMethod)([Invocation](mcp://flutter/api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[toDiagnosticsNode](mcp://flutter/api/foundation/Diagnosticable/toDiagnosticsNode)({[String](mcp://flutter/api/dart-core/String)? name, [DiagnosticsTreeStyle](mcp://flutter/api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](mcp://flutter/api/foundation/DiagnosticsNode/toStringDeep).


[toString](mcp://flutter/api/foundation/Diagnosticable/toString)({[DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](mcp://flutter/api/dart-core/String)
A string representation of this object.


[toStringShort](mcp://flutter/api/foundation/Diagnosticable/toStringShort)() → [String](mcp://flutter/api/dart-core/String)
A brief description of this object, usually just the [runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) and the
[hashCode](mcp://flutter/api/dart-core/Object/hashCode).


## Operators

[operator ==](mcp://flutter/api/material/ThemeData/operator_equals)([Object](mcp://flutter/api/dart-core/Object) other) → [bool](mcp://flutter/api/dart-core/bool)
The equality operator.


## Static Methods

[estimateBrightnessForColor](mcp://flutter/api/material/ThemeData/estimateBrightnessForColor)([Color](mcp://flutter/api/dart-ui/Color) color) → [Brightness](mcp://flutter/api/dart-ui/Brightness)
Determines whether the given [Color](mcp://flutter/api/dart-ui/Color) is [Brightness.light](mcp://flutter/api/dart-ui/Brightness) or
[Brightness.dark](mcp://flutter/api/dart-ui/Brightness).

[lerp](mcp://flutter/api/material/ThemeData/lerp)([ThemeData](mcp://flutter/api/material/ThemeData) a, [ThemeData](mcp://flutter/api/material/ThemeData) b, [double](mcp://flutter/api/dart-core/double) t) → [ThemeData](mcp://flutter/api/material/ThemeData)
Linearly interpolate between two themes.

[localize](mcp://flutter/api/material/ThemeData/localize)([ThemeData](mcp://flutter/api/material/ThemeData) baseTheme, [TextTheme](mcp://flutter/api/material/TextTheme) localTextGeometry) → [ThemeData](mcp://flutter/api/material/ThemeData)
Returns a new theme built by merging the text geometry provided by the
`localTextGeometry` theme with the `baseTheme`.