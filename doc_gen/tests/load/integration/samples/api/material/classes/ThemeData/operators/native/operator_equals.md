# operator == method

@[override](mcp://flutter/api/dart-core/override)
[bool](mcp://flutter/api/dart-core/bool) operator ==(
[Object](mcp://flutter/api/dart-core/Object) other
)


The equality operator.

The default behavior for all [Object](mcp://flutter/api/dart-core/Object) s is to return true if and
only if this object and `other` are the same object.

Override this method to specify a different equality relation on
a class. The overriding method must still be an equivalence relation.
That is, it must be:

- Total: It must return a boolean for all arguments. It should never throw.

- Reflexive: For all objects `o`, `o == o` must be true.

- Symmetric: For all objects `o1` and `o2`, `o1 == o2` and `o2 == o1` must
either both be true, or both be false.

- Transitive: For all objects `o1`, `o2`, and `o3`, if `o1 == o2` and `o2 == o3` are true, then `o1 == o3` must be true.

The method should also be consistent over time,
so whether two objects are equal should only change
if at least one of the objects was modified.

If a subclass overrides the equality operator, it should override
the [hashCode](mcp://flutter/api/material/ThemeData/hashCode) method as well to maintain consistency.

## Implementation

```dart
@override
bool operator ==(Object other) {
  if (other.runtimeType != runtimeType) {
    return false;
  }
  return other is ThemeData &&
      // For the sanity of the reader, make sure these properties are in the same
      // order in every place that they are separated by section comments (e.g.
      // GENERAL CONFIGURATION). Each section except for deprecations should be
      // alphabetical by symbol name.
      mapEquals(other.adaptationMap, adaptationMap) &&
      other.applyElevationOverlayColor == applyElevationOverlayColor &&
      other.cupertinoOverrideTheme == cupertinoOverrideTheme &&
      mapEquals(other.extensions, extensions) &&
      other.inputDecorationTheme == inputDecorationTheme &&
      other.materialTapTargetSize == materialTapTargetSize &&
      other.pageTransitionsTheme == pageTransitionsTheme &&
      other.platform == platform &&
      other.scrollbarTheme == scrollbarTheme &&
      other.splashFactory == splashFactory &&
      other.useMaterial3 == useMaterial3 &&
      other.visualDensity == visualDensity &&
      // COLOR
      other.canvasColor == canvasColor &&
      other.cardColor == cardColor &&
      other.colorScheme == colorScheme &&
      other.disabledColor == disabledColor &&
      other.dividerColor == dividerColor &&
      other.focusColor == focusColor &&
      other.highlightColor == highlightColor &&
      other.hintColor == hintColor &&
      other.hoverColor == hoverColor &&
      other.primaryColor == primaryColor &&
      other.primaryColorDark == primaryColorDark &&
      other.primaryColorLight == primaryColorLight &&
      other.scaffoldBackgroundColor == scaffoldBackgroundColor &&
      other.secondaryHeaderColor == secondaryHeaderColor &&
      other.shadowColor == shadowColor &&
      other.splashColor == splashColor &&
      other.unselectedWidgetColor == unselectedWidgetColor &&
      // TYPOGRAPHY & ICONOGRAPHY
      other.iconTheme == iconTheme &&
      other.primaryIconTheme == primaryIconTheme &&
      other.primaryTextTheme == primaryTextTheme &&
      other.textTheme == textTheme &&
      other.typography == typography &&
      // COMPONENT THEMES
      other.actionIconTheme == actionIconTheme &&
      other.appBarTheme == appBarTheme &&
      other.badgeTheme == badgeTheme &&
      other.bannerTheme == bannerTheme &&
      other.bottomAppBarTheme == bottomAppBarTheme &&
      other.bottomNavigationBarTheme == bottomNavigationBarTheme &&
      other.bottomSheetTheme == bottomSheetTheme &&
      other.buttonTheme == buttonTheme &&
      other.cardTheme == cardTheme &&
      other.carouselViewTheme == carouselViewTheme &&
      other.checkboxTheme == checkboxTheme &&
      other.chipTheme == chipTheme &&
      other.dataTableTheme == dataTableTheme &&
      other.datePickerTheme == datePickerTheme &&
      other.dialogTheme == dialogTheme &&
      other.dividerTheme == dividerTheme &&
      other.drawerTheme == drawerTheme &&
      other.dropdownMenuTheme == dropdownMenuTheme &&
      other.elevatedButtonTheme == elevatedButtonTheme &&
      other.expansionTileTheme == expansionTileTheme &&
      other.filledButtonTheme == filledButtonTheme &&
      other.floatingActionButtonTheme == floatingActionButtonTheme &&
      other.iconButtonTheme == iconButtonTheme &&
      other.listTileTheme == listTileTheme &&
      other.menuBarTheme == menuBarTheme &&
      other.menuButtonTheme == menuButtonTheme &&
      other.menuTheme == menuTheme &&
      other.navigationBarTheme == navigationBarTheme &&
      other.navigationDrawerTheme == navigationDrawerTheme &&
      other.navigationRailTheme == navigationRailTheme &&
      other.outlinedButtonTheme == outlinedButtonTheme &&
      other.popupMenuTheme == popupMenuTheme &&
      other.progressIndicatorTheme == progressIndicatorTheme &&
      other.radioTheme == radioTheme &&
      other.searchBarTheme == searchBarTheme &&
      other.searchViewTheme == searchViewTheme &&
      other.segmentedButtonTheme == segmentedButtonTheme &&
      other.sliderTheme == sliderTheme &&
      other.snackBarTheme == snackBarTheme &&
      other.switchTheme == switchTheme &&
      other.tabBarTheme == tabBarTheme &&
      other.textButtonTheme == textButtonTheme &&
      other.textSelectionTheme == textSelectionTheme &&
      other.timePickerTheme == timePickerTheme &&
      other.toggleButtonsTheme == toggleButtonsTheme &&
      other.tooltipTheme == tooltipTheme &&
      // DEPRECATED (newest deprecations at the bottom)
      other.buttonBarTheme == buttonBarTheme &&
      other.dialogBackgroundColor == dialogBackgroundColor &&
      other.indicatorColor == indicatorColor;
}
```