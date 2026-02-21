# useMaterial3 property

[bool](flutter-docs://api/dart-core/bool) useMaterial3


A temporary flag that can be used to opt-out of Material 3 features.

This flag is *true* by default. If false, then components will
continue to use the colors, typography and other features of
Material 2.

In the long run this flag will be deprecated and eventually
only Material 3 will be supported. We recommend that applications
migrate to Material 3 as soon as that's practical. Until that migration
is complete, this flag can be set to false.

## Defaults

If a [ThemeData](flutter-docs://api/material/ThemeData) is *constructed* with [useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) set to true, then
some properties will get updated defaults. However, the [ThemeData.copyWith](flutter-docs://api/material/ThemeData/copyWith) method with [useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3) set to true will *not* change any of these properties in the resulting [ThemeData](flutter-docs://api/material/ThemeData).

| Property | Material 3 default | Material 2 default |
| --- | --- | --- |
| [colorScheme](flutter-docs://api/material/ThemeData/colorScheme) | M3 baseline light color scheme | M2 baseline light color scheme |
| [typography](flutter-docs://api/material/ThemeData/typography) | [Typography.material2021](flutter-docs://api/material/Typography/Typography.material2021) | [Typography.material2014](flutter-docs://api/material/Typography/Typography.material2014) |
| [splashFactory](flutter-docs://api/material/ThemeData/splashFactory) | [InkSparkle](flutter-docs://api/material/InkSparkle)* or [InkRipple](flutter-docs://api/material/InkRipple) | [InkSplash](flutter-docs://api/material/InkSplash) |


* if the target platform is Android and the app is not
running on the web, otherwise it will fallback to [InkRipple](flutter-docs://api/material/InkRipple).

If [brightness](flutter-docs://api/material/ThemeData/brightness) is [Brightness.dark](flutter-docs://api/dart-ui/Brightness) then the default color scheme will
be either the M3 baseline dark color scheme or the M2 baseline dark color
scheme depending on [useMaterial3](flutter-docs://api/material/ThemeData/useMaterial3).

## Affected widgets

This flag affects styles and components.

### Styles

- Color: [ColorScheme](flutter-docs://api/material/ColorScheme), [Material](flutter-docs://api/material/Material) (see table above)
- Shape: (see components below)
- Typography: [Typography](flutter-docs://api/material/Typography) (see table above)


### Components

- Badges: [Badge](flutter-docs://api/material/Badge)
- Bottom app bar: [BottomAppBar](flutter-docs://api/material/BottomAppBar)
- Bottom sheets: [BottomSheet](flutter-docs://api/material/BottomSheet)
- Buttons
  * Common buttons: [ElevatedButton](flutter-docs://api/material/ElevatedButton), [FilledButton](flutter-docs://api/material/FilledButton), [FilledButton.tonal](flutter-docs://api/material/FilledButton/FilledButton.tonal), [OutlinedButton](flutter-docs://api/material/OutlinedButton), [TextButton](flutter-docs://api/material/TextButton)
  * FAB: [FloatingActionButton](flutter-docs://api/material/FloatingActionButton), [FloatingActionButton.extended](flutter-docs://api/material/FloatingActionButton/FloatingActionButton.extended)
  * Icon buttons: [IconButton](flutter-docs://api/material/IconButton), [IconButton.filled](flutter-docs://api/material/IconButton/IconButton.filled) (*new*), [IconButton.filledTonal](flutter-docs://api/material/IconButton/IconButton.filledTonal), [IconButton.outlined](flutter-docs://api/material/IconButton/IconButton.outlined)
  * Segmented buttons: [SegmentedButton](flutter-docs://api/material/SegmentedButton) (replacing [ToggleButtons](flutter-docs://api/material/ToggleButtons))
- Cards: [Card](flutter-docs://api/material/Card)
- Checkbox: [Checkbox](flutter-docs://api/material/Checkbox), [CheckboxListTile](flutter-docs://api/material/CheckboxListTile)
- Chips:
  * [ActionChip](flutter-docs://api/material/ActionChip) (used for Assist and Suggestion chips),
  * [FilterChip](flutter-docs://api/material/FilterChip), [ChoiceChip](flutter-docs://api/material/ChoiceChip) (used for single selection filter chips),
  * [InputChip](flutter-docs://api/material/InputChip)
- Date pickers: [showDatePicker](flutter-docs://api/material/showDatePicker), [showDateRangePicker](flutter-docs://api/material/showDateRangePicker), [DatePickerDialog](flutter-docs://api/material/DatePickerDialog), [DateRangePickerDialog](flutter-docs://api/material/DateRangePickerDialog), [InputDatePickerFormField](flutter-docs://api/material/InputDatePickerFormField)
- Dialogs: [AlertDialog](flutter-docs://api/material/AlertDialog), [Dialog.fullscreen](flutter-docs://api/material/Dialog/Dialog.fullscreen)
- Divider: [Divider](flutter-docs://api/material/Divider), [VerticalDivider](flutter-docs://api/material/VerticalDivider)
- Lists: [ListTile](flutter-docs://api/material/ListTile)
- Menus: [MenuAnchor](flutter-docs://api/material/MenuAnchor), [DropdownMenu](flutter-docs://api/material/DropdownMenu), [MenuBar](flutter-docs://api/material/MenuBar)
- Navigation bar: [NavigationBar](flutter-docs://api/material/NavigationBar) (replacing [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar))
- Navigation drawer: [NavigationDrawer](flutter-docs://api/material/NavigationDrawer) (replacing [Drawer](flutter-docs://api/material/Drawer))
- Navigation rail: [NavigationRail](flutter-docs://api/material/NavigationRail)
- Progress indicators: [CircularProgressIndicator](flutter-docs://api/material/CircularProgressIndicator), [LinearProgressIndicator](flutter-docs://api/material/LinearProgressIndicator)
- Radio button: [Radio](flutter-docs://api/material/Radio), [RadioListTile](flutter-docs://api/material/RadioListTile)
- Search: [SearchBar](flutter-docs://api/material/SearchBar), [SearchAnchor](flutter-docs://api/material/SearchAnchor),
- Snack bar: [SnackBar](flutter-docs://api/material/SnackBar)
- Slider: [Slider](flutter-docs://api/material/Slider), [RangeSlider](flutter-docs://api/material/RangeSlider)
- Switch: [Switch](flutter-docs://api/material/Switch), [SwitchListTile](flutter-docs://api/material/SwitchListTile)
- Tabs: [TabBar](flutter-docs://api/material/TabBar), [TabBar.secondary](flutter-docs://api/material/TabBar/TabBar.secondary)
- TextFields: [TextField](flutter-docs://api/material/TextField) together with its [InputDecoration](flutter-docs://api/material/InputDecoration)
- Time pickers: [showTimePicker](flutter-docs://api/material/showTimePicker), [TimePickerDialog](flutter-docs://api/material/TimePickerDialog)
- Top app bar: [AppBar](flutter-docs://api/material/AppBar), [SliverAppBar](flutter-docs://api/material/SliverAppBar), [SliverAppBar.medium](flutter-docs://api/material/SliverAppBar/SliverAppBar.medium), [SliverAppBar.large](flutter-docs://api/material/SliverAppBar/SliverAppBar.large)


In addition, this flag enables features introduced in Android 12.

- Stretch overscroll: [MaterialScrollBehavior](flutter-docs://api/material/MaterialScrollBehavior)
- Ripple: `splashFactory` (see table above)


See also:

- [Material 3 specification](https://m3.material.io/).


## Implementation

```dart
final bool useMaterial3;
```