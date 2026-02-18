# hashCode property

1. @[override](mcp://flutter/api/dart-core/override)

[int](mcp://flutter/api/dart-core/int) get hashCode


The hash code for this object.

A hash code is a single integer which represents the state of the object
that affects [operator ==](mcp://flutter/api/material/ThemeData/operator_equals) comparisons.

All objects have hash codes.
The default hash code implemented by [Object](mcp://flutter/api/dart-core/Object) represents only the identity of the object,
the same way as the default [operator ==](mcp://flutter/api/material/ThemeData/operator_equals) implementation only considers objects
equal if they are identical (see [identityHashCode](mcp://flutter/api/dart-core/identityHashCode)).

If [operator ==](mcp://flutter/api/material/ThemeData/operator_equals) is overridden to use the object state instead,
the hash code must also be changed to represent that state,
otherwise the object cannot be used in hash based data structures
like the default [Set](mcp://flutter/api/dart-core/Set) and [Map](mcp://flutter/api/dart-core/Map) implementations.

Hash codes must be the same for objects that are equal to each other
according to [operator ==](mcp://flutter/api/material/ThemeData/operator_equals).
The hash code of an object should only change if the object changes
in a way that affects equality.
There are no further requirements for the hash codes.
They need not be consistent between executions of the same program
and there are no distribution guarantees.

Objects that are not equal are allowed to have the same hash code.
It is even technically allowed that all instances have the same hash code,
but if clashes happen too often,
it may reduce the efficiency of hash-based data structures
like [HashSet](mcp://flutter/api/dart-collection/HashSet) or [HashMap](mcp://flutter/api/dart-collection/HashMap).

If a subclass overrides [hashCode](mcp://flutter/api/material/ThemeData/hashCode), it should override the [operator ==](mcp://flutter/api/material/ThemeData/operator_equals) operator as well to maintain consistency.

## Implementation

```dart
@override
int get hashCode {
  final List<Object?> values = <Object?>[
    // For the sanity of the reader, make sure these properties are in the same
    // order in every place that they are separated by section comments (e.g.
    // GENERAL CONFIGURATION). Each section except for deprecations should be
    // alphabetical by symbol name.

    // GENERAL CONFIGURATION
    ...adaptationMap.keys,
    ...adaptationMap.values,
    applyElevationOverlayColor,
    cupertinoOverrideTheme,
    ...extensions.keys,
    ...extensions.values,
    inputDecorationTheme,
    materialTapTargetSize,
    pageTransitionsTheme,
    platform,
    scrollbarTheme,
    splashFactory,
    useMaterial3,
    visualDensity,
    // COLOR
    canvasColor,
    cardColor,
    colorScheme,
    disabledColor,
    dividerColor,
    focusColor,
    highlightColor,
    hintColor,
    hoverColor,
    primaryColor,
    primaryColorDark,
    primaryColorLight,
    scaffoldBackgroundColor,
    secondaryHeaderColor,
    shadowColor,
    splashColor,
    unselectedWidgetColor,
    // TYPOGRAPHY & ICONOGRAPHY
    iconTheme,
    primaryIconTheme,
    primaryTextTheme,
    textTheme,
    typography,
    // COMPONENT THEMES
    actionIconTheme,
    appBarTheme,
    badgeTheme,
    bannerTheme,
    bottomAppBarTheme,
    bottomNavigationBarTheme,
    bottomSheetTheme,
    buttonTheme,
    cardTheme,
    carouselViewTheme,
    checkboxTheme,
    chipTheme,
    dataTableTheme,
    datePickerTheme,
    dialogTheme,
    dividerTheme,
    drawerTheme,
    dropdownMenuTheme,
    elevatedButtonTheme,
    expansionTileTheme,
    filledButtonTheme,
    floatingActionButtonTheme,
    iconButtonTheme,
    listTileTheme,
    menuBarTheme,
    menuButtonTheme,
    menuTheme,
    navigationBarTheme,
    navigationDrawerTheme,
    navigationRailTheme,
    outlinedButtonTheme,
    popupMenuTheme,
    progressIndicatorTheme,
    radioTheme,
    searchBarTheme,
    searchViewTheme,
    segmentedButtonTheme,
    sliderTheme,
    snackBarTheme,
    switchTheme,
    tabBarTheme,
    textButtonTheme,
    textSelectionTheme,
    timePickerTheme,
    toggleButtonsTheme,
    tooltipTheme,
    // DEPRECATED (newest deprecations at the bottom)
    buttonBarTheme,
    dialogBackgroundColor,
    indicatorColor,
  ];
  return Object.hashAll(values);
}
```