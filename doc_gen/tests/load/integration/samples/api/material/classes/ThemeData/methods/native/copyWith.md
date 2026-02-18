# copyWith method

[ThemeData](mcp://flutter/api/material/ThemeData) copyWith({
[Iterable](mcp://flutter/api/dart-core/Iterable)<[Adaptation](mcp://flutter/api/material/Adaptation)<[Object](mcp://flutter/api/dart-core/Object)>>? adaptations,
[bool](mcp://flutter/api/dart-core/bool)? applyElevationOverlayColor,
[NoDefaultCupertinoThemeData](mcp://flutter/api/cupertino/NoDefaultCupertinoThemeData)? cupertinoOverrideTheme,
[Iterable](mcp://flutter/api/dart-core/Iterable)<[ThemeExtension](mcp://flutter/api/material/ThemeExtension)>? extensions,
[Object](mcp://flutter/api/dart-core/Object)? inputDecorationTheme,
[MaterialTapTargetSize](mcp://flutter/api/material/MaterialTapTargetSize)? materialTapTargetSize,
[PageTransitionsTheme](mcp://flutter/api/material/PageTransitionsTheme)? pageTransitionsTheme,
[TargetPlatform](mcp://flutter/api/foundation/TargetPlatform)? platform,
[ScrollbarThemeData](mcp://flutter/api/material/ScrollbarThemeData)? scrollbarTheme,
[InteractiveInkFeatureFactory](mcp://flutter/api/material/InteractiveInkFeatureFactory)? splashFactory,
[VisualDensity](mcp://flutter/api/material/VisualDensity)? visualDensity,
[ColorScheme](mcp://flutter/api/material/ColorScheme)? colorScheme,
[Brightness](mcp://flutter/api/dart-ui/Brightness)? brightness,
[Color](mcp://flutter/api/dart-ui/Color)? canvasColor,
[Color](mcp://flutter/api/dart-ui/Color)? cardColor,
[Color](mcp://flutter/api/dart-ui/Color)? disabledColor,
[Color](mcp://flutter/api/dart-ui/Color)? dividerColor,
[Color](mcp://flutter/api/dart-ui/Color)? focusColor,
[Color](mcp://flutter/api/dart-ui/Color)? highlightColor,
[Color](mcp://flutter/api/dart-ui/Color)? hintColor,
[Color](mcp://flutter/api/dart-ui/Color)? hoverColor,
[Color](mcp://flutter/api/dart-ui/Color)? primaryColor,
[Color](mcp://flutter/api/dart-ui/Color)? primaryColorDark,
[Color](mcp://flutter/api/dart-ui/Color)? primaryColorLight,
[Color](mcp://flutter/api/dart-ui/Color)? scaffoldBackgroundColor,
[Color](mcp://flutter/api/dart-ui/Color)? secondaryHeaderColor,
[Color](mcp://flutter/api/dart-ui/Color)? shadowColor,
[Color](mcp://flutter/api/dart-ui/Color)? splashColor,
[Color](mcp://flutter/api/dart-ui/Color)? unselectedWidgetColor,
[IconThemeData](mcp://flutter/api/widgets/IconThemeData)? iconTheme,
[IconThemeData](mcp://flutter/api/widgets/IconThemeData)? primaryIconTheme,
[TextTheme](mcp://flutter/api/material/TextTheme)? primaryTextTheme,
[TextTheme](mcp://flutter/api/material/TextTheme)? textTheme,
[Typography](mcp://flutter/api/material/Typography)? typography,
[ActionIconThemeData](mcp://flutter/api/material/ActionIconThemeData)? actionIconTheme,
[Object](mcp://flutter/api/dart-core/Object)? appBarTheme,
[BadgeThemeData](mcp://flutter/api/material/BadgeThemeData)? badgeTheme,
[MaterialBannerThemeData](mcp://flutter/api/material/MaterialBannerThemeData)? bannerTheme,
[BottomAppBarThemeData](mcp://flutter/api/material/BottomAppBarThemeData)? bottomAppBarTheme,
[BottomNavigationBarThemeData](mcp://flutter/api/material/BottomNavigationBarThemeData)? bottomNavigationBarTheme,
[BottomSheetThemeData](mcp://flutter/api/material/BottomSheetThemeData)? bottomSheetTheme,
[ButtonThemeData](mcp://flutter/api/material/ButtonThemeData)? buttonTheme,
[CardThemeData](mcp://flutter/api/material/CardThemeData)? cardTheme,
[CarouselViewThemeData](mcp://flutter/api/material/CarouselViewThemeData)? carouselViewTheme,
[CheckboxThemeData](mcp://flutter/api/material/CheckboxThemeData)? checkboxTheme,
[ChipThemeData](mcp://flutter/api/material/ChipThemeData)? chipTheme,
[DataTableThemeData](mcp://flutter/api/material/DataTableThemeData)? dataTableTheme,
[DatePickerThemeData](mcp://flutter/api/material/DatePickerThemeData)? datePickerTheme,
[DialogThemeData](mcp://flutter/api/material/DialogThemeData)? dialogTheme,
[DividerThemeData](mcp://flutter/api/material/DividerThemeData)? dividerTheme,
[DrawerThemeData](mcp://flutter/api/material/DrawerThemeData)? drawerTheme,
[DropdownMenuThemeData](mcp://flutter/api/material/DropdownMenuThemeData)? dropdownMenuTheme,
[ElevatedButtonThemeData](mcp://flutter/api/material/ElevatedButtonThemeData)? elevatedButtonTheme,
[ExpansionTileThemeData](mcp://flutter/api/material/ExpansionTileThemeData)? expansionTileTheme,
[FilledButtonThemeData](mcp://flutter/api/material/FilledButtonThemeData)? filledButtonTheme,
[FloatingActionButtonThemeData](mcp://flutter/api/material/FloatingActionButtonThemeData)? floatingActionButtonTheme,
[IconButtonThemeData](mcp://flutter/api/material/IconButtonThemeData)? iconButtonTheme,
[ListTileThemeData](mcp://flutter/api/material/ListTileThemeData)? listTileTheme,
[MenuBarThemeData](mcp://flutter/api/material/MenuBarThemeData)? menuBarTheme,
[MenuButtonThemeData](mcp://flutter/api/material/MenuButtonThemeData)? menuButtonTheme,
[MenuThemeData](mcp://flutter/api/material/MenuThemeData)? menuTheme,
[NavigationBarThemeData](mcp://flutter/api/material/NavigationBarThemeData)? navigationBarTheme,
[NavigationDrawerThemeData](mcp://flutter/api/material/NavigationDrawerThemeData)? navigationDrawerTheme,
[NavigationRailThemeData](mcp://flutter/api/material/NavigationRailThemeData)? navigationRailTheme,
[OutlinedButtonThemeData](mcp://flutter/api/material/OutlinedButtonThemeData)? outlinedButtonTheme,
[PopupMenuThemeData](mcp://flutter/api/material/PopupMenuThemeData)? popupMenuTheme,
[ProgressIndicatorThemeData](mcp://flutter/api/material/ProgressIndicatorThemeData)? progressIndicatorTheme,
[RadioThemeData](mcp://flutter/api/material/RadioThemeData)? radioTheme,
[SearchBarThemeData](mcp://flutter/api/material/SearchBarThemeData)? searchBarTheme,
[SearchViewThemeData](mcp://flutter/api/material/SearchViewThemeData)? searchViewTheme,
[SegmentedButtonThemeData](mcp://flutter/api/material/SegmentedButtonThemeData)? segmentedButtonTheme,
[SliderThemeData](mcp://flutter/api/material/SliderThemeData)? sliderTheme,
[SnackBarThemeData](mcp://flutter/api/material/SnackBarThemeData)? snackBarTheme,
[SwitchThemeData](mcp://flutter/api/material/SwitchThemeData)? switchTheme,
[TabBarThemeData](mcp://flutter/api/material/TabBarThemeData)? tabBarTheme,
[TextButtonThemeData](mcp://flutter/api/material/TextButtonThemeData)? textButtonTheme,
[TextSelectionThemeData](mcp://flutter/api/material/TextSelectionThemeData)? textSelectionTheme,
[TimePickerThemeData](mcp://flutter/api/material/TimePickerThemeData)? timePickerTheme,
[ToggleButtonsThemeData](mcp://flutter/api/material/ToggleButtonsThemeData)? toggleButtonsTheme,
[TooltipThemeData](mcp://flutter/api/material/TooltipThemeData)? tooltipTheme,
@[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use a ThemeData constructor (.from, .light, or .dark) instead. ' 'These constructors all have a useMaterial3 argument, ' 'and they set appropriate default values based on its value. ' 'See the useMaterial3 API documentation for full details. ' 'This feature was deprecated after v3.13.0-0.2.pre.') [bool](mcp://flutter/api/dart-core/bool)? useMaterial3,
@[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use OverflowBar instead. ' 'This feature was deprecated after v3.21.0-10.0.pre.') [ButtonBarThemeData](mcp://flutter/api/material/ButtonBarThemeData)? buttonBarTheme,
@[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use DialogThemeData.backgroundColor instead. ' 'This feature was deprecated after v3.27.0-0.1.pre.') [Color](mcp://flutter/api/dart-ui/Color)? dialogBackgroundColor,
@[Deprecated](mcp://flutter/api/dart-core/Deprecated/Deprecated)('Use TabBarThemeData.indicatorColor instead. ' 'This feature was deprecated after v3.28.0-1.0.pre.') [Color](mcp://flutter/api/dart-ui/Color)? indicatorColor,
})

Creates a copy of this theme but with the given fields replaced with the new values.

The `brightness` value is applied to the `colorScheme`.

## Implementation

```dart
ThemeData copyWith({
  // For the sanity of the reader, make sure these properties are in the same
  // order in every place that they are separated by section comments (e.g.
  // GENERAL CONFIGURATION). Each section except for deprecations should be
  // alphabetical by symbol name.

  // GENERAL CONFIGURATION
  Iterable<Adaptation<Object>>? adaptations,
  bool? applyElevationOverlayColor,
  NoDefaultCupertinoThemeData? cupertinoOverrideTheme,
  Iterable<ThemeExtension<dynamic>>? extensions,
  Object? inputDecorationTheme,
  MaterialTapTargetSize? materialTapTargetSize,
  PageTransitionsTheme? pageTransitionsTheme,
  TargetPlatform? platform,
  ScrollbarThemeData? scrollbarTheme,
  InteractiveInkFeatureFactory? splashFactory,
  VisualDensity? visualDensity,
  // COLOR
  ColorScheme? colorScheme,
  Brightness? brightness,
  // [colorScheme] is the preferred way to configure colors. The [Color] properties
  // listed below (as well as primarySwatch) will gradually be phased out, see
  // https://github.com/flutter/flutter/issues/91772.
  Color? canvasColor,
  Color? cardColor,
  Color? disabledColor,
  Color? dividerColor,
  Color? focusColor,
  Color? highlightColor,
  Color? hintColor,
  Color? hoverColor,
  Color? primaryColor,
  Color? primaryColorDark,
  Color? primaryColorLight,
  Color? scaffoldBackgroundColor,
  Color? secondaryHeaderColor,
  Color? shadowColor,
  Color? splashColor,
  Color? unselectedWidgetColor,
  // TYPOGRAPHY & ICONOGRAPHY
  IconThemeData? iconTheme,
  IconThemeData? primaryIconTheme,
  TextTheme? primaryTextTheme,
  TextTheme? textTheme,
  Typography? typography,
  // COMPONENT THEMES
  ActionIconThemeData? actionIconTheme,
  // TODO(huycozy): Change the parameter type to AppBarThemeData
  Object? appBarTheme,
  BadgeThemeData? badgeTheme,
  MaterialBannerThemeData? bannerTheme,
  BottomAppBarThemeData? bottomAppBarTheme,
  BottomNavigationBarThemeData? bottomNavigationBarTheme,
  BottomSheetThemeData? bottomSheetTheme,
  ButtonThemeData? buttonTheme,
  CardThemeData? cardTheme,
  CarouselViewThemeData? carouselViewTheme,
  CheckboxThemeData? checkboxTheme,
  ChipThemeData? chipTheme,
  DataTableThemeData? dataTableTheme,
  DatePickerThemeData? datePickerTheme,
  DialogThemeData? dialogTheme,
  DividerThemeData? dividerTheme,
  DrawerThemeData? drawerTheme,
  DropdownMenuThemeData? dropdownMenuTheme,
  ElevatedButtonThemeData? elevatedButtonTheme,
  ExpansionTileThemeData? expansionTileTheme,
  FilledButtonThemeData? filledButtonTheme,
  FloatingActionButtonThemeData? floatingActionButtonTheme,
  IconButtonThemeData? iconButtonTheme,
  ListTileThemeData? listTileTheme,
  MenuBarThemeData? menuBarTheme,
  MenuButtonThemeData? menuButtonTheme,
  MenuThemeData? menuTheme,
  NavigationBarThemeData? navigationBarTheme,
  NavigationDrawerThemeData? navigationDrawerTheme,
  NavigationRailThemeData? navigationRailTheme,
  OutlinedButtonThemeData? outlinedButtonTheme,
  PopupMenuThemeData? popupMenuTheme,
  ProgressIndicatorThemeData? progressIndicatorTheme,
  RadioThemeData? radioTheme,
  SearchBarThemeData? searchBarTheme,
  SearchViewThemeData? searchViewTheme,
  SegmentedButtonThemeData? segmentedButtonTheme,
  SliderThemeData? sliderTheme,
  SnackBarThemeData? snackBarTheme,
  SwitchThemeData? switchTheme,
  TabBarThemeData? tabBarTheme,
  TextButtonThemeData? textButtonTheme,
  TextSelectionThemeData? textSelectionTheme,
  TimePickerThemeData? timePickerTheme,
  ToggleButtonsThemeData? toggleButtonsTheme,
  TooltipThemeData? tooltipTheme,
  // DEPRECATED (newest deprecations at the bottom)
  @Deprecated(
    'Use a ThemeData constructor (.from, .light, or .dark) instead. '
    'These constructors all have a useMaterial3 argument, '
    'and they set appropriate default values based on its value. '
    'See the useMaterial3 API documentation for full details. '
    'This feature was deprecated after v3.13.0-0.2.pre.',
  )
  bool? useMaterial3,
  @Deprecated(
    'Use OverflowBar instead. '
    'This feature was deprecated after v3.21.0-10.0.pre.',
  )
  ButtonBarThemeData? buttonBarTheme,
  @Deprecated(
    'Use DialogThemeData.backgroundColor instead. '
    'This feature was deprecated after v3.27.0-0.1.pre.',
  )
  Color? dialogBackgroundColor,
  @Deprecated(
    'Use TabBarThemeData.indicatorColor instead. '
    'This feature was deprecated after v3.28.0-1.0.pre.',
  )
  Color? indicatorColor,
}) {
  cupertinoOverrideTheme = cupertinoOverrideTheme?.noDefault();

  // TODO(bleroux): Clean this up once the type of `inputDecorationTheme` is changed to `InputDecorationThemeData`
  if (inputDecorationTheme != null) {
    if (inputDecorationTheme is InputDecorationTheme) {
      inputDecorationTheme = inputDecorationTheme.data;
    } else if (inputDecorationTheme is! InputDecorationThemeData) {
      throw ArgumentError(
        'inputDecorationTheme must be either a InputDecorationThemeData or a InputDecorationTheme',
      );
    }
  }

  return ThemeData.raw(
    // For the sanity of the reader, make sure these properties are in the same
    // order in every place that they are separated by section comments (e.g.
    // GENERAL CONFIGURATION). Each section except for deprecations should be
    // alphabetical by symbol name.

    // GENERAL CONFIGURATION
    adaptationMap: adaptations != null ? _createAdaptationMap(adaptations) : adaptationMap,
    applyElevationOverlayColor: applyElevationOverlayColor ?? this.applyElevationOverlayColor,
    cupertinoOverrideTheme: cupertinoOverrideTheme ?? this.cupertinoOverrideTheme,
    extensions: (extensions != null) ? _themeExtensionIterableToMap(extensions) : this.extensions,
    inputDecorationTheme:
        inputDecorationTheme as InputDecorationThemeData? ?? this.inputDecorationTheme,
    materialTapTargetSize: materialTapTargetSize ?? this.materialTapTargetSize,
    pageTransitionsTheme: pageTransitionsTheme ?? this.pageTransitionsTheme,
    platform: platform ?? this.platform,
    scrollbarTheme: scrollbarTheme ?? this.scrollbarTheme,
    splashFactory: splashFactory ?? this.splashFactory,
    // When deprecated useMaterial3 removed, maintain `this.useMaterial3` here
    // for == evaluation.
    useMaterial3: useMaterial3 ?? this.useMaterial3,
    visualDensity: visualDensity ?? this.visualDensity,
    // COLOR
    canvasColor: canvasColor ?? this.canvasColor,
    cardColor: cardColor ?? this.cardColor,
    colorScheme: (colorScheme ?? this.colorScheme).copyWith(brightness: brightness),
    disabledColor: disabledColor ?? this.disabledColor,
    dividerColor: dividerColor ?? this.dividerColor,
    focusColor: focusColor ?? this.focusColor,
    highlightColor: highlightColor ?? this.highlightColor,
    hintColor: hintColor ?? this.hintColor,
    hoverColor: hoverColor ?? this.hoverColor,
    primaryColor: primaryColor ?? this.primaryColor,
    primaryColorDark: primaryColorDark ?? this.primaryColorDark,
    primaryColorLight: primaryColorLight ?? this.primaryColorLight,
    scaffoldBackgroundColor: scaffoldBackgroundColor ?? this.scaffoldBackgroundColor,
    secondaryHeaderColor: secondaryHeaderColor ?? this.secondaryHeaderColor,
    shadowColor: shadowColor ?? this.shadowColor,
    splashColor: splashColor ?? this.splashColor,
    unselectedWidgetColor: unselectedWidgetColor ?? this.unselectedWidgetColor,
    // TYPOGRAPHY & ICONOGRAPHY
    iconTheme: iconTheme ?? this.iconTheme,
    primaryIconTheme: primaryIconTheme ?? this.primaryIconTheme,
    primaryTextTheme: primaryTextTheme ?? this.primaryTextTheme,
    textTheme: textTheme ?? this.textTheme,
    typography: typography ?? this.typography,
    // COMPONENT THEMES
    actionIconTheme: actionIconTheme ?? this.actionIconTheme,
    // TODO(huycozy): Remove this check when appBarTheme is a AppBarThemeData
    appBarTheme: () {
      if (appBarTheme != null) {
        if (appBarTheme is AppBarTheme) {
          return appBarTheme.data;
        } else if (appBarTheme is! AppBarThemeData) {
          throw ArgumentError('appBarTheme must be either a AppBarThemeData or a AppBarTheme');
        }
      }
      return appBarTheme as AppBarThemeData? ?? this.appBarTheme;
    }(),
    badgeTheme: badgeTheme ?? this.badgeTheme,
    bannerTheme: bannerTheme ?? this.bannerTheme,
    bottomAppBarTheme: bottomAppBarTheme ?? this.bottomAppBarTheme,
    bottomNavigationBarTheme: bottomNavigationBarTheme ?? this.bottomNavigationBarTheme,
    bottomSheetTheme: bottomSheetTheme ?? this.bottomSheetTheme,
    buttonTheme: buttonTheme ?? this.buttonTheme,
    cardTheme: cardTheme ?? this.cardTheme,
    carouselViewTheme: carouselViewTheme ?? this.carouselViewTheme,
    checkboxTheme: checkboxTheme ?? this.checkboxTheme,
    chipTheme: chipTheme ?? this.chipTheme,
    dataTableTheme: dataTableTheme ?? this.dataTableTheme,
    datePickerTheme: datePickerTheme ?? this.datePickerTheme,
    dialogTheme: dialogTheme ?? this.dialogTheme,
    dividerTheme: dividerTheme ?? this.dividerTheme,
    drawerTheme: drawerTheme ?? this.drawerTheme,
    dropdownMenuTheme: dropdownMenuTheme ?? this.dropdownMenuTheme,
    elevatedButtonTheme: elevatedButtonTheme ?? this.elevatedButtonTheme,
    expansionTileTheme: expansionTileTheme ?? this.expansionTileTheme,
    filledButtonTheme: filledButtonTheme ?? this.filledButtonTheme,
    floatingActionButtonTheme: floatingActionButtonTheme ?? this.floatingActionButtonTheme,
    iconButtonTheme: iconButtonTheme ?? this.iconButtonTheme,
    listTileTheme: listTileTheme ?? this.listTileTheme,
    menuBarTheme: menuBarTheme ?? this.menuBarTheme,
    menuButtonTheme: menuButtonTheme ?? this.menuButtonTheme,
    menuTheme: menuTheme ?? this.menuTheme,
    navigationBarTheme: navigationBarTheme ?? this.navigationBarTheme,
    navigationDrawerTheme: navigationDrawerTheme ?? this.navigationDrawerTheme,
    navigationRailTheme: navigationRailTheme ?? this.navigationRailTheme,
    outlinedButtonTheme: outlinedButtonTheme ?? this.outlinedButtonTheme,
    popupMenuTheme: popupMenuTheme ?? this.popupMenuTheme,
    progressIndicatorTheme: progressIndicatorTheme ?? this.progressIndicatorTheme,
    radioTheme: radioTheme ?? this.radioTheme,
    searchBarTheme: searchBarTheme ?? this.searchBarTheme,
    searchViewTheme: searchViewTheme ?? this.searchViewTheme,
    segmentedButtonTheme: segmentedButtonTheme ?? this.segmentedButtonTheme,
    sliderTheme: sliderTheme ?? this.sliderTheme,
    snackBarTheme: snackBarTheme ?? this.snackBarTheme,
    switchTheme: switchTheme ?? this.switchTheme,
    tabBarTheme: tabBarTheme ?? this.tabBarTheme,
    textButtonTheme: textButtonTheme ?? this.textButtonTheme,
    textSelectionTheme: textSelectionTheme ?? this.textSelectionTheme,
    timePickerTheme: timePickerTheme ?? this.timePickerTheme,
    toggleButtonsTheme: toggleButtonsTheme ?? this.toggleButtonsTheme,
    tooltipTheme: tooltipTheme ?? this.tooltipTheme,
    // DEPRECATED (newest deprecations at the bottom)
    buttonBarTheme: buttonBarTheme ?? _buttonBarTheme,
    dialogBackgroundColor: dialogBackgroundColor ?? this.dialogBackgroundColor,
    indicatorColor: indicatorColor ?? this.indicatorColor,
  );
}
```