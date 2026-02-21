# build method

@[override](flutter-docs://api/dart-core/override)
[Widget](flutter-docs://api/widgets/Widget) build(
[BuildContext](flutter-docs://api/widgets/BuildContext) context
)


Describes the part of the user interface represented by this widget.

The framework calls this method when this widget is inserted into the tree
in a given [BuildContext](flutter-docs://api/widgets/BuildContext) and when the dependencies of this widget change
(e.g., an [InheritedWidget](flutter-docs://api/widgets/InheritedWidget) referenced by this widget changes). This
method can potentially be called in every frame and should not have any side
effects beyond building a widget.

The framework replaces the subtree below this widget with the widget
returned by this method, either by updating the existing subtree or by
removing the subtree and inflating a new subtree, depending on whether the
widget returned by this method can update the root of the existing
subtree, as determined by calling [Widget.canUpdate](flutter-docs://api/widgets/Widget/canUpdate).

Typically implementations return a newly created constellation of widgets
that are configured with information from this widget's constructor and
from the given [BuildContext](flutter-docs://api/widgets/BuildContext).

The given [BuildContext](flutter-docs://api/widgets/BuildContext) contains information about the location in the
tree at which this widget is being built. For example, the context
provides the set of inherited widgets for this location in the tree. A
given widget might be built with multiple different [BuildContext](flutter-docs://api/widgets/BuildContext) arguments over time if the widget is moved around the tree or if the
widget is inserted into the tree in multiple places at once.

The implementation of this method must only depend on:

- the fields of the widget, which themselves must not change over time,
and
- any ambient state obtained from the `context` using
[BuildContext.dependOnInheritedWidgetOfExactType](flutter-docs://api/widgets/BuildContext/dependOnInheritedWidgetOfExactType).


If a widget's [build](flutter-docs://api/material/ListTile/build) method is to depend on anything else, use a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) instead.

See also:

- [StatelessWidget](flutter-docs://api/widgets/StatelessWidget), which contains the discussion on performance considerations.


## Implementation

```dart
@override
Widget build(BuildContext context) {
  assert(debugCheckHasMaterial(context));
  final ThemeData theme = Theme.of(context);
  final IconButtonThemeData iconButtonTheme = IconButtonTheme.of(context);
  final ListTileThemeData tileTheme = ListTileTheme.of(context);
  final ListTileStyle listTileStyle =
      style ?? tileTheme.style ?? theme.listTileTheme.style ?? ListTileStyle.list;
  final ListTileThemeData defaults = theme.useMaterial3
      ? _LisTileDefaultsM3(context)
      : _LisTileDefaultsM2(context, listTileStyle);
  final Set<WidgetState> states = <WidgetState>{
    if (!enabled) WidgetState.disabled,
    if (selected) WidgetState.selected,
  };

  Color? resolveColor(
    Color? explicitColor,
    Color? selectedColor,
    Color? enabledColor, [
    Color? disabledColor,
  ]) {
    return _IndividualOverrides(
      explicitColor: explicitColor,
      selectedColor: selectedColor,
      enabledColor: enabledColor,
      disabledColor: disabledColor,
    ).resolve(states);
  }

  Color? effectiveIconColor =
      resolveColor(iconColor, selectedColor, iconColor) ??
      resolveColor(tileTheme.iconColor, tileTheme.selectedColor, tileTheme.iconColor) ??
      resolveColor(
        theme.listTileTheme.iconColor,
        theme.listTileTheme.selectedColor,
        theme.listTileTheme.iconColor,
      );

  final Color? defaultEffectiveIconColor = resolveColor(
    defaults.iconColor,
    defaults.selectedColor,
    defaults.iconColor,
    theme.disabledColor,
  );

  final Color? effectiveIconButtonColor =
      effectiveIconColor ??
      iconButtonTheme.style?.foregroundColor?.resolve(states) ??
      defaultEffectiveIconColor;

  effectiveIconColor ??= defaultEffectiveIconColor;

  final Color? effectiveColor =
      resolveColor(textColor, selectedColor, textColor) ??
      resolveColor(tileTheme.textColor, tileTheme.selectedColor, tileTheme.textColor) ??
      resolveColor(
        theme.listTileTheme.textColor,
        theme.listTileTheme.selectedColor,
        theme.listTileTheme.textColor,
      ) ??
      resolveColor(
        defaults.textColor,
        defaults.selectedColor,
        defaults.textColor,
        theme.disabledColor,
      );
  final IconThemeData iconThemeData = IconThemeData(color: effectiveIconColor);
  final IconButtonThemeData iconButtonThemeData = IconButtonThemeData(
    style:
        IconButtonTheme.of(context).style?.copyWith(
          foregroundColor: WidgetStatePropertyAll<Color?>(effectiveIconButtonColor),
        ) ??
        IconButton.styleFrom(foregroundColor: effectiveIconButtonColor),
  );

  TextStyle? leadingAndTrailingStyle;
  if (leading != null || trailing != null) {
    leadingAndTrailingStyle =
        leadingAndTrailingTextStyle ??
        tileTheme.leadingAndTrailingTextStyle ??
        defaults.leadingAndTrailingTextStyle!;
    final Color? leadingAndTrailingTextColor = effectiveColor;
    leadingAndTrailingStyle = leadingAndTrailingStyle.copyWith(
      color: leadingAndTrailingTextColor,
    );
  }

  Widget? leadingIcon;
  if (leading != null) {
    leadingIcon = AnimatedDefaultTextStyle(
      style: leadingAndTrailingStyle!,
      duration: kThemeChangeDuration,
      child: leading!,
    );
  }

  TextStyle titleStyle = titleTextStyle ?? tileTheme.titleTextStyle ?? defaults.titleTextStyle!;
  final Color? titleColor = effectiveColor;
  titleStyle = titleStyle.copyWith(
    color: titleColor,
    fontSize: _isDenseLayout(theme, tileTheme) ? 13.0 : null,
  );
  final Widget titleText = AnimatedDefaultTextStyle(
    style: titleStyle,
    duration: kThemeChangeDuration,
    child: title ?? const SizedBox(),
  );

  Widget? subtitleText;
  TextStyle? subtitleStyle;
  if (subtitle != null) {
    subtitleStyle =
        subtitleTextStyle ?? tileTheme.subtitleTextStyle ?? defaults.subtitleTextStyle!;
    final Color? subtitleColor = effectiveColor;
    subtitleStyle = subtitleStyle.copyWith(
      color: subtitleColor,
      fontSize: _isDenseLayout(theme, tileTheme) ? 12.0 : null,
    );
    subtitleText = AnimatedDefaultTextStyle(
      style: subtitleStyle,
      duration: kThemeChangeDuration,
      child: subtitle!,
    );
  }

  Widget? trailingIcon;
  if (trailing != null) {
    trailingIcon = AnimatedDefaultTextStyle(
      style: leadingAndTrailingStyle!,
      duration: kThemeChangeDuration,
      child: trailing!,
    );
  }

  final TextDirection textDirection = Directionality.of(context);
  final EdgeInsets resolvedContentPadding =
      contentPadding?.resolve(textDirection) ??
      tileTheme.contentPadding?.resolve(textDirection) ??
      defaults.contentPadding!.resolve(textDirection);

  // Show basic cursor when ListTile isn't enabled or gesture callbacks are null.
  final Set<WidgetState> mouseStates = <WidgetState>{
    if (!enabled || (onTap == null && onLongPress == null)) WidgetState.disabled,
  };
  final MouseCursor effectiveMouseCursor =
      WidgetStateProperty.resolveAs<MouseCursor?>(mouseCursor, mouseStates) ??
      tileTheme.mouseCursor?.resolve(mouseStates) ??
      WidgetStateMouseCursor.clickable.resolve(mouseStates);

  final ListTileTitleAlignment effectiveTitleAlignment =
      titleAlignment ??
      tileTheme.titleAlignment ??
      (theme.useMaterial3
          ? ListTileTitleAlignment.threeLine
          : ListTileTitleAlignment.titleHeight);

  return InkWell(
    customBorder: shape ?? tileTheme.shape,
    onTap: enabled ? onTap : null,
    onLongPress: enabled ? onLongPress : null,
    onFocusChange: onFocusChange,
    mouseCursor: effectiveMouseCursor,
    canRequestFocus: enabled,
    focusNode: focusNode,
    focusColor: focusColor,
    hoverColor: hoverColor,
    splashColor: splashColor,
    autofocus: autofocus,
    enableFeedback: enableFeedback ?? tileTheme.enableFeedback ?? true,
    statesController: statesController,
    child: Semantics(
      button: internalAddSemanticForOnTap && (onTap != null || onLongPress != null),
      selected: selected,
      enabled: enabled,
      child: Ink(
        decoration: ShapeDecoration(
          shape: shape ?? tileTheme.shape ?? const Border(),
          color: _tileBackgroundColor(theme, tileTheme, defaults),
        ),
        child: SafeArea(
          top: false,
          bottom: false,
          minimum: resolvedContentPadding,
          child: IconTheme.merge(
            data: iconThemeData,
            child: IconButtonTheme(
              data: iconButtonThemeData,
              child: _ListTile(
                leading: leadingIcon,
                title: titleText,
                subtitle: subtitleText,
                trailing: trailingIcon,
                isDense: _isDenseLayout(theme, tileTheme),
                visualDensity: visualDensity ?? tileTheme.visualDensity ?? theme.visualDensity,
                isThreeLine:
                    isThreeLine ??
                    tileTheme.isThreeLine ??
                    theme.listTileTheme.isThreeLine ??
                    false,
                textDirection: textDirection,
                titleBaselineType:
                    titleStyle.textBaseline ?? defaults.titleTextStyle!.textBaseline!,
                subtitleBaselineType:
                    subtitleStyle?.textBaseline ?? defaults.subtitleTextStyle!.textBaseline!,
                horizontalTitleGap: horizontalTitleGap ?? tileTheme.horizontalTitleGap ?? 16,
                minVerticalPadding:
                    minVerticalPadding ??
                    tileTheme.minVerticalPadding ??
                    defaults.minVerticalPadding!,
                minLeadingWidth:
                    minLeadingWidth ?? tileTheme.minLeadingWidth ?? defaults.minLeadingWidth!,
                minTileHeight: minTileHeight ?? tileTheme.minTileHeight,
                titleAlignment: effectiveTitleAlignment,
              ),
            ),
          ),
        ),
      ),
    ),
  );
}
```