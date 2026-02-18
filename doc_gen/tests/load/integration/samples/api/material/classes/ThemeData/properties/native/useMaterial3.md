# useMaterial3 property

[bool](mcp://flutter/api/dart-core/bool) useMaterial3


A temporary flag that can be used to opt-out of Material 3 features.

This flag is *true* by default. If false, then components will
continue to use the colors, typography and other features of
Material 2.

In the long run this flag will be deprecated and eventually
only Material 3 will be supported. We recommend that applications
migrate to Material 3 as soon as that's practical. Until that migration
is complete, this flag can be set to false.

## Defaults

If a [ThemeData](mcp://flutter/api/material/ThemeData) is *constructed* with [useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) set to true, then
some properties will get updated defaults. However, the [ThemeData.copyWith](mcp://flutter/api/material/ThemeData/copyWith) method with [useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3) set to true will *not* change any of these properties in the resulting [ThemeData](mcp://flutter/api/material/ThemeData).

| Property | Material 3 default | Material 2 default |
| --- | --- | --- |
| [colorScheme](mcp://flutter/api/material/ThemeData/colorScheme) | M3 baseline light color scheme | M2 baseline light color scheme |
| [typography](mcp://flutter/api/material/ThemeData/typography) | [Typography.material2021](mcp://flutter/api/material/Typography/Typography.material2021) | [Typography.material2014](mcp://flutter/api/material/Typography/Typography.material2014) |
| [splashFactory](mcp://flutter/api/material/ThemeData/splashFactory) | [InkSparkle](mcp://flutter/api/material/InkSparkle)* or [InkRipple](mcp://flutter/api/material/InkRipple) | [InkSplash](mcp://flutter/api/material/InkSplash) |


* if the target platform is Android and the app is not
running on the web, otherwise it will fallback to [InkRipple](mcp://flutter/api/material/InkRipple).

If [brightness](mcp://flutter/api/material/ThemeData/brightness) is [Brightness.dark](mcp://flutter/api/dart-ui/Brightness) then the default color scheme will
be either the M3 baseline dark color scheme or the M2 baseline dark color
scheme depending on [useMaterial3](mcp://flutter/api/material/ThemeData/useMaterial3).

## Affected widgets

This flag affects styles and components.

### Styles

- Color: [ColorScheme](mcp://flutter/api/material/ColorScheme), [Material](mcp://flutter/api/material/Material) (see table above)
- Shape: (see components below)
- Typography: [Typography](mcp://flutter/api/material/Typography) (see table above)


### Components

- Badges: [Badge](mcp://flutter/api/material/Badge)
- Bottom app bar: [BottomAppBar](mcp://flutter/api/material/BottomAppBar)
- Bottom sheets: [BottomSheet](mcp://flutter/api/material/BottomSheet)
- Buttons
  * Common buttons: [ElevatedButton](mcp://flutter/api/material/ElevatedButton), [FilledButton](mcp://flutter/api/material/FilledButton), [FilledButton.tonal](mcp://flutter/api/material/FilledButton/FilledButton.tonal), [OutlinedButton](mcp://flutter/api/material/OutlinedButton), [TextButton](mcp://flutter/api/material/TextButton)
  * FAB: [FloatingActionButton](mcp://flutter/api/material/FloatingActionButton), [FloatingActionButton.extended](mcp://flutter/api/material/FloatingActionButton/FloatingActionButton.extended)
  * Icon buttons: [IconButton](mcp://flutter/api/material/IconButton), [IconButton.filled](mcp://flutter/api/material/IconButton/IconButton.filled) (*new*), [IconButton.filledTonal](mcp://flutter/api/material/IconButton/IconButton.filledTonal), [IconButton.outlined](mcp://flutter/api/material/IconButton/IconButton.outlined)
  * Segmented buttons: [SegmentedButton](mcp://flutter/api/material/SegmentedButton) (replacing [ToggleButtons](mcp://flutter/api/material/ToggleButtons))
- Cards: [Card](mcp://flutter/api/material/Card)
- Checkbox: [Checkbox](mcp://flutter/api/material/Checkbox), [CheckboxListTile](mcp://flutter/api/material/CheckboxListTile)
- Chips:
  * [ActionChip](mcp://flutter/api/material/ActionChip) (used for Assist and Suggestion chips),
  * [FilterChip](mcp://flutter/api/material/FilterChip), [ChoiceChip](mcp://flutter/api/material/ChoiceChip) (used for single selection filter chips),
  * [InputChip](mcp://flutter/api/material/InputChip)
- Date pickers: [showDatePicker](mcp://flutter/api/material/showDatePicker), [showDateRangePicker](mcp://flutter/api/material/showDateRangePicker), [DatePickerDialog](mcp://flutter/api/material/DatePickerDialog), [DateRangePickerDialog](mcp://flutter/api/material/DateRangePickerDialog), [InputDatePickerFormField](mcp://flutter/api/material/InputDatePickerFormField)
- Dialogs: [AlertDialog](mcp://flutter/api/material/AlertDialog), [Dialog.fullscreen](mcp://flutter/api/material/Dialog/Dialog.fullscreen)
- Divider: [Divider](mcp://flutter/api/material/Divider), [VerticalDivider](mcp://flutter/api/material/VerticalDivider)
- Lists: [ListTile](mcp://flutter/api/material/ListTile)
- Menus: [MenuAnchor](mcp://flutter/api/material/MenuAnchor), [DropdownMenu](mcp://flutter/api/material/DropdownMenu), [MenuBar](mcp://flutter/api/material/MenuBar)
- Navigation bar: [NavigationBar](mcp://flutter/api/material/NavigationBar) (replacing [BottomNavigationBar](mcp://flutter/api/material/BottomNavigationBar))
- Navigation drawer: [NavigationDrawer](mcp://flutter/api/material/NavigationDrawer) (replacing [Drawer](mcp://flutter/api/material/Drawer))
- Navigation rail: [NavigationRail](mcp://flutter/api/material/NavigationRail)
- Progress indicators: [CircularProgressIndicator](mcp://flutter/api/material/CircularProgressIndicator), [LinearProgressIndicator](mcp://flutter/api/material/LinearProgressIndicator)
- Radio button: [Radio](mcp://flutter/api/material/Radio), [RadioListTile](mcp://flutter/api/material/RadioListTile)
- Search: [SearchBar](mcp://flutter/api/material/SearchBar), [SearchAnchor](mcp://flutter/api/material/SearchAnchor),
- Snack bar: [SnackBar](mcp://flutter/api/material/SnackBar)
- Slider: [Slider](mcp://flutter/api/material/Slider), [RangeSlider](mcp://flutter/api/material/RangeSlider)
- Switch: [Switch](mcp://flutter/api/material/Switch), [SwitchListTile](mcp://flutter/api/material/SwitchListTile)
- Tabs: [TabBar](mcp://flutter/api/material/TabBar), [TabBar.secondary](mcp://flutter/api/material/TabBar/TabBar.secondary)
- TextFields: [TextField](mcp://flutter/api/material/TextField) together with its [InputDecoration](mcp://flutter/api/material/InputDecoration)
- Time pickers: [showTimePicker](mcp://flutter/api/material/showTimePicker), [TimePickerDialog](mcp://flutter/api/material/TimePickerDialog)
- Top app bar: [AppBar](mcp://flutter/api/material/AppBar), [SliverAppBar](mcp://flutter/api/material/SliverAppBar), [SliverAppBar.medium](mcp://flutter/api/material/SliverAppBar/SliverAppBar.medium), [SliverAppBar.large](mcp://flutter/api/material/SliverAppBar/SliverAppBar.large)


In addition, this flag enables features introduced in Android 12.

- Stretch overscroll: [MaterialScrollBehavior](mcp://flutter/api/material/MaterialScrollBehavior)
- Ripple: `splashFactory` (see table above)


See also:

- [Material 3 specification](https://m3.material.io/).


## Implementation

```dart
final bool useMaterial3;
```