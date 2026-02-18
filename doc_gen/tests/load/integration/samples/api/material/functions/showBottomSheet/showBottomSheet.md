# showBottomSheet function

[PersistentBottomSheetController](mcp://flutter/api/material/PersistentBottomSheetController) showBottomSheet({
required [BuildContext](mcp://flutter/api/widgets/BuildContext) context,
required [WidgetBuilder](mcp://flutter/api/widgets/WidgetBuilder) builder,
[Color](mcp://flutter/api/dart-ui/Color)? backgroundColor,
[double](mcp://flutter/api/dart-core/double)? elevation,
[ShapeBorder](mcp://flutter/api/painting/ShapeBorder)? shape,
[Clip](mcp://flutter/api/dart-ui/Clip)? clipBehavior,
[BoxConstraints](mcp://flutter/api/rendering/BoxConstraints)? constraints,
[bool](mcp://flutter/api/dart-core/bool)? enableDrag,
[bool](mcp://flutter/api/dart-core/bool)? showDragHandle,
[AnimationController](mcp://flutter/api/animation/AnimationController)? transitionAnimationController,
[AnimationStyle](mcp://flutter/api/animation/AnimationStyle)? sheetAnimationStyle,
})

Shows a Material Design bottom sheet in the nearest [Scaffold](mcp://flutter/api/material/Scaffold) ancestor. To
show a persistent bottom sheet, use the [Scaffold.bottomSheet](mcp://flutter/api/material/Scaffold/bottomSheet).

Returns a controller that can be used to close and otherwise manipulate the
bottom sheet.

The optional `backgroundColor`, `elevation`, `shape`, `clipBehavior`, `constraints` and `transitionAnimationController` parameters can be passed in to customize the appearance and behavior of
persistent bottom sheets (see the documentation for these on [BottomSheet](mcp://flutter/api/material/BottomSheet) for more details).

The `enableDrag` parameter specifies whether the bottom sheet can be
dragged up and down and dismissed by swiping downwards.

The `sheetAnimationStyle` parameter is used to override the bottom sheet
animation duration and reverse animation duration.

If [AnimationStyle.duration](mcp://flutter/api/animation/AnimationStyle/duration) is provided, it will be used to override
the bottom sheet animation duration in the underlying [BottomSheet.createAnimationController](mcp://flutter/api/material/BottomSheet/createAnimationController).

If [AnimationStyle.reverseDuration](mcp://flutter/api/animation/AnimationStyle/reverseDuration) is provided, it will be used to
override the bottom sheet reverse animation duration in the underlying [BottomSheet.createAnimationController](mcp://flutter/api/material/BottomSheet/createAnimationController).

To disable the bottom sheet animation, use [AnimationStyle.noAnimation](mcp://flutter/api/animation/AnimationStyle/noAnimation).

This sample showcases how to override the [showBottomSheet](mcp://flutter/api/material/showBottomSheet) animation
duration and reverse animation duration using [AnimationStyle](mcp://flutter/api/animation/AnimationStyle).


To create a local project with this code sample, run:  flutter create --sample=material.showBottomSheet.1 mysample

[Omitted code: Interactive sample]

To rebuild the bottom sheet (e.g. if it is stateful), call[PersistentBottomSheetController.setState](mcp://flutter/api/material/ScaffoldFeatureController/setState) on the controller returned by
this method.

The new bottom sheet becomes a [LocalHistoryEntry](mcp://flutter/api/widgets/LocalHistoryEntry) for the enclosing [ModalRoute](mcp://flutter/api/widgets/ModalRoute) and a back button is added to the app bar of the [Scaffold](mcp://flutter/api/material/Scaffold) that closes the bottom sheet.

To create a persistent bottom sheet that is not a [LocalHistoryEntry](mcp://flutter/api/widgets/LocalHistoryEntry) and
does not add a back button to the enclosing Scaffold's app bar, use the [Scaffold.bottomSheet](mcp://flutter/api/material/Scaffold/bottomSheet) constructor parameter.

A closely related widget is a modal bottom sheet, which is an alternative
to a menu or a dialog and prevents the user from interacting with the rest
of the app. Modal bottom sheets can be created and displayed with the[showModalBottomSheet](mcp://flutter/api/material/showModalBottomSheet) function.

The `context` argument is used to look up the [Scaffold](mcp://flutter/api/material/Scaffold) for the bottom
sheet. It is only used when the method is called. Its corresponding widget
can be safely removed from the tree before the bottom sheet is closed.

See also:

- [BottomSheet](mcp://flutter/api/material/BottomSheet), which becomes the parent of the widget returned by the
`builder`.
- [showModalBottomSheet](mcp://flutter/api/material/showModalBottomSheet), which can be used to display a modal bottom
sheet.
- [Scaffold.of](mcp://flutter/api/material/Scaffold/of), for information about how to obtain the [BuildContext](mcp://flutter/api/widgets/BuildContext).
- The Material 2 spec at [m2.material.io/components/sheets-bottom](https://m2.material.io/components/sheets-bottom).
- The Material 3 spec at [m3.material.io/components/bottom-sheets/overview](https://m3.material.io/components/bottom-sheets/overview).
- [AnimationStyle](mcp://flutter/api/animation/AnimationStyle), which is used to override the bottom sheet animation
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