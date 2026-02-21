# showMenu<T> function

[Future](flutter-docs://api/dart-async/Future)<T?>showMenu<T>({
required [BuildContext](flutter-docs://api/widgets/BuildContext) context,
[RelativeRect](flutter-docs://api/rendering/RelativeRect)? position,
[PopupMenuPositionBuilder](flutter-docs://api/material/PopupMenuPositionBuilder)? positionBuilder,
required [List](flutter-docs://api/dart-core/List)<[PopupMenuEntry](flutter-docs://api/material/PopupMenuEntry)<T>> items,
T? initialValue,
[double](flutter-docs://api/dart-core/double)? elevation,
[Color](flutter-docs://api/dart-ui/Color)? shadowColor,
[Color](flutter-docs://api/dart-ui/Color)? surfaceTintColor,
[String](flutter-docs://api/dart-core/String)? semanticLabel,
[ShapeBorder](flutter-docs://api/painting/ShapeBorder)? shape,
[EdgeInsetsGeometry](flutter-docs://api/painting/EdgeInsetsGeometry)? menuPadding,
[Color](flutter-docs://api/dart-ui/Color)? color,
[bool](flutter-docs://api/dart-core/bool) useRootNavigator = false,
[BoxConstraints](flutter-docs://api/rendering/BoxConstraints)? constraints,
[Clip](flutter-docs://api/dart-ui/Clip) clipBehavior = Clip.none,
[RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings,
[AnimationStyle](flutter-docs://api/animation/AnimationStyle)? popUpAnimationStyle,
[bool](flutter-docs://api/dart-core/bool)? requestFocus,
})

Shows a popup menu that contains the `items` at `position`.

The `items` parameter must not be empty.

Only one of `position` or `positionBuilder` should be provided. Providing both
throws an assertion error. The `positionBuilder` is called at the time the
menu is shown to compute its position and every time the layout is updated,
which is useful when the position needs
to be determined at runtime based on the current layout.

If `initialValue` is specified then the first item with a matching value
will be highlighted and the value of `position` gives the rectangle whose
vertical center will be aligned with the vertical center of the highlighted
item (when possible).

If `initialValue` is not specified then the top of the menu will be aligned
with the top of the `position` rectangle.

In both cases, the menu position will be adjusted if necessary to fit on the
screen.

Horizontally, the menu is positioned so that it grows in the direction that
has the most room. For example, if the `position` describes a rectangle on
the left edge of the screen, then the left edge of the menu is aligned with
the left edge of the `position`, and the menu grows to the right. If both
edges of the `position` are equidistant from the opposite edge of the
screen, then the ambient [Directionality](flutter-docs://api/widgets/Directionality) is used as a tie-breaker,
preferring to grow in the reading direction.

The positioning of the `initialValue` at the `position` is implemented by
iterating over the `items` to find the first whose [PopupMenuEntry.represents](flutter-docs://api/material/PopupMenuEntry/represents) method returns true for `initialValue`, and then
summing the values of [PopupMenuEntry.height](flutter-docs://api/material/PopupMenuEntry/height) for all the preceding widgets
in the list.

The `elevation` argument specifies the z-coordinate at which to place the
menu. The elevation defaults to 8, the appropriate elevation for popup
menus.

The `context` argument is used to look up the [Navigator](flutter-docs://api/widgets/Navigator) and [Theme](flutter-docs://api/material/Theme) for
the menu. It is only used when the method is called. Its corresponding
widget can be safely removed from the tree before the popup menu is closed.

The `useRootNavigator` argument is used to determine whether to push the
menu to the [Navigator](flutter-docs://api/widgets/Navigator) furthest from or nearest to the given `context`. It
is `false` by default.

The `semanticLabel` argument is used by accessibility frameworks to
announce screen transitions when the menu is opened and closed. If this
label is not provided, it will default to [MaterialLocalizations.popupMenuLabel](flutter-docs://api/material/MaterialLocalizations/popupMenuLabel).

The `clipBehavior` argument is used to clip the shape of the menu. Defaults to [Clip.none](flutter-docs://api/dart-ui/Clip).

The `requestFocus` argument specifies whether the menu should request focus
when it appears. If it is null, [Navigator.requestFocus](flutter-docs://api/widgets/Navigator/requestFocus) is used instead.

See also:

- [PopupMenuItem](flutter-docs://api/material/PopupMenuItem), a popup menu entry for a single value.
- [PopupMenuDivider](flutter-docs://api/material/PopupMenuDivider), a popup menu entry that is just a horizontal line.
- [CheckedPopupMenuItem](flutter-docs://api/material/CheckedPopupMenuItem), a popup menu item with a checkmark.
- [PopupMenuButton](flutter-docs://api/material/PopupMenuButton), which provides an [IconButton](flutter-docs://api/material/IconButton) that shows a menu by
calling this method automatically.
- [SemanticsConfiguration.namesRoute](flutter-docs://api/semantics/SemanticsConfiguration/namesRoute), for a description of edge triggered
semantics.


## Implementation

```dart
Future<T?> showMenu<T>({
  required BuildContext context,
  RelativeRect? position,
  PopupMenuPositionBuilder? positionBuilder,
  required List<PopupMenuEntry<T>> items,
  T? initialValue,
  double? elevation,
  Color? shadowColor,
  Color? surfaceTintColor,
  String? semanticLabel,
  ShapeBorder? shape,
  EdgeInsetsGeometry? menuPadding,
  Color? color,
  bool useRootNavigator = false,
  BoxConstraints? constraints,
  Clip clipBehavior = Clip.none,
  RouteSettings? routeSettings,
  AnimationStyle? popUpAnimationStyle,
  bool? requestFocus,
}) {
  assert(items.isNotEmpty);
  assert(debugCheckHasMaterialLocalizations(context));
  assert(
    (position != null) != (positionBuilder != null),
    'Either position or positionBuilder must be provided.',
  );

  switch (Theme.of(context).platform) {
    case TargetPlatform.iOS:
    case TargetPlatform.macOS:
      break;
    case TargetPlatform.android:
    case TargetPlatform.fuchsia:
    case TargetPlatform.linux:
    case TargetPlatform.windows:
      semanticLabel ??= MaterialLocalizations.of(context).popupMenuLabel;
  }

  final List<GlobalKey> menuItemKeys = List<GlobalKey>.generate(
    items.length,
    (int index) => GlobalKey(),
  );
  final NavigatorState navigator = Navigator.of(context, rootNavigator: useRootNavigator);
  return navigator.push(
    _PopupMenuRoute<T>(
      position: position,
      positionBuilder: positionBuilder,
      items: items,
      itemKeys: menuItemKeys,
      initialValue: initialValue,
      elevation: elevation,
      shadowColor: shadowColor,
      surfaceTintColor: surfaceTintColor,
      semanticLabel: semanticLabel,
      barrierLabel: MaterialLocalizations.of(context).menuDismissLabel,
      shape: shape,
      menuPadding: menuPadding,
      color: color,
      capturedThemes: InheritedTheme.capture(from: context, to: navigator.context),
      constraints: constraints,
      clipBehavior: clipBehavior,
      settings: routeSettings,
      popUpAnimationStyle: popUpAnimationStyle,
      requestFocus: requestFocus,
    ),
  );
}
```