# showBottomSheet function

[PersistentBottomSheetController](flutter-docs://api/material/PersistentBottomSheetController) showBottomSheet({
required [BuildContext](flutter-docs://api/widgets/BuildContext) context,
required [WidgetBuilder](flutter-docs://api/widgets/WidgetBuilder) builder,
[Color](flutter-docs://api/dart-ui/Color)? backgroundColor,
[double](flutter-docs://api/dart-core/double)? elevation,
[ShapeBorder](flutter-docs://api/painting/ShapeBorder)? shape,
[Clip](flutter-docs://api/dart-ui/Clip)? clipBehavior,
[BoxConstraints](flutter-docs://api/rendering/BoxConstraints)? constraints,
[bool](flutter-docs://api/dart-core/bool)? enableDrag,
[bool](flutter-docs://api/dart-core/bool)? showDragHandle,
[AnimationController](flutter-docs://api/animation/AnimationController)? transitionAnimationController,
[AnimationStyle](flutter-docs://api/animation/AnimationStyle)? sheetAnimationStyle,
})

Shows a Material Design bottom sheet in the nearest [Scaffold](flutter-docs://api/material/Scaffold) ancestor. To
show a persistent bottom sheet, use the [Scaffold.bottomSheet](flutter-docs://api/material/Scaffold/bottomSheet).

Returns a controller that can be used to close and otherwise manipulate the
bottom sheet.

The optional `backgroundColor`, `elevation`, `shape`, `clipBehavior`, `constraints` and `transitionAnimationController` parameters can be passed in to customize the appearance and behavior of
persistent bottom sheets (see the documentation for these on [BottomSheet](flutter-docs://api/material/BottomSheet) for more details).

The `enableDrag` parameter specifies whether the bottom sheet can be
dragged up and down and dismissed by swiping downwards.

The `sheetAnimationStyle` parameter is used to override the bottom sheet
animation duration and reverse animation duration.

If [AnimationStyle.duration](flutter-docs://api/animation/AnimationStyle/duration) is provided, it will be used to override
the bottom sheet animation duration in the underlying [BottomSheet.createAnimationController](flutter-docs://api/material/BottomSheet/createAnimationController).

If [AnimationStyle.reverseDuration](flutter-docs://api/animation/AnimationStyle/reverseDuration) is provided, it will be used to
override the bottom sheet reverse animation duration in the underlying [BottomSheet.createAnimationController](flutter-docs://api/material/BottomSheet/createAnimationController).

To disable the bottom sheet animation, use [AnimationStyle.noAnimation](flutter-docs://api/animation/AnimationStyle/noAnimation).

This sample showcases how to override the [showBottomSheet](flutter-docs://api/material/showBottomSheet) animation
duration and reverse animation duration using [AnimationStyle](flutter-docs://api/animation/AnimationStyle).


To create a local project with this code sample, run:  flutter create --sample=material.showBottomSheet.1 mysample

[Omitted code: Interactive sample]

To rebuild the bottom sheet (e.g. if it is stateful), call[PersistentBottomSheetController.setState](flutter-docs://api/material/ScaffoldFeatureController/setState) on the controller returned by
this method.

The new bottom sheet becomes a [LocalHistoryEntry](flutter-docs://api/widgets/LocalHistoryEntry) for the enclosing [ModalRoute](flutter-docs://api/widgets/ModalRoute) and a back button is added to the app bar of the [Scaffold](flutter-docs://api/material/Scaffold) that closes the bottom sheet.

To create a persistent bottom sheet that is not a [LocalHistoryEntry](flutter-docs://api/widgets/LocalHistoryEntry) and
does not add a back button to the enclosing Scaffold's app bar, use the [Scaffold.bottomSheet](flutter-docs://api/material/Scaffold/bottomSheet) constructor parameter.

A closely related widget is a modal bottom sheet, which is an alternative
to a menu or a dialog and prevents the user from interacting with the rest
of the app. Modal bottom sheets can be created and displayed with the[showModalBottomSheet](flutter-docs://api/material/showModalBottomSheet) function.

The `context` argument is used to look up the [Scaffold](flutter-docs://api/material/Scaffold) for the bottom
sheet. It is only used when the method is called. Its corresponding widget
can be safely removed from the tree before the bottom sheet is closed.

See also:

- [BottomSheet](flutter-docs://api/material/BottomSheet), which becomes the parent of the widget returned by the
`builder`.
- [showModalBottomSheet](flutter-docs://api/material/showModalBottomSheet), which can be used to display a modal bottom
sheet.
- [Scaffold.of](flutter-docs://api/material/Scaffold/of), for information about how to obtain the [BuildContext](flutter-docs://api/widgets/BuildContext).
- The Material 2 spec at [m2.material.io/components/sheets-bottom](https://m2.material.io/components/sheets-bottom).
- The Material 3 spec at [m3.material.io/components/bottom-sheets/overview](https://m3.material.io/components/bottom-sheets/overview).
- [AnimationStyle](flutter-docs://api/animation/AnimationStyle), which is used to override the bottom sheet animation
duration and reverse animation duration.


## Implementation

```dart
PersistentBottomSheetController showBottomSheet({
  required BuildContext context,
  required WidgetBuilder builder,
  Color? backgroundColor,
  double? elevation,
  ShapeBorder? shape,
  Clip? clipBehavior,
  BoxConstraints? constraints,
  bool? enableDrag,
  bool? showDragHandle,
  AnimationController? transitionAnimationController,
  AnimationStyle? sheetAnimationStyle,
}) {
  assert(debugCheckHasScaffold(context));

  return Scaffold.of(context).showBottomSheet(
    builder,
    backgroundColor: backgroundColor,
    elevation: elevation,
    shape: shape,
    clipBehavior: clipBehavior,
    constraints: constraints,
    enableDrag: enableDrag,
    showDragHandle: showDragHandle,
    transitionAnimationController: transitionAnimationController,
    sheetAnimationStyle: sheetAnimationStyle,
  );
}
```