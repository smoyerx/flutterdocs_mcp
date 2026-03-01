# material library

Flutter widgets implementing Material Design.

To use, import `package:flutter/material.dart`.

[https://www.youtube.com/embed/DL0Ix1lnC4w?rel=0](https://www.youtube.com/embed/DL0Ix1lnC4w?rel=0)

See also:

- [docs.flutter.dev/ui/widgets/material](https://docs.flutter.dev/ui/widgets/material) for a catalog of commonly-used Material component widgets.
- [m3.material.io](https://m3.material.io/) for the Material 3 specification
- [m2.material.io](https://m2.material.io/) for the Material 2 specification


## Classes

[AboutDialog](flutter-docs://api/material/AboutDialog)
An about box. This is a dialog box with the application's icon, name,
version number, and copyright, plus a button to show licenses for software
used by the application.

[AboutListTile](flutter-docs://api/material/AboutListTile)
A [ListTile](flutter-docs://api/material/ListTile) that shows an about box.

[AbsorbPointer](flutter-docs://api/widgets/AbsorbPointer)
A widget that absorbs pointers during hit testing.

[AbstractLayoutBuilder](flutter-docs://api/widgets/AbstractLayoutBuilder)<LayoutInfoType>
An abstract superclass for widgets that defer their building until layout.

[Accumulator](flutter-docs://api/painting/Accumulator)
Mutable wrapper of an integer that can be passed by reference to track a
value across a recursive stack.

[Action](flutter-docs://api/widgets/Action)<T extends [Intent](flutter-docs://api/widgets/Intent)>
Base class for an action or command to be performed.

[ActionChip](flutter-docs://api/material/ActionChip)
A Material Design action chip.

[ActionDispatcher](flutter-docs://api/widgets/ActionDispatcher)
An action dispatcher that invokes the actions given to it.

[ActionIconTheme](flutter-docs://api/material/ActionIconTheme)
An inherited widget that overrides the default icon of [BackButtonIcon](flutter-docs://api/material/BackButtonIcon),
[CloseButtonIcon](flutter-docs://api/material/CloseButtonIcon), [DrawerButtonIcon](flutter-docs://api/material/DrawerButtonIcon), and [EndDrawerButtonIcon](flutter-docs://api/material/EndDrawerButtonIcon) in this
widget's subtree.

[ActionIconThemeData](flutter-docs://api/material/ActionIconThemeData)
A [ActionIconThemeData](flutter-docs://api/material/ActionIconThemeData) that overrides the default icons of
[BackButton](flutter-docs://api/material/BackButton), [CloseButton](flutter-docs://api/material/CloseButton), [DrawerButton](flutter-docs://api/material/DrawerButton), and [EndDrawerButton](flutter-docs://api/material/EndDrawerButton) with
[ActionIconTheme.of](flutter-docs://api/material/ActionIconTheme/of) or the overall [Theme](flutter-docs://api/material/Theme)'s [ThemeData.actionIconTheme](flutter-docs://api/material/ThemeData/actionIconTheme).

[ActionListener](flutter-docs://api/widgets/ActionListener)
A helper widget for making sure that listeners on an action are removed properly.

[Actions](flutter-docs://api/widgets/Actions)
A widget that maps [Intent](flutter-docs://api/widgets/Intent) s to [Action](flutter-docs://api/widgets/Action) s to be used by its descendants
when invoking an [Action](flutter-docs://api/widgets/Action).

[ActivateAction](flutter-docs://api/widgets/ActivateAction)
An [Action](flutter-docs://api/widgets/Action) that activates the currently focused control.

[ActivateIntent](flutter-docs://api/widgets/ActivateIntent)
An [Intent](flutter-docs://api/widgets/Intent) that activates the currently focused control.

[Adaptation](flutter-docs://api/material/Adaptation)<T>
Defines a customized theme for components with an `adaptive` factory constructor.

[AdaptiveTextSelectionToolbar](flutter-docs://api/material/AdaptiveTextSelectionToolbar)
The default context menu for text selection for the current platform.

[AlertDialog](flutter-docs://api/material/AlertDialog)
A Material Design alert dialog.

[Align](flutter-docs://api/widgets/Align)
A widget that aligns its child within itself and optionally sizes itself
based on the child's size.

[Alignment](flutter-docs://api/painting/Alignment)
A point within a rectangle.

[AlignmentDirectional](flutter-docs://api/painting/AlignmentDirectional)
An offset that's expressed as a fraction of a [Size](flutter-docs://api/dart-ui/Size), but whose horizontal
component is dependent on the writing direction.

[AlignmentGeometry](flutter-docs://api/painting/AlignmentGeometry)
Base class for [Alignment](flutter-docs://api/painting/Alignment) that allows for text-direction aware
resolution.

[AlignmentGeometryTween](flutter-docs://api/rendering/AlignmentGeometryTween)
An interpolation between two [AlignmentGeometry](flutter-docs://api/painting/AlignmentGeometry).

[AlignmentTween](flutter-docs://api/rendering/AlignmentTween)
An interpolation between two alignments.

[AlignTransition](flutter-docs://api/widgets/AlignTransition)
Animated version of an [Align](flutter-docs://api/widgets/Align) that animates its [Align.alignment](flutter-docs://api/widgets/Align/alignment) property.

[AlwaysScrollableScrollPhysics](flutter-docs://api/widgets/AlwaysScrollableScrollPhysics)
Scroll physics that always lets the user scroll.

[AlwaysStoppedAnimation](flutter-docs://api/animation/AlwaysStoppedAnimation)<T>
An animation that is always stopped at a given value.

[AndroidView](flutter-docs://api/widgets/AndroidView)
Embeds an Android view in the Widget hierarchy.

[AndroidViewSurface](flutter-docs://api/widgets/AndroidViewSurface)
Integrates an Android view with Flutter's compositor, touch, and semantics subsystems.

[Animatable](flutter-docs://api/animation/Animatable)<T>
An object that can produce a value of type `T` given an [Animation<double>](flutter-docs://api/animation/Animation) as input.

[AnimatedAlign](flutter-docs://api/widgets/AnimatedAlign)
Animated version of [Align](flutter-docs://api/widgets/Align) which automatically transitions the child's
position over a given duration whenever the given [alignment](flutter-docs://api/widgets/AnimatedAlign/alignment) changes.

[AnimatedBuilder](flutter-docs://api/widgets/AnimatedBuilder)
A general-purpose widget for building animations.

[AnimatedContainer](flutter-docs://api/widgets/AnimatedContainer)
Animated version of [Container](flutter-docs://api/widgets/Container) that gradually changes its values over a period of time.

[AnimatedCrossFade](flutter-docs://api/widgets/AnimatedCrossFade)
A widget that cross-fades between two given children and animates itself
between their sizes.

[AnimatedDefaultTextStyle](flutter-docs://api/widgets/AnimatedDefaultTextStyle)
Animated version of [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle) which automatically transitions the
default text style (the text style to apply to descendant [Text](flutter-docs://api/widgets/Text) widgets
without explicit style) over a given duration whenever the given style
changes.

[AnimatedFractionallySizedBox](flutter-docs://api/widgets/AnimatedFractionallySizedBox)
Animated version of [FractionallySizedBox](flutter-docs://api/widgets/FractionallySizedBox) which automatically transitions the
child's size over a given duration whenever the given [widthFactor](flutter-docs://api/widgets/AnimatedFractionallySizedBox/widthFactor) or
[heightFactor](flutter-docs://api/widgets/AnimatedFractionallySizedBox/heightFactor) changes, as well as the position whenever the given [alignment](flutter-docs://api/widgets/AnimatedFractionallySizedBox/alignment) changes.

[AnimatedGrid](flutter-docs://api/widgets/AnimatedGrid)
A scrolling container that animates items when they are inserted into or removed from a grid.
in a grid.

[AnimatedGridState](flutter-docs://api/widgets/AnimatedGridState)
The [State](flutter-docs://api/widgets/State) for an [AnimatedGrid](flutter-docs://api/widgets/AnimatedGrid) that animates items when they are
inserted or removed.

[AnimatedIcon](flutter-docs://api/material/AnimatedIcon)
Shows an animated icon at a given animation [progress](flutter-docs://api/material/AnimatedIcon/progress).

[AnimatedIconData](flutter-docs://api/material/AnimatedIconData)
Vector graphics data for icons used by [AnimatedIcon](flutter-docs://api/material/AnimatedIcon).

[AnimatedIcons](flutter-docs://api/material/AnimatedIcons)
Identifier for the supported Material Design animated icons.

[AnimatedList](flutter-docs://api/widgets/AnimatedList)
A scrolling container that animates items when they are inserted or removed.

[AnimatedListState](flutter-docs://api/widgets/AnimatedListState)
The [AnimatedListState](flutter-docs://api/widgets/AnimatedListState) for [AnimatedList](flutter-docs://api/widgets/AnimatedList), a scrolling list container that
animates items when they are inserted or removed.

[AnimatedModalBarrier](flutter-docs://api/widgets/AnimatedModalBarrier)
A widget that prevents the user from interacting with widgets behind itself,
and can be configured with an animated color value.

[AnimatedOpacity](flutter-docs://api/widgets/AnimatedOpacity)
Animated version of [Opacity](flutter-docs://api/widgets/Opacity) which automatically transitions the child's
opacity over a given duration whenever the given opacity changes.

[AnimatedPadding](flutter-docs://api/widgets/AnimatedPadding)
Animated version of [Padding](flutter-docs://api/widgets/Padding) which automatically transitions the
indentation over a given duration whenever the given inset changes.

[AnimatedPhysicalModel](flutter-docs://api/widgets/AnimatedPhysicalModel)
Animated version of [PhysicalModel](flutter-docs://api/widgets/PhysicalModel).

[AnimatedPositioned](flutter-docs://api/widgets/AnimatedPositioned)
Animated version of [Positioned](flutter-docs://api/widgets/Positioned) which automatically transitions the child's
position over a given duration whenever the given position changes.

[AnimatedPositionedDirectional](flutter-docs://api/widgets/AnimatedPositionedDirectional)
Animated version of [PositionedDirectional](flutter-docs://api/widgets/PositionedDirectional) which automatically transitions
the child's position over a given duration whenever the given position
changes.

[AnimatedRotation](flutter-docs://api/widgets/AnimatedRotation)
Animated version of [Transform.rotate](flutter-docs://api/widgets/Transform/Transform.rotate) which automatically transitions the child's
rotation over a given duration whenever the given rotation changes.

[AnimatedScale](flutter-docs://api/widgets/AnimatedScale)
Animated version of [Transform.scale](flutter-docs://api/widgets/Transform/Transform.scale) which automatically transitions the child's
scale over a given duration whenever the given scale changes.

[AnimatedSize](flutter-docs://api/widgets/AnimatedSize)
Animated widget that automatically transitions its size over a given
duration whenever the given child's size changes.

[AnimatedSlide](flutter-docs://api/widgets/AnimatedSlide)
Widget which automatically transitions the child's
offset relative to its normal position whenever the given offset changes.

[AnimatedSwitcher](flutter-docs://api/widgets/AnimatedSwitcher)
A widget that by default does a cross-fade between a new widget and the
widget previously set on the [AnimatedSwitcher](flutter-docs://api/widgets/AnimatedSwitcher) as a child.

[AnimatedTheme](flutter-docs://api/material/AnimatedTheme)
Animated version of [Theme](flutter-docs://api/material/Theme) which automatically transitions the colors,
etc, over a given duration whenever the given theme changes.

[AnimatedWidget](flutter-docs://api/widgets/AnimatedWidget)
A widget that rebuilds when the given [Listenable](flutter-docs://api/foundation/Listenable) changes value.

[AnimatedWidgetBaseState](flutter-docs://api/widgets/AnimatedWidgetBaseState)<T extends [ImplicitlyAnimatedWidget](flutter-docs://api/widgets/ImplicitlyAnimatedWidget)>
A base class for widgets with implicit animations that need to rebuild their
widget tree as the animation runs.

[Animation](flutter-docs://api/animation/Animation)<T>
A value which might change over time, moving forward or backward.

[AnimationController](flutter-docs://api/animation/AnimationController)
A controller for an animation.

[AnimationMax](flutter-docs://api/animation/AnimationMax)<T extends [num](flutter-docs://api/dart-core/num)>
An animation that tracks the maximum of two other animations.

[AnimationMean](flutter-docs://api/animation/AnimationMean)
An animation of [double](flutter-docs://api/dart-core/double) s that tracks the mean of two other animations.

[AnimationMin](flutter-docs://api/animation/AnimationMin)<T extends [num](flutter-docs://api/dart-core/num)>
An animation that tracks the minimum of two other animations.

[AnimationStyle](flutter-docs://api/animation/AnimationStyle)
Used to override the default parameters of an animation.

[AnnotatedRegion](flutter-docs://api/widgets/AnnotatedRegion)<T extends [Object](flutter-docs://api/dart-core/Object)>
Annotates a region of the layer tree with a value.

[AppBar](flutter-docs://api/material/AppBar)
A Material Design app bar.

[AppBarTheme](flutter-docs://api/material/AppBarTheme)
Defines default property values for descendant [AppBar](flutter-docs://api/material/AppBar) widgets.

[AppBarThemeData](flutter-docs://api/material/AppBarThemeData)
Defines default property values for descendant [AppBar](flutter-docs://api/material/AppBar) widgets.

[AppKitView](flutter-docs://api/widgets/AppKitView)
Widget that contains a macOS AppKit view.

[AppLifecycleListener](flutter-docs://api/widgets/AppLifecycleListener)
A listener that can be used to listen to changes in the application
lifecycle.

[AspectRatio](flutter-docs://api/widgets/AspectRatio)
A widget that attempts to size the child to a specific aspect ratio.

[AssetBundle](flutter-docs://api/services/AssetBundle)
A collection of resources used by the application.

[AssetBundleImageKey](flutter-docs://api/painting/AssetBundleImageKey)
Key for the image obtained by an [AssetImage](flutter-docs://api/painting/AssetImage) or [ExactAssetImage](flutter-docs://api/painting/ExactAssetImage).

[AssetBundleImageProvider](flutter-docs://api/painting/AssetBundleImageProvider)
A subclass of [ImageProvider](flutter-docs://api/painting/ImageProvider) that knows about [AssetBundle](flutter-docs://api/services/AssetBundle) s.

[AssetImage](flutter-docs://api/painting/AssetImage)
Fetches an image from an [AssetBundle](flutter-docs://api/services/AssetBundle), having determined the exact image to
use based on the context.

[AsyncSnapshot](flutter-docs://api/widgets/AsyncSnapshot)<T>
Immutable representation of the most recent interaction with an asynchronous
computation.

[Autocomplete](flutter-docs://api/material/Autocomplete)<T extends [Object](flutter-docs://api/dart-core/Object)>
A widget for helping the user make a selection by entering some text and
choosing from among a list of options.

[AutocompleteFirstOptionIntent](flutter-docs://api/widgets/AutocompleteFirstOptionIntent)
An [Intent](flutter-docs://api/widgets/Intent) to highlight the first option in the autocomplete list.

[AutocompleteHighlightedOption](flutter-docs://api/widgets/AutocompleteHighlightedOption)
An inherited widget used to indicate which autocomplete option should be
highlighted for keyboard navigation.

[AutocompleteLastOptionIntent](flutter-docs://api/widgets/AutocompleteLastOptionIntent)
An [Intent](flutter-docs://api/widgets/Intent) to highlight the last option in the autocomplete list.

[AutocompleteNextOptionIntent](flutter-docs://api/widgets/AutocompleteNextOptionIntent)
An [Intent](flutter-docs://api/widgets/Intent) to highlight the next option in the autocomplete list.

[AutocompleteNextPageOptionIntent](flutter-docs://api/widgets/AutocompleteNextPageOptionIntent)
An [Intent](flutter-docs://api/widgets/Intent) to highlight the option one page after the currently highlighted
option in the autocomplete list.

[AutocompletePreviousOptionIntent](flutter-docs://api/widgets/AutocompletePreviousOptionIntent)
An [Intent](flutter-docs://api/widgets/Intent) to highlight the previous option in the autocomplete list.

[AutocompletePreviousPageOptionIntent](flutter-docs://api/widgets/AutocompletePreviousPageOptionIntent)
An [Intent](flutter-docs://api/widgets/Intent) to highlight the option one page before the currently
highlighted option in the autocomplete list.

[AutofillGroup](flutter-docs://api/widgets/AutofillGroup)
An [AutofillScope](flutter-docs://api/services/AutofillScope) widget that groups [AutofillClient](flutter-docs://api/services/AutofillClient) s together.

[AutofillGroupState](flutter-docs://api/widgets/AutofillGroupState)
State associated with an [AutofillGroup](flutter-docs://api/widgets/AutofillGroup) widget.

[AutofillHints](flutter-docs://api/services/AutofillHints)
A collection of commonly used autofill hint strings on different platforms.

[AutomaticKeepAlive](flutter-docs://api/widgets/AutomaticKeepAlive)
Allows subtrees to request to be kept alive in lazy lists.

[AutomaticNotchedShape](flutter-docs://api/painting/AutomaticNotchedShape)
A [NotchedShape](flutter-docs://api/painting/NotchedShape) created from [ShapeBorder](flutter-docs://api/painting/ShapeBorder) s.

[BackButton](flutter-docs://api/material/BackButton)
A Material Design back icon button.

[BackButtonDispatcher](flutter-docs://api/widgets/BackButtonDispatcher)
Report to a [Router](flutter-docs://api/widgets/Router) when the user taps the back button on platforms that
support back buttons (such as Android).

[BackButtonIcon](flutter-docs://api/material/BackButtonIcon)
A "back" icon that's appropriate for the current [TargetPlatform](flutter-docs://api/foundation/TargetPlatform).

[BackButtonListener](flutter-docs://api/widgets/BackButtonListener)
A convenience widget that registers a callback for when the back button is pressed.

[BackdropFilter](flutter-docs://api/widgets/BackdropFilter)
A widget that applies a filter to the existing painted content and then
paints [child](flutter-docs://api/widgets/SingleChildRenderObjectWidget/child).

[BackdropGroup](flutter-docs://api/widgets/BackdropGroup)
A widget that establishes a shared backdrop layer for all child [BackdropFilter](flutter-docs://api/widgets/BackdropFilter) widgets that opt into using it.

[BackdropKey](flutter-docs://api/rendering/BackdropKey)
A backdrop key uniquely identifies the backdrop that a [BackdropFilterLayer](flutter-docs://api/rendering/BackdropFilterLayer) samples from.

[Badge](flutter-docs://api/material/Badge)
A Material Design "badge".

[BadgeTheme](flutter-docs://api/material/BadgeTheme)
An inherited widget that overrides the default color style, and size
parameters for [Badge](flutter-docs://api/material/Badge) s in this widget's subtree.

[BadgeThemeData](flutter-docs://api/material/BadgeThemeData)
Overrides the default properties values for descendant [Badge](flutter-docs://api/material/Badge) widgets.

[BallisticScrollActivity](flutter-docs://api/widgets/BallisticScrollActivity)
The activity a scroll view performs after being set into motion.

[Banner](flutter-docs://api/widgets/Banner)
Displays a diagonal message above the corner of another widget.

[BannerPainter](flutter-docs://api/widgets/BannerPainter)
Paints a [Banner](flutter-docs://api/widgets/Banner).

[Baseline](flutter-docs://api/widgets/Baseline)
A widget that positions its child according to the child's baseline.

[BeveledRectangleBorder](flutter-docs://api/painting/BeveledRectangleBorder)
A rectangular border with flattened or "beveled" corners.

[BlockSemantics](flutter-docs://api/widgets/BlockSemantics)
A widget that drops the semantics of all widget that were painted before it
in the same semantic container.

[Border](flutter-docs://api/painting/Border)
A border of a box, comprised of four sides: top, right, bottom, left.

[BorderDirectional](flutter-docs://api/painting/BorderDirectional)
A border of a box, comprised of four sides, the lateral sides of which
flip over based on the reading direction.

[BorderRadius](flutter-docs://api/painting/BorderRadius)
An immutable set of radii for each corner of a rectangle.

[BorderRadiusDirectional](flutter-docs://api/painting/BorderRadiusDirectional)
An immutable set of radii for each corner of a rectangle, but with the
corners specified in a manner dependent on the writing direction.

[BorderRadiusGeometry](flutter-docs://api/painting/BorderRadiusGeometry)
Base class for [BorderRadius](flutter-docs://api/painting/BorderRadius) that allows for text-direction aware resolution.

[BorderRadiusTween](flutter-docs://api/widgets/BorderRadiusTween)
An interpolation between two [BorderRadius](flutter-docs://api/painting/BorderRadius) s.

[BorderSide](flutter-docs://api/painting/BorderSide)
A side of a border of a box.

[BorderTween](flutter-docs://api/widgets/BorderTween)
An interpolation between two [Border](flutter-docs://api/painting/Border) s.

[BottomAppBar](flutter-docs://api/material/BottomAppBar)
A container that is typically used with [Scaffold.bottomNavigationBar](flutter-docs://api/material/Scaffold/bottomNavigationBar).

[BottomAppBarTheme](flutter-docs://api/material/BottomAppBarTheme)
Defines default property values for descendant [BottomAppBar](flutter-docs://api/material/BottomAppBar) widgets.

[BottomAppBarThemeData](flutter-docs://api/material/BottomAppBarThemeData)
Defines default property values for descendant [BottomAppBar](flutter-docs://api/material/BottomAppBar) widgets.

[BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar)
A material widget that's displayed at the bottom of an app for selecting
among a small number of views, typically between three and five.

[BottomNavigationBarItem](flutter-docs://api/widgets/BottomNavigationBarItem)
An interactive button within either material's [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar) or the iOS themed [CupertinoTabBar](flutter-docs://api/cupertino/CupertinoTabBar) with an icon and title.

[BottomNavigationBarTheme](flutter-docs://api/material/BottomNavigationBarTheme)
Applies a bottom navigation bar theme to descendant [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar) widgets.

[BottomNavigationBarThemeData](flutter-docs://api/material/BottomNavigationBarThemeData)
Defines default property values for descendant [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar) widgets.

[BottomSheet](flutter-docs://api/material/BottomSheet)
A Material Design bottom sheet.

[BottomSheetThemeData](flutter-docs://api/material/BottomSheetThemeData)
Defines default property values for [BottomSheet](flutter-docs://api/material/BottomSheet)'s [Material](flutter-docs://api/material/Material).

[BouncingScrollPhysics](flutter-docs://api/widgets/BouncingScrollPhysics)
Scroll physics for environments that allow the scroll offset to go beyond
the bounds of the content, but then bounce the content back to the edge of
those bounds.

[BouncingScrollSimulation](flutter-docs://api/widgets/BouncingScrollSimulation)
An implementation of scroll physics that matches iOS.

[BoxBorder](flutter-docs://api/painting/BoxBorder)
Base class for box borders that can paint as rectangles, circles, or rounded
rectangles.

[BoxConstraints](flutter-docs://api/rendering/BoxConstraints)
Immutable layout constraints for [RenderBox](flutter-docs://api/rendering/RenderBox) layout.

[BoxConstraintsTween](flutter-docs://api/widgets/BoxConstraintsTween)
An interpolation between two [BoxConstraints](flutter-docs://api/rendering/BoxConstraints).

[BoxDecoration](flutter-docs://api/painting/BoxDecoration)
An immutable description of how to paint a box.

[BoxPainter](flutter-docs://api/painting/BoxPainter)
A stateful class that can paint a particular [Decoration](flutter-docs://api/painting/Decoration).

[BoxScrollView](flutter-docs://api/widgets/BoxScrollView)
A [ScrollView](flutter-docs://api/widgets/ScrollView) that uses a single child layout model.

[BoxShadow](flutter-docs://api/painting/BoxShadow)
A shadow cast by a box.

[BuildContext](flutter-docs://api/widgets/BuildContext)
A handle to the location of a widget in the widget tree.

[Builder](flutter-docs://api/widgets/Builder)
A stateless utility widget whose [build](flutter-docs://api/widgets/Builder/build) method uses its
[builder](flutter-docs://api/widgets/Builder/builder) callback to create the widget's child.

[BuildOwner](flutter-docs://api/widgets/BuildOwner)
Manager class for the widgets framework.

[BuildScope](flutter-docs://api/widgets/BuildScope)
A class that determines the scope of a [BuildOwner.buildScope](flutter-docs://api/widgets/BuildOwner/buildScope) operation.

[ButtonActivateIntent](flutter-docs://api/widgets/ButtonActivateIntent)
An [Intent](flutter-docs://api/widgets/Intent) that activates the currently focused button.

[ButtonBar](flutter-docs://api/material/ButtonBar)
An end-aligned row of buttons, laying out into a column if there is not
enough horizontal space.

[ButtonBarTheme](flutter-docs://api/material/ButtonBarTheme)
Applies a button bar theme to descendant [ButtonBar](flutter-docs://api/material/ButtonBar) widgets.

[ButtonBarThemeData](flutter-docs://api/material/ButtonBarThemeData)
Defines the visual properties of [ButtonBar](flutter-docs://api/material/ButtonBar) widgets.

[ButtonSegment](flutter-docs://api/material/ButtonSegment)<T>
Data describing a segment of a [SegmentedButton](flutter-docs://api/material/SegmentedButton).

[ButtonStyle](flutter-docs://api/material/ButtonStyle)
The visual properties that most buttons have in common.

[ButtonStyleButton](flutter-docs://api/material/ButtonStyleButton)
The base [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) class for buttons whose style is defined by a [ButtonStyle](flutter-docs://api/material/ButtonStyle) object.

[ButtonTheme](flutter-docs://api/material/ButtonTheme)
Used with [ButtonThemeData](flutter-docs://api/material/ButtonThemeData) to configure the color and geometry of buttons.

[ButtonThemeData](flutter-docs://api/material/ButtonThemeData)
Used with [ButtonTheme](flutter-docs://api/material/ButtonTheme) to configure the color and geometry of buttons.

[CalendarDatePicker](flutter-docs://api/material/CalendarDatePicker)
Displays a grid of days for a given month and allows the user to select a
date.

[CalendarDelegate](flutter-docs://api/material/CalendarDelegate)<T extends [DateTime](flutter-docs://api/dart-core/DateTime)>
Controls the calendar system used in the date picker.

[CallbackAction](flutter-docs://api/widgets/CallbackAction)<T extends [Intent](flutter-docs://api/widgets/Intent)>
An [Action](flutter-docs://api/widgets/Action) that takes a callback in order to configure it without having to
create an explicit [Action](flutter-docs://api/widgets/Action) subclass just to call a callback.

[CallbackShortcuts](flutter-docs://api/widgets/CallbackShortcuts)
A widget that binds key combinations to specific callbacks.

[Canvas](flutter-docs://api/dart-ui/Canvas)
An interface for recording graphical operations.

[CapturedThemes](flutter-docs://api/widgets/CapturedThemes)
Stores a list of captured [InheritedTheme](flutter-docs://api/widgets/InheritedTheme) s that can be wrapped around a
child [Widget](flutter-docs://api/widgets/Widget).

[Card](flutter-docs://api/material/Card)
A Material Design card: a panel with slightly rounded corners and an
elevation shadow.

[CardTheme](flutter-docs://api/material/CardTheme)
Defines default property values for descendant [Card](flutter-docs://api/material/Card) widgets.

[CardThemeData](flutter-docs://api/material/CardThemeData)
Defines default property values for descendant [Card](flutter-docs://api/material/Card) widgets.

[CarouselController](flutter-docs://api/material/CarouselController)
A controller for [CarouselView](flutter-docs://api/material/CarouselView).

[CarouselScrollPhysics](flutter-docs://api/material/CarouselScrollPhysics)
Scroll physics used by a [CarouselView](flutter-docs://api/material/CarouselView).

[CarouselView](flutter-docs://api/material/CarouselView)
A Material Design carousel widget.

[CarouselViewTheme](flutter-docs://api/material/CarouselViewTheme)
Applies a carousel theme to descendant [CarouselView](flutter-docs://api/material/CarouselView) widgets.

[CarouselViewThemeData](flutter-docs://api/material/CarouselViewThemeData)
Defines default property values for descendant [CarouselView](flutter-docs://api/material/CarouselView) widgets.

[CatmullRomCurve](flutter-docs://api/animation/CatmullRomCurve)
An animation easing curve that passes smoothly through the given control
points using a centripetal Catmull-Rom spline.

[CatmullRomSpline](flutter-docs://api/animation/CatmullRomSpline)
A 2D spline that passes smoothly through the given control points using a
centripetal Catmull-Rom spline.

[Center](flutter-docs://api/widgets/Center)
A widget that centers its child within itself.

[ChangeNotifier](flutter-docs://api/foundation/ChangeNotifier)
A class that can be extended or mixed in that provides a change notification
API using [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) for notifications.

[CharacterActivator](flutter-docs://api/widgets/CharacterActivator)
A shortcut combination that is triggered by a key event that produces a
specific character.

[CharacterRange](flutter-docs://api/package-characters_characters/CharacterRange)
A range of characters of a [Characters](flutter-docs://api/package-characters_characters/Characters).

[Characters](flutter-docs://api/package-characters_characters/Characters)
The characters of a string.

[Checkbox](flutter-docs://api/material/Checkbox)
A Material Design checkbox.

[CheckboxListTile](flutter-docs://api/material/CheckboxListTile)
A [ListTile](flutter-docs://api/material/ListTile) with a [Checkbox](flutter-docs://api/material/Checkbox). In other words, a checkbox with a label.

[CheckboxMenuButton](flutter-docs://api/material/CheckboxMenuButton)
A menu item that combines a [Checkbox](flutter-docs://api/material/Checkbox) widget with a [MenuItemButton](flutter-docs://api/material/MenuItemButton).

[CheckboxTheme](flutter-docs://api/material/CheckboxTheme)
Applies a checkbox theme to descendant [Checkbox](flutter-docs://api/material/Checkbox) widgets.

[CheckboxThemeData](flutter-docs://api/material/CheckboxThemeData)
Defines default property values for descendant [Checkbox](flutter-docs://api/material/Checkbox) widgets.

[CheckedModeBanner](flutter-docs://api/widgets/CheckedModeBanner)
Displays a [Banner](flutter-docs://api/widgets/Banner) saying "DEBUG" when running in debug mode.
[MaterialApp](flutter-docs://api/material/MaterialApp) builds one of these by default.

[CheckedPopupMenuItem](flutter-docs://api/material/CheckedPopupMenuItem)<T>
An item with a checkmark in a Material Design popup menu.

[CheckmarkableChipAttributes](flutter-docs://api/material/CheckmarkableChipAttributes)
An interface for Material Design chips that can have check marks.

[ChildBackButtonDispatcher](flutter-docs://api/widgets/ChildBackButtonDispatcher)
A variant of [BackButtonDispatcher](flutter-docs://api/widgets/BackButtonDispatcher) which listens to notifications from a
parent back button dispatcher, and can take priority from its parent for the
handling of such notifications.

[ChildVicinity](flutter-docs://api/widgets/ChildVicinity)
The relative position of a child in a [TwoDimensionalViewport](flutter-docs://api/widgets/TwoDimensionalViewport) in relation
to other children of the viewport.

[Chip](flutter-docs://api/material/Chip)
A Material Design chip.

[ChipAnimationStyle](flutter-docs://api/material/ChipAnimationStyle)
A helper class that overrides the default chip animation parameters.

[ChipAttributes](flutter-docs://api/material/ChipAttributes)
An interface defining the base attributes for a Material Design chip.

[ChipTheme](flutter-docs://api/material/ChipTheme)
Applies a chip theme to descendant [RawChip](flutter-docs://api/material/RawChip)-based widgets, like [Chip](flutter-docs://api/material/Chip),
[InputChip](flutter-docs://api/material/InputChip), [ChoiceChip](flutter-docs://api/material/ChoiceChip), [FilterChip](flutter-docs://api/material/FilterChip), and [ActionChip](flutter-docs://api/material/ActionChip).

[ChipThemeData](flutter-docs://api/material/ChipThemeData)
Holds the color, shape, and text styles for a Material Design chip theme.

[ChoiceChip](flutter-docs://api/material/ChoiceChip)
A Material Design choice chip.

[CircleAvatar](flutter-docs://api/material/CircleAvatar)
A circle that represents a user.

[CircleBorder](flutter-docs://api/painting/CircleBorder)
A border that fits a circle within the available space.

[CircularNotchedRectangle](flutter-docs://api/painting/CircularNotchedRectangle)
A rectangle with a smooth circular notch.

[CircularProgressIndicator](flutter-docs://api/material/CircularProgressIndicator)
A Material Design circular progress indicator, which spins to indicate that
the application is busy.

[ClampingScrollPhysics](flutter-docs://api/widgets/ClampingScrollPhysics)
Scroll physics for environments that prevent the scroll offset from reaching
beyond the bounds of the content.

[ClampingScrollSimulation](flutter-docs://api/widgets/ClampingScrollSimulation)
An implementation of scroll physics that aligns with Android.

[ClipboardStatusNotifier](flutter-docs://api/widgets/ClipboardStatusNotifier)
A [ValueNotifier](flutter-docs://api/foundation/ValueNotifier) whose [value](flutter-docs://api/foundation/ValueNotifier/value) indicates whether the current contents of
the clipboard can be pasted.

[ClipContext](flutter-docs://api/painting/ClipContext)
Clip utilities used by [PaintingContext](flutter-docs://api/rendering/PaintingContext).

[ClipOval](flutter-docs://api/widgets/ClipOval)
A widget that clips its child using an oval.

[ClipPath](flutter-docs://api/widgets/ClipPath)
A widget that clips its child using a path.

[ClipRect](flutter-docs://api/widgets/ClipRect)
A widget that clips its child using a rectangle.

[ClipRRect](flutter-docs://api/widgets/ClipRRect)
A widget that clips its child using a rounded rectangle.

[ClipRSuperellipse](flutter-docs://api/widgets/ClipRSuperellipse)
A widget that clips its child using a rounded superellipse.

[CloseButton](flutter-docs://api/material/CloseButton)
A Material Design close icon button.

[CloseButtonIcon](flutter-docs://api/material/CloseButtonIcon)
A "close" icon that's appropriate for the current [TargetPlatform](flutter-docs://api/foundation/TargetPlatform).

[Color](flutter-docs://api/dart-ui/Color)
An immutable color value in ARGB format.

[ColoredBox](flutter-docs://api/widgets/ColoredBox)
A widget that paints its area with a specified [Color](flutter-docs://api/dart-ui/Color) and then draws its
child on top of that color.

[ColorFilter](flutter-docs://api/dart-ui/ColorFilter)
A description of a color filter to apply when drawing a shape or compositing
a layer with a particular [Paint](flutter-docs://api/dart-ui/Paint). A color filter is a function that takes
two colors, and outputs one color. When applied during compositing, it is
independently applied to each pixel of the layer being drawn before the
entire layer is merged with the destination.

[ColorFiltered](flutter-docs://api/widgets/ColorFiltered)
Applies a [ColorFilter](flutter-docs://api/dart-ui/ColorFilter) to its child.

[ColorProperty](flutter-docs://api/painting/ColorProperty)
[DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) that has an [Color](flutter-docs://api/dart-ui/Color) as value.

[Colors](flutter-docs://api/material/Colors)
[Color](flutter-docs://api/dart-ui/Color) and [ColorSwatch](flutter-docs://api/painting/ColorSwatch) constants which represent Material design's
[color palette](https://material.io/design/color/).

[ColorScheme](flutter-docs://api/material/ColorScheme)
A set of 45 colors based on the
[Material spec](https://m3.material.io/styles/color/the-color-system/color-roles) that can be used to configure the color properties of most components.

[ColorSwatch](flutter-docs://api/painting/ColorSwatch)<T>
A color that has a small table of related colors called a "swatch".

[ColorTween](flutter-docs://api/animation/ColorTween)
An interpolation between two colors.

[Column](flutter-docs://api/widgets/Column)
A widget that displays its children in a vertical array.

[ComponentElement](flutter-docs://api/widgets/ComponentElement)
An [Element](flutter-docs://api/widgets/Element) that composes other [Element](flutter-docs://api/widgets/Element) s.

[CompositedTransformFollower](flutter-docs://api/widgets/CompositedTransformFollower)
A widget that follows a [CompositedTransformTarget](flutter-docs://api/widgets/CompositedTransformTarget).

[CompositedTransformTarget](flutter-docs://api/widgets/CompositedTransformTarget)
A widget that can be targeted by a [CompositedTransformFollower](flutter-docs://api/widgets/CompositedTransformFollower).

[CompoundAnimation](flutter-docs://api/animation/CompoundAnimation)<T>
An interface for combining multiple Animations. Subclasses need only
implement the `value` getter to control how the child animations are
combined. Can be chained to combine more than 2 animations.

[ConstantTween](flutter-docs://api/animation/ConstantTween)<T>
A tween with a constant value.

[ConstrainedBox](flutter-docs://api/widgets/ConstrainedBox)
A widget that imposes additional constraints on its child.

[ConstrainedLayoutBuilder](flutter-docs://api/widgets/ConstrainedLayoutBuilder)<ConstraintType extends [Constraints](flutter-docs://api/rendering/Constraints)>
A specialized [AbstractLayoutBuilder](flutter-docs://api/widgets/AbstractLayoutBuilder) whose widget subtree depends on the
incoming `ConstraintType` that will be imposed on the widget.

[ConstraintsTransformBox](flutter-docs://api/widgets/ConstraintsTransformBox)
A container widget that applies an arbitrary transform to its constraints,
and sizes its child using the resulting [BoxConstraints](flutter-docs://api/rendering/BoxConstraints), optionally
clipping, or treating the overflow as an error.

[Container](flutter-docs://api/widgets/Container)
A convenience widget that combines common painting, positioning, and sizing
widgets.

[ContentInsertionConfiguration](flutter-docs://api/widgets/ContentInsertionConfiguration)
Configures the ability to insert media content through the soft keyboard.

[ContextAction](flutter-docs://api/widgets/ContextAction)<T extends [Intent](flutter-docs://api/widgets/Intent)>
An abstract [Action](flutter-docs://api/widgets/Action) subclass that adds an optional [BuildContext](flutter-docs://api/widgets/BuildContext) to the
[isEnabled](flutter-docs://api/widgets/ContextAction/isEnabled) and [invoke](flutter-docs://api/widgets/ContextAction/invoke) methods to be able to provide context to actions.

[ContextMenuButtonItem](flutter-docs://api/widgets/ContextMenuButtonItem)
The type and callback for a context menu button.

[ContextMenuController](flutter-docs://api/widgets/ContextMenuController)
Builds and manages a context menu at a given location.

[ContinuousRectangleBorder](flutter-docs://api/painting/ContinuousRectangleBorder)
A rectangular border with smooth continuous transitions between the straight
sides and the rounded corners.

[ControlsDetails](flutter-docs://api/material/ControlsDetails)
Container for all the information necessary to build a Stepper widget's
forward and backward controls for any given step.

[CopySelectionTextIntent](flutter-docs://api/widgets/CopySelectionTextIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a user interaction that attempts to copy or cut
the current selection in the field.

[Cubic](flutter-docs://api/animation/Cubic)
A cubic polynomial mapping of the unit interval.

[CupertinoBasedMaterialThemeData](flutter-docs://api/material/CupertinoBasedMaterialThemeData)
A class for creating a Material theme with a color scheme based off of the
colors from a [CupertinoThemeData](flutter-docs://api/cupertino/CupertinoThemeData). This is intended to be used only in the
case when a Material widget is unable to find a Material theme in the tree,
but is able to find a Cupertino theme. Most often this will occur when a
Material widget is used inside of a [CupertinoApp](flutter-docs://api/cupertino/CupertinoApp).

[CupertinoPageTransitionsBuilder](flutter-docs://api/material/CupertinoPageTransitionsBuilder)
Used by [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) to define a horizontal [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) page transition animation that matches native iOS page transitions.

[Curve](flutter-docs://api/animation/Curve)
An parametric animation easing curve, i.e. a mapping of the unit interval to
the unit interval.

[Curve2D](flutter-docs://api/animation/Curve2D)
Abstract class that defines an API for evaluating 2D parametric curves.

[Curve2DSample](flutter-docs://api/animation/Curve2DSample)
A class that holds a sample of a 2D parametric curve, containing the [value](flutter-docs://api/animation/Curve2DSample/value) (the X, Y coordinates) of the curve at the parametric value [t](flutter-docs://api/animation/Curve2DSample/t).

[CurvedAnimation](flutter-docs://api/animation/CurvedAnimation)
An animation that applies a curve to another animation.

[Curves](flutter-docs://api/animation/Curves)
A collection of common animation curves.

[CurveTween](flutter-docs://api/animation/CurveTween)
Transforms the value of the given animation by the given curve.

[CustomClipper](flutter-docs://api/rendering/CustomClipper)<T>
An interface for providing custom clips.

[CustomMultiChildLayout](flutter-docs://api/widgets/CustomMultiChildLayout)
A widget that uses a delegate to size and position multiple children.

[CustomPaint](flutter-docs://api/widgets/CustomPaint)
A widget that provides a canvas on which to draw during the paint phase.

[CustomPainter](flutter-docs://api/rendering/CustomPainter)
The interface used by [CustomPaint](flutter-docs://api/widgets/CustomPaint) (in the widgets library) and
[RenderCustomPaint](flutter-docs://api/rendering/RenderCustomPaint) (in the rendering library).

[CustomPainterSemantics](flutter-docs://api/rendering/CustomPainterSemantics)
Contains properties describing information drawn in a rectangle contained by
the [Canvas](flutter-docs://api/dart-ui/Canvas) used by a [CustomPaint](flutter-docs://api/widgets/CustomPaint).

[CustomScrollView](flutter-docs://api/widgets/CustomScrollView)
A [ScrollView](flutter-docs://api/widgets/ScrollView) that creates custom scroll effects using [slivers](flutter-docs://api/widgets/CustomScrollView/slivers).

[CustomSingleChildLayout](flutter-docs://api/widgets/CustomSingleChildLayout)
A widget that defers the layout of its single child to a delegate.

[DataCell](flutter-docs://api/material/DataCell)
The data for a cell of a [DataTable](flutter-docs://api/material/DataTable).

[DataColumn](flutter-docs://api/material/DataColumn)
Column configuration for a [DataTable](flutter-docs://api/material/DataTable).

[DataRow](flutter-docs://api/material/DataRow)
Row configuration and cell data for a [DataTable](flutter-docs://api/material/DataTable).

[DataTable](flutter-docs://api/material/DataTable)
A data table that follows the
[Material 2](https://material.io/go/design-data-tables) design specification.

[DataTableSource](flutter-docs://api/material/DataTableSource)
A data source for obtaining row data for [PaginatedDataTable](flutter-docs://api/material/PaginatedDataTable) objects.

[DataTableTheme](flutter-docs://api/material/DataTableTheme)
Applies a data table theme to descendant [DataTable](flutter-docs://api/material/DataTable) widgets.

[DataTableThemeData](flutter-docs://api/material/DataTableThemeData)
Defines default property values for descendant [DataTable](flutter-docs://api/material/DataTable) widgets.

[DatePickerDialog](flutter-docs://api/material/DatePickerDialog)
A Material-style date picker dialog.

[DatePickerTheme](flutter-docs://api/material/DatePickerTheme)
An inherited widget that defines the visual properties for
[DatePickerDialog](flutter-docs://api/material/DatePickerDialog) s in this widget's subtree.

[DatePickerThemeData](flutter-docs://api/material/DatePickerThemeData)
Overrides the default values of visual properties for descendant
[DatePickerDialog](flutter-docs://api/material/DatePickerDialog) widgets.

[DateRangePickerDialog](flutter-docs://api/material/DateRangePickerDialog)
A Material-style date range picker dialog.

[DateTimeRange](flutter-docs://api/material/DateTimeRange)<T extends [DateTime](flutter-docs://api/dart-core/DateTime)>
Encapsulates a start and end [DateTime](flutter-docs://api/dart-core/DateTime) that represent the range of dates.

[DateUtils](flutter-docs://api/material/DateUtils)
Utility functions for working with dates.

[DebugCreator](flutter-docs://api/widgets/DebugCreator)
A wrapper class for the [Element](flutter-docs://api/widgets/Element) that is the creator of a [RenderObject](flutter-docs://api/rendering/RenderObject).

[DecoratedBox](flutter-docs://api/widgets/DecoratedBox)
A widget that paints a [Decoration](flutter-docs://api/painting/Decoration) either before or after its child paints.

[DecoratedBoxTransition](flutter-docs://api/widgets/DecoratedBoxTransition)
Animated version of a [DecoratedBox](flutter-docs://api/widgets/DecoratedBox) that animates the different properties
of its [Decoration](flutter-docs://api/painting/Decoration).

[DecoratedSliver](flutter-docs://api/widgets/DecoratedSliver)
A sliver widget that paints a [Decoration](flutter-docs://api/painting/Decoration) either before or after its child
paints.

[Decoration](flutter-docs://api/painting/Decoration)
A description of a box decoration (a decoration applied to a [Rect](flutter-docs://api/dart-ui/Rect)).

[DecorationImage](flutter-docs://api/painting/DecorationImage)
An image for a box decoration.

[DecorationImagePainter](flutter-docs://api/painting/DecorationImagePainter)
The painter for a [DecorationImage](flutter-docs://api/painting/DecorationImage).

[DecorationTween](flutter-docs://api/widgets/DecorationTween)
An interpolation between two [Decoration](flutter-docs://api/painting/Decoration) s.

[DefaultAssetBundle](flutter-docs://api/widgets/DefaultAssetBundle)
A widget that determines the default asset bundle for its descendants.

[DefaultMaterialLocalizations](flutter-docs://api/material/DefaultMaterialLocalizations)
US English strings for the material widgets.

[DefaultPlatformMenuDelegate](flutter-docs://api/widgets/DefaultPlatformMenuDelegate)
The platform menu delegate that handles the built-in macOS platform menu
generation using the 'flutter/menu' channel.

[DefaultSelectionStyle](flutter-docs://api/widgets/DefaultSelectionStyle)
The selection style to apply to descendant [EditableText](flutter-docs://api/widgets/EditableText) widgets which
don't have an explicit style.

[DefaultTabController](flutter-docs://api/material/DefaultTabController)
The [TabController](flutter-docs://api/material/TabController) for descendant widgets that don't specify one
explicitly.

[DefaultTextEditingShortcuts](flutter-docs://api/widgets/DefaultTextEditingShortcuts)
A widget with the shortcuts used for the default text editing behavior.

[DefaultTextHeightBehavior](flutter-docs://api/widgets/DefaultTextHeightBehavior)
The [TextHeightBehavior](flutter-docs://api/dart-ui/TextHeightBehavior) that will apply to descendant [Text](flutter-docs://api/widgets/Text) and [EditableText](flutter-docs://api/widgets/EditableText) widgets which have not explicitly set [Text.textHeightBehavior](flutter-docs://api/widgets/Text/textHeightBehavior).

[DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle)
The text style to apply to descendant [Text](flutter-docs://api/widgets/Text) widgets which don't have an
explicit style.

[DefaultTextStyleTransition](flutter-docs://api/widgets/DefaultTextStyleTransition)
Animated version of a [DefaultTextStyle](flutter-docs://api/widgets/DefaultTextStyle) that animates the different properties
of its [TextStyle](flutter-docs://api/painting/TextStyle).

[DefaultTransitionDelegate](flutter-docs://api/widgets/DefaultTransitionDelegate)<T>
The default implementation of [TransitionDelegate](flutter-docs://api/widgets/TransitionDelegate) that the [Navigator](flutter-docs://api/widgets/Navigator) will
use if its [Navigator.transitionDelegate](flutter-docs://api/widgets/Navigator/transitionDelegate) is not specified.

[DefaultWidgetsLocalizations](flutter-docs://api/widgets/DefaultWidgetsLocalizations)
US English localizations for the widgets library.

[DeletableChipAttributes](flutter-docs://api/material/DeletableChipAttributes)
An interface for Material Design chips that can be deleted.

[DeleteCharacterIntent](flutter-docs://api/widgets/DeleteCharacterIntent)
Deletes the character before or after the caret location, based on whether
`forward` is true.

[DeleteToLineBreakIntent](flutter-docs://api/widgets/DeleteToLineBreakIntent)
Deletes from the current caret location to the previous or next soft or hard
line break, based on whether `forward` is true.

[DeleteToNextWordBoundaryIntent](flutter-docs://api/widgets/DeleteToNextWordBoundaryIntent)
Deletes from the current caret location to the previous or next word
boundary, based on whether `forward` is true.

[DesktopTextSelectionControls](flutter-docs://api/material/DesktopTextSelectionControls)
Desktop Material styled text selection controls.

[DesktopTextSelectionToolbar](flutter-docs://api/material/DesktopTextSelectionToolbar)
A Material-style desktop text selection toolbar.

[DesktopTextSelectionToolbarButton](flutter-docs://api/material/DesktopTextSelectionToolbarButton)
A [TextButton](flutter-docs://api/material/TextButton) for the Material desktop text selection toolbar.

[DesktopTextSelectionToolbarLayoutDelegate](flutter-docs://api/widgets/DesktopTextSelectionToolbarLayoutDelegate)
Positions the toolbar at [anchor](flutter-docs://api/widgets/DesktopTextSelectionToolbarLayoutDelegate/anchor) if it fits, otherwise moves it so that it
just fits fully on-screen.

[DevToolsDeepLinkProperty](flutter-docs://api/widgets/DevToolsDeepLinkProperty)
Debugging message for DevTools deep links.

[DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)
Defines diagnostics data for a [value](flutter-docs://api/foundation/DiagnosticsNode/value).

[Dialog](flutter-docs://api/material/Dialog)
A Material Design dialog.

[DialogRoute](flutter-docs://api/material/DialogRoute)<T>
A dialog route with Material entrance and exit animations,
modal barrier color, and modal barrier behavior (dialog is dismissible
with a tap on the barrier).

[DialogTheme](flutter-docs://api/material/DialogTheme)
Defines a theme for [Dialog](flutter-docs://api/material/Dialog) widgets.

[DialogThemeData](flutter-docs://api/material/DialogThemeData)
Defines default property values for descendant [Dialog](flutter-docs://api/material/Dialog) widgets.

[DirectionalCaretMovementIntent](flutter-docs://api/widgets/DirectionalCaretMovementIntent)
A [DirectionalTextEditingIntent](flutter-docs://api/widgets/DirectionalTextEditingIntent) that moves the caret or the selection to a
new location.

[DirectionalFocusAction](flutter-docs://api/widgets/DirectionalFocusAction)
An [Action](flutter-docs://api/widgets/Action) that moves the focus to the focusable node in the direction
configured by the associated [DirectionalFocusIntent.direction](flutter-docs://api/widgets/DirectionalFocusIntent/direction).

[DirectionalFocusIntent](flutter-docs://api/widgets/DirectionalFocusIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents moving to the next focusable node in the given
[direction](flutter-docs://api/widgets/DirectionalFocusIntent/direction).

[Directionality](flutter-docs://api/widgets/Directionality)
A widget that determines the ambient directionality of text and
text-direction-sensitive render objects.

[DirectionalTextEditingIntent](flutter-docs://api/widgets/DirectionalTextEditingIntent)
A text editing related [Intent](flutter-docs://api/widgets/Intent) that performs an operation towards a given
direction of the current caret location.

[DisabledChipAttributes](flutter-docs://api/material/DisabledChipAttributes)
An interface for Material Design chips that can be enabled and disabled.

[DisableWidgetInspectorScope](flutter-docs://api/widgets/DisableWidgetInspectorScope)
Disables the Flutter DevTools Widget Inspector for a [Widget](flutter-docs://api/widgets/Widget) subtree.

[DismissAction](flutter-docs://api/widgets/DismissAction)
An [Action](flutter-docs://api/widgets/Action) that dismisses the focused widget.

[Dismissible](flutter-docs://api/widgets/Dismissible)
A widget that can be dismissed by dragging in the indicated [direction](flutter-docs://api/widgets/Dismissible/direction).

[DismissIntent](flutter-docs://api/widgets/DismissIntent)
An [Intent](flutter-docs://api/widgets/Intent) that dismisses the currently focused widget.

[DismissMenuAction](flutter-docs://api/widgets/DismissMenuAction)
An action that closes all the menus associated with the given
[MenuController](flutter-docs://api/widgets/MenuController).

[DismissUpdateDetails](flutter-docs://api/widgets/DismissUpdateDetails)
Details for [DismissUpdateCallback](flutter-docs://api/widgets/DismissUpdateCallback).

[DisplayFeatureSubScreen](flutter-docs://api/widgets/DisplayFeatureSubScreen)
Positions [child](flutter-docs://api/widgets/DisplayFeatureSubScreen/child) such that it avoids overlapping any [DisplayFeature](flutter-docs://api/dart-ui/DisplayFeature) that
splits the screen into sub-screens.

[DisposableBuildContext](flutter-docs://api/widgets/DisposableBuildContext)<T extends [State](flutter-docs://api/widgets/State)<[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>>
Provides non-leaking access to a [BuildContext](flutter-docs://api/widgets/BuildContext).

[Divider](flutter-docs://api/material/Divider)
A thin horizontal line, with padding on either side.

[DividerTheme](flutter-docs://api/material/DividerTheme)
An inherited widget that defines the configuration for
[Divider](flutter-docs://api/material/Divider) s, [VerticalDivider](flutter-docs://api/material/VerticalDivider) s, dividers between [ListTile](flutter-docs://api/material/ListTile) s, and dividers
between rows in [DataTable](flutter-docs://api/material/DataTable) s in this widget's subtree.

[DividerThemeData](flutter-docs://api/material/DividerThemeData)
Defines the visual properties of [Divider](flutter-docs://api/material/Divider), [VerticalDivider](flutter-docs://api/material/VerticalDivider), dividers
between [ListTile](flutter-docs://api/material/ListTile) s, and dividers between rows in [DataTable](flutter-docs://api/material/DataTable) s.

[DoNothingAction](flutter-docs://api/widgets/DoNothingAction)
An [Action](flutter-docs://api/widgets/Action) that doesn't perform any action when invoked.

[DoNothingAndStopPropagationIntent](flutter-docs://api/widgets/DoNothingAndStopPropagationIntent)
An [Intent](flutter-docs://api/widgets/Intent) that is bound to a [DoNothingAction](flutter-docs://api/widgets/DoNothingAction), but, in addition to not
performing an action, also stops the propagation of the key event bound to
this intent to other key event handlers in the focus chain.

[DoNothingAndStopPropagationTextIntent](flutter-docs://api/widgets/DoNothingAndStopPropagationTextIntent)
An [Intent](flutter-docs://api/widgets/Intent) to send the event straight to the engine.

[DoNothingIntent](flutter-docs://api/widgets/DoNothingIntent)
An [Intent](flutter-docs://api/widgets/Intent) that is bound to a [DoNothingAction](flutter-docs://api/widgets/DoNothingAction).

[DragBoundary](flutter-docs://api/widgets/DragBoundary)
Provides a [DragBoundaryDelegate](flutter-docs://api/widgets/DragBoundaryDelegate) for its descendants whose bounds are those defined by this widget.

[DragBoundaryDelegate](flutter-docs://api/widgets/DragBoundaryDelegate)<T>
The interface for defining the algorithm for a boundary that a specified shape is dragged within.

[DragDownDetails](flutter-docs://api/gestures/DragDownDetails)
Details object for callbacks that use [GestureDragDownCallback](flutter-docs://api/gestures/GestureDragDownCallback).

[DragEndDetails](flutter-docs://api/gestures/DragEndDetails)
Details object for callbacks that use [GestureDragEndCallback](flutter-docs://api/gestures/GestureDragEndCallback).

[Draggable](flutter-docs://api/widgets/Draggable)<T extends [Object](flutter-docs://api/dart-core/Object)>
A widget that can be dragged from to a [DragTarget](flutter-docs://api/widgets/DragTarget).

[DraggableDetails](flutter-docs://api/widgets/DraggableDetails)
Represents the details when a specific pointer event occurred on
the [Draggable](flutter-docs://api/widgets/Draggable).

[DraggableScrollableActuator](flutter-docs://api/widgets/DraggableScrollableActuator)
A widget that can notify a descendent [DraggableScrollableSheet](flutter-docs://api/widgets/DraggableScrollableSheet) that it
should reset its position to the initial state.

[DraggableScrollableController](flutter-docs://api/widgets/DraggableScrollableController)
Controls a [DraggableScrollableSheet](flutter-docs://api/widgets/DraggableScrollableSheet).

[DraggableScrollableNotification](flutter-docs://api/widgets/DraggableScrollableNotification)
A [Notification](flutter-docs://api/widgets/Notification) related to the extent, which is the size, and scroll
offset, which is the position of the child list, of the
[DraggableScrollableSheet](flutter-docs://api/widgets/DraggableScrollableSheet).

[DraggableScrollableSheet](flutter-docs://api/widgets/DraggableScrollableSheet)
A container for a [Scrollable](flutter-docs://api/widgets/Scrollable) that responds to drag gestures by resizing
the scrollable until a limit is reached, and then scrolling.

[DragScrollActivity](flutter-docs://api/widgets/DragScrollActivity)
The activity a scroll view performs when the user drags their finger
across the screen.

[DragStartDetails](flutter-docs://api/gestures/DragStartDetails)
Details object for callbacks that use [GestureDragStartCallback](flutter-docs://api/gestures/GestureDragStartCallback).

[DragTarget](flutter-docs://api/widgets/DragTarget)<T extends [Object](flutter-docs://api/dart-core/Object)>
A widget that receives data when a [Draggable](flutter-docs://api/widgets/Draggable) widget is dropped.

[DragTargetDetails](flutter-docs://api/widgets/DragTargetDetails)<T>
Represents the details when a pointer event occurred on the [DragTarget](flutter-docs://api/widgets/DragTarget).

[DragUpdateDetails](flutter-docs://api/gestures/DragUpdateDetails)
Details object for callbacks that use [GestureDragUpdateCallback](flutter-docs://api/gestures/GestureDragUpdateCallback).

[Drawer](flutter-docs://api/material/Drawer)
A Material Design panel that slides in horizontally from the edge of a
[Scaffold](flutter-docs://api/material/Scaffold) to show navigation links in an application.

[DrawerButton](flutter-docs://api/material/DrawerButton)
A Material Design drawer icon button.

[DrawerButtonIcon](flutter-docs://api/material/DrawerButtonIcon)
A "drawer" icon that's appropriate for the current [TargetPlatform](flutter-docs://api/foundation/TargetPlatform).

[DrawerController](flutter-docs://api/material/DrawerController)
Provides interactive behavior for [Drawer](flutter-docs://api/material/Drawer) widgets.

[DrawerControllerState](flutter-docs://api/material/DrawerControllerState)
State for a [DrawerController](flutter-docs://api/material/DrawerController).

[DrawerHeader](flutter-docs://api/material/DrawerHeader)
The top-most region of a Material Design drawer. The header's [child](flutter-docs://api/material/DrawerHeader/child) widget, if any, is placed inside a [Container](flutter-docs://api/widgets/Container) whose [decoration](flutter-docs://api/material/DrawerHeader/decoration) can be
passed as an argument, inset by the given [padding](flutter-docs://api/material/DrawerHeader/padding).

[DrawerTheme](flutter-docs://api/material/DrawerTheme)
An inherited widget that defines visual properties for [Drawer](flutter-docs://api/material/Drawer) s in this
widget's subtree.

[DrawerThemeData](flutter-docs://api/material/DrawerThemeData)
Defines default property values for descendant [Drawer](flutter-docs://api/material/Drawer) widgets.

[DrivenScrollActivity](flutter-docs://api/widgets/DrivenScrollActivity)
An activity that drives a scroll view through a given animation.

[DropdownButton](flutter-docs://api/material/DropdownButton)<T>
A Material Design button for selecting from a list of items.

[DropdownButtonFormField](flutter-docs://api/material/DropdownButtonFormField)<T>
A [FormField](flutter-docs://api/widgets/FormField) that contains a [DropdownButton](flutter-docs://api/material/DropdownButton).

[DropdownButtonHideUnderline](flutter-docs://api/material/DropdownButtonHideUnderline)
An inherited widget that causes any descendant [DropdownButton](flutter-docs://api/material/DropdownButton) widgets to not include their regular underline.

[DropdownMenu](flutter-docs://api/material/DropdownMenu)<T>
A dropdown menu that can be opened from a [TextField](flutter-docs://api/material/TextField). The selected
menu item is displayed in that field.

[DropdownMenuEntry](flutter-docs://api/material/DropdownMenuEntry)<T>
Defines a [DropdownMenu](flutter-docs://api/material/DropdownMenu) menu button that represents one item view in the menu.

[DropdownMenuFormField](flutter-docs://api/material/DropdownMenuFormField)<T>
A [FormField](flutter-docs://api/widgets/FormField) that contains a [DropdownMenu](flutter-docs://api/material/DropdownMenu).

[DropdownMenuItem](flutter-docs://api/material/DropdownMenuItem)<T>
An item in a menu created by a [DropdownButton](flutter-docs://api/material/DropdownButton).

[DropdownMenuTheme](flutter-docs://api/material/DropdownMenuTheme)
An inherited widget that defines the visual properties for [DropdownMenu](flutter-docs://api/material/DropdownMenu) s in this widget's subtree.

[DropdownMenuThemeData](flutter-docs://api/material/DropdownMenuThemeData)
Overrides the default values of visual properties for descendant [DropdownMenu](flutter-docs://api/material/DropdownMenu) widgets.

[DropRangeSliderValueIndicatorShape](flutter-docs://api/material/DropRangeSliderValueIndicatorShape)
The shape of a Material 3 [RangeSlider](flutter-docs://api/material/RangeSlider)'s value indicators.

[DropSliderValueIndicatorShape](flutter-docs://api/material/DropSliderValueIndicatorShape)
The default shape of a Material 3 [Slider](flutter-docs://api/material/Slider)'s value indicator.

[DualTransitionBuilder](flutter-docs://api/widgets/DualTransitionBuilder)
A transition builder that animates its [child](flutter-docs://api/widgets/DualTransitionBuilder/child) based on the
[AnimationStatus](flutter-docs://api/animation/AnimationStatus) of the provided [animation](flutter-docs://api/widgets/DualTransitionBuilder/animation).

[Durations](flutter-docs://api/material/Durations)
The set of durations in the Material specification.

[Easing](flutter-docs://api/material/Easing)
The set of easing curves in the Material specification.

[EdgeDraggingAutoScroller](flutter-docs://api/widgets/EdgeDraggingAutoScroller)
An auto scroller that scrolls the [scrollable](flutter-docs://api/widgets/EdgeDraggingAutoScroller/scrollable) if a drag gesture drags close
to its edge.

[EdgeInsets](flutter-docs://api/painting/EdgeInsets)
An immutable set of offsets in each of the four cardinal directions.

[EdgeInsetsDirectional](flutter-docs://api/painting/EdgeInsetsDirectional)
An immutable set of offsets in each of the four cardinal directions, but
whose horizontal components are dependent on the writing direction.

[EdgeInsetsGeometry](flutter-docs://api/painting/EdgeInsetsGeometry)
Base class for [EdgeInsets](flutter-docs://api/painting/EdgeInsets) that allows for text-direction aware
resolution.

[EdgeInsetsGeometryTween](flutter-docs://api/widgets/EdgeInsetsGeometryTween)
An interpolation between two [EdgeInsetsGeometry](flutter-docs://api/painting/EdgeInsetsGeometry) s.

[EdgeInsetsTween](flutter-docs://api/widgets/EdgeInsetsTween)
An interpolation between two [EdgeInsets](flutter-docs://api/painting/EdgeInsets) s.

[EditableText](flutter-docs://api/widgets/EditableText)
A basic text input field.

[EditableTextState](flutter-docs://api/widgets/EditableTextState)
State for an [EditableText](flutter-docs://api/widgets/EditableText).

[EditableTextTapOutsideIntent](flutter-docs://api/widgets/EditableTextTapOutsideIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a tap outside the field.

[EditableTextTapUpOutsideIntent](flutter-docs://api/widgets/EditableTextTapUpOutsideIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a tap outside the field.

[ElasticInCurve](flutter-docs://api/animation/ElasticInCurve)
An oscillating curve that grows in magnitude while overshooting its bounds.

[ElasticInOutCurve](flutter-docs://api/animation/ElasticInOutCurve)
An oscillating curve that grows and then shrinks in magnitude while
overshooting its bounds.

[ElasticOutCurve](flutter-docs://api/animation/ElasticOutCurve)
An oscillating curve that shrinks in magnitude while overshooting its bounds.

[Element](flutter-docs://api/widgets/Element)
An instantiation of a [Widget](flutter-docs://api/widgets/Widget) at a particular location in the tree.

[ElevatedButton](flutter-docs://api/material/ElevatedButton)
A Material Design "elevated button".

[ElevatedButtonTheme](flutter-docs://api/material/ElevatedButtonTheme)
Overrides the default [ButtonStyle](flutter-docs://api/material/ButtonStyle) of its [ElevatedButton](flutter-docs://api/material/ElevatedButton) descendants.

[ElevatedButtonThemeData](flutter-docs://api/material/ElevatedButtonThemeData)
A [ButtonStyle](flutter-docs://api/material/ButtonStyle) that overrides the default appearance of
[ElevatedButton](flutter-docs://api/material/ElevatedButton) s when it's used with [ElevatedButtonTheme](flutter-docs://api/material/ElevatedButtonTheme) or with the
overall [Theme](flutter-docs://api/material/Theme)'s [ThemeData.elevatedButtonTheme](flutter-docs://api/material/ThemeData/elevatedButtonTheme).

[ElevationOverlay](flutter-docs://api/material/ElevationOverlay)
A utility class for dealing with the overlay color needed
to indicate elevation of surfaces.

[EmptyTextSelectionControls](flutter-docs://api/widgets/EmptyTextSelectionControls)
Text selection controls that do not show any toolbars or handles.

[EnableWidgetInspectorScope](flutter-docs://api/widgets/EnableWidgetInspectorScope)
Enables the Flutter DevTools Widget Inspector for a [Widget](flutter-docs://api/widgets/Widget) subtree.

[EndDrawerButton](flutter-docs://api/material/EndDrawerButton)
A Material Design end drawer icon button.

[EndDrawerButtonIcon](flutter-docs://api/material/EndDrawerButtonIcon)
A "end drawer" icon that's appropriate for the current [TargetPlatform](flutter-docs://api/foundation/TargetPlatform).

[ErrorDescription](flutter-docs://api/foundation/ErrorDescription)
An explanation of the problem and its cause, any information that may help
track down the problem, background information, etc.

[ErrorHint](flutter-docs://api/foundation/ErrorHint)
An [ErrorHint](flutter-docs://api/foundation/ErrorHint) provides specific, non-obvious advice that may be applicable.

[ErrorSummary](flutter-docs://api/foundation/ErrorSummary)
A short (one line) description of the problem that was detected.

[ErrorWidget](flutter-docs://api/widgets/ErrorWidget)
A widget that renders an exception's message.

[ExactAssetImage](flutter-docs://api/painting/ExactAssetImage)
Fetches an image from an [AssetBundle](flutter-docs://api/services/AssetBundle), associating it with the given scale.

[ExcludeFocus](flutter-docs://api/widgets/ExcludeFocus)
A widget that controls whether or not the descendants of this widget are
focusable.

[ExcludeFocusTraversal](flutter-docs://api/widgets/ExcludeFocusTraversal)
A widget that controls whether or not the descendants of this widget are
traversable.

[ExcludeSemantics](flutter-docs://api/widgets/ExcludeSemantics)
A widget that drops all the semantics of its descendants.

[Expanded](flutter-docs://api/widgets/Expanded)
A widget that expands a child of a [Row](flutter-docs://api/widgets/Row), [Column](flutter-docs://api/widgets/Column), or [Flex](flutter-docs://api/widgets/Flex) so that the child fills the available space.

[ExpandIcon](flutter-docs://api/material/ExpandIcon)
A widget representing a rotating expand/collapse button. The icon rotates
180 degrees when pressed, then reverts the animation on a second press.
The underlying icon is [Icons.expand_more](flutter-docs://api/material/Icons/expand_more).

[ExpandSelectionToDocumentBoundaryIntent](flutter-docs://api/widgets/ExpandSelectionToDocumentBoundaryIntent)
Expands the current selection to the document boundary in the direction
given by [forward](flutter-docs://api/widgets/DirectionalTextEditingIntent/forward).

[ExpandSelectionToLineBreakIntent](flutter-docs://api/widgets/ExpandSelectionToLineBreakIntent)
Expands the current selection to the closest line break in the direction
given by [forward](flutter-docs://api/widgets/DirectionalTextEditingIntent/forward).

[Expansible](flutter-docs://api/widgets/Expansible)
A [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) that expands and collapses.

[ExpansibleController](flutter-docs://api/widgets/ExpansibleController)
A controller for managing the expansion state of an [Expansible](flutter-docs://api/widgets/Expansible).

[ExpansionPanel](flutter-docs://api/material/ExpansionPanel)
A material expansion panel. It has a header and a body and can be either
expanded or collapsed. The body of the panel is only visible when it is
expanded.

[ExpansionPanelList](flutter-docs://api/material/ExpansionPanelList)
A material expansion panel list that lays out its children and animates
expansions.

[ExpansionPanelRadio](flutter-docs://api/material/ExpansionPanelRadio)
An expansion panel that allows for radio-like functionality.
This means that at any given time, at most, one [ExpansionPanelRadio](flutter-docs://api/material/ExpansionPanelRadio) can remain expanded.

[ExpansionTile](flutter-docs://api/material/ExpansionTile)
A single-line [ListTile](flutter-docs://api/material/ListTile) with an expansion arrow icon that expands or collapses
the tile to reveal or hide the [children](flutter-docs://api/material/ExpansionTile/children).

[ExpansionTileTheme](flutter-docs://api/material/ExpansionTileTheme)
Overrides the default [ExpansionTileTheme](flutter-docs://api/material/ExpansionTileTheme) of its [ExpansionTile](flutter-docs://api/material/ExpansionTile) descendants.

[ExpansionTileThemeData](flutter-docs://api/material/ExpansionTileThemeData)
Used with [ExpansionTileTheme](flutter-docs://api/material/ExpansionTileTheme) to define default property values for
descendant [ExpansionTile](flutter-docs://api/material/ExpansionTile) widgets.

[ExtendSelectionByCharacterIntent](flutter-docs://api/widgets/ExtendSelectionByCharacterIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the previous or the next character
boundary.

[ExtendSelectionByPageIntent](flutter-docs://api/widgets/ExtendSelectionByPageIntent)
Scrolls up or down by page depending on the [forward](flutter-docs://api/widgets/DirectionalTextEditingIntent/forward) parameter.
Extends the selection up or down by page based on the [forward](flutter-docs://api/widgets/DirectionalTextEditingIntent/forward) parameter.

[ExtendSelectionToDocumentBoundaryIntent](flutter-docs://api/widgets/ExtendSelectionToDocumentBoundaryIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the start or the end of the document.

[ExtendSelectionToLineBreakIntent](flutter-docs://api/widgets/ExtendSelectionToLineBreakIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the closest line break in the direction
given by [forward](flutter-docs://api/widgets/DirectionalTextEditingIntent/forward).

[ExtendSelectionToNextParagraphBoundaryIntent](flutter-docs://api/widgets/ExtendSelectionToNextParagraphBoundaryIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the previous or the next paragraph
boundary.

[ExtendSelectionToNextParagraphBoundaryOrCaretLocationIntent](flutter-docs://api/widgets/ExtendSelectionToNextParagraphBoundaryOrCaretLocationIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the previous or the next paragraph
boundary depending on the [forward](flutter-docs://api/widgets/DirectionalTextEditingIntent/forward) parameter.

[ExtendSelectionToNextWordBoundaryIntent](flutter-docs://api/widgets/ExtendSelectionToNextWordBoundaryIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the previous or the next word
boundary.

[ExtendSelectionToNextWordBoundaryOrCaretLocationIntent](flutter-docs://api/widgets/ExtendSelectionToNextWordBoundaryOrCaretLocationIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the previous or the next word
boundary, or the [TextSelection.base](flutter-docs://api/services/TextSelection/base) position if it's closer in the move
direction.

[ExtendSelectionVerticallyToAdjacentLineIntent](flutter-docs://api/widgets/ExtendSelectionVerticallyToAdjacentLineIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the closest position on the adjacent
line.

[ExtendSelectionVerticallyToAdjacentPageIntent](flutter-docs://api/widgets/ExtendSelectionVerticallyToAdjacentPageIntent)
Expands, or moves the current selection from the current
[TextSelection.extent](flutter-docs://api/services/TextSelection/extent) position to the closest position on the adjacent
page.

[FadeForwardsPageTransitionsBuilder](flutter-docs://api/material/FadeForwardsPageTransitionsBuilder)
Used by [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) to define a horizontal [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) page
transition animation that looks like the default page transition
used on Android U.

[FadeInImage](flutter-docs://api/widgets/FadeInImage)
An image that shows a [placeholder](flutter-docs://api/widgets/FadeInImage/placeholder) image while the target [image](flutter-docs://api/widgets/FadeInImage/image) is
loading, then fades in the new image when it loads.

[FadeTransition](flutter-docs://api/widgets/FadeTransition)
Animates the opacity of a widget.

[FadeUpwardsPageTransitionsBuilder](flutter-docs://api/material/FadeUpwardsPageTransitionsBuilder)
Used by [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) to define a vertically fading
[MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) page transition animation that looks like
the default page transition used on Android O.

[Feedback](flutter-docs://api/widgets/Feedback)
Provides platform-specific acoustic and/or haptic feedback for certain
actions.

[FileImage](flutter-docs://api/painting/FileImage)
Decodes the given [File](flutter-docs://api/dart-io/File) object as an image, associating it with the given
scale.

[FilledButton](flutter-docs://api/material/FilledButton)
A Material Design filled button.

[FilledButtonTheme](flutter-docs://api/material/FilledButtonTheme)
Overrides the default [ButtonStyle](flutter-docs://api/material/ButtonStyle) of its [FilledButton](flutter-docs://api/material/FilledButton) descendants.

[FilledButtonThemeData](flutter-docs://api/material/FilledButtonThemeData)
A [ButtonStyle](flutter-docs://api/material/ButtonStyle) that overrides the default appearance of
[FilledButton](flutter-docs://api/material/FilledButton) s when it's used with [FilledButtonTheme](flutter-docs://api/material/FilledButtonTheme) or with the
overall [Theme](flutter-docs://api/material/Theme)'s [ThemeData.filledButtonTheme](flutter-docs://api/material/ThemeData/filledButtonTheme).

[FilterChip](flutter-docs://api/material/FilterChip)
A Material Design filter chip.

[FittedBox](flutter-docs://api/widgets/FittedBox)
Scales and positions its child within itself according to [fit](flutter-docs://api/widgets/FittedBox/fit).

[FittedSizes](flutter-docs://api/painting/FittedSizes)
The pair of sizes returned by [applyBoxFit](flutter-docs://api/painting/applyBoxFit).

[FixedColumnWidth](flutter-docs://api/rendering/FixedColumnWidth)
Sizes the column to a specific number of pixels.

[FixedExtentMetrics](flutter-docs://api/widgets/FixedExtentMetrics)
Metrics for a [ScrollPosition](flutter-docs://api/widgets/ScrollPosition) to a scroll view with fixed item sizes.

[FixedExtentScrollController](flutter-docs://api/widgets/FixedExtentScrollController)
A controller for scroll views whose items have the same size.

[FixedExtentScrollPhysics](flutter-docs://api/widgets/FixedExtentScrollPhysics)
A snapping physics that always lands directly on items instead of anywhere
within the scroll extent.

[FixedScrollMetrics](flutter-docs://api/widgets/FixedScrollMetrics)
An immutable snapshot of values associated with a [Scrollable](flutter-docs://api/widgets/Scrollable) viewport.

[Flex](flutter-docs://api/widgets/Flex)
A widget that displays its children in a one-dimensional array.

[FlexColumnWidth](flutter-docs://api/rendering/FlexColumnWidth)
Sizes the column by taking a part of the remaining space once all
the other columns have been laid out.

[Flexible](flutter-docs://api/widgets/Flexible)
A widget that controls how a child of a [Row](flutter-docs://api/widgets/Row), [Column](flutter-docs://api/widgets/Column), or [Flex](flutter-docs://api/widgets/Flex) flexes.

[FlexibleSpaceBar](flutter-docs://api/material/FlexibleSpaceBar)
The part of a Material Design [AppBar](flutter-docs://api/material/AppBar) that expands, collapses, and
stretches.

[FlexibleSpaceBarSettings](flutter-docs://api/material/FlexibleSpaceBarSettings)
Provides sizing and opacity information to a [FlexibleSpaceBar](flutter-docs://api/material/FlexibleSpaceBar).

[FlippedCurve](flutter-docs://api/animation/FlippedCurve)
A curve that is the reversed inversion of its given curve.

[FlippedTweenSequence](flutter-docs://api/animation/FlippedTweenSequence)
Enables creating a flipped [Animation](flutter-docs://api/animation/Animation) whose value is defined by a sequence
of [Tween](flutter-docs://api/animation/Tween) s.

[FloatingActionButton](flutter-docs://api/material/FloatingActionButton)
A Material Design floating action button.

[FloatingActionButtonAnimator](flutter-docs://api/material/FloatingActionButtonAnimator)
Provider of animations to move the [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) between [FloatingActionButtonLocation](flutter-docs://api/material/FloatingActionButtonLocation) s.

[FloatingActionButtonLocation](flutter-docs://api/material/FloatingActionButtonLocation)
An object that defines a position for the [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) based on the [Scaffold](flutter-docs://api/material/Scaffold)'s [ScaffoldPrelayoutGeometry](flutter-docs://api/material/ScaffoldPrelayoutGeometry).

[FloatingActionButtonThemeData](flutter-docs://api/material/FloatingActionButtonThemeData)
Defines default property values for descendant [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) widgets.

[FloatingLabelAlignment](flutter-docs://api/material/FloatingLabelAlignment)
Defines **where** the floating label should be displayed within an
[InputDecorator](flutter-docs://api/material/InputDecorator).

[Flow](flutter-docs://api/widgets/Flow)
A widget that sizes and positions children efficiently, according to the
logic in a [FlowDelegate](flutter-docs://api/rendering/FlowDelegate).

[FlowDelegate](flutter-docs://api/rendering/FlowDelegate)
A delegate that controls the appearance of a flow layout.

[FlowPaintingContext](flutter-docs://api/rendering/FlowPaintingContext)
A context in which a [FlowDelegate](flutter-docs://api/rendering/FlowDelegate) paints.

[FlutterErrorDetails](flutter-docs://api/foundation/FlutterErrorDetails)
Class for information provided to [FlutterExceptionHandler](flutter-docs://api/foundation/FlutterExceptionHandler) callbacks.

[FlutterLogo](flutter-docs://api/widgets/FlutterLogo)
The Flutter logo, in widget form. This widget respects the [IconTheme](flutter-docs://api/widgets/IconTheme).
For guidelines on using the Flutter logo, visit <https://flutter.dev/brand>.

[FlutterLogoDecoration](flutter-docs://api/painting/FlutterLogoDecoration)
An immutable description of how to paint Flutter's logo.

[Focus](flutter-docs://api/widgets/Focus)
A widget that manages a [FocusNode](flutter-docs://api/widgets/FocusNode) to allow keyboard focus to be given
to this widget and its descendants.

[FocusableActionDetector](flutter-docs://api/widgets/FocusableActionDetector)
A widget that combines the functionality of [Actions](flutter-docs://api/widgets/Actions), [Shortcuts](flutter-docs://api/widgets/Shortcuts),
[MouseRegion](flutter-docs://api/widgets/MouseRegion) and a [Focus](flutter-docs://api/widgets/Focus) widget to create a detector that defines actions
and key bindings, and provides callbacks for handling focus and hover
highlights.

[FocusAttachment](flutter-docs://api/widgets/FocusAttachment)
An attachment point for a [FocusNode](flutter-docs://api/widgets/FocusNode).

[FocusManager](flutter-docs://api/widgets/FocusManager)
Manages the focus tree.

[FocusNode](flutter-docs://api/widgets/FocusNode)
An object that can be used by a stateful widget to obtain the keyboard focus
and to handle keyboard events.

[FocusOrder](flutter-docs://api/widgets/FocusOrder)
Base class for all sort orders for [OrderedTraversalPolicy](flutter-docs://api/widgets/OrderedTraversalPolicy) traversal.

[FocusScope](flutter-docs://api/widgets/FocusScope)
A [FocusScope](flutter-docs://api/widgets/FocusScope) is similar to a [Focus](flutter-docs://api/widgets/Focus), but also serves as a scope for its
descendants, restricting focus traversal to the scoped controls.

[FocusScopeNode](flutter-docs://api/widgets/FocusScopeNode)
A subclass of [FocusNode](flutter-docs://api/widgets/FocusNode) that acts as a scope for its descendants,
maintaining information about which descendant is currently or was last
focused.

[FocusTraversalGroup](flutter-docs://api/widgets/FocusTraversalGroup)
A widget that describes the inherited focus policy for focus traversal for
its descendants, grouping them into a separate traversal group.

[FocusTraversalOrder](flutter-docs://api/widgets/FocusTraversalOrder)
An inherited widget that describes the order in which its child subtree
should be traversed.

[FocusTraversalPolicy](flutter-docs://api/widgets/FocusTraversalPolicy)
Determines how focusable widgets are traversed within a [FocusTraversalGroup](flutter-docs://api/widgets/FocusTraversalGroup).

[FontFeature](flutter-docs://api/dart-ui/FontFeature)
A feature tag and value that affect the selection of glyphs in a font.

[FontVariation](flutter-docs://api/dart-ui/FontVariation)
An axis tag and value that can be used to customize variable fonts.

[FontWeight](flutter-docs://api/dart-ui/FontWeight)
The thickness of the glyphs used to draw the text.

[ForcePressDetails](flutter-docs://api/gestures/ForcePressDetails)
Details object for callbacks that use [GestureForcePressStartCallback](flutter-docs://api/gestures/GestureForcePressStartCallback),
[GestureForcePressPeakCallback](flutter-docs://api/gestures/GestureForcePressPeakCallback), [GestureForcePressEndCallback](flutter-docs://api/gestures/GestureForcePressEndCallback) or
[GestureForcePressUpdateCallback](flutter-docs://api/gestures/GestureForcePressUpdateCallback).

[Form](flutter-docs://api/widgets/Form)
An optional container for grouping together multiple form field widgets
(e.g. [TextField](flutter-docs://api/material/TextField) widgets).

[FormField](flutter-docs://api/widgets/FormField)<T>
A single form field.

[FormFieldState](flutter-docs://api/widgets/FormFieldState)<T>
The current state of a [FormField](flutter-docs://api/widgets/FormField). Passed to the [FormFieldBuilder](flutter-docs://api/widgets/FormFieldBuilder) method
for use in constructing the form field's widget.

[FormState](flutter-docs://api/widgets/FormState)
State associated with a [Form](flutter-docs://api/widgets/Form) widget.

[FractionallySizedBox](flutter-docs://api/widgets/FractionallySizedBox)
A widget that sizes its child to a fraction of the total available space.
For more details about the layout algorithm, see
[RenderFractionallySizedOverflowBox](flutter-docs://api/rendering/RenderFractionallySizedOverflowBox).

[FractionalOffset](flutter-docs://api/painting/FractionalOffset)
An offset that's expressed as a fraction of a [Size](flutter-docs://api/dart-ui/Size).

[FractionalOffsetTween](flutter-docs://api/rendering/FractionalOffsetTween)
An interpolation between two fractional offsets.

[FractionalTranslation](flutter-docs://api/widgets/FractionalTranslation)
Applies a translation transformation before painting its child.

[FractionColumnWidth](flutter-docs://api/rendering/FractionColumnWidth)
Sizes the column to a fraction of the table's constraints' maxWidth.

[FutureBuilder](flutter-docs://api/widgets/FutureBuilder)<T>
A widget that builds itself based on the latest snapshot of interaction with
a [Future](flutter-docs://api/dart-async/Future).

[GappedRangeSliderTrackShape](flutter-docs://api/material/GappedRangeSliderTrackShape)
The [GappedRangeSliderTrackShape](flutter-docs://api/material/GappedRangeSliderTrackShape) consists of active and inactive
tracks. The active track uses the [SliderThemeData.activeTrackColor](flutter-docs://api/material/SliderThemeData/activeTrackColor) and the
inactive tracks uses the [SliderThemeData.inactiveTrackColor](flutter-docs://api/material/SliderThemeData/inactiveTrackColor).

[GappedSliderTrackShape](flutter-docs://api/material/GappedSliderTrackShape)
The gapped shape of a [Slider](flutter-docs://api/material/Slider)'s track.

[GestureDetector](flutter-docs://api/widgets/GestureDetector)
A widget that detects gestures.

[GestureRecognizerFactory](flutter-docs://api/widgets/GestureRecognizerFactory)<T extends [GestureRecognizer](flutter-docs://api/gestures/GestureRecognizer)>
Factory for creating gesture recognizers.

[GestureRecognizerFactoryWithHandlers](flutter-docs://api/widgets/GestureRecognizerFactoryWithHandlers)<T extends [GestureRecognizer](flutter-docs://api/gestures/GestureRecognizer)>
Factory for creating gesture recognizers that delegates to callbacks.

[GlobalKey](flutter-docs://api/widgets/GlobalKey)<T extends [State](flutter-docs://api/widgets/State)<[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>>
A key that is unique across the entire app.

[GlobalObjectKey](flutter-docs://api/widgets/GlobalObjectKey)<T extends [State](flutter-docs://api/widgets/State)<[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>>
A global key that takes its identity from the object used as its value.

[GlowingOverscrollIndicator](flutter-docs://api/widgets/GlowingOverscrollIndicator)
A visual indication that a scroll view has overscrolled.

[GlyphInfo](flutter-docs://api/dart-ui/GlyphInfo)
The measurements of a character (or a sequence of visually connected
characters) within a paragraph.

[Gradient](flutter-docs://api/painting/Gradient)
A 2D gradient.

[GradientRotation](flutter-docs://api/painting/GradientRotation)
A [GradientTransform](flutter-docs://api/painting/GradientTransform) that rotates the gradient around the center-point of
its bounding box.

[GradientTransform](flutter-docs://api/painting/GradientTransform)
Base class for transforming gradient shaders without applying the same
transform to the entire canvas.

[GregorianCalendarDelegate](flutter-docs://api/material/GregorianCalendarDelegate)
A [CalendarDelegate](flutter-docs://api/material/CalendarDelegate) implementation for the Gregorian calendar system.

[GridPaper](flutter-docs://api/widgets/GridPaper)
A widget that draws a rectilinear grid of lines one pixel wide.

[GridTile](flutter-docs://api/material/GridTile)
A tile in a Material Design grid list.

[GridTileBar](flutter-docs://api/material/GridTileBar)
A header used in a Material Design [GridTile](flutter-docs://api/material/GridTile).

[GridView](flutter-docs://api/widgets/GridView)
A scrollable, 2D array of widgets.

[HandleRangeSliderThumbShape](flutter-docs://api/material/HandleRangeSliderThumbShape)
The bar shape of [RangeSlider](flutter-docs://api/material/RangeSlider)'s thumbs.

[HandleThumbShape](flutter-docs://api/material/HandleThumbShape)
The bar shape of a [Slider](flutter-docs://api/material/Slider)'s thumb.

[Hero](flutter-docs://api/widgets/Hero)
A widget that marks its child as being a candidate for
[hero animations](https://docs.flutter.dev/ui/animations/hero-animations).

[HeroController](flutter-docs://api/widgets/HeroController)
A [Navigator](flutter-docs://api/widgets/Navigator) observer that manages [Hero](flutter-docs://api/widgets/Hero) transitions.

[HeroControllerScope](flutter-docs://api/widgets/HeroControllerScope)
An inherited widget to host a hero controller.

[HeroMode](flutter-docs://api/widgets/HeroMode)
Enables or disables [Hero](flutter-docs://api/widgets/Hero) es in the widget subtree.

[HoldScrollActivity](flutter-docs://api/widgets/HoldScrollActivity)
A scroll activity that does nothing but can be released to resume
normal idle behavior.

[HSLColor](flutter-docs://api/painting/HSLColor)
A color represented using [alpha](flutter-docs://api/painting/HSLColor/alpha), [hue](flutter-docs://api/painting/HSLColor/hue), [saturation](flutter-docs://api/painting/HSLColor/saturation), and [lightness](flutter-docs://api/painting/HSLColor/lightness).

[HSVColor](flutter-docs://api/painting/HSVColor)
A color represented using [alpha](flutter-docs://api/painting/HSVColor/alpha), [hue](flutter-docs://api/painting/HSVColor/hue), [saturation](flutter-docs://api/painting/HSVColor/saturation), and [value](flutter-docs://api/painting/HSVColor/value).

[HtmlElementView](flutter-docs://api/widgets/HtmlElementView)
Embeds an HTML element in the Widget hierarchy in Flutter web.

[Icon](flutter-docs://api/widgets/Icon)
A graphical icon widget drawn with a glyph from a font described in
an [IconData](flutter-docs://api/widgets/IconData) such as material's predefined [IconData](flutter-docs://api/widgets/IconData) s in [Icons](flutter-docs://api/material/Icons).

[IconButton](flutter-docs://api/material/IconButton)
A Material Design icon button.

[IconButtonTheme](flutter-docs://api/material/IconButtonTheme)
Overrides the default [ButtonStyle](flutter-docs://api/material/ButtonStyle) of its [IconButton](flutter-docs://api/material/IconButton) descendants.

[IconButtonThemeData](flutter-docs://api/material/IconButtonThemeData)
A [ButtonStyle](flutter-docs://api/material/ButtonStyle) that overrides the default appearance of
[IconButton](flutter-docs://api/material/IconButton) s when it's used with the [IconButton](flutter-docs://api/material/IconButton), the [IconButtonTheme](flutter-docs://api/material/IconButtonTheme) or the
overall [Theme](flutter-docs://api/material/Theme)'s [ThemeData.iconButtonTheme](flutter-docs://api/material/ThemeData/iconButtonTheme).

[IconData](flutter-docs://api/widgets/IconData)
A description of an icon fulfilled by a font glyph.

[IconDataProperty](flutter-docs://api/widgets/IconDataProperty)
[DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) that has an [IconData](flutter-docs://api/widgets/IconData) as value.

[Icons](flutter-docs://api/material/Icons)
Identifiers for the supported [Material Icons](https://material.io/resources/icons).

[IconTheme](flutter-docs://api/widgets/IconTheme)
Controls the default properties of icons in a widget subtree.

[IconThemeData](flutter-docs://api/widgets/IconThemeData)
Defines the size, font variations, color, opacity, and shadows of icons.

[IdleScrollActivity](flutter-docs://api/widgets/IdleScrollActivity)
A scroll activity that does nothing.

[IgnoreBaseline](flutter-docs://api/widgets/IgnoreBaseline)
A widget that causes the parent to ignore the [child](flutter-docs://api/widgets/SingleChildRenderObjectWidget/child) for the purposes
of baseline alignment.

[IgnorePointer](flutter-docs://api/widgets/IgnorePointer)
A widget that is invisible during hit testing.

[Image](flutter-docs://api/widgets/Image)
A widget that displays an image.

[ImageCache](flutter-docs://api/painting/ImageCache)
Class for caching images.

[ImageCacheStatus](flutter-docs://api/painting/ImageCacheStatus)
Information about how the [ImageCache](flutter-docs://api/painting/ImageCache) is tracking an image.

[ImageChunkEvent](flutter-docs://api/painting/ImageChunkEvent)
An immutable notification of image bytes that have been incrementally loaded.

[ImageConfiguration](flutter-docs://api/painting/ImageConfiguration)
Configuration information passed to the [ImageProvider.resolve](flutter-docs://api/painting/ImageProvider/resolve) method to
select a specific image.

[ImageFiltered](flutter-docs://api/widgets/ImageFiltered)
Applies an [ImageFilter](flutter-docs://api/dart-ui/ImageFilter) to its child.

[ImageIcon](flutter-docs://api/widgets/ImageIcon)
An icon that comes from an [ImageProvider](flutter-docs://api/painting/ImageProvider), e.g. an [AssetImage](flutter-docs://api/painting/AssetImage).

[ImageInfo](flutter-docs://api/painting/ImageInfo)
A [dart:ui.Image](flutter-docs://api/dart-ui/Image) object with its corresponding scale.

[ImageProvider](flutter-docs://api/painting/ImageProvider)<T extends [Object](flutter-docs://api/dart-core/Object)>
Identifies an image without committing to the precise final asset. This
allows a set of images to be identified and for the precise image to later
be resolved based on the environment, e.g. the device pixel ratio.

[ImageShader](flutter-docs://api/dart-ui/ImageShader)
A shader (as used by [Paint.shader](flutter-docs://api/dart-ui/Paint/shader)) that tiles an image.

[ImageSizeInfo](flutter-docs://api/painting/ImageSizeInfo)
Tracks the bytes used by a [dart:ui.Image](flutter-docs://api/dart-ui/Image) compared to the bytes needed to
paint that image without scaling it.

[ImageStream](flutter-docs://api/painting/ImageStream)
A handle to an image resource.

[ImageStreamCompleter](flutter-docs://api/painting/ImageStreamCompleter)
Base class for those that manage the loading of [dart:ui.Image](flutter-docs://api/dart-ui/Image) objects for
[ImageStream](flutter-docs://api/painting/ImageStream) s.

[ImageStreamCompleterHandle](flutter-docs://api/painting/ImageStreamCompleterHandle)
An opaque handle that keeps an [ImageStreamCompleter](flutter-docs://api/painting/ImageStreamCompleter) alive even if it has
lost its last listener.

[ImageStreamListener](flutter-docs://api/painting/ImageStreamListener)
Interface for receiving notifications about the loading of an image.

[ImplicitlyAnimatedWidget](flutter-docs://api/widgets/ImplicitlyAnimatedWidget)
An abstract class for building widgets that animate changes to their
properties.

[ImplicitlyAnimatedWidgetState](flutter-docs://api/widgets/ImplicitlyAnimatedWidgetState)<T extends [ImplicitlyAnimatedWidget](flutter-docs://api/widgets/ImplicitlyAnimatedWidget)>
A base class for the `State` of widgets with implicit animations.

[IndexedSemantics](flutter-docs://api/widgets/IndexedSemantics)
A widget that annotates the child semantics with an index.

[IndexedSlot](flutter-docs://api/widgets/IndexedSlot)<T extends [Element](flutter-docs://api/widgets/Element)?>
A value for [Element.slot](flutter-docs://api/widgets/Element/slot) used for children of
[MultiChildRenderObjectElement](flutter-docs://api/widgets/MultiChildRenderObjectElement) s.

[IndexedStack](flutter-docs://api/widgets/IndexedStack)
A [Stack](flutter-docs://api/widgets/Stack) that shows a single child from a list of children.

[InheritedElement](flutter-docs://api/widgets/InheritedElement)
An [Element](flutter-docs://api/widgets/Element) that uses an [InheritedWidget](flutter-docs://api/widgets/InheritedWidget) as its configuration.

[InheritedModel](flutter-docs://api/widgets/InheritedModel)<T>
An [InheritedWidget](flutter-docs://api/widgets/InheritedWidget) that's intended to be used as the base class for models
whose dependents may only depend on one part or "aspect" of the overall
model.

[InheritedModelElement](flutter-docs://api/widgets/InheritedModelElement)<T>
An [Element](flutter-docs://api/widgets/Element) that uses a [InheritedModel](flutter-docs://api/widgets/InheritedModel) as its configuration.

[InheritedNotifier](flutter-docs://api/widgets/InheritedNotifier)<T extends [Listenable](flutter-docs://api/foundation/Listenable)>
An inherited widget for a [Listenable](flutter-docs://api/foundation/Listenable) [notifier](flutter-docs://api/widgets/InheritedNotifier/notifier), which updates its
dependencies when the [notifier](flutter-docs://api/widgets/InheritedNotifier/notifier) is triggered.

[InheritedTheme](flutter-docs://api/widgets/InheritedTheme)
An [InheritedWidget](flutter-docs://api/widgets/InheritedWidget) that defines visual properties like colors
and text styles, which the [child](flutter-docs://api/widgets/ProxyWidget/child)'s subtree depends on.

[InheritedWidget](flutter-docs://api/widgets/InheritedWidget)
Base class for widgets that efficiently propagate information down the tree.

[Ink](flutter-docs://api/material/Ink)
A convenience widget for drawing images and other decorations on [Material](flutter-docs://api/material/Material) widgets, so that [InkWell](flutter-docs://api/material/InkWell) and [InkResponse](flutter-docs://api/material/InkResponse) splashes will render over them.

[InkDecoration](flutter-docs://api/material/InkDecoration)
A decoration on a part of a [Material](flutter-docs://api/material/Material).

[InkFeature](flutter-docs://api/material/InkFeature)
A visual reaction on a piece of [Material](flutter-docs://api/material/Material).

[InkHighlight](flutter-docs://api/material/InkHighlight)
A visual emphasis on a part of a [Material](flutter-docs://api/material/Material) receiving user interaction.

[InkResponse](flutter-docs://api/material/InkResponse)
An area of a [Material](flutter-docs://api/material/Material) that responds to touch. Has a configurable shape and
can be configured to clip splashes that extend outside its bounds or not.

[InkRipple](flutter-docs://api/material/InkRipple)
A visual reaction on a piece of [Material](flutter-docs://api/material/Material) to user input.

[InkSparkle](flutter-docs://api/material/InkSparkle)
Begin a Material 3 ink sparkle ripple, centered at the tap or click position
relative to the [referenceBox](flutter-docs://api/material/InkFeature/referenceBox).

[InkSplash](flutter-docs://api/material/InkSplash)
A visual reaction on a piece of [Material](flutter-docs://api/material/Material) to user input.

[InkWell](flutter-docs://api/material/InkWell)
A rectangular area of a [Material](flutter-docs://api/material/Material) that responds to touch.

[InlineSpan](flutter-docs://api/painting/InlineSpan)
An immutable span of inline content which forms part of a paragraph.

[InlineSpanSemanticsInformation](flutter-docs://api/painting/InlineSpanSemanticsInformation)
The textual and semantic label information for an [InlineSpan](flutter-docs://api/painting/InlineSpan).

[InputBorder](flutter-docs://api/material/InputBorder)
Defines the appearance of an [InputDecorator](flutter-docs://api/material/InputDecorator)'s border.

[InputChip](flutter-docs://api/material/InputChip)
A Material Design input chip.

[InputDatePickerFormField](flutter-docs://api/material/InputDatePickerFormField)
A [TextFormField](flutter-docs://api/material/TextFormField) configured to accept and validate a date entered by a user.

[InputDecoration](flutter-docs://api/material/InputDecoration)
The border, labels, icons, and styles used to decorate a Material
Design text field.

[InputDecorationTheme](flutter-docs://api/material/InputDecorationTheme)
Defines the default appearance of [InputDecorator](flutter-docs://api/material/InputDecorator) s.

[InputDecorationThemeData](flutter-docs://api/material/InputDecorationThemeData)
Defines the default appearance of [InputDecorator](flutter-docs://api/material/InputDecorator) s.

[InputDecorator](flutter-docs://api/material/InputDecorator)
Defines the appearance of a Material Design text field.

[InspectorButton](flutter-docs://api/widgets/InspectorButton)
An abstract base class for creating Material or Cupertino-styled inspector
buttons.

[InspectorReferenceData](flutter-docs://api/widgets/InspectorReferenceData)
Structure to help reference count Dart objects referenced by a GUI tool
using [WidgetInspectorService](flutter-docs://api/widgets/WidgetInspectorService).

[InspectorSelection](flutter-docs://api/widgets/InspectorSelection)
Mutable selection state of the inspector.

[InspectorSerializationDelegate](flutter-docs://api/widgets/InspectorSerializationDelegate)
A delegate that configures how a hierarchy of [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode) s are
serialized by the Flutter Inspector.

[Intent](flutter-docs://api/widgets/Intent)
An abstract class representing a particular configuration of an [Action](flutter-docs://api/widgets/Action).

[InteractiveInkFeature](flutter-docs://api/material/InteractiveInkFeature)
An ink feature that displays a [color](flutter-docs://api/material/InteractiveInkFeature/color) "splash" in response to a user
gesture that can be confirmed or canceled.

[InteractiveInkFeatureFactory](flutter-docs://api/material/InteractiveInkFeatureFactory)
An encapsulation of an [InteractiveInkFeature](flutter-docs://api/material/InteractiveInkFeature) constructor used by
[InkWell](flutter-docs://api/material/InkWell), [InkResponse](flutter-docs://api/material/InkResponse), and [ThemeData](flutter-docs://api/material/ThemeData).

[InteractiveViewer](flutter-docs://api/widgets/InteractiveViewer)
A widget that enables pan and zoom interactions with its child.

[Interval](flutter-docs://api/animation/Interval)
A curve that is 0.0 until [begin](flutter-docs://api/animation/Interval/begin), then curved (according to [curve](flutter-docs://api/animation/Interval/curve)) from
0.0 at [begin](flutter-docs://api/animation/Interval/begin) to 1.0 at [end](flutter-docs://api/animation/Interval/end), then remains 1.0 past [end](flutter-docs://api/animation/Interval/end).

[IntrinsicColumnWidth](flutter-docs://api/rendering/IntrinsicColumnWidth)
Sizes the column according to the intrinsic dimensions of all the
cells in that column.

[IntrinsicHeight](flutter-docs://api/widgets/IntrinsicHeight)
A widget that sizes its child to the child's intrinsic height.

[IntrinsicWidth](flutter-docs://api/widgets/IntrinsicWidth)
A widget that sizes its child to the child's maximum intrinsic width.

[IntTween](flutter-docs://api/animation/IntTween)
An interpolation between two integers that rounds.

[IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem)
Describes a context menu button that will be rendered in the iOS system
context menu and not by Flutter itself.

[IOSSystemContextMenuItemCopy](flutter-docs://api/widgets/IOSSystemContextMenuItemCopy)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the system's built-in
copy button.

[IOSSystemContextMenuItemCustom](flutter-docs://api/widgets/IOSSystemContextMenuItemCustom)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for custom action buttons
defined by the developer.

[IOSSystemContextMenuItemCut](flutter-docs://api/widgets/IOSSystemContextMenuItemCut)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the system's built-in
cut button.

[IOSSystemContextMenuItemLiveText](flutter-docs://api/widgets/IOSSystemContextMenuItemLiveText)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the
system's built-in Live Text button.

[IOSSystemContextMenuItemLookUp](flutter-docs://api/widgets/IOSSystemContextMenuItemLookUp)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the
system's built-in look up button.

[IOSSystemContextMenuItemPaste](flutter-docs://api/widgets/IOSSystemContextMenuItemPaste)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the system's built-in
paste button.

[IOSSystemContextMenuItemSearchWeb](flutter-docs://api/widgets/IOSSystemContextMenuItemSearchWeb)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the
system's built-in search web button.

[IOSSystemContextMenuItemSelectAll](flutter-docs://api/widgets/IOSSystemContextMenuItemSelectAll)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the system's built-in
select all button.

[IOSSystemContextMenuItemShare](flutter-docs://api/widgets/IOSSystemContextMenuItemShare)
Creates an instance of [IOSSystemContextMenuItem](flutter-docs://api/widgets/IOSSystemContextMenuItem) for the
system's built-in share button.

[KeepAlive](flutter-docs://api/widgets/KeepAlive)
Mark a child as needing to stay alive even when it's in a lazy list that
would otherwise remove it.

[KeepAliveHandle](flutter-docs://api/widgets/KeepAliveHandle)
A [Listenable](flutter-docs://api/foundation/Listenable) which can be manually triggered.

[KeepAliveNotification](flutter-docs://api/widgets/KeepAliveNotification)
Indicates that the subtree through which this notification bubbles must be
kept alive even if it would normally be discarded as an optimization.

[Key](flutter-docs://api/foundation/Key)
A [Key](flutter-docs://api/foundation/Key) is an identifier for [Widget](flutter-docs://api/widgets/Widget) s, [Element](flutter-docs://api/widgets/Element) s and [SemanticsNode](flutter-docs://api/semantics/SemanticsNode) s.

[KeyboardInsertedContent](flutter-docs://api/services/KeyboardInsertedContent)
A class representing rich content (such as a PNG image) inserted via the
system input method.

[KeyboardListener](flutter-docs://api/widgets/KeyboardListener)
A widget that calls a callback whenever the user presses or releases a key
on a keyboard.

[KeyedSubtree](flutter-docs://api/widgets/KeyedSubtree)
A widget that builds its child.

[KeyEvent](flutter-docs://api/services/KeyEvent)
Defines the interface for keyboard key events.

[KeySet](flutter-docs://api/widgets/KeySet)<T extends [KeyboardKey](flutter-docs://api/services/KeyboardKey)>
A set of [KeyboardKey](flutter-docs://api/services/KeyboardKey) s that can be used as the keys in a [Map](flutter-docs://api/dart-core/Map).

[LabeledGlobalKey](flutter-docs://api/widgets/LabeledGlobalKey)<T extends [State](flutter-docs://api/widgets/State)<[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>>
A global key with a debugging label.

[LayerLink](flutter-docs://api/rendering/LayerLink)
An object that a [LeaderLayer](flutter-docs://api/rendering/LeaderLayer) can register with.

[LayoutBuilder](flutter-docs://api/widgets/LayoutBuilder)
Builds a widget tree that can depend on the parent widget's size.

[LayoutChangedNotification](flutter-docs://api/widgets/LayoutChangedNotification)
Indicates that the layout of one of the descendants of the object receiving
this notification has changed in some way, and that therefore any
assumptions about that layout are no longer valid.

[LayoutId](flutter-docs://api/widgets/LayoutId)
Metadata for identifying children in a [CustomMultiChildLayout](flutter-docs://api/widgets/CustomMultiChildLayout).

[LeafRenderObjectElement](flutter-docs://api/widgets/LeafRenderObjectElement)
An [Element](flutter-docs://api/widgets/Element) that uses a [LeafRenderObjectWidget](flutter-docs://api/widgets/LeafRenderObjectWidget) as its configuration.

[LeafRenderObjectWidget](flutter-docs://api/widgets/LeafRenderObjectWidget)
A superclass for [RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget) s that configure [RenderObject](flutter-docs://api/rendering/RenderObject) subclasses
that have no children.

[LexicalFocusOrder](flutter-docs://api/widgets/LexicalFocusOrder)
Can be given to a [FocusTraversalOrder](flutter-docs://api/widgets/FocusTraversalOrder) widget to use a String to assign a
lexical order to a widget subtree that is using a
[OrderedTraversalPolicy](flutter-docs://api/widgets/OrderedTraversalPolicy) to define the order in which widgets should be
traversed with the keyboard.

[LicensePage](flutter-docs://api/material/LicensePage)
A page that shows licenses for software used by the application.

[LimitedBox](flutter-docs://api/widgets/LimitedBox)
A box that limits its size only when it's unconstrained.

[LinearBorder](flutter-docs://api/painting/LinearBorder)
An [OutlinedBorder](flutter-docs://api/painting/OutlinedBorder) like [BoxBorder](flutter-docs://api/painting/BoxBorder) that allows one to define a rectangular (box) border
in terms of zero to four [LinearBorderEdge](flutter-docs://api/painting/LinearBorderEdge) s, each of which is rendered as a single line.

[LinearBorderEdge](flutter-docs://api/painting/LinearBorderEdge)
Defines the relative size and alignment of one [LinearBorder](flutter-docs://api/painting/LinearBorder) edge.

[LinearGradient](flutter-docs://api/painting/LinearGradient)
A 2D linear gradient.

[LinearProgressIndicator](flutter-docs://api/material/LinearProgressIndicator)
A Material Design linear progress indicator, also known as a progress bar.

[LineMetrics](flutter-docs://api/dart-ui/LineMetrics)
[LineMetrics](flutter-docs://api/dart-ui/LineMetrics) stores the measurements and statistics of a single line in the
paragraph.

[ListBody](flutter-docs://api/widgets/ListBody)
A widget that arranges its children sequentially along a given axis, forcing
them to the dimension of the parent in the other axis.

[Listenable](flutter-docs://api/foundation/Listenable)
An object that maintains a list of listeners.

[ListenableBuilder](flutter-docs://api/widgets/ListenableBuilder)
A general-purpose widget for building a widget subtree when a [Listenable](flutter-docs://api/foundation/Listenable) changes.

[Listener](flutter-docs://api/widgets/Listener)
A widget that calls callbacks in response to common pointer events.

[ListTile](flutter-docs://api/material/ListTile)
A single fixed-height row that typically contains some text as well as
a leading or trailing icon.

[ListTileTheme](flutter-docs://api/material/ListTileTheme)
An inherited widget that defines color and style parameters for [ListTile](flutter-docs://api/material/ListTile) s
in this widget's subtree.

[ListTileThemeData](flutter-docs://api/material/ListTileThemeData)
Used with [ListTileTheme](flutter-docs://api/material/ListTileTheme) to define default property values for
descendant [ListTile](flutter-docs://api/material/ListTile) widgets, as well as classes that build
[ListTile](flutter-docs://api/material/ListTile) s, like [CheckboxListTile](flutter-docs://api/material/CheckboxListTile), [RadioListTile](flutter-docs://api/material/RadioListTile), and
[SwitchListTile](flutter-docs://api/material/SwitchListTile).

[ListView](flutter-docs://api/widgets/ListView)
A scrollable list of widgets arranged linearly.

[ListWheelChildBuilderDelegate](flutter-docs://api/widgets/ListWheelChildBuilderDelegate)
A delegate that supplies children for [ListWheelScrollView](flutter-docs://api/widgets/ListWheelScrollView) using a builder
callback.

[ListWheelChildDelegate](flutter-docs://api/widgets/ListWheelChildDelegate)
A delegate that supplies children for [ListWheelScrollView](flutter-docs://api/widgets/ListWheelScrollView).

[ListWheelChildListDelegate](flutter-docs://api/widgets/ListWheelChildListDelegate)
A delegate that supplies children for [ListWheelScrollView](flutter-docs://api/widgets/ListWheelScrollView) using an
explicit list.

[ListWheelChildLoopingListDelegate](flutter-docs://api/widgets/ListWheelChildLoopingListDelegate)
A delegate that supplies infinite children for [ListWheelScrollView](flutter-docs://api/widgets/ListWheelScrollView) by
looping an explicit list.

[ListWheelElement](flutter-docs://api/widgets/ListWheelElement)
Element that supports building children lazily for [ListWheelViewport](flutter-docs://api/widgets/ListWheelViewport).

[ListWheelScrollView](flutter-docs://api/widgets/ListWheelScrollView)
A box in which children on a wheel can be scrolled.

[ListWheelViewport](flutter-docs://api/widgets/ListWheelViewport)
A viewport showing a subset of children on a wheel.

[LiveTextInputStatusNotifier](flutter-docs://api/widgets/LiveTextInputStatusNotifier)
A [ValueNotifier](flutter-docs://api/foundation/ValueNotifier) whose [value](flutter-docs://api/foundation/ValueNotifier/value) indicates whether the current device supports the Live Text
(OCR) function.

[Locale](flutter-docs://api/dart-ui/Locale)
An identifier used to select a user's language and formatting preferences.

[LocalHistoryEntry](flutter-docs://api/widgets/LocalHistoryEntry)
An entry in the history of a [LocalHistoryRoute](flutter-docs://api/widgets/LocalHistoryRoute).

[Localizations](flutter-docs://api/widgets/Localizations)
Defines the [Locale](flutter-docs://api/dart-ui/Locale) for its `child` and the localized resources that the
child depends on.

[LocalizationsDelegate](flutter-docs://api/widgets/LocalizationsDelegate)<T>
A factory for a set of localized resources of type `T`, to be loaded by a
[Localizations](flutter-docs://api/widgets/Localizations) widget.

[LocalizationsResolver](flutter-docs://api/widgets/LocalizationsResolver)
A helper class used to manage localization resolution.

[LocalKey](flutter-docs://api/foundation/LocalKey)
A key that is not a [GlobalKey](flutter-docs://api/widgets/GlobalKey).

[LogicalKeySet](flutter-docs://api/widgets/LogicalKeySet)
A set of [LogicalKeyboardKey](flutter-docs://api/services/LogicalKeyboardKey) s that can be used as the keys in a map.

[LongPressDraggable](flutter-docs://api/widgets/LongPressDraggable)<T extends [Object](flutter-docs://api/dart-core/Object)>
Makes its child draggable starting from long press.

[LongPressEndDetails](flutter-docs://api/gestures/LongPressEndDetails)
Details for callbacks that use [GestureLongPressEndCallback](flutter-docs://api/gestures/GestureLongPressEndCallback).

[LongPressMoveUpdateDetails](flutter-docs://api/gestures/LongPressMoveUpdateDetails)
Details for callbacks that use [GestureLongPressMoveUpdateCallback](flutter-docs://api/gestures/GestureLongPressMoveUpdateCallback).

[LongPressStartDetails](flutter-docs://api/gestures/LongPressStartDetails)
Details for callbacks that use [GestureLongPressStartCallback](flutter-docs://api/gestures/GestureLongPressStartCallback).

[LookupBoundary](flutter-docs://api/widgets/LookupBoundary)
A lookup boundary controls what entities are visible to descendants of the
boundary via the static lookup methods provided by the boundary.

[Magnifier](flutter-docs://api/material/Magnifier)
A Material-styled magnifying glass.

[MagnifierController](flutter-docs://api/widgets/MagnifierController)
A controller for a magnifier.

[MagnifierDecoration](flutter-docs://api/widgets/MagnifierDecoration)
The decorations to put around the loupe in a [RawMagnifier](flutter-docs://api/widgets/RawMagnifier).

[MagnifierInfo](flutter-docs://api/widgets/MagnifierInfo)
A data class that contains the geometry information of text layouts
and selection gestures, used to position magnifiers.

[MaskFilter](flutter-docs://api/dart-ui/MaskFilter)
A mask filter to apply to shapes as they are painted. A mask filter is a
function that takes a bitmap of color pixels, and returns another bitmap of
color pixels.

[Material](flutter-docs://api/material/Material)
A piece of material.

[MaterialAccentColor](flutter-docs://api/material/MaterialAccentColor)
Defines a single accent color as well a swatch of four shades of the
accent color.

[MaterialApp](flutter-docs://api/material/MaterialApp)
An application that uses Material Design.

[MaterialBanner](flutter-docs://api/material/MaterialBanner)
A Material Design banner.

[MaterialBannerTheme](flutter-docs://api/material/MaterialBannerTheme)
An inherited widget that defines the configuration for
[MaterialBanner](flutter-docs://api/material/MaterialBanner) s in this widget's subtree.

[MaterialBannerThemeData](flutter-docs://api/material/MaterialBannerThemeData)
Defines the visual properties of [MaterialBanner](flutter-docs://api/material/MaterialBanner) widgets.

[MaterialBasedCupertinoThemeData](flutter-docs://api/material/MaterialBasedCupertinoThemeData)
A [CupertinoThemeData](flutter-docs://api/cupertino/CupertinoThemeData) that defers unspecified theme attributes to an
upstream Material [ThemeData](flutter-docs://api/material/ThemeData).

[MaterialButton](flutter-docs://api/material/MaterialButton)
A utility class for building Material buttons that depend on the
ambient [ButtonTheme](flutter-docs://api/material/ButtonTheme) and [Theme](flutter-docs://api/material/Theme).

[MaterialColor](flutter-docs://api/material/MaterialColor)
Defines a single color as well a color swatch with ten shades of the color.

[MaterialGap](flutter-docs://api/material/MaterialGap)
A class that represents a gap within [MergeableMaterial](flutter-docs://api/material/MergeableMaterial).

[MaterialInkController](flutter-docs://api/material/MaterialInkController)
An interface for creating [InkSplash](flutter-docs://api/material/InkSplash) s and [InkHighlight](flutter-docs://api/material/InkHighlight) s on a [Material](flutter-docs://api/material/Material).

[MaterialLocalizations](flutter-docs://api/material/MaterialLocalizations)
Defines the localized resource values used by the Material widgets.

[MaterialPage](flutter-docs://api/material/MaterialPage)<T>
A page that creates a material style [PageRoute](flutter-docs://api/widgets/PageRoute).

[MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute)<T>
A modal route that replaces the entire screen with a platform-adaptive
transition.

[MaterialPointArcTween](flutter-docs://api/material/MaterialPointArcTween)
A [Tween](flutter-docs://api/animation/Tween) that interpolates an [Offset](flutter-docs://api/dart-ui/Offset) along a circular arc.

[MaterialRectArcTween](flutter-docs://api/material/MaterialRectArcTween)
A [Tween](flutter-docs://api/animation/Tween) that interpolates a [Rect](flutter-docs://api/dart-ui/Rect) by having its opposite corners follow
circular arcs.

[MaterialRectCenterArcTween](flutter-docs://api/material/MaterialRectCenterArcTween)
A [Tween](flutter-docs://api/animation/Tween) that interpolates a [Rect](flutter-docs://api/dart-ui/Rect) by moving it along a circular arc from
[begin](flutter-docs://api/material/MaterialRectCenterArcTween/begin)'s [Rect.center](flutter-docs://api/dart-ui/Rect/center) to [end](flutter-docs://api/material/MaterialRectCenterArcTween/end)'s [Rect.center](flutter-docs://api/dart-ui/Rect/center) while interpolating the
rectangle's width and height.

[MaterialScrollBehavior](flutter-docs://api/material/MaterialScrollBehavior)
Describes how [Scrollable](flutter-docs://api/widgets/Scrollable) widgets behave for [MaterialApp](flutter-docs://api/material/MaterialApp) s.

[MaterialSlice](flutter-docs://api/material/MaterialSlice)
A class that can be used as a child to [MergeableMaterial](flutter-docs://api/material/MergeableMaterial). It is a slice
of [Material](flutter-docs://api/material/Material) that animates merging with other slices.

[MaterialStateOutlineInputBorder](flutter-docs://api/material/MaterialStateOutlineInputBorder)
Defines a [OutlineInputBorder](flutter-docs://api/material/OutlineInputBorder) that is also a [MaterialStateProperty](flutter-docs://api/material/MaterialStateProperty).

[MaterialStateUnderlineInputBorder](flutter-docs://api/material/MaterialStateUnderlineInputBorder)
Defines a [UnderlineInputBorder](flutter-docs://api/material/UnderlineInputBorder) that is also a [MaterialStateProperty](flutter-docs://api/material/MaterialStateProperty).

[MaterialTextSelectionControls](flutter-docs://api/material/MaterialTextSelectionControls)
Android Material styled text selection controls.

[MaterialTextSelectionHandleControls](flutter-docs://api/material/MaterialTextSelectionHandleControls)
Android Material styled text selection handle controls.

[Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4)
4D Matrix.
Values are stored in column major order.

[Matrix4Tween](flutter-docs://api/widgets/Matrix4Tween)
An interpolation between two [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4) s.

[MatrixTransition](flutter-docs://api/widgets/MatrixTransition)
Animates the [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4) of a transformed widget.

[MatrixUtils](flutter-docs://api/painting/MatrixUtils)
Utility functions for working with matrices.

[MaxColumnWidth](flutter-docs://api/rendering/MaxColumnWidth)
Sizes the column such that it is the size that is the maximum of
two column width specifications.

[MediaQuery](flutter-docs://api/widgets/MediaQuery)
Establishes a subtree in which media queries resolve to the given data.

[MediaQueryData](flutter-docs://api/widgets/MediaQueryData)
Information about a piece of media (e.g., a window).

[MemoryImage](flutter-docs://api/painting/MemoryImage)
Decodes the given [Uint8List](flutter-docs://api/dart-typed_data/Uint8List) buffer as an image, associating it with the
given scale.

[MenuAcceleratorCallbackBinding](flutter-docs://api/material/MenuAcceleratorCallbackBinding)
An [InheritedWidget](flutter-docs://api/widgets/InheritedWidget) that provides a descendant [MenuAcceleratorLabel](flutter-docs://api/material/MenuAcceleratorLabel) with
the function to invoke when the accelerator is pressed.

[MenuAcceleratorLabel](flutter-docs://api/material/MenuAcceleratorLabel)
A widget that draws the label text for a menu item (typically a
[MenuItemButton](flutter-docs://api/material/MenuItemButton) or [SubmenuButton](flutter-docs://api/material/SubmenuButton)) and renders its child with information
about the currently active keyboard accelerator.

[MenuAnchor](flutter-docs://api/material/MenuAnchor)
A widget used to mark the "anchor" for a set of submenus, defining the
rectangle used to position the menu, which can be done either with an
explicit location, or with an alignment.

[MenuBar](flutter-docs://api/material/MenuBar)
A menu bar that manages cascading child menus.

[MenuBarTheme](flutter-docs://api/material/MenuBarTheme)
An inherited widget that defines the configuration for the [MenuBar](flutter-docs://api/material/MenuBar) widgets
in this widget's descendants.

[MenuBarThemeData](flutter-docs://api/material/MenuBarThemeData)
A data class that [MenuBarTheme](flutter-docs://api/material/MenuBarTheme) uses to define the visual properties of
[MenuBar](flutter-docs://api/material/MenuBar) widgets.

[MenuButtonTheme](flutter-docs://api/material/MenuButtonTheme)
Overrides the default [ButtonStyle](flutter-docs://api/material/ButtonStyle) of its [MenuItemButton](flutter-docs://api/material/MenuItemButton) and
[SubmenuButton](flutter-docs://api/material/SubmenuButton) descendants.

[MenuButtonThemeData](flutter-docs://api/material/MenuButtonThemeData)
A [ButtonStyle](flutter-docs://api/material/ButtonStyle) theme that overrides the default appearance of
[SubmenuButton](flutter-docs://api/material/SubmenuButton) s and [MenuItemButton](flutter-docs://api/material/MenuItemButton) s when it's used with a
[MenuButtonTheme](flutter-docs://api/material/MenuButtonTheme) or with the overall [Theme](flutter-docs://api/material/Theme)'s [ThemeData.menuTheme](flutter-docs://api/material/ThemeData/menuTheme).

[MenuController](flutter-docs://api/widgets/MenuController)
A controller used to manage a menu created by a subclass of [RawMenuAnchor](flutter-docs://api/widgets/RawMenuAnchor),
such as [MenuAnchor](flutter-docs://api/material/MenuAnchor), [MenuBar](flutter-docs://api/material/MenuBar), [SubmenuButton](flutter-docs://api/material/SubmenuButton).

[MenuItemButton](flutter-docs://api/material/MenuItemButton)
A button for use in a [MenuBar](flutter-docs://api/material/MenuBar), in a menu created with [MenuAnchor](flutter-docs://api/material/MenuAnchor), or on
its own, that can be activated by click or keyboard navigation.

[MenuStyle](flutter-docs://api/material/MenuStyle)
The visual properties that menus have in common.

[MenuTheme](flutter-docs://api/material/MenuTheme)
An inherited widget that defines the configuration in this widget's
descendants for menus created by the [SubmenuButton](flutter-docs://api/material/SubmenuButton), [MenuBar](flutter-docs://api/material/MenuBar), or
[MenuAnchor](flutter-docs://api/material/MenuAnchor) widgets.

[MenuThemeData](flutter-docs://api/material/MenuThemeData)
Defines the configuration of the submenus created by the [SubmenuButton](flutter-docs://api/material/SubmenuButton),
[MenuBar](flutter-docs://api/material/MenuBar), or [MenuAnchor](flutter-docs://api/material/MenuAnchor) widgets.

[MergeableMaterial](flutter-docs://api/material/MergeableMaterial)
Displays a list of [MergeableMaterialItem](flutter-docs://api/material/MergeableMaterialItem) children. The list contains
[MaterialSlice](flutter-docs://api/material/MaterialSlice) items whose boundaries are either "merged" with adjacent
items or separated by a [MaterialGap](flutter-docs://api/material/MaterialGap). The [children](flutter-docs://api/material/MergeableMaterial/children) are distributed along
the given [mainAxis](flutter-docs://api/material/MergeableMaterial/mainAxis) in the same way as the children of a [ListBody](flutter-docs://api/widgets/ListBody). When
the list of children changes, gaps are automatically animated open or closed
as needed.

[MergeableMaterialItem](flutter-docs://api/material/MergeableMaterialItem)
The base type for [MaterialSlice](flutter-docs://api/material/MaterialSlice) and [MaterialGap](flutter-docs://api/material/MaterialGap).

[MergeSemantics](flutter-docs://api/widgets/MergeSemantics)
A widget that merges the semantics of its descendants.

[MetaData](flutter-docs://api/widgets/MetaData)
Holds opaque meta data in the render tree.

[MinColumnWidth](flutter-docs://api/rendering/MinColumnWidth)
Sizes the column such that it is the size that is the minimum of
two column width specifications.

[ModalBarrier](flutter-docs://api/widgets/ModalBarrier)
A widget that prevents the user from interacting with widgets behind itself.

[ModalBottomSheetRoute](flutter-docs://api/material/ModalBottomSheetRoute)<T>
A route that represents a Material Design modal bottom sheet.

[ModalRoute](flutter-docs://api/widgets/ModalRoute)<T>
A route that blocks interaction with previous routes.

[MouseCursor](flutter-docs://api/services/MouseCursor)
An interface for mouse cursor definitions.

[MouseRegion](flutter-docs://api/widgets/MouseRegion)
A widget that tracks the movement of mice.

[MultiChildLayoutDelegate](flutter-docs://api/rendering/MultiChildLayoutDelegate)
A delegate that controls the layout of multiple children.

[MultiChildRenderObjectElement](flutter-docs://api/widgets/MultiChildRenderObjectElement)
An [Element](flutter-docs://api/widgets/Element) that uses a [MultiChildRenderObjectWidget](flutter-docs://api/widgets/MultiChildRenderObjectWidget) as its configuration.

[MultiChildRenderObjectWidget](flutter-docs://api/widgets/MultiChildRenderObjectWidget)
A superclass for [RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget) s that configure [RenderObject](flutter-docs://api/rendering/RenderObject) subclasses
that have a single list of children. (This superclass only provides the
storage for that child list, it doesn't actually provide the updating
logic.)

[MultiFrameImageStreamCompleter](flutter-docs://api/painting/MultiFrameImageStreamCompleter)
Manages the decoding and scheduling of image frames.

[MultiSelectableSelectionContainerDelegate](flutter-docs://api/widgets/MultiSelectableSelectionContainerDelegate)
A delegate that handles events and updates for multiple [Selectable](flutter-docs://api/rendering/Selectable) children.

[NavigationBar](flutter-docs://api/material/NavigationBar)
Material 3 Navigation Bar component.

[NavigationBarTheme](flutter-docs://api/material/NavigationBarTheme)
An inherited widget that defines visual properties for [NavigationBar](flutter-docs://api/material/NavigationBar) s and
[NavigationDestination](flutter-docs://api/material/NavigationDestination) s in this widget's subtree.

[NavigationBarThemeData](flutter-docs://api/material/NavigationBarThemeData)
Defines default property values for descendant [NavigationBar](flutter-docs://api/material/NavigationBar) widgets.

[NavigationDestination](flutter-docs://api/material/NavigationDestination)
A Material 3 [NavigationBar](flutter-docs://api/material/NavigationBar) destination.

[NavigationDrawer](flutter-docs://api/material/NavigationDrawer)
Material Design Navigation Drawer component.

[NavigationDrawerDestination](flutter-docs://api/material/NavigationDrawerDestination)
A Material Design [NavigationDrawer](flutter-docs://api/material/NavigationDrawer) destination.

[NavigationDrawerTheme](flutter-docs://api/material/NavigationDrawerTheme)
An inherited widget that defines visual properties for [NavigationDrawer](flutter-docs://api/material/NavigationDrawer) s and
[NavigationDestination](flutter-docs://api/material/NavigationDestination) s in this widget's subtree.

[NavigationDrawerThemeData](flutter-docs://api/material/NavigationDrawerThemeData)
Defines default property values for descendant [NavigationDrawer](flutter-docs://api/material/NavigationDrawer) widgets.

[NavigationIndicator](flutter-docs://api/material/NavigationIndicator)
Selection Indicator for the Material 3 [NavigationBar](flutter-docs://api/material/NavigationBar) and [NavigationRail](flutter-docs://api/material/NavigationRail) components.

[NavigationNotification](flutter-docs://api/widgets/NavigationNotification)
A notification that a change in navigation has taken place.

[NavigationRail](flutter-docs://api/material/NavigationRail)
A Material Design widget that is meant to be displayed at the left or right of an
app to navigate between a small number of views, typically between three and
five.

[NavigationRailDestination](flutter-docs://api/material/NavigationRailDestination)
Defines a [NavigationRail](flutter-docs://api/material/NavigationRail) button that represents one "destination" view.

[NavigationRailTheme](flutter-docs://api/material/NavigationRailTheme)
An inherited widget that defines visual properties for [NavigationRail](flutter-docs://api/material/NavigationRail) s and
[NavigationRailDestination](flutter-docs://api/material/NavigationRailDestination) s in this widget's subtree.

[NavigationRailThemeData](flutter-docs://api/material/NavigationRailThemeData)
Defines default property values for descendant [NavigationRail](flutter-docs://api/material/NavigationRail) widgets.

[NavigationToolbar](flutter-docs://api/widgets/NavigationToolbar)
[NavigationToolbar](flutter-docs://api/widgets/NavigationToolbar) is a layout helper to position 3 widgets or groups of
widgets along a horizontal axis that's sensible for an application's
navigation bar such as in Material Design and in iOS.

[Navigator](flutter-docs://api/widgets/Navigator)
A widget that manages a set of child widgets with a stack discipline.

[NavigatorObserver](flutter-docs://api/widgets/NavigatorObserver)
An interface for observing the behavior of a [Navigator](flutter-docs://api/widgets/Navigator).

[NavigatorPopHandler](flutter-docs://api/widgets/NavigatorPopHandler)<T>
Enables the handling of system back gestures.

[NavigatorState](flutter-docs://api/widgets/NavigatorState)
The state for a [Navigator](flutter-docs://api/widgets/Navigator) widget.

[NestedScrollView](flutter-docs://api/widgets/NestedScrollView)
A scrolling view inside of which can be nested other scrolling views, with
their scroll positions being intrinsically linked.

[NestedScrollViewState](flutter-docs://api/widgets/NestedScrollViewState)
The [State](flutter-docs://api/widgets/State) for a [NestedScrollView](flutter-docs://api/widgets/NestedScrollView).

[NestedScrollViewViewport](flutter-docs://api/widgets/NestedScrollViewViewport)
The [Viewport](flutter-docs://api/widgets/Viewport) variant used by [NestedScrollView](flutter-docs://api/widgets/NestedScrollView).

[NetworkImage](flutter-docs://api/painting/NetworkImage)
Fetches the given URL from the network, associating it with the given scale.

[NeverScrollableScrollPhysics](flutter-docs://api/widgets/NeverScrollableScrollPhysics)
Scroll physics that does not allow the user to scroll.

[NextFocusAction](flutter-docs://api/widgets/NextFocusAction)
An [Action](flutter-docs://api/widgets/Action) that moves the focus to the next focusable node in the focus
order.

[NextFocusIntent](flutter-docs://api/widgets/NextFocusIntent)
An [Intent](flutter-docs://api/widgets/Intent) bound to [NextFocusAction](flutter-docs://api/widgets/NextFocusAction), which moves the focus to the next
focusable node in the focus traversal order.

[NoSplash](flutter-docs://api/material/NoSplash)
An [InteractiveInkFeature](flutter-docs://api/material/InteractiveInkFeature) that doesn't paint a splash.

[NotchedShape](flutter-docs://api/painting/NotchedShape)
A shape with a notch in its outline.

[Notification](flutter-docs://api/widgets/Notification)
A notification that can bubble up the widget tree.

[NotificationListener](flutter-docs://api/widgets/NotificationListener)<T extends [Notification](flutter-docs://api/widgets/Notification)>
A widget that listens for [Notification](flutter-docs://api/widgets/Notification) s bubbling up the tree.

[NumericFocusOrder](flutter-docs://api/widgets/NumericFocusOrder)
Can be given to a [FocusTraversalOrder](flutter-docs://api/widgets/FocusTraversalOrder) widget to assign a numerical order
to a widget subtree that is using a [OrderedTraversalPolicy](flutter-docs://api/widgets/OrderedTraversalPolicy) to define the
order in which widgets should be traversed with the keyboard.

[ObjectKey](flutter-docs://api/widgets/ObjectKey)
A key that takes its identity from the object used as its value.

[Offset](flutter-docs://api/dart-ui/Offset)
An immutable 2D floating-point offset.

[Offstage](flutter-docs://api/widgets/Offstage)
A widget that lays the child out as if it was in the tree, but without
painting anything, without making the child available for hit testing, and
without taking any room in the parent.

[OneFrameImageStreamCompleter](flutter-docs://api/painting/OneFrameImageStreamCompleter)
Manages the loading of [dart:ui.Image](flutter-docs://api/dart-ui/Image) objects for static [ImageStream](flutter-docs://api/painting/ImageStream) s (those
with only one frame).

[Opacity](flutter-docs://api/widgets/Opacity)
A widget that makes its child partially transparent.

[OpenUpwardsPageTransitionsBuilder](flutter-docs://api/material/OpenUpwardsPageTransitionsBuilder)
Used by [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) to define a vertical [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) page
transition animation that looks like the default page transition
used on Android P.

[OrderedTraversalPolicy](flutter-docs://api/widgets/OrderedTraversalPolicy)
A [FocusTraversalPolicy](flutter-docs://api/widgets/FocusTraversalPolicy) that orders nodes by an explicit order that resides
in the nearest [FocusTraversalOrder](flutter-docs://api/widgets/FocusTraversalOrder) widget ancestor.

[OrientationBuilder](flutter-docs://api/widgets/OrientationBuilder)
Builds a widget tree that can depend on the parent widget's orientation
(distinct from the device orientation).

[OutlinedBorder](flutter-docs://api/painting/OutlinedBorder)
A ShapeBorder that draws an outline with the width and color specified
by [side](flutter-docs://api/painting/OutlinedBorder/side).

[OutlinedButton](flutter-docs://api/material/OutlinedButton)
A Material Design "Outlined Button"; essentially a [TextButton](flutter-docs://api/material/TextButton) with an outlined border.

[OutlinedButtonTheme](flutter-docs://api/material/OutlinedButtonTheme)
Overrides the default [ButtonStyle](flutter-docs://api/material/ButtonStyle) of its [OutlinedButton](flutter-docs://api/material/OutlinedButton) descendants.

[OutlinedButtonThemeData](flutter-docs://api/material/OutlinedButtonThemeData)
A [ButtonStyle](flutter-docs://api/material/ButtonStyle) that overrides the default appearance of
[OutlinedButton](flutter-docs://api/material/OutlinedButton) s when it's used with [OutlinedButtonTheme](flutter-docs://api/material/OutlinedButtonTheme) or with the
overall [Theme](flutter-docs://api/material/Theme)'s [ThemeData.outlinedButtonTheme](flutter-docs://api/material/ThemeData/outlinedButtonTheme).

[OutlineInputBorder](flutter-docs://api/material/OutlineInputBorder)
Draws a rounded rectangle around an [InputDecorator](flutter-docs://api/material/InputDecorator)'s container.

[OvalBorder](flutter-docs://api/painting/OvalBorder)
A border that fits an elliptical shape.

[OverflowBar](flutter-docs://api/widgets/OverflowBar)
A widget that lays out its [children](flutter-docs://api/widgets/MultiChildRenderObjectWidget/children) in a row unless they
"overflow" the available horizontal space, in which case it lays
them out in a column instead.

[OverflowBox](flutter-docs://api/widgets/OverflowBox)
A widget that imposes different constraints on its child than it gets
from its parent, possibly allowing the child to overflow the parent.

[Overlay](flutter-docs://api/widgets/Overlay)
A stack of entries that can be managed independently.

[OverlayEntry](flutter-docs://api/widgets/OverlayEntry)
A place in an [Overlay](flutter-docs://api/widgets/Overlay) that can contain a widget.

[OverlayPortal](flutter-docs://api/widgets/OverlayPortal)
A widget that renders its overlay child on an [Overlay](flutter-docs://api/widgets/Overlay).

[OverlayPortalController](flutter-docs://api/widgets/OverlayPortalController)
A class to show, hide and bring to top an [OverlayPortal](flutter-docs://api/widgets/OverlayPortal)'s overlay child
in the target [Overlay](flutter-docs://api/widgets/Overlay).

[OverlayRoute](flutter-docs://api/widgets/OverlayRoute)<T>
A route that displays widgets in the [Navigator](flutter-docs://api/widgets/Navigator)'s [Overlay](flutter-docs://api/widgets/Overlay).

[OverlayState](flutter-docs://api/widgets/OverlayState)
The current state of an [Overlay](flutter-docs://api/widgets/Overlay).

[OverscrollIndicatorNotification](flutter-docs://api/widgets/OverscrollIndicatorNotification)
A notification that either a [GlowingOverscrollIndicator](flutter-docs://api/widgets/GlowingOverscrollIndicator) or a
[StretchingOverscrollIndicator](flutter-docs://api/widgets/StretchingOverscrollIndicator) will start showing an overscroll indication.

[OverscrollNotification](flutter-docs://api/widgets/OverscrollNotification)
A notification that a [Scrollable](flutter-docs://api/widgets/Scrollable) widget has not changed its scroll position
because the change would have caused its scroll position to go outside of
its scroll bounds.

[Padding](flutter-docs://api/widgets/Padding)
A widget that insets its child by the given padding.

[PaddleRangeSliderValueIndicatorShape](flutter-docs://api/material/PaddleRangeSliderValueIndicatorShape)
A variant shape of a [RangeSlider](flutter-docs://api/material/RangeSlider)'s value indicators. The value indicator
is in the shape of an upside-down pear.

[PaddleSliderValueIndicatorShape](flutter-docs://api/material/PaddleSliderValueIndicatorShape)
A variant shape of a [Slider](flutter-docs://api/material/Slider)'s value indicator . The value indicator is in
the shape of an upside-down pear.

[Page](flutter-docs://api/widgets/Page)<T>
Describes the configuration of a [Route](flutter-docs://api/widgets/Route).

[PageController](flutter-docs://api/widgets/PageController)
A controller for [PageView](flutter-docs://api/widgets/PageView).

[PageMetrics](flutter-docs://api/widgets/PageMetrics)
Metrics for a [PageView](flutter-docs://api/widgets/PageView).

[PageRoute](flutter-docs://api/widgets/PageRoute)<T>
A modal route that replaces the entire screen.

[PageRouteBuilder](flutter-docs://api/widgets/PageRouteBuilder)<T>
A utility class for defining one-off page routes in terms of callbacks.

[PageScrollPhysics](flutter-docs://api/widgets/PageScrollPhysics)
Scroll physics used by a [PageView](flutter-docs://api/widgets/PageView).

[PageStorage](flutter-docs://api/widgets/PageStorage)
Establish a subtree in which widgets can opt into persisting states after
being destroyed.

[PageStorageBucket](flutter-docs://api/widgets/PageStorageBucket)
A storage bucket associated with a page in an app.

[PageStorageKey](flutter-docs://api/widgets/PageStorageKey)<T>
A [Key](flutter-docs://api/foundation/Key) that can be used to persist the widget state in storage after the
destruction and will be restored when recreated.

[PageTransitionsBuilder](flutter-docs://api/widgets/PageTransitionsBuilder)
Defines a page transition animation for a [PageRoute](flutter-docs://api/widgets/PageRoute).

[PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme)
Defines the page transition animations used by [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) for different [TargetPlatform](flutter-docs://api/foundation/TargetPlatform) s.

[PageView](flutter-docs://api/widgets/PageView)
A scrollable list that works page by page.

[PaginatedDataTable](flutter-docs://api/material/PaginatedDataTable)
A table that follows the
[Material 2](https://material.io/go/design-data-tables) design specification, using multiple pages to display data.

[PaginatedDataTableState](flutter-docs://api/material/PaginatedDataTableState)
Holds the state of a [PaginatedDataTable](flutter-docs://api/material/PaginatedDataTable).

[Paint](flutter-docs://api/dart-ui/Paint)
A description of the style to use when drawing on a [Canvas](flutter-docs://api/dart-ui/Canvas).

[PaintingContext](flutter-docs://api/rendering/PaintingContext)
A place to paint.

[ParametricCurve](flutter-docs://api/animation/ParametricCurve)<T>
An abstract class providing an interface for evaluating a parametric curve.

[ParentDataElement](flutter-docs://api/widgets/ParentDataElement)<T extends [ParentData](flutter-docs://api/rendering/ParentData)>
An [Element](flutter-docs://api/widgets/Element) that uses a [ParentDataWidget](flutter-docs://api/widgets/ParentDataWidget) as its configuration.

[ParentDataWidget](flutter-docs://api/widgets/ParentDataWidget)<T extends [ParentData](flutter-docs://api/rendering/ParentData)>
Base class for widgets that hook [ParentData](flutter-docs://api/rendering/ParentData) information to children of
[RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget) s.

[PasteTextIntent](flutter-docs://api/widgets/PasteTextIntent)
An [Intent](flutter-docs://api/widgets/Intent) to paste text from [Clipboard](flutter-docs://api/services/Clipboard) to the field.

[Path](flutter-docs://api/dart-ui/Path)
A complex, one-dimensional subset of a plane.

[PerformanceOverlay](flutter-docs://api/widgets/PerformanceOverlay)
Displays performance statistics.

[PersistentBottomSheetController](flutter-docs://api/material/PersistentBottomSheetController)
A [ScaffoldFeatureController](flutter-docs://api/material/ScaffoldFeatureController) for standard bottom sheets.

[PhysicalModel](flutter-docs://api/widgets/PhysicalModel)
A widget representing a physical layer that clips its children to a shape.

[PhysicalShape](flutter-docs://api/widgets/PhysicalShape)
A widget representing a physical layer that clips its children to a path.

[PinnedHeaderSliver](flutter-docs://api/widgets/PinnedHeaderSliver)
A sliver that keeps its Widget child at the top of the a [CustomScrollView](flutter-docs://api/widgets/CustomScrollView).

[Placeholder](flutter-docs://api/widgets/Placeholder)
A widget that draws a box that represents where other widgets will one day
be added.

[PlaceholderDimensions](flutter-docs://api/painting/PlaceholderDimensions)
Holds the [Size](flutter-docs://api/dart-ui/Size) and baseline required to represent the dimensions of
a placeholder in text.

[PlaceholderSpan](flutter-docs://api/painting/PlaceholderSpan)
An immutable placeholder that is embedded inline within text.

[PlatformAdaptiveIcons](flutter-docs://api/material/PlatformAdaptiveIcons)
A set of platform-adaptive Material Design icons.

[PlatformMenu](flutter-docs://api/widgets/PlatformMenu)
A class for representing menu items that have child submenus.

[PlatformMenuBar](flutter-docs://api/widgets/PlatformMenuBar)
A menu bar that uses the platform's native APIs to construct and render a
menu described by a [PlatformMenu](flutter-docs://api/widgets/PlatformMenu)/[PlatformMenuItem](flutter-docs://api/widgets/PlatformMenuItem) hierarchy.

[PlatformMenuDelegate](flutter-docs://api/widgets/PlatformMenuDelegate)
An abstract delegate class that can be used to set
[WidgetsBinding.platformMenuDelegate](flutter-docs://api/widgets/WidgetsBinding/platformMenuDelegate) to provide for managing platform
menus.

[PlatformMenuItem](flutter-docs://api/widgets/PlatformMenuItem)
A class for [PlatformMenuItem](flutter-docs://api/widgets/PlatformMenuItem) s that do not have submenus (as a [PlatformMenu](flutter-docs://api/widgets/PlatformMenu) would), but can be selected.

[PlatformMenuItemGroup](flutter-docs://api/widgets/PlatformMenuItemGroup)
A class that groups other menu items into sections delineated by dividers.

[PlatformProvidedMenuItem](flutter-docs://api/widgets/PlatformProvidedMenuItem)
A class that represents a menu item that is provided by the platform.

[PlatformRouteInformationProvider](flutter-docs://api/widgets/PlatformRouteInformationProvider)
The route information provider that propagates the platform route information changes.

[PlatformSelectableRegionContextMenu](flutter-docs://api/widgets/PlatformSelectableRegionContextMenu)
A widget that provides native selection context menu for its child subtree.

[PlatformViewCreationParams](flutter-docs://api/widgets/PlatformViewCreationParams)
The parameters used to create a [PlatformViewController](flutter-docs://api/services/PlatformViewController).

[PlatformViewLink](flutter-docs://api/widgets/PlatformViewLink)
Links a platform view with the Flutter framework.

[PlatformViewSurface](flutter-docs://api/widgets/PlatformViewSurface)
Integrates a platform view with Flutter's compositor, touch, and semantics subsystems.

[PointerCancelEvent](flutter-docs://api/gestures/PointerCancelEvent)
The input from the pointer is no longer directed towards this receiver.

[PointerDownEvent](flutter-docs://api/gestures/PointerDownEvent)
The pointer has made contact with the device.

[PointerEvent](flutter-docs://api/gestures/PointerEvent)
Base class for touch, stylus, or mouse events.

[PointerMoveEvent](flutter-docs://api/gestures/PointerMoveEvent)
The pointer has moved with respect to the device while the pointer is in
contact with the device.

[PointerUpEvent](flutter-docs://api/gestures/PointerUpEvent)
The pointer has stopped making contact with the device.

[PopEntry](flutter-docs://api/widgets/PopEntry)<T>
Allows listening to and preventing pops.

[PopScope](flutter-docs://api/widgets/PopScope)<T>
Manages back navigation gestures.

[PopupMenuButton](flutter-docs://api/material/PopupMenuButton)<T>
Displays a menu when pressed and calls [onSelected](flutter-docs://api/material/PopupMenuButton/onSelected) when the menu is dismissed
because an item was selected. The value passed to [onSelected](flutter-docs://api/material/PopupMenuButton/onSelected) is the value of
the selected menu item.

[PopupMenuButtonState](flutter-docs://api/material/PopupMenuButtonState)<T>
The [State](flutter-docs://api/widgets/State) for a [PopupMenuButton](flutter-docs://api/material/PopupMenuButton).

[PopupMenuDivider](flutter-docs://api/material/PopupMenuDivider)
A horizontal divider in a Material Design popup menu.

[PopupMenuEntry](flutter-docs://api/material/PopupMenuEntry)<T>
A base class for entries in a Material Design popup menu.

[PopupMenuItem](flutter-docs://api/material/PopupMenuItem)<T>
An item in a Material Design popup menu.

[PopupMenuItemState](flutter-docs://api/material/PopupMenuItemState)<T, W extends [PopupMenuItem](flutter-docs://api/material/PopupMenuItem)<T>>
The [State](flutter-docs://api/widgets/State) for [PopupMenuItem](flutter-docs://api/material/PopupMenuItem) subclasses.

[PopupMenuTheme](flutter-docs://api/material/PopupMenuTheme)
An inherited widget that defines the configuration for
popup menus in this widget's subtree.

[PopupMenuThemeData](flutter-docs://api/material/PopupMenuThemeData)
Defines the visual properties of the routes used to display popup menus
as well as [PopupMenuItem](flutter-docs://api/material/PopupMenuItem) and [PopupMenuDivider](flutter-docs://api/material/PopupMenuDivider) widgets.

[PopupRoute](flutter-docs://api/widgets/PopupRoute)<T>
A modal route that overlays a widget over the current route.

[Positioned](flutter-docs://api/widgets/Positioned)
A widget that controls where a child of a [Stack](flutter-docs://api/widgets/Stack) is positioned.

[PositionedDirectional](flutter-docs://api/widgets/PositionedDirectional)
A widget that controls where a child of a [Stack](flutter-docs://api/widgets/Stack) is positioned without
committing to a specific [TextDirection](flutter-docs://api/dart-ui/TextDirection).

[PositionedTransition](flutter-docs://api/widgets/PositionedTransition)
Animated version of [Positioned](flutter-docs://api/widgets/Positioned) which takes a specific
[Animation<RelativeRect>](flutter-docs://api/animation/Animation) to transition the child's position from a start
position to an end position over the lifetime of the animation.

[PredictiveBackFullscreenPageTransitionsBuilder](flutter-docs://api/material/PredictiveBackFullscreenPageTransitionsBuilder)
Used by [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) to define a [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) page
transition animation that looks like Android's Full Screen page transition.

[PredictiveBackPageTransitionsBuilder](flutter-docs://api/material/PredictiveBackPageTransitionsBuilder)
Used by [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) to define a [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) page
transition animation that looks like the default page transition used on
Android U and above when using predictive back.

[PredictiveBackRoute](flutter-docs://api/widgets/PredictiveBackRoute)
An interface for a route that supports predictive back gestures.

[PreferredSize](flutter-docs://api/widgets/PreferredSize)
A widget with a preferred size.

[PreferredSizeWidget](flutter-docs://api/widgets/PreferredSizeWidget)
An interface for widgets that can return the size this widget would prefer
if it were otherwise unconstrained.

[PreviousFocusAction](flutter-docs://api/widgets/PreviousFocusAction)
An [Action](flutter-docs://api/widgets/Action) that moves the focus to the previous focusable node in the focus
order.

[PreviousFocusIntent](flutter-docs://api/widgets/PreviousFocusIntent)
An [Intent](flutter-docs://api/widgets/Intent) bound to [PreviousFocusAction](flutter-docs://api/widgets/PreviousFocusAction), which moves the focus to the
previous focusable node in the focus traversal order.

[PrimaryScrollController](flutter-docs://api/widgets/PrimaryScrollController)
Associates a [ScrollController](flutter-docs://api/widgets/ScrollController) with a subtree.

[PrioritizedAction](flutter-docs://api/widgets/PrioritizedAction)
An [Action](flutter-docs://api/widgets/Action) that iterates through a list of [Intent](flutter-docs://api/widgets/Intent) s, invoking the first
that is enabled.

[PrioritizedIntents](flutter-docs://api/widgets/PrioritizedIntents)
An [Intent](flutter-docs://api/widgets/Intent) that evaluates a series of specified [orderedIntents](flutter-docs://api/widgets/PrioritizedIntents/orderedIntents) for
execution.

[ProgressIndicator](flutter-docs://api/material/ProgressIndicator)
A base class for Material Design progress indicators.

[ProgressIndicatorTheme](flutter-docs://api/material/ProgressIndicatorTheme)
An inherited widget that defines the configuration for
[ProgressIndicator](flutter-docs://api/material/ProgressIndicator) s in this widget's subtree.

[ProgressIndicatorThemeData](flutter-docs://api/material/ProgressIndicatorThemeData)
Defines the visual properties of [ProgressIndicator](flutter-docs://api/material/ProgressIndicator) widgets.

[ProxyAnimation](flutter-docs://api/animation/ProxyAnimation)
An animation that is a proxy for another animation.

[ProxyElement](flutter-docs://api/widgets/ProxyElement)
An [Element](flutter-docs://api/widgets/Element) that uses a [ProxyWidget](flutter-docs://api/widgets/ProxyWidget) as its configuration.

[ProxyWidget](flutter-docs://api/widgets/ProxyWidget)
A widget that has a child widget provided to it, instead of building a new
widget.

[RadialGradient](flutter-docs://api/painting/RadialGradient)
A 2D radial gradient.

[Radio](flutter-docs://api/material/Radio)<T>
A Material Design radio button.

[RadioGroup](flutter-docs://api/widgets/RadioGroup)<T>
A group for radios.

[RadioGroupRegistry](flutter-docs://api/widgets/RadioGroupRegistry)<T>
An abstract interface for registering a group of radios.

[RadioListTile](flutter-docs://api/material/RadioListTile)<T>
A [ListTile](flutter-docs://api/material/ListTile) with a [Radio](flutter-docs://api/material/Radio). In other words, a radio button with a label.

[RadioMenuButton](flutter-docs://api/material/RadioMenuButton)<T>
A menu item that combines a [Radio](flutter-docs://api/material/Radio) widget with a [MenuItemButton](flutter-docs://api/material/MenuItemButton).

[RadioTheme](flutter-docs://api/material/RadioTheme)
Applies a radio theme to descendant [Radio](flutter-docs://api/material/Radio) widgets.

[RadioThemeData](flutter-docs://api/material/RadioThemeData)
Defines default property values for descendant [Radio](flutter-docs://api/material/Radio) widgets.

[Radius](flutter-docs://api/dart-ui/Radius)
A radius for either circular or elliptical shapes.

[RangeLabels](flutter-docs://api/material/RangeLabels)
Object for setting range slider label values that appear in the value
indicator for each thumb.

[RangeMaintainingScrollPhysics](flutter-docs://api/widgets/RangeMaintainingScrollPhysics)
Scroll physics that attempt to keep the scroll position in range when the
contents change dimensions suddenly.

[RangeSlider](flutter-docs://api/material/RangeSlider)
A Material Design range slider.

[RangeSliderThumbShape](flutter-docs://api/material/RangeSliderThumbShape)
Base class for [RangeSlider](flutter-docs://api/material/RangeSlider) thumb shapes.

[RangeSliderTickMarkShape](flutter-docs://api/material/RangeSliderTickMarkShape)
Base class for [RangeSlider](flutter-docs://api/material/RangeSlider) tick mark shapes.

[RangeSliderTrackShape](flutter-docs://api/material/RangeSliderTrackShape)
Base class for [RangeSlider](flutter-docs://api/material/RangeSlider) track shapes.

[RangeSliderValueIndicatorShape](flutter-docs://api/material/RangeSliderValueIndicatorShape)
Base class for [RangeSlider](flutter-docs://api/material/RangeSlider) value indicator shapes.

[RangeValues](flutter-docs://api/material/RangeValues)
Object for representing range slider thumb values.

[RawAutocomplete](flutter-docs://api/widgets/RawAutocomplete)<T extends [Object](flutter-docs://api/dart-core/Object)>
A widget for helping the user make a selection by entering some text and
choosing from among a list of options.

[RawChip](flutter-docs://api/material/RawChip)
A raw Material Design chip.

[RawDialogRoute](flutter-docs://api/widgets/RawDialogRoute)<T>
A general dialog route which allows for customization of the dialog popup.

[RawGestureDetector](flutter-docs://api/widgets/RawGestureDetector)
A widget that detects gestures described by the given gesture
factories.

[RawGestureDetectorState](flutter-docs://api/widgets/RawGestureDetectorState)
State for a [RawGestureDetector](flutter-docs://api/widgets/RawGestureDetector).

[RawImage](flutter-docs://api/widgets/RawImage)
A widget that displays a [dart:ui.Image](flutter-docs://api/dart-ui/Image) directly.

[RawKeyboardListener](flutter-docs://api/widgets/RawKeyboardListener)
A widget that calls a callback whenever the user presses or releases a key
on a keyboard.

[RawKeyEvent](flutter-docs://api/services/RawKeyEvent)
Defines the interface for raw key events.

[RawMagnifier](flutter-docs://api/widgets/RawMagnifier)
A common base class for magnifiers.

[RawMaterialButton](flutter-docs://api/material/RawMaterialButton)
Creates a button based on [Semantics](flutter-docs://api/widgets/Semantics), [Material](flutter-docs://api/material/Material), and [InkWell](flutter-docs://api/material/InkWell) widgets.

[RawMenuAnchor](flutter-docs://api/widgets/RawMenuAnchor)
A widget that wraps a child and anchors a floating menu.

[RawMenuAnchorGroup](flutter-docs://api/widgets/RawMenuAnchorGroup)
Creates a menu anchor that is always visible and is not displayed in an
[OverlayPortal](flutter-docs://api/widgets/OverlayPortal).

[RawMenuOverlayInfo](flutter-docs://api/widgets/RawMenuOverlayInfo)
Anchor and menu information passed to [RawMenuAnchor](flutter-docs://api/widgets/RawMenuAnchor).

[RawRadio](flutter-docs://api/widgets/RawRadio)<T>
A Radio button that provides basic radio functionalities.

[RawScrollbar](flutter-docs://api/widgets/RawScrollbar)
An extendable base class for building scrollbars that fade in and out.

[RawScrollbarState](flutter-docs://api/widgets/RawScrollbarState)<T extends [RawScrollbar](flutter-docs://api/widgets/RawScrollbar)>
The state for a [RawScrollbar](flutter-docs://api/widgets/RawScrollbar) widget, also shared by the [Scrollbar](flutter-docs://api/material/Scrollbar) and
[CupertinoScrollbar](flutter-docs://api/cupertino/CupertinoScrollbar) widgets.

[RawView](flutter-docs://api/widgets/RawView)
The lower level workhorse widget for [View](flutter-docs://api/widgets/View) that bootstraps a render tree
for a view.

[ReadingOrderTraversalPolicy](flutter-docs://api/widgets/ReadingOrderTraversalPolicy)
Traverses the focus order in "reading order".

[Rect](flutter-docs://api/dart-ui/Rect)
An immutable, 2D, axis-aligned, floating-point rectangle whose coordinates
are relative to a given origin.

[RectangularRangeSliderTrackShape](flutter-docs://api/material/RectangularRangeSliderTrackShape)
A [RangeSlider](flutter-docs://api/material/RangeSlider) track that's a simple rectangle.

[RectangularRangeSliderValueIndicatorShape](flutter-docs://api/material/RectangularRangeSliderValueIndicatorShape)
The default shape of a [RangeSlider](flutter-docs://api/material/RangeSlider)'s value indicators.

[RectangularSliderTrackShape](flutter-docs://api/material/RectangularSliderTrackShape)
A [Slider](flutter-docs://api/material/Slider) track that's a simple rectangle.

[RectangularSliderValueIndicatorShape](flutter-docs://api/material/RectangularSliderValueIndicatorShape)
The default shape of a [Slider](flutter-docs://api/material/Slider)'s value indicator.

[RectTween](flutter-docs://api/animation/RectTween)
An interpolation between two rectangles.

[RedoTextIntent](flutter-docs://api/widgets/RedoTextIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a user interaction that attempts to go back to
the previous editing state.

[RefreshIndicator](flutter-docs://api/material/RefreshIndicator)
A widget that supports the Material "swipe to refresh" idiom.

[RefreshIndicatorState](flutter-docs://api/material/RefreshIndicatorState)
Contains the state for a [RefreshIndicator](flutter-docs://api/material/RefreshIndicator). This class can be used to
programmatically show the refresh indicator, see the [show](flutter-docs://api/material/RefreshIndicatorState/show) method.

[RefreshProgressIndicator](flutter-docs://api/material/RefreshProgressIndicator)
An indicator for the progress of refreshing the contents of a widget.

[RelativePositionedTransition](flutter-docs://api/widgets/RelativePositionedTransition)
Animated version of [Positioned](flutter-docs://api/widgets/Positioned) which transitions the child's position
based on the value of [rect](flutter-docs://api/widgets/RelativePositionedTransition/rect) relative to a bounding box with the
specified [size](flutter-docs://api/widgets/RelativePositionedTransition/size).

[RelativeRect](flutter-docs://api/rendering/RelativeRect)
An immutable 2D, axis-aligned, floating-point rectangle whose coordinates
are given relative to another rectangle's edges, known as the container.
Since the dimensions of the rectangle are relative to those of the
container, this class has no width and height members. To determine the
width or height of the rectangle, convert it to a [Rect](flutter-docs://api/dart-ui/Rect) using [toRect()](flutter-docs://api/rendering/RelativeRect/toRect) (passing the container's own Rect), and then examine that object.

[RelativeRectTween](flutter-docs://api/widgets/RelativeRectTween)
An interpolation between two relative rects.

[RenderBox](flutter-docs://api/rendering/RenderBox)
A render object in a 2D Cartesian coordinate system.

[RenderNestedScrollViewViewport](flutter-docs://api/widgets/RenderNestedScrollViewViewport)
The [RenderViewport](flutter-docs://api/rendering/RenderViewport) variant used by [NestedScrollView](flutter-docs://api/widgets/NestedScrollView).

[RenderObject](flutter-docs://api/rendering/RenderObject)
An object in the render tree.

[RenderObjectElement](flutter-docs://api/widgets/RenderObjectElement)
An [Element](flutter-docs://api/widgets/Element) that uses a [RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget) as its configuration.

[RenderObjectToWidgetAdapter](flutter-docs://api/widgets/RenderObjectToWidgetAdapter)<T extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
A bridge from a [RenderObject](flutter-docs://api/rendering/RenderObject) to an [Element](flutter-docs://api/widgets/Element) tree.

[RenderObjectToWidgetElement](flutter-docs://api/widgets/RenderObjectToWidgetElement)<T extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
The root of an element tree that is hosted by a [RenderObject](flutter-docs://api/rendering/RenderObject).

[RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget)
[RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget) s provide the configuration for [RenderObjectElement](flutter-docs://api/widgets/RenderObjectElement) s,
which wrap [RenderObject](flutter-docs://api/rendering/RenderObject) s, which provide the actual rendering of the
application.

[RenderSemanticsGestureHandler](flutter-docs://api/rendering/RenderSemanticsGestureHandler)
Listens for the specified gestures from the semantics server (e.g.
an accessibility tool).

[RenderSliverOverlapAbsorber](flutter-docs://api/widgets/RenderSliverOverlapAbsorber)
A sliver that wraps another, forcing its layout extent to be treated as
overlap.

[RenderSliverOverlapInjector](flutter-docs://api/widgets/RenderSliverOverlapInjector)
A sliver that has a sliver geometry based on the values stored in a
[SliverOverlapAbsorberHandle](flutter-docs://api/widgets/SliverOverlapAbsorberHandle).

[RenderTapRegion](flutter-docs://api/widgets/RenderTapRegion)
A render object that defines a region that can detect taps inside or outside
of itself and any group of regions it belongs to, without participating in
the [gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system.

[RenderTapRegionSurface](flutter-docs://api/widgets/RenderTapRegionSurface)
A render object that provides notification of a tap inside or outside of a
set of registered regions, without participating in the [gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system
(other than to consume tap down events if [TapRegion.consumeOutsideTaps](flutter-docs://api/widgets/TapRegion/consumeOutsideTaps) is
true).

[RenderTreeRootElement](flutter-docs://api/widgets/RenderTreeRootElement)
A [RenderObjectElement](flutter-docs://api/widgets/RenderObjectElement) used to manage the root of a render tree.

[RenderTwoDimensionalViewport](flutter-docs://api/widgets/RenderTwoDimensionalViewport)
A base class for viewing render objects that scroll in two dimensions.

[ReorderableDelayedDragStartListener](flutter-docs://api/widgets/ReorderableDelayedDragStartListener)
A wrapper widget that will recognize the start of a drag operation by
looking for a long press event. Once it is recognized, it will start
a drag operation on the wrapped item in the reorderable list.

[ReorderableDragStartListener](flutter-docs://api/widgets/ReorderableDragStartListener)
A wrapper widget that will recognize the start of a drag on the wrapped
widget by a [PointerDownEvent](flutter-docs://api/gestures/PointerDownEvent), and immediately initiate dragging the
wrapped item to a new location in a reorderable list.

[ReorderableList](flutter-docs://api/widgets/ReorderableList)
A scrolling container that allows the user to interactively reorder the
list items.

[ReorderableListState](flutter-docs://api/widgets/ReorderableListState)
The state for a list that allows the user to interactively reorder
the list items.

[ReorderableListView](flutter-docs://api/material/ReorderableListView)
A list whose items the user can interactively reorder by dragging.

[RepaintBoundary](flutter-docs://api/widgets/RepaintBoundary)
A widget that creates a separate display list for its child.

[ReplaceTextIntent](flutter-docs://api/widgets/ReplaceTextIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a user interaction that attempts to modify the
current [TextEditingValue](flutter-docs://api/flutter_test/TextEditingValue) in an input field.

[RequestFocusAction](flutter-docs://api/widgets/RequestFocusAction)
An [Action](flutter-docs://api/widgets/Action) that requests the focus on the node it is given in its
[RequestFocusIntent](flutter-docs://api/widgets/RequestFocusIntent).

[RequestFocusIntent](flutter-docs://api/widgets/RequestFocusIntent)
An intent for use with the [RequestFocusAction](flutter-docs://api/widgets/RequestFocusAction), which supplies the
[FocusNode](flutter-docs://api/widgets/FocusNode) that should be focused.

[ResizeImage](flutter-docs://api/painting/ResizeImage)
Instructs Flutter to decode the image at the specified dimensions
instead of at its native size.

[ResizeImageKey](flutter-docs://api/painting/ResizeImageKey)
Key used internally by [ResizeImage](flutter-docs://api/painting/ResizeImage).

[RestorableBool](flutter-docs://api/widgets/RestorableBool)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [bool](flutter-docs://api/dart-core/bool).

[RestorableBoolN](flutter-docs://api/widgets/RestorableBoolN)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [bool](flutter-docs://api/dart-core/bool) that is
nullable.

[RestorableChangeNotifier](flutter-docs://api/widgets/RestorableChangeNotifier)<T extends [ChangeNotifier](flutter-docs://api/foundation/ChangeNotifier)>
A base class for creating a [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that stores and restores a
[ChangeNotifier](flutter-docs://api/foundation/ChangeNotifier).

[RestorableDateTime](flutter-docs://api/widgets/RestorableDateTime)
A [RestorableValue](flutter-docs://api/widgets/RestorableValue) that knows how to save and restore [DateTime](flutter-docs://api/dart-core/DateTime).

[RestorableDateTimeN](flutter-docs://api/widgets/RestorableDateTimeN)
A [RestorableValue](flutter-docs://api/widgets/RestorableValue) that knows how to save and restore [DateTime](flutter-docs://api/dart-core/DateTime) that is
nullable.

[RestorableDouble](flutter-docs://api/widgets/RestorableDouble)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [double](flutter-docs://api/dart-core/double).

[RestorableDoubleN](flutter-docs://api/widgets/RestorableDoubleN)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [double](flutter-docs://api/dart-core/double) that is nullable.

[RestorableEnum](flutter-docs://api/widgets/RestorableEnum)<T extends [Enum](flutter-docs://api/dart-core/Enum)>
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore an [Enum](flutter-docs://api/dart-core/Enum) type.

[RestorableEnumN](flutter-docs://api/widgets/RestorableEnumN)<T extends [Enum](flutter-docs://api/dart-core/Enum)>
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a nullable [Enum](flutter-docs://api/dart-core/Enum) type.

[RestorableInt](flutter-docs://api/widgets/RestorableInt)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore an [int](flutter-docs://api/dart-core/int).

[RestorableIntN](flutter-docs://api/widgets/RestorableIntN)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore an [int](flutter-docs://api/dart-core/int) that is nullable.

[RestorableListenable](flutter-docs://api/widgets/RestorableListenable)<T extends [Listenable](flutter-docs://api/foundation/Listenable)>
A base class for creating a [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that stores and restores a
[Listenable](flutter-docs://api/foundation/Listenable).

[RestorableNum](flutter-docs://api/widgets/RestorableNum)<T extends [num](flutter-docs://api/dart-core/num)>
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [num](flutter-docs://api/dart-core/num).

[RestorableNumN](flutter-docs://api/widgets/RestorableNumN)<T extends [num](flutter-docs://api/dart-core/num)?>
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [num](flutter-docs://api/dart-core/num) that is nullable.

[RestorableProperty](flutter-docs://api/widgets/RestorableProperty)<T>
Manages an object of type `T`, whose value a [State](flutter-docs://api/widgets/State) object wants to have
restored during state restoration.

[RestorableRouteFuture](flutter-docs://api/widgets/RestorableRouteFuture)<T>
Gives access to a [Route](flutter-docs://api/widgets/Route) object and its return value that was added to a
navigator via one of its "restorable" API methods.

[RestorableString](flutter-docs://api/widgets/RestorableString)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [String](flutter-docs://api/dart-core/String).

[RestorableStringN](flutter-docs://api/widgets/RestorableStringN)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a [String](flutter-docs://api/dart-core/String) that is nullable.

[RestorableTextEditingController](flutter-docs://api/widgets/RestorableTextEditingController)
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that knows how to store and restore a
[TextEditingController](flutter-docs://api/widgets/TextEditingController).

[RestorableTimeOfDay](flutter-docs://api/material/RestorableTimeOfDay)
A [RestorableValue](flutter-docs://api/widgets/RestorableValue) that knows how to save and restore [TimeOfDay](flutter-docs://api/material/TimeOfDay).

[RestorableValue](flutter-docs://api/widgets/RestorableValue)<T>
A [RestorableProperty](flutter-docs://api/widgets/RestorableProperty) that makes the wrapped value accessible to the owning
[State](flutter-docs://api/widgets/State) object via the [value](flutter-docs://api/widgets/RestorableValue/value) getter and setter.

[RestorationBucket](flutter-docs://api/services/RestorationBucket)
A [RestorationBucket](flutter-docs://api/services/RestorationBucket) holds pieces of the restoration data that a part of
the application needs to restore its state.

[RestorationScope](flutter-docs://api/widgets/RestorationScope)
Creates a new scope for restoration IDs used by descendant widgets to claim
[RestorationBucket](flutter-docs://api/services/RestorationBucket) s.

[ReverseAnimation](flutter-docs://api/animation/ReverseAnimation)
An animation that is the reverse of another animation.

[ReverseTween](flutter-docs://api/animation/ReverseTween)<T extends [Object](flutter-docs://api/dart-core/Object)?>
A [Tween](flutter-docs://api/animation/Tween) that evaluates its [parent](flutter-docs://api/animation/ReverseTween/parent) in reverse.

[RichText](flutter-docs://api/widgets/RichText)
A paragraph of rich text.

[RootBackButtonDispatcher](flutter-docs://api/widgets/RootBackButtonDispatcher)
The default implementation of back button dispatcher for the root router.

[RootElement](flutter-docs://api/widgets/RootElement)
The root of the element tree.

[RootRenderObjectElement](flutter-docs://api/widgets/RootRenderObjectElement)
Deprecated. Unused in the framework and will be removed in a future version
of Flutter.

[RootRestorationScope](flutter-docs://api/widgets/RootRestorationScope)
Inserts a child bucket of [RestorationManager.rootBucket](flutter-docs://api/services/RestorationManager/rootBucket) into the widget
tree and makes it available to descendants via [RestorationScope.of](flutter-docs://api/widgets/RestorationScope/of).

[RootWidget](flutter-docs://api/widgets/RootWidget)
A widget for the root of the widget tree.

[RotatedBox](flutter-docs://api/widgets/RotatedBox)
A widget that rotates its child by a integral number of quarter turns.

[RotationTransition](flutter-docs://api/widgets/RotationTransition)
Animates the rotation of a widget.

[RoundedRectangleBorder](flutter-docs://api/painting/RoundedRectangleBorder)
A rectangular border with rounded corners.

[RoundedRectRangeSliderTrackShape](flutter-docs://api/material/RoundedRectRangeSliderTrackShape)
The default shape of a [RangeSlider](flutter-docs://api/material/RangeSlider)'s track.

[RoundedRectRangeSliderValueIndicatorShape](flutter-docs://api/material/RoundedRectRangeSliderValueIndicatorShape)
The rounded rectangle shape of a [RangeSlider](flutter-docs://api/material/RangeSlider)'s value indicators.

[RoundedRectSliderTrackShape](flutter-docs://api/material/RoundedRectSliderTrackShape)
The default shape of a [Slider](flutter-docs://api/material/Slider)'s track.

[RoundedRectSliderValueIndicatorShape](flutter-docs://api/material/RoundedRectSliderValueIndicatorShape)
The rounded rectangle shape of a [Slider](flutter-docs://api/material/Slider)'s value indicator.

[RoundedSuperellipseBorder](flutter-docs://api/painting/RoundedSuperellipseBorder)
A rectangular border with rounded corners following the shape of an
[RSuperellipse](flutter-docs://api/dart-ui/RSuperellipse).

[RoundRangeSliderThumbShape](flutter-docs://api/material/RoundRangeSliderThumbShape)
The default shape of a [RangeSlider](flutter-docs://api/material/RangeSlider)'s thumbs.

[RoundRangeSliderTickMarkShape](flutter-docs://api/material/RoundRangeSliderTickMarkShape)
The default shape of each [RangeSlider](flutter-docs://api/material/RangeSlider) tick mark.

[RoundSliderOverlayShape](flutter-docs://api/material/RoundSliderOverlayShape)
The default shape of a [Slider](flutter-docs://api/material/Slider)'s thumb overlay.

[RoundSliderThumbShape](flutter-docs://api/material/RoundSliderThumbShape)
The default shape of a [Slider](flutter-docs://api/material/Slider)'s thumb.

[RoundSliderTickMarkShape](flutter-docs://api/material/RoundSliderTickMarkShape)
The default shape of each [Slider](flutter-docs://api/material/Slider) tick mark.

[Route](flutter-docs://api/widgets/Route)<T>
An abstraction for an entry managed by a [Navigator](flutter-docs://api/widgets/Navigator).

[RouteAware](flutter-docs://api/widgets/RouteAware)
An interface for objects that are aware of their current [Route](flutter-docs://api/widgets/Route).

[RouteInformation](flutter-docs://api/widgets/RouteInformation)
A piece of routing information.

[RouteInformationParser](flutter-docs://api/widgets/RouteInformationParser)<T>
A delegate that is used by the [Router](flutter-docs://api/widgets/Router) widget to parse a route information
into a configuration of type T.

[RouteInformationProvider](flutter-docs://api/widgets/RouteInformationProvider)
A route information provider that provides route information for the
[Router](flutter-docs://api/widgets/Router) widget

[RouteObserver](flutter-docs://api/widgets/RouteObserver)<R extends [Route](flutter-docs://api/widgets/Route)>
A [Navigator](flutter-docs://api/widgets/Navigator) observer that notifies [RouteAware](flutter-docs://api/widgets/RouteAware) s of changes to the
state of their [Route](flutter-docs://api/widgets/Route).

[Router](flutter-docs://api/widgets/Router)<T>
The dispatcher for opening and closing pages of an application.

[RouterConfig](flutter-docs://api/widgets/RouterConfig)<T>
A convenient bundle to configure a [Router](flutter-docs://api/widgets/Router) widget.

[RouterDelegate](flutter-docs://api/widgets/RouterDelegate)<T>
A delegate that is used by the [Router](flutter-docs://api/widgets/Router) widget to build and configure a
navigating widget.

[RouteSettings](flutter-docs://api/widgets/RouteSettings)
Data that might be useful in constructing a [Route](flutter-docs://api/widgets/Route).

[RouteTransitionRecord](flutter-docs://api/widgets/RouteTransitionRecord)
A [Route](flutter-docs://api/widgets/Route) wrapper interface that can be staged for [TransitionDelegate](flutter-docs://api/widgets/TransitionDelegate) to
decide how its underlying [Route](flutter-docs://api/widgets/Route) should transition on or off screen.

[Row](flutter-docs://api/widgets/Row)
A widget that displays its children in a horizontal array.

[RRect](flutter-docs://api/dart-ui/RRect)
An immutable rounded rectangle with the custom radii for all four corners.

[RSTransform](flutter-docs://api/dart-ui/RSTransform)
A transform consisting of a translation, a rotation, and a uniform scale.

[RSuperellipse](flutter-docs://api/dart-ui/RSuperellipse)
An immutable rounded superellipse.

[SafeArea](flutter-docs://api/widgets/SafeArea)
A widget that insets its child with sufficient padding to avoid intrusions
by the operating system.

[SawTooth](flutter-docs://api/animation/SawTooth)
A sawtooth curve that repeats a given number of times over the unit interval.

[Scaffold](flutter-docs://api/material/Scaffold)
Implements the basic Material Design visual layout structure.

[ScaffoldFeatureController](flutter-docs://api/material/ScaffoldFeatureController)<T extends [Widget](flutter-docs://api/widgets/Widget), U>
An interface for controlling a feature of a [Scaffold](flutter-docs://api/material/Scaffold).

[ScaffoldGeometry](flutter-docs://api/material/ScaffoldGeometry)
Geometry information for [Scaffold](flutter-docs://api/material/Scaffold) components after layout is finished.

[ScaffoldMessenger](flutter-docs://api/material/ScaffoldMessenger)
Manages [SnackBar](flutter-docs://api/material/SnackBar) s and [MaterialBanner](flutter-docs://api/material/MaterialBanner) s for descendant [Scaffold](flutter-docs://api/material/Scaffold) s.

[ScaffoldMessengerState](flutter-docs://api/material/ScaffoldMessengerState)
State for a [ScaffoldMessenger](flutter-docs://api/material/ScaffoldMessenger).

[ScaffoldPrelayoutGeometry](flutter-docs://api/material/ScaffoldPrelayoutGeometry)
The geometry of the [Scaffold](flutter-docs://api/material/Scaffold) after all its contents have been laid out
except the [FloatingActionButton](flutter-docs://api/material/FloatingActionButton).

[ScaffoldState](flutter-docs://api/material/ScaffoldState)
State for a [Scaffold](flutter-docs://api/material/Scaffold).

[ScaleEndDetails](flutter-docs://api/gestures/ScaleEndDetails)
Details for [GestureScaleEndCallback](flutter-docs://api/gestures/GestureScaleEndCallback).

[ScaleStartDetails](flutter-docs://api/gestures/ScaleStartDetails)
Details for [GestureScaleStartCallback](flutter-docs://api/gestures/GestureScaleStartCallback).

[ScaleTransition](flutter-docs://api/widgets/ScaleTransition)
Animates the scale of a transformed widget.

[ScaleUpdateDetails](flutter-docs://api/gestures/ScaleUpdateDetails)
Details for [GestureScaleUpdateCallback](flutter-docs://api/gestures/GestureScaleUpdateCallback).

[Scrollable](flutter-docs://api/widgets/Scrollable)
A widget that manages scrolling in one dimension and informs the [Viewport](flutter-docs://api/widgets/Viewport) through which the content is viewed.

[ScrollableDetails](flutter-docs://api/widgets/ScrollableDetails)
Describes the aspects of a Scrollable widget to inform inherited widgets
like [ScrollBehavior](flutter-docs://api/widgets/ScrollBehavior) for decorating or enumerate the properties of combined
Scrollables, such as [TwoDimensionalScrollable](flutter-docs://api/widgets/TwoDimensionalScrollable).

[ScrollableState](flutter-docs://api/widgets/ScrollableState)
State object for a [Scrollable](flutter-docs://api/widgets/Scrollable) widget.

[ScrollAction](flutter-docs://api/widgets/ScrollAction)
An [Action](flutter-docs://api/widgets/Action) that scrolls the relevant [Scrollable](flutter-docs://api/widgets/Scrollable) by the amount configured
in the [ScrollIntent](flutter-docs://api/widgets/ScrollIntent) given to it.

[ScrollActivity](flutter-docs://api/widgets/ScrollActivity)
Base class for scrolling activities like dragging and flinging.

[ScrollActivityDelegate](flutter-docs://api/widgets/ScrollActivityDelegate)
A backend for a [ScrollActivity](flutter-docs://api/widgets/ScrollActivity).

[ScrollAwareImageProvider](flutter-docs://api/widgets/ScrollAwareImageProvider)<T extends [Object](flutter-docs://api/dart-core/Object)>
An [ImageProvider](flutter-docs://api/painting/ImageProvider) that makes use of
[Scrollable.recommendDeferredLoadingForContext](flutter-docs://api/widgets/Scrollable/recommendDeferredLoadingForContext) to avoid loading images when
rapidly scrolling.

[Scrollbar](flutter-docs://api/material/Scrollbar)
A Material Design scrollbar.

[ScrollbarPainter](flutter-docs://api/widgets/ScrollbarPainter)
Paints a scrollbar's track and thumb.

[ScrollbarTheme](flutter-docs://api/material/ScrollbarTheme)
Applies a scrollbar theme to descendant [Scrollbar](flutter-docs://api/material/Scrollbar) widgets.

[ScrollbarThemeData](flutter-docs://api/material/ScrollbarThemeData)
Defines default property values for descendant [Scrollbar](flutter-docs://api/material/Scrollbar) widgets.

[ScrollBehavior](flutter-docs://api/widgets/ScrollBehavior)
Describes how [Scrollable](flutter-docs://api/widgets/Scrollable) widgets should behave.

[ScrollConfiguration](flutter-docs://api/widgets/ScrollConfiguration)
Controls how [Scrollable](flutter-docs://api/widgets/Scrollable) widgets behave in a subtree.

[ScrollContext](flutter-docs://api/widgets/ScrollContext)
An interface that [Scrollable](flutter-docs://api/widgets/Scrollable) widgets implement in order to use
[ScrollPosition](flutter-docs://api/widgets/ScrollPosition).

[ScrollController](flutter-docs://api/widgets/ScrollController)
Controls a scrollable widget.

[ScrollDragController](flutter-docs://api/widgets/ScrollDragController)
Scrolls a scroll view as the user drags their finger across the screen.

[ScrollEndNotification](flutter-docs://api/widgets/ScrollEndNotification)
A notification that a [Scrollable](flutter-docs://api/widgets/Scrollable) widget has stopped scrolling.

[ScrollHoldController](flutter-docs://api/widgets/ScrollHoldController)
Interface for holding a [Scrollable](flutter-docs://api/widgets/Scrollable) stationary.

[ScrollIncrementDetails](flutter-docs://api/widgets/ScrollIncrementDetails)
A details object that describes the type of scroll increment being requested
of a [ScrollIncrementCalculator](flutter-docs://api/widgets/ScrollIncrementCalculator) function, as well as the current metrics
for the scrollable.

[ScrollIntent](flutter-docs://api/widgets/ScrollIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents scrolling the nearest scrollable by an amount
appropriate for the [type](flutter-docs://api/widgets/ScrollIntent/type) specified.

[ScrollMetricsNotification](flutter-docs://api/widgets/ScrollMetricsNotification)
A notification that a scrollable widget's [ScrollMetrics](flutter-docs://api/widgets/ScrollMetrics) have changed.

[ScrollNotification](flutter-docs://api/widgets/ScrollNotification)
A [Notification](flutter-docs://api/widgets/Notification) related to scrolling.

[ScrollNotificationObserver](flutter-docs://api/widgets/ScrollNotificationObserver)
Notifies its listeners when a descendant scrolls.

[ScrollNotificationObserverState](flutter-docs://api/widgets/ScrollNotificationObserverState)
The listener list state for a [ScrollNotificationObserver](flutter-docs://api/widgets/ScrollNotificationObserver) returned by
[ScrollNotificationObserver.of](flutter-docs://api/widgets/ScrollNotificationObserver/of).

[ScrollPhysics](flutter-docs://api/widgets/ScrollPhysics)
Determines the physics of a [Scrollable](flutter-docs://api/widgets/Scrollable) widget.

[ScrollPosition](flutter-docs://api/widgets/ScrollPosition)
Determines which portion of the content is visible in a scroll view.

[ScrollPositionWithSingleContext](flutter-docs://api/widgets/ScrollPositionWithSingleContext)
A scroll position that manages scroll activities for a single
[ScrollContext](flutter-docs://api/widgets/ScrollContext).

[ScrollSpringSimulation](flutter-docs://api/physics/ScrollSpringSimulation)
A [SpringSimulation](flutter-docs://api/physics/SpringSimulation) where the value of [x](flutter-docs://api/physics/ScrollSpringSimulation/x) is guaranteed to have exactly the
end value when the simulation [isDone](flutter-docs://api/physics/SpringSimulation/isDone).

[ScrollStartNotification](flutter-docs://api/widgets/ScrollStartNotification)
A notification that a [Scrollable](flutter-docs://api/widgets/Scrollable) widget has started scrolling.

[ScrollToDocumentBoundaryIntent](flutter-docs://api/widgets/ScrollToDocumentBoundaryIntent)
Scrolls to the beginning or end of the document depending on the [forward](flutter-docs://api/widgets/DirectionalTextEditingIntent/forward) parameter.

[ScrollUpdateNotification](flutter-docs://api/widgets/ScrollUpdateNotification)
A notification that a [Scrollable](flutter-docs://api/widgets/Scrollable) widget has changed its scroll position.

[ScrollView](flutter-docs://api/widgets/ScrollView)
A widget that combines a [Scrollable](flutter-docs://api/widgets/Scrollable) and a [Viewport](flutter-docs://api/widgets/Viewport) to create an
interactive scrolling pane of content in one dimension.

[SearchAnchor](flutter-docs://api/material/SearchAnchor)
Manages a "search view" route that allows the user to select one of the
suggested completions for a search query.

[SearchBar](flutter-docs://api/material/SearchBar)
A Material Design search bar.

[SearchBarTheme](flutter-docs://api/material/SearchBarTheme)
Applies a search bar theme to descendant [SearchBar](flutter-docs://api/material/SearchBar) widgets.

[SearchBarThemeData](flutter-docs://api/material/SearchBarThemeData)
Defines default property values for descendant [SearchBar](flutter-docs://api/material/SearchBar) widgets.

[SearchController](flutter-docs://api/material/SearchController)
A controller to manage a search view created by [SearchAnchor](flutter-docs://api/material/SearchAnchor).

[SearchDelegate](flutter-docs://api/material/SearchDelegate)<T>
Delegate for [showSearch](flutter-docs://api/material/showSearch) to define the content of the search page.

[SearchViewTheme](flutter-docs://api/material/SearchViewTheme)
An inherited widget that defines the configuration in this widget's
descendants for search view created by the [SearchAnchor](flutter-docs://api/material/SearchAnchor) widget.

[SearchViewThemeData](flutter-docs://api/material/SearchViewThemeData)
Defines the configuration of the search views created by the [SearchAnchor](flutter-docs://api/material/SearchAnchor) widget.

[SegmentedButton](flutter-docs://api/material/SegmentedButton)<T>
A Material button that allows the user to select from limited set of options.

[SegmentedButtonState](flutter-docs://api/material/SegmentedButtonState)<T>
State for [SegmentedButton](flutter-docs://api/material/SegmentedButton).

[SegmentedButtonTheme](flutter-docs://api/material/SegmentedButtonTheme)
An inherited widget that defines the visual properties for
[SegmentedButton](flutter-docs://api/material/SegmentedButton) s in this widget's subtree.

[SegmentedButtonThemeData](flutter-docs://api/material/SegmentedButtonThemeData)
Overrides the default values of visual properties for descendant
[SegmentedButton](flutter-docs://api/material/SegmentedButton) widgets.

[SelectableChipAttributes](flutter-docs://api/material/SelectableChipAttributes)
An interface for Material Design chips that can be selected.

[SelectableRegion](flutter-docs://api/widgets/SelectableRegion)
A widget that introduces an area for user selections.

[SelectableRegionSelectionStatusScope](flutter-docs://api/widgets/SelectableRegionSelectionStatusScope)
Notifies its listeners when the selection under a [SelectableRegion](flutter-docs://api/widgets/SelectableRegion) or
[SelectionArea](flutter-docs://api/material/SelectionArea) is being changed or finalized.

[SelectableRegionState](flutter-docs://api/widgets/SelectableRegionState)
State for a [SelectableRegion](flutter-docs://api/widgets/SelectableRegion).

[SelectableText](flutter-docs://api/material/SelectableText)
A run of selectable text with a single style.

[SelectAction](flutter-docs://api/widgets/SelectAction)
An action that selects the currently focused control.

[SelectAllTextIntent](flutter-docs://api/widgets/SelectAllTextIntent)
An [Intent](flutter-docs://api/widgets/Intent) to select everything in the field.

[SelectIntent](flutter-docs://api/widgets/SelectIntent)
An [Intent](flutter-docs://api/widgets/Intent) that selects the currently focused control.

[SelectionArea](flutter-docs://api/material/SelectionArea)
A widget that introduces an area for user selections with adaptive selection
controls.

[SelectionAreaState](flutter-docs://api/material/SelectionAreaState)
State for a [SelectionArea](flutter-docs://api/material/SelectionArea).

[SelectionContainer](flutter-docs://api/widgets/SelectionContainer)
A container that handles [SelectionEvent](flutter-docs://api/rendering/SelectionEvent) s for the [Selectable](flutter-docs://api/rendering/Selectable) s in
the subtree.

[SelectionContainerDelegate](flutter-docs://api/widgets/SelectionContainerDelegate)
A delegate to handle [SelectionEvent](flutter-docs://api/rendering/SelectionEvent) s for a [SelectionContainer](flutter-docs://api/widgets/SelectionContainer).

[SelectionDetails](flutter-docs://api/widgets/SelectionDetails)
A read-only interface for accessing the details of a selection under a [SelectionListener](flutter-docs://api/widgets/SelectionListener).

[SelectionListener](flutter-docs://api/widgets/SelectionListener)
A [SelectionContainer](flutter-docs://api/widgets/SelectionContainer) that allows the user to access the [SelectionDetails](flutter-docs://api/widgets/SelectionDetails) and
listen to selection changes for the child subtree it wraps under a [SelectionArea](flutter-docs://api/material/SelectionArea) or [SelectableRegion](flutter-docs://api/widgets/SelectableRegion).

[SelectionListenerNotifier](flutter-docs://api/widgets/SelectionListenerNotifier)
Notifies listeners when the selection under a [SelectionListener](flutter-docs://api/widgets/SelectionListener) has been
changed.

[SelectionOverlay](flutter-docs://api/widgets/SelectionOverlay)
An object that manages a pair of selection handles and a toolbar.

[SelectionRegistrarScope](flutter-docs://api/widgets/SelectionRegistrarScope)
An inherited widget to host a [SelectionRegistrar](flutter-docs://api/rendering/SelectionRegistrar) for the subtree.

[Semantics](flutter-docs://api/widgets/Semantics)
A widget that annotates the widget tree with a description of the meaning of
the widgets.

[SemanticsDebugger](flutter-docs://api/widgets/SemanticsDebugger)
A widget that visualizes the semantics for the child.

[SemanticsGestureDelegate](flutter-docs://api/widgets/SemanticsGestureDelegate)
A base class that describes what semantics notations a [RawGestureDetector](flutter-docs://api/widgets/RawGestureDetector) should add to the render object [RenderSemanticsGestureHandler](flutter-docs://api/rendering/RenderSemanticsGestureHandler).

[SensitiveContent](flutter-docs://api/widgets/SensitiveContent)
Widget to set the [ContentSensitivity](flutter-docs://api/services/ContentSensitivity) of content in the widget
tree.

[SensitiveContentHost](flutter-docs://api/widgets/SensitiveContentHost)
Host of the current content sensitivity for the widget tree that contains
some number [SensitiveContent](flutter-docs://api/widgets/SensitiveContent) widgets.

[Shader](flutter-docs://api/dart-ui/Shader)
Base class for objects such as [Gradient](flutter-docs://api/dart-ui/Gradient) and [ImageShader](flutter-docs://api/dart-ui/ImageShader) which
correspond to shaders as used by [Paint.shader](flutter-docs://api/dart-ui/Paint/shader).

[ShaderMask](flutter-docs://api/widgets/ShaderMask)
A widget that applies a mask generated by a [Shader](flutter-docs://api/dart-ui/Shader) to its child.

[ShaderWarmUp](flutter-docs://api/painting/ShaderWarmUp)
Interface for drawing an image to warm up Skia shader compilations.

[Shadow](flutter-docs://api/dart-ui/Shadow)
A single shadow.

[ShapeBorder](flutter-docs://api/painting/ShapeBorder)
Base class for shape outlines.

[ShapeBorderClipper](flutter-docs://api/rendering/ShapeBorderClipper)
A [CustomClipper](flutter-docs://api/rendering/CustomClipper) that clips to the outer path of a [ShapeBorder](flutter-docs://api/painting/ShapeBorder).

[ShapeBorderTween](flutter-docs://api/material/ShapeBorderTween)
An interpolation between two [ShapeBorder](flutter-docs://api/painting/ShapeBorder) s.

[ShapeDecoration](flutter-docs://api/painting/ShapeDecoration)
An immutable description of how to paint an arbitrary shape.

[SharedAppData](flutter-docs://api/widgets/SharedAppData)
Enables sharing key/value data with its `child` and all of the
child's descendants.

[ShortcutActivator](flutter-docs://api/widgets/ShortcutActivator)
An interface to define the keyboard key combination to trigger a shortcut.

[ShortcutManager](flutter-docs://api/widgets/ShortcutManager)
A manager of keyboard shortcut bindings used by [Shortcuts](flutter-docs://api/widgets/Shortcuts) to handle key
events.

[ShortcutMapProperty](flutter-docs://api/widgets/ShortcutMapProperty)
A [DiagnosticsProperty](flutter-docs://api/foundation/DiagnosticsProperty) which handles formatting a `Map<LogicalKeySet, Intent>` (the same type as the [Shortcuts.shortcuts](flutter-docs://api/widgets/Shortcuts/shortcuts) property) so that its
diagnostic output is human-readable.

[ShortcutRegistrar](flutter-docs://api/widgets/ShortcutRegistrar)
A widget that holds a [ShortcutRegistry](flutter-docs://api/widgets/ShortcutRegistry) which allows descendants to add,
remove, or replace shortcuts.

[ShortcutRegistry](flutter-docs://api/widgets/ShortcutRegistry)
A class used by [ShortcutRegistrar](flutter-docs://api/widgets/ShortcutRegistrar) that allows adding or removing shortcut
bindings by descendants of the [ShortcutRegistrar](flutter-docs://api/widgets/ShortcutRegistrar).

[ShortcutRegistryEntry](flutter-docs://api/widgets/ShortcutRegistryEntry)
A entry returned by [ShortcutRegistry.addAll](flutter-docs://api/widgets/ShortcutRegistry/addAll) that allows the caller to
identify the shortcuts they registered with the [ShortcutRegistry](flutter-docs://api/widgets/ShortcutRegistry) through
the [ShortcutRegistrar](flutter-docs://api/widgets/ShortcutRegistrar).

[Shortcuts](flutter-docs://api/widgets/Shortcuts)
A widget that creates key bindings to specific actions for its
descendants.

[ShortcutSerialization](flutter-docs://api/widgets/ShortcutSerialization)
A class used by [MenuSerializableShortcut](flutter-docs://api/widgets/MenuSerializableShortcut) to describe the shortcut for
serialization to send to the platform for rendering a [PlatformMenuBar](flutter-docs://api/widgets/PlatformMenuBar).

[ShrinkWrappingViewport](flutter-docs://api/widgets/ShrinkWrappingViewport)
A widget that is bigger on the inside and shrink wraps its children in the
main axis.

[SimpleDialog](flutter-docs://api/material/SimpleDialog)
A simple Material Design dialog.

[SimpleDialogOption](flutter-docs://api/material/SimpleDialogOption)
An option used in a [SimpleDialog](flutter-docs://api/material/SimpleDialog).

[Simulation](flutter-docs://api/physics/Simulation)
The base class for all simulations.

[SingleActivator](flutter-docs://api/widgets/SingleActivator)
A shortcut key combination of a single key and modifiers.

[SingleChildLayoutDelegate](flutter-docs://api/rendering/SingleChildLayoutDelegate)
A delegate for computing the layout of a render object with a single child.

[SingleChildRenderObjectElement](flutter-docs://api/widgets/SingleChildRenderObjectElement)
An [Element](flutter-docs://api/widgets/Element) that uses a [SingleChildRenderObjectWidget](flutter-docs://api/widgets/SingleChildRenderObjectWidget) as its configuration.

[SingleChildRenderObjectWidget](flutter-docs://api/widgets/SingleChildRenderObjectWidget)
A superclass for [RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget) s that configure [RenderObject](flutter-docs://api/rendering/RenderObject) subclasses
that have a single child slot.

[SingleChildScrollView](flutter-docs://api/widgets/SingleChildScrollView)
A box in which a single widget can be scrolled.

[Size](flutter-docs://api/dart-ui/Size)
Holds a 2D floating-point size.

[SizeChangedLayoutNotification](flutter-docs://api/widgets/SizeChangedLayoutNotification)
Indicates that the size of one of the descendants of the object receiving
this notification has changed, and that therefore any assumptions about that
layout are no longer valid.

[SizeChangedLayoutNotifier](flutter-docs://api/widgets/SizeChangedLayoutNotifier)
A widget that automatically dispatches a [SizeChangedLayoutNotification](flutter-docs://api/widgets/SizeChangedLayoutNotification) when the layout dimensions of its child change.

[SizedBox](flutter-docs://api/widgets/SizedBox)
A box with a specified size.

[SizedOverflowBox](flutter-docs://api/widgets/SizedOverflowBox)
A widget that is a specific size but passes its original constraints
through to its child, which may then overflow.

[SizeTransition](flutter-docs://api/widgets/SizeTransition)
Animates its own size and clips and aligns its child.

[SizeTween](flutter-docs://api/animation/SizeTween)
An interpolation between two sizes.

[Slider](flutter-docs://api/material/Slider)
A Material Design slider.

[SliderComponentShape](flutter-docs://api/material/SliderComponentShape)
Base class for slider thumb, thumb overlay, and value indicator shapes.

[SliderTheme](flutter-docs://api/material/SliderTheme)
Applies a slider theme to descendant [Slider](flutter-docs://api/material/Slider) widgets.

[SliderThemeData](flutter-docs://api/material/SliderThemeData)
Holds the color, shape, and typography values for a Material Design slider
theme.

[SliderTickMarkShape](flutter-docs://api/material/SliderTickMarkShape)
Base class for [Slider](flutter-docs://api/material/Slider) tick mark shapes.

[SliderTrackShape](flutter-docs://api/material/SliderTrackShape)
Base class for slider track shapes.

[SlideTransition](flutter-docs://api/widgets/SlideTransition)
Animates the position of a widget relative to its normal position.

[SliverAnimatedGrid](flutter-docs://api/widgets/SliverAnimatedGrid)
A [SliverGrid](flutter-docs://api/widgets/SliverGrid) that animates items when they are inserted or removed.

[SliverAnimatedGridState](flutter-docs://api/widgets/SliverAnimatedGridState)
The state for a [SliverAnimatedGrid](flutter-docs://api/widgets/SliverAnimatedGrid) that animates items when they are
inserted or removed.

[SliverAnimatedList](flutter-docs://api/widgets/SliverAnimatedList)
A [SliverList](flutter-docs://api/widgets/SliverList) that animates items when they are inserted or removed.

[SliverAnimatedListState](flutter-docs://api/widgets/SliverAnimatedListState)
The state for a [SliverAnimatedList](flutter-docs://api/widgets/SliverAnimatedList) that animates items when they are
inserted or removed.

[SliverAnimatedOpacity](flutter-docs://api/widgets/SliverAnimatedOpacity)
Animated version of [SliverOpacity](flutter-docs://api/widgets/SliverOpacity) which automatically transitions the
sliver child's opacity over a given duration whenever the given opacity
changes.

[SliverAppBar](flutter-docs://api/material/SliverAppBar)
A Material Design app bar that integrates with a [CustomScrollView](flutter-docs://api/widgets/CustomScrollView).

[SliverChildBuilderDelegate](flutter-docs://api/widgets/SliverChildBuilderDelegate)
A delegate that supplies children for slivers using a builder callback.

[SliverChildDelegate](flutter-docs://api/widgets/SliverChildDelegate)
A delegate that supplies children for slivers.

[SliverChildListDelegate](flutter-docs://api/widgets/SliverChildListDelegate)
A delegate that supplies children for slivers using an explicit list.

[SliverConstrainedCrossAxis](flutter-docs://api/widgets/SliverConstrainedCrossAxis)
A sliver that constrains the cross axis extent of its sliver child.

[SliverCrossAxisExpanded](flutter-docs://api/widgets/SliverCrossAxisExpanded)
Set a flex factor for allocating space in the cross axis direction.

[SliverCrossAxisGroup](flutter-docs://api/widgets/SliverCrossAxisGroup)
A sliver that places multiple sliver children in a linear array along
the cross axis.

[SliverEnsureSemantics](flutter-docs://api/widgets/SliverEnsureSemantics)
A sliver that ensures its sliver child is included in the semantics tree.

[SliverFadeTransition](flutter-docs://api/widgets/SliverFadeTransition)
Animates the opacity of a sliver widget.

[SliverFillRemaining](flutter-docs://api/widgets/SliverFillRemaining)
A sliver that contains a single box child that fills the remaining space in
the viewport.

[SliverFillViewport](flutter-docs://api/widgets/SliverFillViewport)
A sliver that contains multiple box children that each fills the viewport.

[SliverFixedExtentList](flutter-docs://api/widgets/SliverFixedExtentList)
A sliver that places multiple box children with the same main axis extent in
a linear array.

[SliverFloatingHeader](flutter-docs://api/widgets/SliverFloatingHeader)
A sliver that shows its [child](flutter-docs://api/widgets/SliverFloatingHeader/child) when the user scrolls forward and hides it
when the user scrolls backwards.

[SliverGrid](flutter-docs://api/widgets/SliverGrid)
A sliver that places multiple box children in a two dimensional arrangement.

[SliverGridDelegate](flutter-docs://api/rendering/SliverGridDelegate)
Controls the layout of tiles in a grid.

[SliverGridDelegateWithFixedCrossAxisCount](flutter-docs://api/rendering/SliverGridDelegateWithFixedCrossAxisCount)
Creates grid layouts with a fixed number of tiles in the cross axis.

[SliverGridDelegateWithMaxCrossAxisExtent](flutter-docs://api/rendering/SliverGridDelegateWithMaxCrossAxisExtent)
Creates grid layouts with tiles that each have a maximum cross-axis extent.

[SliverIgnorePointer](flutter-docs://api/widgets/SliverIgnorePointer)
A sliver widget that is invisible during hit testing.

[SliverLayoutBuilder](flutter-docs://api/widgets/SliverLayoutBuilder)
Builds a sliver widget tree that can depend on its own [SliverConstraints](flutter-docs://api/rendering/SliverConstraints).

[SliverList](flutter-docs://api/widgets/SliverList)
A sliver that places multiple box children in a linear array along the main
axis.

[SliverMainAxisGroup](flutter-docs://api/widgets/SliverMainAxisGroup)
A sliver that places multiple sliver children in a linear array along
the main axis, one after another.

[SliverMultiBoxAdaptorElement](flutter-docs://api/widgets/SliverMultiBoxAdaptorElement)
An element that lazily builds children for a [SliverMultiBoxAdaptorWidget](flutter-docs://api/widgets/SliverMultiBoxAdaptorWidget).

[SliverMultiBoxAdaptorWidget](flutter-docs://api/widgets/SliverMultiBoxAdaptorWidget)
A base class for slivers that have multiple box children.

[SliverOffstage](flutter-docs://api/widgets/SliverOffstage)
A sliver that lays its sliver child out as if it was in the tree, but
without painting anything, without making the sliver child available for hit
testing, and without taking any room in the parent.

[SliverOpacity](flutter-docs://api/widgets/SliverOpacity)
A sliver widget that makes its sliver child partially transparent.

[SliverOverlapAbsorber](flutter-docs://api/widgets/SliverOverlapAbsorber)
A sliver that wraps another, forcing its layout extent to be treated as
overlap.

[SliverOverlapAbsorberHandle](flutter-docs://api/widgets/SliverOverlapAbsorberHandle)
Handle to provide to a [SliverOverlapAbsorber](flutter-docs://api/widgets/SliverOverlapAbsorber), a [SliverOverlapInjector](flutter-docs://api/widgets/SliverOverlapInjector),
and an [NestedScrollViewViewport](flutter-docs://api/widgets/NestedScrollViewViewport), to shift overlap in a [NestedScrollView](flutter-docs://api/widgets/NestedScrollView).

[SliverOverlapInjector](flutter-docs://api/widgets/SliverOverlapInjector)
A sliver that has a sliver geometry based on the values stored in a
[SliverOverlapAbsorberHandle](flutter-docs://api/widgets/SliverOverlapAbsorberHandle).

[SliverPadding](flutter-docs://api/widgets/SliverPadding)
A sliver that applies padding on each side of another sliver.

[SliverPersistentHeader](flutter-docs://api/widgets/SliverPersistentHeader)
A sliver whose size varies when the sliver is scrolled to the edge
of the viewport opposite the sliver's [GrowthDirection](flutter-docs://api/rendering/GrowthDirection).

[SliverPersistentHeaderDelegate](flutter-docs://api/widgets/SliverPersistentHeaderDelegate)
Delegate for configuring a [SliverPersistentHeader](flutter-docs://api/widgets/SliverPersistentHeader).

[SliverPrototypeExtentList](flutter-docs://api/widgets/SliverPrototypeExtentList)
A sliver that places its box children in a linear array and constrains them
to have the same extent as a prototype item along the main axis.

[SliverReorderableList](flutter-docs://api/widgets/SliverReorderableList)
A sliver list that allows the user to interactively reorder the list items.

[SliverReorderableListState](flutter-docs://api/widgets/SliverReorderableListState)
The state for a sliver list that allows the user to interactively reorder
the list items.

[SliverResizingHeader](flutter-docs://api/widgets/SliverResizingHeader)
A sliver that is pinned to the start of its [CustomScrollView](flutter-docs://api/widgets/CustomScrollView) and
reacts to scrolling by resizing between the intrinsic sizes of its
min and max extent prototypes.

[SliverSafeArea](flutter-docs://api/widgets/SliverSafeArea)
A sliver that insets another sliver by sufficient padding to avoid
intrusions by the operating system.

[SliverSemantics](flutter-docs://api/widgets/SliverSemantics)
A sliver that annotates its subtree with a description of the meaning of
the slivers.

[SliverToBoxAdapter](flutter-docs://api/widgets/SliverToBoxAdapter)
A sliver that contains a single box widget.

[SliverVariedExtentList](flutter-docs://api/widgets/SliverVariedExtentList)
A sliver that places its box children in a linear array and constrains them
to have the corresponding extent returned by [itemExtentBuilder](flutter-docs://api/widgets/SliverVariedExtentList/itemExtentBuilder).

[SliverVisibility](flutter-docs://api/widgets/SliverVisibility)
Whether to show or hide a sliver child.

[SliverWithKeepAliveWidget](flutter-docs://api/widgets/SliverWithKeepAliveWidget)
A base class for slivers that have [KeepAlive](flutter-docs://api/widgets/KeepAlive) children.

[SlottedMultiChildRenderObjectWidget](flutter-docs://api/widgets/SlottedMultiChildRenderObjectWidget)<SlotType, ChildType extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
A superclass for [RenderObjectWidget](flutter-docs://api/widgets/RenderObjectWidget) s that configure [RenderObject](flutter-docs://api/rendering/RenderObject) subclasses that organize their children in different slots.

[SlottedRenderObjectElement](flutter-docs://api/widgets/SlottedRenderObjectElement)<SlotType, ChildType extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
Element used by the [SlottedMultiChildRenderObjectWidget](flutter-docs://api/widgets/SlottedMultiChildRenderObjectWidget).

[SnackBar](flutter-docs://api/material/SnackBar)
A lightweight message with an optional action which briefly displays at the
bottom of the screen.

[SnackBarAction](flutter-docs://api/material/SnackBarAction)
A button for a [SnackBar](flutter-docs://api/material/SnackBar), known as an "action".

[SnackBarThemeData](flutter-docs://api/material/SnackBarThemeData)
Customizes default property values for [SnackBar](flutter-docs://api/material/SnackBar) widgets.

[SnapshotController](flutter-docs://api/widgets/SnapshotController)
A controller for the [SnapshotWidget](flutter-docs://api/widgets/SnapshotWidget) that controls when the child image is displayed
and when to regenerated the child image.

[SnapshotPainter](flutter-docs://api/widgets/SnapshotPainter)
A painter used to paint either a snapshot or the child widgets that
would be a snapshot.

[SnapshotWidget](flutter-docs://api/widgets/SnapshotWidget)
A widget that can replace its child with a snapshotted version of the child.

[Spacer](flutter-docs://api/widgets/Spacer)
Spacer creates an adjustable, empty spacer that can be used to tune the
spacing between widgets in a [Flex](flutter-docs://api/widgets/Flex) container, like [Row](flutter-docs://api/widgets/Row) or [Column](flutter-docs://api/widgets/Column).

[SpellCheckConfiguration](flutter-docs://api/widgets/SpellCheckConfiguration)
Controls how spell check is performed for text input.

[SpellCheckSuggestionsToolbar](flutter-docs://api/material/SpellCheckSuggestionsToolbar)
The default spell check suggestions toolbar for Android.

[SpellCheckSuggestionsToolbarLayoutDelegate](flutter-docs://api/material/SpellCheckSuggestionsToolbarLayoutDelegate)
Positions the toolbar below [anchor](flutter-docs://api/material/SpellCheckSuggestionsToolbarLayoutDelegate/anchor) or adjusts it higher to fit above
the bottom view insets, if applicable.

[Split](flutter-docs://api/animation/Split)
A curve that progresses according to [beginCurve](flutter-docs://api/animation/Split/beginCurve) until [split](flutter-docs://api/animation/Split/split), then
according to [endCurve](flutter-docs://api/animation/Split/endCurve).

[SpringDescription](flutter-docs://api/physics/SpringDescription)
Structure that describes a spring's constants.

[Stack](flutter-docs://api/widgets/Stack)
A widget that positions its children relative to the edges of its box.

[StadiumBorder](flutter-docs://api/painting/StadiumBorder)
A border that fits a stadium-shaped border (a box with semicircles on the ends)
within the rectangle of the widget it is applied to.

[StandardFabLocation](flutter-docs://api/material/StandardFabLocation)
A base class that simplifies building [FloatingActionButtonLocation](flutter-docs://api/material/FloatingActionButtonLocation) s when
used with mixins [FabTopOffsetY](flutter-docs://api/material/FabTopOffsetY), [FabFloatOffsetY](flutter-docs://api/material/FabFloatOffsetY), [FabDockedOffsetY](flutter-docs://api/material/FabDockedOffsetY),
[FabStartOffsetX](flutter-docs://api/material/FabStartOffsetX), [FabCenterOffsetX](flutter-docs://api/material/FabCenterOffsetX), [FabEndOffsetX](flutter-docs://api/material/FabEndOffsetX), and [FabMiniOffsetAdjustment](flutter-docs://api/material/FabMiniOffsetAdjustment).

[StarBorder](flutter-docs://api/painting/StarBorder)
A border that fits a star or polygon-shaped border within the rectangle of
the widget it is applied to.

[State](flutter-docs://api/widgets/State)<T extends [StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>
The logic and internal state for a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget).

[StatefulBuilder](flutter-docs://api/widgets/StatefulBuilder)
A platonic widget that both has state and calls a closure to obtain its child widget.

[StatefulElement](flutter-docs://api/widgets/StatefulElement)
An [Element](flutter-docs://api/widgets/Element) that uses a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) as its configuration.

[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)
A widget that has mutable state.

[StatelessElement](flutter-docs://api/widgets/StatelessElement)
An [Element](flutter-docs://api/widgets/Element) that uses a [StatelessWidget](flutter-docs://api/widgets/StatelessWidget) as its configuration.

[StatelessWidget](flutter-docs://api/widgets/StatelessWidget)
A widget that does not require mutable state.

[StaticSelectionContainerDelegate](flutter-docs://api/widgets/StaticSelectionContainerDelegate)
A delegate that manages updating multiple [Selectable](flutter-docs://api/rendering/Selectable) children where the
[Selectable](flutter-docs://api/rendering/Selectable) s do not change or move around frequently.

[StatusTransitionWidget](flutter-docs://api/widgets/StatusTransitionWidget)
A widget that rebuilds when the given animation changes status.

[Step](flutter-docs://api/material/Step)
A material step used in [Stepper](flutter-docs://api/material/Stepper). The step can have a title and subtitle,
an icon within its circle, some content and a state that governs its
styling.

[Stepper](flutter-docs://api/material/Stepper)
A material stepper widget that displays progress through a sequence of
steps. Steppers are particularly useful in the case of forms where one step
requires the completion of another one, or where multiple steps need to be
completed in order to submit the whole form.

[StepStyle](flutter-docs://api/material/StepStyle)
This class is used to override the default visual properties of [Step](flutter-docs://api/material/Step) widgets within a [Stepper](flutter-docs://api/material/Stepper).

[StepTween](flutter-docs://api/animation/StepTween)
An interpolation between two integers that floors.

[StreamBuilder](flutter-docs://api/widgets/StreamBuilder)<T>
Widget that builds itself based on the latest snapshot of interaction with
a [Stream](flutter-docs://api/dart-async/Stream).

[StreamBuilderBase](flutter-docs://api/widgets/StreamBuilderBase)<T, S>
Base class for widgets that build themselves based on interaction with
a specified [Stream](flutter-docs://api/dart-async/Stream).

[StretchEffect](flutter-docs://api/widgets/StretchEffect)
A widget that applies a stretching visual effect to its child.

[StretchingOverscrollIndicator](flutter-docs://api/widgets/StretchingOverscrollIndicator)
A Material Design visual indication that a scroll view has overscrolled.

[StrutStyle](flutter-docs://api/painting/StrutStyle)
Defines the strut, which sets the minimum height a line can be
relative to the baseline.

[SubmenuButton](flutter-docs://api/material/SubmenuButton)
A menu button that displays a cascading menu.

[SweepGradient](flutter-docs://api/painting/SweepGradient)
A 2D sweep gradient.

[Switch](flutter-docs://api/material/Switch)
A Material Design switch.

[SwitchListTile](flutter-docs://api/material/SwitchListTile)
A [ListTile](flutter-docs://api/material/ListTile) with a [Switch](flutter-docs://api/material/Switch). In other words, a switch with a label.

[SwitchTheme](flutter-docs://api/material/SwitchTheme)
Applies a switch theme to descendant [Switch](flutter-docs://api/material/Switch) widgets.

[SwitchThemeData](flutter-docs://api/material/SwitchThemeData)
Defines default property values for descendant [Switch](flutter-docs://api/material/Switch) widgets.

[SystemContextMenu](flutter-docs://api/widgets/SystemContextMenu)
Displays the system context menu on top of the Flutter view.

[SystemMouseCursors](flutter-docs://api/services/SystemMouseCursors)
A collection of system [MouseCursor](flutter-docs://api/services/MouseCursor) s.

[SystemTextScaler](flutter-docs://api/widgets/SystemTextScaler)
A [TextScaler](flutter-docs://api/painting/TextScaler) that reflects the user's font scale preferences from the
platform's accessibility settings.

[Tab](flutter-docs://api/material/Tab)
A Material Design [TabBar](flutter-docs://api/material/TabBar) tab.

[TabBar](flutter-docs://api/material/TabBar)
A Material Design primary tab bar.

[TabBarTheme](flutter-docs://api/material/TabBarTheme)
Defines a theme for [TabBar](flutter-docs://api/material/TabBar) widgets.

[TabBarThemeData](flutter-docs://api/material/TabBarThemeData)
Defines default property values for descendant [TabBar](flutter-docs://api/material/TabBar) widgets.

[TabBarView](flutter-docs://api/material/TabBarView)
A page view that displays the widget which corresponds to the currently
selected tab.

[TabController](flutter-docs://api/material/TabController)
Coordinates tab selection between a [TabBar](flutter-docs://api/material/TabBar) and a [TabBarView](flutter-docs://api/material/TabBarView).

[Table](flutter-docs://api/widgets/Table)
A widget that uses the table layout algorithm for its children.

[TableBorder](flutter-docs://api/rendering/TableBorder)
Border specification for [Table](flutter-docs://api/widgets/Table) widgets.

[TableCell](flutter-docs://api/widgets/TableCell)
A widget that controls how a child of a [Table](flutter-docs://api/widgets/Table) is aligned.

[TableColumnWidth](flutter-docs://api/rendering/TableColumnWidth)
Base class to describe how wide a column in a [RenderTable](flutter-docs://api/rendering/RenderTable) should be.

[TableRow](flutter-docs://api/widgets/TableRow)
A horizontal group of cells in a [Table](flutter-docs://api/widgets/Table).

[TableRowInkWell](flutter-docs://api/material/TableRowInkWell)
A rectangular area of a Material that responds to touch but clips
its ink splashes to the current table row of the nearest table.

[TabPageSelector](flutter-docs://api/material/TabPageSelector)
Uses [TabPageSelectorIndicator](flutter-docs://api/material/TabPageSelectorIndicator) to display a row of small circular
indicators, one per tab.

[TabPageSelectorIndicator](flutter-docs://api/material/TabPageSelectorIndicator)
Displays a single circle with the specified size, border style, border color
and background colors.

[TapDownDetails](flutter-docs://api/gestures/TapDownDetails)
Details for [GestureTapDownCallback](flutter-docs://api/gestures/GestureTapDownCallback), such as position.

[TappableChipAttributes](flutter-docs://api/material/TappableChipAttributes)
An interface for Material Design chips that can be tapped.

[TapRegion](flutter-docs://api/widgets/TapRegion)
A widget that defines a region that can detect taps inside or outside of
itself and any group of regions it belongs to, without participating in the
[gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system
(other than to consume tap down events if [consumeOutsideTaps](flutter-docs://api/widgets/TapRegion/consumeOutsideTaps) is true).

[TapRegionRegistry](flutter-docs://api/widgets/TapRegionRegistry)
An interface for registering and unregistering a [RenderTapRegion](flutter-docs://api/widgets/RenderTapRegion) (typically created with a [TapRegion](flutter-docs://api/widgets/TapRegion) widget) with a
[RenderTapRegionSurface](flutter-docs://api/widgets/RenderTapRegionSurface) (typically created with a [TapRegionSurface](flutter-docs://api/widgets/TapRegionSurface) widget).

[TapRegionSurface](flutter-docs://api/widgets/TapRegionSurface)
A widget that provides notification of a tap inside or outside of a set of
registered regions, without participating in the [gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system.

[TapUpDetails](flutter-docs://api/gestures/TapUpDetails)
Details for [GestureTapUpCallback](flutter-docs://api/gestures/GestureTapUpCallback), such as position.

[Text](flutter-docs://api/widgets/Text)
A run of text with a single style.

[TextAlignVertical](flutter-docs://api/painting/TextAlignVertical)
The vertical alignment of text within an input box.

[TextBox](flutter-docs://api/dart-ui/TextBox)
A rectangle enclosing a run of text.

[TextButton](flutter-docs://api/material/TextButton)
A Material Design "Text Button".

[TextButtonTheme](flutter-docs://api/material/TextButtonTheme)
Overrides the default [ButtonStyle](flutter-docs://api/material/ButtonStyle) of its [TextButton](flutter-docs://api/material/TextButton) descendants.

[TextButtonThemeData](flutter-docs://api/material/TextButtonThemeData)
A [ButtonStyle](flutter-docs://api/material/ButtonStyle) that overrides the default appearance of
[TextButton](flutter-docs://api/material/TextButton) s when it's used with [TextButtonTheme](flutter-docs://api/material/TextButtonTheme) or with the
overall [Theme](flutter-docs://api/material/Theme)'s [ThemeData.textButtonTheme](flutter-docs://api/material/ThemeData/textButtonTheme).

[TextDecoration](flutter-docs://api/dart-ui/TextDecoration)
A linear decoration to draw near the text.

[TextEditingController](flutter-docs://api/widgets/TextEditingController)
A controller for an editable text field.

[TextEditingValue](flutter-docs://api/flutter_test/TextEditingValue)
The current text, selection, and composing state for editing a run of text.

[TextField](flutter-docs://api/material/TextField)
A Material Design text field.

[TextFieldTapRegion](flutter-docs://api/widgets/TextFieldTapRegion)
A [TapRegion](flutter-docs://api/widgets/TapRegion) that adds its children to the tap region group for widgets
based on the [EditableText](flutter-docs://api/widgets/EditableText) text editing widget, such as [TextField](flutter-docs://api/material/TextField) and
[CupertinoTextField](flutter-docs://api/cupertino/CupertinoTextField).

[TextFormField](flutter-docs://api/material/TextFormField)
A [FormField](flutter-docs://api/widgets/FormField) that contains a [TextField](flutter-docs://api/material/TextField).

[TextHeightBehavior](flutter-docs://api/dart-ui/TextHeightBehavior)
Defines how to apply `TextStyle.height` over and under text.

[TextInputType](flutter-docs://api/services/TextInputType)
The type of information for which to optimize the text input control.

[TextMagnifier](flutter-docs://api/material/TextMagnifier)
A [Magnifier](flutter-docs://api/material/Magnifier) positioned by rules dictated by the native Android magnifier.

[TextMagnifierConfiguration](flutter-docs://api/widgets/TextMagnifierConfiguration)
A configuration object for a magnifier (e.g. in a text field).

[TextPainter](flutter-docs://api/painting/TextPainter)
An object that paints a [TextSpan](flutter-docs://api/painting/TextSpan) tree into a [Canvas](flutter-docs://api/dart-ui/Canvas).

[TextPosition](flutter-docs://api/dart-ui/TextPosition)
A position in a string of text.

[TextRange](flutter-docs://api/dart-ui/TextRange)
A range of characters in a string of text.

[TextScaler](flutter-docs://api/painting/TextScaler)
A class that describes how textual contents should be scaled for better
readability.

[TextSelection](flutter-docs://api/services/TextSelection)
A range of text that represents a selection.

[TextSelectionControls](flutter-docs://api/widgets/TextSelectionControls)
An interface for building the selection UI, to be provided by the
implementer of the toolbar widget.

[TextSelectionGestureDetector](flutter-docs://api/widgets/TextSelectionGestureDetector)
A gesture detector to respond to non-exclusive event chains for a text field.

[TextSelectionGestureDetectorBuilder](flutter-docs://api/widgets/TextSelectionGestureDetectorBuilder)
Builds a [TextSelectionGestureDetector](flutter-docs://api/widgets/TextSelectionGestureDetector) to wrap an [EditableText](flutter-docs://api/widgets/EditableText).

[TextSelectionGestureDetectorBuilderDelegate](flutter-docs://api/widgets/TextSelectionGestureDetectorBuilderDelegate)
Delegate interface for the [TextSelectionGestureDetectorBuilder](flutter-docs://api/widgets/TextSelectionGestureDetectorBuilder).

[TextSelectionOverlay](flutter-docs://api/widgets/TextSelectionOverlay)
An object that manages a pair of text selection handles for a
[RenderEditable](flutter-docs://api/rendering/RenderEditable).

[TextSelectionPoint](flutter-docs://api/rendering/TextSelectionPoint)
Represents the coordinates of the point in a selection, and the text
direction at that point, relative to top left of the [RenderEditable](flutter-docs://api/rendering/RenderEditable) that
holds the selection.

[TextSelectionTheme](flutter-docs://api/material/TextSelectionTheme)
An inherited widget that defines the appearance of text selection in
this widget's subtree.

[TextSelectionThemeData](flutter-docs://api/material/TextSelectionThemeData)
Defines the visual properties needed for text selection in [TextField](flutter-docs://api/material/TextField) and
[SelectableText](flutter-docs://api/material/SelectableText) widgets.

[TextSelectionToolbar](flutter-docs://api/material/TextSelectionToolbar)
A fully-functional Material-style text selection toolbar.

[TextSelectionToolbarAnchors](flutter-docs://api/widgets/TextSelectionToolbarAnchors)
The position information for a text selection toolbar.

[TextSelectionToolbarLayoutDelegate](flutter-docs://api/widgets/TextSelectionToolbarLayoutDelegate)
A [SingleChildLayoutDelegate](flutter-docs://api/rendering/SingleChildLayoutDelegate) for use with [CustomSingleChildLayout](flutter-docs://api/widgets/CustomSingleChildLayout) that
positions its child above [anchorAbove](flutter-docs://api/widgets/TextSelectionToolbarLayoutDelegate/anchorAbove) if it fits, or otherwise below
[anchorBelow](flutter-docs://api/widgets/TextSelectionToolbarLayoutDelegate/anchorBelow).

[TextSelectionToolbarTextButton](flutter-docs://api/material/TextSelectionToolbarTextButton)
A button styled like a Material native Android text selection menu button.

[TextSpan](flutter-docs://api/painting/TextSpan)
An immutable span of text.

[TextStyle](flutter-docs://api/painting/TextStyle)
An immutable style describing how to format and paint text.

[TextStyleTween](flutter-docs://api/widgets/TextStyleTween)
An interpolation between two [TextStyle](flutter-docs://api/painting/TextStyle) s.

[TextTheme](flutter-docs://api/material/TextTheme)
Material design text theme.

[Texture](flutter-docs://api/widgets/Texture)
A rectangle upon which a backend texture is mapped.

[Theme](flutter-docs://api/material/Theme)
Applies a theme to descendant widgets.

[ThemeData](flutter-docs://api/material/ThemeData)
Defines the configuration of the overall visual [Theme](flutter-docs://api/material/Theme) for a [MaterialApp](flutter-docs://api/material/MaterialApp) or a widget subtree within the app.

[ThemeDataTween](flutter-docs://api/material/ThemeDataTween)
An interpolation between two [ThemeData](flutter-docs://api/material/ThemeData) s.

[ThemeExtension](flutter-docs://api/material/ThemeExtension)<T extends [ThemeExtension](flutter-docs://api/material/ThemeExtension)<T>>
An interface that defines custom additions to a [ThemeData](flutter-docs://api/material/ThemeData) object.

[ThreePointCubic](flutter-docs://api/animation/ThreePointCubic)
A cubic polynomial composed of two curves that share a common center point.

[Threshold](flutter-docs://api/animation/Threshold)
A curve that is 0.0 until it hits the threshold, then it jumps to 1.0.

[TickerFuture](flutter-docs://api/scheduler/TickerFuture)
An object representing an ongoing [Ticker](flutter-docs://api/scheduler/Ticker) sequence.

[TickerMode](flutter-docs://api/widgets/TickerMode)
Enables or disables tickers (and thus animation controllers) in the widget
subtree.

[TickerProvider](flutter-docs://api/scheduler/TickerProvider)
An interface implemented by classes that can vend [Ticker](flutter-docs://api/scheduler/Ticker) objects.

[TimeOfDay](flutter-docs://api/material/TimeOfDay)
A value representing a time during the day, independent of the date that
day might fall on or the time zone.

[TimePickerDialog](flutter-docs://api/material/TimePickerDialog)
A Material Design time picker designed to appear inside a popup dialog.

[TimePickerTheme](flutter-docs://api/material/TimePickerTheme)
An inherited widget that defines the configuration for time pickers
displayed using [showTimePicker](flutter-docs://api/material/showTimePicker) in this widget's subtree.

[TimePickerThemeData](flutter-docs://api/material/TimePickerThemeData)
Defines the visual properties of the widget displayed with [showTimePicker](flutter-docs://api/material/showTimePicker).

[Title](flutter-docs://api/widgets/Title)
A widget that describes this app in the operating system.

[ToggleablePainter](flutter-docs://api/widgets/ToggleablePainter)
A base class for a [CustomPainter](flutter-docs://api/rendering/CustomPainter) that may be passed to
[ToggleableStateMixin.buildToggleable](flutter-docs://api/widgets/ToggleableStateMixin/buildToggleable) to draw the visual representation of
a Toggleable.

[ToggleButtons](flutter-docs://api/material/ToggleButtons)
A set of toggle buttons.

[ToggleButtonsTheme](flutter-docs://api/material/ToggleButtonsTheme)
An inherited widget that defines color and border parameters for
[ToggleButtons](flutter-docs://api/material/ToggleButtons) in this widget's subtree.

[ToggleButtonsThemeData](flutter-docs://api/material/ToggleButtonsThemeData)
Defines the color and border properties of [ToggleButtons](flutter-docs://api/material/ToggleButtons) widgets.

[Tolerance](flutter-docs://api/physics/Tolerance)
Structure that specifies maximum allowable magnitudes for distances,
durations, and velocity differences to be considered equal.

[ToolbarItemsParentData](flutter-docs://api/widgets/ToolbarItemsParentData)
ParentData that determines whether or not to paint the corresponding child.

[ToolbarOptions](flutter-docs://api/widgets/ToolbarOptions)
Toolbar configuration for [EditableText](flutter-docs://api/widgets/EditableText).

[Tooltip](flutter-docs://api/material/Tooltip)
A Material Design tooltip.

[TooltipState](flutter-docs://api/material/TooltipState)
Contains the state for a [Tooltip](flutter-docs://api/material/Tooltip).

[TooltipTheme](flutter-docs://api/material/TooltipTheme)
Applies a tooltip theme to descendant [Tooltip](flutter-docs://api/material/Tooltip) widgets.

[TooltipThemeData](flutter-docs://api/material/TooltipThemeData)
Defines the visual properties of [Tooltip](flutter-docs://api/material/Tooltip) widgets, a tooltip theme.

[TooltipVisibility](flutter-docs://api/material/TooltipVisibility)
Overrides the visibility of descendant [Tooltip](flutter-docs://api/material/Tooltip) widgets.

[TrackingScrollController](flutter-docs://api/widgets/TrackingScrollController)
A [ScrollController](flutter-docs://api/widgets/ScrollController) whose [initialScrollOffset](flutter-docs://api/widgets/TrackingScrollController/initialScrollOffset) tracks its most recently
updated [ScrollPosition](flutter-docs://api/widgets/ScrollPosition).

[TrainHoppingAnimation](flutter-docs://api/animation/TrainHoppingAnimation)
This animation starts by proxying one animation, but when the value of that
animation crosses the value of the second (either because the second is
going in the opposite direction, or because the one overtakes the other),
the animation hops over to proxying the second animation.

[Transform](flutter-docs://api/widgets/Transform)
A widget that applies a transformation before painting its child.

[TransformationController](flutter-docs://api/widgets/TransformationController)
A thin wrapper on [ValueNotifier](flutter-docs://api/foundation/ValueNotifier) whose value is a [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4) representing a
transformation.

[TransformProperty](flutter-docs://api/painting/TransformProperty)
Property which handles [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4) that represent transforms.

[TransitionDelegate](flutter-docs://api/widgets/TransitionDelegate)<T>
The delegate that decides how pages added and removed from [Navigator.pages](flutter-docs://api/widgets/Navigator/pages) transition in or out of the screen.

[TransitionRoute](flutter-docs://api/widgets/TransitionRoute)<T>
A route with entrance and exit transitions.

[TransposeCharactersIntent](flutter-docs://api/widgets/TransposeCharactersIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a user interaction that attempts to swap the
characters immediately around the cursor.

[TreeSliver](flutter-docs://api/widgets/TreeSliver)<T>
A widget that displays [TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode) s that expand and collapse in a
vertically and horizontally scrolling [Viewport](flutter-docs://api/widgets/Viewport).

[TreeSliverController](flutter-docs://api/widgets/TreeSliverController)
Enables control over the [TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode) s of a [TreeSliver](flutter-docs://api/widgets/TreeSliver).

[TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode)<T>
A data structure for configuring children of a [TreeSliver](flutter-docs://api/widgets/TreeSliver).

[Tween](flutter-docs://api/animation/Tween)<T extends [Object](flutter-docs://api/dart-core/Object)?>
A linear interpolation between a beginning and ending value.

[TweenAnimationBuilder](flutter-docs://api/widgets/TweenAnimationBuilder)<T extends [Object](flutter-docs://api/dart-core/Object)?>
[Widget](flutter-docs://api/widgets/Widget) builder that animates a property of a [Widget](flutter-docs://api/widgets/Widget) to a target value
whenever the target value changes.

[TweenSequence](flutter-docs://api/animation/TweenSequence)<T>
Enables creating an [Animation](flutter-docs://api/animation/Animation) whose value is defined by a sequence of
[Tween](flutter-docs://api/animation/Tween) s.

[TweenSequenceItem](flutter-docs://api/animation/TweenSequenceItem)<T>
A simple holder for one element of a [TweenSequence](flutter-docs://api/animation/TweenSequence).

[TwoDimensionalChildBuilderDelegate](flutter-docs://api/widgets/TwoDimensionalChildBuilderDelegate)
A delegate that supplies children for a [TwoDimensionalScrollView](flutter-docs://api/widgets/TwoDimensionalScrollView) using a
builder callback.

[TwoDimensionalChildDelegate](flutter-docs://api/widgets/TwoDimensionalChildDelegate)
A delegate that supplies children for scrolling in two dimensions.

[TwoDimensionalChildListDelegate](flutter-docs://api/widgets/TwoDimensionalChildListDelegate)
A delegate that supplies children for a [TwoDimensionalViewport](flutter-docs://api/widgets/TwoDimensionalViewport) using an
explicit two dimensional array.

[TwoDimensionalChildManager](flutter-docs://api/widgets/TwoDimensionalChildManager)
A delegate used by [RenderTwoDimensionalViewport](flutter-docs://api/widgets/RenderTwoDimensionalViewport) to manage its children.

[TwoDimensionalScrollable](flutter-docs://api/widgets/TwoDimensionalScrollable)
A widget that manages scrolling in both the vertical and horizontal
dimensions and informs the [TwoDimensionalViewport](flutter-docs://api/widgets/TwoDimensionalViewport) through which the
content is viewed.

[TwoDimensionalScrollableState](flutter-docs://api/widgets/TwoDimensionalScrollableState)
State object for a [TwoDimensionalScrollable](flutter-docs://api/widgets/TwoDimensionalScrollable) widget.

[TwoDimensionalScrollView](flutter-docs://api/widgets/TwoDimensionalScrollView)
A widget that combines a [TwoDimensionalScrollable](flutter-docs://api/widgets/TwoDimensionalScrollable) and a
[TwoDimensionalViewport](flutter-docs://api/widgets/TwoDimensionalViewport) to create an interactive scrolling pane of content
in both vertical and horizontal dimensions.

[TwoDimensionalViewport](flutter-docs://api/widgets/TwoDimensionalViewport)
A widget through which a portion of larger content can be viewed, typically
in combination with a [TwoDimensionalScrollable](flutter-docs://api/widgets/TwoDimensionalScrollable).

[TwoDimensionalViewportParentData](flutter-docs://api/widgets/TwoDimensionalViewportParentData)
Parent data structure used by [RenderTwoDimensionalViewport](flutter-docs://api/widgets/RenderTwoDimensionalViewport).

[Typography](flutter-docs://api/material/Typography)
The color and geometry [TextTheme](flutter-docs://api/material/TextTheme) s for Material apps.

[UiKitView](flutter-docs://api/widgets/UiKitView)
Embeds an iOS view in the Widget hierarchy.

[UnconstrainedBox](flutter-docs://api/widgets/UnconstrainedBox)
A widget that imposes no constraints on its child, allowing it to render
at its "natural" size.

[UnderlineInputBorder](flutter-docs://api/material/UnderlineInputBorder)
Draws a horizontal line at the bottom of an [InputDecorator](flutter-docs://api/material/InputDecorator)'s container and
defines the container's shape.

[UnderlineTabIndicator](flutter-docs://api/material/UnderlineTabIndicator)
Used with [TabBar.indicator](flutter-docs://api/material/TabBar/indicator) to draw a horizontal line below the
selected tab.

[UndoHistory](flutter-docs://api/widgets/UndoHistory)<T>
Provides undo/redo capabilities for a [ValueNotifier](flutter-docs://api/foundation/ValueNotifier).

[UndoHistoryController](flutter-docs://api/widgets/UndoHistoryController)
A controller for the undo history, for example for an editable text field.

[UndoHistoryState](flutter-docs://api/widgets/UndoHistoryState)<T>
State for a [UndoHistory](flutter-docs://api/widgets/UndoHistory).

[UndoHistoryValue](flutter-docs://api/widgets/UndoHistoryValue)
Represents whether the current undo stack can undo or redo.

[UndoTextIntent](flutter-docs://api/widgets/UndoTextIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a user interaction that attempts to go back to
the previous editing state.

[UniqueKey](flutter-docs://api/foundation/UniqueKey)
A key that is only equal to itself.

[UniqueWidget](flutter-docs://api/widgets/UniqueWidget)<T extends [State](flutter-docs://api/widgets/State)<[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>>
Base class for stateful widgets that have exactly one inflated instance in
the tree.

[UnmanagedRestorationScope](flutter-docs://api/widgets/UnmanagedRestorationScope)
Inserts a provided [RestorationBucket](flutter-docs://api/services/RestorationBucket) into the widget tree and makes it
available to descendants via [RestorationScope.of](flutter-docs://api/widgets/RestorationScope/of).

[UpdateSelectionIntent](flutter-docs://api/widgets/UpdateSelectionIntent)
An [Intent](flutter-docs://api/widgets/Intent) that represents a user interaction that attempts to change the
selection in an input field.

[UserAccountsDrawerHeader](flutter-docs://api/material/UserAccountsDrawerHeader)
A Material Design [Drawer](flutter-docs://api/material/Drawer) header that identifies the app's user.

[UserScrollNotification](flutter-docs://api/widgets/UserScrollNotification)
A notification that the user has changed the [ScrollDirection](flutter-docs://api/rendering/ScrollDirection) in which they
are scrolling, or have stopped scrolling.

[ValueKey](flutter-docs://api/foundation/ValueKey)<T>
A key that uses a value of a particular type to identify itself.

[ValueListenableBuilder](flutter-docs://api/widgets/ValueListenableBuilder)<T>
A widget whose content stays synced with a [ValueListenable](flutter-docs://api/foundation/ValueListenable).

[ValueNotifier](flutter-docs://api/foundation/ValueNotifier)<T>
A [ChangeNotifier](flutter-docs://api/foundation/ChangeNotifier) that holds a single value.

[Velocity](flutter-docs://api/gestures/Velocity)
A velocity in two dimensions.

[VerticalDivider](flutter-docs://api/material/VerticalDivider)
A thin vertical line, with padding on either side.

[View](flutter-docs://api/widgets/View)
Bootstraps a render tree that is rendered into the provided [FlutterView](flutter-docs://api/dart-ui/FlutterView).

[ViewAnchor](flutter-docs://api/widgets/ViewAnchor)
Decorates a [child](flutter-docs://api/widgets/ViewAnchor/child) widget with a side [View](flutter-docs://api/widgets/View).

[ViewCollection](flutter-docs://api/widgets/ViewCollection)
A collection of sibling [View](flutter-docs://api/widgets/View) s.

[Viewport](flutter-docs://api/widgets/Viewport)
A widget through which a portion of larger content can be viewed, typically
in combination with a [Scrollable](flutter-docs://api/widgets/Scrollable).

[Visibility](flutter-docs://api/widgets/Visibility)
Whether to show or hide a child.

[VisualDensity](flutter-docs://api/material/VisualDensity)
Defines the visual density of user interface components.

[VoidCallbackAction](flutter-docs://api/widgets/VoidCallbackAction)
An [Action](flutter-docs://api/widgets/Action) that invokes the [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) given to it in the
[VoidCallbackIntent](flutter-docs://api/widgets/VoidCallbackIntent) passed to it when invoked.

[VoidCallbackIntent](flutter-docs://api/widgets/VoidCallbackIntent)
An [Intent](flutter-docs://api/widgets/Intent) that keeps a [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) to be invoked by a
[VoidCallbackAction](flutter-docs://api/widgets/VoidCallbackAction) when it receives this intent.

[WeakMap](flutter-docs://api/widgets/WeakMap)<K, V>
Does not hold keys from garbage collection.

[Widget](flutter-docs://api/widgets/Widget)
Describes the configuration for an [Element](flutter-docs://api/widgets/Element).

[WidgetInspector](flutter-docs://api/widgets/WidgetInspector)
A widget that enables inspecting the child widget's structure.

[WidgetOrderTraversalPolicy](flutter-docs://api/widgets/WidgetOrderTraversalPolicy)
A [FocusTraversalPolicy](flutter-docs://api/widgets/FocusTraversalPolicy) that traverses the focus order in widget hierarchy
order.

[WidgetsApp](flutter-docs://api/widgets/WidgetsApp)
A convenience widget that wraps a number of widgets that are commonly
required for an application.

[WidgetsBindingObserver](flutter-docs://api/widgets/WidgetsBindingObserver)
Interface for classes that register with the Widgets layer binding.

[WidgetsFlutterBinding](flutter-docs://api/widgets/WidgetsFlutterBinding)
A concrete binding for applications based on the Widgets framework.

[WidgetsLocalizations](flutter-docs://api/widgets/WidgetsLocalizations)
Interface for localized resource values for the lowest levels of the Flutter
framework.

[WidgetSpan](flutter-docs://api/widgets/WidgetSpan)
An immutable widget that is embedded inline within text.

[WidgetStateBorderSide](flutter-docs://api/widgets/WidgetStateBorderSide)
Defines a [BorderSide](flutter-docs://api/painting/BorderSide) whose value depends on a set of [WidgetState](flutter-docs://api/widgets/WidgetState) s
which represent the interactive state of a component.

[WidgetStateColor](flutter-docs://api/widgets/WidgetStateColor)
Defines a [Color](flutter-docs://api/dart-ui/Color) that is also a [WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty).

[WidgetStateInputBorder](flutter-docs://api/material/WidgetStateInputBorder)
Defines an [InputBorder](flutter-docs://api/material/InputBorder) that is also a [WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty).

[WidgetStateMapper](flutter-docs://api/widgets/WidgetStateMapper)<T>
Uses a [WidgetStateMap](flutter-docs://api/widgets/WidgetStateMap) to resolve to a single value of type `T` based on
the current set of Widget states.

[WidgetStateMouseCursor](flutter-docs://api/widgets/WidgetStateMouseCursor)
Defines a [MouseCursor](flutter-docs://api/services/MouseCursor) whose value depends on a set of [WidgetState](flutter-docs://api/widgets/WidgetState) s which
represent the interactive state of a component.

[WidgetStateOutlinedBorder](flutter-docs://api/widgets/WidgetStateOutlinedBorder)
Defines an [OutlinedBorder](flutter-docs://api/painting/OutlinedBorder) whose value depends on a set of [WidgetState](flutter-docs://api/widgets/WidgetState) s
which represent the interactive state of a component.

[WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty)<T>
Interface for classes that [resolve](flutter-docs://api/widgets/WidgetStateProperty/resolve) to a value of type `T` based
on a widget's interactive "state", which is defined as a set
of [WidgetState](flutter-docs://api/widgets/WidgetState) s.

[WidgetStatePropertyAll](flutter-docs://api/widgets/WidgetStatePropertyAll)<T>
Convenience class for creating a [WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty) that
resolves to the given value for all states.

[WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint)
This class allows [WidgetState](flutter-docs://api/widgets/WidgetState) enum values to be combined
using [WidgetStateOperators](flutter-docs://api/widgets/WidgetStateOperators).

[WidgetStatesController](flutter-docs://api/widgets/WidgetStatesController)
Manages a set of [WidgetState](flutter-docs://api/widgets/WidgetState) s and notifies listeners of changes.

[WidgetStateTextStyle](flutter-docs://api/widgets/WidgetStateTextStyle)
Defines a [TextStyle](flutter-docs://api/painting/TextStyle) that is also a [WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty).

[WidgetToRenderBoxAdapter](flutter-docs://api/widgets/WidgetToRenderBoxAdapter)
An adapter for placing a specific [RenderBox](flutter-docs://api/rendering/RenderBox) in the widget tree.

[WillPopScope](flutter-docs://api/widgets/WillPopScope)
Registers a callback to veto attempts by the user to dismiss the enclosing
[ModalRoute](flutter-docs://api/widgets/ModalRoute).

[WordBoundary](flutter-docs://api/painting/WordBoundary)
A [TextBoundary](flutter-docs://api/services/TextBoundary) subclass for locating word breaks.

[Wrap](flutter-docs://api/widgets/Wrap)
A widget that displays its children in multiple horizontal or vertical runs.

[YearPicker](flutter-docs://api/material/YearPicker)
A scrollable grid of years to allow picking a year.

[ZoomPageTransitionsBuilder](flutter-docs://api/material/ZoomPageTransitionsBuilder)
Used by [PageTransitionsTheme](flutter-docs://api/material/PageTransitionsTheme) to define a zooming [MaterialPageRoute](flutter-docs://api/material/MaterialPageRoute) page
transition animation that looks like the default page transition used on
Android Q.

## Enums

[AndroidOverscrollIndicator](flutter-docs://api/widgets/AndroidOverscrollIndicator)
Types of overscroll indicators supported by [TargetPlatform.android](flutter-docs://api/foundation/TargetPlatform).

[AnimationBehavior](flutter-docs://api/animation/AnimationBehavior)
Configures how an [AnimationController](flutter-docs://api/animation/AnimationController) behaves when animations are
disabled.

[AnimationStatus](flutter-docs://api/animation/AnimationStatus)
The status of an animation.

[AppLifecycleState](flutter-docs://api/dart-ui/AppLifecycleState)
States that an application can be in once it is running.

[AutofillContextAction](flutter-docs://api/widgets/AutofillContextAction)
Predefined autofill context clean up actions.

[AutovalidateMode](flutter-docs://api/widgets/AutovalidateMode)
Used to configure the auto validation of [FormField](flutter-docs://api/widgets/FormField) and [Form](flutter-docs://api/widgets/Form) widgets.

[Axis](flutter-docs://api/painting/Axis)
The two cardinal directions in two dimensions.

[AxisDirection](flutter-docs://api/painting/AxisDirection)
A direction along either the horizontal or vertical [Axis](flutter-docs://api/painting/Axis) in which the
origin, or zero position, is determined.

[BannerLocation](flutter-docs://api/widgets/BannerLocation)
Where to show a [Banner](flutter-docs://api/widgets/Banner).

[BlendMode](flutter-docs://api/dart-ui/BlendMode)
Algorithms to use when painting on the canvas.

[BlurStyle](flutter-docs://api/dart-ui/BlurStyle)
Styles to use for blurs in [MaskFilter](flutter-docs://api/dart-ui/MaskFilter) objects.

[BorderStyle](flutter-docs://api/painting/BorderStyle)
The style of line to draw for a [BorderSide](flutter-docs://api/painting/BorderSide) in a [Border](flutter-docs://api/painting/Border).

[BottomNavigationBarLandscapeLayout](flutter-docs://api/material/BottomNavigationBarLandscapeLayout)
Refines the layout of a [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar) when the enclosing
[MediaQueryData.orientation](flutter-docs://api/widgets/MediaQueryData/orientation) is [Orientation.landscape](flutter-docs://api/widgets/Orientation).

[BottomNavigationBarType](flutter-docs://api/material/BottomNavigationBarType)
Defines the layout and behavior of a [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar).

[BoxFit](flutter-docs://api/painting/BoxFit)
How a box should be inscribed into another box.

[BoxShape](flutter-docs://api/painting/BoxShape)
The shape to use when rendering a [Border](flutter-docs://api/painting/Border) or [BoxDecoration](flutter-docs://api/painting/BoxDecoration).

[Brightness](flutter-docs://api/dart-ui/Brightness)
Describes the contrast of a theme or color palette.

[ButtonBarLayoutBehavior](flutter-docs://api/material/ButtonBarLayoutBehavior)
Used with [ButtonTheme](flutter-docs://api/material/ButtonTheme) and [ButtonThemeData](flutter-docs://api/material/ButtonThemeData) to define how the button bar
should size itself with either constraints or internal padding.

[ButtonTextTheme](flutter-docs://api/material/ButtonTextTheme)
Used with [ButtonTheme](flutter-docs://api/material/ButtonTheme) and [ButtonThemeData](flutter-docs://api/material/ButtonThemeData) to define a button's base
colors, and the defaults for the button's minimum size, internal padding,
and shape.

[ChangeReportingBehavior](flutter-docs://api/widgets/ChangeReportingBehavior)
The behavior of reporting the selected item index in a [ListWheelScrollView](flutter-docs://api/widgets/ListWheelScrollView).

[Clip](flutter-docs://api/dart-ui/Clip)
Different ways to clip content.

[ClipboardStatus](flutter-docs://api/widgets/ClipboardStatus)
An enumeration of the status of the content on the user's clipboard.

[CollapseMode](flutter-docs://api/material/CollapseMode)
The collapsing effect while the space bar collapses from its full size.

[ConnectionState](flutter-docs://api/widgets/ConnectionState)
The state of connection to an asynchronous computation.

[ContextMenuButtonType](flutter-docs://api/widgets/ContextMenuButtonType)
The buttons that can appear in a context menu by default.

[CrossAxisAlignment](flutter-docs://api/rendering/CrossAxisAlignment)
How the children should be placed along the cross axis in a flex layout.

[CrossFadeState](flutter-docs://api/widgets/CrossFadeState)
Specifies which of two children to show. See [AnimatedCrossFade](flutter-docs://api/widgets/AnimatedCrossFade).

[DatePickerEntryMode](flutter-docs://api/material/DatePickerEntryMode)
Mode of date entry method for the date picker dialog.

[DatePickerMode](flutter-docs://api/material/DatePickerMode)
Initial display of a calendar date picker.

[DayPeriod](flutter-docs://api/material/DayPeriod)
Whether the [TimeOfDay](flutter-docs://api/material/TimeOfDay) is before or after noon.

[DecorationPosition](flutter-docs://api/rendering/DecorationPosition)
Where to paint a box decoration.

[DiagnosticLevel](flutter-docs://api/foundation/DiagnosticLevel)
The various priority levels used to filter which diagnostics are shown and
omitted.

[DiagonalDragBehavior](flutter-docs://api/widgets/DiagonalDragBehavior)
Specifies how to configure the [DragGestureRecognizer](flutter-docs://api/gestures/DragGestureRecognizer) s of a
[TwoDimensionalScrollable](flutter-docs://api/widgets/TwoDimensionalScrollable).

[DismissDirection](flutter-docs://api/widgets/DismissDirection)
The direction in which a [Dismissible](flutter-docs://api/widgets/Dismissible) can be dismissed.

[DrawerAlignment](flutter-docs://api/material/DrawerAlignment)
The possible alignments of a [Drawer](flutter-docs://api/material/Drawer).

[DropdownMenuCloseBehavior](flutter-docs://api/material/DropdownMenuCloseBehavior)
Defines the behavior for closing the dropdown menu when an item is selected.

[DynamicSchemeVariant](flutter-docs://api/material/DynamicSchemeVariant)
The algorithm used to construct a [ColorScheme](flutter-docs://api/material/ColorScheme) in [ColorScheme.fromSeed](flutter-docs://api/material/ColorScheme/ColorScheme.fromSeed).

[FilterQuality](flutter-docs://api/dart-ui/FilterQuality)
Quality levels for image sampling in [ImageFilter](flutter-docs://api/dart-ui/ImageFilter) and [Shader](flutter-docs://api/dart-ui/Shader) objects that sample
images and for [Canvas](flutter-docs://api/dart-ui/Canvas) operations that render images.

[FlexFit](flutter-docs://api/rendering/FlexFit)
How the child is inscribed into the available space.

[FloatingHeaderSnapMode](flutter-docs://api/widgets/FloatingHeaderSnapMode)
Specifies how a partially visible [SliverFloatingHeader](flutter-docs://api/widgets/SliverFloatingHeader) animates
into a view when a user scroll gesture ends.

[FloatingLabelBehavior](flutter-docs://api/material/FloatingLabelBehavior)
Defines **how** the floating label should behave.

[FlutterLogoStyle](flutter-docs://api/painting/FlutterLogoStyle)
Possible ways to draw Flutter's logo.

[FocusHighlightMode](flutter-docs://api/widgets/FocusHighlightMode)
An enum to describe which kind of focus highlight behavior to use when
displaying focus information.

[FocusHighlightStrategy](flutter-docs://api/widgets/FocusHighlightStrategy)
An enum to describe how the current value of [FocusManager.highlightMode](flutter-docs://api/widgets/FocusManager/highlightMode) is
determined. The strategy is set on [FocusManager.highlightStrategy](flutter-docs://api/widgets/FocusManager/highlightStrategy).

[FontStyle](flutter-docs://api/dart-ui/FontStyle)
Whether to use the italic type variation of glyphs in the font.

[GrowthDirection](flutter-docs://api/rendering/GrowthDirection)
The direction in which a sliver's contents are ordered, relative to the
scroll offset axis.

[HeroFlightDirection](flutter-docs://api/widgets/HeroFlightDirection)
Direction of the hero's flight based on the navigation operation.

[HitTestBehavior](flutter-docs://api/rendering/HitTestBehavior)
How to behave during hit tests.

[HourFormat](flutter-docs://api/material/HourFormat)
Describes how hours are formatted.

[IconAlignment](flutter-docs://api/material/IconAlignment)
Determines the alignment of the icon within the widgets such as:

[ImageRepeat](flutter-docs://api/painting/ImageRepeat)
How to paint any portions of a box not covered by an image.

[InspectorButtonVariant](flutter-docs://api/widgets/InspectorButtonVariant)
Defines the visual and behavioral variants for an [InspectorButton](flutter-docs://api/widgets/InspectorButton).

[KeyEventResult](flutter-docs://api/widgets/KeyEventResult)
An enum that describes how to handle a key event handled by a
[FocusOnKeyCallback](flutter-docs://api/widgets/FocusOnKeyCallback) or [FocusOnKeyEventCallback](flutter-docs://api/widgets/FocusOnKeyEventCallback).

[ListTileControlAffinity](flutter-docs://api/material/ListTileControlAffinity)
Where to place the control in widgets that use [ListTile](flutter-docs://api/material/ListTile) to position a
control next to a label.

[ListTileStyle](flutter-docs://api/material/ListTileStyle)
Defines the title font used for [ListTile](flutter-docs://api/material/ListTile) descendants of a [ListTileTheme](flutter-docs://api/material/ListTileTheme).

[ListTileTitleAlignment](flutter-docs://api/material/ListTileTitleAlignment)
Defines how [ListTile.leading](flutter-docs://api/material/ListTile/leading) and [ListTile.trailing](flutter-docs://api/material/ListTile/trailing) are
vertically aligned relative to the [ListTile](flutter-docs://api/material/ListTile)'s titles
([ListTile.title](flutter-docs://api/material/ListTile/title) and [ListTile.subtitle](flutter-docs://api/material/ListTile/subtitle)).

[LiveTextInputStatus](flutter-docs://api/widgets/LiveTextInputStatus)
An enumeration that indicates whether the current device is available for Live Text input.

[LockState](flutter-docs://api/widgets/LockState)
Determines how the state of a lock key is used to accept a shortcut.

[MainAxisAlignment](flutter-docs://api/rendering/MainAxisAlignment)
How the children should be placed along the main axis in a flex layout.

[MainAxisSize](flutter-docs://api/rendering/MainAxisSize)
How much space should be occupied in the main axis.

[MaterialBannerClosedReason](flutter-docs://api/material/MaterialBannerClosedReason)
Specify how a [MaterialBanner](flutter-docs://api/material/MaterialBanner) was closed.

[MaterialTapTargetSize](flutter-docs://api/material/MaterialTapTargetSize)
Configures the tap target and layout size of certain Material widgets.

[MaterialType](flutter-docs://api/material/MaterialType)
The various kinds of material in Material Design. Used to
configure the default behavior of [Material](flutter-docs://api/material/Material) widgets.

[NavigationDestinationLabelBehavior](flutter-docs://api/material/NavigationDestinationLabelBehavior)
Specifies when each [NavigationDestination](flutter-docs://api/material/NavigationDestination)'s label should appear.

[NavigationMode](flutter-docs://api/widgets/NavigationMode)
Describes the navigation mode to be set by a [MediaQuery](flutter-docs://api/widgets/MediaQuery) widget.

[NavigationRailLabelType](flutter-docs://api/material/NavigationRailLabelType)
Defines the behavior of the labels of a [NavigationRail](flutter-docs://api/material/NavigationRail).

[OptionsViewOpenDirection](flutter-docs://api/widgets/OptionsViewOpenDirection)
A direction in which to open the options-view overlay.

[Orientation](flutter-docs://api/widgets/Orientation)
Whether in portrait or landscape.

[OverflowBarAlignment](flutter-docs://api/widgets/OverflowBarAlignment)
Defines the horizontal alignment of [OverflowBar](flutter-docs://api/widgets/OverflowBar) children
when they're laid out in an overflow column.

[OverlayChildLocation](flutter-docs://api/widgets/OverlayChildLocation)
The location of the [Overlay](flutter-docs://api/widgets/Overlay) that an [OverlayPortal](flutter-docs://api/widgets/OverlayPortal) renders its overlay
child on.

[PaintingStyle](flutter-docs://api/dart-ui/PaintingStyle)
Strategies for painting shapes and paths on a canvas.

[PanAxis](flutter-docs://api/widgets/PanAxis)
This enum is used to specify the behavior of the [InteractiveViewer](flutter-docs://api/widgets/InteractiveViewer) when
the user drags the viewport.

[PathFillType](flutter-docs://api/dart-ui/PathFillType)
Determines the winding rule that decides how the interior of a [Path](flutter-docs://api/dart-ui/Path) is
calculated.

[PathOperation](flutter-docs://api/dart-ui/PathOperation)
Strategies for combining paths.

[PlaceholderAlignment](flutter-docs://api/dart-ui/PlaceholderAlignment)
Where to vertically align the placeholder relative to the surrounding text.

[PlatformProvidedMenuItemType](flutter-docs://api/widgets/PlatformProvidedMenuItemType)
The list of possible platform provided, prebuilt menus for use in a
[PlatformMenuBar](flutter-docs://api/widgets/PlatformMenuBar).

[PopupMenuPosition](flutter-docs://api/material/PopupMenuPosition)
Used to configure how the [PopupMenuButton](flutter-docs://api/material/PopupMenuButton) positions its popup menu.

[RefreshIndicatorStatus](flutter-docs://api/material/RefreshIndicatorStatus)
Indicates current status of Material `RefreshIndicator`.

[RefreshIndicatorTriggerMode](flutter-docs://api/material/RefreshIndicatorTriggerMode)
Used to configure how [RefreshIndicator](flutter-docs://api/material/RefreshIndicator) can be triggered.

[RenderComparison](flutter-docs://api/painting/RenderComparison)
The description of the difference between two objects, in the context of how
it will affect the rendering.

[ResizeImagePolicy](flutter-docs://api/painting/ResizeImagePolicy)
Configures the behavior for [ResizeImage](flutter-docs://api/painting/ResizeImage).

[RouteInformationReportingType](flutter-docs://api/widgets/RouteInformationReportingType)
The [Router](flutter-docs://api/widgets/Router)'s intention when it reports a new [RouteInformation](flutter-docs://api/widgets/RouteInformation) to the
[RouteInformationProvider](flutter-docs://api/widgets/RouteInformationProvider).

[RoutePopDisposition](flutter-docs://api/widgets/RoutePopDisposition)
Indicates whether the current route should be popped.

[ScriptCategory](flutter-docs://api/material/ScriptCategory)
A characterization of the of a [TextTheme](flutter-docs://api/material/TextTheme)'s glyphs that is used to define
its localized [TextStyle](flutter-docs://api/painting/TextStyle) geometry for [ThemeData.textTheme](flutter-docs://api/material/ThemeData/textTheme).

[ScrollbarOrientation](flutter-docs://api/widgets/ScrollbarOrientation)
An orientation along either the horizontal or vertical [Axis](flutter-docs://api/painting/Axis).

[ScrollDecelerationRate](flutter-docs://api/widgets/ScrollDecelerationRate)
The rate at which scroll momentum will be decelerated.

[ScrollIncrementType](flutter-docs://api/widgets/ScrollIncrementType)
Describes the type of scroll increment that will be performed by a
[ScrollAction](flutter-docs://api/widgets/ScrollAction) on a [Scrollable](flutter-docs://api/widgets/Scrollable).

[ScrollPositionAlignmentPolicy](flutter-docs://api/widgets/ScrollPositionAlignmentPolicy)
The policy to use when applying the `alignment` parameter of
[ScrollPosition.ensureVisible](flutter-docs://api/widgets/ScrollPosition/ensureVisible).

[ScrollViewKeyboardDismissBehavior](flutter-docs://api/widgets/ScrollViewKeyboardDismissBehavior)
A representation of how a [ScrollView](flutter-docs://api/widgets/ScrollView) should dismiss the on-screen
keyboard.

[SelectableRegionSelectionStatus](flutter-docs://api/widgets/SelectableRegionSelectionStatus)
The status of the selection under a [SelectableRegion](flutter-docs://api/widgets/SelectableRegion).

[SelectionChangedCause](flutter-docs://api/services/SelectionChangedCause)
Indicates what triggered the change in selected text (including changes to
the cursor location).

[ShowValueIndicator](flutter-docs://api/material/ShowValueIndicator)
Describes the conditions under which the value indicator on a [Slider](flutter-docs://api/material/Slider) will be shown. Used with [SliderThemeData.showValueIndicator](flutter-docs://api/material/SliderThemeData/showValueIndicator).

[SliderInteraction](flutter-docs://api/material/SliderInteraction)
Possible ways for a user to interact with a [Slider](flutter-docs://api/material/Slider).

[SliverPaintOrder](flutter-docs://api/rendering/SliverPaintOrder)
Specifies an order in which to paint the slivers of a [Viewport](flutter-docs://api/widgets/Viewport).

[SmartDashesType](flutter-docs://api/services/SmartDashesType)
Indicates how to handle the intelligent replacement of dashes in text input.

[SmartQuotesType](flutter-docs://api/services/SmartQuotesType)
Indicates how to handle the intelligent replacement of quotes in text input.

[SnackBarBehavior](flutter-docs://api/material/SnackBarBehavior)
Defines where a [SnackBar](flutter-docs://api/material/SnackBar) should appear within a [Scaffold](flutter-docs://api/material/Scaffold) and how its
location should be adjusted when the scaffold also includes a
[FloatingActionButton](flutter-docs://api/material/FloatingActionButton) or a [BottomNavigationBar](flutter-docs://api/material/BottomNavigationBar).

[SnackBarClosedReason](flutter-docs://api/material/SnackBarClosedReason)
Specify how a [SnackBar](flutter-docs://api/material/SnackBar) was closed.

[SnapshotMode](flutter-docs://api/widgets/SnapshotMode)
Controls how the [SnapshotWidget](flutter-docs://api/widgets/SnapshotWidget) paints its child.

[StackFit](flutter-docs://api/rendering/StackFit)
How to size the non-positioned children of a [Stack](flutter-docs://api/widgets/Stack).

[StandardComponentType](flutter-docs://api/widgets/StandardComponentType)
An enum identifying standard UI components.

[StepperType](flutter-docs://api/material/StepperType)
Defines the [Stepper](flutter-docs://api/material/Stepper)'s main axis.

[StepState](flutter-docs://api/material/StepState)
The state of a [Step](flutter-docs://api/material/Step) which is used to control the style of the circle and
text.

[StretchMode](flutter-docs://api/material/StretchMode)
The stretching effect while the space bar stretches beyond its full size.

[StrokeCap](flutter-docs://api/dart-ui/StrokeCap)
Styles to use for line endings.

[StrokeJoin](flutter-docs://api/dart-ui/StrokeJoin)
Styles to use for line segment joins.

[TabAlignment](flutter-docs://api/material/TabAlignment)
Defines how tabs are aligned horizontally in a [TabBar](flutter-docs://api/material/TabBar).

[TabBarIndicatorSize](flutter-docs://api/material/TabBarIndicatorSize)
Defines how the bounds of the selected tab indicator are computed.

[TabIndicatorAnimation](flutter-docs://api/material/TabIndicatorAnimation)
Defines how the tab indicator animates when the selected tab changes.

[TableCellVerticalAlignment](flutter-docs://api/rendering/TableCellVerticalAlignment)
Vertical alignment options for cells in [RenderTable](flutter-docs://api/rendering/RenderTable) objects.

[TargetPlatform](flutter-docs://api/foundation/TargetPlatform)
The platform that user interaction should adapt to target.

[TextAffinity](flutter-docs://api/dart-ui/TextAffinity)
A way to disambiguate a [TextPosition](flutter-docs://api/dart-ui/TextPosition) when its offset could match two
different locations in the rendered string.

[TextAlign](flutter-docs://api/dart-ui/TextAlign)
Whether and how to align text horizontally.

[TextBaseline](flutter-docs://api/dart-ui/TextBaseline)
A horizontal line used for aligning text.

[TextCapitalization](flutter-docs://api/services/TextCapitalization)
Configures how the platform keyboard will select an uppercase or
lowercase keyboard.

[TextDecorationStyle](flutter-docs://api/dart-ui/TextDecorationStyle)
The style in which to draw a text decoration

[TextDirection](flutter-docs://api/dart-ui/TextDirection)
A direction in which text flows.

[TextInputAction](flutter-docs://api/flutter_test/TextInputAction)
An action the user has requested the text input control to perform.

[TextLeadingDistribution](flutter-docs://api/dart-ui/TextLeadingDistribution)
How the ["leading"](https://en.wikipedia.org/wiki/Leading) is distributed
over and under the text.

[TextOverflow](flutter-docs://api/painting/TextOverflow)
How overflowing text should be handled.

[TextSelectionHandleType](flutter-docs://api/rendering/TextSelectionHandleType)
The type of selection handle to be displayed.

[TextWidthBasis](flutter-docs://api/painting/TextWidthBasis)
The different ways of measuring the width of one or more lines of text.

[ThemeMode](flutter-docs://api/material/ThemeMode)
Describes which theme will be used by [MaterialApp](flutter-docs://api/material/MaterialApp).

[Thumb](flutter-docs://api/material/Thumb)
Identifier for a thumb.

[TileMode](flutter-docs://api/dart-ui/TileMode)
Defines how to handle areas outside the defined bounds of a gradient or image filter.

[TimeOfDayFormat](flutter-docs://api/material/TimeOfDayFormat)
Determines how the time picker invoked using [showTimePicker](flutter-docs://api/material/showTimePicker) formats and
lays out the time controls.

[TimePickerEntryMode](flutter-docs://api/material/TimePickerEntryMode)
Interactive input mode of the time picker dialog.

[TooltipTriggerMode](flutter-docs://api/material/TooltipTriggerMode)
The method of interaction that will trigger a tooltip.
Used in [Tooltip.triggerMode](flutter-docs://api/material/Tooltip/triggerMode) and [TooltipThemeData.triggerMode](flutter-docs://api/material/TooltipThemeData/triggerMode).

[TraversalDirection](flutter-docs://api/widgets/TraversalDirection)
A direction along either the horizontal or vertical axes.

[TraversalEdgeBehavior](flutter-docs://api/widgets/TraversalEdgeBehavior)
Controls the focus transfer at the edges of a [FocusScopeNode](flutter-docs://api/widgets/FocusScopeNode).
For movement transfers (previous or next), the edge represents
the first or last items. For directional transfers, the edge
represents the outermost items of the [FocusScopeNode](flutter-docs://api/widgets/FocusScopeNode), For example:
for moving downwards, the edge node is the one with the largest bottom
coordinate; for moving leftwards, the edge node is the one with the
smallest x coordinate.

[UnfocusDisposition](flutter-docs://api/widgets/UnfocusDisposition)
Describe what should happen after [FocusNode.unfocus](flutter-docs://api/widgets/FocusNode/unfocus) is called.

[VertexMode](flutter-docs://api/dart-ui/VertexMode)
Defines how a list of points is interpreted when drawing a set of triangles.

[VerticalDirection](flutter-docs://api/painting/VerticalDirection)
A direction in which boxes flow vertically.

[WebHtmlElementStrategy](flutter-docs://api/painting/WebHtmlElementStrategy)
The strategy for [Image.network](flutter-docs://api/widgets/Image/Image.network) and [NetworkImage](flutter-docs://api/painting/NetworkImage) to decide whether to
display images in HTML elements contained in a platform view instead of
fetching bytes.

[WidgetInspectorServiceExtensions](flutter-docs://api/widgets/WidgetInspectorServiceExtensions)
Service extension constants for the Widget Inspector.

[WidgetsServiceExtensions](flutter-docs://api/widgets/WidgetsServiceExtensions)
Service extension constants for the widgets library.

[WidgetState](flutter-docs://api/widgets/WidgetState)
Interactive states that some of the widgets can take on when receiving input
from the user.

[WrapAlignment](flutter-docs://api/rendering/WrapAlignment)
How [Wrap](flutter-docs://api/widgets/Wrap) should align objects.

[WrapCrossAlignment](flutter-docs://api/rendering/WrapCrossAlignment)
Who [Wrap](flutter-docs://api/widgets/Wrap) should align children within a run in the cross axis.

## Mixins

[AnimationEagerListenerMixin](flutter-docs://api/animation/AnimationEagerListenerMixin)
A mixin that replaces the [didRegisterListener](flutter-docs://api/animation/AnimationEagerListenerMixin/didRegisterListener)/[didUnregisterListener](flutter-docs://api/animation/AnimationEagerListenerMixin/didUnregisterListener) contract
with a dispose contract.

[AnimationLazyListenerMixin](flutter-docs://api/animation/AnimationLazyListenerMixin)
A mixin that helps listen to another object only when this object has registered listeners.

[AnimationLocalListenersMixin](flutter-docs://api/animation/AnimationLocalListenersMixin)
A mixin that implements the [addListener](flutter-docs://api/animation/AnimationLocalListenersMixin/addListener)/[removeListener](flutter-docs://api/animation/AnimationLocalListenersMixin/removeListener) protocol and notifies
all the registered listeners when [notifyListeners](flutter-docs://api/animation/AnimationLocalListenersMixin/notifyListeners) is called.

[AnimationLocalStatusListenersMixin](flutter-docs://api/animation/AnimationLocalStatusListenersMixin)
A mixin that implements the addStatusListener/removeStatusListener protocol
and notifies all the registered listeners when notifyStatusListeners is
called.

[AnimationWithParentMixin](flutter-docs://api/animation/AnimationWithParentMixin)<T>
Implements most of the [Animation](flutter-docs://api/animation/Animation) interface by deferring its behavior to a
given [parent](flutter-docs://api/animation/AnimationWithParentMixin/parent) Animation.

[AutomaticKeepAliveClientMixin](flutter-docs://api/widgets/AutomaticKeepAliveClientMixin)<T extends [StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>
A mixin with convenience methods for clients of [AutomaticKeepAlive](flutter-docs://api/widgets/AutomaticKeepAlive). It is used
with [State](flutter-docs://api/widgets/State) subclasses to manage keep-alive behavior in lazily built lists.

[BaseRangeSliderTrackShape](flutter-docs://api/material/BaseRangeSliderTrackShape)
Base range slider track shape that provides an implementation of [getPreferredRect](flutter-docs://api/material/BaseRangeSliderTrackShape/getPreferredRect) for
default sizing.

[BaseSliderTrackShape](flutter-docs://api/material/BaseSliderTrackShape)
Base track shape that provides an implementation of [getPreferredRect](flutter-docs://api/material/BaseSliderTrackShape/getPreferredRect) for
default sizing.

[DirectionalFocusTraversalPolicyMixin](flutter-docs://api/widgets/DirectionalFocusTraversalPolicyMixin)
A mixin class that provides an implementation for finding a node in a
particular direction.

[FabCenterOffsetX](flutter-docs://api/material/FabCenterOffsetX)
Mixin for a "center" floating action button location, such as [FloatingActionButtonLocation.centerFloat](flutter-docs://api/material/FloatingActionButtonLocation/centerFloat).

[FabContainedOffsetY](flutter-docs://api/material/FabContainedOffsetY)
Mixin for a "contained" floating action button location, such as [FloatingActionButtonLocation.endContained](flutter-docs://api/material/FloatingActionButtonLocation/endContained).

[FabDockedOffsetY](flutter-docs://api/material/FabDockedOffsetY)
Mixin for a "docked" floating action button location, such as [FloatingActionButtonLocation.endDocked](flutter-docs://api/material/FloatingActionButtonLocation/endDocked).

[FabEndOffsetX](flutter-docs://api/material/FabEndOffsetX)
Mixin for an "end" floating action button location, such as [FloatingActionButtonLocation.endDocked](flutter-docs://api/material/FloatingActionButtonLocation/endDocked).

[FabFloatOffsetY](flutter-docs://api/material/FabFloatOffsetY)
Mixin for a "float" floating action button location, such as [FloatingActionButtonLocation.centerFloat](flutter-docs://api/material/FloatingActionButtonLocation/centerFloat).

[FabMiniOffsetAdjustment](flutter-docs://api/material/FabMiniOffsetAdjustment)
Mixin for a "mini" floating action button location, such as [FloatingActionButtonLocation.miniStartTop](flutter-docs://api/material/FloatingActionButtonLocation/miniStartTop).

[FabStartOffsetX](flutter-docs://api/material/FabStartOffsetX)
Mixin for a "start" floating action button location, such as [FloatingActionButtonLocation.startTop](flutter-docs://api/material/FloatingActionButtonLocation/startTop).

[FabTopOffsetY](flutter-docs://api/material/FabTopOffsetY)
Mixin for a "top" floating action button location, such as
[FloatingActionButtonLocation.startTop](flutter-docs://api/material/FloatingActionButtonLocation/startTop).

[LocalHistoryRoute](flutter-docs://api/widgets/LocalHistoryRoute)<T>
A mixin used by routes to handle back navigations internally by popping a list.

[MaterialRouteTransitionMixin](flutter-docs://api/material/MaterialRouteTransitionMixin)<T>
A mixin that provides platform-adaptive transitions for a [PageRoute](flutter-docs://api/widgets/PageRoute).

[MaterialStateMixin](flutter-docs://api/material/MaterialStateMixin)<T extends [StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>
Mixin for [State](flutter-docs://api/widgets/State) classes that require knowledge of changing [WidgetState](flutter-docs://api/widgets/WidgetState) values for their child widgets.

[MenuSerializableShortcut](flutter-docs://api/widgets/MenuSerializableShortcut)
A mixin allowing a [ShortcutActivator](flutter-docs://api/widgets/ShortcutActivator) to provide data for serialization of
the shortcut when sending to the platform.

[NotifiableElementMixin](flutter-docs://api/widgets/NotifiableElementMixin)
Mixin this class to allow receiving [Notification](flutter-docs://api/widgets/Notification) objects dispatched by
child elements.

[PaintingBinding](flutter-docs://api/painting/PaintingBinding)
Binding for the painting library.

[PopNavigatorRouterDelegateMixin](flutter-docs://api/widgets/PopNavigatorRouterDelegateMixin)<T>
A mixin that wires [RouterDelegate.popRoute](flutter-docs://api/widgets/RouterDelegate/popRoute) to the [Navigator](flutter-docs://api/widgets/Navigator) it builds.

[RadioClient](flutter-docs://api/widgets/RadioClient)<T>
A client for a [RadioGroupRegistry](flutter-docs://api/widgets/RadioGroupRegistry).

[RenderAbstractLayoutBuilderMixin](flutter-docs://api/widgets/RenderAbstractLayoutBuilderMixin)<LayoutInfoType, ChildType extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
Generic mixin for [RenderObject](flutter-docs://api/rendering/RenderObject) s created by an [AbstractLayoutBuilder](flutter-docs://api/widgets/AbstractLayoutBuilder) with
the the same `LayoutInfoType`.

[RestorationMixin](flutter-docs://api/widgets/RestorationMixin)<S extends [StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>
Manages the restoration data for a [State](flutter-docs://api/widgets/State) object of a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget).

[RootElementMixin](flutter-docs://api/widgets/RootElementMixin)
Mixin for the element at the root of the tree.

[ScrollMetrics](flutter-docs://api/widgets/ScrollMetrics)
A description of a [Scrollable](flutter-docs://api/widgets/Scrollable)'s contents, useful for modeling the state
of its viewport.

[SingleTickerProviderStateMixin](flutter-docs://api/widgets/SingleTickerProviderStateMixin)<T extends [StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>
Provides a single [Ticker](flutter-docs://api/scheduler/Ticker) that is configured to only tick while the current
tree is enabled, as defined by [TickerMode](flutter-docs://api/widgets/TickerMode).

[SlottedContainerRenderObjectMixin](flutter-docs://api/widgets/SlottedContainerRenderObjectMixin)<SlotType, ChildType extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
Mixin for a [RenderObject](flutter-docs://api/rendering/RenderObject) configured by a [SlottedMultiChildRenderObjectWidget](flutter-docs://api/widgets/SlottedMultiChildRenderObjectWidget).

[SlottedMultiChildRenderObjectWidgetMixin](flutter-docs://api/widgets/SlottedMultiChildRenderObjectWidgetMixin)<SlotType, ChildType extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
A mixin version of [SlottedMultiChildRenderObjectWidget](flutter-docs://api/widgets/SlottedMultiChildRenderObjectWidget).

[TextSelectionDelegate](flutter-docs://api/services/TextSelectionDelegate)
A mixin for manipulating the selection, provided for toolbar or shortcut
keys.

[TextSelectionHandleControls](flutter-docs://api/widgets/TextSelectionHandleControls)
[TextSelectionControls](flutter-docs://api/widgets/TextSelectionControls) that specifically do not manage the toolbar in order
to leave that to [EditableText.contextMenuBuilder](flutter-docs://api/widgets/EditableText/contextMenuBuilder).

[TickerProviderStateMixin](flutter-docs://api/widgets/TickerProviderStateMixin)<T extends [StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>
Provides [Ticker](flutter-docs://api/scheduler/Ticker) objects that are configured to only tick while the current
tree is enabled, as defined by [TickerMode](flutter-docs://api/widgets/TickerMode).

[ToggleableStateMixin](flutter-docs://api/widgets/ToggleableStateMixin)<S extends [StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>
A mixin for [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) s that implement toggleable
controls with toggle animations (e.g. [Switch](flutter-docs://api/material/Switch) es, [CupertinoSwitch](flutter-docs://api/cupertino/CupertinoSwitch) es,
[Checkbox](flutter-docs://api/material/Checkbox) es, [CupertinoCheckbox](flutter-docs://api/cupertino/CupertinoCheckbox) es, [Radio](flutter-docs://api/material/Radio) s, and [CupertinoRadio](flutter-docs://api/cupertino/CupertinoRadio) s).

[TreeSliverStateMixin](flutter-docs://api/widgets/TreeSliverStateMixin)<T>
A mixin for classes implementing a tree structure as expected by a
[TreeSliverController](flutter-docs://api/widgets/TreeSliverController).

[ViewportElementMixin](flutter-docs://api/widgets/ViewportElementMixin)
A mixin that allows [Element](flutter-docs://api/widgets/Element) s containing [Viewport](flutter-docs://api/widgets/Viewport) like widgets to correctly
modify the notification depth of a [ViewportNotificationMixin](flutter-docs://api/widgets/ViewportNotificationMixin).

[ViewportNotificationMixin](flutter-docs://api/widgets/ViewportNotificationMixin)
Mixin for [Notification](flutter-docs://api/widgets/Notification) s that track how many [RenderAbstractViewport](flutter-docs://api/rendering/RenderAbstractViewport) they
have bubbled through.

[WidgetInspectorService](flutter-docs://api/widgets/WidgetInspectorService)
Service used by GUI tools to interact with the [WidgetInspector](flutter-docs://api/widgets/WidgetInspector).

[WidgetsBinding](flutter-docs://api/widgets/WidgetsBinding)
The glue between the widgets layer and the Flutter engine.

## Extension Types

[OverlayChildLayoutInfo](flutter-docs://api/widgets/OverlayChildLayoutInfo)
The additional layout information available to the
[OverlayPortal.overlayChildLayoutBuilder](flutter-docs://api/widgets/OverlayPortal/OverlayPortal.overlayChildLayoutBuilder) callback.

## Extensions

[StringCharacters](flutter-docs://api/package-characters_characters/StringCharacters) on [String](flutter-docs://api/dart-core/String)
[WidgetStateOperators](flutter-docs://api/widgets/WidgetStateOperators) on [WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint)
These operators can be used inside a [WidgetStateMap](flutter-docs://api/widgets/WidgetStateMap) to combine states
and find a match.

## Constants

[accelerateEasing](flutter-docs://api/material/accelerateEasing) → const [Curve](flutter-docs://api/animation/Curve)
The accelerate easing curve in the Material 2 specification.

[decelerateEasing](flutter-docs://api/material/decelerateEasing) → const [Curve](flutter-docs://api/animation/Curve)
The decelerate easing curve in the Material 2 specification.

[factory](flutter-docs://api/meta/factory) → const _Factory
Used to annotate an instance or static method `m`. Indicates that `m` must
either be abstract or must return a newly allocated object or `null`. In
addition, every method that either implements or overrides `m` is implicitly
annotated with this same annotation.

[immutable](flutter-docs://api/meta/immutable) → const [Immutable](flutter-docs://api/meta/Immutable)
Used to annotate a class `C`. Indicates that `C` and all subtypes of `C` must be immutable.

[iOSHorizontalOffset](flutter-docs://api/material/iOSHorizontalOffset) → const [int](flutter-docs://api/dart-core/int)
An eyeballed value that moves the cursor slightly left of where it is
rendered for text on Android so its positioning more accurately matches the
native iOS text cursor positioning.

[kAlwaysCompleteAnimation](flutter-docs://api/cupertino/kAlwaysCompleteAnimation) → const [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)>
An animation that is always complete.

[kAlwaysDismissedAnimation](flutter-docs://api/cupertino/kAlwaysDismissedAnimation) → const [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)>
An animation that is always dismissed.

[kBottomNavigationBarHeight](flutter-docs://api/material/kBottomNavigationBarHeight) → const [double](flutter-docs://api/dart-core/double)
The height of the bottom navigation bar.

[kDefaultContentInsertionMimeTypes](flutter-docs://api/cupertino/kDefaultContentInsertionMimeTypes) → const [List](flutter-docs://api/dart-core/List)<[String](flutter-docs://api/dart-core/String)>
The default mime types to be used when allowedMimeTypes is not provided.

[kDefaultFontSize](flutter-docs://api/rendering/kDefaultFontSize) → const [double](flutter-docs://api/dart-core/double)
The default font size if none is specified.

[kDefaultRouteDirectionalTraversalEdgeBehavior](flutter-docs://api/cupertino/kDefaultRouteDirectionalTraversalEdgeBehavior) → const [TraversalEdgeBehavior](flutter-docs://api/widgets/TraversalEdgeBehavior)
The default value of [Navigator.routeDirectionalTraversalEdgeBehavior](flutter-docs://api/widgets/Navigator/routeDirectionalTraversalEdgeBehavior).

[kDefaultRouteTraversalEdgeBehavior](flutter-docs://api/cupertino/kDefaultRouteTraversalEdgeBehavior) → const [TraversalEdgeBehavior](flutter-docs://api/widgets/TraversalEdgeBehavior)
The default value of [Navigator.routeTraversalEdgeBehavior](flutter-docs://api/widgets/Navigator/routeTraversalEdgeBehavior).

[kElevationToShadow](flutter-docs://api/material/kElevationToShadow) → const [Map](flutter-docs://api/dart-core/Map)<[int](flutter-docs://api/dart-core/int), [List](flutter-docs://api/dart-core/List)<[BoxShadow](flutter-docs://api/painting/BoxShadow)>>
Map of elevation offsets used by Material Design to [BoxShadow](flutter-docs://api/painting/BoxShadow) definitions.

[kFloatingActionButtonMargin](flutter-docs://api/material/kFloatingActionButtonMargin) → const [double](flutter-docs://api/dart-core/double)
The margin that a [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) should leave between it and the
edge of the screen.

[kFloatingActionButtonSegue](flutter-docs://api/material/kFloatingActionButtonSegue) → const [Duration](flutter-docs://api/dart-core/Duration)
The amount of time the [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) takes to transition in or out.

[kFloatingActionButtonTurnInterval](flutter-docs://api/material/kFloatingActionButtonTurnInterval) → const [double](flutter-docs://api/dart-core/double)
The fraction of a circle the [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) should turn when it enters.

[kMaterialEdges](flutter-docs://api/material/kMaterialEdges) → const [Map](flutter-docs://api/dart-core/Map)<[MaterialType](flutter-docs://api/material/MaterialType), [BorderRadius](flutter-docs://api/painting/BorderRadius)?>
The border radii used by the various kinds of material in Material Design.

[kMaterialListPadding](flutter-docs://api/material/kMaterialListPadding) → const [EdgeInsets](flutter-docs://api/painting/EdgeInsets)
The padding added around material list items.

[kMiniButtonOffsetAdjustment](flutter-docs://api/material/kMiniButtonOffsetAdjustment) → const [double](flutter-docs://api/dart-core/double)
If a [FloatingActionButton](flutter-docs://api/material/FloatingActionButton) is used on a [Scaffold](flutter-docs://api/material/Scaffold) in certain positions,
it is moved [kMiniButtonOffsetAdjustment](flutter-docs://api/material/kMiniButtonOffsetAdjustment) pixels closer to the edge of the screen.

[kMinInteractiveDimension](flutter-docs://api/material/kMinInteractiveDimension) → const [double](flutter-docs://api/dart-core/double)
The minimum dimension of any interactive region according to Material
guidelines.

[kRadialReactionAlpha](flutter-docs://api/material/kRadialReactionAlpha) → const [int](flutter-docs://api/dart-core/int)
The value of the alpha channel to use when drawing a circular material ink response.

[kRadialReactionDuration](flutter-docs://api/material/kRadialReactionDuration) → const [Duration](flutter-docs://api/dart-core/Duration)
The amount of time a circular material ink response should take to expand to its full size.

[kRadialReactionRadius](flutter-docs://api/material/kRadialReactionRadius) → const [double](flutter-docs://api/dart-core/double)
The default radius of a circular material ink response in logical pixels.

[kTabLabelPadding](flutter-docs://api/material/kTabLabelPadding) → const [EdgeInsets](flutter-docs://api/painting/EdgeInsets)
The horizontal padding included by [Tab](flutter-docs://api/material/Tab) s.

[kTabScrollDuration](flutter-docs://api/material/kTabScrollDuration) → const [Duration](flutter-docs://api/dart-core/Duration)
The duration of the horizontal scroll animation that occurs when a tab is tapped.

[kTextHeightNone](flutter-docs://api/dart-ui/kTextHeightNone) → const [double](flutter-docs://api/dart-core/double)
A `TextStyle.height` value that indicates the text span should take
the height defined by the font, which may not be exactly the height of
`TextStyle.fontSize`.

[kTextTabBarHeight](flutter-docs://api/material/kTextTabBarHeight) → const [double](flutter-docs://api/dart-core/double)
The height of a tab bar containing text.

[kThemeAnimationDuration](flutter-docs://api/material/kThemeAnimationDuration) → const [Duration](flutter-docs://api/dart-core/Duration)
The duration over which theme changes animate by default.

[kThemeChangeDuration](flutter-docs://api/material/kThemeChangeDuration) → const [Duration](flutter-docs://api/dart-core/Duration)
The amount of time theme change animations should last.

[kToolbarHeight](flutter-docs://api/material/kToolbarHeight) → const [double](flutter-docs://api/dart-core/double)
The height of the toolbar component of the [AppBar](flutter-docs://api/material/AppBar).

[mustCallSuper](flutter-docs://api/meta/mustCallSuper) → const _MustCallSuper
Used to annotate an instance member (method, getter, setter, operator, or
field) `m`. Indicates that every invocation of a member that overrides `m` must also invoke `m`. In addition, every method that overrides `m` is
implicitly annotated with this same annotation.

[optionalTypeArgs](flutter-docs://api/meta/optionalTypeArgs) → const _OptionalTypeArgs
Used to annotate a class, mixin, extension, function, method, or typedef
declaration `C`. Indicates that any type arguments declared on `C` are to
be treated as optional.

[protected](flutter-docs://api/meta/protected) → const _Protected
Used to annotate an instance member in a class or mixin which is meant to
be visible only within the declaring library, and to other instance members
of the class or mixin, and their subtypes.

[required](flutter-docs://api/meta/required) → const [Required](flutter-docs://api/meta/Required)
Used to annotate a named parameter `p` in a method or function `f`.
Indicates that every invocation of `f` must include an argument
corresponding to `p`, despite the fact that `p` would otherwise be an
optional parameter.

[standardEasing](flutter-docs://api/material/standardEasing) → const [Curve](flutter-docs://api/animation/Curve)
The standard easing curve in the Material 2 specification.

[staticIconProvider](flutter-docs://api/cupertino/staticIconProvider) → const [Object](flutter-docs://api/dart-core/Object)
Annotation for classes that only provide static const [IconData](flutter-docs://api/widgets/IconData) instances.

[visibleForTesting](flutter-docs://api/meta/visibleForTesting) → const _VisibleForTesting
Used to annotate a declaration that was made public, so that it is more
visible than otherwise necessary, to make code testable.

[widgetFactory](flutter-docs://api/cupertino/widgetFactory) → const _WidgetFactory
Annotation which marks a function as a widget factory for the purpose of
widget creation tracking.

## Properties

[debugCaptureShaderWarmUpImage](flutter-docs://api/rendering/debugCaptureShaderWarmUpImage) ↔ [ShaderWarmUpImageCallback](flutter-docs://api/painting/ShaderWarmUpImageCallback)
Called by [ShaderWarmUp.execute](flutter-docs://api/painting/ShaderWarmUp/execute) immediately after it creates an [Image](flutter-docs://api/dart-ui/Image).


[debugCaptureShaderWarmUpPicture](flutter-docs://api/rendering/debugCaptureShaderWarmUpPicture) ↔ [ShaderWarmUpPictureCallback](flutter-docs://api/painting/ShaderWarmUpPictureCallback)
Called by [ShaderWarmUp.execute](flutter-docs://api/painting/ShaderWarmUp/execute) immediately after it creates a [Picture](flutter-docs://api/dart-ui/Picture).


[debugDisableShadows](flutter-docs://api/rendering/debugDisableShadows) ↔ [bool](flutter-docs://api/dart-core/bool)
Whether to replace all shadows with solid color blocks.


[debugEnhanceBuildTimelineArguments](flutter-docs://api/cupertino/debugEnhanceBuildTimelineArguments) ↔ [bool](flutter-docs://api/dart-core/bool)
Adds debugging information to [Timeline](flutter-docs://api/dart-developer/Timeline) events related to [Widget](flutter-docs://api/widgets/Widget) builds.


[debugFocusChanges](flutter-docs://api/cupertino/debugFocusChanges) ↔ [bool](flutter-docs://api/dart-core/bool)
Setting to true will cause extensive logging to occur when focus changes occur.


[debugHighlightDeprecatedWidgets](flutter-docs://api/cupertino/debugHighlightDeprecatedWidgets) ↔ [bool](flutter-docs://api/dart-core/bool)
Show banners for deprecated widgets.


[debugImageOverheadAllowance](flutter-docs://api/rendering/debugImageOverheadAllowance) ↔ [int](flutter-docs://api/dart-core/int)
The number of bytes an image must use before it triggers inversion when
[debugInvertOversizedImages](flutter-docs://api/rendering/debugInvertOversizedImages) is true.


[debugInvertOversizedImages](flutter-docs://api/rendering/debugInvertOversizedImages) ↔ [bool](flutter-docs://api/dart-core/bool)
If true, the framework will color invert and horizontally flip images that
have been decoded to a size taking at least [debugImageOverheadAllowance](flutter-docs://api/rendering/debugImageOverheadAllowance) bytes more than necessary.


[debugNetworkImageHttpClientProvider](flutter-docs://api/rendering/debugNetworkImageHttpClientProvider) ↔ [HttpClientProvider](flutter-docs://api/painting/HttpClientProvider)?
Provider from which [NetworkImage](flutter-docs://api/painting/NetworkImage) will get its [HttpClient](flutter-docs://api/dart-io/HttpClient) in debug builds.


[debugOnPaintImage](flutter-docs://api/rendering/debugOnPaintImage) ↔ [PaintImageCallback](flutter-docs://api/painting/PaintImageCallback)?
If not null, called when the framework is about to paint an [Image](flutter-docs://api/dart-ui/Image) to a
[Canvas](flutter-docs://api/dart-ui/Canvas) with an [ImageSizeInfo](flutter-docs://api/painting/ImageSizeInfo) that contains the decoded size of the
image as well as its output size.


[debugOnRebuildDirtyWidget](flutter-docs://api/cupertino/debugOnRebuildDirtyWidget) ↔ [RebuildDirtyWidgetCallback](flutter-docs://api/widgets/RebuildDirtyWidgetCallback)?
Callback invoked for every dirty widget built each frame.


[debugPrint](flutter-docs://api/rendering/debugPrint) ↔ [DebugPrintCallback](flutter-docs://api/foundation/DebugPrintCallback)
Prints a message to the console, which you can access using the "flutter"
tool's "logs" command ("flutter logs").


[debugPrintBuildScope](flutter-docs://api/cupertino/debugPrintBuildScope) ↔ [bool](flutter-docs://api/dart-core/bool)
Log all calls to [BuildOwner.buildScope](flutter-docs://api/widgets/BuildOwner/buildScope).


[debugPrintGlobalKeyedWidgetLifecycle](flutter-docs://api/cupertino/debugPrintGlobalKeyedWidgetLifecycle) ↔ [bool](flutter-docs://api/dart-core/bool)
Log when widgets with global keys are deactivated and log when they are
reactivated (retaken).


[debugPrintRebuildDirtyWidgets](flutter-docs://api/cupertino/debugPrintRebuildDirtyWidgets) ↔ [bool](flutter-docs://api/dart-core/bool)
Log the dirty widgets that are built each frame.


[debugPrintScheduleBuildForStacks](flutter-docs://api/cupertino/debugPrintScheduleBuildForStacks) ↔ [bool](flutter-docs://api/dart-core/bool)
Log the call stacks that mark widgets as needing to be rebuilt.


[debugProfileBuildsEnabled](flutter-docs://api/cupertino/debugProfileBuildsEnabled) ↔ [bool](flutter-docs://api/dart-core/bool)
Adds [Timeline](flutter-docs://api/dart-developer/Timeline) events for every Widget built.


[debugProfileBuildsEnabledUserWidgets](flutter-docs://api/cupertino/debugProfileBuildsEnabledUserWidgets) ↔ [bool](flutter-docs://api/dart-core/bool)
Adds [Timeline](flutter-docs://api/dart-developer/Timeline) events for every user-created [Widget](flutter-docs://api/widgets/Widget) built.


[desktopTextSelectionControls](flutter-docs://api/material/desktopTextSelectionControls) → [TextSelectionControls](flutter-docs://api/widgets/TextSelectionControls)
Desktop text selection controls that loosely follow Material design
conventions.


[desktopTextSelectionHandleControls](flutter-docs://api/material/desktopTextSelectionHandleControls) → [TextSelectionControls](flutter-docs://api/widgets/TextSelectionControls)
Desktop text selection handle controls that loosely follow Material design
conventions.


[emptyTextSelectionControls](flutter-docs://api/cupertino/emptyTextSelectionControls) → [TextSelectionControls](flutter-docs://api/widgets/TextSelectionControls)
Text selection controls that do not show any toolbars or handles.


[imageCache](flutter-docs://api/rendering/imageCache) → [ImageCache](flutter-docs://api/painting/ImageCache)
The singleton that implements the Flutter framework's image cache.


[kDefaultIconDarkColor](flutter-docs://api/material/kDefaultIconDarkColor) → [Color](flutter-docs://api/dart-ui/Color)
The default color for [ThemeData.iconTheme](flutter-docs://api/material/ThemeData/iconTheme) when [ThemeData.brightness](flutter-docs://api/material/ThemeData/brightness) is
[Brightness.light](flutter-docs://api/dart-ui/Brightness). This color is used in [IconButton](flutter-docs://api/material/IconButton) to detect whether
[IconTheme.of(context).color](flutter-docs://api/widgets/IconTheme/of) is the same as the default color of [ThemeData.iconTheme](flutter-docs://api/material/ThemeData/iconTheme).


[kDefaultIconLightColor](flutter-docs://api/material/kDefaultIconLightColor) → [Color](flutter-docs://api/dart-ui/Color)
The default color for [ThemeData.iconTheme](flutter-docs://api/material/ThemeData/iconTheme) when [ThemeData.brightness](flutter-docs://api/material/ThemeData/brightness) is
[Brightness.dark](flutter-docs://api/dart-ui/Brightness). This color is used in [IconButton](flutter-docs://api/material/IconButton) to detect whether
[IconTheme.of(context).color](flutter-docs://api/widgets/IconTheme/of) is the same as the default color of [ThemeData.iconTheme](flutter-docs://api/material/ThemeData/iconTheme).


[materialTextSelectionControls](flutter-docs://api/material/materialTextSelectionControls) → [TextSelectionControls](flutter-docs://api/widgets/TextSelectionControls)
Text selection controls that follow the Material Design specification.


[materialTextSelectionHandleControls](flutter-docs://api/material/materialTextSelectionHandleControls) → [TextSelectionControls](flutter-docs://api/widgets/TextSelectionControls)
Text selection handle controls that follow the Material Design specification.


[primaryFocus](flutter-docs://api/cupertino/primaryFocus) → [FocusNode](flutter-docs://api/widgets/FocusNode)?
Provides convenient access to the current [FocusManager.primaryFocus](flutter-docs://api/widgets/FocusManager/primaryFocus) from
the [WidgetsBinding](flutter-docs://api/widgets/WidgetsBinding) instance.


## Functions

[applyBoxFit](flutter-docs://api/painting/applyBoxFit)([BoxFit](flutter-docs://api/painting/BoxFit) fit, [Size](flutter-docs://api/dart-ui/Size) inputSize, [Size](flutter-docs://api/dart-ui/Size) outputSize) → [FittedSizes](flutter-docs://api/painting/FittedSizes)
Apply a [BoxFit](flutter-docs://api/painting/BoxFit) value.

[axisDirectionIsReversed](flutter-docs://api/painting/axisDirectionIsReversed)([AxisDirection](flutter-docs://api/painting/AxisDirection) axisDirection) → [bool](flutter-docs://api/dart-core/bool)
Returns whether traveling along the given axis direction visits coordinates
along that axis in numerically decreasing order.

[axisDirectionToAxis](flutter-docs://api/painting/axisDirectionToAxis)([AxisDirection](flutter-docs://api/painting/AxisDirection) axisDirection) → [Axis](flutter-docs://api/painting/Axis)
Returns the [Axis](flutter-docs://api/painting/Axis) that contains the given [AxisDirection](flutter-docs://api/painting/AxisDirection).

[basicLocaleListResolution](flutter-docs://api/widgets/basicLocaleListResolution)([List](flutter-docs://api/dart-core/List)<[Locale](flutter-docs://api/dart-ui/Locale)>? preferredLocales, [Iterable](flutter-docs://api/dart-core/Iterable)<[Locale](flutter-docs://api/dart-ui/Locale)> supportedLocales) → [Locale](flutter-docs://api/dart-ui/Locale)
The default locale resolution algorithm.

[buildTextSpanWithSpellCheckSuggestions](flutter-docs://api/widgets/buildTextSpanWithSpellCheckSuggestions)([TextEditingValue](flutter-docs://api/flutter_test/TextEditingValue) value, [bool](flutter-docs://api/dart-core/bool) composingWithinCurrentTextRange, [TextStyle](flutter-docs://api/painting/TextStyle)? style, [TextStyle](flutter-docs://api/painting/TextStyle) misspelledTextStyle, [SpellCheckResults](flutter-docs://api/services/SpellCheckResults) spellCheckResults) → [TextSpan](flutter-docs://api/painting/TextSpan)
Builds the [TextSpan](flutter-docs://api/painting/TextSpan) tree given the current state of the text input and
spell check results.

[childDragAnchorStrategy](flutter-docs://api/widgets/childDragAnchorStrategy)([Draggable](flutter-docs://api/widgets/Draggable)<[Object](flutter-docs://api/dart-core/Object)> draggable, [BuildContext](flutter-docs://api/widgets/BuildContext) context, [Offset](flutter-docs://api/dart-ui/Offset) position) → [Offset](flutter-docs://api/dart-ui/Offset)
Display the feedback anchored at the position of the original child.

[combineKeyEventResults](flutter-docs://api/widgets/combineKeyEventResults)([Iterable](flutter-docs://api/dart-core/Iterable)<[KeyEventResult](flutter-docs://api/widgets/KeyEventResult)> results) → [KeyEventResult](flutter-docs://api/widgets/KeyEventResult)
Combine the results returned by multiple [FocusOnKeyCallback](flutter-docs://api/widgets/FocusOnKeyCallback) s or
[FocusOnKeyEventCallback](flutter-docs://api/widgets/FocusOnKeyEventCallback) s.

[combineSemanticsInfo](flutter-docs://api/painting/combineSemanticsInfo)([List](flutter-docs://api/dart-core/List)<[InlineSpanSemanticsInformation](flutter-docs://api/painting/InlineSpanSemanticsInformation)> infoList) → [List](flutter-docs://api/dart-core/List)<[InlineSpanSemanticsInformation](flutter-docs://api/painting/InlineSpanSemanticsInformation)>
Combines _semanticsInfo entries where permissible.

[createLocalImageConfiguration](flutter-docs://api/widgets/createLocalImageConfiguration)([BuildContext](flutter-docs://api/widgets/BuildContext) context, {[Size](flutter-docs://api/dart-ui/Size)? size}) → [ImageConfiguration](flutter-docs://api/painting/ImageConfiguration)
Creates an [ImageConfiguration](flutter-docs://api/painting/ImageConfiguration) based on the given [BuildContext](flutter-docs://api/widgets/BuildContext) (and
optionally size).

[debugAssertAllPaintingVarsUnset](flutter-docs://api/painting/debugAssertAllPaintingVarsUnset)([String](flutter-docs://api/dart-core/String) reason, {[bool](flutter-docs://api/dart-core/bool) debugDisableShadowsOverride = false}) → [bool](flutter-docs://api/dart-core/bool)
Returns true if none of the painting library debug variables have been changed.

[debugAssertAllWidgetVarsUnset](flutter-docs://api/widgets/debugAssertAllWidgetVarsUnset)([String](flutter-docs://api/dart-core/String) reason) → [bool](flutter-docs://api/dart-core/bool)
Returns true if none of the widget library debug variables have been changed.

[debugCheckCanResolveTextDirection](flutter-docs://api/painting/debugCheckCanResolveTextDirection)([TextDirection](flutter-docs://api/dart-ui/TextDirection)? direction, [String](flutter-docs://api/dart-core/String) target) → [bool](flutter-docs://api/dart-core/bool)
Asserts that a given [TextDirection](flutter-docs://api/dart-ui/TextDirection) is not null.

[debugCheckHasDirectionality](flutter-docs://api/widgets/debugCheckHasDirectionality)([BuildContext](flutter-docs://api/widgets/BuildContext) context, {[String](flutter-docs://api/dart-core/String)? why, [String](flutter-docs://api/dart-core/String)? hint, [String](flutter-docs://api/dart-core/String)? alternative}) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [Directionality](flutter-docs://api/widgets/Directionality) ancestor.

[debugCheckHasMaterial](flutter-docs://api/material/debugCheckHasMaterial)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [Material](flutter-docs://api/material/Material) ancestor within the closest
[LookupBoundary](flutter-docs://api/widgets/LookupBoundary).

[debugCheckHasMaterialLocalizations](flutter-docs://api/material/debugCheckHasMaterialLocalizations)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [Localizations](flutter-docs://api/widgets/Localizations) ancestor that contains
a [MaterialLocalizations](flutter-docs://api/material/MaterialLocalizations) delegate.

[debugCheckHasMediaQuery](flutter-docs://api/widgets/debugCheckHasMediaQuery)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [MediaQuery](flutter-docs://api/widgets/MediaQuery) ancestor.

[debugCheckHasOverlay](flutter-docs://api/widgets/debugCheckHasOverlay)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has an [Overlay](flutter-docs://api/widgets/Overlay) ancestor.

[debugCheckHasScaffold](flutter-docs://api/material/debugCheckHasScaffold)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [Scaffold](flutter-docs://api/material/Scaffold) ancestor.

[debugCheckHasScaffoldMessenger](flutter-docs://api/material/debugCheckHasScaffoldMessenger)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [ScaffoldMessenger](flutter-docs://api/material/ScaffoldMessenger) ancestor.

[debugCheckHasTable](flutter-docs://api/widgets/debugCheckHasTable)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [Table](flutter-docs://api/widgets/Table) ancestor.

[debugCheckHasWidgetsLocalizations](flutter-docs://api/widgets/debugCheckHasWidgetsLocalizations)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [bool](flutter-docs://api/dart-core/bool)
Asserts that the given context has a [Localizations](flutter-docs://api/widgets/Localizations) ancestor that contains
a [WidgetsLocalizations](flutter-docs://api/widgets/WidgetsLocalizations) delegate.

[debugChildrenHaveDuplicateKeys](flutter-docs://api/widgets/debugChildrenHaveDuplicateKeys)([Widget](flutter-docs://api/widgets/Widget) parent, [Iterable](flutter-docs://api/dart-core/Iterable)<[Widget](flutter-docs://api/widgets/Widget)> children, {[String](flutter-docs://api/dart-core/String)? message}) → [bool](flutter-docs://api/dart-core/bool)
Asserts if the given child list contains any duplicate non-null keys.

[debugDescribeFocusTree](flutter-docs://api/widgets/debugDescribeFocusTree)() → [String](flutter-docs://api/dart-core/String)
Returns a text representation of the current focus tree, along with the
current attributes on each node.

[debugDescribeTransform](flutter-docs://api/painting/debugDescribeTransform)([Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4)? transform) → [List](flutter-docs://api/dart-core/List)<[String](flutter-docs://api/dart-core/String)>
Returns a list of strings representing the given transform in a format
useful for [TransformProperty](flutter-docs://api/painting/TransformProperty).

[debugDumpApp](flutter-docs://api/widgets/debugDumpApp)() → void
Print a string representation of the currently running app.

[debugDumpFocusTree](flutter-docs://api/widgets/debugDumpFocusTree)() → void
Prints a text representation of the current focus tree, along with the
current attributes on each node.

[debugDumpLayerTree](flutter-docs://api/rendering/debugDumpLayerTree)() → void
Prints a textual representation of the layer trees.

[debugDumpRenderTree](flutter-docs://api/rendering/debugDumpRenderTree)() → void
Prints a textual representation of the render trees.

[debugFlushLastFrameImageSizeInfo](flutter-docs://api/painting/debugFlushLastFrameImageSizeInfo)() → void
Flushes inter-frame tracking of image size information from [paintImage](flutter-docs://api/painting/paintImage).

[debugIsLocalCreationLocation](flutter-docs://api/widgets/debugIsLocalCreationLocation)([Object](flutter-docs://api/dart-core/Object) object) → [bool](flutter-docs://api/dart-core/bool)
Returns if an object is user created.

[debugIsWidgetLocalCreation](flutter-docs://api/widgets/debugIsWidgetLocalCreation)([Widget](flutter-docs://api/widgets/Widget) widget) → [bool](flutter-docs://api/dart-core/bool)
Returns true if a [Widget](flutter-docs://api/widgets/Widget) is user created.

[debugItemsHaveDuplicateKeys](flutter-docs://api/widgets/debugItemsHaveDuplicateKeys)([Iterable](flutter-docs://api/dart-core/Iterable)<[Widget](flutter-docs://api/widgets/Widget)> items) → [bool](flutter-docs://api/dart-core/bool)
Asserts if the given list of items contains any duplicate non-null keys.

[debugPrintStack](flutter-docs://api/foundation/debugPrintStack)({[StackTrace](flutter-docs://api/dart-core/StackTrace)? stackTrace, [String](flutter-docs://api/dart-core/String)? label, [int](flutter-docs://api/dart-core/int)? maxFrames}) → void
Dump the stack to the console using [debugPrint](flutter-docs://api/rendering/debugPrint) and
[FlutterError.defaultStackFilter](flutter-docs://api/foundation/FlutterError/defaultStackFilter).

[debugTransformDebugCreator](flutter-docs://api/widgets/debugTransformDebugCreator)([Iterable](flutter-docs://api/dart-core/Iterable)<[DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)> properties) → [Iterable](flutter-docs://api/dart-core/Iterable)<[DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)>
Transformer to parse and gather information about [DiagnosticsDebugCreator](flutter-docs://api/rendering/DiagnosticsDebugCreator).

[debugWidgetBuilderValue](flutter-docs://api/widgets/debugWidgetBuilderValue)([Widget](flutter-docs://api/widgets/Widget) widget, [Widget](flutter-docs://api/widgets/Widget)? built) → void
Asserts that the `built` widget is not null.

[decodeImageFromList](flutter-docs://api/painting/decodeImageFromList)([Uint8List](flutter-docs://api/dart-typed_data/Uint8List) bytes) → [Future](flutter-docs://api/dart-async/Future)<[Image](flutter-docs://api/dart-ui/Image)>
Creates an image from a list of bytes.

[defaultScrollNotificationPredicate](flutter-docs://api/widgets/defaultScrollNotificationPredicate)([ScrollNotification](flutter-docs://api/widgets/ScrollNotification) notification) → [bool](flutter-docs://api/dart-core/bool)
A [ScrollNotificationPredicate](flutter-docs://api/widgets/ScrollNotificationPredicate) that checks whether
`notification.depth == 0`, which means that the notification did not bubble
through any intervening scrolling widgets.

[flipAxis](flutter-docs://api/painting/flipAxis)([Axis](flutter-docs://api/painting/Axis) direction) → [Axis](flutter-docs://api/painting/Axis)
Returns the opposite of the given [Axis](flutter-docs://api/painting/Axis).

[flipAxisDirection](flutter-docs://api/painting/flipAxisDirection)([AxisDirection](flutter-docs://api/painting/AxisDirection) axisDirection) → [AxisDirection](flutter-docs://api/painting/AxisDirection)
Returns the opposite of the given [AxisDirection](flutter-docs://api/painting/AxisDirection).

[getAxisDirectionFromAxisReverseAndDirectionality](flutter-docs://api/widgets/getAxisDirectionFromAxisReverseAndDirectionality)([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Axis](flutter-docs://api/painting/Axis) axis, [bool](flutter-docs://api/dart-core/bool) reverse) → [AxisDirection](flutter-docs://api/painting/AxisDirection)
Returns the [AxisDirection](flutter-docs://api/painting/AxisDirection) in the given [Axis](flutter-docs://api/painting/Axis) in the current
[Directionality](flutter-docs://api/widgets/Directionality) (or the reverse if `reverse` is true).

[hourFormat](flutter-docs://api/material/hourFormat)({required [TimeOfDayFormat](flutter-docs://api/material/TimeOfDayFormat) of}) → [HourFormat](flutter-docs://api/material/HourFormat)
The [HourFormat](flutter-docs://api/material/HourFormat) used for the given [TimeOfDayFormat](flutter-docs://api/material/TimeOfDayFormat).

[intentForMacOSSelector](flutter-docs://api/widgets/intentForMacOSSelector)([String](flutter-docs://api/dart-core/String) selectorName) → [Intent](flutter-docs://api/widgets/Intent)?
Maps the selector from NSStandardKeyBindingResponding to the Intent if the
selector is recognized.

[lerpFontVariations](flutter-docs://api/painting/lerpFontVariations)([List](flutter-docs://api/dart-core/List)<[FontVariation](flutter-docs://api/dart-ui/FontVariation)>? a, [List](flutter-docs://api/dart-core/List)<[FontVariation](flutter-docs://api/dart-ui/FontVariation)>? b, [double](flutter-docs://api/dart-core/double) t) → [List](flutter-docs://api/dart-core/List)<[FontVariation](flutter-docs://api/dart-ui/FontVariation)>?
Interpolate between two lists of [FontVariation](flutter-docs://api/dart-ui/FontVariation) objects.

[paintBorder](flutter-docs://api/painting/paintBorder)([Canvas](flutter-docs://api/dart-ui/Canvas) canvas, [Rect](flutter-docs://api/dart-ui/Rect) rect, {[BorderSide](flutter-docs://api/painting/BorderSide) top = BorderSide.none, [BorderSide](flutter-docs://api/painting/BorderSide) right = BorderSide.none, [BorderSide](flutter-docs://api/painting/BorderSide) bottom = BorderSide.none, [BorderSide](flutter-docs://api/painting/BorderSide) left = BorderSide.none}) → void
Paints a border around the given rectangle on the canvas.

[paintImage](flutter-docs://api/painting/paintImage)({required [Canvas](flutter-docs://api/dart-ui/Canvas) canvas, required [Rect](flutter-docs://api/dart-ui/Rect) rect, required [Image](flutter-docs://api/dart-ui/Image) image, [String](flutter-docs://api/dart-core/String)? debugImageLabel, [double](flutter-docs://api/dart-core/double) scale = 1.0, [double](flutter-docs://api/dart-core/double) opacity = 1.0, [ColorFilter](flutter-docs://api/dart-ui/ColorFilter)? colorFilter, [BoxFit](flutter-docs://api/painting/BoxFit)? fit, [Alignment](flutter-docs://api/painting/Alignment) alignment = Alignment.center, [Rect](flutter-docs://api/dart-ui/Rect)? centerSlice, [ImageRepeat](flutter-docs://api/painting/ImageRepeat) repeat = ImageRepeat.noRepeat, [bool](flutter-docs://api/dart-core/bool) flipHorizontally = false, [bool](flutter-docs://api/dart-core/bool) invertColors = false, [FilterQuality](flutter-docs://api/dart-ui/FilterQuality) filterQuality = FilterQuality.medium, [bool](flutter-docs://api/dart-core/bool) isAntiAlias = false, [BlendMode](flutter-docs://api/dart-ui/BlendMode) blendMode = BlendMode.srcOver}) → void
Paints an image into the given rectangle on the canvas.

[paintZigZag](flutter-docs://api/painting/paintZigZag)([Canvas](flutter-docs://api/dart-ui/Canvas) canvas, [Paint](flutter-docs://api/dart-ui/Paint) paint, [Offset](flutter-docs://api/dart-ui/Offset) start, [Offset](flutter-docs://api/dart-ui/Offset) end, [int](flutter-docs://api/dart-core/int) zigs, [double](flutter-docs://api/dart-core/double) width) → void
Draw a line between two points, which cuts diagonally back and forth across
the line that connects the two points.

[pointerDragAnchorStrategy](flutter-docs://api/widgets/pointerDragAnchorStrategy)([Draggable](flutter-docs://api/widgets/Draggable)<[Object](flutter-docs://api/dart-core/Object)> draggable, [BuildContext](flutter-docs://api/widgets/BuildContext) context, [Offset](flutter-docs://api/dart-ui/Offset) position) → [Offset](flutter-docs://api/dart-ui/Offset)
Display the feedback anchored at the position of the touch that started
the drag.

[positionDependentBox](flutter-docs://api/painting/positionDependentBox)({required [Size](flutter-docs://api/dart-ui/Size) size, required [Size](flutter-docs://api/dart-ui/Size) childSize, required [Offset](flutter-docs://api/dart-ui/Offset) target, required [bool](flutter-docs://api/dart-core/bool) preferBelow, [double](flutter-docs://api/dart-core/double) verticalOffset = 0.0, [double](flutter-docs://api/dart-core/double) margin = 10.0}) → [Offset](flutter-docs://api/dart-ui/Offset)
Position a child box within a container box, either above or below a target
point.

[precacheImage](flutter-docs://api/widgets/precacheImage)([ImageProvider](flutter-docs://api/painting/ImageProvider)<[Object](flutter-docs://api/dart-core/Object)> provider, [BuildContext](flutter-docs://api/widgets/BuildContext) context, {[Size](flutter-docs://api/dart-ui/Size)? size, [ImageErrorListener](flutter-docs://api/painting/ImageErrorListener)? onError}) → [Future](flutter-docs://api/dart-async/Future)<void>
Prefetches an image into the image cache.

[runApp](flutter-docs://api/widgets/runApp)([Widget](flutter-docs://api/widgets/Widget) app) → void
Inflate the given widget and attach it to the view.

[runWidget](flutter-docs://api/widgets/runWidget)([Widget](flutter-docs://api/widgets/Widget) app) → void
Inflate the given widget and bootstrap the widget tree.

[showAboutDialog](flutter-docs://api/material/showAboutDialog)({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, [String](flutter-docs://api/dart-core/String)? applicationName, [String](flutter-docs://api/dart-core/String)? applicationVersion, [Widget](flutter-docs://api/widgets/Widget)? applicationIcon, [String](flutter-docs://api/dart-core/String)? applicationLegalese, [List](flutter-docs://api/dart-core/List)<[Widget](flutter-docs://api/widgets/Widget)>? children, [bool](flutter-docs://api/dart-core/bool) barrierDismissible = true, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint}) → void
Displays an [AboutDialog](flutter-docs://api/material/AboutDialog), which describes the application and provides a
button to show licenses for software used by the application.

[showAdaptiveAboutDialog](flutter-docs://api/material/showAdaptiveAboutDialog)({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, [String](flutter-docs://api/dart-core/String)? applicationName, [String](flutter-docs://api/dart-core/String)? applicationVersion, [Widget](flutter-docs://api/widgets/Widget)? applicationIcon, [String](flutter-docs://api/dart-core/String)? applicationLegalese, [List](flutter-docs://api/dart-core/List)<[Widget](flutter-docs://api/widgets/Widget)>? children, [bool](flutter-docs://api/dart-core/bool) barrierDismissible = true, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint}) → void
Displays either a Material or Cupertino [AboutDialog](flutter-docs://api/material/AboutDialog) depending on platform,
which describes the application and provides a button to show licenses
for software used by the application.

[showAdaptiveDialog](flutter-docs://api/material/showAdaptiveDialog)<T>({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, required [WidgetBuilder](flutter-docs://api/widgets/WidgetBuilder) builder, [bool](flutter-docs://api/dart-core/bool)? barrierDismissible, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [bool](flutter-docs://api/dart-core/bool) useSafeArea = true, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint, [TraversalEdgeBehavior](flutter-docs://api/widgets/TraversalEdgeBehavior)? traversalEdgeBehavior, [bool](flutter-docs://api/dart-core/bool)? requestFocus, [AnimationStyle](flutter-docs://api/animation/AnimationStyle)? animationStyle}) → [Future](flutter-docs://api/dart-async/Future)<T?>
Displays either a Material or Cupertino dialog depending on platform.

[showBottomSheet](flutter-docs://api/material/showBottomSheet)({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, required [WidgetBuilder](flutter-docs://api/widgets/WidgetBuilder) builder, [Color](flutter-docs://api/dart-ui/Color)? backgroundColor, [double](flutter-docs://api/dart-core/double)? elevation, [ShapeBorder](flutter-docs://api/painting/ShapeBorder)? shape, [Clip](flutter-docs://api/dart-ui/Clip)? clipBehavior, [BoxConstraints](flutter-docs://api/rendering/BoxConstraints)? constraints, [bool](flutter-docs://api/dart-core/bool)? enableDrag, [bool](flutter-docs://api/dart-core/bool)? showDragHandle, [AnimationController](flutter-docs://api/animation/AnimationController)? transitionAnimationController, [AnimationStyle](flutter-docs://api/animation/AnimationStyle)? sheetAnimationStyle}) → [PersistentBottomSheetController](flutter-docs://api/material/PersistentBottomSheetController)
Shows a Material Design bottom sheet in the nearest [Scaffold](flutter-docs://api/material/Scaffold) ancestor. To
show a persistent bottom sheet, use the [Scaffold.bottomSheet](flutter-docs://api/material/Scaffold/bottomSheet).

[showDatePicker](flutter-docs://api/material/showDatePicker)({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, [DateTime](flutter-docs://api/dart-core/DateTime)? initialDate, required [DateTime](flutter-docs://api/dart-core/DateTime) firstDate, required [DateTime](flutter-docs://api/dart-core/DateTime) lastDate, [DateTime](flutter-docs://api/dart-core/DateTime)? currentDate, [DatePickerEntryMode](flutter-docs://api/material/DatePickerEntryMode) initialEntryMode = DatePickerEntryMode.calendar, [SelectableDayPredicate](flutter-docs://api/widgets/SelectableDayPredicate)? selectableDayPredicate, [String](flutter-docs://api/dart-core/String)? helpText, [String](flutter-docs://api/dart-core/String)? cancelText, [String](flutter-docs://api/dart-core/String)? confirmText, [Locale](flutter-docs://api/dart-ui/Locale)? locale, [bool](flutter-docs://api/dart-core/bool) barrierDismissible = true, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [TextDirection](flutter-docs://api/dart-ui/TextDirection)? textDirection, [TransitionBuilder](flutter-docs://api/widgets/TransitionBuilder)? builder, [DatePickerMode](flutter-docs://api/material/DatePickerMode) initialDatePickerMode = DatePickerMode.day, [String](flutter-docs://api/dart-core/String)? errorFormatText, [String](flutter-docs://api/dart-core/String)? errorInvalidText, [String](flutter-docs://api/dart-core/String)? fieldHintText, [String](flutter-docs://api/dart-core/String)? fieldLabelText, [TextInputType](flutter-docs://api/services/TextInputType)? keyboardType, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint, [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[DatePickerEntryMode](flutter-docs://api/material/DatePickerEntryMode)>? onDatePickerModeChange, [Icon](flutter-docs://api/widgets/Icon)? switchToInputEntryModeIcon, [Icon](flutter-docs://api/widgets/Icon)? switchToCalendarEntryModeIcon, [CalendarDelegate](flutter-docs://api/material/CalendarDelegate)<[DateTime](flutter-docs://api/dart-core/DateTime)> calendarDelegate = const GregorianCalendarDelegate()}) → [Future](flutter-docs://api/dart-async/Future)<[DateTime](flutter-docs://api/dart-core/DateTime)?>
Shows a dialog containing a Material Design date picker.

[showDateRangePicker](flutter-docs://api/material/showDateRangePicker)({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, [DateTimeRange](flutter-docs://api/material/DateTimeRange)<[DateTime](flutter-docs://api/dart-core/DateTime)>? initialDateRange, required [DateTime](flutter-docs://api/dart-core/DateTime) firstDate, required [DateTime](flutter-docs://api/dart-core/DateTime) lastDate, [DateTime](flutter-docs://api/dart-core/DateTime)? currentDate, [DatePickerEntryMode](flutter-docs://api/material/DatePickerEntryMode) initialEntryMode = DatePickerEntryMode.calendar, [String](flutter-docs://api/dart-core/String)? helpText, [String](flutter-docs://api/dart-core/String)? cancelText, [String](flutter-docs://api/dart-core/String)? confirmText, [String](flutter-docs://api/dart-core/String)? saveText, [String](flutter-docs://api/dart-core/String)? errorFormatText, [String](flutter-docs://api/dart-core/String)? errorInvalidText, [String](flutter-docs://api/dart-core/String)? errorInvalidRangeText, [String](flutter-docs://api/dart-core/String)? fieldStartHintText, [String](flutter-docs://api/dart-core/String)? fieldEndHintText, [String](flutter-docs://api/dart-core/String)? fieldStartLabelText, [String](flutter-docs://api/dart-core/String)? fieldEndLabelText, [Locale](flutter-docs://api/dart-ui/Locale)? locale, [bool](flutter-docs://api/dart-core/bool) barrierDismissible = true, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [TextDirection](flutter-docs://api/dart-ui/TextDirection)? textDirection, [TransitionBuilder](flutter-docs://api/widgets/TransitionBuilder)? builder, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint, [TextInputType](flutter-docs://api/services/TextInputType) keyboardType = TextInputType.datetime, [Icon](flutter-docs://api/widgets/Icon)? switchToInputEntryModeIcon, [Icon](flutter-docs://api/widgets/Icon)? switchToCalendarEntryModeIcon, [SelectableDayForRangePredicate](flutter-docs://api/material/SelectableDayForRangePredicate)? selectableDayPredicate, [CalendarDelegate](flutter-docs://api/material/CalendarDelegate)<[DateTime](flutter-docs://api/dart-core/DateTime)> calendarDelegate = const GregorianCalendarDelegate()}) → [Future](flutter-docs://api/dart-async/Future)<[DateTimeRange](flutter-docs://api/material/DateTimeRange)<[DateTime](flutter-docs://api/dart-core/DateTime)>?>
Shows a full screen modal dialog containing a Material Design date range
picker.

[showDialog](flutter-docs://api/material/showDialog)<T>({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, required [WidgetBuilder](flutter-docs://api/widgets/WidgetBuilder) builder, [bool](flutter-docs://api/dart-core/bool) barrierDismissible = true, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [bool](flutter-docs://api/dart-core/bool) useSafeArea = true, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint, [TraversalEdgeBehavior](flutter-docs://api/widgets/TraversalEdgeBehavior)? traversalEdgeBehavior, [bool](flutter-docs://api/dart-core/bool) fullscreenDialog = false, [bool](flutter-docs://api/dart-core/bool)? requestFocus, [AnimationStyle](flutter-docs://api/animation/AnimationStyle)? animationStyle}) → [Future](flutter-docs://api/dart-async/Future)<T?>
Displays a Material dialog above the current contents of the app, with
Material entrance and exit animations, modal barrier color, and modal
barrier behavior (dialog is dismissible with a tap on the barrier).

[showGeneralDialog](flutter-docs://api/widgets/showGeneralDialog)<T extends [Object](flutter-docs://api/dart-core/Object)?>({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, required [RoutePageBuilder](flutter-docs://api/widgets/RoutePageBuilder) pageBuilder, [bool](flutter-docs://api/dart-core/bool) barrierDismissible = false, [String](flutter-docs://api/dart-core/String)? barrierLabel, [Color](flutter-docs://api/dart-ui/Color) barrierColor = const Color(0x80000000), [Duration](flutter-docs://api/dart-core/Duration) transitionDuration = const Duration(milliseconds: 200), [RouteTransitionsBuilder](flutter-docs://api/widgets/RouteTransitionsBuilder)? transitionBuilder, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [bool](flutter-docs://api/dart-core/bool) fullscreenDialog = false, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint, [bool](flutter-docs://api/dart-core/bool)? requestFocus}) → [Future](flutter-docs://api/dart-async/Future)<T?>
Displays a dialog above the current contents of the app.

[showLicensePage](flutter-docs://api/material/showLicensePage)({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, [String](flutter-docs://api/dart-core/String)? applicationName, [String](flutter-docs://api/dart-core/String)? applicationVersion, [Widget](flutter-docs://api/widgets/Widget)? applicationIcon, [String](flutter-docs://api/dart-core/String)? applicationLegalese, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = false}) → void
Displays a [LicensePage](flutter-docs://api/material/LicensePage), which shows licenses for software used by the
application.

[showMenu](flutter-docs://api/material/showMenu)<T>({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, [RelativeRect](flutter-docs://api/rendering/RelativeRect)? position, [PopupMenuPositionBuilder](flutter-docs://api/material/PopupMenuPositionBuilder)? positionBuilder, required [List](flutter-docs://api/dart-core/List)<[PopupMenuEntry](flutter-docs://api/material/PopupMenuEntry)<T>> items, T? initialValue, [double](flutter-docs://api/dart-core/double)? elevation, [Color](flutter-docs://api/dart-ui/Color)? shadowColor, [Color](flutter-docs://api/dart-ui/Color)? surfaceTintColor, [String](flutter-docs://api/dart-core/String)? semanticLabel, [ShapeBorder](flutter-docs://api/painting/ShapeBorder)? shape, [EdgeInsetsGeometry](flutter-docs://api/painting/EdgeInsetsGeometry)? menuPadding, [Color](flutter-docs://api/dart-ui/Color)? color, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = false, [BoxConstraints](flutter-docs://api/rendering/BoxConstraints)? constraints, [Clip](flutter-docs://api/dart-ui/Clip) clipBehavior = Clip.none, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [AnimationStyle](flutter-docs://api/animation/AnimationStyle)? popUpAnimationStyle, [bool](flutter-docs://api/dart-core/bool)? requestFocus}) → [Future](flutter-docs://api/dart-async/Future)<T?>
Shows a popup menu that contains the `items` at `position`.

[showModalBottomSheet](flutter-docs://api/material/showModalBottomSheet)<T>({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, required [WidgetBuilder](flutter-docs://api/widgets/WidgetBuilder) builder, [Color](flutter-docs://api/dart-ui/Color)? backgroundColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [double](flutter-docs://api/dart-core/double)? elevation, [ShapeBorder](flutter-docs://api/painting/ShapeBorder)? shape, [Clip](flutter-docs://api/dart-ui/Clip)? clipBehavior, [BoxConstraints](flutter-docs://api/rendering/BoxConstraints)? constraints, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [bool](flutter-docs://api/dart-core/bool) isScrollControlled = false, [double](flutter-docs://api/dart-core/double) scrollControlDisabledMaxHeightRatio = _defaultScrollControlDisabledMaxHeightRatio, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = false, [bool](flutter-docs://api/dart-core/bool) isDismissible = true, [bool](flutter-docs://api/dart-core/bool) enableDrag = true, [bool](flutter-docs://api/dart-core/bool)? showDragHandle, [bool](flutter-docs://api/dart-core/bool) useSafeArea = false, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [AnimationController](flutter-docs://api/animation/AnimationController)? transitionAnimationController, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint, [AnimationStyle](flutter-docs://api/animation/AnimationStyle)? sheetAnimationStyle, [bool](flutter-docs://api/dart-core/bool)? requestFocus}) → [Future](flutter-docs://api/dart-async/Future)<T?>
Shows a modal Material Design bottom sheet.

[showSearch](flutter-docs://api/material/showSearch)<T>({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, required [SearchDelegate](flutter-docs://api/material/SearchDelegate)<T> delegate, [String](flutter-docs://api/dart-core/String)? query = '', [bool](flutter-docs://api/dart-core/bool) useRootNavigator = false, [bool](flutter-docs://api/dart-core/bool) maintainState = false}) → [Future](flutter-docs://api/dart-async/Future)<T?>
Shows a full screen search page and returns the search result selected by
the user when the page is closed.

[showTimePicker](flutter-docs://api/material/showTimePicker)({required [BuildContext](flutter-docs://api/widgets/BuildContext) context, required [TimeOfDay](flutter-docs://api/material/TimeOfDay) initialTime, [TransitionBuilder](flutter-docs://api/widgets/TransitionBuilder)? builder, [bool](flutter-docs://api/dart-core/bool) barrierDismissible = true, [Color](flutter-docs://api/dart-ui/Color)? barrierColor, [String](flutter-docs://api/dart-core/String)? barrierLabel, [bool](flutter-docs://api/dart-core/bool) useRootNavigator = true, [TimePickerEntryMode](flutter-docs://api/material/TimePickerEntryMode) initialEntryMode = TimePickerEntryMode.dial, [String](flutter-docs://api/dart-core/String)? cancelText, [String](flutter-docs://api/dart-core/String)? confirmText, [String](flutter-docs://api/dart-core/String)? helpText, [String](flutter-docs://api/dart-core/String)? errorInvalidText, [String](flutter-docs://api/dart-core/String)? hourLabelText, [String](flutter-docs://api/dart-core/String)? minuteLabelText, [RouteSettings](flutter-docs://api/widgets/RouteSettings)? routeSettings, [EntryModeChangeCallback](flutter-docs://api/material/EntryModeChangeCallback)? onEntryModeChanged, [Offset](flutter-docs://api/dart-ui/Offset)? anchorPoint, [Orientation](flutter-docs://api/widgets/Orientation)? orientation, [Icon](flutter-docs://api/widgets/Icon)? switchToInputEntryModeIcon, [Icon](flutter-docs://api/widgets/Icon)? switchToTimerEntryModeIcon, [bool](flutter-docs://api/dart-core/bool) emptyInitialInput = false}) → [Future](flutter-docs://api/dart-async/Future)<[TimeOfDay](flutter-docs://api/material/TimeOfDay)?>
Shows a dialog containing a Material Design time picker.

[textDirectionToAxisDirection](flutter-docs://api/painting/textDirectionToAxisDirection)([TextDirection](flutter-docs://api/dart-ui/TextDirection) textDirection) → [AxisDirection](flutter-docs://api/painting/AxisDirection)
Returns the [AxisDirection](flutter-docs://api/painting/AxisDirection) in which reading occurs in the given [TextDirection](flutter-docs://api/dart-ui/TextDirection).

## Typedefs

[ActionListenerCallback](flutter-docs://api/widgets/ActionListenerCallback) = void Function([Action](flutter-docs://api/widgets/Action)<[Intent](flutter-docs://api/widgets/Intent)> action)
The kind of callback that an [Action](flutter-docs://api/widgets/Action) uses to notify of changes to the
action's state.

[AnimatableCallback](flutter-docs://api/animation/AnimatableCallback)<T> = T Function([double](flutter-docs://api/dart-core/double) value)
A typedef used by [Animatable.fromCallback](flutter-docs://api/animation/Animatable/Animatable.fromCallback) to create an [Animatable](flutter-docs://api/animation/Animatable) from a callback.

[AnimatedCrossFadeBuilder](flutter-docs://api/widgets/AnimatedCrossFadeBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([Widget](flutter-docs://api/widgets/Widget) topChild, [Key](flutter-docs://api/foundation/Key) topChildKey, [Widget](flutter-docs://api/widgets/Widget) bottomChild, [Key](flutter-docs://api/foundation/Key) bottomChildKey)
Signature for the [AnimatedCrossFade.layoutBuilder](flutter-docs://api/widgets/AnimatedCrossFade/layoutBuilder) callback.

[AnimatedItemBuilder](flutter-docs://api/widgets/AnimatedItemBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [int](flutter-docs://api/dart-core/int) index, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation)
Signature for the builder callback used by [AnimatedList](flutter-docs://api/widgets/AnimatedList), [AnimatedList.separated](flutter-docs://api/widgets/AnimatedList/AnimatedList.separated) & [AnimatedGrid](flutter-docs://api/widgets/AnimatedGrid) to build their animated children.

[AnimatedRemovedItemBuilder](flutter-docs://api/widgets/AnimatedRemovedItemBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation)
Signature for the builder callback used in `AnimatedListState.removeItem` and
`AnimatedGridState.removeItem` to animate their children after they have
been removed.

[AnimatedSwitcherLayoutBuilder](flutter-docs://api/widgets/AnimatedSwitcherLayoutBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([Widget](flutter-docs://api/widgets/Widget)? currentChild, [List](flutter-docs://api/dart-core/List)<[Widget](flutter-docs://api/widgets/Widget)> previousChildren)
Signature for builders used to generate custom layouts for
[AnimatedSwitcher](flutter-docs://api/widgets/AnimatedSwitcher).

[AnimatedSwitcherTransitionBuilder](flutter-docs://api/widgets/AnimatedSwitcherTransitionBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([Widget](flutter-docs://api/widgets/Widget) child, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation)
Signature for builders used to generate custom transitions for
[AnimatedSwitcher](flutter-docs://api/widgets/AnimatedSwitcher).

[AnimatedTransitionBuilder](flutter-docs://api/widgets/AnimatedTransitionBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation, [Widget](flutter-docs://api/widgets/Widget)? child)
Builder callback used by [DualTransitionBuilder](flutter-docs://api/widgets/DualTransitionBuilder).

[AnimationStatusListener](flutter-docs://api/animation/AnimationStatusListener) = void Function([AnimationStatus](flutter-docs://api/animation/AnimationStatus) status)
Signature for listeners attached using [Animation.addStatusListener](flutter-docs://api/animation/Animation/addStatusListener).

[AppExitRequestCallback](flutter-docs://api/widgets/AppExitRequestCallback) = [Future](flutter-docs://api/dart-async/Future)<[AppExitResponse](flutter-docs://api/dart-ui/AppExitResponse)> Function()
A callback type that is used by [AppLifecycleListener.onExitRequested](flutter-docs://api/widgets/AppLifecycleListener/onExitRequested) to
ask the application if it wants to cancel application termination or not.

[AppPrivateCommandCallback](flutter-docs://api/widgets/AppPrivateCommandCallback) = void Function([String](flutter-docs://api/dart-core/String) action, [Map](flutter-docs://api/dart-core/Map)<[String](flutter-docs://api/dart-core/String), dynamic> data)
Signature for the callback that reports the app private command results.

[AsyncWidgetBuilder](flutter-docs://api/widgets/AsyncWidgetBuilder)<T> = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [AsyncSnapshot](flutter-docs://api/widgets/AsyncSnapshot)<T> snapshot)
Signature for strategies that build widgets based on asynchronous
interaction.

[AutocompleteFieldViewBuilder](flutter-docs://api/widgets/AutocompleteFieldViewBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [TextEditingController](flutter-docs://api/widgets/TextEditingController) textEditingController, [FocusNode](flutter-docs://api/widgets/FocusNode) focusNode, [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) onFieldSubmitted)
The type of the Autocomplete callback which returns the widget that
contains the input [TextField](flutter-docs://api/material/TextField) or [TextFormField](flutter-docs://api/material/TextFormField).

[AutocompleteOnSelected](flutter-docs://api/widgets/AutocompleteOnSelected)<T extends [Object](flutter-docs://api/dart-core/Object)> = void Function(T option)
The type of the callback used by the [RawAutocomplete](flutter-docs://api/widgets/RawAutocomplete) widget to indicate
that the user has selected an option.

[AutocompleteOptionsBuilder](flutter-docs://api/widgets/AutocompleteOptionsBuilder)<T extends [Object](flutter-docs://api/dart-core/Object)> = [FutureOr](flutter-docs://api/dart-async/FutureOr)<[Iterable](flutter-docs://api/dart-core/Iterable)<T>> Function([TextEditingValue](flutter-docs://api/flutter_test/TextEditingValue) textEditingValue)
The type of the [RawAutocomplete](flutter-docs://api/widgets/RawAutocomplete) callback which computes the list of
optional completions for the widget's field, based on the text the user has
entered so far.

[AutocompleteOptionsViewBuilder](flutter-docs://api/widgets/AutocompleteOptionsViewBuilder)<T extends [Object](flutter-docs://api/dart-core/Object)> = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [AutocompleteOnSelected](flutter-docs://api/widgets/AutocompleteOnSelected)<T> onSelected, [Iterable](flutter-docs://api/dart-core/Iterable)<T> options)
The type of the [RawAutocomplete](flutter-docs://api/widgets/RawAutocomplete) callback which returns a [Widget](flutter-docs://api/widgets/Widget) that
displays the specified `options` and calls `onSelected` if the user
selects an option.

[AutocompleteOptionToString](flutter-docs://api/widgets/AutocompleteOptionToString)<T extends [Object](flutter-docs://api/dart-core/Object)> = [String](flutter-docs://api/dart-core/String) Function(T option)
The type of the [RawAutocomplete](flutter-docs://api/widgets/RawAutocomplete) callback that converts an option value to
a string which can be displayed in the widget's options menu.

[BottomSheetDragEndHandler](flutter-docs://api/material/BottomSheetDragEndHandler) = void Function([DragEndDetails](flutter-docs://api/gestures/DragEndDetails) details, {required [bool](flutter-docs://api/dart-core/bool) isClosing})
A callback for when the user stops dragging the bottom sheet.

[BottomSheetDragStartHandler](flutter-docs://api/material/BottomSheetDragStartHandler) = void Function([DragStartDetails](flutter-docs://api/gestures/DragStartDetails) details)
A callback for when the user begins dragging the bottom sheet.

[BoxConstraintsTransform](flutter-docs://api/rendering/BoxConstraintsTransform) = [BoxConstraints](flutter-docs://api/rendering/BoxConstraints) Function([BoxConstraints](flutter-docs://api/rendering/BoxConstraints) constraints)
Signature for a function that transforms a [BoxConstraints](flutter-docs://api/rendering/BoxConstraints) to another
[BoxConstraints](flutter-docs://api/rendering/BoxConstraints).

[ButtonLayerBuilder](flutter-docs://api/material/ButtonLayerBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Set](flutter-docs://api/dart-core/Set)<[WidgetState](flutter-docs://api/widgets/WidgetState)> states, [Widget](flutter-docs://api/widgets/Widget)? child)
The type for [ButtonStyle.backgroundBuilder](flutter-docs://api/material/ButtonStyle/backgroundBuilder) and [ButtonStyle.foregroundBuilder](flutter-docs://api/material/ButtonStyle/foregroundBuilder).

[ChildIndexGetter](flutter-docs://api/widgets/ChildIndexGetter) = [int](flutter-docs://api/dart-core/int)? Function([Key](flutter-docs://api/foundation/Key) key)
Called to find the new index of a child based on its `key` in case of
reordering.

[ConditionalElementVisitor](flutter-docs://api/widgets/ConditionalElementVisitor) = [bool](flutter-docs://api/dart-core/bool) Function([Element](flutter-docs://api/widgets/Element) element)
Signature for the callback to [BuildContext.visitAncestorElements](flutter-docs://api/widgets/BuildContext/visitAncestorElements).

[ConfirmDismissCallback](flutter-docs://api/widgets/ConfirmDismissCallback) = [Future](flutter-docs://api/dart-async/Future)<[bool](flutter-docs://api/dart-core/bool)?> Function([DismissDirection](flutter-docs://api/widgets/DismissDirection) direction)
Signature used by [Dismissible](flutter-docs://api/widgets/Dismissible) to give the application an opportunity to
confirm or veto a dismiss gesture.

[ControlsWidgetBuilder](flutter-docs://api/material/ControlsWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [ControlsDetails](flutter-docs://api/material/ControlsDetails) details)
A builder that creates a widget given the two callbacks `onStepContinue` and
`onStepCancel`.

[CreatePlatformViewCallback](flutter-docs://api/widgets/CreatePlatformViewCallback) = [PlatformViewController](flutter-docs://api/services/PlatformViewController) Function([PlatformViewCreationParams](flutter-docs://api/widgets/PlatformViewCreationParams) params)
Constructs a [PlatformViewController](flutter-docs://api/services/PlatformViewController).

[CreateRectTween](flutter-docs://api/widgets/CreateRectTween) = [Tween](flutter-docs://api/animation/Tween)<[Rect](flutter-docs://api/dart-ui/Rect)?> Function([Rect](flutter-docs://api/dart-ui/Rect)? begin, [Rect](flutter-docs://api/dart-ui/Rect)? end)
Signature for a function that takes two [Rect](flutter-docs://api/dart-ui/Rect) instances and returns a
[RectTween](flutter-docs://api/animation/RectTween) that transitions between them.

[DataColumnSortCallback](flutter-docs://api/material/DataColumnSortCallback) = void Function([int](flutter-docs://api/dart-core/int) columnIndex, [bool](flutter-docs://api/dart-core/bool) ascending)
Signature for [DataColumn.onSort](flutter-docs://api/material/DataColumn/onSort) callback.

[DecoderBufferCallback](flutter-docs://api/painting/DecoderBufferCallback) = [Future](flutter-docs://api/dart-async/Future)<[Codec](flutter-docs://api/dart-ui/Codec)> Function([ImmutableBuffer](flutter-docs://api/dart-ui/ImmutableBuffer) buffer, {[bool](flutter-docs://api/dart-core/bool) allowUpscaling, [int](flutter-docs://api/dart-core/int)? cacheHeight, [int](flutter-docs://api/dart-core/int)? cacheWidth})
Performs the decode process for use in [ImageProvider.loadBuffer](flutter-docs://api/painting/ImageProvider/loadBuffer).

[DelegatedTransitionBuilder](flutter-docs://api/widgets/DelegatedTransitionBuilder) = [Widget](flutter-docs://api/widgets/Widget)? Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> secondaryAnimation, [bool](flutter-docs://api/dart-core/bool) allowSnapshotting, [Widget](flutter-docs://api/widgets/Widget)? child)
Signature for a builder used to control a page's exit transition.

[DidRemovePageCallback](flutter-docs://api/widgets/DidRemovePageCallback) = void Function([Page](flutter-docs://api/widgets/Page)<[Object](flutter-docs://api/dart-core/Object)?> page)
Signature for the [Navigator.onDidRemovePage](flutter-docs://api/widgets/Navigator/onDidRemovePage) callback.

[DismissDirectionCallback](flutter-docs://api/widgets/DismissDirectionCallback) = void Function([DismissDirection](flutter-docs://api/widgets/DismissDirection) direction)
Signature used by [Dismissible](flutter-docs://api/widgets/Dismissible) to indicate that it has been dismissed in
the given `direction`.

[DismissUpdateCallback](flutter-docs://api/widgets/DismissUpdateCallback) = void Function([DismissUpdateDetails](flutter-docs://api/widgets/DismissUpdateDetails) details)
Signature used by [Dismissible](flutter-docs://api/widgets/Dismissible) to indicate that the dismissible has been dragged.

[DragAnchorStrategy](flutter-docs://api/widgets/DragAnchorStrategy) = [Offset](flutter-docs://api/dart-ui/Offset) Function([Draggable](flutter-docs://api/widgets/Draggable)<[Object](flutter-docs://api/dart-core/Object)> draggable, [BuildContext](flutter-docs://api/widgets/BuildContext) context, [Offset](flutter-docs://api/dart-ui/Offset) position)
Signature for the strategy that determines the drag start point of a [Draggable](flutter-docs://api/widgets/Draggable).

[DragEndCallback](flutter-docs://api/widgets/DragEndCallback) = void Function([DraggableDetails](flutter-docs://api/widgets/DraggableDetails) details)
Signature for when the draggable is dropped.

[DraggableCanceledCallback](flutter-docs://api/widgets/DraggableCanceledCallback) = void Function([Velocity](flutter-docs://api/gestures/Velocity) velocity, [Offset](flutter-docs://api/dart-ui/Offset) offset)
Signature for when a [Draggable](flutter-docs://api/widgets/Draggable) is dropped without being accepted by a [DragTarget](flutter-docs://api/widgets/DragTarget).

[DragTargetAccept](flutter-docs://api/widgets/DragTargetAccept)<T> = void Function(T data)
Signature for causing a [DragTarget](flutter-docs://api/widgets/DragTarget) to accept the given data.

[DragTargetAcceptWithDetails](flutter-docs://api/widgets/DragTargetAcceptWithDetails)<T> = void Function([DragTargetDetails](flutter-docs://api/widgets/DragTargetDetails)<T> details)
Signature for determining information about the acceptance by a [DragTarget](flutter-docs://api/widgets/DragTarget).

[DragTargetBuilder](flutter-docs://api/widgets/DragTargetBuilder)<T> = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [List](flutter-docs://api/dart-core/List)<T?> candidateData, [List](flutter-docs://api/dart-core/List) rejectedData)
Signature for building children of a [DragTarget](flutter-docs://api/widgets/DragTarget).

[DragTargetLeave](flutter-docs://api/widgets/DragTargetLeave)<T> = void Function(T? data)
Signature for when a [Draggable](flutter-docs://api/widgets/Draggable) leaves a [DragTarget](flutter-docs://api/widgets/DragTarget).

[DragTargetMove](flutter-docs://api/widgets/DragTargetMove)<T> = void Function([DragTargetDetails](flutter-docs://api/widgets/DragTargetDetails)<T> details)
Signature for when a [Draggable](flutter-docs://api/widgets/Draggable) moves within a [DragTarget](flutter-docs://api/widgets/DragTarget).

[DragTargetWillAccept](flutter-docs://api/widgets/DragTargetWillAccept)<T> = [bool](flutter-docs://api/dart-core/bool) Function(T? data)
Signature for determining whether the given data will be accepted by a [DragTarget](flutter-docs://api/widgets/DragTarget).

[DragTargetWillAcceptWithDetails](flutter-docs://api/widgets/DragTargetWillAcceptWithDetails)<T> = [bool](flutter-docs://api/dart-core/bool) Function([DragTargetDetails](flutter-docs://api/widgets/DragTargetDetails)<T> details)
Signature for determining whether the given data will be accepted by a [DragTarget](flutter-docs://api/widgets/DragTarget),
based on provided information.

[DragUpdateCallback](flutter-docs://api/widgets/DragUpdateCallback) = void Function([DragUpdateDetails](flutter-docs://api/gestures/DragUpdateDetails) details)
Signature for when a [Draggable](flutter-docs://api/widgets/Draggable) is dragged across the screen.

[DrawerCallback](flutter-docs://api/material/DrawerCallback) = void Function([bool](flutter-docs://api/dart-core/bool) isOpened)
Signature for the callback that's called when a [DrawerController](flutter-docs://api/material/DrawerController) is
opened or closed.

[DropdownButtonBuilder](flutter-docs://api/material/DropdownButtonBuilder) = [List](flutter-docs://api/dart-core/List)<[Widget](flutter-docs://api/widgets/Widget)> Function([BuildContext](flutter-docs://api/widgets/BuildContext) context)
A builder to customize dropdown buttons.

[EditableTextContextMenuBuilder](flutter-docs://api/widgets/EditableTextContextMenuBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [EditableTextState](flutter-docs://api/widgets/EditableTextState) editableTextState)
Signature for a widget builder that builds a context menu for the given
[EditableTextState](flutter-docs://api/widgets/EditableTextState).

[ElementCreatedCallback](flutter-docs://api/widgets/ElementCreatedCallback) = void Function([Object](flutter-docs://api/dart-core/Object) element)
The signature of the function that gets called when the [HtmlElementView](flutter-docs://api/widgets/HtmlElementView) DOM element is created.

[ElementVisitor](flutter-docs://api/widgets/ElementVisitor) = void Function([Element](flutter-docs://api/widgets/Element) element)
Signature for the callback to [BuildContext.visitChildElements](flutter-docs://api/widgets/BuildContext/visitChildElements).

[EntryModeChangeCallback](flutter-docs://api/material/EntryModeChangeCallback) = void Function([TimePickerEntryMode](flutter-docs://api/material/TimePickerEntryMode) mode)
Signature for when the time picker entry mode is changed.

[ErrorWidgetBuilder](flutter-docs://api/widgets/ErrorWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([FlutterErrorDetails](flutter-docs://api/foundation/FlutterErrorDetails) details)
Signature for the constructor that is called when an error occurs while
building a widget.

[ExitWidgetSelectionButtonBuilder](flutter-docs://api/widgets/ExitWidgetSelectionButtonBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, {required [GlobalKey](flutter-docs://api/widgets/GlobalKey)<[State](flutter-docs://api/widgets/State)<[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)>> key, required [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) onPressed, required [String](flutter-docs://api/dart-core/String) semanticsLabel})
Signature for the builder callback used by
[WidgetInspector.exitWidgetSelectionButtonBuilder](flutter-docs://api/widgets/WidgetInspector/exitWidgetSelectionButtonBuilder).

[ExpansibleBuilder](flutter-docs://api/widgets/ExpansibleBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Widget](flutter-docs://api/widgets/Widget) header, [Widget](flutter-docs://api/widgets/Widget) body, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation)
The type of the callback that uses the header and body of an [Expansible](flutter-docs://api/widgets/Expansible) widget to build the widget.

[ExpansibleComponentBuilder](flutter-docs://api/widgets/ExpansibleComponentBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation)
The type of the callback that returns the header or body of an [Expansible](flutter-docs://api/widgets/Expansible).

[ExpansionPanelCallback](flutter-docs://api/material/ExpansionPanelCallback) = void Function([int](flutter-docs://api/dart-core/int) panelIndex, [bool](flutter-docs://api/dart-core/bool) isExpanded)
Signature for the callback that's called when an [ExpansionPanel](flutter-docs://api/material/ExpansionPanel) is
expanded or collapsed.

[ExpansionPanelHeaderBuilder](flutter-docs://api/material/ExpansionPanelHeaderBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [bool](flutter-docs://api/dart-core/bool) isExpanded)
Signature for the callback that's called when the header of the
[ExpansionPanel](flutter-docs://api/material/ExpansionPanel) needs to rebuild.

[ExpansionTileController](flutter-docs://api/material/ExpansionTileController) = [ExpansibleController](flutter-docs://api/widgets/ExpansibleController)
Enables control over a single [ExpansionTile](flutter-docs://api/material/ExpansionTile)'s expanded/collapsed state.

[FilterCallback](flutter-docs://api/material/FilterCallback)<T> = [List](flutter-docs://api/dart-core/List)<[DropdownMenuEntry](flutter-docs://api/material/DropdownMenuEntry)<T>> Function([List](flutter-docs://api/dart-core/List)<[DropdownMenuEntry](flutter-docs://api/material/DropdownMenuEntry)<T>> entries, [String](flutter-docs://api/dart-core/String) filter)
A callback function that returns the list of the items that matches the
current applied filter.

[FocusOnKeyCallback](flutter-docs://api/widgets/FocusOnKeyCallback) = [KeyEventResult](flutter-docs://api/widgets/KeyEventResult) Function([FocusNode](flutter-docs://api/widgets/FocusNode) node, [RawKeyEvent](flutter-docs://api/services/RawKeyEvent) event)
Signature of a callback used by [Focus.onKey](flutter-docs://api/widgets/Focus/onKey) and [FocusScope.onKey](flutter-docs://api/widgets/Focus/onKey) to receive key events.

[FocusOnKeyEventCallback](flutter-docs://api/widgets/FocusOnKeyEventCallback) = [KeyEventResult](flutter-docs://api/widgets/KeyEventResult) Function([FocusNode](flutter-docs://api/widgets/FocusNode) node, [KeyEvent](flutter-docs://api/services/KeyEvent) event)
Signature of a callback used by [Focus.onKeyEvent](flutter-docs://api/widgets/Focus/onKeyEvent) and [FocusScope.onKeyEvent](flutter-docs://api/widgets/Focus/onKeyEvent) to receive key events.

[FormFieldBuilder](flutter-docs://api/widgets/FormFieldBuilder)<T> = [Widget](flutter-docs://api/widgets/Widget) Function([FormFieldState](flutter-docs://api/widgets/FormFieldState)<T> field)
Signature for building the widget representing the form field.

[FormFieldErrorBuilder](flutter-docs://api/widgets/FormFieldErrorBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [String](flutter-docs://api/dart-core/String) errorText)
Signature for a callback that builds an error widget.

[FormFieldSetter](flutter-docs://api/widgets/FormFieldSetter)<T> = void Function(T? newValue)
Signature for being notified when a form field changes value.

[FormFieldValidator](flutter-docs://api/widgets/FormFieldValidator)<T> = [String](flutter-docs://api/dart-core/String)? Function(T? value)
Signature for validating a form field.

[GenerateAppTitle](flutter-docs://api/widgets/GenerateAppTitle) = [String](flutter-docs://api/dart-core/String) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context)
The signature of [WidgetsApp.onGenerateTitle](flutter-docs://api/widgets/WidgetsApp/onGenerateTitle).

[GestureDragCancelCallback](flutter-docs://api/gestures/GestureDragCancelCallback) = void Function()
Signature for when the pointer that previously triggered a
[GestureDragDownCallback](flutter-docs://api/gestures/GestureDragDownCallback) did not complete.

[GestureDragDownCallback](flutter-docs://api/gestures/GestureDragDownCallback) = void Function([DragDownDetails](flutter-docs://api/gestures/DragDownDetails) details)
Signature for when a pointer has contacted the screen and might begin to
move.

[GestureDragEndCallback](flutter-docs://api/gestures/GestureDragEndCallback) = void Function([DragEndDetails](flutter-docs://api/gestures/DragEndDetails) details)
Signature for when a pointer that was previously in contact with the screen
and moving is no longer in contact with the screen.

[GestureDragStartCallback](flutter-docs://api/gestures/GestureDragStartCallback) = void Function([DragStartDetails](flutter-docs://api/gestures/DragStartDetails) details)
Signature for when a pointer has contacted the screen and has begun to move.

[GestureDragUpdateCallback](flutter-docs://api/gestures/GestureDragUpdateCallback) = void Function([DragUpdateDetails](flutter-docs://api/gestures/DragUpdateDetails) details)
Signature for when a pointer that is in contact with the screen and moving
has moved again.

[GestureForcePressEndCallback](flutter-docs://api/gestures/GestureForcePressEndCallback) = void Function([ForcePressDetails](flutter-docs://api/gestures/ForcePressDetails) details)
Signature for when the pointer that previously triggered a
[ForcePressGestureRecognizer.onStart](flutter-docs://api/gestures/ForcePressGestureRecognizer/onStart) callback is no longer in contact
with the screen.

[GestureForcePressPeakCallback](flutter-docs://api/gestures/GestureForcePressPeakCallback) = void Function([ForcePressDetails](flutter-docs://api/gestures/ForcePressDetails) details)
Signature used by [ForcePressGestureRecognizer](flutter-docs://api/gestures/ForcePressGestureRecognizer) for when a pointer that has
pressed with at least [ForcePressGestureRecognizer.peakPressure](flutter-docs://api/gestures/ForcePressGestureRecognizer/peakPressure).

[GestureForcePressStartCallback](flutter-docs://api/gestures/GestureForcePressStartCallback) = void Function([ForcePressDetails](flutter-docs://api/gestures/ForcePressDetails) details)
Signature used by a [ForcePressGestureRecognizer](flutter-docs://api/gestures/ForcePressGestureRecognizer) for when a pointer has
pressed with at least [ForcePressGestureRecognizer.startPressure](flutter-docs://api/gestures/ForcePressGestureRecognizer/startPressure).

[GestureForcePressUpdateCallback](flutter-docs://api/gestures/GestureForcePressUpdateCallback) = void Function([ForcePressDetails](flutter-docs://api/gestures/ForcePressDetails) details)
Signature used by [ForcePressGestureRecognizer](flutter-docs://api/gestures/ForcePressGestureRecognizer) during the frames
after the triggering of a [ForcePressGestureRecognizer.onStart](flutter-docs://api/gestures/ForcePressGestureRecognizer/onStart) callback.

[GestureLongPressCallback](flutter-docs://api/gestures/GestureLongPressCallback) = void Function()
Callback signature for [LongPressGestureRecognizer.onLongPress](flutter-docs://api/gestures/LongPressGestureRecognizer/onLongPress).

[GestureLongPressEndCallback](flutter-docs://api/gestures/GestureLongPressEndCallback) = void Function([LongPressEndDetails](flutter-docs://api/gestures/LongPressEndDetails) details)
Callback signature for [LongPressGestureRecognizer.onLongPressEnd](flutter-docs://api/gestures/LongPressGestureRecognizer/onLongPressEnd).

[GestureLongPressMoveUpdateCallback](flutter-docs://api/gestures/GestureLongPressMoveUpdateCallback) = void Function([LongPressMoveUpdateDetails](flutter-docs://api/gestures/LongPressMoveUpdateDetails) details)
Callback signature for [LongPressGestureRecognizer.onLongPressMoveUpdate](flutter-docs://api/gestures/LongPressGestureRecognizer/onLongPressMoveUpdate).

[GestureLongPressStartCallback](flutter-docs://api/gestures/GestureLongPressStartCallback) = void Function([LongPressStartDetails](flutter-docs://api/gestures/LongPressStartDetails) details)
Callback signature for [LongPressGestureRecognizer.onLongPressStart](flutter-docs://api/gestures/LongPressGestureRecognizer/onLongPressStart).

[GestureLongPressUpCallback](flutter-docs://api/gestures/GestureLongPressUpCallback) = void Function()
Callback signature for [LongPressGestureRecognizer.onLongPressUp](flutter-docs://api/gestures/LongPressGestureRecognizer/onLongPressUp).

[GestureRecognizerFactoryConstructor](flutter-docs://api/widgets/GestureRecognizerFactoryConstructor)<T extends [GestureRecognizer](flutter-docs://api/gestures/GestureRecognizer)> = T Function()
Signature for closures that implement [GestureRecognizerFactory.constructor](flutter-docs://api/widgets/GestureRecognizerFactory/constructor).

[GestureRecognizerFactoryInitializer](flutter-docs://api/widgets/GestureRecognizerFactoryInitializer)<T extends [GestureRecognizer](flutter-docs://api/gestures/GestureRecognizer)> = void Function(T instance)
Signature for closures that implement [GestureRecognizerFactory.initializer](flutter-docs://api/widgets/GestureRecognizerFactory/initializer).

[GestureScaleEndCallback](flutter-docs://api/gestures/GestureScaleEndCallback) = void Function([ScaleEndDetails](flutter-docs://api/gestures/ScaleEndDetails) details)
Signature for when the pointers are no longer in contact with the screen.

[GestureScaleStartCallback](flutter-docs://api/gestures/GestureScaleStartCallback) = void Function([ScaleStartDetails](flutter-docs://api/gestures/ScaleStartDetails) details)
Signature for when the pointers in contact with the screen have established
a focal point and initial scale of 1.0.

[GestureScaleUpdateCallback](flutter-docs://api/gestures/GestureScaleUpdateCallback) = void Function([ScaleUpdateDetails](flutter-docs://api/gestures/ScaleUpdateDetails) details)
Signature for when the pointers in contact with the screen have indicated a
new focal point and/or scale.

[GestureTapCallback](flutter-docs://api/gestures/GestureTapCallback) = void Function()
Signature for when a tap has occurred.

[GestureTapCancelCallback](flutter-docs://api/gestures/GestureTapCancelCallback) = void Function()
Signature for when the pointer that previously triggered a
[GestureTapDownCallback](flutter-docs://api/gestures/GestureTapDownCallback) will not end up causing a tap.

[GestureTapDownCallback](flutter-docs://api/gestures/GestureTapDownCallback) = void Function([TapDownDetails](flutter-docs://api/gestures/TapDownDetails) details)
Signature for when a pointer that might cause a tap has contacted the
screen.

[GestureTapUpCallback](flutter-docs://api/gestures/GestureTapUpCallback) = void Function([TapUpDetails](flutter-docs://api/gestures/TapUpDetails) details)
Signature for when a pointer that will trigger a tap has stopped contacting
the screen.

[HeroFlightShuttleBuilder](flutter-docs://api/widgets/HeroFlightShuttleBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) flightContext, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation, [HeroFlightDirection](flutter-docs://api/widgets/HeroFlightDirection) flightDirection, [BuildContext](flutter-docs://api/widgets/BuildContext) fromHeroContext, [BuildContext](flutter-docs://api/widgets/BuildContext) toHeroContext)
A function that lets [Hero](flutter-docs://api/widgets/Hero) es self supply a [Widget](flutter-docs://api/widgets/Widget) that is shown during the
hero's flight from one route to another instead of default (which is to
show the destination route's instance of the Hero).

[HeroPlaceholderBuilder](flutter-docs://api/widgets/HeroPlaceholderBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Size](flutter-docs://api/dart-ui/Size) heroSize, [Widget](flutter-docs://api/widgets/Widget) child)
Signature for a function that builds a [Hero](flutter-docs://api/widgets/Hero) placeholder widget given a
child and a [Size](flutter-docs://api/dart-ui/Size).

[HttpClientProvider](flutter-docs://api/painting/HttpClientProvider) = [HttpClient](flutter-docs://api/dart-io/HttpClient) Function()
Signature for a method that returns an [HttpClient](flutter-docs://api/dart-io/HttpClient).

[ImageChunkListener](flutter-docs://api/painting/ImageChunkListener) = void Function([ImageChunkEvent](flutter-docs://api/painting/ImageChunkEvent) event)
Signature for listening to [ImageChunkEvent](flutter-docs://api/painting/ImageChunkEvent) events.

[ImageDecoderCallback](flutter-docs://api/painting/ImageDecoderCallback) = [Future](flutter-docs://api/dart-async/Future)<[Codec](flutter-docs://api/dart-ui/Codec)> Function([ImmutableBuffer](flutter-docs://api/dart-ui/ImmutableBuffer) buffer, {[TargetImageSizeCallback](flutter-docs://api/dart-ui/TargetImageSizeCallback)? getTargetSize})
Performs the decode process for use in [ImageProvider.loadImage](flutter-docs://api/painting/ImageProvider/loadImage).

[ImageErrorListener](flutter-docs://api/painting/ImageErrorListener) = void Function([Object](flutter-docs://api/dart-core/Object) exception, [StackTrace](flutter-docs://api/dart-core/StackTrace)? stackTrace)
Signature for reporting errors when resolving images.

[ImageErrorWidgetBuilder](flutter-docs://api/widgets/ImageErrorWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Object](flutter-docs://api/dart-core/Object) error, [StackTrace](flutter-docs://api/dart-core/StackTrace)? stackTrace)
Signature used by [Image.errorBuilder](flutter-docs://api/widgets/Image/errorBuilder) to create a replacement widget to
render instead of the image.

[ImageFrameBuilder](flutter-docs://api/widgets/ImageFrameBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Widget](flutter-docs://api/widgets/Widget) child, [int](flutter-docs://api/dart-core/int)? frame, [bool](flutter-docs://api/dart-core/bool) wasSynchronouslyLoaded)
Signature used by [Image.frameBuilder](flutter-docs://api/widgets/Image/frameBuilder) to control the widget that will be
used when an [Image](flutter-docs://api/widgets/Image) is built.

[ImageListener](flutter-docs://api/painting/ImageListener) = void Function([ImageInfo](flutter-docs://api/painting/ImageInfo) image, [bool](flutter-docs://api/dart-core/bool) synchronousCall)
Signature for callbacks reporting that an image is available.

[ImageLoadingBuilder](flutter-docs://api/widgets/ImageLoadingBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Widget](flutter-docs://api/widgets/Widget) child, [ImageChunkEvent](flutter-docs://api/painting/ImageChunkEvent)? loadingProgress)
Signature used by [Image.loadingBuilder](flutter-docs://api/widgets/Image/loadingBuilder) to build a representation of the
image's loading progress.

[IndexedWidgetBuilder](flutter-docs://api/widgets/IndexedWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [int](flutter-docs://api/dart-core/int) index)
Signature for a function that creates a widget for a given index, e.g., in a
list.

[InitialRouteListFactory](flutter-docs://api/widgets/InitialRouteListFactory) = [List](flutter-docs://api/dart-core/List)<[Route](flutter-docs://api/widgets/Route)> Function([String](flutter-docs://api/dart-core/String) initialRoute)
The signature of [WidgetsApp.onGenerateInitialRoutes](flutter-docs://api/widgets/WidgetsApp/onGenerateInitialRoutes).

[InlineSpanVisitor](flutter-docs://api/painting/InlineSpanVisitor) = [bool](flutter-docs://api/dart-core/bool) Function([InlineSpan](flutter-docs://api/painting/InlineSpan) span)
Called on each span as [InlineSpan.visitChildren](flutter-docs://api/painting/InlineSpan/visitChildren) walks the [InlineSpan](flutter-docs://api/painting/InlineSpan) tree.

[InputCounterWidgetBuilder](flutter-docs://api/material/InputCounterWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget)? Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, {required [int](flutter-docs://api/dart-core/int) currentLength, required [bool](flutter-docs://api/dart-core/bool) isFocused, required [int](flutter-docs://api/dart-core/int)? maxLength})
Signature for the [TextField.buildCounter](flutter-docs://api/material/TextField/buildCounter) callback.

[InspectorSelectionChangedCallback](flutter-docs://api/widgets/InspectorSelectionChangedCallback) = void Function()
Signature for the selection change callback used by
[WidgetInspectorService.selectionChangedCallback](flutter-docs://api/widgets/WidgetInspectorService/selectionChangedCallback).

[InteractiveViewerWidgetBuilder](flutter-docs://api/widgets/InteractiveViewerWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Quad](flutter-docs://api/package-vector_math_vector_math_64/Quad) viewport)
A signature for widget builders that take a [Quad](flutter-docs://api/package-vector_math_vector_math_64/Quad) of the current viewport.

[LayoutWidgetBuilder](flutter-docs://api/widgets/LayoutWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [BoxConstraints](flutter-docs://api/rendering/BoxConstraints) constraints)
The signature of the [LayoutBuilder](flutter-docs://api/widgets/LayoutBuilder) builder function.

[LocaleListResolutionCallback](flutter-docs://api/widgets/LocaleListResolutionCallback) = [Locale](flutter-docs://api/dart-ui/Locale)? Function([List](flutter-docs://api/dart-core/List)<[Locale](flutter-docs://api/dart-ui/Locale)>? locales, [Iterable](flutter-docs://api/dart-core/Iterable)<[Locale](flutter-docs://api/dart-ui/Locale)> supportedLocales)
The signature of [WidgetsApp.localeListResolutionCallback](flutter-docs://api/widgets/WidgetsApp/localeListResolutionCallback).

[LocaleResolutionCallback](flutter-docs://api/widgets/LocaleResolutionCallback) = [Locale](flutter-docs://api/dart-ui/Locale)? Function([Locale](flutter-docs://api/dart-ui/Locale)? locale, [Iterable](flutter-docs://api/dart-core/Iterable)<[Locale](flutter-docs://api/dart-ui/Locale)> supportedLocales)
The signature of [WidgetsApp.localeResolutionCallback](flutter-docs://api/widgets/WidgetsApp/localeResolutionCallback).

[MagnifierBuilder](flutter-docs://api/widgets/MagnifierBuilder) = [Widget](flutter-docs://api/widgets/Widget)? Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [MagnifierController](flutter-docs://api/widgets/MagnifierController) controller, [ValueNotifier](flutter-docs://api/foundation/ValueNotifier)<[MagnifierInfo](flutter-docs://api/widgets/MagnifierInfo)> magnifierInfo)
Signature for a builder that builds a [Widget](flutter-docs://api/widgets/Widget) with a [MagnifierController](flutter-docs://api/widgets/MagnifierController).

[MaterialPropertyResolver](flutter-docs://api/material/MaterialPropertyResolver)<T> = [WidgetPropertyResolver](flutter-docs://api/widgets/WidgetPropertyResolver)<T>
Signature for the function that returns a value of type `T` based on a given
set of states.

[MaterialState](flutter-docs://api/material/MaterialState) = [WidgetState](flutter-docs://api/widgets/WidgetState)
Interactive states that some of the Material widgets can take on when
receiving input from the user.

[MaterialStateBorderSide](flutter-docs://api/material/MaterialStateBorderSide) = [WidgetStateBorderSide](flutter-docs://api/widgets/WidgetStateBorderSide)
Defines a [BorderSide](flutter-docs://api/painting/BorderSide) whose value depends on a set of [MaterialState](flutter-docs://api/material/MaterialState) s
which represent the interactive state of a component.

[MaterialStateColor](flutter-docs://api/material/MaterialStateColor) = [WidgetStateColor](flutter-docs://api/widgets/WidgetStateColor)
Defines a [Color](flutter-docs://api/dart-ui/Color) that is also a [MaterialStateProperty](flutter-docs://api/material/MaterialStateProperty).

[MaterialStateMouseCursor](flutter-docs://api/material/MaterialStateMouseCursor) = [WidgetStateMouseCursor](flutter-docs://api/widgets/WidgetStateMouseCursor)
Defines a [MouseCursor](flutter-docs://api/services/MouseCursor) whose value depends on a set of [MaterialState](flutter-docs://api/material/MaterialState) s which
represent the interactive state of a component.

[MaterialStateOutlinedBorder](flutter-docs://api/material/MaterialStateOutlinedBorder) = [WidgetStateOutlinedBorder](flutter-docs://api/widgets/WidgetStateOutlinedBorder)
Defines an [OutlinedBorder](flutter-docs://api/painting/OutlinedBorder) whose value depends on a set of [MaterialState](flutter-docs://api/material/MaterialState) s
which represent the interactive state of a component.

[MaterialStateProperty](flutter-docs://api/material/MaterialStateProperty)<T>
 = [WidgetStateProperty](flutter-docs://api/widgets/WidgetStateProperty)<T>
Interface for classes that [resolve](flutter-docs://api/widgets/WidgetStateProperty/resolve) to a value of type `T` based
on a widget's interactive "state", which is defined as a set
of [MaterialState](flutter-docs://api/material/MaterialState) s.

[MaterialStatePropertyAll](flutter-docs://api/material/MaterialStatePropertyAll)<T>
 = [WidgetStatePropertyAll](flutter-docs://api/widgets/WidgetStatePropertyAll)<T>
Convenience class for creating a [MaterialStateProperty](flutter-docs://api/material/MaterialStateProperty) that
resolves to the given value for all states.

[MaterialStatesController](flutter-docs://api/material/MaterialStatesController) = [WidgetStatesController](flutter-docs://api/widgets/WidgetStatesController)
Manages a set of [MaterialState](flutter-docs://api/material/MaterialState) s and notifies listeners of changes.

[MaterialStateTextStyle](flutter-docs://api/material/MaterialStateTextStyle) = [WidgetStateTextStyle](flutter-docs://api/widgets/WidgetStateTextStyle)
Defines a [TextStyle](flutter-docs://api/painting/TextStyle) that is also a [MaterialStateProperty](flutter-docs://api/material/MaterialStateProperty).

[MenuAcceleratorChildBuilder](flutter-docs://api/material/MenuAcceleratorChildBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [String](flutter-docs://api/dart-core/String) label, [int](flutter-docs://api/dart-core/int) index)
The type of builder function used for building a [MenuAcceleratorLabel](flutter-docs://api/material/MenuAcceleratorLabel)'s
[MenuAcceleratorLabel.builder](flutter-docs://api/material/MenuAcceleratorLabel/builder) function.

[MenuAnchorChildBuilder](flutter-docs://api/material/MenuAnchorChildBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [MenuController](flutter-docs://api/widgets/MenuController) controller, [Widget](flutter-docs://api/widgets/Widget)? child)
The type of builder function used by [MenuAnchor.builder](flutter-docs://api/material/MenuAnchor/builder) to build the
widget that the [MenuAnchor](flutter-docs://api/material/MenuAnchor) surrounds.

[MenuItemSerializableIdGenerator](flutter-docs://api/widgets/MenuItemSerializableIdGenerator) = [int](flutter-docs://api/dart-core/int) Function([PlatformMenuItem](flutter-docs://api/widgets/PlatformMenuItem) item)
The signature for a function that generates unique menu item IDs for
serialization of a [PlatformMenuItem](flutter-docs://api/widgets/PlatformMenuItem).

[MoveExitWidgetSelectionButtonBuilder](flutter-docs://api/widgets/MoveExitWidgetSelectionButtonBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, {required [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) onPressed, required [String](flutter-docs://api/dart-core/String) semanticsLabel, [bool](flutter-docs://api/dart-core/bool) usesDefaultAlignment})
Signature for the builder callback used by
[WidgetInspector.moveExitWidgetSelectionButtonBuilder](flutter-docs://api/widgets/WidgetInspector/moveExitWidgetSelectionButtonBuilder).

[NavigatorFinderCallback](flutter-docs://api/widgets/NavigatorFinderCallback) = [NavigatorState](flutter-docs://api/widgets/NavigatorState) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context)
A callback that given a [BuildContext](flutter-docs://api/widgets/BuildContext) finds a [NavigatorState](flutter-docs://api/widgets/NavigatorState).

[NestedScrollViewHeaderSliversBuilder](flutter-docs://api/widgets/NestedScrollViewHeaderSliversBuilder) = [List](flutter-docs://api/dart-core/List)<[Widget](flutter-docs://api/widgets/Widget)> Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [bool](flutter-docs://api/dart-core/bool) innerBoxIsScrolled)
Signature used by [NestedScrollView](flutter-docs://api/widgets/NestedScrollView) for building its header.

[NotificationListenerCallback](flutter-docs://api/widgets/NotificationListenerCallback)<T extends [Notification](flutter-docs://api/widgets/Notification)> = [bool](flutter-docs://api/dart-core/bool) Function(T notification)
Signature for [Notification](flutter-docs://api/widgets/Notification) listeners.

[NullableIndexedWidgetBuilder](flutter-docs://api/widgets/NullableIndexedWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget)? Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [int](flutter-docs://api/dart-core/int) index)
Signature for a function that creates a widget for a given index, e.g., in a
list, but may return null.

[OnInvokeCallback](flutter-docs://api/widgets/OnInvokeCallback)<T extends [Intent](flutter-docs://api/widgets/Intent)> = [Object](flutter-docs://api/dart-core/Object)? Function(T intent)
The signature of a callback accepted by [CallbackAction.onInvoke](flutter-docs://api/widgets/CallbackAction/onInvoke).

[OnKeyEventCallback](flutter-docs://api/widgets/OnKeyEventCallback) = [KeyEventResult](flutter-docs://api/widgets/KeyEventResult) Function([KeyEvent](flutter-docs://api/services/KeyEvent) event)
Signature of a callback used by [FocusManager.addEarlyKeyEventHandler](flutter-docs://api/widgets/FocusManager/addEarlyKeyEventHandler) and
[FocusManager.addLateKeyEventHandler](flutter-docs://api/widgets/FocusManager/addLateKeyEventHandler).

[OrientationWidgetBuilder](flutter-docs://api/widgets/OrientationWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Orientation](flutter-docs://api/widgets/Orientation) orientation)
Signature for a function that builds a widget given an [Orientation](flutter-docs://api/widgets/Orientation).

[OverlayChildLayoutBuilder](flutter-docs://api/widgets/OverlayChildLayoutBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [OverlayChildLayoutInfo](flutter-docs://api/widgets/OverlayChildLayoutInfo) info)
The signature of the widget builder callback used in
[OverlayPortal.overlayChildLayoutBuilder](flutter-docs://api/widgets/OverlayPortal/OverlayPortal.overlayChildLayoutBuilder).

[PageRouteFactory](flutter-docs://api/widgets/PageRouteFactory) = [PageRoute](flutter-docs://api/widgets/PageRoute)<T> Function<T>([RouteSettings](flutter-docs://api/widgets/RouteSettings) settings, [WidgetBuilder](flutter-docs://api/widgets/WidgetBuilder) builder)
The signature of [WidgetsApp.pageRouteBuilder](flutter-docs://api/widgets/WidgetsApp/pageRouteBuilder).

[PaintImageCallback](flutter-docs://api/painting/PaintImageCallback) = void Function([ImageSizeInfo](flutter-docs://api/painting/ImageSizeInfo) info)
Called when the framework is about to paint an [Image](flutter-docs://api/dart-ui/Image) to a [Canvas](flutter-docs://api/dart-ui/Canvas) with an
[ImageSizeInfo](flutter-docs://api/painting/ImageSizeInfo) that contains the decoded size of the image as well as its
output size.

[PaintRangeValueIndicator](flutter-docs://api/material/PaintRangeValueIndicator) = void Function([PaintingContext](flutter-docs://api/rendering/PaintingContext) context, [Offset](flutter-docs://api/dart-ui/Offset) offset)
[RangeSlider](flutter-docs://api/material/RangeSlider) uses this callback to paint the value indicator on the overlay.
Since the value indicator is painted on the Overlay; this method paints the
value indicator in a [RenderBox](flutter-docs://api/rendering/RenderBox) that appears in the [Overlay](flutter-docs://api/widgets/Overlay).

[PaintValueIndicator](flutter-docs://api/material/PaintValueIndicator) = void Function([PaintingContext](flutter-docs://api/rendering/PaintingContext) context, [Offset](flutter-docs://api/dart-ui/Offset) offset)
[Slider](flutter-docs://api/material/Slider) uses this callback to paint the value indicator on the overlay.

[PlatformViewSurfaceFactory](flutter-docs://api/widgets/PlatformViewSurfaceFactory) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [PlatformViewController](flutter-docs://api/services/PlatformViewController) controller)
A factory for a surface presenting a platform view as part of the widget hierarchy.

[PointerCancelEventListener](flutter-docs://api/rendering/PointerCancelEventListener) = void Function([PointerCancelEvent](flutter-docs://api/gestures/PointerCancelEvent) event)
Signature for listening to [PointerCancelEvent](flutter-docs://api/gestures/PointerCancelEvent) events.

[PointerDownEventListener](flutter-docs://api/rendering/PointerDownEventListener) = void Function([PointerDownEvent](flutter-docs://api/gestures/PointerDownEvent) event)
Signature for listening to [PointerDownEvent](flutter-docs://api/gestures/PointerDownEvent) events.

[PointerMoveEventListener](flutter-docs://api/rendering/PointerMoveEventListener) = void Function([PointerMoveEvent](flutter-docs://api/gestures/PointerMoveEvent) event)
Signature for listening to [PointerMoveEvent](flutter-docs://api/gestures/PointerMoveEvent) events.

[PointerUpEventListener](flutter-docs://api/rendering/PointerUpEventListener) = void Function([PointerUpEvent](flutter-docs://api/gestures/PointerUpEvent) event)
Signature for listening to [PointerUpEvent](flutter-docs://api/gestures/PointerUpEvent) events.

[PopInvokedCallback](flutter-docs://api/widgets/PopInvokedCallback) = void Function([bool](flutter-docs://api/dart-core/bool) didPop)
A callback type for informing that a navigation pop has been invoked,
whether or not it was handled successfully.

[PopInvokedWithResultCallback](flutter-docs://api/widgets/PopInvokedWithResultCallback)<T> = void Function([bool](flutter-docs://api/dart-core/bool) didPop, T? result)
A callback type for informing that a navigation pop has been invoked,
whether or not it was handled successfully.

[PopPageCallback](flutter-docs://api/widgets/PopPageCallback) = [bool](flutter-docs://api/dart-core/bool) Function([Route](flutter-docs://api/widgets/Route) route, dynamic result)
Signature for the [Navigator.onPopPage](flutter-docs://api/widgets/Navigator/onPopPage) callback.

[PopResultCallback](flutter-docs://api/widgets/PopResultCallback)<T> = void Function(T? result)
A signature for a function that is passed the result of a [Route](flutter-docs://api/widgets/Route).

[PopupMenuCanceled](flutter-docs://api/material/PopupMenuCanceled) = void Function()
Signature for the callback invoked when a [PopupMenuButton](flutter-docs://api/material/PopupMenuButton) is dismissed
without selecting an item.

[PopupMenuItemBuilder](flutter-docs://api/material/PopupMenuItemBuilder)<T> = [List](flutter-docs://api/dart-core/List)<[PopupMenuEntry](flutter-docs://api/material/PopupMenuEntry)<T>> Function([BuildContext](flutter-docs://api/widgets/BuildContext) context)
Signature used by [PopupMenuButton](flutter-docs://api/material/PopupMenuButton) to lazily construct the items shown when
the button is pressed.

[PopupMenuItemSelected](flutter-docs://api/material/PopupMenuItemSelected)<T> = void Function(T value)
Signature for the callback invoked when a menu item is selected. The
argument is the value of the [PopupMenuItem](flutter-docs://api/material/PopupMenuItem) that caused its menu to be
dismissed.

[PopupMenuPositionBuilder](flutter-docs://api/material/PopupMenuPositionBuilder) = [RelativeRect](flutter-docs://api/rendering/RelativeRect) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [BoxConstraints](flutter-docs://api/rendering/BoxConstraints) constraints)
A builder that creates a [RelativeRect](flutter-docs://api/rendering/RelativeRect) to position a popup menu.
Both [BuildContext](flutter-docs://api/widgets/BuildContext) and [BoxConstraints](flutter-docs://api/rendering/BoxConstraints) are from the [PopupRoute](flutter-docs://api/widgets/PopupRoute) that
displays this menu.

[RadioBuilder](flutter-docs://api/widgets/RadioBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [ToggleableStateMixin](flutter-docs://api/widgets/ToggleableStateMixin)<[StatefulWidget](flutter-docs://api/widgets/StatefulWidget)> state)
Signature for [RawRadio.builder](flutter-docs://api/widgets/RawRadio/builder).

[RangeThumbSelector](flutter-docs://api/material/RangeThumbSelector) = [Thumb](flutter-docs://api/material/Thumb)? Function([TextDirection](flutter-docs://api/dart-ui/TextDirection) textDirection, [RangeValues](flutter-docs://api/material/RangeValues) values, [double](flutter-docs://api/dart-core/double) tapValue, [Size](flutter-docs://api/dart-ui/Size) thumbSize, [Size](flutter-docs://api/dart-ui/Size) trackSize, [double](flutter-docs://api/dart-core/double) dx)
Decides which thumbs (if any) should be selected.

[RawMenuAnchorChildBuilder](flutter-docs://api/widgets/RawMenuAnchorChildBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [MenuController](flutter-docs://api/widgets/MenuController) controller, [Widget](flutter-docs://api/widgets/Widget)? child)
Signature for the builder function used by [RawMenuAnchor.builder](flutter-docs://api/widgets/RawMenuAnchor/builder) to build
the widget that the [RawMenuAnchor](flutter-docs://api/widgets/RawMenuAnchor) surrounds.

[RawMenuAnchorCloseRequestedCallback](flutter-docs://api/widgets/RawMenuAnchorCloseRequestedCallback) = void Function([VoidCallback](flutter-docs://api/dart-ui/VoidCallback) hideOverlay)
Signature for the callback used by [RawMenuAnchor.onCloseRequested](flutter-docs://api/widgets/RawMenuAnchor/onCloseRequested) to
intercept requests to close a menu.

[RawMenuAnchorOpenRequestedCallback](flutter-docs://api/widgets/RawMenuAnchorOpenRequestedCallback) = void Function([Offset](flutter-docs://api/dart-ui/Offset)? position, [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) showOverlay)
Signature for the callback used by [RawMenuAnchor.onOpenRequested](flutter-docs://api/widgets/RawMenuAnchor/onOpenRequested) to
intercept requests to open a menu.

[RawMenuAnchorOverlayBuilder](flutter-docs://api/widgets/RawMenuAnchorOverlayBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [RawMenuOverlayInfo](flutter-docs://api/widgets/RawMenuOverlayInfo) info)
Signature for the builder function used by [RawMenuAnchor.overlayBuilder](flutter-docs://api/widgets/RawMenuAnchor/overlayBuilder) to
build a menu's overlay.

[RebuildDirtyWidgetCallback](flutter-docs://api/widgets/RebuildDirtyWidgetCallback) = void Function([Element](flutter-docs://api/widgets/Element) e, [bool](flutter-docs://api/dart-core/bool) builtOnce)
Signature for [debugOnRebuildDirtyWidget](flutter-docs://api/cupertino/debugOnRebuildDirtyWidget) implementations.

[RectCallback](flutter-docs://api/material/RectCallback) = [Rect](flutter-docs://api/dart-ui/Rect) Function()
Signature for the callback used by ink effects to obtain the rectangle for the effect.

[RefreshCallback](flutter-docs://api/material/RefreshCallback) = [Future](flutter-docs://api/dart-async/Future)<void> Function()
The signature for a function that's called when the user has dragged a
[RefreshIndicator](flutter-docs://api/material/RefreshIndicator) far enough to demonstrate that they want the app to
refresh. The returned [Future](flutter-docs://api/dart-async/Future) must complete when the refresh operation is
finished.

[RegisterServiceExtensionCallback](flutter-docs://api/widgets/RegisterServiceExtensionCallback) = void Function({required [ServiceExtensionCallback](flutter-docs://api/foundation/ServiceExtensionCallback) callback, required [String](flutter-docs://api/dart-core/String) name})
Signature for a method that registers the service extension `callback` with
the given `name`.

[RegisterViewFactory](flutter-docs://api/widgets/RegisterViewFactory) = void Function([String](flutter-docs://api/dart-core/String), [Object](flutter-docs://api/dart-core/Object) ([int](flutter-docs://api/dart-core/int) viewId), {[bool](flutter-docs://api/dart-core/bool) isVisible})
Function signature for `ui_web.platformViewRegistry.registerViewFactory`.

[RenderConstrainedLayoutBuilder](flutter-docs://api/widgets/RenderConstrainedLayoutBuilder)<LayoutInfoType, ChildType extends [RenderObject](flutter-docs://api/rendering/RenderObject)>
 = [RenderAbstractLayoutBuilderMixin](flutter-docs://api/widgets/RenderAbstractLayoutBuilderMixin)<LayoutInfoType, ChildType>
Generic mixin for [RenderObject](flutter-docs://api/rendering/RenderObject) s created by an [AbstractLayoutBuilder](flutter-docs://api/widgets/AbstractLayoutBuilder) with
the the same `LayoutInfoType`.

[ReorderCallback](flutter-docs://api/widgets/ReorderCallback) = void Function([int](flutter-docs://api/dart-core/int) oldIndex, [int](flutter-docs://api/dart-core/int) newIndex)
A callback used by [ReorderableList](flutter-docs://api/widgets/ReorderableList) to report that a list item has moved
to a new position in the list.

[ReorderDragBoundaryProvider](flutter-docs://api/widgets/ReorderDragBoundaryProvider) = [DragBoundaryDelegate](flutter-docs://api/widgets/DragBoundaryDelegate)<[Rect](flutter-docs://api/dart-ui/Rect)>? Function([BuildContext](flutter-docs://api/widgets/BuildContext) context)
Used to provide drag boundaries during drag-and-drop reordering.

[ReorderItemProxyDecorator](flutter-docs://api/widgets/ReorderItemProxyDecorator) = [Widget](flutter-docs://api/widgets/Widget) Function([Widget](flutter-docs://api/widgets/Widget) child, [int](flutter-docs://api/dart-core/int) index, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation)
Signature for the builder callback used to decorate the dragging item in
[ReorderableList](flutter-docs://api/widgets/ReorderableList) and [SliverReorderableList](flutter-docs://api/widgets/SliverReorderableList).

[RestorableRouteBuilder](flutter-docs://api/widgets/RestorableRouteBuilder)<T> = [Route](flutter-docs://api/widgets/Route)<T> Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Object](flutter-docs://api/dart-core/Object)? arguments)
Creates a [Route](flutter-docs://api/widgets/Route) that is to be added to a [Navigator](flutter-docs://api/widgets/Navigator).

[RouteCompletionCallback](flutter-docs://api/widgets/RouteCompletionCallback)<T> = void Function(T result)
A callback to handle the result of a completed [Route](flutter-docs://api/widgets/Route).

[RouteFactory](flutter-docs://api/widgets/RouteFactory) = [Route](flutter-docs://api/widgets/Route)? Function([RouteSettings](flutter-docs://api/widgets/RouteSettings) settings)
Creates a route for the given route settings.

[RouteListFactory](flutter-docs://api/widgets/RouteListFactory) = [List](flutter-docs://api/dart-core/List)<[Route](flutter-docs://api/widgets/Route)> Function([NavigatorState](flutter-docs://api/widgets/NavigatorState) navigator, [String](flutter-docs://api/dart-core/String) initialRoute)
Creates a series of one or more routes.

[RoutePageBuilder](flutter-docs://api/widgets/RoutePageBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> secondaryAnimation)
Signature for the function that builds a route's primary contents.
Used in [PageRouteBuilder](flutter-docs://api/widgets/PageRouteBuilder) and [showGeneralDialog](flutter-docs://api/widgets/showGeneralDialog).

[RoutePredicate](flutter-docs://api/widgets/RoutePredicate) = [bool](flutter-docs://api/dart-core/bool) Function([Route](flutter-docs://api/widgets/Route) route)
Signature for the [Navigator.popUntil](flutter-docs://api/widgets/Navigator/popUntil) predicate argument.

[RoutePresentationCallback](flutter-docs://api/widgets/RoutePresentationCallback) = [String](flutter-docs://api/dart-core/String) Function([NavigatorState](flutter-docs://api/widgets/NavigatorState) navigator, [Object](flutter-docs://api/dart-core/Object)? arguments)
A callback that given some `arguments` and a `navigator` adds a new
restorable route to that `navigator` and returns the opaque ID of that
new route.

[RouteTransitionsBuilder](flutter-docs://api/widgets/RouteTransitionsBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> animation, [Animation](flutter-docs://api/animation/Animation)<[double](flutter-docs://api/dart-core/double)> secondaryAnimation, [Widget](flutter-docs://api/widgets/Widget) child)
Signature for the function that builds a route's transitions.
Used in [PageRouteBuilder](flutter-docs://api/widgets/PageRouteBuilder) and [showGeneralDialog](flutter-docs://api/widgets/showGeneralDialog).

[ScrollableWidgetBuilder](flutter-docs://api/widgets/ScrollableWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [ScrollController](flutter-docs://api/widgets/ScrollController) scrollController)
The signature of a method that provides a [BuildContext](flutter-docs://api/widgets/BuildContext) and
[ScrollController](flutter-docs://api/widgets/ScrollController) for building a widget that may overflow the draggable
[Axis](flutter-docs://api/painting/Axis) of the containing [DraggableScrollableSheet](flutter-docs://api/widgets/DraggableScrollableSheet).

[ScrollControllerCallback](flutter-docs://api/widgets/ScrollControllerCallback) = void Function([ScrollPosition](flutter-docs://api/widgets/ScrollPosition) position)
Signature for when a [ScrollController](flutter-docs://api/widgets/ScrollController) has added or removed a
[ScrollPosition](flutter-docs://api/widgets/ScrollPosition).

[ScrollIncrementCalculator](flutter-docs://api/widgets/ScrollIncrementCalculator) = [double](flutter-docs://api/dart-core/double) Function([ScrollIncrementDetails](flutter-docs://api/widgets/ScrollIncrementDetails) details)
A typedef for a function that can calculate the offset for a type of scroll
increment given a [ScrollIncrementDetails](flutter-docs://api/widgets/ScrollIncrementDetails).

[ScrollNotificationCallback](flutter-docs://api/widgets/ScrollNotificationCallback) = void Function([ScrollNotification](flutter-docs://api/widgets/ScrollNotification) notification)
A [ScrollNotification](flutter-docs://api/widgets/ScrollNotification) listener for [ScrollNotificationObserver](flutter-docs://api/widgets/ScrollNotificationObserver).

[ScrollNotificationPredicate](flutter-docs://api/widgets/ScrollNotificationPredicate) = [bool](flutter-docs://api/dart-core/bool) Function([ScrollNotification](flutter-docs://api/widgets/ScrollNotification) notification)
A predicate for [ScrollNotification](flutter-docs://api/widgets/ScrollNotification), used to customize widgets that
listen to notifications from their children.

[SearchAnchorChildBuilder](flutter-docs://api/material/SearchAnchorChildBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [SearchController](flutter-docs://api/material/SearchController) controller)
Signature for a function that creates a [Widget](flutter-docs://api/widgets/Widget) which is used to open a search view.

[SearchCallback](flutter-docs://api/material/SearchCallback)<T> = [int](flutter-docs://api/dart-core/int)? Function([List](flutter-docs://api/dart-core/List)<[DropdownMenuEntry](flutter-docs://api/material/DropdownMenuEntry)<T>> entries, [String](flutter-docs://api/dart-core/String) query)
A callback function that returns the index of the item that matches the
current contents of a text field.

[SelectableDayForRangePredicate](flutter-docs://api/material/SelectableDayForRangePredicate) = [bool](flutter-docs://api/dart-core/bool) Function([DateTime](flutter-docs://api/dart-core/DateTime) day, [DateTime](flutter-docs://api/dart-core/DateTime)? selectedStartDay, [DateTime](flutter-docs://api/dart-core/DateTime)? selectedEndDay)
Signature for predicating enabled dates in date range pickers.

[SelectableDayPredicate](flutter-docs://api/widgets/SelectableDayPredicate) = [bool](flutter-docs://api/dart-core/bool) Function([DateTime](flutter-docs://api/dart-core/DateTime) day)
Signature for predicating dates for enabled date selections.

[SelectableRegionContextMenuBuilder](flutter-docs://api/widgets/SelectableRegionContextMenuBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [SelectableRegionState](flutter-docs://api/widgets/SelectableRegionState) selectableRegionState)
Signature for a widget builder that builds a context menu for the given
[SelectableRegionState](flutter-docs://api/widgets/SelectableRegionState).

[SelectionChangedCallback](flutter-docs://api/widgets/SelectionChangedCallback) = void Function([TextSelection](flutter-docs://api/services/TextSelection) selection, [SelectionChangedCause](flutter-docs://api/services/SelectionChangedCause)? cause)
Signature for the callback that reports when the user changes the selection
(including the cursor location).

[SemanticFormatterCallback](flutter-docs://api/material/SemanticFormatterCallback) = [String](flutter-docs://api/dart-core/String) Function([double](flutter-docs://api/dart-core/double) value)
A callback that formats a numeric value from a [Slider](flutter-docs://api/material/Slider) or [RangeSlider](flutter-docs://api/material/RangeSlider) widget.

[SemanticIndexCallback](flutter-docs://api/widgets/SemanticIndexCallback) = [int](flutter-docs://api/dart-core/int)? Function([Widget](flutter-docs://api/widgets/Widget) widget, [int](flutter-docs://api/dart-core/int) localIndex)
A callback which produces a semantic index given a widget and the local index.

[SemanticsBuilderCallback](flutter-docs://api/rendering/SemanticsBuilderCallback) = [List](flutter-docs://api/dart-core/List)<[CustomPainterSemantics](flutter-docs://api/rendering/CustomPainterSemantics)> Function([Size](flutter-docs://api/dart-ui/Size) size)
Signature of the function returned by [CustomPainter.semanticsBuilder](flutter-docs://api/rendering/CustomPainter/semanticsBuilder).

[ShaderCallback](flutter-docs://api/rendering/ShaderCallback) = [Shader](flutter-docs://api/dart-ui/Shader) Function([Rect](flutter-docs://api/dart-ui/Rect) bounds)
Signature for a function that creates a [Shader](flutter-docs://api/dart-ui/Shader) for a given [Rect](flutter-docs://api/dart-ui/Rect).

[ShaderWarmUpImageCallback](flutter-docs://api/painting/ShaderWarmUpImageCallback) = [bool](flutter-docs://api/dart-core/bool) Function([Image](flutter-docs://api/dart-ui/Image) image)
The signature of [debugCaptureShaderWarmUpImage](flutter-docs://api/rendering/debugCaptureShaderWarmUpImage).

[ShaderWarmUpPictureCallback](flutter-docs://api/painting/ShaderWarmUpPictureCallback) = [bool](flutter-docs://api/dart-core/bool) Function([Picture](flutter-docs://api/dart-ui/Picture) picture)
The signature of [debugCaptureShaderWarmUpPicture](flutter-docs://api/rendering/debugCaptureShaderWarmUpPicture).

[SharedAppDataInitCallback](flutter-docs://api/widgets/SharedAppDataInitCallback)<T> = T Function()
The type of the [SharedAppData.getValue](flutter-docs://api/widgets/SharedAppData/getValue) `init` parameter.

[SliverLayoutWidgetBuilder](flutter-docs://api/widgets/SliverLayoutWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [SliverConstraints](flutter-docs://api/rendering/SliverConstraints) constraints)
The signature of the [SliverLayoutBuilder](flutter-docs://api/widgets/SliverLayoutBuilder) builder function.

[StatefulWidgetBuilder](flutter-docs://api/widgets/StatefulWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [StateSetter](flutter-docs://api/widgets/StateSetter) setState)
Signature for the builder callback used by [StatefulBuilder](flutter-docs://api/widgets/StatefulBuilder).

[StateSetter](flutter-docs://api/widgets/StateSetter) = void Function([VoidCallback](flutter-docs://api/dart-ui/VoidCallback) fn)
The signature of [State.setState](flutter-docs://api/widgets/State/setState) functions.

[StepIconBuilder](flutter-docs://api/material/StepIconBuilder) = [Widget](flutter-docs://api/widgets/Widget)? Function([int](flutter-docs://api/dart-core/int) stepIndex, [StepState](flutter-docs://api/material/StepState) stepState)
A builder that creates the icon widget for the [Step](flutter-docs://api/material/Step) at `stepIndex`, given
`stepState`.

[SuggestionsBuilder](flutter-docs://api/material/SuggestionsBuilder) = [FutureOr](flutter-docs://api/dart-async/FutureOr)<[Iterable](flutter-docs://api/dart-core/Iterable)<[Widget](flutter-docs://api/widgets/Widget)>> Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [SearchController](flutter-docs://api/material/SearchController) controller)
Signature for a function that creates a [Widget](flutter-docs://api/widgets/Widget) to build the suggestion list
based on the input in the search bar.

[TabValueChanged](flutter-docs://api/material/TabValueChanged)<T> = void Function(T value, [int](flutter-docs://api/dart-core/int) index)
Signature for [TabBar](flutter-docs://api/material/TabBar) callbacks that report that an underlying value has
changed for a given [Tab](flutter-docs://api/material/Tab) at `index`.

[TapBehaviorButtonBuilder](flutter-docs://api/widgets/TapBehaviorButtonBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, {required [VoidCallback](flutter-docs://api/dart-ui/VoidCallback) onPressed, required [bool](flutter-docs://api/dart-core/bool) selectionOnTapEnabled, required [String](flutter-docs://api/dart-core/String) semanticsLabel})
Signature for the builder callback used by
[WidgetInspector.tapBehaviorButtonBuilder](flutter-docs://api/widgets/WidgetInspector/tapBehaviorButtonBuilder).

[TapRegionCallback](flutter-docs://api/widgets/TapRegionCallback) = void Function([PointerDownEvent](flutter-docs://api/gestures/PointerDownEvent) event)
Signature for a callback called for a [PointerDownEvent](flutter-docs://api/gestures/PointerDownEvent) relative to a [TapRegion](flutter-docs://api/widgets/TapRegion).

[TapRegionUpCallback](flutter-docs://api/widgets/TapRegionUpCallback) = void Function([PointerUpEvent](flutter-docs://api/gestures/PointerUpEvent) event)
Signature for a callback called for a [PointerUpEvent](flutter-docs://api/gestures/PointerUpEvent) relative to a [TapRegion](flutter-docs://api/widgets/TapRegion).

[ToolbarBuilder](flutter-docs://api/widgets/ToolbarBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Widget](flutter-docs://api/widgets/Widget) child)
The type for a Function that builds a toolbar's container with the given
child.

[TooltipTriggeredCallback](flutter-docs://api/material/TooltipTriggeredCallback) = void Function()
Signature for when a tooltip is triggered.

[TransformCallback](flutter-docs://api/widgets/TransformCallback) = [Matrix4](flutter-docs://api/package-vector_math_vector_math_64/Matrix4) Function([double](flutter-docs://api/dart-core/double) animationValue)
Signature for the callback to [MatrixTransition.onTransform](flutter-docs://api/widgets/MatrixTransition/onTransform).

[TransitionBuilder](flutter-docs://api/widgets/TransitionBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [Widget](flutter-docs://api/widgets/Widget)? child)
A builder that builds a widget given a child.

[TraversalRequestFocusCallback](flutter-docs://api/widgets/TraversalRequestFocusCallback) = void Function([FocusNode](flutter-docs://api/widgets/FocusNode) node, {[double](flutter-docs://api/dart-core/double)? alignment, [ScrollPositionAlignmentPolicy](flutter-docs://api/widgets/ScrollPositionAlignmentPolicy)? alignmentPolicy, [Curve](flutter-docs://api/animation/Curve)? curve, [Duration](flutter-docs://api/dart-core/Duration)? duration})
Signature for the callback that's called when a traversal policy
requests focus.

[TreeSliverNodeBuilder](flutter-docs://api/widgets/TreeSliverNodeBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode)<[Object](flutter-docs://api/dart-core/Object)?> node, [AnimationStyle](flutter-docs://api/animation/AnimationStyle) animationStyle)
Signature for a function that creates a [Widget](flutter-docs://api/widgets/Widget) to represent the given
[TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode) in the [TreeSliver](flutter-docs://api/widgets/TreeSliver).

[TreeSliverNodeCallback](flutter-docs://api/widgets/TreeSliverNodeCallback) = void Function([TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode)<[Object](flutter-docs://api/dart-core/Object)?> node)
Signature for a function that is called when a [TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode) is toggled,
changing its expanded state.

[TreeSliverRowExtentBuilder](flutter-docs://api/widgets/TreeSliverRowExtentBuilder) = [double](flutter-docs://api/dart-core/double) Function([TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode)<[Object](flutter-docs://api/dart-core/Object)?> node, [SliverLayoutDimensions](flutter-docs://api/rendering/SliverLayoutDimensions) dimensions)
Signature for a function that returns an extent for the given
[TreeSliverNode](flutter-docs://api/widgets/TreeSliverNode) in the [TreeSliver](flutter-docs://api/widgets/TreeSliver).

[TweenConstructor](flutter-docs://api/widgets/TweenConstructor)<T extends [Object](flutter-docs://api/dart-core/Object)> = [Tween](flutter-docs://api/animation/Tween)<T> Function(T targetValue)
Signature for a [Tween](flutter-docs://api/animation/Tween) factory.

[TweenVisitor](flutter-docs://api/widgets/TweenVisitor)<T extends [Object](flutter-docs://api/dart-core/Object)> = [Tween](flutter-docs://api/animation/Tween)<T>? Function([Tween](flutter-docs://api/animation/Tween)<T>? tween, T targetValue, [TweenConstructor](flutter-docs://api/widgets/TweenConstructor)<T> constructor)
Signature for callbacks passed to [ImplicitlyAnimatedWidgetState.forEachTween](flutter-docs://api/widgets/ImplicitlyAnimatedWidgetState/forEachTween).

[TwoDimensionalIndexedWidgetBuilder](flutter-docs://api/widgets/TwoDimensionalIndexedWidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget)? Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [ChildVicinity](flutter-docs://api/widgets/ChildVicinity) vicinity)
Signature for a function that creates a widget for a given [ChildVicinity](flutter-docs://api/widgets/ChildVicinity),
e.g., in a [TwoDimensionalScrollView](flutter-docs://api/widgets/TwoDimensionalScrollView), but may return null.

[TwoDimensionalViewportBuilder](flutter-docs://api/widgets/TwoDimensionalViewportBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [ViewportOffset](flutter-docs://api/rendering/ViewportOffset) verticalPosition, [ViewportOffset](flutter-docs://api/rendering/ViewportOffset) horizontalPosition)
Signature used by [TwoDimensionalScrollable](flutter-docs://api/widgets/TwoDimensionalScrollable) to build the viewport through
which the scrollable content is displayed.

[ValueChanged](flutter-docs://api/foundation/ValueChanged)<T> = void Function(T value)
Signature for callbacks that report that an underlying value has changed.

[ValueGetter](flutter-docs://api/foundation/ValueGetter)<T> = T Function()
Signature for callbacks that are to report a value on demand.

[ValueListenableTransformer](flutter-docs://api/animation/ValueListenableTransformer)<T> = T Function(T)
Signature for method used to transform values in [Animation.fromValueListenable](flutter-docs://api/animation/Animation/Animation.fromValueListenable).

[ValueSetter](flutter-docs://api/foundation/ValueSetter)<T> = void Function(T value)
Signature for callbacks that report that a value has been set.

[ValueWidgetBuilder](flutter-docs://api/widgets/ValueWidgetBuilder)<T> = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, T value, [Widget](flutter-docs://api/widgets/Widget)? child)
Builds a [Widget](flutter-docs://api/widgets/Widget) when given a concrete value of a [ValueListenable<T>](flutter-docs://api/foundation/ValueListenable).

[ViewBuilder](flutter-docs://api/material/ViewBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([Iterable](flutter-docs://api/dart-core/Iterable)<[Widget](flutter-docs://api/widgets/Widget)> suggestions)
Signature for a function that creates a [Widget](flutter-docs://api/widgets/Widget) to layout the suggestion list.

[ViewportBuilder](flutter-docs://api/widgets/ViewportBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context, [ViewportOffset](flutter-docs://api/rendering/ViewportOffset) position)
Signature used by [Scrollable](flutter-docs://api/widgets/Scrollable) to build the viewport through which the
scrollable content is displayed.

[VoidCallback](flutter-docs://api/dart-ui/VoidCallback) = void Function()
Signature of callbacks that have no arguments and return no data.

[WidgetBuilder](flutter-docs://api/widgets/WidgetBuilder) = [Widget](flutter-docs://api/widgets/Widget) Function([BuildContext](flutter-docs://api/widgets/BuildContext) context)
Signature for a function that creates a widget, e.g. [StatelessWidget.build](flutter-docs://api/widgets/StatelessWidget/build) or [State.build](flutter-docs://api/widgets/State/build).

[WidgetPropertyResolver](flutter-docs://api/widgets/WidgetPropertyResolver)<T> = T Function([Set](flutter-docs://api/dart-core/Set)<[WidgetState](flutter-docs://api/widgets/WidgetState)> states)
Signature for the function that returns a value of type `T` based on a given
set of states.

[WidgetStateMap](flutter-docs://api/widgets/WidgetStateMap)<T>
 = [Map](flutter-docs://api/dart-core/Map)<[WidgetStatesConstraint](flutter-docs://api/widgets/WidgetStatesConstraint), T>
A [Map](flutter-docs://api/dart-core/Map) used to resolve to a single value of type `T` based on
the current set of Widget states.

[WillPopCallback](flutter-docs://api/widgets/WillPopCallback) = [Future](flutter-docs://api/dart-async/Future)<[bool](flutter-docs://api/dart-core/bool)> Function()
Signature for a callback that verifies that it's OK to call [Navigator.pop](flutter-docs://api/widgets/Navigator/pop).

## Exceptions / Errors

[FlutterError](flutter-docs://api/foundation/FlutterError)
Error class used to report Flutter-specific assertion failures and
contract violations.

[NetworkImageLoadException](flutter-docs://api/painting/NetworkImageLoadException)
The exception thrown when the HTTP request to load a network image fails.

[TickerCanceled](flutter-docs://api/scheduler/TickerCanceled)
Exception thrown by [Ticker](flutter-docs://api/scheduler/Ticker) objects on the [TickerFuture.orCancel](flutter-docs://api/scheduler/TickerFuture/orCancel) future
when the ticker is canceled.