# widgets library

The Flutter widgets framework.

To use, import `package:flutter/widgets.dart`.

See also:

- [flutter.dev/widgets](https://flutter.dev/widgets/) for a catalog of commonly-used Flutter widgets.


## Classes

[AbsorbPointer](mcp://flutter/api/widgets/AbsorbPointer)
A widget that absorbs pointers during hit testing.

[AbstractLayoutBuilder](mcp://flutter/api/widgets/AbstractLayoutBuilder)<LayoutInfoType>
An abstract superclass for widgets that defer their building until layout.

[Accumulator](mcp://flutter/api/painting/Accumulator)
Mutable wrapper of an integer that can be passed by reference to track a
value across a recursive stack.

[Action](mcp://flutter/api/widgets/Action)<T extends [Intent](mcp://flutter/api/widgets/Intent)>
Base class for an action or command to be performed.

[ActionDispatcher](mcp://flutter/api/widgets/ActionDispatcher)
An action dispatcher that invokes the actions given to it.

[ActionListener](mcp://flutter/api/widgets/ActionListener)
A helper widget for making sure that listeners on an action are removed properly.

[Actions](mcp://flutter/api/widgets/Actions)
A widget that maps [Intent](mcp://flutter/api/widgets/Intent) s to [Action](mcp://flutter/api/widgets/Action) s to be used by its descendants
when invoking an [Action](mcp://flutter/api/widgets/Action).

[ActivateAction](mcp://flutter/api/widgets/ActivateAction)
An [Action](mcp://flutter/api/widgets/Action) that activates the currently focused control.

[ActivateIntent](mcp://flutter/api/widgets/ActivateIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that activates the currently focused control.

[Align](mcp://flutter/api/widgets/Align)
A widget that aligns its child within itself and optionally sizes itself
based on the child's size.

[Alignment](mcp://flutter/api/painting/Alignment)
A point within a rectangle.

[AlignmentDirectional](mcp://flutter/api/painting/AlignmentDirectional)
An offset that's expressed as a fraction of a [Size](mcp://flutter/api/dart-ui/Size), but whose horizontal
component is dependent on the writing direction.

[AlignmentGeometry](mcp://flutter/api/painting/AlignmentGeometry)
Base class for [Alignment](mcp://flutter/api/painting/Alignment) that allows for text-direction aware
resolution.

[AlignmentGeometryTween](mcp://flutter/api/rendering/AlignmentGeometryTween)
An interpolation between two [AlignmentGeometry](mcp://flutter/api/painting/AlignmentGeometry).

[AlignmentTween](mcp://flutter/api/rendering/AlignmentTween)
An interpolation between two alignments.

[AlignTransition](mcp://flutter/api/widgets/AlignTransition)
Animated version of an [Align](mcp://flutter/api/widgets/Align) that animates its [Align.alignment](mcp://flutter/api/widgets/Align/alignment) property.

[AlwaysScrollableScrollPhysics](mcp://flutter/api/widgets/AlwaysScrollableScrollPhysics)
Scroll physics that always lets the user scroll.

[AlwaysStoppedAnimation](mcp://flutter/api/animation/AlwaysStoppedAnimation)<T>
An animation that is always stopped at a given value.

[AndroidView](mcp://flutter/api/widgets/AndroidView)
Embeds an Android view in the Widget hierarchy.

[AndroidViewSurface](mcp://flutter/api/widgets/AndroidViewSurface)
Integrates an Android view with Flutter's compositor, touch, and semantics subsystems.

[Animatable](mcp://flutter/api/animation/Animatable)<T>
An object that can produce a value of type `T` given an [Animation<double>](mcp://flutter/api/animation/Animation) as input.

[AnimatedAlign](mcp://flutter/api/widgets/AnimatedAlign)
Animated version of [Align](mcp://flutter/api/widgets/Align) which automatically transitions the child's
position over a given duration whenever the given [alignment](mcp://flutter/api/widgets/AnimatedAlign/alignment) changes.

[AnimatedBuilder](mcp://flutter/api/widgets/AnimatedBuilder)
A general-purpose widget for building animations.

[AnimatedContainer](mcp://flutter/api/widgets/AnimatedContainer)
Animated version of [Container](mcp://flutter/api/widgets/Container) that gradually changes its values over a period of time.

[AnimatedCrossFade](mcp://flutter/api/widgets/AnimatedCrossFade)
A widget that cross-fades between two given children and animates itself
between their sizes.

[AnimatedDefaultTextStyle](mcp://flutter/api/widgets/AnimatedDefaultTextStyle)
Animated version of [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle) which automatically transitions the
default text style (the text style to apply to descendant [Text](mcp://flutter/api/widgets/Text) widgets
without explicit style) over a given duration whenever the given style
changes.

[AnimatedFractionallySizedBox](mcp://flutter/api/widgets/AnimatedFractionallySizedBox)
Animated version of [FractionallySizedBox](mcp://flutter/api/widgets/FractionallySizedBox) which automatically transitions the
child's size over a given duration whenever the given [widthFactor](mcp://flutter/api/widgets/AnimatedFractionallySizedBox/widthFactor) or
[heightFactor](mcp://flutter/api/widgets/AnimatedFractionallySizedBox/heightFactor) changes, as well as the position whenever the given [alignment](mcp://flutter/api/widgets/AnimatedFractionallySizedBox/alignment) changes.

[AnimatedGrid](mcp://flutter/api/widgets/AnimatedGrid)
A scrolling container that animates items when they are inserted into or removed from a grid.
in a grid.

[AnimatedGridState](mcp://flutter/api/widgets/AnimatedGridState)
The [State](mcp://flutter/api/widgets/State) for an [AnimatedGrid](mcp://flutter/api/widgets/AnimatedGrid) that animates items when they are
inserted or removed.

[AnimatedList](mcp://flutter/api/widgets/AnimatedList)
A scrolling container that animates items when they are inserted or removed.

[AnimatedListState](mcp://flutter/api/widgets/AnimatedListState)
The [AnimatedListState](mcp://flutter/api/widgets/AnimatedListState) for [AnimatedList](mcp://flutter/api/widgets/AnimatedList), a scrolling list container that
animates items when they are inserted or removed.

[AnimatedModalBarrier](mcp://flutter/api/widgets/AnimatedModalBarrier)
A widget that prevents the user from interacting with widgets behind itself,
and can be configured with an animated color value.

[AnimatedOpacity](mcp://flutter/api/widgets/AnimatedOpacity)
Animated version of [Opacity](mcp://flutter/api/widgets/Opacity) which automatically transitions the child's
opacity over a given duration whenever the given opacity changes.

[AnimatedPadding](mcp://flutter/api/widgets/AnimatedPadding)
Animated version of [Padding](mcp://flutter/api/widgets/Padding) which automatically transitions the
indentation over a given duration whenever the given inset changes.

[AnimatedPhysicalModel](mcp://flutter/api/widgets/AnimatedPhysicalModel)
Animated version of [PhysicalModel](mcp://flutter/api/widgets/PhysicalModel).

[AnimatedPositioned](mcp://flutter/api/widgets/AnimatedPositioned)
Animated version of [Positioned](mcp://flutter/api/widgets/Positioned) which automatically transitions the child's
position over a given duration whenever the given position changes.

[AnimatedPositionedDirectional](mcp://flutter/api/widgets/AnimatedPositionedDirectional)
Animated version of [PositionedDirectional](mcp://flutter/api/widgets/PositionedDirectional) which automatically transitions
the child's position over a given duration whenever the given position
changes.

[AnimatedRotation](mcp://flutter/api/widgets/AnimatedRotation)
Animated version of [Transform.rotate](mcp://flutter/api/widgets/Transform/Transform.rotate) which automatically transitions the child's
rotation over a given duration whenever the given rotation changes.

[AnimatedScale](mcp://flutter/api/widgets/AnimatedScale)
Animated version of [Transform.scale](mcp://flutter/api/widgets/Transform/Transform.scale) which automatically transitions the child's
scale over a given duration whenever the given scale changes.

[AnimatedSize](mcp://flutter/api/widgets/AnimatedSize)
Animated widget that automatically transitions its size over a given
duration whenever the given child's size changes.

[AnimatedSlide](mcp://flutter/api/widgets/AnimatedSlide)
Widget which automatically transitions the child's
offset relative to its normal position whenever the given offset changes.

[AnimatedSwitcher](mcp://flutter/api/widgets/AnimatedSwitcher)
A widget that by default does a cross-fade between a new widget and the
widget previously set on the [AnimatedSwitcher](mcp://flutter/api/widgets/AnimatedSwitcher) as a child.

[AnimatedWidget](mcp://flutter/api/widgets/AnimatedWidget)
A widget that rebuilds when the given [Listenable](mcp://flutter/api/foundation/Listenable) changes value.

[AnimatedWidgetBaseState](mcp://flutter/api/widgets/AnimatedWidgetBaseState)<T extends [ImplicitlyAnimatedWidget](mcp://flutter/api/widgets/ImplicitlyAnimatedWidget)>
A base class for widgets with implicit animations that need to rebuild their
widget tree as the animation runs.

[Animation](mcp://flutter/api/animation/Animation)<T>
A value which might change over time, moving forward or backward.

[AnimationController](mcp://flutter/api/animation/AnimationController)
A controller for an animation.

[AnimationMax](mcp://flutter/api/animation/AnimationMax)<T extends [num](mcp://flutter/api/dart-core/num)>
An animation that tracks the maximum of two other animations.

[AnimationMean](mcp://flutter/api/animation/AnimationMean)
An animation of [double](mcp://flutter/api/dart-core/double) s that tracks the mean of two other animations.

[AnimationMin](mcp://flutter/api/animation/AnimationMin)<T extends [num](mcp://flutter/api/dart-core/num)>
An animation that tracks the minimum of two other animations.

[AnimationStyle](mcp://flutter/api/animation/AnimationStyle)
Used to override the default parameters of an animation.

[AnnotatedRegion](mcp://flutter/api/widgets/AnnotatedRegion)<T extends [Object](mcp://flutter/api/dart-core/Object)>
Annotates a region of the layer tree with a value.

[AppKitView](mcp://flutter/api/widgets/AppKitView)
Widget that contains a macOS AppKit view.

[AppLifecycleListener](mcp://flutter/api/widgets/AppLifecycleListener)
A listener that can be used to listen to changes in the application
lifecycle.

[AspectRatio](mcp://flutter/api/widgets/AspectRatio)
A widget that attempts to size the child to a specific aspect ratio.

[AssetBundle](mcp://flutter/api/services/AssetBundle)
A collection of resources used by the application.

[AssetBundleImageKey](mcp://flutter/api/painting/AssetBundleImageKey)
Key for the image obtained by an [AssetImage](mcp://flutter/api/painting/AssetImage) or [ExactAssetImage](mcp://flutter/api/painting/ExactAssetImage).

[AssetBundleImageProvider](mcp://flutter/api/painting/AssetBundleImageProvider)
A subclass of [ImageProvider](mcp://flutter/api/painting/ImageProvider) that knows about [AssetBundle](mcp://flutter/api/services/AssetBundle) s.

[AssetImage](mcp://flutter/api/painting/AssetImage)
Fetches an image from an [AssetBundle](mcp://flutter/api/services/AssetBundle), having determined the exact image to
use based on the context.

[AsyncSnapshot](mcp://flutter/api/widgets/AsyncSnapshot)<T>
Immutable representation of the most recent interaction with an asynchronous
computation.

[AutocompleteFirstOptionIntent](mcp://flutter/api/widgets/AutocompleteFirstOptionIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to highlight the first option in the autocomplete list.

[AutocompleteHighlightedOption](mcp://flutter/api/widgets/AutocompleteHighlightedOption)
An inherited widget used to indicate which autocomplete option should be
highlighted for keyboard navigation.

[AutocompleteLastOptionIntent](mcp://flutter/api/widgets/AutocompleteLastOptionIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to highlight the last option in the autocomplete list.

[AutocompleteNextOptionIntent](mcp://flutter/api/widgets/AutocompleteNextOptionIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to highlight the next option in the autocomplete list.

[AutocompleteNextPageOptionIntent](mcp://flutter/api/widgets/AutocompleteNextPageOptionIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to highlight the option one page after the currently highlighted
option in the autocomplete list.

[AutocompletePreviousOptionIntent](mcp://flutter/api/widgets/AutocompletePreviousOptionIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to highlight the previous option in the autocomplete list.

[AutocompletePreviousPageOptionIntent](mcp://flutter/api/widgets/AutocompletePreviousPageOptionIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to highlight the option one page before the currently
highlighted option in the autocomplete list.

[AutofillGroup](mcp://flutter/api/widgets/AutofillGroup)
An [AutofillScope](mcp://flutter/api/services/AutofillScope) widget that groups [AutofillClient](mcp://flutter/api/services/AutofillClient) s together.

[AutofillGroupState](mcp://flutter/api/widgets/AutofillGroupState)
State associated with an [AutofillGroup](mcp://flutter/api/widgets/AutofillGroup) widget.

[AutofillHints](mcp://flutter/api/services/AutofillHints)
A collection of commonly used autofill hint strings on different platforms.

[AutomaticKeepAlive](mcp://flutter/api/widgets/AutomaticKeepAlive)
Allows subtrees to request to be kept alive in lazy lists.

[AutomaticNotchedShape](mcp://flutter/api/painting/AutomaticNotchedShape)
A [NotchedShape](mcp://flutter/api/painting/NotchedShape) created from [ShapeBorder](mcp://flutter/api/painting/ShapeBorder) s.

[BackButtonDispatcher](mcp://flutter/api/widgets/BackButtonDispatcher)
Report to a [Router](mcp://flutter/api/widgets/Router) when the user taps the back button on platforms that
support back buttons (such as Android).

[BackButtonListener](mcp://flutter/api/widgets/BackButtonListener)
A convenience widget that registers a callback for when the back button is pressed.

[BackdropFilter](mcp://flutter/api/widgets/BackdropFilter)
A widget that applies a filter to the existing painted content and then
paints [child](mcp://flutter/api/widgets/SingleChildRenderObjectWidget/child).

[BackdropGroup](mcp://flutter/api/widgets/BackdropGroup)
A widget that establishes a shared backdrop layer for all child [BackdropFilter](mcp://flutter/api/widgets/BackdropFilter) widgets that opt into using it.

[BackdropKey](mcp://flutter/api/rendering/BackdropKey)
A backdrop key uniquely identifies the backdrop that a [BackdropFilterLayer](mcp://flutter/api/rendering/BackdropFilterLayer) samples from.

[BallisticScrollActivity](mcp://flutter/api/widgets/BallisticScrollActivity)
The activity a scroll view performs after being set into motion.

[Banner](mcp://flutter/api/widgets/Banner)
Displays a diagonal message above the corner of another widget.

[BannerPainter](mcp://flutter/api/widgets/BannerPainter)
Paints a [Banner](mcp://flutter/api/widgets/Banner).

[Baseline](mcp://flutter/api/widgets/Baseline)
A widget that positions its child according to the child's baseline.

[BeveledRectangleBorder](mcp://flutter/api/painting/BeveledRectangleBorder)
A rectangular border with flattened or "beveled" corners.

[BlockSemantics](mcp://flutter/api/widgets/BlockSemantics)
A widget that drops the semantics of all widget that were painted before it
in the same semantic container.

[Border](mcp://flutter/api/painting/Border)
A border of a box, comprised of four sides: top, right, bottom, left.

[BorderDirectional](mcp://flutter/api/painting/BorderDirectional)
A border of a box, comprised of four sides, the lateral sides of which
flip over based on the reading direction.

[BorderRadius](mcp://flutter/api/painting/BorderRadius)
An immutable set of radii for each corner of a rectangle.

[BorderRadiusDirectional](mcp://flutter/api/painting/BorderRadiusDirectional)
An immutable set of radii for each corner of a rectangle, but with the
corners specified in a manner dependent on the writing direction.

[BorderRadiusGeometry](mcp://flutter/api/painting/BorderRadiusGeometry)
Base class for [BorderRadius](mcp://flutter/api/painting/BorderRadius) that allows for text-direction aware resolution.

[BorderRadiusTween](mcp://flutter/api/widgets/BorderRadiusTween)
An interpolation between two [BorderRadius](mcp://flutter/api/painting/BorderRadius) s.

[BorderSide](mcp://flutter/api/painting/BorderSide)
A side of a border of a box.

[BorderTween](mcp://flutter/api/widgets/BorderTween)
An interpolation between two [Border](mcp://flutter/api/painting/Border) s.

[BottomNavigationBarItem](mcp://flutter/api/widgets/BottomNavigationBarItem)
An interactive button within either material's [BottomNavigationBar](mcp://flutter/api/material/BottomNavigationBar) or the iOS themed [CupertinoTabBar](mcp://flutter/api/cupertino/CupertinoTabBar) with an icon and title.

[BouncingScrollPhysics](mcp://flutter/api/widgets/BouncingScrollPhysics)
Scroll physics for environments that allow the scroll offset to go beyond
the bounds of the content, but then bounce the content back to the edge of
those bounds.

[BouncingScrollSimulation](mcp://flutter/api/widgets/BouncingScrollSimulation)
An implementation of scroll physics that matches iOS.

[BoxBorder](mcp://flutter/api/painting/BoxBorder)
Base class for box borders that can paint as rectangles, circles, or rounded
rectangles.

[BoxConstraints](mcp://flutter/api/rendering/BoxConstraints)
Immutable layout constraints for [RenderBox](mcp://flutter/api/rendering/RenderBox) layout.

[BoxConstraintsTween](mcp://flutter/api/widgets/BoxConstraintsTween)
An interpolation between two [BoxConstraints](mcp://flutter/api/rendering/BoxConstraints).

[BoxDecoration](mcp://flutter/api/painting/BoxDecoration)
An immutable description of how to paint a box.

[BoxPainter](mcp://flutter/api/painting/BoxPainter)
A stateful class that can paint a particular [Decoration](mcp://flutter/api/painting/Decoration).

[BoxScrollView](mcp://flutter/api/widgets/BoxScrollView)
A [ScrollView](mcp://flutter/api/widgets/ScrollView) that uses a single child layout model.

[BoxShadow](mcp://flutter/api/painting/BoxShadow)
A shadow cast by a box.

[BuildContext](mcp://flutter/api/widgets/BuildContext)
A handle to the location of a widget in the widget tree.

[Builder](mcp://flutter/api/widgets/Builder)
A stateless utility widget whose [build](mcp://flutter/api/widgets/Builder/build) method uses its
[builder](mcp://flutter/api/widgets/Builder/builder) callback to create the widget's child.

[BuildOwner](mcp://flutter/api/widgets/BuildOwner)
Manager class for the widgets framework.

[BuildScope](mcp://flutter/api/widgets/BuildScope)
A class that determines the scope of a [BuildOwner.buildScope](mcp://flutter/api/widgets/BuildOwner/buildScope) operation.

[ButtonActivateIntent](mcp://flutter/api/widgets/ButtonActivateIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that activates the currently focused button.

[CallbackAction](mcp://flutter/api/widgets/CallbackAction)<T extends [Intent](mcp://flutter/api/widgets/Intent)>
An [Action](mcp://flutter/api/widgets/Action) that takes a callback in order to configure it without having to
create an explicit [Action](mcp://flutter/api/widgets/Action) subclass just to call a callback.

[CallbackShortcuts](mcp://flutter/api/widgets/CallbackShortcuts)
A widget that binds key combinations to specific callbacks.

[Canvas](mcp://flutter/api/dart-ui/Canvas)
An interface for recording graphical operations.

[CapturedThemes](mcp://flutter/api/widgets/CapturedThemes)
Stores a list of captured [InheritedTheme](mcp://flutter/api/widgets/InheritedTheme) s that can be wrapped around a
child [Widget](mcp://flutter/api/widgets/Widget).

[CatmullRomCurve](mcp://flutter/api/animation/CatmullRomCurve)
An animation easing curve that passes smoothly through the given control
points using a centripetal Catmull-Rom spline.

[CatmullRomSpline](mcp://flutter/api/animation/CatmullRomSpline)
A 2D spline that passes smoothly through the given control points using a
centripetal Catmull-Rom spline.

[Center](mcp://flutter/api/widgets/Center)
A widget that centers its child within itself.

[ChangeNotifier](mcp://flutter/api/foundation/ChangeNotifier)
A class that can be extended or mixed in that provides a change notification
API using [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) for notifications.

[CharacterActivator](mcp://flutter/api/widgets/CharacterActivator)
A shortcut combination that is triggered by a key event that produces a
specific character.

[CharacterRange](mcp://flutter/api/package-characters_characters/CharacterRange)
A range of characters of a [Characters](mcp://flutter/api/package-characters_characters/Characters).

[Characters](mcp://flutter/api/package-characters_characters/Characters)
The characters of a string.

[CheckedModeBanner](mcp://flutter/api/widgets/CheckedModeBanner)
Displays a [Banner](mcp://flutter/api/widgets/Banner) saying "DEBUG" when running in debug mode.
[MaterialApp](mcp://flutter/api/material/MaterialApp) builds one of these by default.

[ChildBackButtonDispatcher](mcp://flutter/api/widgets/ChildBackButtonDispatcher)
A variant of [BackButtonDispatcher](mcp://flutter/api/widgets/BackButtonDispatcher) which listens to notifications from a
parent back button dispatcher, and can take priority from its parent for the
handling of such notifications.

[ChildVicinity](mcp://flutter/api/widgets/ChildVicinity)
The relative position of a child in a [TwoDimensionalViewport](mcp://flutter/api/widgets/TwoDimensionalViewport) in relation
to other children of the viewport.

[CircleBorder](mcp://flutter/api/painting/CircleBorder)
A border that fits a circle within the available space.

[CircularNotchedRectangle](mcp://flutter/api/painting/CircularNotchedRectangle)
A rectangle with a smooth circular notch.

[ClampingScrollPhysics](mcp://flutter/api/widgets/ClampingScrollPhysics)
Scroll physics for environments that prevent the scroll offset from reaching
beyond the bounds of the content.

[ClampingScrollSimulation](mcp://flutter/api/widgets/ClampingScrollSimulation)
An implementation of scroll physics that aligns with Android.

[ClipboardStatusNotifier](mcp://flutter/api/widgets/ClipboardStatusNotifier)
A [ValueNotifier](mcp://flutter/api/foundation/ValueNotifier) whose [value](mcp://flutter/api/foundation/ValueNotifier/value) indicates whether the current contents of
the clipboard can be pasted.

[ClipContext](mcp://flutter/api/painting/ClipContext)
Clip utilities used by [PaintingContext](mcp://flutter/api/rendering/PaintingContext).

[ClipOval](mcp://flutter/api/widgets/ClipOval)
A widget that clips its child using an oval.

[ClipPath](mcp://flutter/api/widgets/ClipPath)
A widget that clips its child using a path.

[ClipRect](mcp://flutter/api/widgets/ClipRect)
A widget that clips its child using a rectangle.

[ClipRRect](mcp://flutter/api/widgets/ClipRRect)
A widget that clips its child using a rounded rectangle.

[ClipRSuperellipse](mcp://flutter/api/widgets/ClipRSuperellipse)
A widget that clips its child using a rounded superellipse.

[Color](mcp://flutter/api/dart-ui/Color)
An immutable color value in ARGB format.

[ColoredBox](mcp://flutter/api/widgets/ColoredBox)
A widget that paints its area with a specified [Color](mcp://flutter/api/dart-ui/Color) and then draws its
child on top of that color.

[ColorFilter](mcp://flutter/api/dart-ui/ColorFilter)
A description of a color filter to apply when drawing a shape or compositing
a layer with a particular [Paint](mcp://flutter/api/dart-ui/Paint). A color filter is a function that takes
two colors, and outputs one color. When applied during compositing, it is
independently applied to each pixel of the layer being drawn before the
entire layer is merged with the destination.

[ColorFiltered](mcp://flutter/api/widgets/ColorFiltered)
Applies a [ColorFilter](mcp://flutter/api/dart-ui/ColorFilter) to its child.

[ColorProperty](mcp://flutter/api/painting/ColorProperty)
[DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) that has an [Color](mcp://flutter/api/dart-ui/Color) as value.

[ColorSwatch](mcp://flutter/api/painting/ColorSwatch)<T>
A color that has a small table of related colors called a "swatch".

[ColorTween](mcp://flutter/api/animation/ColorTween)
An interpolation between two colors.

[Column](mcp://flutter/api/widgets/Column)
A widget that displays its children in a vertical array.

[ComponentElement](mcp://flutter/api/widgets/ComponentElement)
An [Element](mcp://flutter/api/widgets/Element) that composes other [Element](mcp://flutter/api/widgets/Element) s.

[CompositedTransformFollower](mcp://flutter/api/widgets/CompositedTransformFollower)
A widget that follows a [CompositedTransformTarget](mcp://flutter/api/widgets/CompositedTransformTarget).

[CompositedTransformTarget](mcp://flutter/api/widgets/CompositedTransformTarget)
A widget that can be targeted by a [CompositedTransformFollower](mcp://flutter/api/widgets/CompositedTransformFollower).

[CompoundAnimation](mcp://flutter/api/animation/CompoundAnimation)<T>
An interface for combining multiple Animations. Subclasses need only
implement the `value` getter to control how the child animations are
combined. Can be chained to combine more than 2 animations.

[ConstantTween](mcp://flutter/api/animation/ConstantTween)<T>
A tween with a constant value.

[ConstrainedBox](mcp://flutter/api/widgets/ConstrainedBox)
A widget that imposes additional constraints on its child.

[ConstrainedLayoutBuilder](mcp://flutter/api/widgets/ConstrainedLayoutBuilder)<ConstraintType extends [Constraints](mcp://flutter/api/rendering/Constraints)>
A specialized [AbstractLayoutBuilder](mcp://flutter/api/widgets/AbstractLayoutBuilder) whose widget subtree depends on the
incoming `ConstraintType` that will be imposed on the widget.

[ConstraintsTransformBox](mcp://flutter/api/widgets/ConstraintsTransformBox)
A container widget that applies an arbitrary transform to its constraints,
and sizes its child using the resulting [BoxConstraints](mcp://flutter/api/rendering/BoxConstraints), optionally
clipping, or treating the overflow as an error.

[Container](mcp://flutter/api/widgets/Container)
A convenience widget that combines common painting, positioning, and sizing
widgets.

[ContentInsertionConfiguration](mcp://flutter/api/widgets/ContentInsertionConfiguration)
Configures the ability to insert media content through the soft keyboard.

[ContextAction](mcp://flutter/api/widgets/ContextAction)<T extends [Intent](mcp://flutter/api/widgets/Intent)>
An abstract [Action](mcp://flutter/api/widgets/Action) subclass that adds an optional [BuildContext](mcp://flutter/api/widgets/BuildContext) to the
[isEnabled](mcp://flutter/api/widgets/ContextAction/isEnabled) and [invoke](mcp://flutter/api/widgets/ContextAction/invoke) methods to be able to provide context to actions.

[ContextMenuButtonItem](mcp://flutter/api/widgets/ContextMenuButtonItem)
The type and callback for a context menu button.

[ContextMenuController](mcp://flutter/api/widgets/ContextMenuController)
Builds and manages a context menu at a given location.

[ContinuousRectangleBorder](mcp://flutter/api/painting/ContinuousRectangleBorder)
A rectangular border with smooth continuous transitions between the straight
sides and the rounded corners.

[CopySelectionTextIntent](mcp://flutter/api/widgets/CopySelectionTextIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a user interaction that attempts to copy or cut
the current selection in the field.

[Cubic](mcp://flutter/api/animation/Cubic)
A cubic polynomial mapping of the unit interval.

[Curve](mcp://flutter/api/animation/Curve)
An parametric animation easing curve, i.e. a mapping of the unit interval to
the unit interval.

[Curve2D](mcp://flutter/api/animation/Curve2D)
Abstract class that defines an API for evaluating 2D parametric curves.

[Curve2DSample](mcp://flutter/api/animation/Curve2DSample)
A class that holds a sample of a 2D parametric curve, containing the [value](mcp://flutter/api/animation/Curve2DSample/value) (the X, Y coordinates) of the curve at the parametric value [t](mcp://flutter/api/animation/Curve2DSample/t).

[CurvedAnimation](mcp://flutter/api/animation/CurvedAnimation)
An animation that applies a curve to another animation.

[Curves](mcp://flutter/api/animation/Curves)
A collection of common animation curves.

[CurveTween](mcp://flutter/api/animation/CurveTween)
Transforms the value of the given animation by the given curve.

[CustomClipper](mcp://flutter/api/rendering/CustomClipper)<T>
An interface for providing custom clips.

[CustomMultiChildLayout](mcp://flutter/api/widgets/CustomMultiChildLayout)
A widget that uses a delegate to size and position multiple children.

[CustomPaint](mcp://flutter/api/widgets/CustomPaint)
A widget that provides a canvas on which to draw during the paint phase.

[CustomPainter](mcp://flutter/api/rendering/CustomPainter)
The interface used by [CustomPaint](mcp://flutter/api/widgets/CustomPaint) (in the widgets library) and
[RenderCustomPaint](mcp://flutter/api/rendering/RenderCustomPaint) (in the rendering library).

[CustomPainterSemantics](mcp://flutter/api/rendering/CustomPainterSemantics)
Contains properties describing information drawn in a rectangle contained by
the [Canvas](mcp://flutter/api/dart-ui/Canvas) used by a [CustomPaint](mcp://flutter/api/widgets/CustomPaint).

[CustomScrollView](mcp://flutter/api/widgets/CustomScrollView)
A [ScrollView](mcp://flutter/api/widgets/ScrollView) that creates custom scroll effects using [slivers](mcp://flutter/api/widgets/CustomScrollView/slivers).

[CustomSingleChildLayout](mcp://flutter/api/widgets/CustomSingleChildLayout)
A widget that defers the layout of its single child to a delegate.

[DebugCreator](mcp://flutter/api/widgets/DebugCreator)
A wrapper class for the [Element](mcp://flutter/api/widgets/Element) that is the creator of a [RenderObject](mcp://flutter/api/rendering/RenderObject).

[DecoratedBox](mcp://flutter/api/widgets/DecoratedBox)
A widget that paints a [Decoration](mcp://flutter/api/painting/Decoration) either before or after its child paints.

[DecoratedBoxTransition](mcp://flutter/api/widgets/DecoratedBoxTransition)
Animated version of a [DecoratedBox](mcp://flutter/api/widgets/DecoratedBox) that animates the different properties
of its [Decoration](mcp://flutter/api/painting/Decoration).

[DecoratedSliver](mcp://flutter/api/widgets/DecoratedSliver)
A sliver widget that paints a [Decoration](mcp://flutter/api/painting/Decoration) either before or after its child
paints.

[Decoration](mcp://flutter/api/painting/Decoration)
A description of a box decoration (a decoration applied to a [Rect](mcp://flutter/api/dart-ui/Rect)).

[DecorationImage](mcp://flutter/api/painting/DecorationImage)
An image for a box decoration.

[DecorationImagePainter](mcp://flutter/api/painting/DecorationImagePainter)
The painter for a [DecorationImage](mcp://flutter/api/painting/DecorationImage).

[DecorationTween](mcp://flutter/api/widgets/DecorationTween)
An interpolation between two [Decoration](mcp://flutter/api/painting/Decoration) s.

[DefaultAssetBundle](mcp://flutter/api/widgets/DefaultAssetBundle)
A widget that determines the default asset bundle for its descendants.

[DefaultPlatformMenuDelegate](mcp://flutter/api/widgets/DefaultPlatformMenuDelegate)
The platform menu delegate that handles the built-in macOS platform menu
generation using the 'flutter/menu' channel.

[DefaultSelectionStyle](mcp://flutter/api/widgets/DefaultSelectionStyle)
The selection style to apply to descendant [EditableText](mcp://flutter/api/widgets/EditableText) widgets which
don't have an explicit style.

[DefaultTextEditingShortcuts](mcp://flutter/api/widgets/DefaultTextEditingShortcuts)
A widget with the shortcuts used for the default text editing behavior.

[DefaultTextHeightBehavior](mcp://flutter/api/widgets/DefaultTextHeightBehavior)
The [TextHeightBehavior](mcp://flutter/api/dart-ui/TextHeightBehavior) that will apply to descendant [Text](mcp://flutter/api/widgets/Text) and [EditableText](mcp://flutter/api/widgets/EditableText) widgets which have not explicitly set [Text.textHeightBehavior](mcp://flutter/api/widgets/Text/textHeightBehavior).

[DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle)
The text style to apply to descendant [Text](mcp://flutter/api/widgets/Text) widgets which don't have an
explicit style.

[DefaultTextStyleTransition](mcp://flutter/api/widgets/DefaultTextStyleTransition)
Animated version of a [DefaultTextStyle](mcp://flutter/api/widgets/DefaultTextStyle) that animates the different properties
of its [TextStyle](mcp://flutter/api/painting/TextStyle).

[DefaultTransitionDelegate](mcp://flutter/api/widgets/DefaultTransitionDelegate)<T>
The default implementation of [TransitionDelegate](mcp://flutter/api/widgets/TransitionDelegate) that the [Navigator](mcp://flutter/api/widgets/Navigator) will
use if its [Navigator.transitionDelegate](mcp://flutter/api/widgets/Navigator/transitionDelegate) is not specified.

[DefaultWidgetsLocalizations](mcp://flutter/api/widgets/DefaultWidgetsLocalizations)
US English localizations for the widgets library.

[DeleteCharacterIntent](mcp://flutter/api/widgets/DeleteCharacterIntent)
Deletes the character before or after the caret location, based on whether
`forward` is true.

[DeleteToLineBreakIntent](mcp://flutter/api/widgets/DeleteToLineBreakIntent)
Deletes from the current caret location to the previous or next soft or hard
line break, based on whether `forward` is true.

[DeleteToNextWordBoundaryIntent](mcp://flutter/api/widgets/DeleteToNextWordBoundaryIntent)
Deletes from the current caret location to the previous or next word
boundary, based on whether `forward` is true.

[DesktopTextSelectionToolbarLayoutDelegate](mcp://flutter/api/widgets/DesktopTextSelectionToolbarLayoutDelegate)
Positions the toolbar at [anchor](mcp://flutter/api/widgets/DesktopTextSelectionToolbarLayoutDelegate/anchor) if it fits, otherwise moves it so that it
just fits fully on-screen.

[DevToolsDeepLinkProperty](mcp://flutter/api/widgets/DevToolsDeepLinkProperty)
Debugging message for DevTools deep links.

[DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)
Defines diagnostics data for a [value](mcp://flutter/api/foundation/DiagnosticsNode/value).

[DirectionalCaretMovementIntent](mcp://flutter/api/widgets/DirectionalCaretMovementIntent)
A [DirectionalTextEditingIntent](mcp://flutter/api/widgets/DirectionalTextEditingIntent) that moves the caret or the selection to a
new location.

[DirectionalFocusAction](mcp://flutter/api/widgets/DirectionalFocusAction)
An [Action](mcp://flutter/api/widgets/Action) that moves the focus to the focusable node in the direction
configured by the associated [DirectionalFocusIntent.direction](mcp://flutter/api/widgets/DirectionalFocusIntent/direction).

[DirectionalFocusIntent](mcp://flutter/api/widgets/DirectionalFocusIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents moving to the next focusable node in the given
[direction](mcp://flutter/api/widgets/DirectionalFocusIntent/direction).

[Directionality](mcp://flutter/api/widgets/Directionality)
A widget that determines the ambient directionality of text and
text-direction-sensitive render objects.

[DirectionalTextEditingIntent](mcp://flutter/api/widgets/DirectionalTextEditingIntent)
A text editing related [Intent](mcp://flutter/api/widgets/Intent) that performs an operation towards a given
direction of the current caret location.

[DisableWidgetInspectorScope](mcp://flutter/api/widgets/DisableWidgetInspectorScope)
Disables the Flutter DevTools Widget Inspector for a [Widget](mcp://flutter/api/widgets/Widget) subtree.

[DismissAction](mcp://flutter/api/widgets/DismissAction)
An [Action](mcp://flutter/api/widgets/Action) that dismisses the focused widget.

[Dismissible](mcp://flutter/api/widgets/Dismissible)
A widget that can be dismissed by dragging in the indicated [direction](mcp://flutter/api/widgets/Dismissible/direction).

[DismissIntent](mcp://flutter/api/widgets/DismissIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that dismisses the currently focused widget.

[DismissMenuAction](mcp://flutter/api/widgets/DismissMenuAction)
An action that closes all the menus associated with the given
[MenuController](mcp://flutter/api/widgets/MenuController).

[DismissUpdateDetails](mcp://flutter/api/widgets/DismissUpdateDetails)
Details for [DismissUpdateCallback](mcp://flutter/api/widgets/DismissUpdateCallback).

[DisplayFeatureSubScreen](mcp://flutter/api/widgets/DisplayFeatureSubScreen)
Positions [child](mcp://flutter/api/widgets/DisplayFeatureSubScreen/child) such that it avoids overlapping any [DisplayFeature](mcp://flutter/api/dart-ui/DisplayFeature) that
splits the screen into sub-screens.

[DisposableBuildContext](mcp://flutter/api/widgets/DisposableBuildContext)<T extends [State](mcp://flutter/api/widgets/State)<[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>>
Provides non-leaking access to a [BuildContext](mcp://flutter/api/widgets/BuildContext).

[DoNothingAction](mcp://flutter/api/widgets/DoNothingAction)
An [Action](mcp://flutter/api/widgets/Action) that doesn't perform any action when invoked.

[DoNothingAndStopPropagationIntent](mcp://flutter/api/widgets/DoNothingAndStopPropagationIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that is bound to a [DoNothingAction](mcp://flutter/api/widgets/DoNothingAction), but, in addition to not
performing an action, also stops the propagation of the key event bound to
this intent to other key event handlers in the focus chain.

[DoNothingAndStopPropagationTextIntent](mcp://flutter/api/widgets/DoNothingAndStopPropagationTextIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to send the event straight to the engine.

[DoNothingIntent](mcp://flutter/api/widgets/DoNothingIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that is bound to a [DoNothingAction](mcp://flutter/api/widgets/DoNothingAction).

[DragBoundary](mcp://flutter/api/widgets/DragBoundary)
Provides a [DragBoundaryDelegate](mcp://flutter/api/widgets/DragBoundaryDelegate) for its descendants whose bounds are those defined by this widget.

[DragBoundaryDelegate](mcp://flutter/api/widgets/DragBoundaryDelegate)<T>
The interface for defining the algorithm for a boundary that a specified shape is dragged within.

[DragDownDetails](mcp://flutter/api/gestures/DragDownDetails)
Details object for callbacks that use [GestureDragDownCallback](mcp://flutter/api/gestures/GestureDragDownCallback).

[DragEndDetails](mcp://flutter/api/gestures/DragEndDetails)
Details object for callbacks that use [GestureDragEndCallback](mcp://flutter/api/gestures/GestureDragEndCallback).

[Draggable](mcp://flutter/api/widgets/Draggable)<T extends [Object](mcp://flutter/api/dart-core/Object)>
A widget that can be dragged from to a [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DraggableDetails](mcp://flutter/api/widgets/DraggableDetails)
Represents the details when a specific pointer event occurred on
the [Draggable](mcp://flutter/api/widgets/Draggable).

[DraggableScrollableActuator](mcp://flutter/api/widgets/DraggableScrollableActuator)
A widget that can notify a descendent [DraggableScrollableSheet](mcp://flutter/api/widgets/DraggableScrollableSheet) that it
should reset its position to the initial state.

[DraggableScrollableController](mcp://flutter/api/widgets/DraggableScrollableController)
Controls a [DraggableScrollableSheet](mcp://flutter/api/widgets/DraggableScrollableSheet).

[DraggableScrollableNotification](mcp://flutter/api/widgets/DraggableScrollableNotification)
A [Notification](mcp://flutter/api/widgets/Notification) related to the extent, which is the size, and scroll
offset, which is the position of the child list, of the
[DraggableScrollableSheet](mcp://flutter/api/widgets/DraggableScrollableSheet).

[DraggableScrollableSheet](mcp://flutter/api/widgets/DraggableScrollableSheet)
A container for a [Scrollable](mcp://flutter/api/widgets/Scrollable) that responds to drag gestures by resizing
the scrollable until a limit is reached, and then scrolling.

[DragScrollActivity](mcp://flutter/api/widgets/DragScrollActivity)
The activity a scroll view performs when the user drags their finger
across the screen.

[DragStartDetails](mcp://flutter/api/gestures/DragStartDetails)
Details object for callbacks that use [GestureDragStartCallback](mcp://flutter/api/gestures/GestureDragStartCallback).

[DragTarget](mcp://flutter/api/widgets/DragTarget)<T extends [Object](mcp://flutter/api/dart-core/Object)>
A widget that receives data when a [Draggable](mcp://flutter/api/widgets/Draggable) widget is dropped.

[DragTargetDetails](mcp://flutter/api/widgets/DragTargetDetails)<T>
Represents the details when a pointer event occurred on the [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DragUpdateDetails](mcp://flutter/api/gestures/DragUpdateDetails)
Details object for callbacks that use [GestureDragUpdateCallback](mcp://flutter/api/gestures/GestureDragUpdateCallback).

[DrivenScrollActivity](mcp://flutter/api/widgets/DrivenScrollActivity)
An activity that drives a scroll view through a given animation.

[DualTransitionBuilder](mcp://flutter/api/widgets/DualTransitionBuilder)
A transition builder that animates its [child](mcp://flutter/api/widgets/DualTransitionBuilder/child) based on the
[AnimationStatus](mcp://flutter/api/animation/AnimationStatus) of the provided [animation](mcp://flutter/api/widgets/DualTransitionBuilder/animation).

[EdgeDraggingAutoScroller](mcp://flutter/api/widgets/EdgeDraggingAutoScroller)
An auto scroller that scrolls the [scrollable](mcp://flutter/api/widgets/EdgeDraggingAutoScroller/scrollable) if a drag gesture drags close
to its edge.

[EdgeInsets](mcp://flutter/api/painting/EdgeInsets)
An immutable set of offsets in each of the four cardinal directions.

[EdgeInsetsDirectional](mcp://flutter/api/painting/EdgeInsetsDirectional)
An immutable set of offsets in each of the four cardinal directions, but
whose horizontal components are dependent on the writing direction.

[EdgeInsetsGeometry](mcp://flutter/api/painting/EdgeInsetsGeometry)
Base class for [EdgeInsets](mcp://flutter/api/painting/EdgeInsets) that allows for text-direction aware
resolution.

[EdgeInsetsGeometryTween](mcp://flutter/api/widgets/EdgeInsetsGeometryTween)
An interpolation between two [EdgeInsetsGeometry](mcp://flutter/api/painting/EdgeInsetsGeometry) s.

[EdgeInsetsTween](mcp://flutter/api/widgets/EdgeInsetsTween)
An interpolation between two [EdgeInsets](mcp://flutter/api/painting/EdgeInsets) s.

[EditableText](mcp://flutter/api/widgets/EditableText)
A basic text input field.

[EditableTextState](mcp://flutter/api/widgets/EditableTextState)
State for an [EditableText](mcp://flutter/api/widgets/EditableText).

[EditableTextTapOutsideIntent](mcp://flutter/api/widgets/EditableTextTapOutsideIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a tap outside the field.

[EditableTextTapUpOutsideIntent](mcp://flutter/api/widgets/EditableTextTapUpOutsideIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a tap outside the field.

[ElasticInCurve](mcp://flutter/api/animation/ElasticInCurve)
An oscillating curve that grows in magnitude while overshooting its bounds.

[ElasticInOutCurve](mcp://flutter/api/animation/ElasticInOutCurve)
An oscillating curve that grows and then shrinks in magnitude while
overshooting its bounds.

[ElasticOutCurve](mcp://flutter/api/animation/ElasticOutCurve)
An oscillating curve that shrinks in magnitude while overshooting its bounds.

[Element](mcp://flutter/api/widgets/Element)
An instantiation of a [Widget](mcp://flutter/api/widgets/Widget) at a particular location in the tree.

[EmptyTextSelectionControls](mcp://flutter/api/widgets/EmptyTextSelectionControls)
Text selection controls that do not show any toolbars or handles.

[EnableWidgetInspectorScope](mcp://flutter/api/widgets/EnableWidgetInspectorScope)
Enables the Flutter DevTools Widget Inspector for a [Widget](mcp://flutter/api/widgets/Widget) subtree.

[ErrorDescription](mcp://flutter/api/foundation/ErrorDescription)
An explanation of the problem and its cause, any information that may help
track down the problem, background information, etc.

[ErrorHint](mcp://flutter/api/foundation/ErrorHint)
An [ErrorHint](mcp://flutter/api/foundation/ErrorHint) provides specific, non-obvious advice that may be applicable.

[ErrorSummary](mcp://flutter/api/foundation/ErrorSummary)
A short (one line) description of the problem that was detected.

[ErrorWidget](mcp://flutter/api/widgets/ErrorWidget)
A widget that renders an exception's message.

[ExactAssetImage](mcp://flutter/api/painting/ExactAssetImage)
Fetches an image from an [AssetBundle](mcp://flutter/api/services/AssetBundle), associating it with the given scale.

[ExcludeFocus](mcp://flutter/api/widgets/ExcludeFocus)
A widget that controls whether or not the descendants of this widget are
focusable.

[ExcludeFocusTraversal](mcp://flutter/api/widgets/ExcludeFocusTraversal)
A widget that controls whether or not the descendants of this widget are
traversable.

[ExcludeSemantics](mcp://flutter/api/widgets/ExcludeSemantics)
A widget that drops all the semantics of its descendants.

[Expanded](mcp://flutter/api/widgets/Expanded)
A widget that expands a child of a [Row](mcp://flutter/api/widgets/Row), [Column](mcp://flutter/api/widgets/Column), or [Flex](mcp://flutter/api/widgets/Flex) so that the child fills the available space.

[ExpandSelectionToDocumentBoundaryIntent](mcp://flutter/api/widgets/ExpandSelectionToDocumentBoundaryIntent)
Expands the current selection to the document boundary in the direction
given by [forward](mcp://flutter/api/widgets/DirectionalTextEditingIntent/forward).

[ExpandSelectionToLineBreakIntent](mcp://flutter/api/widgets/ExpandSelectionToLineBreakIntent)
Expands the current selection to the closest line break in the direction
given by [forward](mcp://flutter/api/widgets/DirectionalTextEditingIntent/forward).

[Expansible](mcp://flutter/api/widgets/Expansible)
A [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) that expands and collapses.

[ExpansibleController](mcp://flutter/api/widgets/ExpansibleController)
A controller for managing the expansion state of an [Expansible](mcp://flutter/api/widgets/Expansible).

[ExtendSelectionByCharacterIntent](mcp://flutter/api/widgets/ExtendSelectionByCharacterIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the previous or the next character
boundary.

[ExtendSelectionByPageIntent](mcp://flutter/api/widgets/ExtendSelectionByPageIntent)
Scrolls up or down by page depending on the [forward](mcp://flutter/api/widgets/DirectionalTextEditingIntent/forward) parameter.
Extends the selection up or down by page based on the [forward](mcp://flutter/api/widgets/DirectionalTextEditingIntent/forward) parameter.

[ExtendSelectionToDocumentBoundaryIntent](mcp://flutter/api/widgets/ExtendSelectionToDocumentBoundaryIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the start or the end of the document.

[ExtendSelectionToLineBreakIntent](mcp://flutter/api/widgets/ExtendSelectionToLineBreakIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the closest line break in the direction
given by [forward](mcp://flutter/api/widgets/DirectionalTextEditingIntent/forward).

[ExtendSelectionToNextParagraphBoundaryIntent](mcp://flutter/api/widgets/ExtendSelectionToNextParagraphBoundaryIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the previous or the next paragraph
boundary.

[ExtendSelectionToNextParagraphBoundaryOrCaretLocationIntent](mcp://flutter/api/widgets/ExtendSelectionToNextParagraphBoundaryOrCaretLocationIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the previous or the next paragraph
boundary depending on the [forward](mcp://flutter/api/widgets/DirectionalTextEditingIntent/forward) parameter.

[ExtendSelectionToNextWordBoundaryIntent](mcp://flutter/api/widgets/ExtendSelectionToNextWordBoundaryIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the previous or the next word
boundary.

[ExtendSelectionToNextWordBoundaryOrCaretLocationIntent](mcp://flutter/api/widgets/ExtendSelectionToNextWordBoundaryOrCaretLocationIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the previous or the next word
boundary, or the [TextSelection.base](mcp://flutter/api/services/TextSelection/base) position if it's closer in the move
direction.

[ExtendSelectionVerticallyToAdjacentLineIntent](mcp://flutter/api/widgets/ExtendSelectionVerticallyToAdjacentLineIntent)
Extends, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the closest position on the adjacent
line.

[ExtendSelectionVerticallyToAdjacentPageIntent](mcp://flutter/api/widgets/ExtendSelectionVerticallyToAdjacentPageIntent)
Expands, or moves the current selection from the current
[TextSelection.extent](mcp://flutter/api/services/TextSelection/extent) position to the closest position on the adjacent
page.

[FadeInImage](mcp://flutter/api/widgets/FadeInImage)
An image that shows a [placeholder](mcp://flutter/api/widgets/FadeInImage/placeholder) image while the target [image](mcp://flutter/api/widgets/FadeInImage/image) is
loading, then fades in the new image when it loads.

[FadeTransition](mcp://flutter/api/widgets/FadeTransition)
Animates the opacity of a widget.

[Feedback](mcp://flutter/api/widgets/Feedback)
Provides platform-specific acoustic and/or haptic feedback for certain
actions.

[FileImage](mcp://flutter/api/painting/FileImage)
Decodes the given [File](mcp://flutter/api/dart-io/File) object as an image, associating it with the given
scale.

[FittedBox](mcp://flutter/api/widgets/FittedBox)
Scales and positions its child within itself according to [fit](mcp://flutter/api/widgets/FittedBox/fit).

[FittedSizes](mcp://flutter/api/painting/FittedSizes)
The pair of sizes returned by [applyBoxFit](mcp://flutter/api/painting/applyBoxFit).

[FixedColumnWidth](mcp://flutter/api/rendering/FixedColumnWidth)
Sizes the column to a specific number of pixels.

[FixedExtentMetrics](mcp://flutter/api/widgets/FixedExtentMetrics)
Metrics for a [ScrollPosition](mcp://flutter/api/widgets/ScrollPosition) to a scroll view with fixed item sizes.

[FixedExtentScrollController](mcp://flutter/api/widgets/FixedExtentScrollController)
A controller for scroll views whose items have the same size.

[FixedExtentScrollPhysics](mcp://flutter/api/widgets/FixedExtentScrollPhysics)
A snapping physics that always lands directly on items instead of anywhere
within the scroll extent.

[FixedScrollMetrics](mcp://flutter/api/widgets/FixedScrollMetrics)
An immutable snapshot of values associated with a [Scrollable](mcp://flutter/api/widgets/Scrollable) viewport.

[Flex](mcp://flutter/api/widgets/Flex)
A widget that displays its children in a one-dimensional array.

[FlexColumnWidth](mcp://flutter/api/rendering/FlexColumnWidth)
Sizes the column by taking a part of the remaining space once all
the other columns have been laid out.

[Flexible](mcp://flutter/api/widgets/Flexible)
A widget that controls how a child of a [Row](mcp://flutter/api/widgets/Row), [Column](mcp://flutter/api/widgets/Column), or [Flex](mcp://flutter/api/widgets/Flex) flexes.

[FlippedCurve](mcp://flutter/api/animation/FlippedCurve)
A curve that is the reversed inversion of its given curve.

[FlippedTweenSequence](mcp://flutter/api/animation/FlippedTweenSequence)
Enables creating a flipped [Animation](mcp://flutter/api/animation/Animation) whose value is defined by a sequence
of [Tween](mcp://flutter/api/animation/Tween) s.

[Flow](mcp://flutter/api/widgets/Flow)
A widget that sizes and positions children efficiently, according to the
logic in a [FlowDelegate](mcp://flutter/api/rendering/FlowDelegate).

[FlowDelegate](mcp://flutter/api/rendering/FlowDelegate)
A delegate that controls the appearance of a flow layout.

[FlowPaintingContext](mcp://flutter/api/rendering/FlowPaintingContext)
A context in which a [FlowDelegate](mcp://flutter/api/rendering/FlowDelegate) paints.

[FlutterErrorDetails](mcp://flutter/api/foundation/FlutterErrorDetails)
Class for information provided to [FlutterExceptionHandler](mcp://flutter/api/foundation/FlutterExceptionHandler) callbacks.

[FlutterLogo](mcp://flutter/api/widgets/FlutterLogo)
The Flutter logo, in widget form. This widget respects the [IconTheme](mcp://flutter/api/widgets/IconTheme).
For guidelines on using the Flutter logo, visit <https://flutter.dev/brand>.

[FlutterLogoDecoration](mcp://flutter/api/painting/FlutterLogoDecoration)
An immutable description of how to paint Flutter's logo.

[Focus](mcp://flutter/api/widgets/Focus)
A widget that manages a [FocusNode](mcp://flutter/api/widgets/FocusNode) to allow keyboard focus to be given
to this widget and its descendants.

[FocusableActionDetector](mcp://flutter/api/widgets/FocusableActionDetector)
A widget that combines the functionality of [Actions](mcp://flutter/api/widgets/Actions), [Shortcuts](mcp://flutter/api/widgets/Shortcuts),
[MouseRegion](mcp://flutter/api/widgets/MouseRegion) and a [Focus](mcp://flutter/api/widgets/Focus) widget to create a detector that defines actions
and key bindings, and provides callbacks for handling focus and hover
highlights.

[FocusAttachment](mcp://flutter/api/widgets/FocusAttachment)
An attachment point for a [FocusNode](mcp://flutter/api/widgets/FocusNode).

[FocusManager](mcp://flutter/api/widgets/FocusManager)
Manages the focus tree.

[FocusNode](mcp://flutter/api/widgets/FocusNode)
An object that can be used by a stateful widget to obtain the keyboard focus
and to handle keyboard events.

[FocusOrder](mcp://flutter/api/widgets/FocusOrder)
Base class for all sort orders for [OrderedTraversalPolicy](mcp://flutter/api/widgets/OrderedTraversalPolicy) traversal.

[FocusScope](mcp://flutter/api/widgets/FocusScope)
A [FocusScope](mcp://flutter/api/widgets/FocusScope) is similar to a [Focus](mcp://flutter/api/widgets/Focus), but also serves as a scope for its
descendants, restricting focus traversal to the scoped controls.

[FocusScopeNode](mcp://flutter/api/widgets/FocusScopeNode)
A subclass of [FocusNode](mcp://flutter/api/widgets/FocusNode) that acts as a scope for its descendants,
maintaining information about which descendant is currently or was last
focused.

[FocusTraversalGroup](mcp://flutter/api/widgets/FocusTraversalGroup)
A widget that describes the inherited focus policy for focus traversal for
its descendants, grouping them into a separate traversal group.

[FocusTraversalOrder](mcp://flutter/api/widgets/FocusTraversalOrder)
An inherited widget that describes the order in which its child subtree
should be traversed.

[FocusTraversalPolicy](mcp://flutter/api/widgets/FocusTraversalPolicy)
Determines how focusable widgets are traversed within a [FocusTraversalGroup](mcp://flutter/api/widgets/FocusTraversalGroup).

[FontFeature](mcp://flutter/api/dart-ui/FontFeature)
A feature tag and value that affect the selection of glyphs in a font.

[FontVariation](mcp://flutter/api/dart-ui/FontVariation)
An axis tag and value that can be used to customize variable fonts.

[FontWeight](mcp://flutter/api/dart-ui/FontWeight)
The thickness of the glyphs used to draw the text.

[ForcePressDetails](mcp://flutter/api/gestures/ForcePressDetails)
Details object for callbacks that use [GestureForcePressStartCallback](mcp://flutter/api/gestures/GestureForcePressStartCallback),
[GestureForcePressPeakCallback](mcp://flutter/api/gestures/GestureForcePressPeakCallback), [GestureForcePressEndCallback](mcp://flutter/api/gestures/GestureForcePressEndCallback) or
[GestureForcePressUpdateCallback](mcp://flutter/api/gestures/GestureForcePressUpdateCallback).

[Form](mcp://flutter/api/widgets/Form)
An optional container for grouping together multiple form field widgets
(e.g. [TextField](mcp://flutter/api/material/TextField) widgets).

[FormField](mcp://flutter/api/widgets/FormField)<T>
A single form field.

[FormFieldState](mcp://flutter/api/widgets/FormFieldState)<T>
The current state of a [FormField](mcp://flutter/api/widgets/FormField). Passed to the [FormFieldBuilder](mcp://flutter/api/widgets/FormFieldBuilder) method
for use in constructing the form field's widget.

[FormState](mcp://flutter/api/widgets/FormState)
State associated with a [Form](mcp://flutter/api/widgets/Form) widget.

[FractionallySizedBox](mcp://flutter/api/widgets/FractionallySizedBox)
A widget that sizes its child to a fraction of the total available space.
For more details about the layout algorithm, see
[RenderFractionallySizedOverflowBox](mcp://flutter/api/rendering/RenderFractionallySizedOverflowBox).

[FractionalOffset](mcp://flutter/api/painting/FractionalOffset)
An offset that's expressed as a fraction of a [Size](mcp://flutter/api/dart-ui/Size).

[FractionalOffsetTween](mcp://flutter/api/rendering/FractionalOffsetTween)
An interpolation between two fractional offsets.

[FractionalTranslation](mcp://flutter/api/widgets/FractionalTranslation)
Applies a translation transformation before painting its child.

[FractionColumnWidth](mcp://flutter/api/rendering/FractionColumnWidth)
Sizes the column to a fraction of the table's constraints' maxWidth.

[FutureBuilder](mcp://flutter/api/widgets/FutureBuilder)<T>
A widget that builds itself based on the latest snapshot of interaction with
a [Future](mcp://flutter/api/dart-async/Future).

[GestureDetector](mcp://flutter/api/widgets/GestureDetector)
A widget that detects gestures.

[GestureRecognizerFactory](mcp://flutter/api/widgets/GestureRecognizerFactory)<T extends [GestureRecognizer](mcp://flutter/api/gestures/GestureRecognizer)>
Factory for creating gesture recognizers.

[GestureRecognizerFactoryWithHandlers](mcp://flutter/api/widgets/GestureRecognizerFactoryWithHandlers)<T extends [GestureRecognizer](mcp://flutter/api/gestures/GestureRecognizer)>
Factory for creating gesture recognizers that delegates to callbacks.

[GlobalKey](mcp://flutter/api/widgets/GlobalKey)<T extends [State](mcp://flutter/api/widgets/State)<[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>>
A key that is unique across the entire app.

[GlobalObjectKey](mcp://flutter/api/widgets/GlobalObjectKey)<T extends [State](mcp://flutter/api/widgets/State)<[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>>
A global key that takes its identity from the object used as its value.

[GlowingOverscrollIndicator](mcp://flutter/api/widgets/GlowingOverscrollIndicator)
A visual indication that a scroll view has overscrolled.

[GlyphInfo](mcp://flutter/api/dart-ui/GlyphInfo)
The measurements of a character (or a sequence of visually connected
characters) within a paragraph.

[Gradient](mcp://flutter/api/painting/Gradient)
A 2D gradient.

[GradientRotation](mcp://flutter/api/painting/GradientRotation)
A [GradientTransform](mcp://flutter/api/painting/GradientTransform) that rotates the gradient around the center-point of
its bounding box.

[GradientTransform](mcp://flutter/api/painting/GradientTransform)
Base class for transforming gradient shaders without applying the same
transform to the entire canvas.

[GridPaper](mcp://flutter/api/widgets/GridPaper)
A widget that draws a rectilinear grid of lines one pixel wide.

[GridView](mcp://flutter/api/widgets/GridView)
A scrollable, 2D array of widgets.

[Hero](mcp://flutter/api/widgets/Hero)
A widget that marks its child as being a candidate for
[hero animations](https://docs.flutter.dev/ui/animations/hero-animations).

[HeroController](mcp://flutter/api/widgets/HeroController)
A [Navigator](mcp://flutter/api/widgets/Navigator) observer that manages [Hero](mcp://flutter/api/widgets/Hero) transitions.

[HeroControllerScope](mcp://flutter/api/widgets/HeroControllerScope)
An inherited widget to host a hero controller.

[HeroMode](mcp://flutter/api/widgets/HeroMode)
Enables or disables [Hero](mcp://flutter/api/widgets/Hero) es in the widget subtree.

[HoldScrollActivity](mcp://flutter/api/widgets/HoldScrollActivity)
A scroll activity that does nothing but can be released to resume
normal idle behavior.

[HSLColor](mcp://flutter/api/painting/HSLColor)
A color represented using [alpha](mcp://flutter/api/painting/HSLColor/alpha), [hue](mcp://flutter/api/painting/HSLColor/hue), [saturation](mcp://flutter/api/painting/HSLColor/saturation), and [lightness](mcp://flutter/api/painting/HSLColor/lightness).

[HSVColor](mcp://flutter/api/painting/HSVColor)
A color represented using [alpha](mcp://flutter/api/painting/HSVColor/alpha), [hue](mcp://flutter/api/painting/HSVColor/hue), [saturation](mcp://flutter/api/painting/HSVColor/saturation), and [value](mcp://flutter/api/painting/HSVColor/value).

[HtmlElementView](mcp://flutter/api/widgets/HtmlElementView)
Embeds an HTML element in the Widget hierarchy in Flutter web.

[Icon](mcp://flutter/api/widgets/Icon)
A graphical icon widget drawn with a glyph from a font described in
an [IconData](mcp://flutter/api/widgets/IconData) such as material's predefined [IconData](mcp://flutter/api/widgets/IconData) s in [Icons](mcp://flutter/api/material/Icons).

[IconData](mcp://flutter/api/widgets/IconData)
A description of an icon fulfilled by a font glyph.

[IconDataProperty](mcp://flutter/api/widgets/IconDataProperty)
[DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) that has an [IconData](mcp://flutter/api/widgets/IconData) as value.

[IconTheme](mcp://flutter/api/widgets/IconTheme)
Controls the default properties of icons in a widget subtree.

[IconThemeData](mcp://flutter/api/widgets/IconThemeData)
Defines the size, font variations, color, opacity, and shadows of icons.

[IdleScrollActivity](mcp://flutter/api/widgets/IdleScrollActivity)
A scroll activity that does nothing.

[IgnoreBaseline](mcp://flutter/api/widgets/IgnoreBaseline)
A widget that causes the parent to ignore the [child](mcp://flutter/api/widgets/SingleChildRenderObjectWidget/child) for the purposes
of baseline alignment.

[IgnorePointer](mcp://flutter/api/widgets/IgnorePointer)
A widget that is invisible during hit testing.

[Image](mcp://flutter/api/widgets/Image)
A widget that displays an image.

[ImageCache](mcp://flutter/api/painting/ImageCache)
Class for caching images.

[ImageCacheStatus](mcp://flutter/api/painting/ImageCacheStatus)
Information about how the [ImageCache](mcp://flutter/api/painting/ImageCache) is tracking an image.

[ImageChunkEvent](mcp://flutter/api/painting/ImageChunkEvent)
An immutable notification of image bytes that have been incrementally loaded.

[ImageConfiguration](mcp://flutter/api/painting/ImageConfiguration)
Configuration information passed to the [ImageProvider.resolve](mcp://flutter/api/painting/ImageProvider/resolve) method to
select a specific image.

[ImageFiltered](mcp://flutter/api/widgets/ImageFiltered)
Applies an [ImageFilter](mcp://flutter/api/dart-ui/ImageFilter) to its child.

[ImageIcon](mcp://flutter/api/widgets/ImageIcon)
An icon that comes from an [ImageProvider](mcp://flutter/api/painting/ImageProvider), e.g. an [AssetImage](mcp://flutter/api/painting/AssetImage).

[ImageInfo](mcp://flutter/api/painting/ImageInfo)
A [dart:ui.Image](mcp://flutter/api/dart-ui/Image) object with its corresponding scale.

[ImageProvider](mcp://flutter/api/painting/ImageProvider)<T extends [Object](mcp://flutter/api/dart-core/Object)>
Identifies an image without committing to the precise final asset. This
allows a set of images to be identified and for the precise image to later
be resolved based on the environment, e.g. the device pixel ratio.

[ImageShader](mcp://flutter/api/dart-ui/ImageShader)
A shader (as used by [Paint.shader](mcp://flutter/api/dart-ui/Paint/shader)) that tiles an image.

[ImageSizeInfo](mcp://flutter/api/painting/ImageSizeInfo)
Tracks the bytes used by a [dart:ui.Image](mcp://flutter/api/dart-ui/Image) compared to the bytes needed to
paint that image without scaling it.

[ImageStream](mcp://flutter/api/painting/ImageStream)
A handle to an image resource.

[ImageStreamCompleter](mcp://flutter/api/painting/ImageStreamCompleter)
Base class for those that manage the loading of [dart:ui.Image](mcp://flutter/api/dart-ui/Image) objects for
[ImageStream](mcp://flutter/api/painting/ImageStream) s.

[ImageStreamCompleterHandle](mcp://flutter/api/painting/ImageStreamCompleterHandle)
An opaque handle that keeps an [ImageStreamCompleter](mcp://flutter/api/painting/ImageStreamCompleter) alive even if it has
lost its last listener.

[ImageStreamListener](mcp://flutter/api/painting/ImageStreamListener)
Interface for receiving notifications about the loading of an image.

[ImplicitlyAnimatedWidget](mcp://flutter/api/widgets/ImplicitlyAnimatedWidget)
An abstract class for building widgets that animate changes to their
properties.

[ImplicitlyAnimatedWidgetState](mcp://flutter/api/widgets/ImplicitlyAnimatedWidgetState)<T extends [ImplicitlyAnimatedWidget](mcp://flutter/api/widgets/ImplicitlyAnimatedWidget)>
A base class for the `State` of widgets with implicit animations.

[IndexedSemantics](mcp://flutter/api/widgets/IndexedSemantics)
A widget that annotates the child semantics with an index.

[IndexedSlot](mcp://flutter/api/widgets/IndexedSlot)<T extends [Element](mcp://flutter/api/widgets/Element)?>
A value for [Element.slot](mcp://flutter/api/widgets/Element/slot) used for children of
[MultiChildRenderObjectElement](mcp://flutter/api/widgets/MultiChildRenderObjectElement) s.

[IndexedStack](mcp://flutter/api/widgets/IndexedStack)
A [Stack](mcp://flutter/api/widgets/Stack) that shows a single child from a list of children.

[InheritedElement](mcp://flutter/api/widgets/InheritedElement)
An [Element](mcp://flutter/api/widgets/Element) that uses an [InheritedWidget](mcp://flutter/api/widgets/InheritedWidget) as its configuration.

[InheritedModel](mcp://flutter/api/widgets/InheritedModel)<T>
An [InheritedWidget](mcp://flutter/api/widgets/InheritedWidget) that's intended to be used as the base class for models
whose dependents may only depend on one part or "aspect" of the overall
model.

[InheritedModelElement](mcp://flutter/api/widgets/InheritedModelElement)<T>
An [Element](mcp://flutter/api/widgets/Element) that uses a [InheritedModel](mcp://flutter/api/widgets/InheritedModel) as its configuration.

[InheritedNotifier](mcp://flutter/api/widgets/InheritedNotifier)<T extends [Listenable](mcp://flutter/api/foundation/Listenable)>
An inherited widget for a [Listenable](mcp://flutter/api/foundation/Listenable) [notifier](mcp://flutter/api/widgets/InheritedNotifier/notifier), which updates its
dependencies when the [notifier](mcp://flutter/api/widgets/InheritedNotifier/notifier) is triggered.

[InheritedTheme](mcp://flutter/api/widgets/InheritedTheme)
An [InheritedWidget](mcp://flutter/api/widgets/InheritedWidget) that defines visual properties like colors
and text styles, which the [child](mcp://flutter/api/widgets/ProxyWidget/child)'s subtree depends on.

[InheritedWidget](mcp://flutter/api/widgets/InheritedWidget)
Base class for widgets that efficiently propagate information down the tree.

[InlineSpan](mcp://flutter/api/painting/InlineSpan)
An immutable span of inline content which forms part of a paragraph.

[InlineSpanSemanticsInformation](mcp://flutter/api/painting/InlineSpanSemanticsInformation)
The textual and semantic label information for an [InlineSpan](mcp://flutter/api/painting/InlineSpan).

[InspectorButton](mcp://flutter/api/widgets/InspectorButton)
An abstract base class for creating Material or Cupertino-styled inspector
buttons.

[InspectorReferenceData](mcp://flutter/api/widgets/InspectorReferenceData)
Structure to help reference count Dart objects referenced by a GUI tool
using [WidgetInspectorService](mcp://flutter/api/widgets/WidgetInspectorService).

[InspectorSelection](mcp://flutter/api/widgets/InspectorSelection)
Mutable selection state of the inspector.

[InspectorSerializationDelegate](mcp://flutter/api/widgets/InspectorSerializationDelegate)
A delegate that configures how a hierarchy of [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode) s are
serialized by the Flutter Inspector.

[Intent](mcp://flutter/api/widgets/Intent)
An abstract class representing a particular configuration of an [Action](mcp://flutter/api/widgets/Action).

[InteractiveViewer](mcp://flutter/api/widgets/InteractiveViewer)
A widget that enables pan and zoom interactions with its child.

[Interval](mcp://flutter/api/animation/Interval)
A curve that is 0.0 until [begin](mcp://flutter/api/animation/Interval/begin), then curved (according to [curve](mcp://flutter/api/animation/Interval/curve)) from
0.0 at [begin](mcp://flutter/api/animation/Interval/begin) to 1.0 at [end](mcp://flutter/api/animation/Interval/end), then remains 1.0 past [end](mcp://flutter/api/animation/Interval/end).

[IntrinsicColumnWidth](mcp://flutter/api/rendering/IntrinsicColumnWidth)
Sizes the column according to the intrinsic dimensions of all the
cells in that column.

[IntrinsicHeight](mcp://flutter/api/widgets/IntrinsicHeight)
A widget that sizes its child to the child's intrinsic height.

[IntrinsicWidth](mcp://flutter/api/widgets/IntrinsicWidth)
A widget that sizes its child to the child's maximum intrinsic width.

[IntTween](mcp://flutter/api/animation/IntTween)
An interpolation between two integers that rounds.

[IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem)
Describes a context menu button that will be rendered in the iOS system
context menu and not by Flutter itself.

[IOSSystemContextMenuItemCopy](mcp://flutter/api/widgets/IOSSystemContextMenuItemCopy)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the system's built-in
copy button.

[IOSSystemContextMenuItemCustom](mcp://flutter/api/widgets/IOSSystemContextMenuItemCustom)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for custom action buttons
defined by the developer.

[IOSSystemContextMenuItemCut](mcp://flutter/api/widgets/IOSSystemContextMenuItemCut)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the system's built-in
cut button.

[IOSSystemContextMenuItemLiveText](mcp://flutter/api/widgets/IOSSystemContextMenuItemLiveText)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the
system's built-in Live Text button.

[IOSSystemContextMenuItemLookUp](mcp://flutter/api/widgets/IOSSystemContextMenuItemLookUp)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the
system's built-in look up button.

[IOSSystemContextMenuItemPaste](mcp://flutter/api/widgets/IOSSystemContextMenuItemPaste)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the system's built-in
paste button.

[IOSSystemContextMenuItemSearchWeb](mcp://flutter/api/widgets/IOSSystemContextMenuItemSearchWeb)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the
system's built-in search web button.

[IOSSystemContextMenuItemSelectAll](mcp://flutter/api/widgets/IOSSystemContextMenuItemSelectAll)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the system's built-in
select all button.

[IOSSystemContextMenuItemShare](mcp://flutter/api/widgets/IOSSystemContextMenuItemShare)
Creates an instance of [IOSSystemContextMenuItem](mcp://flutter/api/widgets/IOSSystemContextMenuItem) for the
system's built-in share button.

[KeepAlive](mcp://flutter/api/widgets/KeepAlive)
Mark a child as needing to stay alive even when it's in a lazy list that
would otherwise remove it.

[KeepAliveHandle](mcp://flutter/api/widgets/KeepAliveHandle)
A [Listenable](mcp://flutter/api/foundation/Listenable) which can be manually triggered.

[KeepAliveNotification](mcp://flutter/api/widgets/KeepAliveNotification)
Indicates that the subtree through which this notification bubbles must be
kept alive even if it would normally be discarded as an optimization.

[Key](mcp://flutter/api/foundation/Key)
A [Key](mcp://flutter/api/foundation/Key) is an identifier for [Widget](mcp://flutter/api/widgets/Widget) s, [Element](mcp://flutter/api/widgets/Element) s and [SemanticsNode](mcp://flutter/api/semantics/SemanticsNode) s.

[KeyboardInsertedContent](mcp://flutter/api/services/KeyboardInsertedContent)
A class representing rich content (such as a PNG image) inserted via the
system input method.

[KeyboardListener](mcp://flutter/api/widgets/KeyboardListener)
A widget that calls a callback whenever the user presses or releases a key
on a keyboard.

[KeyedSubtree](mcp://flutter/api/widgets/KeyedSubtree)
A widget that builds its child.

[KeyEvent](mcp://flutter/api/services/KeyEvent)
Defines the interface for keyboard key events.

[KeySet](mcp://flutter/api/widgets/KeySet)<T extends [KeyboardKey](mcp://flutter/api/services/KeyboardKey)>
A set of [KeyboardKey](mcp://flutter/api/services/KeyboardKey) s that can be used as the keys in a [Map](mcp://flutter/api/dart-core/Map).

[LabeledGlobalKey](mcp://flutter/api/widgets/LabeledGlobalKey)<T extends [State](mcp://flutter/api/widgets/State)<[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>>
A global key with a debugging label.

[LayerLink](mcp://flutter/api/rendering/LayerLink)
An object that a [LeaderLayer](mcp://flutter/api/rendering/LeaderLayer) can register with.

[LayoutBuilder](mcp://flutter/api/widgets/LayoutBuilder)
Builds a widget tree that can depend on the parent widget's size.

[LayoutChangedNotification](mcp://flutter/api/widgets/LayoutChangedNotification)
Indicates that the layout of one of the descendants of the object receiving
this notification has changed in some way, and that therefore any
assumptions about that layout are no longer valid.

[LayoutId](mcp://flutter/api/widgets/LayoutId)
Metadata for identifying children in a [CustomMultiChildLayout](mcp://flutter/api/widgets/CustomMultiChildLayout).

[LeafRenderObjectElement](mcp://flutter/api/widgets/LeafRenderObjectElement)
An [Element](mcp://flutter/api/widgets/Element) that uses a [LeafRenderObjectWidget](mcp://flutter/api/widgets/LeafRenderObjectWidget) as its configuration.

[LeafRenderObjectWidget](mcp://flutter/api/widgets/LeafRenderObjectWidget)
A superclass for [RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget) s that configure [RenderObject](mcp://flutter/api/rendering/RenderObject) subclasses
that have no children.

[LexicalFocusOrder](mcp://flutter/api/widgets/LexicalFocusOrder)
Can be given to a [FocusTraversalOrder](mcp://flutter/api/widgets/FocusTraversalOrder) widget to use a String to assign a
lexical order to a widget subtree that is using a
[OrderedTraversalPolicy](mcp://flutter/api/widgets/OrderedTraversalPolicy) to define the order in which widgets should be
traversed with the keyboard.

[LimitedBox](mcp://flutter/api/widgets/LimitedBox)
A box that limits its size only when it's unconstrained.

[LinearBorder](mcp://flutter/api/painting/LinearBorder)
An [OutlinedBorder](mcp://flutter/api/painting/OutlinedBorder) like [BoxBorder](mcp://flutter/api/painting/BoxBorder) that allows one to define a rectangular (box) border
in terms of zero to four [LinearBorderEdge](mcp://flutter/api/painting/LinearBorderEdge) s, each of which is rendered as a single line.

[LinearBorderEdge](mcp://flutter/api/painting/LinearBorderEdge)
Defines the relative size and alignment of one [LinearBorder](mcp://flutter/api/painting/LinearBorder) edge.

[LinearGradient](mcp://flutter/api/painting/LinearGradient)
A 2D linear gradient.

[LineMetrics](mcp://flutter/api/dart-ui/LineMetrics)
[LineMetrics](mcp://flutter/api/dart-ui/LineMetrics) stores the measurements and statistics of a single line in the
paragraph.

[ListBody](mcp://flutter/api/widgets/ListBody)
A widget that arranges its children sequentially along a given axis, forcing
them to the dimension of the parent in the other axis.

[Listenable](mcp://flutter/api/foundation/Listenable)
An object that maintains a list of listeners.

[ListenableBuilder](mcp://flutter/api/widgets/ListenableBuilder)
A general-purpose widget for building a widget subtree when a [Listenable](mcp://flutter/api/foundation/Listenable) changes.

[Listener](mcp://flutter/api/widgets/Listener)
A widget that calls callbacks in response to common pointer events.

[ListView](mcp://flutter/api/widgets/ListView)
A scrollable list of widgets arranged linearly.

[ListWheelChildBuilderDelegate](mcp://flutter/api/widgets/ListWheelChildBuilderDelegate)
A delegate that supplies children for [ListWheelScrollView](mcp://flutter/api/widgets/ListWheelScrollView) using a builder
callback.

[ListWheelChildDelegate](mcp://flutter/api/widgets/ListWheelChildDelegate)
A delegate that supplies children for [ListWheelScrollView](mcp://flutter/api/widgets/ListWheelScrollView).

[ListWheelChildListDelegate](mcp://flutter/api/widgets/ListWheelChildListDelegate)
A delegate that supplies children for [ListWheelScrollView](mcp://flutter/api/widgets/ListWheelScrollView) using an
explicit list.

[ListWheelChildLoopingListDelegate](mcp://flutter/api/widgets/ListWheelChildLoopingListDelegate)
A delegate that supplies infinite children for [ListWheelScrollView](mcp://flutter/api/widgets/ListWheelScrollView) by
looping an explicit list.

[ListWheelElement](mcp://flutter/api/widgets/ListWheelElement)
Element that supports building children lazily for [ListWheelViewport](mcp://flutter/api/widgets/ListWheelViewport).

[ListWheelScrollView](mcp://flutter/api/widgets/ListWheelScrollView)
A box in which children on a wheel can be scrolled.

[ListWheelViewport](mcp://flutter/api/widgets/ListWheelViewport)
A viewport showing a subset of children on a wheel.

[LiveTextInputStatusNotifier](mcp://flutter/api/widgets/LiveTextInputStatusNotifier)
A [ValueNotifier](mcp://flutter/api/foundation/ValueNotifier) whose [value](mcp://flutter/api/foundation/ValueNotifier/value) indicates whether the current device supports the Live Text
(OCR) function.

[Locale](mcp://flutter/api/dart-ui/Locale)
An identifier used to select a user's language and formatting preferences.

[LocalHistoryEntry](mcp://flutter/api/widgets/LocalHistoryEntry)
An entry in the history of a [LocalHistoryRoute](mcp://flutter/api/widgets/LocalHistoryRoute).

[Localizations](mcp://flutter/api/widgets/Localizations)
Defines the [Locale](mcp://flutter/api/dart-ui/Locale) for its `child` and the localized resources that the
child depends on.

[LocalizationsDelegate](mcp://flutter/api/widgets/LocalizationsDelegate)<T>
A factory for a set of localized resources of type `T`, to be loaded by a
[Localizations](mcp://flutter/api/widgets/Localizations) widget.

[LocalizationsResolver](mcp://flutter/api/widgets/LocalizationsResolver)
A helper class used to manage localization resolution.

[LocalKey](mcp://flutter/api/foundation/LocalKey)
A key that is not a [GlobalKey](mcp://flutter/api/widgets/GlobalKey).

[LogicalKeySet](mcp://flutter/api/widgets/LogicalKeySet)
A set of [LogicalKeyboardKey](mcp://flutter/api/services/LogicalKeyboardKey) s that can be used as the keys in a map.

[LongPressDraggable](mcp://flutter/api/widgets/LongPressDraggable)<T extends [Object](mcp://flutter/api/dart-core/Object)>
Makes its child draggable starting from long press.

[LongPressEndDetails](mcp://flutter/api/gestures/LongPressEndDetails)
Details for callbacks that use [GestureLongPressEndCallback](mcp://flutter/api/gestures/GestureLongPressEndCallback).

[LongPressMoveUpdateDetails](mcp://flutter/api/gestures/LongPressMoveUpdateDetails)
Details for callbacks that use [GestureLongPressMoveUpdateCallback](mcp://flutter/api/gestures/GestureLongPressMoveUpdateCallback).

[LongPressStartDetails](mcp://flutter/api/gestures/LongPressStartDetails)
Details for callbacks that use [GestureLongPressStartCallback](mcp://flutter/api/gestures/GestureLongPressStartCallback).

[LookupBoundary](mcp://flutter/api/widgets/LookupBoundary)
A lookup boundary controls what entities are visible to descendants of the
boundary via the static lookup methods provided by the boundary.

[MagnifierController](mcp://flutter/api/widgets/MagnifierController)
A controller for a magnifier.

[MagnifierDecoration](mcp://flutter/api/widgets/MagnifierDecoration)
The decorations to put around the loupe in a [RawMagnifier](mcp://flutter/api/widgets/RawMagnifier).

[MagnifierInfo](mcp://flutter/api/widgets/MagnifierInfo)
A data class that contains the geometry information of text layouts
and selection gestures, used to position magnifiers.

[MaskFilter](mcp://flutter/api/dart-ui/MaskFilter)
A mask filter to apply to shapes as they are painted. A mask filter is a
function that takes a bitmap of color pixels, and returns another bitmap of
color pixels.

[Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4)
4D Matrix.
Values are stored in column major order.

[Matrix4Tween](mcp://flutter/api/widgets/Matrix4Tween)
An interpolation between two [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4) s.

[MatrixTransition](mcp://flutter/api/widgets/MatrixTransition)
Animates the [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4) of a transformed widget.

[MatrixUtils](mcp://flutter/api/painting/MatrixUtils)
Utility functions for working with matrices.

[MaxColumnWidth](mcp://flutter/api/rendering/MaxColumnWidth)
Sizes the column such that it is the size that is the maximum of
two column width specifications.

[MediaQuery](mcp://flutter/api/widgets/MediaQuery)
Establishes a subtree in which media queries resolve to the given data.

[MediaQueryData](mcp://flutter/api/widgets/MediaQueryData)
Information about a piece of media (e.g., a window).

[MemoryImage](mcp://flutter/api/painting/MemoryImage)
Decodes the given [Uint8List](mcp://flutter/api/dart-typed_data/Uint8List) buffer as an image, associating it with the
given scale.

[MenuController](mcp://flutter/api/widgets/MenuController)
A controller used to manage a menu created by a subclass of [RawMenuAnchor](mcp://flutter/api/widgets/RawMenuAnchor),
such as [MenuAnchor](mcp://flutter/api/material/MenuAnchor), [MenuBar](mcp://flutter/api/material/MenuBar), [SubmenuButton](mcp://flutter/api/material/SubmenuButton).

[MergeSemantics](mcp://flutter/api/widgets/MergeSemantics)
A widget that merges the semantics of its descendants.

[MetaData](mcp://flutter/api/widgets/MetaData)
Holds opaque meta data in the render tree.

[MinColumnWidth](mcp://flutter/api/rendering/MinColumnWidth)
Sizes the column such that it is the size that is the minimum of
two column width specifications.

[ModalBarrier](mcp://flutter/api/widgets/ModalBarrier)
A widget that prevents the user from interacting with widgets behind itself.

[ModalRoute](mcp://flutter/api/widgets/ModalRoute)<T>
A route that blocks interaction with previous routes.

[MouseCursor](mcp://flutter/api/services/MouseCursor)
An interface for mouse cursor definitions.

[MouseRegion](mcp://flutter/api/widgets/MouseRegion)
A widget that tracks the movement of mice.

[MultiChildLayoutDelegate](mcp://flutter/api/rendering/MultiChildLayoutDelegate)
A delegate that controls the layout of multiple children.

[MultiChildRenderObjectElement](mcp://flutter/api/widgets/MultiChildRenderObjectElement)
An [Element](mcp://flutter/api/widgets/Element) that uses a [MultiChildRenderObjectWidget](mcp://flutter/api/widgets/MultiChildRenderObjectWidget) as its configuration.

[MultiChildRenderObjectWidget](mcp://flutter/api/widgets/MultiChildRenderObjectWidget)
A superclass for [RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget) s that configure [RenderObject](mcp://flutter/api/rendering/RenderObject) subclasses
that have a single list of children. (This superclass only provides the
storage for that child list, it doesn't actually provide the updating
logic.)

[MultiFrameImageStreamCompleter](mcp://flutter/api/painting/MultiFrameImageStreamCompleter)
Manages the decoding and scheduling of image frames.

[MultiSelectableSelectionContainerDelegate](mcp://flutter/api/widgets/MultiSelectableSelectionContainerDelegate)
A delegate that handles events and updates for multiple [Selectable](mcp://flutter/api/rendering/Selectable) children.

[NavigationNotification](mcp://flutter/api/widgets/NavigationNotification)
A notification that a change in navigation has taken place.

[NavigationToolbar](mcp://flutter/api/widgets/NavigationToolbar)
[NavigationToolbar](mcp://flutter/api/widgets/NavigationToolbar) is a layout helper to position 3 widgets or groups of
widgets along a horizontal axis that's sensible for an application's
navigation bar such as in Material Design and in iOS.

[Navigator](mcp://flutter/api/widgets/Navigator)
A widget that manages a set of child widgets with a stack discipline.

[NavigatorObserver](mcp://flutter/api/widgets/NavigatorObserver)
An interface for observing the behavior of a [Navigator](mcp://flutter/api/widgets/Navigator).

[NavigatorPopHandler](mcp://flutter/api/widgets/NavigatorPopHandler)<T>
Enables the handling of system back gestures.

[NavigatorState](mcp://flutter/api/widgets/NavigatorState)
The state for a [Navigator](mcp://flutter/api/widgets/Navigator) widget.

[NestedScrollView](mcp://flutter/api/widgets/NestedScrollView)
A scrolling view inside of which can be nested other scrolling views, with
their scroll positions being intrinsically linked.

[NestedScrollViewState](mcp://flutter/api/widgets/NestedScrollViewState)
The [State](mcp://flutter/api/widgets/State) for a [NestedScrollView](mcp://flutter/api/widgets/NestedScrollView).

[NestedScrollViewViewport](mcp://flutter/api/widgets/NestedScrollViewViewport)
The [Viewport](mcp://flutter/api/widgets/Viewport) variant used by [NestedScrollView](mcp://flutter/api/widgets/NestedScrollView).

[NetworkImage](mcp://flutter/api/painting/NetworkImage)
Fetches the given URL from the network, associating it with the given scale.

[NeverScrollableScrollPhysics](mcp://flutter/api/widgets/NeverScrollableScrollPhysics)
Scroll physics that does not allow the user to scroll.

[NextFocusAction](mcp://flutter/api/widgets/NextFocusAction)
An [Action](mcp://flutter/api/widgets/Action) that moves the focus to the next focusable node in the focus
order.

[NextFocusIntent](mcp://flutter/api/widgets/NextFocusIntent)
An [Intent](mcp://flutter/api/widgets/Intent) bound to [NextFocusAction](mcp://flutter/api/widgets/NextFocusAction), which moves the focus to the next
focusable node in the focus traversal order.

[NotchedShape](mcp://flutter/api/painting/NotchedShape)
A shape with a notch in its outline.

[Notification](mcp://flutter/api/widgets/Notification)
A notification that can bubble up the widget tree.

[NotificationListener](mcp://flutter/api/widgets/NotificationListener)<T extends [Notification](mcp://flutter/api/widgets/Notification)>
A widget that listens for [Notification](mcp://flutter/api/widgets/Notification) s bubbling up the tree.

[NumericFocusOrder](mcp://flutter/api/widgets/NumericFocusOrder)
Can be given to a [FocusTraversalOrder](mcp://flutter/api/widgets/FocusTraversalOrder) widget to assign a numerical order
to a widget subtree that is using a [OrderedTraversalPolicy](mcp://flutter/api/widgets/OrderedTraversalPolicy) to define the
order in which widgets should be traversed with the keyboard.

[ObjectKey](mcp://flutter/api/widgets/ObjectKey)
A key that takes its identity from the object used as its value.

[Offset](mcp://flutter/api/dart-ui/Offset)
An immutable 2D floating-point offset.

[Offstage](mcp://flutter/api/widgets/Offstage)
A widget that lays the child out as if it was in the tree, but without
painting anything, without making the child available for hit testing, and
without taking any room in the parent.

[OneFrameImageStreamCompleter](mcp://flutter/api/painting/OneFrameImageStreamCompleter)
Manages the loading of [dart:ui.Image](mcp://flutter/api/dart-ui/Image) objects for static [ImageStream](mcp://flutter/api/painting/ImageStream) s (those
with only one frame).

[Opacity](mcp://flutter/api/widgets/Opacity)
A widget that makes its child partially transparent.

[OrderedTraversalPolicy](mcp://flutter/api/widgets/OrderedTraversalPolicy)
A [FocusTraversalPolicy](mcp://flutter/api/widgets/FocusTraversalPolicy) that orders nodes by an explicit order that resides
in the nearest [FocusTraversalOrder](mcp://flutter/api/widgets/FocusTraversalOrder) widget ancestor.

[OrientationBuilder](mcp://flutter/api/widgets/OrientationBuilder)
Builds a widget tree that can depend on the parent widget's orientation
(distinct from the device orientation).

[OutlinedBorder](mcp://flutter/api/painting/OutlinedBorder)
A ShapeBorder that draws an outline with the width and color specified
by [side](mcp://flutter/api/painting/OutlinedBorder/side).

[OvalBorder](mcp://flutter/api/painting/OvalBorder)
A border that fits an elliptical shape.

[OverflowBar](mcp://flutter/api/widgets/OverflowBar)
A widget that lays out its [children](mcp://flutter/api/widgets/MultiChildRenderObjectWidget/children) in a row unless they
"overflow" the available horizontal space, in which case it lays
them out in a column instead.

[OverflowBox](mcp://flutter/api/widgets/OverflowBox)
A widget that imposes different constraints on its child than it gets
from its parent, possibly allowing the child to overflow the parent.

[Overlay](mcp://flutter/api/widgets/Overlay)
A stack of entries that can be managed independently.

[OverlayEntry](mcp://flutter/api/widgets/OverlayEntry)
A place in an [Overlay](mcp://flutter/api/widgets/Overlay) that can contain a widget.

[OverlayPortal](mcp://flutter/api/widgets/OverlayPortal)
A widget that renders its overlay child on an [Overlay](mcp://flutter/api/widgets/Overlay).

[OverlayPortalController](mcp://flutter/api/widgets/OverlayPortalController)
A class to show, hide and bring to top an [OverlayPortal](mcp://flutter/api/widgets/OverlayPortal)'s overlay child
in the target [Overlay](mcp://flutter/api/widgets/Overlay).

[OverlayRoute](mcp://flutter/api/widgets/OverlayRoute)<T>
A route that displays widgets in the [Navigator](mcp://flutter/api/widgets/Navigator)'s [Overlay](mcp://flutter/api/widgets/Overlay).

[OverlayState](mcp://flutter/api/widgets/OverlayState)
The current state of an [Overlay](mcp://flutter/api/widgets/Overlay).

[OverscrollIndicatorNotification](mcp://flutter/api/widgets/OverscrollIndicatorNotification)
A notification that either a [GlowingOverscrollIndicator](mcp://flutter/api/widgets/GlowingOverscrollIndicator) or a
[StretchingOverscrollIndicator](mcp://flutter/api/widgets/StretchingOverscrollIndicator) will start showing an overscroll indication.

[OverscrollNotification](mcp://flutter/api/widgets/OverscrollNotification)
A notification that a [Scrollable](mcp://flutter/api/widgets/Scrollable) widget has not changed its scroll position
because the change would have caused its scroll position to go outside of
its scroll bounds.

[Padding](mcp://flutter/api/widgets/Padding)
A widget that insets its child by the given padding.

[Page](mcp://flutter/api/widgets/Page)<T>
Describes the configuration of a [Route](mcp://flutter/api/widgets/Route).

[PageController](mcp://flutter/api/widgets/PageController)
A controller for [PageView](mcp://flutter/api/widgets/PageView).

[PageMetrics](mcp://flutter/api/widgets/PageMetrics)
Metrics for a [PageView](mcp://flutter/api/widgets/PageView).

[PageRoute](mcp://flutter/api/widgets/PageRoute)<T>
A modal route that replaces the entire screen.

[PageRouteBuilder](mcp://flutter/api/widgets/PageRouteBuilder)<T>
A utility class for defining one-off page routes in terms of callbacks.

[PageScrollPhysics](mcp://flutter/api/widgets/PageScrollPhysics)
Scroll physics used by a [PageView](mcp://flutter/api/widgets/PageView).

[PageStorage](mcp://flutter/api/widgets/PageStorage)
Establish a subtree in which widgets can opt into persisting states after
being destroyed.

[PageStorageBucket](mcp://flutter/api/widgets/PageStorageBucket)
A storage bucket associated with a page in an app.

[PageStorageKey](mcp://flutter/api/widgets/PageStorageKey)<T>
A [Key](mcp://flutter/api/foundation/Key) that can be used to persist the widget state in storage after the
destruction and will be restored when recreated.

[PageTransitionsBuilder](mcp://flutter/api/widgets/PageTransitionsBuilder)
Defines a page transition animation for a [PageRoute](mcp://flutter/api/widgets/PageRoute).

[PageView](mcp://flutter/api/widgets/PageView)
A scrollable list that works page by page.

[Paint](mcp://flutter/api/dart-ui/Paint)
A description of the style to use when drawing on a [Canvas](mcp://flutter/api/dart-ui/Canvas).

[PaintingContext](mcp://flutter/api/rendering/PaintingContext)
A place to paint.

[ParametricCurve](mcp://flutter/api/animation/ParametricCurve)<T>
An abstract class providing an interface for evaluating a parametric curve.

[ParentDataElement](mcp://flutter/api/widgets/ParentDataElement)<T extends [ParentData](mcp://flutter/api/rendering/ParentData)>
An [Element](mcp://flutter/api/widgets/Element) that uses a [ParentDataWidget](mcp://flutter/api/widgets/ParentDataWidget) as its configuration.

[ParentDataWidget](mcp://flutter/api/widgets/ParentDataWidget)<T extends [ParentData](mcp://flutter/api/rendering/ParentData)>
Base class for widgets that hook [ParentData](mcp://flutter/api/rendering/ParentData) information to children of
[RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget) s.

[PasteTextIntent](mcp://flutter/api/widgets/PasteTextIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to paste text from [Clipboard](mcp://flutter/api/services/Clipboard) to the field.

[Path](mcp://flutter/api/dart-ui/Path)
A complex, one-dimensional subset of a plane.

[PerformanceOverlay](mcp://flutter/api/widgets/PerformanceOverlay)
Displays performance statistics.

[PhysicalModel](mcp://flutter/api/widgets/PhysicalModel)
A widget representing a physical layer that clips its children to a shape.

[PhysicalShape](mcp://flutter/api/widgets/PhysicalShape)
A widget representing a physical layer that clips its children to a path.

[PinnedHeaderSliver](mcp://flutter/api/widgets/PinnedHeaderSliver)
A sliver that keeps its Widget child at the top of the a [CustomScrollView](mcp://flutter/api/widgets/CustomScrollView).

[Placeholder](mcp://flutter/api/widgets/Placeholder)
A widget that draws a box that represents where other widgets will one day
be added.

[PlaceholderDimensions](mcp://flutter/api/painting/PlaceholderDimensions)
Holds the [Size](mcp://flutter/api/dart-ui/Size) and baseline required to represent the dimensions of
a placeholder in text.

[PlaceholderSpan](mcp://flutter/api/painting/PlaceholderSpan)
An immutable placeholder that is embedded inline within text.

[PlatformMenu](mcp://flutter/api/widgets/PlatformMenu)
A class for representing menu items that have child submenus.

[PlatformMenuBar](mcp://flutter/api/widgets/PlatformMenuBar)
A menu bar that uses the platform's native APIs to construct and render a
menu described by a [PlatformMenu](mcp://flutter/api/widgets/PlatformMenu)/[PlatformMenuItem](mcp://flutter/api/widgets/PlatformMenuItem) hierarchy.

[PlatformMenuDelegate](mcp://flutter/api/widgets/PlatformMenuDelegate)
An abstract delegate class that can be used to set
[WidgetsBinding.platformMenuDelegate](mcp://flutter/api/widgets/WidgetsBinding/platformMenuDelegate) to provide for managing platform
menus.

[PlatformMenuItem](mcp://flutter/api/widgets/PlatformMenuItem)
A class for [PlatformMenuItem](mcp://flutter/api/widgets/PlatformMenuItem) s that do not have submenus (as a [PlatformMenu](mcp://flutter/api/widgets/PlatformMenu) would), but can be selected.

[PlatformMenuItemGroup](mcp://flutter/api/widgets/PlatformMenuItemGroup)
A class that groups other menu items into sections delineated by dividers.

[PlatformProvidedMenuItem](mcp://flutter/api/widgets/PlatformProvidedMenuItem)
A class that represents a menu item that is provided by the platform.

[PlatformRouteInformationProvider](mcp://flutter/api/widgets/PlatformRouteInformationProvider)
The route information provider that propagates the platform route information changes.

[PlatformSelectableRegionContextMenu](mcp://flutter/api/widgets/PlatformSelectableRegionContextMenu)
A widget that provides native selection context menu for its child subtree.

[PlatformViewCreationParams](mcp://flutter/api/widgets/PlatformViewCreationParams)
The parameters used to create a [PlatformViewController](mcp://flutter/api/services/PlatformViewController).

[PlatformViewLink](mcp://flutter/api/widgets/PlatformViewLink)
Links a platform view with the Flutter framework.

[PlatformViewSurface](mcp://flutter/api/widgets/PlatformViewSurface)
Integrates a platform view with Flutter's compositor, touch, and semantics subsystems.

[PointerCancelEvent](mcp://flutter/api/gestures/PointerCancelEvent)
The input from the pointer is no longer directed towards this receiver.

[PointerDownEvent](mcp://flutter/api/gestures/PointerDownEvent)
The pointer has made contact with the device.

[PointerEvent](mcp://flutter/api/gestures/PointerEvent)
Base class for touch, stylus, or mouse events.

[PointerMoveEvent](mcp://flutter/api/gestures/PointerMoveEvent)
The pointer has moved with respect to the device while the pointer is in
contact with the device.

[PointerUpEvent](mcp://flutter/api/gestures/PointerUpEvent)
The pointer has stopped making contact with the device.

[PopEntry](mcp://flutter/api/widgets/PopEntry)<T>
Allows listening to and preventing pops.

[PopScope](mcp://flutter/api/widgets/PopScope)<T>
Manages back navigation gestures.

[PopupRoute](mcp://flutter/api/widgets/PopupRoute)<T>
A modal route that overlays a widget over the current route.

[Positioned](mcp://flutter/api/widgets/Positioned)
A widget that controls where a child of a [Stack](mcp://flutter/api/widgets/Stack) is positioned.

[PositionedDirectional](mcp://flutter/api/widgets/PositionedDirectional)
A widget that controls where a child of a [Stack](mcp://flutter/api/widgets/Stack) is positioned without
committing to a specific [TextDirection](mcp://flutter/api/dart-ui/TextDirection).

[PositionedTransition](mcp://flutter/api/widgets/PositionedTransition)
Animated version of [Positioned](mcp://flutter/api/widgets/Positioned) which takes a specific
[Animation<RelativeRect>](mcp://flutter/api/animation/Animation) to transition the child's position from a start
position to an end position over the lifetime of the animation.

[PredictiveBackRoute](mcp://flutter/api/widgets/PredictiveBackRoute)
An interface for a route that supports predictive back gestures.

[PreferredSize](mcp://flutter/api/widgets/PreferredSize)
A widget with a preferred size.

[PreferredSizeWidget](mcp://flutter/api/widgets/PreferredSizeWidget)
An interface for widgets that can return the size this widget would prefer
if it were otherwise unconstrained.

[PreviousFocusAction](mcp://flutter/api/widgets/PreviousFocusAction)
An [Action](mcp://flutter/api/widgets/Action) that moves the focus to the previous focusable node in the focus
order.

[PreviousFocusIntent](mcp://flutter/api/widgets/PreviousFocusIntent)
An [Intent](mcp://flutter/api/widgets/Intent) bound to [PreviousFocusAction](mcp://flutter/api/widgets/PreviousFocusAction), which moves the focus to the
previous focusable node in the focus traversal order.

[PrimaryScrollController](mcp://flutter/api/widgets/PrimaryScrollController)
Associates a [ScrollController](mcp://flutter/api/widgets/ScrollController) with a subtree.

[PrioritizedAction](mcp://flutter/api/widgets/PrioritizedAction)
An [Action](mcp://flutter/api/widgets/Action) that iterates through a list of [Intent](mcp://flutter/api/widgets/Intent) s, invoking the first
that is enabled.

[PrioritizedIntents](mcp://flutter/api/widgets/PrioritizedIntents)
An [Intent](mcp://flutter/api/widgets/Intent) that evaluates a series of specified [orderedIntents](mcp://flutter/api/widgets/PrioritizedIntents/orderedIntents) for
execution.

[ProxyAnimation](mcp://flutter/api/animation/ProxyAnimation)
An animation that is a proxy for another animation.

[ProxyElement](mcp://flutter/api/widgets/ProxyElement)
An [Element](mcp://flutter/api/widgets/Element) that uses a [ProxyWidget](mcp://flutter/api/widgets/ProxyWidget) as its configuration.

[ProxyWidget](mcp://flutter/api/widgets/ProxyWidget)
A widget that has a child widget provided to it, instead of building a new
widget.

[RadialGradient](mcp://flutter/api/painting/RadialGradient)
A 2D radial gradient.

[RadioGroup](mcp://flutter/api/widgets/RadioGroup)<T>
A group for radios.

[RadioGroupRegistry](mcp://flutter/api/widgets/RadioGroupRegistry)<T>
An abstract interface for registering a group of radios.

[Radius](mcp://flutter/api/dart-ui/Radius)
A radius for either circular or elliptical shapes.

[RangeMaintainingScrollPhysics](mcp://flutter/api/widgets/RangeMaintainingScrollPhysics)
Scroll physics that attempt to keep the scroll position in range when the
contents change dimensions suddenly.

[RawAutocomplete](mcp://flutter/api/widgets/RawAutocomplete)<T extends [Object](mcp://flutter/api/dart-core/Object)>
A widget for helping the user make a selection by entering some text and
choosing from among a list of options.

[RawDialogRoute](mcp://flutter/api/widgets/RawDialogRoute)<T>
A general dialog route which allows for customization of the dialog popup.

[RawGestureDetector](mcp://flutter/api/widgets/RawGestureDetector)
A widget that detects gestures described by the given gesture
factories.

[RawGestureDetectorState](mcp://flutter/api/widgets/RawGestureDetectorState)
State for a [RawGestureDetector](mcp://flutter/api/widgets/RawGestureDetector).

[RawImage](mcp://flutter/api/widgets/RawImage)
A widget that displays a [dart:ui.Image](mcp://flutter/api/dart-ui/Image) directly.

[RawKeyboardListener](mcp://flutter/api/widgets/RawKeyboardListener)
A widget that calls a callback whenever the user presses or releases a key
on a keyboard.

[RawKeyEvent](mcp://flutter/api/services/RawKeyEvent)
Defines the interface for raw key events.

[RawMagnifier](mcp://flutter/api/widgets/RawMagnifier)
A common base class for magnifiers.

[RawMenuAnchor](mcp://flutter/api/widgets/RawMenuAnchor)
A widget that wraps a child and anchors a floating menu.

[RawMenuAnchorGroup](mcp://flutter/api/widgets/RawMenuAnchorGroup)
Creates a menu anchor that is always visible and is not displayed in an
[OverlayPortal](mcp://flutter/api/widgets/OverlayPortal).

[RawMenuOverlayInfo](mcp://flutter/api/widgets/RawMenuOverlayInfo)
Anchor and menu information passed to [RawMenuAnchor](mcp://flutter/api/widgets/RawMenuAnchor).

[RawRadio](mcp://flutter/api/widgets/RawRadio)<T>
A Radio button that provides basic radio functionalities.

[RawScrollbar](mcp://flutter/api/widgets/RawScrollbar)
An extendable base class for building scrollbars that fade in and out.

[RawScrollbarState](mcp://flutter/api/widgets/RawScrollbarState)<T extends [RawScrollbar](mcp://flutter/api/widgets/RawScrollbar)>
The state for a [RawScrollbar](mcp://flutter/api/widgets/RawScrollbar) widget, also shared by the [Scrollbar](mcp://flutter/api/material/Scrollbar) and
[CupertinoScrollbar](mcp://flutter/api/cupertino/CupertinoScrollbar) widgets.

[RawView](mcp://flutter/api/widgets/RawView)
The lower level workhorse widget for [View](mcp://flutter/api/widgets/View) that bootstraps a render tree
for a view.

[ReadingOrderTraversalPolicy](mcp://flutter/api/widgets/ReadingOrderTraversalPolicy)
Traverses the focus order in "reading order".

[Rect](mcp://flutter/api/dart-ui/Rect)
An immutable, 2D, axis-aligned, floating-point rectangle whose coordinates
are relative to a given origin.

[RectTween](mcp://flutter/api/animation/RectTween)
An interpolation between two rectangles.

[RedoTextIntent](mcp://flutter/api/widgets/RedoTextIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a user interaction that attempts to go back to
the previous editing state.

[RelativePositionedTransition](mcp://flutter/api/widgets/RelativePositionedTransition)
Animated version of [Positioned](mcp://flutter/api/widgets/Positioned) which transitions the child's position
based on the value of [rect](mcp://flutter/api/widgets/RelativePositionedTransition/rect) relative to a bounding box with the
specified [size](mcp://flutter/api/widgets/RelativePositionedTransition/size).

[RelativeRect](mcp://flutter/api/rendering/RelativeRect)
An immutable 2D, axis-aligned, floating-point rectangle whose coordinates
are given relative to another rectangle's edges, known as the container.
Since the dimensions of the rectangle are relative to those of the
container, this class has no width and height members. To determine the
width or height of the rectangle, convert it to a [Rect](mcp://flutter/api/dart-ui/Rect) using [toRect()](mcp://flutter/api/rendering/RelativeRect/toRect) (passing the container's own Rect), and then examine that object.

[RelativeRectTween](mcp://flutter/api/widgets/RelativeRectTween)
An interpolation between two relative rects.

[RenderBox](mcp://flutter/api/rendering/RenderBox)
A render object in a 2D Cartesian coordinate system.

[RenderNestedScrollViewViewport](mcp://flutter/api/widgets/RenderNestedScrollViewViewport)
The [RenderViewport](mcp://flutter/api/rendering/RenderViewport) variant used by [NestedScrollView](mcp://flutter/api/widgets/NestedScrollView).

[RenderObject](mcp://flutter/api/rendering/RenderObject)
An object in the render tree.

[RenderObjectElement](mcp://flutter/api/widgets/RenderObjectElement)
An [Element](mcp://flutter/api/widgets/Element) that uses a [RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget) as its configuration.

[RenderObjectToWidgetAdapter](mcp://flutter/api/widgets/RenderObjectToWidgetAdapter)<T extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
A bridge from a [RenderObject](mcp://flutter/api/rendering/RenderObject) to an [Element](mcp://flutter/api/widgets/Element) tree.

[RenderObjectToWidgetElement](mcp://flutter/api/widgets/RenderObjectToWidgetElement)<T extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
The root of an element tree that is hosted by a [RenderObject](mcp://flutter/api/rendering/RenderObject).

[RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget)
[RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget) s provide the configuration for [RenderObjectElement](mcp://flutter/api/widgets/RenderObjectElement) s,
which wrap [RenderObject](mcp://flutter/api/rendering/RenderObject) s, which provide the actual rendering of the
application.

[RenderSemanticsGestureHandler](mcp://flutter/api/rendering/RenderSemanticsGestureHandler)
Listens for the specified gestures from the semantics server (e.g.
an accessibility tool).

[RenderSliverOverlapAbsorber](mcp://flutter/api/widgets/RenderSliverOverlapAbsorber)
A sliver that wraps another, forcing its layout extent to be treated as
overlap.

[RenderSliverOverlapInjector](mcp://flutter/api/widgets/RenderSliverOverlapInjector)
A sliver that has a sliver geometry based on the values stored in a
[SliverOverlapAbsorberHandle](mcp://flutter/api/widgets/SliverOverlapAbsorberHandle).

[RenderTapRegion](mcp://flutter/api/widgets/RenderTapRegion)
A render object that defines a region that can detect taps inside or outside
of itself and any group of regions it belongs to, without participating in
the [gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system.

[RenderTapRegionSurface](mcp://flutter/api/widgets/RenderTapRegionSurface)
A render object that provides notification of a tap inside or outside of a
set of registered regions, without participating in the [gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system
(other than to consume tap down events if [TapRegion.consumeOutsideTaps](mcp://flutter/api/widgets/TapRegion/consumeOutsideTaps) is
true).

[RenderTreeRootElement](mcp://flutter/api/widgets/RenderTreeRootElement)
A [RenderObjectElement](mcp://flutter/api/widgets/RenderObjectElement) used to manage the root of a render tree.

[RenderTwoDimensionalViewport](mcp://flutter/api/widgets/RenderTwoDimensionalViewport)
A base class for viewing render objects that scroll in two dimensions.

[ReorderableDelayedDragStartListener](mcp://flutter/api/widgets/ReorderableDelayedDragStartListener)
A wrapper widget that will recognize the start of a drag operation by
looking for a long press event. Once it is recognized, it will start
a drag operation on the wrapped item in the reorderable list.

[ReorderableDragStartListener](mcp://flutter/api/widgets/ReorderableDragStartListener)
A wrapper widget that will recognize the start of a drag on the wrapped
widget by a [PointerDownEvent](mcp://flutter/api/gestures/PointerDownEvent), and immediately initiate dragging the
wrapped item to a new location in a reorderable list.

[ReorderableList](mcp://flutter/api/widgets/ReorderableList)
A scrolling container that allows the user to interactively reorder the
list items.

[ReorderableListState](mcp://flutter/api/widgets/ReorderableListState)
The state for a list that allows the user to interactively reorder
the list items.

[RepaintBoundary](mcp://flutter/api/widgets/RepaintBoundary)
A widget that creates a separate display list for its child.

[ReplaceTextIntent](mcp://flutter/api/widgets/ReplaceTextIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a user interaction that attempts to modify the
current [TextEditingValue](mcp://flutter/api/flutter_test/TextEditingValue) in an input field.

[RequestFocusAction](mcp://flutter/api/widgets/RequestFocusAction)
An [Action](mcp://flutter/api/widgets/Action) that requests the focus on the node it is given in its
[RequestFocusIntent](mcp://flutter/api/widgets/RequestFocusIntent).

[RequestFocusIntent](mcp://flutter/api/widgets/RequestFocusIntent)
An intent for use with the [RequestFocusAction](mcp://flutter/api/widgets/RequestFocusAction), which supplies the
[FocusNode](mcp://flutter/api/widgets/FocusNode) that should be focused.

[ResizeImage](mcp://flutter/api/painting/ResizeImage)
Instructs Flutter to decode the image at the specified dimensions
instead of at its native size.

[ResizeImageKey](mcp://flutter/api/painting/ResizeImageKey)
Key used internally by [ResizeImage](mcp://flutter/api/painting/ResizeImage).

[RestorableBool](mcp://flutter/api/widgets/RestorableBool)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [bool](mcp://flutter/api/dart-core/bool).

[RestorableBoolN](mcp://flutter/api/widgets/RestorableBoolN)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [bool](mcp://flutter/api/dart-core/bool) that is
nullable.

[RestorableChangeNotifier](mcp://flutter/api/widgets/RestorableChangeNotifier)<T extends [ChangeNotifier](mcp://flutter/api/foundation/ChangeNotifier)>
A base class for creating a [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that stores and restores a
[ChangeNotifier](mcp://flutter/api/foundation/ChangeNotifier).

[RestorableDateTime](mcp://flutter/api/widgets/RestorableDateTime)
A [RestorableValue](mcp://flutter/api/widgets/RestorableValue) that knows how to save and restore [DateTime](mcp://flutter/api/dart-core/DateTime).

[RestorableDateTimeN](mcp://flutter/api/widgets/RestorableDateTimeN)
A [RestorableValue](mcp://flutter/api/widgets/RestorableValue) that knows how to save and restore [DateTime](mcp://flutter/api/dart-core/DateTime) that is
nullable.

[RestorableDouble](mcp://flutter/api/widgets/RestorableDouble)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [double](mcp://flutter/api/dart-core/double).

[RestorableDoubleN](mcp://flutter/api/widgets/RestorableDoubleN)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [double](mcp://flutter/api/dart-core/double) that is nullable.

[RestorableEnum](mcp://flutter/api/widgets/RestorableEnum)<T extends [Enum](mcp://flutter/api/dart-core/Enum)>
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore an [Enum](mcp://flutter/api/dart-core/Enum) type.

[RestorableEnumN](mcp://flutter/api/widgets/RestorableEnumN)<T extends [Enum](mcp://flutter/api/dart-core/Enum)>
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a nullable [Enum](mcp://flutter/api/dart-core/Enum) type.

[RestorableInt](mcp://flutter/api/widgets/RestorableInt)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore an [int](mcp://flutter/api/dart-core/int).

[RestorableIntN](mcp://flutter/api/widgets/RestorableIntN)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore an [int](mcp://flutter/api/dart-core/int) that is nullable.

[RestorableListenable](mcp://flutter/api/widgets/RestorableListenable)<T extends [Listenable](mcp://flutter/api/foundation/Listenable)>
A base class for creating a [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that stores and restores a
[Listenable](mcp://flutter/api/foundation/Listenable).

[RestorableNum](mcp://flutter/api/widgets/RestorableNum)<T extends [num](mcp://flutter/api/dart-core/num)>
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [num](mcp://flutter/api/dart-core/num).

[RestorableNumN](mcp://flutter/api/widgets/RestorableNumN)<T extends [num](mcp://flutter/api/dart-core/num)?>
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [num](mcp://flutter/api/dart-core/num) that is nullable.

[RestorableProperty](mcp://flutter/api/widgets/RestorableProperty)<T>
Manages an object of type `T`, whose value a [State](mcp://flutter/api/widgets/State) object wants to have
restored during state restoration.

[RestorableRouteFuture](mcp://flutter/api/widgets/RestorableRouteFuture)<T>
Gives access to a [Route](mcp://flutter/api/widgets/Route) object and its return value that was added to a
navigator via one of its "restorable" API methods.

[RestorableString](mcp://flutter/api/widgets/RestorableString)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [String](mcp://flutter/api/dart-core/String).

[RestorableStringN](mcp://flutter/api/widgets/RestorableStringN)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a [String](mcp://flutter/api/dart-core/String) that is nullable.

[RestorableTextEditingController](mcp://flutter/api/widgets/RestorableTextEditingController)
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that knows how to store and restore a
[TextEditingController](mcp://flutter/api/widgets/TextEditingController).

[RestorableValue](mcp://flutter/api/widgets/RestorableValue)<T>
A [RestorableProperty](mcp://flutter/api/widgets/RestorableProperty) that makes the wrapped value accessible to the owning
[State](mcp://flutter/api/widgets/State) object via the [value](mcp://flutter/api/widgets/RestorableValue/value) getter and setter.

[RestorationBucket](mcp://flutter/api/services/RestorationBucket)
A [RestorationBucket](mcp://flutter/api/services/RestorationBucket) holds pieces of the restoration data that a part of
the application needs to restore its state.

[RestorationScope](mcp://flutter/api/widgets/RestorationScope)
Creates a new scope for restoration IDs used by descendant widgets to claim
[RestorationBucket](mcp://flutter/api/services/RestorationBucket) s.

[ReverseAnimation](mcp://flutter/api/animation/ReverseAnimation)
An animation that is the reverse of another animation.

[ReverseTween](mcp://flutter/api/animation/ReverseTween)<T extends [Object](mcp://flutter/api/dart-core/Object)?>
A [Tween](mcp://flutter/api/animation/Tween) that evaluates its [parent](mcp://flutter/api/animation/ReverseTween/parent) in reverse.

[RichText](mcp://flutter/api/widgets/RichText)
A paragraph of rich text.

[RootBackButtonDispatcher](mcp://flutter/api/widgets/RootBackButtonDispatcher)
The default implementation of back button dispatcher for the root router.

[RootElement](mcp://flutter/api/widgets/RootElement)
The root of the element tree.

[RootRenderObjectElement](mcp://flutter/api/widgets/RootRenderObjectElement)
Deprecated. Unused in the framework and will be removed in a future version
of Flutter.

[RootRestorationScope](mcp://flutter/api/widgets/RootRestorationScope)
Inserts a child bucket of [RestorationManager.rootBucket](mcp://flutter/api/services/RestorationManager/rootBucket) into the widget
tree and makes it available to descendants via [RestorationScope.of](mcp://flutter/api/widgets/RestorationScope/of).

[RootWidget](mcp://flutter/api/widgets/RootWidget)
A widget for the root of the widget tree.

[RotatedBox](mcp://flutter/api/widgets/RotatedBox)
A widget that rotates its child by a integral number of quarter turns.

[RotationTransition](mcp://flutter/api/widgets/RotationTransition)
Animates the rotation of a widget.

[RoundedRectangleBorder](mcp://flutter/api/painting/RoundedRectangleBorder)
A rectangular border with rounded corners.

[RoundedSuperellipseBorder](mcp://flutter/api/painting/RoundedSuperellipseBorder)
A rectangular border with rounded corners following the shape of an
[RSuperellipse](mcp://flutter/api/dart-ui/RSuperellipse).

[Route](mcp://flutter/api/widgets/Route)<T>
An abstraction for an entry managed by a [Navigator](mcp://flutter/api/widgets/Navigator).

[RouteAware](mcp://flutter/api/widgets/RouteAware)
An interface for objects that are aware of their current [Route](mcp://flutter/api/widgets/Route).

[RouteInformation](mcp://flutter/api/widgets/RouteInformation)
A piece of routing information.

[RouteInformationParser](mcp://flutter/api/widgets/RouteInformationParser)<T>
A delegate that is used by the [Router](mcp://flutter/api/widgets/Router) widget to parse a route information
into a configuration of type T.

[RouteInformationProvider](mcp://flutter/api/widgets/RouteInformationProvider)
A route information provider that provides route information for the
[Router](mcp://flutter/api/widgets/Router) widget

[RouteObserver](mcp://flutter/api/widgets/RouteObserver)<R extends [Route](mcp://flutter/api/widgets/Route)>
A [Navigator](mcp://flutter/api/widgets/Navigator) observer that notifies [RouteAware](mcp://flutter/api/widgets/RouteAware) s of changes to the
state of their [Route](mcp://flutter/api/widgets/Route).

[Router](mcp://flutter/api/widgets/Router)<T>
The dispatcher for opening and closing pages of an application.

[RouterConfig](mcp://flutter/api/widgets/RouterConfig)<T>
A convenient bundle to configure a [Router](mcp://flutter/api/widgets/Router) widget.

[RouterDelegate](mcp://flutter/api/widgets/RouterDelegate)<T>
A delegate that is used by the [Router](mcp://flutter/api/widgets/Router) widget to build and configure a
navigating widget.

[RouteSettings](mcp://flutter/api/widgets/RouteSettings)
Data that might be useful in constructing a [Route](mcp://flutter/api/widgets/Route).

[RouteTransitionRecord](mcp://flutter/api/widgets/RouteTransitionRecord)
A [Route](mcp://flutter/api/widgets/Route) wrapper interface that can be staged for [TransitionDelegate](mcp://flutter/api/widgets/TransitionDelegate) to
decide how its underlying [Route](mcp://flutter/api/widgets/Route) should transition on or off screen.

[Row](mcp://flutter/api/widgets/Row)
A widget that displays its children in a horizontal array.

[RRect](mcp://flutter/api/dart-ui/RRect)
An immutable rounded rectangle with the custom radii for all four corners.

[RSTransform](mcp://flutter/api/dart-ui/RSTransform)
A transform consisting of a translation, a rotation, and a uniform scale.

[RSuperellipse](mcp://flutter/api/dart-ui/RSuperellipse)
An immutable rounded superellipse.

[SafeArea](mcp://flutter/api/widgets/SafeArea)
A widget that insets its child with sufficient padding to avoid intrusions
by the operating system.

[SawTooth](mcp://flutter/api/animation/SawTooth)
A sawtooth curve that repeats a given number of times over the unit interval.

[ScaleEndDetails](mcp://flutter/api/gestures/ScaleEndDetails)
Details for [GestureScaleEndCallback](mcp://flutter/api/gestures/GestureScaleEndCallback).

[ScaleStartDetails](mcp://flutter/api/gestures/ScaleStartDetails)
Details for [GestureScaleStartCallback](mcp://flutter/api/gestures/GestureScaleStartCallback).

[ScaleTransition](mcp://flutter/api/widgets/ScaleTransition)
Animates the scale of a transformed widget.

[ScaleUpdateDetails](mcp://flutter/api/gestures/ScaleUpdateDetails)
Details for [GestureScaleUpdateCallback](mcp://flutter/api/gestures/GestureScaleUpdateCallback).

[Scrollable](mcp://flutter/api/widgets/Scrollable)
A widget that manages scrolling in one dimension and informs the [Viewport](mcp://flutter/api/widgets/Viewport) through which the content is viewed.

[ScrollableDetails](mcp://flutter/api/widgets/ScrollableDetails)
Describes the aspects of a Scrollable widget to inform inherited widgets
like [ScrollBehavior](mcp://flutter/api/widgets/ScrollBehavior) for decorating or enumerate the properties of combined
Scrollables, such as [TwoDimensionalScrollable](mcp://flutter/api/widgets/TwoDimensionalScrollable).

[ScrollableState](mcp://flutter/api/widgets/ScrollableState)
State object for a [Scrollable](mcp://flutter/api/widgets/Scrollable) widget.

[ScrollAction](mcp://flutter/api/widgets/ScrollAction)
An [Action](mcp://flutter/api/widgets/Action) that scrolls the relevant [Scrollable](mcp://flutter/api/widgets/Scrollable) by the amount configured
in the [ScrollIntent](mcp://flutter/api/widgets/ScrollIntent) given to it.

[ScrollActivity](mcp://flutter/api/widgets/ScrollActivity)
Base class for scrolling activities like dragging and flinging.

[ScrollActivityDelegate](mcp://flutter/api/widgets/ScrollActivityDelegate)
A backend for a [ScrollActivity](mcp://flutter/api/widgets/ScrollActivity).

[ScrollAwareImageProvider](mcp://flutter/api/widgets/ScrollAwareImageProvider)<T extends [Object](mcp://flutter/api/dart-core/Object)>
An [ImageProvider](mcp://flutter/api/painting/ImageProvider) that makes use of
[Scrollable.recommendDeferredLoadingForContext](mcp://flutter/api/widgets/Scrollable/recommendDeferredLoadingForContext) to avoid loading images when
rapidly scrolling.

[ScrollbarPainter](mcp://flutter/api/widgets/ScrollbarPainter)
Paints a scrollbar's track and thumb.

[ScrollBehavior](mcp://flutter/api/widgets/ScrollBehavior)
Describes how [Scrollable](mcp://flutter/api/widgets/Scrollable) widgets should behave.

[ScrollConfiguration](mcp://flutter/api/widgets/ScrollConfiguration)
Controls how [Scrollable](mcp://flutter/api/widgets/Scrollable) widgets behave in a subtree.

[ScrollContext](mcp://flutter/api/widgets/ScrollContext)
An interface that [Scrollable](mcp://flutter/api/widgets/Scrollable) widgets implement in order to use
[ScrollPosition](mcp://flutter/api/widgets/ScrollPosition).

[ScrollController](mcp://flutter/api/widgets/ScrollController)
Controls a scrollable widget.

[ScrollDragController](mcp://flutter/api/widgets/ScrollDragController)
Scrolls a scroll view as the user drags their finger across the screen.

[ScrollEndNotification](mcp://flutter/api/widgets/ScrollEndNotification)
A notification that a [Scrollable](mcp://flutter/api/widgets/Scrollable) widget has stopped scrolling.

[ScrollHoldController](mcp://flutter/api/widgets/ScrollHoldController)
Interface for holding a [Scrollable](mcp://flutter/api/widgets/Scrollable) stationary.

[ScrollIncrementDetails](mcp://flutter/api/widgets/ScrollIncrementDetails)
A details object that describes the type of scroll increment being requested
of a [ScrollIncrementCalculator](mcp://flutter/api/widgets/ScrollIncrementCalculator) function, as well as the current metrics
for the scrollable.

[ScrollIntent](mcp://flutter/api/widgets/ScrollIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents scrolling the nearest scrollable by an amount
appropriate for the [type](mcp://flutter/api/widgets/ScrollIntent/type) specified.

[ScrollMetricsNotification](mcp://flutter/api/widgets/ScrollMetricsNotification)
A notification that a scrollable widget's [ScrollMetrics](mcp://flutter/api/widgets/ScrollMetrics) have changed.

[ScrollNotification](mcp://flutter/api/widgets/ScrollNotification)
A [Notification](mcp://flutter/api/widgets/Notification) related to scrolling.

[ScrollNotificationObserver](mcp://flutter/api/widgets/ScrollNotificationObserver)
Notifies its listeners when a descendant scrolls.

[ScrollNotificationObserverState](mcp://flutter/api/widgets/ScrollNotificationObserverState)
The listener list state for a [ScrollNotificationObserver](mcp://flutter/api/widgets/ScrollNotificationObserver) returned by
[ScrollNotificationObserver.of](mcp://flutter/api/widgets/ScrollNotificationObserver/of).

[ScrollPhysics](mcp://flutter/api/widgets/ScrollPhysics)
Determines the physics of a [Scrollable](mcp://flutter/api/widgets/Scrollable) widget.

[ScrollPosition](mcp://flutter/api/widgets/ScrollPosition)
Determines which portion of the content is visible in a scroll view.

[ScrollPositionWithSingleContext](mcp://flutter/api/widgets/ScrollPositionWithSingleContext)
A scroll position that manages scroll activities for a single
[ScrollContext](mcp://flutter/api/widgets/ScrollContext).

[ScrollSpringSimulation](mcp://flutter/api/physics/ScrollSpringSimulation)
A [SpringSimulation](mcp://flutter/api/physics/SpringSimulation) where the value of [x](mcp://flutter/api/physics/ScrollSpringSimulation/x) is guaranteed to have exactly the
end value when the simulation [isDone](mcp://flutter/api/physics/SpringSimulation/isDone).

[ScrollStartNotification](mcp://flutter/api/widgets/ScrollStartNotification)
A notification that a [Scrollable](mcp://flutter/api/widgets/Scrollable) widget has started scrolling.

[ScrollToDocumentBoundaryIntent](mcp://flutter/api/widgets/ScrollToDocumentBoundaryIntent)
Scrolls to the beginning or end of the document depending on the [forward](mcp://flutter/api/widgets/DirectionalTextEditingIntent/forward) parameter.

[ScrollUpdateNotification](mcp://flutter/api/widgets/ScrollUpdateNotification)
A notification that a [Scrollable](mcp://flutter/api/widgets/Scrollable) widget has changed its scroll position.

[ScrollView](mcp://flutter/api/widgets/ScrollView)
A widget that combines a [Scrollable](mcp://flutter/api/widgets/Scrollable) and a [Viewport](mcp://flutter/api/widgets/Viewport) to create an
interactive scrolling pane of content in one dimension.

[SelectableRegion](mcp://flutter/api/widgets/SelectableRegion)
A widget that introduces an area for user selections.

[SelectableRegionSelectionStatusScope](mcp://flutter/api/widgets/SelectableRegionSelectionStatusScope)
Notifies its listeners when the selection under a [SelectableRegion](mcp://flutter/api/widgets/SelectableRegion) or
[SelectionArea](mcp://flutter/api/material/SelectionArea) is being changed or finalized.

[SelectableRegionState](mcp://flutter/api/widgets/SelectableRegionState)
State for a [SelectableRegion](mcp://flutter/api/widgets/SelectableRegion).

[SelectAction](mcp://flutter/api/widgets/SelectAction)
An action that selects the currently focused control.

[SelectAllTextIntent](mcp://flutter/api/widgets/SelectAllTextIntent)
An [Intent](mcp://flutter/api/widgets/Intent) to select everything in the field.

[SelectIntent](mcp://flutter/api/widgets/SelectIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that selects the currently focused control.

[SelectionContainer](mcp://flutter/api/widgets/SelectionContainer)
A container that handles [SelectionEvent](mcp://flutter/api/rendering/SelectionEvent) s for the [Selectable](mcp://flutter/api/rendering/Selectable) s in
the subtree.

[SelectionContainerDelegate](mcp://flutter/api/widgets/SelectionContainerDelegate)
A delegate to handle [SelectionEvent](mcp://flutter/api/rendering/SelectionEvent) s for a [SelectionContainer](mcp://flutter/api/widgets/SelectionContainer).

[SelectionDetails](mcp://flutter/api/widgets/SelectionDetails)
A read-only interface for accessing the details of a selection under a [SelectionListener](mcp://flutter/api/widgets/SelectionListener).

[SelectionListener](mcp://flutter/api/widgets/SelectionListener)
A [SelectionContainer](mcp://flutter/api/widgets/SelectionContainer) that allows the user to access the [SelectionDetails](mcp://flutter/api/widgets/SelectionDetails) and
listen to selection changes for the child subtree it wraps under a [SelectionArea](mcp://flutter/api/material/SelectionArea) or [SelectableRegion](mcp://flutter/api/widgets/SelectableRegion).

[SelectionListenerNotifier](mcp://flutter/api/widgets/SelectionListenerNotifier)
Notifies listeners when the selection under a [SelectionListener](mcp://flutter/api/widgets/SelectionListener) has been
changed.

[SelectionOverlay](mcp://flutter/api/widgets/SelectionOverlay)
An object that manages a pair of selection handles and a toolbar.

[SelectionRegistrarScope](mcp://flutter/api/widgets/SelectionRegistrarScope)
An inherited widget to host a [SelectionRegistrar](mcp://flutter/api/rendering/SelectionRegistrar) for the subtree.

[Semantics](mcp://flutter/api/widgets/Semantics)
A widget that annotates the widget tree with a description of the meaning of
the widgets.

[SemanticsDebugger](mcp://flutter/api/widgets/SemanticsDebugger)
A widget that visualizes the semantics for the child.

[SemanticsGestureDelegate](mcp://flutter/api/widgets/SemanticsGestureDelegate)
A base class that describes what semantics notations a [RawGestureDetector](mcp://flutter/api/widgets/RawGestureDetector) should add to the render object [RenderSemanticsGestureHandler](mcp://flutter/api/rendering/RenderSemanticsGestureHandler).

[SensitiveContent](mcp://flutter/api/widgets/SensitiveContent)
Widget to set the [ContentSensitivity](mcp://flutter/api/services/ContentSensitivity) of content in the widget
tree.

[SensitiveContentHost](mcp://flutter/api/widgets/SensitiveContentHost)
Host of the current content sensitivity for the widget tree that contains
some number [SensitiveContent](mcp://flutter/api/widgets/SensitiveContent) widgets.

[Shader](mcp://flutter/api/dart-ui/Shader)
Base class for objects such as [Gradient](mcp://flutter/api/dart-ui/Gradient) and [ImageShader](mcp://flutter/api/dart-ui/ImageShader) which
correspond to shaders as used by [Paint.shader](mcp://flutter/api/dart-ui/Paint/shader).

[ShaderMask](mcp://flutter/api/widgets/ShaderMask)
A widget that applies a mask generated by a [Shader](mcp://flutter/api/dart-ui/Shader) to its child.

[ShaderWarmUp](mcp://flutter/api/painting/ShaderWarmUp)
Interface for drawing an image to warm up Skia shader compilations.

[Shadow](mcp://flutter/api/dart-ui/Shadow)
A single shadow.

[ShapeBorder](mcp://flutter/api/painting/ShapeBorder)
Base class for shape outlines.

[ShapeBorderClipper](mcp://flutter/api/rendering/ShapeBorderClipper)
A [CustomClipper](mcp://flutter/api/rendering/CustomClipper) that clips to the outer path of a [ShapeBorder](mcp://flutter/api/painting/ShapeBorder).

[ShapeDecoration](mcp://flutter/api/painting/ShapeDecoration)
An immutable description of how to paint an arbitrary shape.

[SharedAppData](mcp://flutter/api/widgets/SharedAppData)
Enables sharing key/value data with its `child` and all of the
child's descendants.

[ShortcutActivator](mcp://flutter/api/widgets/ShortcutActivator)
An interface to define the keyboard key combination to trigger a shortcut.

[ShortcutManager](mcp://flutter/api/widgets/ShortcutManager)
A manager of keyboard shortcut bindings used by [Shortcuts](mcp://flutter/api/widgets/Shortcuts) to handle key
events.

[ShortcutMapProperty](mcp://flutter/api/widgets/ShortcutMapProperty)
A [DiagnosticsProperty](mcp://flutter/api/foundation/DiagnosticsProperty) which handles formatting a `Map<LogicalKeySet, Intent>` (the same type as the [Shortcuts.shortcuts](mcp://flutter/api/widgets/Shortcuts/shortcuts) property) so that its
diagnostic output is human-readable.

[ShortcutRegistrar](mcp://flutter/api/widgets/ShortcutRegistrar)
A widget that holds a [ShortcutRegistry](mcp://flutter/api/widgets/ShortcutRegistry) which allows descendants to add,
remove, or replace shortcuts.

[ShortcutRegistry](mcp://flutter/api/widgets/ShortcutRegistry)
A class used by [ShortcutRegistrar](mcp://flutter/api/widgets/ShortcutRegistrar) that allows adding or removing shortcut
bindings by descendants of the [ShortcutRegistrar](mcp://flutter/api/widgets/ShortcutRegistrar).

[ShortcutRegistryEntry](mcp://flutter/api/widgets/ShortcutRegistryEntry)
A entry returned by [ShortcutRegistry.addAll](mcp://flutter/api/widgets/ShortcutRegistry/addAll) that allows the caller to
identify the shortcuts they registered with the [ShortcutRegistry](mcp://flutter/api/widgets/ShortcutRegistry) through
the [ShortcutRegistrar](mcp://flutter/api/widgets/ShortcutRegistrar).

[Shortcuts](mcp://flutter/api/widgets/Shortcuts)
A widget that creates key bindings to specific actions for its
descendants.

[ShortcutSerialization](mcp://flutter/api/widgets/ShortcutSerialization)
A class used by [MenuSerializableShortcut](mcp://flutter/api/widgets/MenuSerializableShortcut) to describe the shortcut for
serialization to send to the platform for rendering a [PlatformMenuBar](mcp://flutter/api/widgets/PlatformMenuBar).

[ShrinkWrappingViewport](mcp://flutter/api/widgets/ShrinkWrappingViewport)
A widget that is bigger on the inside and shrink wraps its children in the
main axis.

[Simulation](mcp://flutter/api/physics/Simulation)
The base class for all simulations.

[SingleActivator](mcp://flutter/api/widgets/SingleActivator)
A shortcut key combination of a single key and modifiers.

[SingleChildLayoutDelegate](mcp://flutter/api/rendering/SingleChildLayoutDelegate)
A delegate for computing the layout of a render object with a single child.

[SingleChildRenderObjectElement](mcp://flutter/api/widgets/SingleChildRenderObjectElement)
An [Element](mcp://flutter/api/widgets/Element) that uses a [SingleChildRenderObjectWidget](mcp://flutter/api/widgets/SingleChildRenderObjectWidget) as its configuration.

[SingleChildRenderObjectWidget](mcp://flutter/api/widgets/SingleChildRenderObjectWidget)
A superclass for [RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget) s that configure [RenderObject](mcp://flutter/api/rendering/RenderObject) subclasses
that have a single child slot.

[SingleChildScrollView](mcp://flutter/api/widgets/SingleChildScrollView)
A box in which a single widget can be scrolled.

[Size](mcp://flutter/api/dart-ui/Size)
Holds a 2D floating-point size.

[SizeChangedLayoutNotification](mcp://flutter/api/widgets/SizeChangedLayoutNotification)
Indicates that the size of one of the descendants of the object receiving
this notification has changed, and that therefore any assumptions about that
layout are no longer valid.

[SizeChangedLayoutNotifier](mcp://flutter/api/widgets/SizeChangedLayoutNotifier)
A widget that automatically dispatches a [SizeChangedLayoutNotification](mcp://flutter/api/widgets/SizeChangedLayoutNotification) when the layout dimensions of its child change.

[SizedBox](mcp://flutter/api/widgets/SizedBox)
A box with a specified size.

[SizedOverflowBox](mcp://flutter/api/widgets/SizedOverflowBox)
A widget that is a specific size but passes its original constraints
through to its child, which may then overflow.

[SizeTransition](mcp://flutter/api/widgets/SizeTransition)
Animates its own size and clips and aligns its child.

[SizeTween](mcp://flutter/api/animation/SizeTween)
An interpolation between two sizes.

[SlideTransition](mcp://flutter/api/widgets/SlideTransition)
Animates the position of a widget relative to its normal position.

[SliverAnimatedGrid](mcp://flutter/api/widgets/SliverAnimatedGrid)
A [SliverGrid](mcp://flutter/api/widgets/SliverGrid) that animates items when they are inserted or removed.

[SliverAnimatedGridState](mcp://flutter/api/widgets/SliverAnimatedGridState)
The state for a [SliverAnimatedGrid](mcp://flutter/api/widgets/SliverAnimatedGrid) that animates items when they are
inserted or removed.

[SliverAnimatedList](mcp://flutter/api/widgets/SliverAnimatedList)
A [SliverList](mcp://flutter/api/widgets/SliverList) that animates items when they are inserted or removed.

[SliverAnimatedListState](mcp://flutter/api/widgets/SliverAnimatedListState)
The state for a [SliverAnimatedList](mcp://flutter/api/widgets/SliverAnimatedList) that animates items when they are
inserted or removed.

[SliverAnimatedOpacity](mcp://flutter/api/widgets/SliverAnimatedOpacity)
Animated version of [SliverOpacity](mcp://flutter/api/widgets/SliverOpacity) which automatically transitions the
sliver child's opacity over a given duration whenever the given opacity
changes.

[SliverChildBuilderDelegate](mcp://flutter/api/widgets/SliverChildBuilderDelegate)
A delegate that supplies children for slivers using a builder callback.

[SliverChildDelegate](mcp://flutter/api/widgets/SliverChildDelegate)
A delegate that supplies children for slivers.

[SliverChildListDelegate](mcp://flutter/api/widgets/SliverChildListDelegate)
A delegate that supplies children for slivers using an explicit list.

[SliverConstrainedCrossAxis](mcp://flutter/api/widgets/SliverConstrainedCrossAxis)
A sliver that constrains the cross axis extent of its sliver child.

[SliverCrossAxisExpanded](mcp://flutter/api/widgets/SliverCrossAxisExpanded)
Set a flex factor for allocating space in the cross axis direction.

[SliverCrossAxisGroup](mcp://flutter/api/widgets/SliverCrossAxisGroup)
A sliver that places multiple sliver children in a linear array along
the cross axis.

[SliverEnsureSemantics](mcp://flutter/api/widgets/SliverEnsureSemantics)
A sliver that ensures its sliver child is included in the semantics tree.

[SliverFadeTransition](mcp://flutter/api/widgets/SliverFadeTransition)
Animates the opacity of a sliver widget.

[SliverFillRemaining](mcp://flutter/api/widgets/SliverFillRemaining)
A sliver that contains a single box child that fills the remaining space in
the viewport.

[SliverFillViewport](mcp://flutter/api/widgets/SliverFillViewport)
A sliver that contains multiple box children that each fills the viewport.

[SliverFixedExtentList](mcp://flutter/api/widgets/SliverFixedExtentList)
A sliver that places multiple box children with the same main axis extent in
a linear array.

[SliverFloatingHeader](mcp://flutter/api/widgets/SliverFloatingHeader)
A sliver that shows its [child](mcp://flutter/api/widgets/SliverFloatingHeader/child) when the user scrolls forward and hides it
when the user scrolls backwards.

[SliverGrid](mcp://flutter/api/widgets/SliverGrid)
A sliver that places multiple box children in a two dimensional arrangement.

[SliverGridDelegate](mcp://flutter/api/rendering/SliverGridDelegate)
Controls the layout of tiles in a grid.

[SliverGridDelegateWithFixedCrossAxisCount](mcp://flutter/api/rendering/SliverGridDelegateWithFixedCrossAxisCount)
Creates grid layouts with a fixed number of tiles in the cross axis.

[SliverGridDelegateWithMaxCrossAxisExtent](mcp://flutter/api/rendering/SliverGridDelegateWithMaxCrossAxisExtent)
Creates grid layouts with tiles that each have a maximum cross-axis extent.

[SliverIgnorePointer](mcp://flutter/api/widgets/SliverIgnorePointer)
A sliver widget that is invisible during hit testing.

[SliverLayoutBuilder](mcp://flutter/api/widgets/SliverLayoutBuilder)
Builds a sliver widget tree that can depend on its own [SliverConstraints](mcp://flutter/api/rendering/SliverConstraints).

[SliverList](mcp://flutter/api/widgets/SliverList)
A sliver that places multiple box children in a linear array along the main
axis.

[SliverMainAxisGroup](mcp://flutter/api/widgets/SliverMainAxisGroup)
A sliver that places multiple sliver children in a linear array along
the main axis, one after another.

[SliverMultiBoxAdaptorElement](mcp://flutter/api/widgets/SliverMultiBoxAdaptorElement)
An element that lazily builds children for a [SliverMultiBoxAdaptorWidget](mcp://flutter/api/widgets/SliverMultiBoxAdaptorWidget).

[SliverMultiBoxAdaptorWidget](mcp://flutter/api/widgets/SliverMultiBoxAdaptorWidget)
A base class for slivers that have multiple box children.

[SliverOffstage](mcp://flutter/api/widgets/SliverOffstage)
A sliver that lays its sliver child out as if it was in the tree, but
without painting anything, without making the sliver child available for hit
testing, and without taking any room in the parent.

[SliverOpacity](mcp://flutter/api/widgets/SliverOpacity)
A sliver widget that makes its sliver child partially transparent.

[SliverOverlapAbsorber](mcp://flutter/api/widgets/SliverOverlapAbsorber)
A sliver that wraps another, forcing its layout extent to be treated as
overlap.

[SliverOverlapAbsorberHandle](mcp://flutter/api/widgets/SliverOverlapAbsorberHandle)
Handle to provide to a [SliverOverlapAbsorber](mcp://flutter/api/widgets/SliverOverlapAbsorber), a [SliverOverlapInjector](mcp://flutter/api/widgets/SliverOverlapInjector),
and an [NestedScrollViewViewport](mcp://flutter/api/widgets/NestedScrollViewViewport), to shift overlap in a [NestedScrollView](mcp://flutter/api/widgets/NestedScrollView).

[SliverOverlapInjector](mcp://flutter/api/widgets/SliverOverlapInjector)
A sliver that has a sliver geometry based on the values stored in a
[SliverOverlapAbsorberHandle](mcp://flutter/api/widgets/SliverOverlapAbsorberHandle).

[SliverPadding](mcp://flutter/api/widgets/SliverPadding)
A sliver that applies padding on each side of another sliver.

[SliverPersistentHeader](mcp://flutter/api/widgets/SliverPersistentHeader)
A sliver whose size varies when the sliver is scrolled to the edge
of the viewport opposite the sliver's [GrowthDirection](mcp://flutter/api/rendering/GrowthDirection).

[SliverPersistentHeaderDelegate](mcp://flutter/api/widgets/SliverPersistentHeaderDelegate)
Delegate for configuring a [SliverPersistentHeader](mcp://flutter/api/widgets/SliverPersistentHeader).

[SliverPrototypeExtentList](mcp://flutter/api/widgets/SliverPrototypeExtentList)
A sliver that places its box children in a linear array and constrains them
to have the same extent as a prototype item along the main axis.

[SliverReorderableList](mcp://flutter/api/widgets/SliverReorderableList)
A sliver list that allows the user to interactively reorder the list items.

[SliverReorderableListState](mcp://flutter/api/widgets/SliverReorderableListState)
The state for a sliver list that allows the user to interactively reorder
the list items.

[SliverResizingHeader](mcp://flutter/api/widgets/SliverResizingHeader)
A sliver that is pinned to the start of its [CustomScrollView](mcp://flutter/api/widgets/CustomScrollView) and
reacts to scrolling by resizing between the intrinsic sizes of its
min and max extent prototypes.

[SliverSafeArea](mcp://flutter/api/widgets/SliverSafeArea)
A sliver that insets another sliver by sufficient padding to avoid
intrusions by the operating system.

[SliverSemantics](mcp://flutter/api/widgets/SliverSemantics)
A sliver that annotates its subtree with a description of the meaning of
the slivers.

[SliverToBoxAdapter](mcp://flutter/api/widgets/SliverToBoxAdapter)
A sliver that contains a single box widget.

[SliverVariedExtentList](mcp://flutter/api/widgets/SliverVariedExtentList)
A sliver that places its box children in a linear array and constrains them
to have the corresponding extent returned by [itemExtentBuilder](mcp://flutter/api/widgets/SliverVariedExtentList/itemExtentBuilder).

[SliverVisibility](mcp://flutter/api/widgets/SliverVisibility)
Whether to show or hide a sliver child.

[SliverWithKeepAliveWidget](mcp://flutter/api/widgets/SliverWithKeepAliveWidget)
A base class for slivers that have [KeepAlive](mcp://flutter/api/widgets/KeepAlive) children.

[SlottedMultiChildRenderObjectWidget](mcp://flutter/api/widgets/SlottedMultiChildRenderObjectWidget)<SlotType, ChildType extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
A superclass for [RenderObjectWidget](mcp://flutter/api/widgets/RenderObjectWidget) s that configure [RenderObject](mcp://flutter/api/rendering/RenderObject) subclasses that organize their children in different slots.

[SlottedRenderObjectElement](mcp://flutter/api/widgets/SlottedRenderObjectElement)<SlotType, ChildType extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
Element used by the [SlottedMultiChildRenderObjectWidget](mcp://flutter/api/widgets/SlottedMultiChildRenderObjectWidget).

[SnapshotController](mcp://flutter/api/widgets/SnapshotController)
A controller for the [SnapshotWidget](mcp://flutter/api/widgets/SnapshotWidget) that controls when the child image is displayed
and when to regenerated the child image.

[SnapshotPainter](mcp://flutter/api/widgets/SnapshotPainter)
A painter used to paint either a snapshot or the child widgets that
would be a snapshot.

[SnapshotWidget](mcp://flutter/api/widgets/SnapshotWidget)
A widget that can replace its child with a snapshotted version of the child.

[Spacer](mcp://flutter/api/widgets/Spacer)
Spacer creates an adjustable, empty spacer that can be used to tune the
spacing between widgets in a [Flex](mcp://flutter/api/widgets/Flex) container, like [Row](mcp://flutter/api/widgets/Row) or [Column](mcp://flutter/api/widgets/Column).

[SpellCheckConfiguration](mcp://flutter/api/widgets/SpellCheckConfiguration)
Controls how spell check is performed for text input.

[Split](mcp://flutter/api/animation/Split)
A curve that progresses according to [beginCurve](mcp://flutter/api/animation/Split/beginCurve) until [split](mcp://flutter/api/animation/Split/split), then
according to [endCurve](mcp://flutter/api/animation/Split/endCurve).

[SpringDescription](mcp://flutter/api/physics/SpringDescription)
Structure that describes a spring's constants.

[Stack](mcp://flutter/api/widgets/Stack)
A widget that positions its children relative to the edges of its box.

[StadiumBorder](mcp://flutter/api/painting/StadiumBorder)
A border that fits a stadium-shaped border (a box with semicircles on the ends)
within the rectangle of the widget it is applied to.

[StarBorder](mcp://flutter/api/painting/StarBorder)
A border that fits a star or polygon-shaped border within the rectangle of
the widget it is applied to.

[State](mcp://flutter/api/widgets/State)<T extends [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>
The logic and internal state for a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget).

[StatefulBuilder](mcp://flutter/api/widgets/StatefulBuilder)
A platonic widget that both has state and calls a closure to obtain its child widget.

[StatefulElement](mcp://flutter/api/widgets/StatefulElement)
An [Element](mcp://flutter/api/widgets/Element) that uses a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) as its configuration.

[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)
A widget that has mutable state.

[StatelessElement](mcp://flutter/api/widgets/StatelessElement)
An [Element](mcp://flutter/api/widgets/Element) that uses a [StatelessWidget](mcp://flutter/api/widgets/StatelessWidget) as its configuration.

[StatelessWidget](mcp://flutter/api/widgets/StatelessWidget)
A widget that does not require mutable state.

[StaticSelectionContainerDelegate](mcp://flutter/api/widgets/StaticSelectionContainerDelegate)
A delegate that manages updating multiple [Selectable](mcp://flutter/api/rendering/Selectable) children where the
[Selectable](mcp://flutter/api/rendering/Selectable) s do not change or move around frequently.

[StatusTransitionWidget](mcp://flutter/api/widgets/StatusTransitionWidget)
A widget that rebuilds when the given animation changes status.

[StepTween](mcp://flutter/api/animation/StepTween)
An interpolation between two integers that floors.

[StreamBuilder](mcp://flutter/api/widgets/StreamBuilder)<T>
Widget that builds itself based on the latest snapshot of interaction with
a [Stream](mcp://flutter/api/dart-async/Stream).

[StreamBuilderBase](mcp://flutter/api/widgets/StreamBuilderBase)<T, S>
Base class for widgets that build themselves based on interaction with
a specified [Stream](mcp://flutter/api/dart-async/Stream).

[StretchEffect](mcp://flutter/api/widgets/StretchEffect)
A widget that applies a stretching visual effect to its child.

[StretchingOverscrollIndicator](mcp://flutter/api/widgets/StretchingOverscrollIndicator)
A Material Design visual indication that a scroll view has overscrolled.

[StrutStyle](mcp://flutter/api/painting/StrutStyle)
Defines the strut, which sets the minimum height a line can be
relative to the baseline.

[SweepGradient](mcp://flutter/api/painting/SweepGradient)
A 2D sweep gradient.

[SystemContextMenu](mcp://flutter/api/widgets/SystemContextMenu)
Displays the system context menu on top of the Flutter view.

[SystemMouseCursors](mcp://flutter/api/services/SystemMouseCursors)
A collection of system [MouseCursor](mcp://flutter/api/services/MouseCursor) s.

[SystemTextScaler](mcp://flutter/api/widgets/SystemTextScaler)
A [TextScaler](mcp://flutter/api/painting/TextScaler) that reflects the user's font scale preferences from the
platform's accessibility settings.

[Table](mcp://flutter/api/widgets/Table)
A widget that uses the table layout algorithm for its children.

[TableBorder](mcp://flutter/api/rendering/TableBorder)
Border specification for [Table](mcp://flutter/api/widgets/Table) widgets.

[TableCell](mcp://flutter/api/widgets/TableCell)
A widget that controls how a child of a [Table](mcp://flutter/api/widgets/Table) is aligned.

[TableColumnWidth](mcp://flutter/api/rendering/TableColumnWidth)
Base class to describe how wide a column in a [RenderTable](mcp://flutter/api/rendering/RenderTable) should be.

[TableRow](mcp://flutter/api/widgets/TableRow)
A horizontal group of cells in a [Table](mcp://flutter/api/widgets/Table).

[TapDownDetails](mcp://flutter/api/gestures/TapDownDetails)
Details for [GestureTapDownCallback](mcp://flutter/api/gestures/GestureTapDownCallback), such as position.

[TapRegion](mcp://flutter/api/widgets/TapRegion)
A widget that defines a region that can detect taps inside or outside of
itself and any group of regions it belongs to, without participating in the
[gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system
(other than to consume tap down events if [consumeOutsideTaps](mcp://flutter/api/widgets/TapRegion/consumeOutsideTaps) is true).

[TapRegionRegistry](mcp://flutter/api/widgets/TapRegionRegistry)
An interface for registering and unregistering a [RenderTapRegion](mcp://flutter/api/widgets/RenderTapRegion) (typically created with a [TapRegion](mcp://flutter/api/widgets/TapRegion) widget) with a
[RenderTapRegionSurface](mcp://flutter/api/widgets/RenderTapRegionSurface) (typically created with a [TapRegionSurface](mcp://flutter/api/widgets/TapRegionSurface) widget).

[TapRegionSurface](mcp://flutter/api/widgets/TapRegionSurface)
A widget that provides notification of a tap inside or outside of a set of
registered regions, without participating in the [gesture disambiguation](https://flutter.dev/to/gesture-disambiguation) system.

[TapUpDetails](mcp://flutter/api/gestures/TapUpDetails)
Details for [GestureTapUpCallback](mcp://flutter/api/gestures/GestureTapUpCallback), such as position.

[Text](mcp://flutter/api/widgets/Text)
A run of text with a single style.

[TextAlignVertical](mcp://flutter/api/painting/TextAlignVertical)
The vertical alignment of text within an input box.

[TextBox](mcp://flutter/api/dart-ui/TextBox)
A rectangle enclosing a run of text.

[TextDecoration](mcp://flutter/api/dart-ui/TextDecoration)
A linear decoration to draw near the text.

[TextEditingController](mcp://flutter/api/widgets/TextEditingController)
A controller for an editable text field.

[TextEditingValue](mcp://flutter/api/flutter_test/TextEditingValue)
The current text, selection, and composing state for editing a run of text.

[TextFieldTapRegion](mcp://flutter/api/widgets/TextFieldTapRegion)
A [TapRegion](mcp://flutter/api/widgets/TapRegion) that adds its children to the tap region group for widgets
based on the [EditableText](mcp://flutter/api/widgets/EditableText) text editing widget, such as [TextField](mcp://flutter/api/material/TextField) and
[CupertinoTextField](mcp://flutter/api/cupertino/CupertinoTextField).

[TextHeightBehavior](mcp://flutter/api/dart-ui/TextHeightBehavior)
Defines how to apply `TextStyle.height` over and under text.

[TextInputType](mcp://flutter/api/services/TextInputType)
The type of information for which to optimize the text input control.

[TextMagnifierConfiguration](mcp://flutter/api/widgets/TextMagnifierConfiguration)
A configuration object for a magnifier (e.g. in a text field).

[TextPainter](mcp://flutter/api/painting/TextPainter)
An object that paints a [TextSpan](mcp://flutter/api/painting/TextSpan) tree into a [Canvas](mcp://flutter/api/dart-ui/Canvas).

[TextPosition](mcp://flutter/api/dart-ui/TextPosition)
A position in a string of text.

[TextRange](mcp://flutter/api/dart-ui/TextRange)
A range of characters in a string of text.

[TextScaler](mcp://flutter/api/painting/TextScaler)
A class that describes how textual contents should be scaled for better
readability.

[TextSelection](mcp://flutter/api/services/TextSelection)
A range of text that represents a selection.

[TextSelectionControls](mcp://flutter/api/widgets/TextSelectionControls)
An interface for building the selection UI, to be provided by the
implementer of the toolbar widget.

[TextSelectionGestureDetector](mcp://flutter/api/widgets/TextSelectionGestureDetector)
A gesture detector to respond to non-exclusive event chains for a text field.

[TextSelectionGestureDetectorBuilder](mcp://flutter/api/widgets/TextSelectionGestureDetectorBuilder)
Builds a [TextSelectionGestureDetector](mcp://flutter/api/widgets/TextSelectionGestureDetector) to wrap an [EditableText](mcp://flutter/api/widgets/EditableText).

[TextSelectionGestureDetectorBuilderDelegate](mcp://flutter/api/widgets/TextSelectionGestureDetectorBuilderDelegate)
Delegate interface for the [TextSelectionGestureDetectorBuilder](mcp://flutter/api/widgets/TextSelectionGestureDetectorBuilder).

[TextSelectionOverlay](mcp://flutter/api/widgets/TextSelectionOverlay)
An object that manages a pair of text selection handles for a
[RenderEditable](mcp://flutter/api/rendering/RenderEditable).

[TextSelectionPoint](mcp://flutter/api/rendering/TextSelectionPoint)
Represents the coordinates of the point in a selection, and the text
direction at that point, relative to top left of the [RenderEditable](mcp://flutter/api/rendering/RenderEditable) that
holds the selection.

[TextSelectionToolbarAnchors](mcp://flutter/api/widgets/TextSelectionToolbarAnchors)
The position information for a text selection toolbar.

[TextSelectionToolbarLayoutDelegate](mcp://flutter/api/widgets/TextSelectionToolbarLayoutDelegate)
A [SingleChildLayoutDelegate](mcp://flutter/api/rendering/SingleChildLayoutDelegate) for use with [CustomSingleChildLayout](mcp://flutter/api/widgets/CustomSingleChildLayout) that
positions its child above [anchorAbove](mcp://flutter/api/widgets/TextSelectionToolbarLayoutDelegate/anchorAbove) if it fits, or otherwise below
[anchorBelow](mcp://flutter/api/widgets/TextSelectionToolbarLayoutDelegate/anchorBelow).

[TextSpan](mcp://flutter/api/painting/TextSpan)
An immutable span of text.

[TextStyle](mcp://flutter/api/painting/TextStyle)
An immutable style describing how to format and paint text.

[TextStyleTween](mcp://flutter/api/widgets/TextStyleTween)
An interpolation between two [TextStyle](mcp://flutter/api/painting/TextStyle) s.

[Texture](mcp://flutter/api/widgets/Texture)
A rectangle upon which a backend texture is mapped.

[ThreePointCubic](mcp://flutter/api/animation/ThreePointCubic)
A cubic polynomial composed of two curves that share a common center point.

[Threshold](mcp://flutter/api/animation/Threshold)
A curve that is 0.0 until it hits the threshold, then it jumps to 1.0.

[TickerFuture](mcp://flutter/api/scheduler/TickerFuture)
An object representing an ongoing [Ticker](mcp://flutter/api/scheduler/Ticker) sequence.

[TickerMode](mcp://flutter/api/widgets/TickerMode)
Enables or disables tickers (and thus animation controllers) in the widget
subtree.

[TickerProvider](mcp://flutter/api/scheduler/TickerProvider)
An interface implemented by classes that can vend [Ticker](mcp://flutter/api/scheduler/Ticker) objects.

[Title](mcp://flutter/api/widgets/Title)
A widget that describes this app in the operating system.

[ToggleablePainter](mcp://flutter/api/widgets/ToggleablePainter)
A base class for a [CustomPainter](mcp://flutter/api/rendering/CustomPainter) that may be passed to
[ToggleableStateMixin.buildToggleable](mcp://flutter/api/widgets/ToggleableStateMixin/buildToggleable) to draw the visual representation of
a Toggleable.

[Tolerance](mcp://flutter/api/physics/Tolerance)
Structure that specifies maximum allowable magnitudes for distances,
durations, and velocity differences to be considered equal.

[ToolbarItemsParentData](mcp://flutter/api/widgets/ToolbarItemsParentData)
ParentData that determines whether or not to paint the corresponding child.

[ToolbarOptions](mcp://flutter/api/widgets/ToolbarOptions)
Toolbar configuration for [EditableText](mcp://flutter/api/widgets/EditableText).

[TrackingScrollController](mcp://flutter/api/widgets/TrackingScrollController)
A [ScrollController](mcp://flutter/api/widgets/ScrollController) whose [initialScrollOffset](mcp://flutter/api/widgets/TrackingScrollController/initialScrollOffset) tracks its most recently
updated [ScrollPosition](mcp://flutter/api/widgets/ScrollPosition).

[TrainHoppingAnimation](mcp://flutter/api/animation/TrainHoppingAnimation)
This animation starts by proxying one animation, but when the value of that
animation crosses the value of the second (either because the second is
going in the opposite direction, or because the one overtakes the other),
the animation hops over to proxying the second animation.

[Transform](mcp://flutter/api/widgets/Transform)
A widget that applies a transformation before painting its child.

[TransformationController](mcp://flutter/api/widgets/TransformationController)
A thin wrapper on [ValueNotifier](mcp://flutter/api/foundation/ValueNotifier) whose value is a [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4) representing a
transformation.

[TransformProperty](mcp://flutter/api/painting/TransformProperty)
Property which handles [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4) that represent transforms.

[TransitionDelegate](mcp://flutter/api/widgets/TransitionDelegate)<T>
The delegate that decides how pages added and removed from [Navigator.pages](mcp://flutter/api/widgets/Navigator/pages) transition in or out of the screen.

[TransitionRoute](mcp://flutter/api/widgets/TransitionRoute)<T>
A route with entrance and exit transitions.

[TransposeCharactersIntent](mcp://flutter/api/widgets/TransposeCharactersIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a user interaction that attempts to swap the
characters immediately around the cursor.

[TreeSliver](mcp://flutter/api/widgets/TreeSliver)<T>
A widget that displays [TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode) s that expand and collapse in a
vertically and horizontally scrolling [Viewport](mcp://flutter/api/widgets/Viewport).

[TreeSliverController](mcp://flutter/api/widgets/TreeSliverController)
Enables control over the [TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode) s of a [TreeSliver](mcp://flutter/api/widgets/TreeSliver).

[TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode)<T>
A data structure for configuring children of a [TreeSliver](mcp://flutter/api/widgets/TreeSliver).

[Tween](mcp://flutter/api/animation/Tween)<T extends [Object](mcp://flutter/api/dart-core/Object)?>
A linear interpolation between a beginning and ending value.

[TweenAnimationBuilder](mcp://flutter/api/widgets/TweenAnimationBuilder)<T extends [Object](mcp://flutter/api/dart-core/Object)?>
[Widget](mcp://flutter/api/widgets/Widget) builder that animates a property of a [Widget](mcp://flutter/api/widgets/Widget) to a target value
whenever the target value changes.

[TweenSequence](mcp://flutter/api/animation/TweenSequence)<T>
Enables creating an [Animation](mcp://flutter/api/animation/Animation) whose value is defined by a sequence of
[Tween](mcp://flutter/api/animation/Tween) s.

[TweenSequenceItem](mcp://flutter/api/animation/TweenSequenceItem)<T>
A simple holder for one element of a [TweenSequence](mcp://flutter/api/animation/TweenSequence).

[TwoDimensionalChildBuilderDelegate](mcp://flutter/api/widgets/TwoDimensionalChildBuilderDelegate)
A delegate that supplies children for a [TwoDimensionalScrollView](mcp://flutter/api/widgets/TwoDimensionalScrollView) using a
builder callback.

[TwoDimensionalChildDelegate](mcp://flutter/api/widgets/TwoDimensionalChildDelegate)
A delegate that supplies children for scrolling in two dimensions.

[TwoDimensionalChildListDelegate](mcp://flutter/api/widgets/TwoDimensionalChildListDelegate)
A delegate that supplies children for a [TwoDimensionalViewport](mcp://flutter/api/widgets/TwoDimensionalViewport) using an
explicit two dimensional array.

[TwoDimensionalChildManager](mcp://flutter/api/widgets/TwoDimensionalChildManager)
A delegate used by [RenderTwoDimensionalViewport](mcp://flutter/api/widgets/RenderTwoDimensionalViewport) to manage its children.

[TwoDimensionalScrollable](mcp://flutter/api/widgets/TwoDimensionalScrollable)
A widget that manages scrolling in both the vertical and horizontal
dimensions and informs the [TwoDimensionalViewport](mcp://flutter/api/widgets/TwoDimensionalViewport) through which the
content is viewed.

[TwoDimensionalScrollableState](mcp://flutter/api/widgets/TwoDimensionalScrollableState)
State object for a [TwoDimensionalScrollable](mcp://flutter/api/widgets/TwoDimensionalScrollable) widget.

[TwoDimensionalScrollView](mcp://flutter/api/widgets/TwoDimensionalScrollView)
A widget that combines a [TwoDimensionalScrollable](mcp://flutter/api/widgets/TwoDimensionalScrollable) and a
[TwoDimensionalViewport](mcp://flutter/api/widgets/TwoDimensionalViewport) to create an interactive scrolling pane of content
in both vertical and horizontal dimensions.

[TwoDimensionalViewport](mcp://flutter/api/widgets/TwoDimensionalViewport)
A widget through which a portion of larger content can be viewed, typically
in combination with a [TwoDimensionalScrollable](mcp://flutter/api/widgets/TwoDimensionalScrollable).

[TwoDimensionalViewportParentData](mcp://flutter/api/widgets/TwoDimensionalViewportParentData)
Parent data structure used by [RenderTwoDimensionalViewport](mcp://flutter/api/widgets/RenderTwoDimensionalViewport).

[UiKitView](mcp://flutter/api/widgets/UiKitView)
Embeds an iOS view in the Widget hierarchy.

[UnconstrainedBox](mcp://flutter/api/widgets/UnconstrainedBox)
A widget that imposes no constraints on its child, allowing it to render
at its "natural" size.

[UndoHistory](mcp://flutter/api/widgets/UndoHistory)<T>
Provides undo/redo capabilities for a [ValueNotifier](mcp://flutter/api/foundation/ValueNotifier).

[UndoHistoryController](mcp://flutter/api/widgets/UndoHistoryController)
A controller for the undo history, for example for an editable text field.

[UndoHistoryState](mcp://flutter/api/widgets/UndoHistoryState)<T>
State for a [UndoHistory](mcp://flutter/api/widgets/UndoHistory).

[UndoHistoryValue](mcp://flutter/api/widgets/UndoHistoryValue)
Represents whether the current undo stack can undo or redo.

[UndoTextIntent](mcp://flutter/api/widgets/UndoTextIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a user interaction that attempts to go back to
the previous editing state.

[UniqueKey](mcp://flutter/api/foundation/UniqueKey)
A key that is only equal to itself.

[UniqueWidget](mcp://flutter/api/widgets/UniqueWidget)<T extends [State](mcp://flutter/api/widgets/State)<[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>>
Base class for stateful widgets that have exactly one inflated instance in
the tree.

[UnmanagedRestorationScope](mcp://flutter/api/widgets/UnmanagedRestorationScope)
Inserts a provided [RestorationBucket](mcp://flutter/api/services/RestorationBucket) into the widget tree and makes it
available to descendants via [RestorationScope.of](mcp://flutter/api/widgets/RestorationScope/of).

[UpdateSelectionIntent](mcp://flutter/api/widgets/UpdateSelectionIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that represents a user interaction that attempts to change the
selection in an input field.

[UserScrollNotification](mcp://flutter/api/widgets/UserScrollNotification)
A notification that the user has changed the [ScrollDirection](mcp://flutter/api/rendering/ScrollDirection) in which they
are scrolling, or have stopped scrolling.

[ValueKey](mcp://flutter/api/foundation/ValueKey)<T>
A key that uses a value of a particular type to identify itself.

[ValueListenableBuilder](mcp://flutter/api/widgets/ValueListenableBuilder)<T>
A widget whose content stays synced with a [ValueListenable](mcp://flutter/api/foundation/ValueListenable).

[ValueNotifier](mcp://flutter/api/foundation/ValueNotifier)<T>
A [ChangeNotifier](mcp://flutter/api/foundation/ChangeNotifier) that holds a single value.

[Velocity](mcp://flutter/api/gestures/Velocity)
A velocity in two dimensions.

[View](mcp://flutter/api/widgets/View)
Bootstraps a render tree that is rendered into the provided [FlutterView](mcp://flutter/api/dart-ui/FlutterView).

[ViewAnchor](mcp://flutter/api/widgets/ViewAnchor)
Decorates a [child](mcp://flutter/api/widgets/ViewAnchor/child) widget with a side [View](mcp://flutter/api/widgets/View).

[ViewCollection](mcp://flutter/api/widgets/ViewCollection)
A collection of sibling [View](mcp://flutter/api/widgets/View) s.

[Viewport](mcp://flutter/api/widgets/Viewport)
A widget through which a portion of larger content can be viewed, typically
in combination with a [Scrollable](mcp://flutter/api/widgets/Scrollable).

[Visibility](mcp://flutter/api/widgets/Visibility)
Whether to show or hide a child.

[VoidCallbackAction](mcp://flutter/api/widgets/VoidCallbackAction)
An [Action](mcp://flutter/api/widgets/Action) that invokes the [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) given to it in the
[VoidCallbackIntent](mcp://flutter/api/widgets/VoidCallbackIntent) passed to it when invoked.

[VoidCallbackIntent](mcp://flutter/api/widgets/VoidCallbackIntent)
An [Intent](mcp://flutter/api/widgets/Intent) that keeps a [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) to be invoked by a
[VoidCallbackAction](mcp://flutter/api/widgets/VoidCallbackAction) when it receives this intent.

[WeakMap](mcp://flutter/api/widgets/WeakMap)<K, V>
Does not hold keys from garbage collection.

[Widget](mcp://flutter/api/widgets/Widget)
Describes the configuration for an [Element](mcp://flutter/api/widgets/Element).

[WidgetInspector](mcp://flutter/api/widgets/WidgetInspector)
A widget that enables inspecting the child widget's structure.

[WidgetOrderTraversalPolicy](mcp://flutter/api/widgets/WidgetOrderTraversalPolicy)
A [FocusTraversalPolicy](mcp://flutter/api/widgets/FocusTraversalPolicy) that traverses the focus order in widget hierarchy
order.

[WidgetsApp](mcp://flutter/api/widgets/WidgetsApp)
A convenience widget that wraps a number of widgets that are commonly
required for an application.

[WidgetsBindingObserver](mcp://flutter/api/widgets/WidgetsBindingObserver)
Interface for classes that register with the Widgets layer binding.

[WidgetsFlutterBinding](mcp://flutter/api/widgets/WidgetsFlutterBinding)
A concrete binding for applications based on the Widgets framework.

[WidgetsLocalizations](mcp://flutter/api/widgets/WidgetsLocalizations)
Interface for localized resource values for the lowest levels of the Flutter
framework.

[WidgetSpan](mcp://flutter/api/widgets/WidgetSpan)
An immutable widget that is embedded inline within text.

[WidgetStateBorderSide](mcp://flutter/api/widgets/WidgetStateBorderSide)
Defines a [BorderSide](mcp://flutter/api/painting/BorderSide) whose value depends on a set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s
which represent the interactive state of a component.

[WidgetStateColor](mcp://flutter/api/widgets/WidgetStateColor)
Defines a [Color](mcp://flutter/api/dart-ui/Color) that is also a [WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty).

[WidgetStateMapper](mcp://flutter/api/widgets/WidgetStateMapper)<T>
Uses a [WidgetStateMap](mcp://flutter/api/widgets/WidgetStateMap) to resolve to a single value of type `T` based on
the current set of Widget states.

[WidgetStateMouseCursor](mcp://flutter/api/widgets/WidgetStateMouseCursor)
Defines a [MouseCursor](mcp://flutter/api/services/MouseCursor) whose value depends on a set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s which
represent the interactive state of a component.

[WidgetStateOutlinedBorder](mcp://flutter/api/widgets/WidgetStateOutlinedBorder)
Defines an [OutlinedBorder](mcp://flutter/api/painting/OutlinedBorder) whose value depends on a set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s
which represent the interactive state of a component.

[WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty)<T>
Interface for classes that [resolve](mcp://flutter/api/widgets/WidgetStateProperty/resolve) to a value of type `T` based
on a widget's interactive "state", which is defined as a set
of [WidgetState](mcp://flutter/api/widgets/WidgetState) s.

[WidgetStatePropertyAll](mcp://flutter/api/widgets/WidgetStatePropertyAll)<T>
Convenience class for creating a [WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty) that
resolves to the given value for all states.

[WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint)
This class allows [WidgetState](mcp://flutter/api/widgets/WidgetState) enum values to be combined
using [WidgetStateOperators](mcp://flutter/api/widgets/WidgetStateOperators).

[WidgetStatesController](mcp://flutter/api/widgets/WidgetStatesController)
Manages a set of [WidgetState](mcp://flutter/api/widgets/WidgetState) s and notifies listeners of changes.

[WidgetStateTextStyle](mcp://flutter/api/widgets/WidgetStateTextStyle)
Defines a [TextStyle](mcp://flutter/api/painting/TextStyle) that is also a [WidgetStateProperty](mcp://flutter/api/widgets/WidgetStateProperty).

[WidgetToRenderBoxAdapter](mcp://flutter/api/widgets/WidgetToRenderBoxAdapter)
An adapter for placing a specific [RenderBox](mcp://flutter/api/rendering/RenderBox) in the widget tree.

[WillPopScope](mcp://flutter/api/widgets/WillPopScope)
Registers a callback to veto attempts by the user to dismiss the enclosing
[ModalRoute](mcp://flutter/api/widgets/ModalRoute).

[WordBoundary](mcp://flutter/api/painting/WordBoundary)
A [TextBoundary](mcp://flutter/api/services/TextBoundary) subclass for locating word breaks.

[Wrap](mcp://flutter/api/widgets/Wrap)
A widget that displays its children in multiple horizontal or vertical runs.

## Enums

[AndroidOverscrollIndicator](mcp://flutter/api/widgets/AndroidOverscrollIndicator)
Types of overscroll indicators supported by [TargetPlatform.android](mcp://flutter/api/foundation/TargetPlatform).

[AnimationBehavior](mcp://flutter/api/animation/AnimationBehavior)
Configures how an [AnimationController](mcp://flutter/api/animation/AnimationController) behaves when animations are
disabled.

[AnimationStatus](mcp://flutter/api/animation/AnimationStatus)
The status of an animation.

[AppLifecycleState](mcp://flutter/api/dart-ui/AppLifecycleState)
States that an application can be in once it is running.

[AutofillContextAction](mcp://flutter/api/widgets/AutofillContextAction)
Predefined autofill context clean up actions.

[AutovalidateMode](mcp://flutter/api/widgets/AutovalidateMode)
Used to configure the auto validation of [FormField](mcp://flutter/api/widgets/FormField) and [Form](mcp://flutter/api/widgets/Form) widgets.

[Axis](mcp://flutter/api/painting/Axis)
The two cardinal directions in two dimensions.

[AxisDirection](mcp://flutter/api/painting/AxisDirection)
A direction along either the horizontal or vertical [Axis](mcp://flutter/api/painting/Axis) in which the
origin, or zero position, is determined.

[BannerLocation](mcp://flutter/api/widgets/BannerLocation)
Where to show a [Banner](mcp://flutter/api/widgets/Banner).

[BlendMode](mcp://flutter/api/dart-ui/BlendMode)
Algorithms to use when painting on the canvas.

[BlurStyle](mcp://flutter/api/dart-ui/BlurStyle)
Styles to use for blurs in [MaskFilter](mcp://flutter/api/dart-ui/MaskFilter) objects.

[BorderStyle](mcp://flutter/api/painting/BorderStyle)
The style of line to draw for a [BorderSide](mcp://flutter/api/painting/BorderSide) in a [Border](mcp://flutter/api/painting/Border).

[BoxFit](mcp://flutter/api/painting/BoxFit)
How a box should be inscribed into another box.

[BoxShape](mcp://flutter/api/painting/BoxShape)
The shape to use when rendering a [Border](mcp://flutter/api/painting/Border) or [BoxDecoration](mcp://flutter/api/painting/BoxDecoration).

[Brightness](mcp://flutter/api/dart-ui/Brightness)
Describes the contrast of a theme or color palette.

[ChangeReportingBehavior](mcp://flutter/api/widgets/ChangeReportingBehavior)
The behavior of reporting the selected item index in a [ListWheelScrollView](mcp://flutter/api/widgets/ListWheelScrollView).

[Clip](mcp://flutter/api/dart-ui/Clip)
Different ways to clip content.

[ClipboardStatus](mcp://flutter/api/widgets/ClipboardStatus)
An enumeration of the status of the content on the user's clipboard.

[ConnectionState](mcp://flutter/api/widgets/ConnectionState)
The state of connection to an asynchronous computation.

[ContextMenuButtonType](mcp://flutter/api/widgets/ContextMenuButtonType)
The buttons that can appear in a context menu by default.

[CrossAxisAlignment](mcp://flutter/api/rendering/CrossAxisAlignment)
How the children should be placed along the cross axis in a flex layout.

[CrossFadeState](mcp://flutter/api/widgets/CrossFadeState)
Specifies which of two children to show. See [AnimatedCrossFade](mcp://flutter/api/widgets/AnimatedCrossFade).

[DecorationPosition](mcp://flutter/api/rendering/DecorationPosition)
Where to paint a box decoration.

[DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel)
The various priority levels used to filter which diagnostics are shown and
omitted.

[DiagonalDragBehavior](mcp://flutter/api/widgets/DiagonalDragBehavior)
Specifies how to configure the [DragGestureRecognizer](mcp://flutter/api/gestures/DragGestureRecognizer) s of a
[TwoDimensionalScrollable](mcp://flutter/api/widgets/TwoDimensionalScrollable).

[DismissDirection](mcp://flutter/api/widgets/DismissDirection)
The direction in which a [Dismissible](mcp://flutter/api/widgets/Dismissible) can be dismissed.

[FilterQuality](mcp://flutter/api/dart-ui/FilterQuality)
Quality levels for image sampling in [ImageFilter](mcp://flutter/api/dart-ui/ImageFilter) and [Shader](mcp://flutter/api/dart-ui/Shader) objects that sample
images and for [Canvas](mcp://flutter/api/dart-ui/Canvas) operations that render images.

[FlexFit](mcp://flutter/api/rendering/FlexFit)
How the child is inscribed into the available space.

[FloatingHeaderSnapMode](mcp://flutter/api/widgets/FloatingHeaderSnapMode)
Specifies how a partially visible [SliverFloatingHeader](mcp://flutter/api/widgets/SliverFloatingHeader) animates
into a view when a user scroll gesture ends.

[FlutterLogoStyle](mcp://flutter/api/painting/FlutterLogoStyle)
Possible ways to draw Flutter's logo.

[FocusHighlightMode](mcp://flutter/api/widgets/FocusHighlightMode)
An enum to describe which kind of focus highlight behavior to use when
displaying focus information.

[FocusHighlightStrategy](mcp://flutter/api/widgets/FocusHighlightStrategy)
An enum to describe how the current value of [FocusManager.highlightMode](mcp://flutter/api/widgets/FocusManager/highlightMode) is
determined. The strategy is set on [FocusManager.highlightStrategy](mcp://flutter/api/widgets/FocusManager/highlightStrategy).

[FontStyle](mcp://flutter/api/dart-ui/FontStyle)
Whether to use the italic type variation of glyphs in the font.

[GrowthDirection](mcp://flutter/api/rendering/GrowthDirection)
The direction in which a sliver's contents are ordered, relative to the
scroll offset axis.

[HeroFlightDirection](mcp://flutter/api/widgets/HeroFlightDirection)
Direction of the hero's flight based on the navigation operation.

[HitTestBehavior](mcp://flutter/api/rendering/HitTestBehavior)
How to behave during hit tests.

[ImageRepeat](mcp://flutter/api/painting/ImageRepeat)
How to paint any portions of a box not covered by an image.

[InspectorButtonVariant](mcp://flutter/api/widgets/InspectorButtonVariant)
Defines the visual and behavioral variants for an [InspectorButton](mcp://flutter/api/widgets/InspectorButton).

[KeyEventResult](mcp://flutter/api/widgets/KeyEventResult)
An enum that describes how to handle a key event handled by a
[FocusOnKeyCallback](mcp://flutter/api/widgets/FocusOnKeyCallback) or [FocusOnKeyEventCallback](mcp://flutter/api/widgets/FocusOnKeyEventCallback).

[LiveTextInputStatus](mcp://flutter/api/widgets/LiveTextInputStatus)
An enumeration that indicates whether the current device is available for Live Text input.

[LockState](mcp://flutter/api/widgets/LockState)
Determines how the state of a lock key is used to accept a shortcut.

[MainAxisAlignment](mcp://flutter/api/rendering/MainAxisAlignment)
How the children should be placed along the main axis in a flex layout.

[MainAxisSize](mcp://flutter/api/rendering/MainAxisSize)
How much space should be occupied in the main axis.

[NavigationMode](mcp://flutter/api/widgets/NavigationMode)
Describes the navigation mode to be set by a [MediaQuery](mcp://flutter/api/widgets/MediaQuery) widget.

[OptionsViewOpenDirection](mcp://flutter/api/widgets/OptionsViewOpenDirection)
A direction in which to open the options-view overlay.

[Orientation](mcp://flutter/api/widgets/Orientation)
Whether in portrait or landscape.

[OverflowBarAlignment](mcp://flutter/api/widgets/OverflowBarAlignment)
Defines the horizontal alignment of [OverflowBar](mcp://flutter/api/widgets/OverflowBar) children
when they're laid out in an overflow column.

[OverlayChildLocation](mcp://flutter/api/widgets/OverlayChildLocation)
The location of the [Overlay](mcp://flutter/api/widgets/Overlay) that an [OverlayPortal](mcp://flutter/api/widgets/OverlayPortal) renders its overlay
child on.

[PaintingStyle](mcp://flutter/api/dart-ui/PaintingStyle)
Strategies for painting shapes and paths on a canvas.

[PanAxis](mcp://flutter/api/widgets/PanAxis)
This enum is used to specify the behavior of the [InteractiveViewer](mcp://flutter/api/widgets/InteractiveViewer) when
the user drags the viewport.

[PathFillType](mcp://flutter/api/dart-ui/PathFillType)
Determines the winding rule that decides how the interior of a [Path](mcp://flutter/api/dart-ui/Path) is
calculated.

[PathOperation](mcp://flutter/api/dart-ui/PathOperation)
Strategies for combining paths.

[PlaceholderAlignment](mcp://flutter/api/dart-ui/PlaceholderAlignment)
Where to vertically align the placeholder relative to the surrounding text.

[PlatformProvidedMenuItemType](mcp://flutter/api/widgets/PlatformProvidedMenuItemType)
The list of possible platform provided, prebuilt menus for use in a
[PlatformMenuBar](mcp://flutter/api/widgets/PlatformMenuBar).

[RenderComparison](mcp://flutter/api/painting/RenderComparison)
The description of the difference between two objects, in the context of how
it will affect the rendering.

[ResizeImagePolicy](mcp://flutter/api/painting/ResizeImagePolicy)
Configures the behavior for [ResizeImage](mcp://flutter/api/painting/ResizeImage).

[RouteInformationReportingType](mcp://flutter/api/widgets/RouteInformationReportingType)
The [Router](mcp://flutter/api/widgets/Router)'s intention when it reports a new [RouteInformation](mcp://flutter/api/widgets/RouteInformation) to the
[RouteInformationProvider](mcp://flutter/api/widgets/RouteInformationProvider).

[RoutePopDisposition](mcp://flutter/api/widgets/RoutePopDisposition)
Indicates whether the current route should be popped.

[ScrollbarOrientation](mcp://flutter/api/widgets/ScrollbarOrientation)
An orientation along either the horizontal or vertical [Axis](mcp://flutter/api/painting/Axis).

[ScrollDecelerationRate](mcp://flutter/api/widgets/ScrollDecelerationRate)
The rate at which scroll momentum will be decelerated.

[ScrollIncrementType](mcp://flutter/api/widgets/ScrollIncrementType)
Describes the type of scroll increment that will be performed by a
[ScrollAction](mcp://flutter/api/widgets/ScrollAction) on a [Scrollable](mcp://flutter/api/widgets/Scrollable).

[ScrollPositionAlignmentPolicy](mcp://flutter/api/widgets/ScrollPositionAlignmentPolicy)
The policy to use when applying the `alignment` parameter of
[ScrollPosition.ensureVisible](mcp://flutter/api/widgets/ScrollPosition/ensureVisible).

[ScrollViewKeyboardDismissBehavior](mcp://flutter/api/widgets/ScrollViewKeyboardDismissBehavior)
A representation of how a [ScrollView](mcp://flutter/api/widgets/ScrollView) should dismiss the on-screen
keyboard.

[SelectableRegionSelectionStatus](mcp://flutter/api/widgets/SelectableRegionSelectionStatus)
The status of the selection under a [SelectableRegion](mcp://flutter/api/widgets/SelectableRegion).

[SelectionChangedCause](mcp://flutter/api/services/SelectionChangedCause)
Indicates what triggered the change in selected text (including changes to
the cursor location).

[SliverPaintOrder](mcp://flutter/api/rendering/SliverPaintOrder)
Specifies an order in which to paint the slivers of a [Viewport](mcp://flutter/api/widgets/Viewport).

[SmartDashesType](mcp://flutter/api/services/SmartDashesType)
Indicates how to handle the intelligent replacement of dashes in text input.

[SmartQuotesType](mcp://flutter/api/services/SmartQuotesType)
Indicates how to handle the intelligent replacement of quotes in text input.

[SnapshotMode](mcp://flutter/api/widgets/SnapshotMode)
Controls how the [SnapshotWidget](mcp://flutter/api/widgets/SnapshotWidget) paints its child.

[StackFit](mcp://flutter/api/rendering/StackFit)
How to size the non-positioned children of a [Stack](mcp://flutter/api/widgets/Stack).

[StandardComponentType](mcp://flutter/api/widgets/StandardComponentType)
An enum identifying standard UI components.

[StrokeCap](mcp://flutter/api/dart-ui/StrokeCap)
Styles to use for line endings.

[StrokeJoin](mcp://flutter/api/dart-ui/StrokeJoin)
Styles to use for line segment joins.

[TableCellVerticalAlignment](mcp://flutter/api/rendering/TableCellVerticalAlignment)
Vertical alignment options for cells in [RenderTable](mcp://flutter/api/rendering/RenderTable) objects.

[TargetPlatform](mcp://flutter/api/foundation/TargetPlatform)
The platform that user interaction should adapt to target.

[TextAffinity](mcp://flutter/api/dart-ui/TextAffinity)
A way to disambiguate a [TextPosition](mcp://flutter/api/dart-ui/TextPosition) when its offset could match two
different locations in the rendered string.

[TextAlign](mcp://flutter/api/dart-ui/TextAlign)
Whether and how to align text horizontally.

[TextBaseline](mcp://flutter/api/dart-ui/TextBaseline)
A horizontal line used for aligning text.

[TextDecorationStyle](mcp://flutter/api/dart-ui/TextDecorationStyle)
The style in which to draw a text decoration

[TextDirection](mcp://flutter/api/dart-ui/TextDirection)
A direction in which text flows.

[TextLeadingDistribution](mcp://flutter/api/dart-ui/TextLeadingDistribution)
How the ["leading"](https://en.wikipedia.org/wiki/Leading) is distributed
over and under the text.

[TextOverflow](mcp://flutter/api/painting/TextOverflow)
How overflowing text should be handled.

[TextSelectionHandleType](mcp://flutter/api/rendering/TextSelectionHandleType)
The type of selection handle to be displayed.

[TextWidthBasis](mcp://flutter/api/painting/TextWidthBasis)
The different ways of measuring the width of one or more lines of text.

[TileMode](mcp://flutter/api/dart-ui/TileMode)
Defines how to handle areas outside the defined bounds of a gradient or image filter.

[TraversalDirection](mcp://flutter/api/widgets/TraversalDirection)
A direction along either the horizontal or vertical axes.

[TraversalEdgeBehavior](mcp://flutter/api/widgets/TraversalEdgeBehavior)
Controls the focus transfer at the edges of a [FocusScopeNode](mcp://flutter/api/widgets/FocusScopeNode).
For movement transfers (previous or next), the edge represents
the first or last items. For directional transfers, the edge
represents the outermost items of the [FocusScopeNode](mcp://flutter/api/widgets/FocusScopeNode), For example:
for moving downwards, the edge node is the one with the largest bottom
coordinate; for moving leftwards, the edge node is the one with the
smallest x coordinate.

[UnfocusDisposition](mcp://flutter/api/widgets/UnfocusDisposition)
Describe what should happen after [FocusNode.unfocus](mcp://flutter/api/widgets/FocusNode/unfocus) is called.

[VertexMode](mcp://flutter/api/dart-ui/VertexMode)
Defines how a list of points is interpreted when drawing a set of triangles.

[VerticalDirection](mcp://flutter/api/painting/VerticalDirection)
A direction in which boxes flow vertically.

[WebHtmlElementStrategy](mcp://flutter/api/painting/WebHtmlElementStrategy)
The strategy for [Image.network](mcp://flutter/api/widgets/Image/Image.network) and [NetworkImage](mcp://flutter/api/painting/NetworkImage) to decide whether to
display images in HTML elements contained in a platform view instead of
fetching bytes.

[WidgetInspectorServiceExtensions](mcp://flutter/api/widgets/WidgetInspectorServiceExtensions)
Service extension constants for the Widget Inspector.

[WidgetsServiceExtensions](mcp://flutter/api/widgets/WidgetsServiceExtensions)
Service extension constants for the widgets library.

[WidgetState](mcp://flutter/api/widgets/WidgetState)
Interactive states that some of the widgets can take on when receiving input
from the user.

[WrapAlignment](mcp://flutter/api/rendering/WrapAlignment)
How [Wrap](mcp://flutter/api/widgets/Wrap) should align objects.

[WrapCrossAlignment](mcp://flutter/api/rendering/WrapCrossAlignment)
Who [Wrap](mcp://flutter/api/widgets/Wrap) should align children within a run in the cross axis.

## Mixins

[AnimationEagerListenerMixin](mcp://flutter/api/animation/AnimationEagerListenerMixin)
A mixin that replaces the [didRegisterListener](mcp://flutter/api/animation/AnimationEagerListenerMixin/didRegisterListener)/[didUnregisterListener](mcp://flutter/api/animation/AnimationEagerListenerMixin/didUnregisterListener) contract
with a dispose contract.

[AnimationLazyListenerMixin](mcp://flutter/api/animation/AnimationLazyListenerMixin)
A mixin that helps listen to another object only when this object has registered listeners.

[AnimationLocalListenersMixin](mcp://flutter/api/animation/AnimationLocalListenersMixin)
A mixin that implements the [addListener](mcp://flutter/api/animation/AnimationLocalListenersMixin/addListener)/[removeListener](mcp://flutter/api/animation/AnimationLocalListenersMixin/removeListener) protocol and notifies
all the registered listeners when [notifyListeners](mcp://flutter/api/animation/AnimationLocalListenersMixin/notifyListeners) is called.

[AnimationLocalStatusListenersMixin](mcp://flutter/api/animation/AnimationLocalStatusListenersMixin)
A mixin that implements the addStatusListener/removeStatusListener protocol
and notifies all the registered listeners when notifyStatusListeners is
called.

[AnimationWithParentMixin](mcp://flutter/api/animation/AnimationWithParentMixin)<T>
Implements most of the [Animation](mcp://flutter/api/animation/Animation) interface by deferring its behavior to a
given [parent](mcp://flutter/api/animation/AnimationWithParentMixin/parent) Animation.

[AutomaticKeepAliveClientMixin](mcp://flutter/api/widgets/AutomaticKeepAliveClientMixin)<T extends [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>
A mixin with convenience methods for clients of [AutomaticKeepAlive](mcp://flutter/api/widgets/AutomaticKeepAlive). It is used
with [State](mcp://flutter/api/widgets/State) subclasses to manage keep-alive behavior in lazily built lists.

[DirectionalFocusTraversalPolicyMixin](mcp://flutter/api/widgets/DirectionalFocusTraversalPolicyMixin)
A mixin class that provides an implementation for finding a node in a
particular direction.

[LocalHistoryRoute](mcp://flutter/api/widgets/LocalHistoryRoute)<T>
A mixin used by routes to handle back navigations internally by popping a list.

[MenuSerializableShortcut](mcp://flutter/api/widgets/MenuSerializableShortcut)
A mixin allowing a [ShortcutActivator](mcp://flutter/api/widgets/ShortcutActivator) to provide data for serialization of
the shortcut when sending to the platform.

[NotifiableElementMixin](mcp://flutter/api/widgets/NotifiableElementMixin)
Mixin this class to allow receiving [Notification](mcp://flutter/api/widgets/Notification) objects dispatched by
child elements.

[PaintingBinding](mcp://flutter/api/painting/PaintingBinding)
Binding for the painting library.

[PopNavigatorRouterDelegateMixin](mcp://flutter/api/widgets/PopNavigatorRouterDelegateMixin)<T>
A mixin that wires [RouterDelegate.popRoute](mcp://flutter/api/widgets/RouterDelegate/popRoute) to the [Navigator](mcp://flutter/api/widgets/Navigator) it builds.

[RadioClient](mcp://flutter/api/widgets/RadioClient)<T>
A client for a [RadioGroupRegistry](mcp://flutter/api/widgets/RadioGroupRegistry).

[RenderAbstractLayoutBuilderMixin](mcp://flutter/api/widgets/RenderAbstractLayoutBuilderMixin)<LayoutInfoType, ChildType extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
Generic mixin for [RenderObject](mcp://flutter/api/rendering/RenderObject) s created by an [AbstractLayoutBuilder](mcp://flutter/api/widgets/AbstractLayoutBuilder) with
the the same `LayoutInfoType`.

[RestorationMixin](mcp://flutter/api/widgets/RestorationMixin)<S extends [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>
Manages the restoration data for a [State](mcp://flutter/api/widgets/State) object of a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget).

[RootElementMixin](mcp://flutter/api/widgets/RootElementMixin)
Mixin for the element at the root of the tree.

[ScrollMetrics](mcp://flutter/api/widgets/ScrollMetrics)
A description of a [Scrollable](mcp://flutter/api/widgets/Scrollable)'s contents, useful for modeling the state
of its viewport.

[SingleTickerProviderStateMixin](mcp://flutter/api/widgets/SingleTickerProviderStateMixin)<T extends [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>
Provides a single [Ticker](mcp://flutter/api/scheduler/Ticker) that is configured to only tick while the current
tree is enabled, as defined by [TickerMode](mcp://flutter/api/widgets/TickerMode).

[SlottedContainerRenderObjectMixin](mcp://flutter/api/widgets/SlottedContainerRenderObjectMixin)<SlotType, ChildType extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
Mixin for a [RenderObject](mcp://flutter/api/rendering/RenderObject) configured by a [SlottedMultiChildRenderObjectWidget](mcp://flutter/api/widgets/SlottedMultiChildRenderObjectWidget).

[SlottedMultiChildRenderObjectWidgetMixin](mcp://flutter/api/widgets/SlottedMultiChildRenderObjectWidgetMixin)<SlotType, ChildType extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
A mixin version of [SlottedMultiChildRenderObjectWidget](mcp://flutter/api/widgets/SlottedMultiChildRenderObjectWidget).

[TextSelectionDelegate](mcp://flutter/api/services/TextSelectionDelegate)
A mixin for manipulating the selection, provided for toolbar or shortcut
keys.

[TextSelectionHandleControls](mcp://flutter/api/widgets/TextSelectionHandleControls)
[TextSelectionControls](mcp://flutter/api/widgets/TextSelectionControls) that specifically do not manage the toolbar in order
to leave that to [EditableText.contextMenuBuilder](mcp://flutter/api/widgets/EditableText/contextMenuBuilder).

[TickerProviderStateMixin](mcp://flutter/api/widgets/TickerProviderStateMixin)<T extends [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>
Provides [Ticker](mcp://flutter/api/scheduler/Ticker) objects that are configured to only tick while the current
tree is enabled, as defined by [TickerMode](mcp://flutter/api/widgets/TickerMode).

[ToggleableStateMixin](mcp://flutter/api/widgets/ToggleableStateMixin)<S extends [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>
A mixin for [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) s that implement toggleable
controls with toggle animations (e.g. [Switch](mcp://flutter/api/material/Switch) es, [CupertinoSwitch](mcp://flutter/api/cupertino/CupertinoSwitch) es,
[Checkbox](mcp://flutter/api/material/Checkbox) es, [CupertinoCheckbox](mcp://flutter/api/cupertino/CupertinoCheckbox) es, [Radio](mcp://flutter/api/material/Radio) s, and [CupertinoRadio](mcp://flutter/api/cupertino/CupertinoRadio) s).

[TreeSliverStateMixin](mcp://flutter/api/widgets/TreeSliverStateMixin)<T>
A mixin for classes implementing a tree structure as expected by a
[TreeSliverController](mcp://flutter/api/widgets/TreeSliverController).

[ViewportElementMixin](mcp://flutter/api/widgets/ViewportElementMixin)
A mixin that allows [Element](mcp://flutter/api/widgets/Element) s containing [Viewport](mcp://flutter/api/widgets/Viewport) like widgets to correctly
modify the notification depth of a [ViewportNotificationMixin](mcp://flutter/api/widgets/ViewportNotificationMixin).

[ViewportNotificationMixin](mcp://flutter/api/widgets/ViewportNotificationMixin)
Mixin for [Notification](mcp://flutter/api/widgets/Notification) s that track how many [RenderAbstractViewport](mcp://flutter/api/rendering/RenderAbstractViewport) they
have bubbled through.

[WidgetInspectorService](mcp://flutter/api/widgets/WidgetInspectorService)
Service used by GUI tools to interact with the [WidgetInspector](mcp://flutter/api/widgets/WidgetInspector).

[WidgetsBinding](mcp://flutter/api/widgets/WidgetsBinding)
The glue between the widgets layer and the Flutter engine.

## Extension Types

[OverlayChildLayoutInfo](mcp://flutter/api/widgets/OverlayChildLayoutInfo)
The additional layout information available to the
[OverlayPortal.overlayChildLayoutBuilder](mcp://flutter/api/widgets/OverlayPortal/OverlayPortal.overlayChildLayoutBuilder) callback.

## Extensions

[StringCharacters](mcp://flutter/api/package-characters_characters/StringCharacters) on [String](mcp://flutter/api/dart-core/String)
[WidgetStateOperators](mcp://flutter/api/widgets/WidgetStateOperators) on [WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint)
These operators can be used inside a [WidgetStateMap](mcp://flutter/api/widgets/WidgetStateMap) to combine states
and find a match.

## Constants

[factory](mcp://flutter/api/meta/factory) → const _Factory
Used to annotate an instance or static method `m`. Indicates that `m` must
either be abstract or must return a newly allocated object or `null`. In
addition, every method that either implements or overrides `m` is implicitly
annotated with this same annotation.

[immutable](mcp://flutter/api/meta/immutable) → const [Immutable](mcp://flutter/api/meta/Immutable)
Used to annotate a class `C`. Indicates that `C` and all subtypes of `C` must be immutable.

[kAlwaysCompleteAnimation](mcp://flutter/api/cupertino/kAlwaysCompleteAnimation) → const [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)>
An animation that is always complete.

[kAlwaysDismissedAnimation](mcp://flutter/api/cupertino/kAlwaysDismissedAnimation) → const [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)>
An animation that is always dismissed.

[kDefaultContentInsertionMimeTypes](mcp://flutter/api/cupertino/kDefaultContentInsertionMimeTypes) → const [List](mcp://flutter/api/dart-core/List)<[String](mcp://flutter/api/dart-core/String)>
The default mime types to be used when allowedMimeTypes is not provided.

[kDefaultFontSize](mcp://flutter/api/rendering/kDefaultFontSize) → const [double](mcp://flutter/api/dart-core/double)
The default font size if none is specified.

[kDefaultRouteDirectionalTraversalEdgeBehavior](mcp://flutter/api/cupertino/kDefaultRouteDirectionalTraversalEdgeBehavior) → const [TraversalEdgeBehavior](mcp://flutter/api/widgets/TraversalEdgeBehavior)
The default value of [Navigator.routeDirectionalTraversalEdgeBehavior](mcp://flutter/api/widgets/Navigator/routeDirectionalTraversalEdgeBehavior).

[kDefaultRouteTraversalEdgeBehavior](mcp://flutter/api/cupertino/kDefaultRouteTraversalEdgeBehavior) → const [TraversalEdgeBehavior](mcp://flutter/api/widgets/TraversalEdgeBehavior)
The default value of [Navigator.routeTraversalEdgeBehavior](mcp://flutter/api/widgets/Navigator/routeTraversalEdgeBehavior).

[kTextHeightNone](mcp://flutter/api/dart-ui/kTextHeightNone) → const [double](mcp://flutter/api/dart-core/double)
A `TextStyle.height` value that indicates the text span should take
the height defined by the font, which may not be exactly the height of
`TextStyle.fontSize`.

[mustCallSuper](mcp://flutter/api/meta/mustCallSuper) → const _MustCallSuper
Used to annotate an instance member (method, getter, setter, operator, or
field) `m`. Indicates that every invocation of a member that overrides `m` must also invoke `m`. In addition, every method that overrides `m` is
implicitly annotated with this same annotation.

[optionalTypeArgs](mcp://flutter/api/meta/optionalTypeArgs) → const _OptionalTypeArgs
Used to annotate a class, mixin, extension, function, method, or typedef
declaration `C`. Indicates that any type arguments declared on `C` are to
be treated as optional.

[protected](mcp://flutter/api/meta/protected) → const _Protected
Used to annotate an instance member in a class or mixin which is meant to
be visible only within the declaring library, and to other instance members
of the class or mixin, and their subtypes.

[required](mcp://flutter/api/meta/required) → const [Required](mcp://flutter/api/meta/Required)
Used to annotate a named parameter `p` in a method or function `f`.
Indicates that every invocation of `f` must include an argument
corresponding to `p`, despite the fact that `p` would otherwise be an
optional parameter.

[staticIconProvider](mcp://flutter/api/cupertino/staticIconProvider) → const [Object](mcp://flutter/api/dart-core/Object)
Annotation for classes that only provide static const [IconData](mcp://flutter/api/widgets/IconData) instances.

[visibleForTesting](mcp://flutter/api/meta/visibleForTesting) → const _VisibleForTesting
Used to annotate a declaration that was made public, so that it is more
visible than otherwise necessary, to make code testable.

[widgetFactory](mcp://flutter/api/cupertino/widgetFactory) → const _WidgetFactory
Annotation which marks a function as a widget factory for the purpose of
widget creation tracking.

## Properties

[debugCaptureShaderWarmUpImage](mcp://flutter/api/rendering/debugCaptureShaderWarmUpImage) ↔ [ShaderWarmUpImageCallback](mcp://flutter/api/painting/ShaderWarmUpImageCallback)
Called by [ShaderWarmUp.execute](mcp://flutter/api/painting/ShaderWarmUp/execute) immediately after it creates an [Image](mcp://flutter/api/dart-ui/Image).


[debugCaptureShaderWarmUpPicture](mcp://flutter/api/rendering/debugCaptureShaderWarmUpPicture) ↔ [ShaderWarmUpPictureCallback](mcp://flutter/api/painting/ShaderWarmUpPictureCallback)
Called by [ShaderWarmUp.execute](mcp://flutter/api/painting/ShaderWarmUp/execute) immediately after it creates a [Picture](mcp://flutter/api/dart-ui/Picture).


[debugDisableShadows](mcp://flutter/api/rendering/debugDisableShadows) ↔ [bool](mcp://flutter/api/dart-core/bool)
Whether to replace all shadows with solid color blocks.


[debugEnhanceBuildTimelineArguments](mcp://flutter/api/cupertino/debugEnhanceBuildTimelineArguments) ↔ [bool](mcp://flutter/api/dart-core/bool)
Adds debugging information to [Timeline](mcp://flutter/api/dart-developer/Timeline) events related to [Widget](mcp://flutter/api/widgets/Widget) builds.


[debugFocusChanges](mcp://flutter/api/cupertino/debugFocusChanges) ↔ [bool](mcp://flutter/api/dart-core/bool)
Setting to true will cause extensive logging to occur when focus changes occur.


[debugHighlightDeprecatedWidgets](mcp://flutter/api/cupertino/debugHighlightDeprecatedWidgets) ↔ [bool](mcp://flutter/api/dart-core/bool)
Show banners for deprecated widgets.


[debugImageOverheadAllowance](mcp://flutter/api/rendering/debugImageOverheadAllowance) ↔ [int](mcp://flutter/api/dart-core/int)
The number of bytes an image must use before it triggers inversion when
[debugInvertOversizedImages](mcp://flutter/api/rendering/debugInvertOversizedImages) is true.


[debugInvertOversizedImages](mcp://flutter/api/rendering/debugInvertOversizedImages) ↔ [bool](mcp://flutter/api/dart-core/bool)
If true, the framework will color invert and horizontally flip images that
have been decoded to a size taking at least [debugImageOverheadAllowance](mcp://flutter/api/rendering/debugImageOverheadAllowance) bytes more than necessary.


[debugNetworkImageHttpClientProvider](mcp://flutter/api/rendering/debugNetworkImageHttpClientProvider) ↔ [HttpClientProvider](mcp://flutter/api/painting/HttpClientProvider)?
Provider from which [NetworkImage](mcp://flutter/api/painting/NetworkImage) will get its [HttpClient](mcp://flutter/api/dart-io/HttpClient) in debug builds.


[debugOnPaintImage](mcp://flutter/api/rendering/debugOnPaintImage) ↔ [PaintImageCallback](mcp://flutter/api/painting/PaintImageCallback)?
If not null, called when the framework is about to paint an [Image](mcp://flutter/api/dart-ui/Image) to a
[Canvas](mcp://flutter/api/dart-ui/Canvas) with an [ImageSizeInfo](mcp://flutter/api/painting/ImageSizeInfo) that contains the decoded size of the
image as well as its output size.


[debugOnRebuildDirtyWidget](mcp://flutter/api/cupertino/debugOnRebuildDirtyWidget) ↔ [RebuildDirtyWidgetCallback](mcp://flutter/api/widgets/RebuildDirtyWidgetCallback)?
Callback invoked for every dirty widget built each frame.


[debugPrint](mcp://flutter/api/rendering/debugPrint) ↔ [DebugPrintCallback](mcp://flutter/api/foundation/DebugPrintCallback)
Prints a message to the console, which you can access using the "flutter"
tool's "logs" command ("flutter logs").


[debugPrintBuildScope](mcp://flutter/api/cupertino/debugPrintBuildScope) ↔ [bool](mcp://flutter/api/dart-core/bool)
Log all calls to [BuildOwner.buildScope](mcp://flutter/api/widgets/BuildOwner/buildScope).


[debugPrintGlobalKeyedWidgetLifecycle](mcp://flutter/api/cupertino/debugPrintGlobalKeyedWidgetLifecycle) ↔ [bool](mcp://flutter/api/dart-core/bool)
Log when widgets with global keys are deactivated and log when they are
reactivated (retaken).


[debugPrintRebuildDirtyWidgets](mcp://flutter/api/cupertino/debugPrintRebuildDirtyWidgets) ↔ [bool](mcp://flutter/api/dart-core/bool)
Log the dirty widgets that are built each frame.


[debugPrintScheduleBuildForStacks](mcp://flutter/api/cupertino/debugPrintScheduleBuildForStacks) ↔ [bool](mcp://flutter/api/dart-core/bool)
Log the call stacks that mark widgets as needing to be rebuilt.


[debugProfileBuildsEnabled](mcp://flutter/api/cupertino/debugProfileBuildsEnabled) ↔ [bool](mcp://flutter/api/dart-core/bool)
Adds [Timeline](mcp://flutter/api/dart-developer/Timeline) events for every Widget built.


[debugProfileBuildsEnabledUserWidgets](mcp://flutter/api/cupertino/debugProfileBuildsEnabledUserWidgets) ↔ [bool](mcp://flutter/api/dart-core/bool)
Adds [Timeline](mcp://flutter/api/dart-developer/Timeline) events for every user-created [Widget](mcp://flutter/api/widgets/Widget) built.


[emptyTextSelectionControls](mcp://flutter/api/cupertino/emptyTextSelectionControls) → [TextSelectionControls](mcp://flutter/api/widgets/TextSelectionControls)
Text selection controls that do not show any toolbars or handles.


[imageCache](mcp://flutter/api/rendering/imageCache) → [ImageCache](mcp://flutter/api/painting/ImageCache)
The singleton that implements the Flutter framework's image cache.


[primaryFocus](mcp://flutter/api/cupertino/primaryFocus) → [FocusNode](mcp://flutter/api/widgets/FocusNode)?
Provides convenient access to the current [FocusManager.primaryFocus](mcp://flutter/api/widgets/FocusManager/primaryFocus) from
the [WidgetsBinding](mcp://flutter/api/widgets/WidgetsBinding) instance.


## Functions

[applyBoxFit](mcp://flutter/api/painting/applyBoxFit)([BoxFit](mcp://flutter/api/painting/BoxFit) fit, [Size](mcp://flutter/api/dart-ui/Size) inputSize, [Size](mcp://flutter/api/dart-ui/Size) outputSize) → [FittedSizes](mcp://flutter/api/painting/FittedSizes)
Apply a [BoxFit](mcp://flutter/api/painting/BoxFit) value.

[axisDirectionIsReversed](mcp://flutter/api/painting/axisDirectionIsReversed)([AxisDirection](mcp://flutter/api/painting/AxisDirection) axisDirection) → [bool](mcp://flutter/api/dart-core/bool)
Returns whether traveling along the given axis direction visits coordinates
along that axis in numerically decreasing order.

[axisDirectionToAxis](mcp://flutter/api/painting/axisDirectionToAxis)([AxisDirection](mcp://flutter/api/painting/AxisDirection) axisDirection) → [Axis](mcp://flutter/api/painting/Axis)
Returns the [Axis](mcp://flutter/api/painting/Axis) that contains the given [AxisDirection](mcp://flutter/api/painting/AxisDirection).

[basicLocaleListResolution](mcp://flutter/api/widgets/basicLocaleListResolution)([List](mcp://flutter/api/dart-core/List)<[Locale](mcp://flutter/api/dart-ui/Locale)>? preferredLocales, [Iterable](mcp://flutter/api/dart-core/Iterable)<[Locale](mcp://flutter/api/dart-ui/Locale)> supportedLocales) → [Locale](mcp://flutter/api/dart-ui/Locale)
The default locale resolution algorithm.

[buildTextSpanWithSpellCheckSuggestions](mcp://flutter/api/widgets/buildTextSpanWithSpellCheckSuggestions)([TextEditingValue](mcp://flutter/api/flutter_test/TextEditingValue) value, [bool](mcp://flutter/api/dart-core/bool) composingWithinCurrentTextRange, [TextStyle](mcp://flutter/api/painting/TextStyle)? style, [TextStyle](mcp://flutter/api/painting/TextStyle) misspelledTextStyle, [SpellCheckResults](mcp://flutter/api/services/SpellCheckResults) spellCheckResults) → [TextSpan](mcp://flutter/api/painting/TextSpan)
Builds the [TextSpan](mcp://flutter/api/painting/TextSpan) tree given the current state of the text input and
spell check results.

[childDragAnchorStrategy](mcp://flutter/api/widgets/childDragAnchorStrategy)([Draggable](mcp://flutter/api/widgets/Draggable)<[Object](mcp://flutter/api/dart-core/Object)> draggable, [BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Offset](mcp://flutter/api/dart-ui/Offset) position) → [Offset](mcp://flutter/api/dart-ui/Offset)
Display the feedback anchored at the position of the original child.

[combineKeyEventResults](mcp://flutter/api/widgets/combineKeyEventResults)([Iterable](mcp://flutter/api/dart-core/Iterable)<[KeyEventResult](mcp://flutter/api/widgets/KeyEventResult)> results) → [KeyEventResult](mcp://flutter/api/widgets/KeyEventResult)
Combine the results returned by multiple [FocusOnKeyCallback](mcp://flutter/api/widgets/FocusOnKeyCallback) s or
[FocusOnKeyEventCallback](mcp://flutter/api/widgets/FocusOnKeyEventCallback) s.

[combineSemanticsInfo](mcp://flutter/api/painting/combineSemanticsInfo)([List](mcp://flutter/api/dart-core/List)<[InlineSpanSemanticsInformation](mcp://flutter/api/painting/InlineSpanSemanticsInformation)> infoList) → [List](mcp://flutter/api/dart-core/List)<[InlineSpanSemanticsInformation](mcp://flutter/api/painting/InlineSpanSemanticsInformation)>
Combines _semanticsInfo entries where permissible.

[createLocalImageConfiguration](mcp://flutter/api/widgets/createLocalImageConfiguration)([BuildContext](mcp://flutter/api/widgets/BuildContext) context, {[Size](mcp://flutter/api/dart-ui/Size)? size}) → [ImageConfiguration](mcp://flutter/api/painting/ImageConfiguration)
Creates an [ImageConfiguration](mcp://flutter/api/painting/ImageConfiguration) based on the given [BuildContext](mcp://flutter/api/widgets/BuildContext) (and
optionally size).

[debugAssertAllPaintingVarsUnset](mcp://flutter/api/painting/debugAssertAllPaintingVarsUnset)([String](mcp://flutter/api/dart-core/String) reason, {[bool](mcp://flutter/api/dart-core/bool) debugDisableShadowsOverride = false}) → [bool](mcp://flutter/api/dart-core/bool)
Returns true if none of the painting library debug variables have been changed.

[debugAssertAllWidgetVarsUnset](mcp://flutter/api/widgets/debugAssertAllWidgetVarsUnset)([String](mcp://flutter/api/dart-core/String) reason) → [bool](mcp://flutter/api/dart-core/bool)
Returns true if none of the widget library debug variables have been changed.

[debugCheckCanResolveTextDirection](mcp://flutter/api/painting/debugCheckCanResolveTextDirection)([TextDirection](mcp://flutter/api/dart-ui/TextDirection)? direction, [String](mcp://flutter/api/dart-core/String) target) → [bool](mcp://flutter/api/dart-core/bool)
Asserts that a given [TextDirection](mcp://flutter/api/dart-ui/TextDirection) is not null.

[debugCheckHasDirectionality](mcp://flutter/api/widgets/debugCheckHasDirectionality)([BuildContext](mcp://flutter/api/widgets/BuildContext) context, {[String](mcp://flutter/api/dart-core/String)? why, [String](mcp://flutter/api/dart-core/String)? hint, [String](mcp://flutter/api/dart-core/String)? alternative}) → [bool](mcp://flutter/api/dart-core/bool)
Asserts that the given context has a [Directionality](mcp://flutter/api/widgets/Directionality) ancestor.

[debugCheckHasMediaQuery](mcp://flutter/api/widgets/debugCheckHasMediaQuery)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [bool](mcp://flutter/api/dart-core/bool)
Asserts that the given context has a [MediaQuery](mcp://flutter/api/widgets/MediaQuery) ancestor.

[debugCheckHasOverlay](mcp://flutter/api/widgets/debugCheckHasOverlay)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [bool](mcp://flutter/api/dart-core/bool)
Asserts that the given context has an [Overlay](mcp://flutter/api/widgets/Overlay) ancestor.

[debugCheckHasTable](mcp://flutter/api/widgets/debugCheckHasTable)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [bool](mcp://flutter/api/dart-core/bool)
Asserts that the given context has a [Table](mcp://flutter/api/widgets/Table) ancestor.

[debugCheckHasWidgetsLocalizations](mcp://flutter/api/widgets/debugCheckHasWidgetsLocalizations)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [bool](mcp://flutter/api/dart-core/bool)
Asserts that the given context has a [Localizations](mcp://flutter/api/widgets/Localizations) ancestor that contains
a [WidgetsLocalizations](mcp://flutter/api/widgets/WidgetsLocalizations) delegate.

[debugChildrenHaveDuplicateKeys](mcp://flutter/api/widgets/debugChildrenHaveDuplicateKeys)([Widget](mcp://flutter/api/widgets/Widget) parent, [Iterable](mcp://flutter/api/dart-core/Iterable)<[Widget](mcp://flutter/api/widgets/Widget)> children, {[String](mcp://flutter/api/dart-core/String)? message}) → [bool](mcp://flutter/api/dart-core/bool)
Asserts if the given child list contains any duplicate non-null keys.

[debugDescribeFocusTree](mcp://flutter/api/widgets/debugDescribeFocusTree)() → [String](mcp://flutter/api/dart-core/String)
Returns a text representation of the current focus tree, along with the
current attributes on each node.

[debugDescribeTransform](mcp://flutter/api/painting/debugDescribeTransform)([Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4)? transform) → [List](mcp://flutter/api/dart-core/List)<[String](mcp://flutter/api/dart-core/String)>
Returns a list of strings representing the given transform in a format
useful for [TransformProperty](mcp://flutter/api/painting/TransformProperty).

[debugDumpApp](mcp://flutter/api/widgets/debugDumpApp)() → void
Print a string representation of the currently running app.

[debugDumpFocusTree](mcp://flutter/api/widgets/debugDumpFocusTree)() → void
Prints a text representation of the current focus tree, along with the
current attributes on each node.

[debugDumpLayerTree](mcp://flutter/api/rendering/debugDumpLayerTree)() → void
Prints a textual representation of the layer trees.

[debugDumpRenderTree](mcp://flutter/api/rendering/debugDumpRenderTree)() → void
Prints a textual representation of the render trees.

[debugFlushLastFrameImageSizeInfo](mcp://flutter/api/painting/debugFlushLastFrameImageSizeInfo)() → void
Flushes inter-frame tracking of image size information from [paintImage](mcp://flutter/api/painting/paintImage).

[debugIsLocalCreationLocation](mcp://flutter/api/widgets/debugIsLocalCreationLocation)([Object](mcp://flutter/api/dart-core/Object) object) → [bool](mcp://flutter/api/dart-core/bool)
Returns if an object is user created.

[debugIsWidgetLocalCreation](mcp://flutter/api/widgets/debugIsWidgetLocalCreation)([Widget](mcp://flutter/api/widgets/Widget) widget) → [bool](mcp://flutter/api/dart-core/bool)
Returns true if a [Widget](mcp://flutter/api/widgets/Widget) is user created.

[debugItemsHaveDuplicateKeys](mcp://flutter/api/widgets/debugItemsHaveDuplicateKeys)([Iterable](mcp://flutter/api/dart-core/Iterable)<[Widget](mcp://flutter/api/widgets/Widget)> items) → [bool](mcp://flutter/api/dart-core/bool)
Asserts if the given list of items contains any duplicate non-null keys.

[debugPrintStack](mcp://flutter/api/foundation/debugPrintStack)({[StackTrace](mcp://flutter/api/dart-core/StackTrace)? stackTrace, [String](mcp://flutter/api/dart-core/String)? label, [int](mcp://flutter/api/dart-core/int)? maxFrames}) → void
Dump the stack to the console using [debugPrint](mcp://flutter/api/rendering/debugPrint) and
[FlutterError.defaultStackFilter](mcp://flutter/api/foundation/FlutterError/defaultStackFilter).

[debugTransformDebugCreator](mcp://flutter/api/widgets/debugTransformDebugCreator)([Iterable](mcp://flutter/api/dart-core/Iterable)<[DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)> properties) → [Iterable](mcp://flutter/api/dart-core/Iterable)<[DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)>
Transformer to parse and gather information about [DiagnosticsDebugCreator](mcp://flutter/api/rendering/DiagnosticsDebugCreator).

[debugWidgetBuilderValue](mcp://flutter/api/widgets/debugWidgetBuilderValue)([Widget](mcp://flutter/api/widgets/Widget) widget, [Widget](mcp://flutter/api/widgets/Widget)? built) → void
Asserts that the `built` widget is not null.

[decodeImageFromList](mcp://flutter/api/painting/decodeImageFromList)([Uint8List](mcp://flutter/api/dart-typed_data/Uint8List) bytes) → [Future](mcp://flutter/api/dart-async/Future)<[Image](mcp://flutter/api/dart-ui/Image)>
Creates an image from a list of bytes.

[defaultScrollNotificationPredicate](mcp://flutter/api/widgets/defaultScrollNotificationPredicate)([ScrollNotification](mcp://flutter/api/widgets/ScrollNotification) notification) → [bool](mcp://flutter/api/dart-core/bool)
A [ScrollNotificationPredicate](mcp://flutter/api/widgets/ScrollNotificationPredicate) that checks whether
`notification.depth == 0`, which means that the notification did not bubble
through any intervening scrolling widgets.

[flipAxis](mcp://flutter/api/painting/flipAxis)([Axis](mcp://flutter/api/painting/Axis) direction) → [Axis](mcp://flutter/api/painting/Axis)
Returns the opposite of the given [Axis](mcp://flutter/api/painting/Axis).

[flipAxisDirection](mcp://flutter/api/painting/flipAxisDirection)([AxisDirection](mcp://flutter/api/painting/AxisDirection) axisDirection) → [AxisDirection](mcp://flutter/api/painting/AxisDirection)
Returns the opposite of the given [AxisDirection](mcp://flutter/api/painting/AxisDirection).

[getAxisDirectionFromAxisReverseAndDirectionality](mcp://flutter/api/widgets/getAxisDirectionFromAxisReverseAndDirectionality)([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Axis](mcp://flutter/api/painting/Axis) axis, [bool](mcp://flutter/api/dart-core/bool) reverse) → [AxisDirection](mcp://flutter/api/painting/AxisDirection)
Returns the [AxisDirection](mcp://flutter/api/painting/AxisDirection) in the given [Axis](mcp://flutter/api/painting/Axis) in the current
[Directionality](mcp://flutter/api/widgets/Directionality) (or the reverse if `reverse` is true).

[intentForMacOSSelector](mcp://flutter/api/widgets/intentForMacOSSelector)([String](mcp://flutter/api/dart-core/String) selectorName) → [Intent](mcp://flutter/api/widgets/Intent)?
Maps the selector from NSStandardKeyBindingResponding to the Intent if the
selector is recognized.

[lerpFontVariations](mcp://flutter/api/painting/lerpFontVariations)([List](mcp://flutter/api/dart-core/List)<[FontVariation](mcp://flutter/api/dart-ui/FontVariation)>? a, [List](mcp://flutter/api/dart-core/List)<[FontVariation](mcp://flutter/api/dart-ui/FontVariation)>? b, [double](mcp://flutter/api/dart-core/double) t) → [List](mcp://flutter/api/dart-core/List)<[FontVariation](mcp://flutter/api/dart-ui/FontVariation)>?
Interpolate between two lists of [FontVariation](mcp://flutter/api/dart-ui/FontVariation) objects.

[paintBorder](mcp://flutter/api/painting/paintBorder)([Canvas](mcp://flutter/api/dart-ui/Canvas) canvas, [Rect](mcp://flutter/api/dart-ui/Rect) rect, {[BorderSide](mcp://flutter/api/painting/BorderSide) top = BorderSide.none, [BorderSide](mcp://flutter/api/painting/BorderSide) right = BorderSide.none, [BorderSide](mcp://flutter/api/painting/BorderSide) bottom = BorderSide.none, [BorderSide](mcp://flutter/api/painting/BorderSide) left = BorderSide.none}) → void
Paints a border around the given rectangle on the canvas.

[paintImage](mcp://flutter/api/painting/paintImage)({required [Canvas](mcp://flutter/api/dart-ui/Canvas) canvas, required [Rect](mcp://flutter/api/dart-ui/Rect) rect, required [Image](mcp://flutter/api/dart-ui/Image) image, [String](mcp://flutter/api/dart-core/String)? debugImageLabel, [double](mcp://flutter/api/dart-core/double) scale = 1.0, [double](mcp://flutter/api/dart-core/double) opacity = 1.0, [ColorFilter](mcp://flutter/api/dart-ui/ColorFilter)? colorFilter, [BoxFit](mcp://flutter/api/painting/BoxFit)? fit, [Alignment](mcp://flutter/api/painting/Alignment) alignment = Alignment.center, [Rect](mcp://flutter/api/dart-ui/Rect)? centerSlice, [ImageRepeat](mcp://flutter/api/painting/ImageRepeat) repeat = ImageRepeat.noRepeat, [bool](mcp://flutter/api/dart-core/bool) flipHorizontally = false, [bool](mcp://flutter/api/dart-core/bool) invertColors = false, [FilterQuality](mcp://flutter/api/dart-ui/FilterQuality) filterQuality = FilterQuality.medium, [bool](mcp://flutter/api/dart-core/bool) isAntiAlias = false, [BlendMode](mcp://flutter/api/dart-ui/BlendMode) blendMode = BlendMode.srcOver}) → void
Paints an image into the given rectangle on the canvas.

[paintZigZag](mcp://flutter/api/painting/paintZigZag)([Canvas](mcp://flutter/api/dart-ui/Canvas) canvas, [Paint](mcp://flutter/api/dart-ui/Paint) paint, [Offset](mcp://flutter/api/dart-ui/Offset) start, [Offset](mcp://flutter/api/dart-ui/Offset) end, [int](mcp://flutter/api/dart-core/int) zigs, [double](mcp://flutter/api/dart-core/double) width) → void
Draw a line between two points, which cuts diagonally back and forth across
the line that connects the two points.

[pointerDragAnchorStrategy](mcp://flutter/api/widgets/pointerDragAnchorStrategy)([Draggable](mcp://flutter/api/widgets/Draggable)<[Object](mcp://flutter/api/dart-core/Object)> draggable, [BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Offset](mcp://flutter/api/dart-ui/Offset) position) → [Offset](mcp://flutter/api/dart-ui/Offset)
Display the feedback anchored at the position of the touch that started
the drag.

[positionDependentBox](mcp://flutter/api/painting/positionDependentBox)({required [Size](mcp://flutter/api/dart-ui/Size) size, required [Size](mcp://flutter/api/dart-ui/Size) childSize, required [Offset](mcp://flutter/api/dart-ui/Offset) target, required [bool](mcp://flutter/api/dart-core/bool) preferBelow, [double](mcp://flutter/api/dart-core/double) verticalOffset = 0.0, [double](mcp://flutter/api/dart-core/double) margin = 10.0}) → [Offset](mcp://flutter/api/dart-ui/Offset)
Position a child box within a container box, either above or below a target
point.

[precacheImage](mcp://flutter/api/widgets/precacheImage)([ImageProvider](mcp://flutter/api/painting/ImageProvider)<[Object](mcp://flutter/api/dart-core/Object)> provider, [BuildContext](mcp://flutter/api/widgets/BuildContext) context, {[Size](mcp://flutter/api/dart-ui/Size)? size, [ImageErrorListener](mcp://flutter/api/painting/ImageErrorListener)? onError}) → [Future](mcp://flutter/api/dart-async/Future)<void>
Prefetches an image into the image cache.

[runApp](mcp://flutter/api/widgets/runApp)([Widget](mcp://flutter/api/widgets/Widget) app) → void
Inflate the given widget and attach it to the view.

[runWidget](mcp://flutter/api/widgets/runWidget)([Widget](mcp://flutter/api/widgets/Widget) app) → void
Inflate the given widget and bootstrap the widget tree.

[showGeneralDialog](mcp://flutter/api/widgets/showGeneralDialog)<T extends [Object](mcp://flutter/api/dart-core/Object)?>({required [BuildContext](mcp://flutter/api/widgets/BuildContext) context, required [RoutePageBuilder](mcp://flutter/api/widgets/RoutePageBuilder) pageBuilder, [bool](mcp://flutter/api/dart-core/bool) barrierDismissible = false, [String](mcp://flutter/api/dart-core/String)? barrierLabel, [Color](mcp://flutter/api/dart-ui/Color) barrierColor = const Color(0x80000000), [Duration](mcp://flutter/api/dart-core/Duration) transitionDuration = const Duration(milliseconds: 200), [RouteTransitionsBuilder](mcp://flutter/api/widgets/RouteTransitionsBuilder)? transitionBuilder, [bool](mcp://flutter/api/dart-core/bool) useRootNavigator = true, [bool](mcp://flutter/api/dart-core/bool) fullscreenDialog = false, [RouteSettings](mcp://flutter/api/widgets/RouteSettings)? routeSettings, [Offset](mcp://flutter/api/dart-ui/Offset)? anchorPoint, [bool](mcp://flutter/api/dart-core/bool)? requestFocus}) → [Future](mcp://flutter/api/dart-async/Future)<T?>
Displays a dialog above the current contents of the app.

[textDirectionToAxisDirection](mcp://flutter/api/painting/textDirectionToAxisDirection)([TextDirection](mcp://flutter/api/dart-ui/TextDirection) textDirection) → [AxisDirection](mcp://flutter/api/painting/AxisDirection)
Returns the [AxisDirection](mcp://flutter/api/painting/AxisDirection) in which reading occurs in the given [TextDirection](mcp://flutter/api/dart-ui/TextDirection).

## Typedefs

[ActionListenerCallback](mcp://flutter/api/widgets/ActionListenerCallback)= void Function([Action](mcp://flutter/api/widgets/Action)<[Intent](mcp://flutter/api/widgets/Intent)> action)
The kind of callback that an [Action](mcp://flutter/api/widgets/Action) uses to notify of changes to the
action's state.

[AnimatableCallback](mcp://flutter/api/animation/AnimatableCallback)<T>= T Function([double](mcp://flutter/api/dart-core/double) value)
A typedef used by [Animatable.fromCallback](mcp://flutter/api/animation/Animatable/Animatable.fromCallback) to create an [Animatable](mcp://flutter/api/animation/Animatable) from a callback.

[AnimatedCrossFadeBuilder](mcp://flutter/api/widgets/AnimatedCrossFadeBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([Widget](mcp://flutter/api/widgets/Widget) topChild, [Key](mcp://flutter/api/foundation/Key) topChildKey, [Widget](mcp://flutter/api/widgets/Widget) bottomChild, [Key](mcp://flutter/api/foundation/Key) bottomChildKey)
Signature for the [AnimatedCrossFade.layoutBuilder](mcp://flutter/api/widgets/AnimatedCrossFade/layoutBuilder) callback.

[AnimatedItemBuilder](mcp://flutter/api/widgets/AnimatedItemBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [int](mcp://flutter/api/dart-core/int) index, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation)
Signature for the builder callback used by [AnimatedList](mcp://flutter/api/widgets/AnimatedList), [AnimatedList.separated](mcp://flutter/api/widgets/AnimatedList/AnimatedList.separated) & [AnimatedGrid](mcp://flutter/api/widgets/AnimatedGrid) to build their animated children.

[AnimatedRemovedItemBuilder](mcp://flutter/api/widgets/AnimatedRemovedItemBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation)
Signature for the builder callback used in `AnimatedListState.removeItem` and
`AnimatedGridState.removeItem` to animate their children after they have
been removed.

[AnimatedSwitcherLayoutBuilder](mcp://flutter/api/widgets/AnimatedSwitcherLayoutBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([Widget](mcp://flutter/api/widgets/Widget)? currentChild, [List](mcp://flutter/api/dart-core/List)<[Widget](mcp://flutter/api/widgets/Widget)> previousChildren)
Signature for builders used to generate custom layouts for
[AnimatedSwitcher](mcp://flutter/api/widgets/AnimatedSwitcher).

[AnimatedSwitcherTransitionBuilder](mcp://flutter/api/widgets/AnimatedSwitcherTransitionBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([Widget](mcp://flutter/api/widgets/Widget) child, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation)
Signature for builders used to generate custom transitions for
[AnimatedSwitcher](mcp://flutter/api/widgets/AnimatedSwitcher).

[AnimatedTransitionBuilder](mcp://flutter/api/widgets/AnimatedTransitionBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation, [Widget](mcp://flutter/api/widgets/Widget)? child)
Builder callback used by [DualTransitionBuilder](mcp://flutter/api/widgets/DualTransitionBuilder).

[AnimationStatusListener](mcp://flutter/api/animation/AnimationStatusListener)= void Function([AnimationStatus](mcp://flutter/api/animation/AnimationStatus) status)
Signature for listeners attached using [Animation.addStatusListener](mcp://flutter/api/animation/Animation/addStatusListener).

[AppExitRequestCallback](mcp://flutter/api/widgets/AppExitRequestCallback)= [Future](mcp://flutter/api/dart-async/Future)<[AppExitResponse](mcp://flutter/api/dart-ui/AppExitResponse)> Function()
A callback type that is used by [AppLifecycleListener.onExitRequested](mcp://flutter/api/widgets/AppLifecycleListener/onExitRequested) to
ask the application if it wants to cancel application termination or not.

[AppPrivateCommandCallback](mcp://flutter/api/widgets/AppPrivateCommandCallback)= void Function([String](mcp://flutter/api/dart-core/String) action, [Map](mcp://flutter/api/dart-core/Map)<[String](mcp://flutter/api/dart-core/String), dynamic> data)
Signature for the callback that reports the app private command results.

[AsyncWidgetBuilder](mcp://flutter/api/widgets/AsyncWidgetBuilder)<T>= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [AsyncSnapshot](mcp://flutter/api/widgets/AsyncSnapshot)<T> snapshot)
Signature for strategies that build widgets based on asynchronous
interaction.

[AutocompleteFieldViewBuilder](mcp://flutter/api/widgets/AutocompleteFieldViewBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [TextEditingController](mcp://flutter/api/widgets/TextEditingController) textEditingController, [FocusNode](mcp://flutter/api/widgets/FocusNode) focusNode, [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) onFieldSubmitted)
The type of the Autocomplete callback which returns the widget that
contains the input [TextField](mcp://flutter/api/material/TextField) or [TextFormField](mcp://flutter/api/material/TextFormField).

[AutocompleteOnSelected](mcp://flutter/api/widgets/AutocompleteOnSelected)<T extends [Object](mcp://flutter/api/dart-core/Object)>= void Function(T option)
The type of the callback used by the [RawAutocomplete](mcp://flutter/api/widgets/RawAutocomplete) widget to indicate
that the user has selected an option.

[AutocompleteOptionsBuilder](mcp://flutter/api/widgets/AutocompleteOptionsBuilder)<T extends [Object](mcp://flutter/api/dart-core/Object)>= [FutureOr](mcp://flutter/api/dart-async/FutureOr)<[Iterable](mcp://flutter/api/dart-core/Iterable)<T>> Function([TextEditingValue](mcp://flutter/api/flutter_test/TextEditingValue) textEditingValue)
The type of the [RawAutocomplete](mcp://flutter/api/widgets/RawAutocomplete) callback which computes the list of
optional completions for the widget's field, based on the text the user has
entered so far.

[AutocompleteOptionsViewBuilder](mcp://flutter/api/widgets/AutocompleteOptionsViewBuilder)<T extends [Object](mcp://flutter/api/dart-core/Object)>= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [AutocompleteOnSelected](mcp://flutter/api/widgets/AutocompleteOnSelected)<T> onSelected, [Iterable](mcp://flutter/api/dart-core/Iterable)<T> options)
The type of the [RawAutocomplete](mcp://flutter/api/widgets/RawAutocomplete) callback which returns a [Widget](mcp://flutter/api/widgets/Widget) that
displays the specified `options` and calls `onSelected` if the user
selects an option.

[AutocompleteOptionToString](mcp://flutter/api/widgets/AutocompleteOptionToString)<T extends [Object](mcp://flutter/api/dart-core/Object)>= [String](mcp://flutter/api/dart-core/String) Function(T option)
The type of the [RawAutocomplete](mcp://flutter/api/widgets/RawAutocomplete) callback that converts an option value to
a string which can be displayed in the widget's options menu.

[BoxConstraintsTransform](mcp://flutter/api/rendering/BoxConstraintsTransform)= [BoxConstraints](mcp://flutter/api/rendering/BoxConstraints) Function([BoxConstraints](mcp://flutter/api/rendering/BoxConstraints) constraints)
Signature for a function that transforms a [BoxConstraints](mcp://flutter/api/rendering/BoxConstraints) to another
[BoxConstraints](mcp://flutter/api/rendering/BoxConstraints).

[ChildIndexGetter](mcp://flutter/api/widgets/ChildIndexGetter)= [int](mcp://flutter/api/dart-core/int)? Function([Key](mcp://flutter/api/foundation/Key) key)
Called to find the new index of a child based on its `key` in case of
reordering.

[ConditionalElementVisitor](mcp://flutter/api/widgets/ConditionalElementVisitor)= [bool](mcp://flutter/api/dart-core/bool) Function([Element](mcp://flutter/api/widgets/Element) element)
Signature for the callback to [BuildContext.visitAncestorElements](mcp://flutter/api/widgets/BuildContext/visitAncestorElements).

[ConfirmDismissCallback](mcp://flutter/api/widgets/ConfirmDismissCallback)= [Future](mcp://flutter/api/dart-async/Future)<[bool](mcp://flutter/api/dart-core/bool)?> Function([DismissDirection](mcp://flutter/api/widgets/DismissDirection) direction)
Signature used by [Dismissible](mcp://flutter/api/widgets/Dismissible) to give the application an opportunity to
confirm or veto a dismiss gesture.

[CreatePlatformViewCallback](mcp://flutter/api/widgets/CreatePlatformViewCallback)= [PlatformViewController](mcp://flutter/api/services/PlatformViewController) Function([PlatformViewCreationParams](mcp://flutter/api/widgets/PlatformViewCreationParams) params)
Constructs a [PlatformViewController](mcp://flutter/api/services/PlatformViewController).

[CreateRectTween](mcp://flutter/api/widgets/CreateRectTween)= [Tween](mcp://flutter/api/animation/Tween)<[Rect](mcp://flutter/api/dart-ui/Rect)?> Function([Rect](mcp://flutter/api/dart-ui/Rect)? begin, [Rect](mcp://flutter/api/dart-ui/Rect)? end)
Signature for a function that takes two [Rect](mcp://flutter/api/dart-ui/Rect) instances and returns a
[RectTween](mcp://flutter/api/animation/RectTween) that transitions between them.

[DecoderBufferCallback](mcp://flutter/api/painting/DecoderBufferCallback)= [Future](mcp://flutter/api/dart-async/Future)<[Codec](mcp://flutter/api/dart-ui/Codec)> Function([ImmutableBuffer](mcp://flutter/api/dart-ui/ImmutableBuffer) buffer, {[bool](mcp://flutter/api/dart-core/bool) allowUpscaling, [int](mcp://flutter/api/dart-core/int)? cacheHeight, [int](mcp://flutter/api/dart-core/int)? cacheWidth})
Performs the decode process for use in [ImageProvider.loadBuffer](mcp://flutter/api/painting/ImageProvider/loadBuffer).

[DelegatedTransitionBuilder](mcp://flutter/api/widgets/DelegatedTransitionBuilder)= [Widget](mcp://flutter/api/widgets/Widget)? Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> secondaryAnimation, [bool](mcp://flutter/api/dart-core/bool) allowSnapshotting, [Widget](mcp://flutter/api/widgets/Widget)? child)
Signature for a builder used to control a page's exit transition.

[DidRemovePageCallback](mcp://flutter/api/widgets/DidRemovePageCallback)= void Function([Page](mcp://flutter/api/widgets/Page)<[Object](mcp://flutter/api/dart-core/Object)?> page)
Signature for the [Navigator.onDidRemovePage](mcp://flutter/api/widgets/Navigator/onDidRemovePage) callback.

[DismissDirectionCallback](mcp://flutter/api/widgets/DismissDirectionCallback)= void Function([DismissDirection](mcp://flutter/api/widgets/DismissDirection) direction)
Signature used by [Dismissible](mcp://flutter/api/widgets/Dismissible) to indicate that it has been dismissed in
the given `direction`.

[DismissUpdateCallback](mcp://flutter/api/widgets/DismissUpdateCallback)= void Function([DismissUpdateDetails](mcp://flutter/api/widgets/DismissUpdateDetails) details)
Signature used by [Dismissible](mcp://flutter/api/widgets/Dismissible) to indicate that the dismissible has been dragged.

[DragAnchorStrategy](mcp://flutter/api/widgets/DragAnchorStrategy)= [Offset](mcp://flutter/api/dart-ui/Offset) Function([Draggable](mcp://flutter/api/widgets/Draggable)<[Object](mcp://flutter/api/dart-core/Object)> draggable, [BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Offset](mcp://flutter/api/dart-ui/Offset) position)
Signature for the strategy that determines the drag start point of a [Draggable](mcp://flutter/api/widgets/Draggable).

[DragEndCallback](mcp://flutter/api/widgets/DragEndCallback)= void Function([DraggableDetails](mcp://flutter/api/widgets/DraggableDetails) details)
Signature for when the draggable is dropped.

[DraggableCanceledCallback](mcp://flutter/api/widgets/DraggableCanceledCallback)= void Function([Velocity](mcp://flutter/api/gestures/Velocity) velocity, [Offset](mcp://flutter/api/dart-ui/Offset) offset)
Signature for when a [Draggable](mcp://flutter/api/widgets/Draggable) is dropped without being accepted by a [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DragTargetAccept](mcp://flutter/api/widgets/DragTargetAccept)<T>= void Function(T data)
Signature for causing a [DragTarget](mcp://flutter/api/widgets/DragTarget) to accept the given data.

[DragTargetAcceptWithDetails](mcp://flutter/api/widgets/DragTargetAcceptWithDetails)<T>= void Function([DragTargetDetails](mcp://flutter/api/widgets/DragTargetDetails)<T> details)
Signature for determining information about the acceptance by a [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DragTargetBuilder](mcp://flutter/api/widgets/DragTargetBuilder)<T>= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [List](mcp://flutter/api/dart-core/List)<T?> candidateData, [List](mcp://flutter/api/dart-core/List) rejectedData)
Signature for building children of a [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DragTargetLeave](mcp://flutter/api/widgets/DragTargetLeave)<T>= void Function(T? data)
Signature for when a [Draggable](mcp://flutter/api/widgets/Draggable) leaves a [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DragTargetMove](mcp://flutter/api/widgets/DragTargetMove)<T>= void Function([DragTargetDetails](mcp://flutter/api/widgets/DragTargetDetails)<T> details)
Signature for when a [Draggable](mcp://flutter/api/widgets/Draggable) moves within a [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DragTargetWillAccept](mcp://flutter/api/widgets/DragTargetWillAccept)<T>= [bool](mcp://flutter/api/dart-core/bool) Function(T? data)
Signature for determining whether the given data will be accepted by a [DragTarget](mcp://flutter/api/widgets/DragTarget).

[DragTargetWillAcceptWithDetails](mcp://flutter/api/widgets/DragTargetWillAcceptWithDetails)<T>= [bool](mcp://flutter/api/dart-core/bool) Function([DragTargetDetails](mcp://flutter/api/widgets/DragTargetDetails)<T> details)
Signature for determining whether the given data will be accepted by a [DragTarget](mcp://flutter/api/widgets/DragTarget),
based on provided information.

[DragUpdateCallback](mcp://flutter/api/widgets/DragUpdateCallback)= void Function([DragUpdateDetails](mcp://flutter/api/gestures/DragUpdateDetails) details)
Signature for when a [Draggable](mcp://flutter/api/widgets/Draggable) is dragged across the screen.

[EditableTextContextMenuBuilder](mcp://flutter/api/widgets/EditableTextContextMenuBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [EditableTextState](mcp://flutter/api/widgets/EditableTextState) editableTextState)
Signature for a widget builder that builds a context menu for the given
[EditableTextState](mcp://flutter/api/widgets/EditableTextState).

[ElementCreatedCallback](mcp://flutter/api/widgets/ElementCreatedCallback)= void Function([Object](mcp://flutter/api/dart-core/Object) element)
The signature of the function that gets called when the [HtmlElementView](mcp://flutter/api/widgets/HtmlElementView) DOM element is created.

[ElementVisitor](mcp://flutter/api/widgets/ElementVisitor)= void Function([Element](mcp://flutter/api/widgets/Element) element)
Signature for the callback to [BuildContext.visitChildElements](mcp://flutter/api/widgets/BuildContext/visitChildElements).

[ErrorWidgetBuilder](mcp://flutter/api/widgets/ErrorWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([FlutterErrorDetails](mcp://flutter/api/foundation/FlutterErrorDetails) details)
Signature for the constructor that is called when an error occurs while
building a widget.

[ExitWidgetSelectionButtonBuilder](mcp://flutter/api/widgets/ExitWidgetSelectionButtonBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, {required [GlobalKey](mcp://flutter/api/widgets/GlobalKey)<[State](mcp://flutter/api/widgets/State)<[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)>> key, required [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) onPressed, required [String](mcp://flutter/api/dart-core/String) semanticsLabel})
Signature for the builder callback used by
[WidgetInspector.exitWidgetSelectionButtonBuilder](mcp://flutter/api/widgets/WidgetInspector/exitWidgetSelectionButtonBuilder).

[ExpansibleBuilder](mcp://flutter/api/widgets/ExpansibleBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Widget](mcp://flutter/api/widgets/Widget) header, [Widget](mcp://flutter/api/widgets/Widget) body, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation)
The type of the callback that uses the header and body of an [Expansible](mcp://flutter/api/widgets/Expansible) widget to build the widget.

[ExpansibleComponentBuilder](mcp://flutter/api/widgets/ExpansibleComponentBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation)
The type of the callback that returns the header or body of an [Expansible](mcp://flutter/api/widgets/Expansible).

[FocusOnKeyCallback](mcp://flutter/api/widgets/FocusOnKeyCallback)= [KeyEventResult](mcp://flutter/api/widgets/KeyEventResult) Function([FocusNode](mcp://flutter/api/widgets/FocusNode) node, [RawKeyEvent](mcp://flutter/api/services/RawKeyEvent) event)
Signature of a callback used by [Focus.onKey](mcp://flutter/api/widgets/Focus/onKey) and [FocusScope.onKey](mcp://flutter/api/widgets/Focus/onKey) to receive key events.

[FocusOnKeyEventCallback](mcp://flutter/api/widgets/FocusOnKeyEventCallback)= [KeyEventResult](mcp://flutter/api/widgets/KeyEventResult) Function([FocusNode](mcp://flutter/api/widgets/FocusNode) node, [KeyEvent](mcp://flutter/api/services/KeyEvent) event)
Signature of a callback used by [Focus.onKeyEvent](mcp://flutter/api/widgets/Focus/onKeyEvent) and [FocusScope.onKeyEvent](mcp://flutter/api/widgets/Focus/onKeyEvent) to receive key events.

[FormFieldBuilder](mcp://flutter/api/widgets/FormFieldBuilder)<T>= [Widget](mcp://flutter/api/widgets/Widget) Function([FormFieldState](mcp://flutter/api/widgets/FormFieldState)<T> field)
Signature for building the widget representing the form field.

[FormFieldErrorBuilder](mcp://flutter/api/widgets/FormFieldErrorBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [String](mcp://flutter/api/dart-core/String) errorText)
Signature for a callback that builds an error widget.

[FormFieldSetter](mcp://flutter/api/widgets/FormFieldSetter)<T>= void Function(T? newValue)
Signature for being notified when a form field changes value.

[FormFieldValidator](mcp://flutter/api/widgets/FormFieldValidator)<T>= [String](mcp://flutter/api/dart-core/String)? Function(T? value)
Signature for validating a form field.

[GenerateAppTitle](mcp://flutter/api/widgets/GenerateAppTitle)= [String](mcp://flutter/api/dart-core/String) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context)
The signature of [WidgetsApp.onGenerateTitle](mcp://flutter/api/widgets/WidgetsApp/onGenerateTitle).

[GestureDragCancelCallback](mcp://flutter/api/gestures/GestureDragCancelCallback)= void Function()
Signature for when the pointer that previously triggered a
[GestureDragDownCallback](mcp://flutter/api/gestures/GestureDragDownCallback) did not complete.

[GestureDragDownCallback](mcp://flutter/api/gestures/GestureDragDownCallback)= void Function([DragDownDetails](mcp://flutter/api/gestures/DragDownDetails) details)
Signature for when a pointer has contacted the screen and might begin to
move.

[GestureDragEndCallback](mcp://flutter/api/gestures/GestureDragEndCallback)= void Function([DragEndDetails](mcp://flutter/api/gestures/DragEndDetails) details)
Signature for when a pointer that was previously in contact with the screen
and moving is no longer in contact with the screen.

[GestureDragStartCallback](mcp://flutter/api/gestures/GestureDragStartCallback)= void Function([DragStartDetails](mcp://flutter/api/gestures/DragStartDetails) details)
Signature for when a pointer has contacted the screen and has begun to move.

[GestureDragUpdateCallback](mcp://flutter/api/gestures/GestureDragUpdateCallback)= void Function([DragUpdateDetails](mcp://flutter/api/gestures/DragUpdateDetails) details)
Signature for when a pointer that is in contact with the screen and moving
has moved again.

[GestureForcePressEndCallback](mcp://flutter/api/gestures/GestureForcePressEndCallback)= void Function([ForcePressDetails](mcp://flutter/api/gestures/ForcePressDetails) details)
Signature for when the pointer that previously triggered a
[ForcePressGestureRecognizer.onStart](mcp://flutter/api/gestures/ForcePressGestureRecognizer/onStart) callback is no longer in contact
with the screen.

[GestureForcePressPeakCallback](mcp://flutter/api/gestures/GestureForcePressPeakCallback)= void Function([ForcePressDetails](mcp://flutter/api/gestures/ForcePressDetails) details)
Signature used by [ForcePressGestureRecognizer](mcp://flutter/api/gestures/ForcePressGestureRecognizer) for when a pointer that has
pressed with at least [ForcePressGestureRecognizer.peakPressure](mcp://flutter/api/gestures/ForcePressGestureRecognizer/peakPressure).

[GestureForcePressStartCallback](mcp://flutter/api/gestures/GestureForcePressStartCallback)= void Function([ForcePressDetails](mcp://flutter/api/gestures/ForcePressDetails) details)
Signature used by a [ForcePressGestureRecognizer](mcp://flutter/api/gestures/ForcePressGestureRecognizer) for when a pointer has
pressed with at least [ForcePressGestureRecognizer.startPressure](mcp://flutter/api/gestures/ForcePressGestureRecognizer/startPressure).

[GestureForcePressUpdateCallback](mcp://flutter/api/gestures/GestureForcePressUpdateCallback)= void Function([ForcePressDetails](mcp://flutter/api/gestures/ForcePressDetails) details)
Signature used by [ForcePressGestureRecognizer](mcp://flutter/api/gestures/ForcePressGestureRecognizer) during the frames
after the triggering of a [ForcePressGestureRecognizer.onStart](mcp://flutter/api/gestures/ForcePressGestureRecognizer/onStart) callback.

[GestureLongPressCallback](mcp://flutter/api/gestures/GestureLongPressCallback)= void Function()
Callback signature for [LongPressGestureRecognizer.onLongPress](mcp://flutter/api/gestures/LongPressGestureRecognizer/onLongPress).

[GestureLongPressEndCallback](mcp://flutter/api/gestures/GestureLongPressEndCallback)= void Function([LongPressEndDetails](mcp://flutter/api/gestures/LongPressEndDetails) details)
Callback signature for [LongPressGestureRecognizer.onLongPressEnd](mcp://flutter/api/gestures/LongPressGestureRecognizer/onLongPressEnd).

[GestureLongPressMoveUpdateCallback](mcp://flutter/api/gestures/GestureLongPressMoveUpdateCallback)= void Function([LongPressMoveUpdateDetails](mcp://flutter/api/gestures/LongPressMoveUpdateDetails) details)
Callback signature for [LongPressGestureRecognizer.onLongPressMoveUpdate](mcp://flutter/api/gestures/LongPressGestureRecognizer/onLongPressMoveUpdate).

[GestureLongPressStartCallback](mcp://flutter/api/gestures/GestureLongPressStartCallback)= void Function([LongPressStartDetails](mcp://flutter/api/gestures/LongPressStartDetails) details)
Callback signature for [LongPressGestureRecognizer.onLongPressStart](mcp://flutter/api/gestures/LongPressGestureRecognizer/onLongPressStart).

[GestureLongPressUpCallback](mcp://flutter/api/gestures/GestureLongPressUpCallback)= void Function()
Callback signature for [LongPressGestureRecognizer.onLongPressUp](mcp://flutter/api/gestures/LongPressGestureRecognizer/onLongPressUp).

[GestureRecognizerFactoryConstructor](mcp://flutter/api/widgets/GestureRecognizerFactoryConstructor)<T extends [GestureRecognizer](mcp://flutter/api/gestures/GestureRecognizer)>= T Function()
Signature for closures that implement [GestureRecognizerFactory.constructor](mcp://flutter/api/widgets/GestureRecognizerFactory/constructor).

[GestureRecognizerFactoryInitializer](mcp://flutter/api/widgets/GestureRecognizerFactoryInitializer)<T extends [GestureRecognizer](mcp://flutter/api/gestures/GestureRecognizer)>= void Function(T instance)
Signature for closures that implement [GestureRecognizerFactory.initializer](mcp://flutter/api/widgets/GestureRecognizerFactory/initializer).

[GestureScaleEndCallback](mcp://flutter/api/gestures/GestureScaleEndCallback)= void Function([ScaleEndDetails](mcp://flutter/api/gestures/ScaleEndDetails) details)
Signature for when the pointers are no longer in contact with the screen.

[GestureScaleStartCallback](mcp://flutter/api/gestures/GestureScaleStartCallback)= void Function([ScaleStartDetails](mcp://flutter/api/gestures/ScaleStartDetails) details)
Signature for when the pointers in contact with the screen have established
a focal point and initial scale of 1.0.

[GestureScaleUpdateCallback](mcp://flutter/api/gestures/GestureScaleUpdateCallback)= void Function([ScaleUpdateDetails](mcp://flutter/api/gestures/ScaleUpdateDetails) details)
Signature for when the pointers in contact with the screen have indicated a
new focal point and/or scale.

[GestureTapCallback](mcp://flutter/api/gestures/GestureTapCallback)= void Function()
Signature for when a tap has occurred.

[GestureTapCancelCallback](mcp://flutter/api/gestures/GestureTapCancelCallback)= void Function()
Signature for when the pointer that previously triggered a
[GestureTapDownCallback](mcp://flutter/api/gestures/GestureTapDownCallback) will not end up causing a tap.

[GestureTapDownCallback](mcp://flutter/api/gestures/GestureTapDownCallback)= void Function([TapDownDetails](mcp://flutter/api/gestures/TapDownDetails) details)
Signature for when a pointer that might cause a tap has contacted the
screen.

[GestureTapUpCallback](mcp://flutter/api/gestures/GestureTapUpCallback)= void Function([TapUpDetails](mcp://flutter/api/gestures/TapUpDetails) details)
Signature for when a pointer that will trigger a tap has stopped contacting
the screen.

[HeroFlightShuttleBuilder](mcp://flutter/api/widgets/HeroFlightShuttleBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) flightContext, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation, [HeroFlightDirection](mcp://flutter/api/widgets/HeroFlightDirection) flightDirection, [BuildContext](mcp://flutter/api/widgets/BuildContext) fromHeroContext, [BuildContext](mcp://flutter/api/widgets/BuildContext) toHeroContext)
A function that lets [Hero](mcp://flutter/api/widgets/Hero) es self supply a [Widget](mcp://flutter/api/widgets/Widget) that is shown during the
hero's flight from one route to another instead of default (which is to
show the destination route's instance of the Hero).

[HeroPlaceholderBuilder](mcp://flutter/api/widgets/HeroPlaceholderBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Size](mcp://flutter/api/dart-ui/Size) heroSize, [Widget](mcp://flutter/api/widgets/Widget) child)
Signature for a function that builds a [Hero](mcp://flutter/api/widgets/Hero) placeholder widget given a
child and a [Size](mcp://flutter/api/dart-ui/Size).

[HttpClientProvider](mcp://flutter/api/painting/HttpClientProvider)= [HttpClient](mcp://flutter/api/dart-io/HttpClient) Function()
Signature for a method that returns an [HttpClient](mcp://flutter/api/dart-io/HttpClient).

[ImageChunkListener](mcp://flutter/api/painting/ImageChunkListener)= void Function([ImageChunkEvent](mcp://flutter/api/painting/ImageChunkEvent) event)
Signature for listening to [ImageChunkEvent](mcp://flutter/api/painting/ImageChunkEvent) events.

[ImageDecoderCallback](mcp://flutter/api/painting/ImageDecoderCallback)= [Future](mcp://flutter/api/dart-async/Future)<[Codec](mcp://flutter/api/dart-ui/Codec)> Function([ImmutableBuffer](mcp://flutter/api/dart-ui/ImmutableBuffer) buffer, {[TargetImageSizeCallback](mcp://flutter/api/dart-ui/TargetImageSizeCallback)? getTargetSize})
Performs the decode process for use in [ImageProvider.loadImage](mcp://flutter/api/painting/ImageProvider/loadImage).

[ImageErrorListener](mcp://flutter/api/painting/ImageErrorListener)= void Function([Object](mcp://flutter/api/dart-core/Object) exception, [StackTrace](mcp://flutter/api/dart-core/StackTrace)? stackTrace)
Signature for reporting errors when resolving images.

[ImageErrorWidgetBuilder](mcp://flutter/api/widgets/ImageErrorWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Object](mcp://flutter/api/dart-core/Object) error, [StackTrace](mcp://flutter/api/dart-core/StackTrace)? stackTrace)
Signature used by [Image.errorBuilder](mcp://flutter/api/widgets/Image/errorBuilder) to create a replacement widget to
render instead of the image.

[ImageFrameBuilder](mcp://flutter/api/widgets/ImageFrameBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Widget](mcp://flutter/api/widgets/Widget) child, [int](mcp://flutter/api/dart-core/int)? frame, [bool](mcp://flutter/api/dart-core/bool) wasSynchronouslyLoaded)
Signature used by [Image.frameBuilder](mcp://flutter/api/widgets/Image/frameBuilder) to control the widget that will be
used when an [Image](mcp://flutter/api/widgets/Image) is built.

[ImageListener](mcp://flutter/api/painting/ImageListener)= void Function([ImageInfo](mcp://flutter/api/painting/ImageInfo) image, [bool](mcp://flutter/api/dart-core/bool) synchronousCall)
Signature for callbacks reporting that an image is available.

[ImageLoadingBuilder](mcp://flutter/api/widgets/ImageLoadingBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Widget](mcp://flutter/api/widgets/Widget) child, [ImageChunkEvent](mcp://flutter/api/painting/ImageChunkEvent)? loadingProgress)
Signature used by [Image.loadingBuilder](mcp://flutter/api/widgets/Image/loadingBuilder) to build a representation of the
image's loading progress.

[IndexedWidgetBuilder](mcp://flutter/api/widgets/IndexedWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [int](mcp://flutter/api/dart-core/int) index)
Signature for a function that creates a widget for a given index, e.g., in a
list.

[InitialRouteListFactory](mcp://flutter/api/widgets/InitialRouteListFactory)= [List](mcp://flutter/api/dart-core/List)<[Route](mcp://flutter/api/widgets/Route)> Function([String](mcp://flutter/api/dart-core/String) initialRoute)
The signature of [WidgetsApp.onGenerateInitialRoutes](mcp://flutter/api/widgets/WidgetsApp/onGenerateInitialRoutes).

[InlineSpanVisitor](mcp://flutter/api/painting/InlineSpanVisitor)= [bool](mcp://flutter/api/dart-core/bool) Function([InlineSpan](mcp://flutter/api/painting/InlineSpan) span)
Called on each span as [InlineSpan.visitChildren](mcp://flutter/api/painting/InlineSpan/visitChildren) walks the [InlineSpan](mcp://flutter/api/painting/InlineSpan) tree.

[InspectorSelectionChangedCallback](mcp://flutter/api/widgets/InspectorSelectionChangedCallback)= void Function()
Signature for the selection change callback used by
[WidgetInspectorService.selectionChangedCallback](mcp://flutter/api/widgets/WidgetInspectorService/selectionChangedCallback).

[InteractiveViewerWidgetBuilder](mcp://flutter/api/widgets/InteractiveViewerWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Quad](mcp://flutter/api/package-vector_math_vector_math_64/Quad) viewport)
A signature for widget builders that take a [Quad](mcp://flutter/api/package-vector_math_vector_math_64/Quad) of the current viewport.

[LayoutWidgetBuilder](mcp://flutter/api/widgets/LayoutWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [BoxConstraints](mcp://flutter/api/rendering/BoxConstraints) constraints)
The signature of the [LayoutBuilder](mcp://flutter/api/widgets/LayoutBuilder) builder function.

[LocaleListResolutionCallback](mcp://flutter/api/widgets/LocaleListResolutionCallback)= [Locale](mcp://flutter/api/dart-ui/Locale)? Function([List](mcp://flutter/api/dart-core/List)<[Locale](mcp://flutter/api/dart-ui/Locale)>? locales, [Iterable](mcp://flutter/api/dart-core/Iterable)<[Locale](mcp://flutter/api/dart-ui/Locale)> supportedLocales)
The signature of [WidgetsApp.localeListResolutionCallback](mcp://flutter/api/widgets/WidgetsApp/localeListResolutionCallback).

[LocaleResolutionCallback](mcp://flutter/api/widgets/LocaleResolutionCallback)= [Locale](mcp://flutter/api/dart-ui/Locale)? Function([Locale](mcp://flutter/api/dart-ui/Locale)? locale, [Iterable](mcp://flutter/api/dart-core/Iterable)<[Locale](mcp://flutter/api/dart-ui/Locale)> supportedLocales)
The signature of [WidgetsApp.localeResolutionCallback](mcp://flutter/api/widgets/WidgetsApp/localeResolutionCallback).

[MagnifierBuilder](mcp://flutter/api/widgets/MagnifierBuilder)= [Widget](mcp://flutter/api/widgets/Widget)? Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [MagnifierController](mcp://flutter/api/widgets/MagnifierController) controller, [ValueNotifier](mcp://flutter/api/foundation/ValueNotifier)<[MagnifierInfo](mcp://flutter/api/widgets/MagnifierInfo)> magnifierInfo)
Signature for a builder that builds a [Widget](mcp://flutter/api/widgets/Widget) with a [MagnifierController](mcp://flutter/api/widgets/MagnifierController).

[MenuItemSerializableIdGenerator](mcp://flutter/api/widgets/MenuItemSerializableIdGenerator)= [int](mcp://flutter/api/dart-core/int) Function([PlatformMenuItem](mcp://flutter/api/widgets/PlatformMenuItem) item)
The signature for a function that generates unique menu item IDs for
serialization of a [PlatformMenuItem](mcp://flutter/api/widgets/PlatformMenuItem).

[MoveExitWidgetSelectionButtonBuilder](mcp://flutter/api/widgets/MoveExitWidgetSelectionButtonBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, {required [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) onPressed, required [String](mcp://flutter/api/dart-core/String) semanticsLabel, [bool](mcp://flutter/api/dart-core/bool) usesDefaultAlignment})
Signature for the builder callback used by
[WidgetInspector.moveExitWidgetSelectionButtonBuilder](mcp://flutter/api/widgets/WidgetInspector/moveExitWidgetSelectionButtonBuilder).

[NavigatorFinderCallback](mcp://flutter/api/widgets/NavigatorFinderCallback)= [NavigatorState](mcp://flutter/api/widgets/NavigatorState) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context)
A callback that given a [BuildContext](mcp://flutter/api/widgets/BuildContext) finds a [NavigatorState](mcp://flutter/api/widgets/NavigatorState).

[NestedScrollViewHeaderSliversBuilder](mcp://flutter/api/widgets/NestedScrollViewHeaderSliversBuilder)= [List](mcp://flutter/api/dart-core/List)<[Widget](mcp://flutter/api/widgets/Widget)> Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [bool](mcp://flutter/api/dart-core/bool) innerBoxIsScrolled)
Signature used by [NestedScrollView](mcp://flutter/api/widgets/NestedScrollView) for building its header.

[NotificationListenerCallback](mcp://flutter/api/widgets/NotificationListenerCallback)<T extends [Notification](mcp://flutter/api/widgets/Notification)>= [bool](mcp://flutter/api/dart-core/bool) Function(T notification)
Signature for [Notification](mcp://flutter/api/widgets/Notification) listeners.

[NullableIndexedWidgetBuilder](mcp://flutter/api/widgets/NullableIndexedWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget)? Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [int](mcp://flutter/api/dart-core/int) index)
Signature for a function that creates a widget for a given index, e.g., in a
list, but may return null.

[OnInvokeCallback](mcp://flutter/api/widgets/OnInvokeCallback)<T extends [Intent](mcp://flutter/api/widgets/Intent)>= [Object](mcp://flutter/api/dart-core/Object)? Function(T intent)
The signature of a callback accepted by [CallbackAction.onInvoke](mcp://flutter/api/widgets/CallbackAction/onInvoke).

[OnKeyEventCallback](mcp://flutter/api/widgets/OnKeyEventCallback)= [KeyEventResult](mcp://flutter/api/widgets/KeyEventResult) Function([KeyEvent](mcp://flutter/api/services/KeyEvent) event)
Signature of a callback used by [FocusManager.addEarlyKeyEventHandler](mcp://flutter/api/widgets/FocusManager/addEarlyKeyEventHandler) and
[FocusManager.addLateKeyEventHandler](mcp://flutter/api/widgets/FocusManager/addLateKeyEventHandler).

[OrientationWidgetBuilder](mcp://flutter/api/widgets/OrientationWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Orientation](mcp://flutter/api/widgets/Orientation) orientation)
Signature for a function that builds a widget given an [Orientation](mcp://flutter/api/widgets/Orientation).

[OverlayChildLayoutBuilder](mcp://flutter/api/widgets/OverlayChildLayoutBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [OverlayChildLayoutInfo](mcp://flutter/api/widgets/OverlayChildLayoutInfo) info)
The signature of the widget builder callback used in
[OverlayPortal.overlayChildLayoutBuilder](mcp://flutter/api/widgets/OverlayPortal/OverlayPortal.overlayChildLayoutBuilder).

[PageRouteFactory](mcp://flutter/api/widgets/PageRouteFactory)= [PageRoute](mcp://flutter/api/widgets/PageRoute)<T> Function<T>([RouteSettings](mcp://flutter/api/widgets/RouteSettings) settings, [WidgetBuilder](mcp://flutter/api/widgets/WidgetBuilder) builder)
The signature of [WidgetsApp.pageRouteBuilder](mcp://flutter/api/widgets/WidgetsApp/pageRouteBuilder).

[PaintImageCallback](mcp://flutter/api/painting/PaintImageCallback)= void Function([ImageSizeInfo](mcp://flutter/api/painting/ImageSizeInfo) info)
Called when the framework is about to paint an [Image](mcp://flutter/api/dart-ui/Image) to a [Canvas](mcp://flutter/api/dart-ui/Canvas) with an
[ImageSizeInfo](mcp://flutter/api/painting/ImageSizeInfo) that contains the decoded size of the image as well as its
output size.

[PlatformViewSurfaceFactory](mcp://flutter/api/widgets/PlatformViewSurfaceFactory)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [PlatformViewController](mcp://flutter/api/services/PlatformViewController) controller)
A factory for a surface presenting a platform view as part of the widget hierarchy.

[PointerCancelEventListener](mcp://flutter/api/rendering/PointerCancelEventListener)= void Function([PointerCancelEvent](mcp://flutter/api/gestures/PointerCancelEvent) event)
Signature for listening to [PointerCancelEvent](mcp://flutter/api/gestures/PointerCancelEvent) events.

[PointerDownEventListener](mcp://flutter/api/rendering/PointerDownEventListener)= void Function([PointerDownEvent](mcp://flutter/api/gestures/PointerDownEvent) event)
Signature for listening to [PointerDownEvent](mcp://flutter/api/gestures/PointerDownEvent) events.

[PointerMoveEventListener](mcp://flutter/api/rendering/PointerMoveEventListener)= void Function([PointerMoveEvent](mcp://flutter/api/gestures/PointerMoveEvent) event)
Signature for listening to [PointerMoveEvent](mcp://flutter/api/gestures/PointerMoveEvent) events.

[PointerUpEventListener](mcp://flutter/api/rendering/PointerUpEventListener)= void Function([PointerUpEvent](mcp://flutter/api/gestures/PointerUpEvent) event)
Signature for listening to [PointerUpEvent](mcp://flutter/api/gestures/PointerUpEvent) events.

[PopInvokedCallback](mcp://flutter/api/widgets/PopInvokedCallback)= void Function([bool](mcp://flutter/api/dart-core/bool) didPop)
A callback type for informing that a navigation pop has been invoked,
whether or not it was handled successfully.

[PopInvokedWithResultCallback](mcp://flutter/api/widgets/PopInvokedWithResultCallback)<T>= void Function([bool](mcp://flutter/api/dart-core/bool) didPop, T? result)
A callback type for informing that a navigation pop has been invoked,
whether or not it was handled successfully.

[PopPageCallback](mcp://flutter/api/widgets/PopPageCallback)= [bool](mcp://flutter/api/dart-core/bool) Function([Route](mcp://flutter/api/widgets/Route) route, dynamic result)
Signature for the [Navigator.onPopPage](mcp://flutter/api/widgets/Navigator/onPopPage) callback.

[PopResultCallback](mcp://flutter/api/widgets/PopResultCallback)<T>= void Function(T? result)
A signature for a function that is passed the result of a [Route](mcp://flutter/api/widgets/Route).

[RadioBuilder](mcp://flutter/api/widgets/RadioBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [ToggleableStateMixin](mcp://flutter/api/widgets/ToggleableStateMixin)<[StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)> state)
Signature for [RawRadio.builder](mcp://flutter/api/widgets/RawRadio/builder).

[RawMenuAnchorChildBuilder](mcp://flutter/api/widgets/RawMenuAnchorChildBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [MenuController](mcp://flutter/api/widgets/MenuController) controller, [Widget](mcp://flutter/api/widgets/Widget)? child)
Signature for the builder function used by [RawMenuAnchor.builder](mcp://flutter/api/widgets/RawMenuAnchor/builder) to build
the widget that the [RawMenuAnchor](mcp://flutter/api/widgets/RawMenuAnchor) surrounds.

[RawMenuAnchorCloseRequestedCallback](mcp://flutter/api/widgets/RawMenuAnchorCloseRequestedCallback)= void Function([VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) hideOverlay)
Signature for the callback used by [RawMenuAnchor.onCloseRequested](mcp://flutter/api/widgets/RawMenuAnchor/onCloseRequested) to
intercept requests to close a menu.

[RawMenuAnchorOpenRequestedCallback](mcp://flutter/api/widgets/RawMenuAnchorOpenRequestedCallback)= void Function([Offset](mcp://flutter/api/dart-ui/Offset)? position, [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) showOverlay)
Signature for the callback used by [RawMenuAnchor.onOpenRequested](mcp://flutter/api/widgets/RawMenuAnchor/onOpenRequested) to
intercept requests to open a menu.

[RawMenuAnchorOverlayBuilder](mcp://flutter/api/widgets/RawMenuAnchorOverlayBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [RawMenuOverlayInfo](mcp://flutter/api/widgets/RawMenuOverlayInfo) info)
Signature for the builder function used by [RawMenuAnchor.overlayBuilder](mcp://flutter/api/widgets/RawMenuAnchor/overlayBuilder) to
build a menu's overlay.

[RebuildDirtyWidgetCallback](mcp://flutter/api/widgets/RebuildDirtyWidgetCallback)= void Function([Element](mcp://flutter/api/widgets/Element) e, [bool](mcp://flutter/api/dart-core/bool) builtOnce)
Signature for [debugOnRebuildDirtyWidget](mcp://flutter/api/cupertino/debugOnRebuildDirtyWidget) implementations.

[RegisterServiceExtensionCallback](mcp://flutter/api/widgets/RegisterServiceExtensionCallback)= void Function({required [ServiceExtensionCallback](mcp://flutter/api/foundation/ServiceExtensionCallback) callback, required [String](mcp://flutter/api/dart-core/String) name})
Signature for a method that registers the service extension `callback` with
the given `name`.

[RegisterViewFactory](mcp://flutter/api/widgets/RegisterViewFactory)= void Function([String](mcp://flutter/api/dart-core/String), [Object](mcp://flutter/api/dart-core/Object) ([int](mcp://flutter/api/dart-core/int) viewId), {[bool](mcp://flutter/api/dart-core/bool) isVisible})
Function signature for `ui_web.platformViewRegistry.registerViewFactory`.

[RenderConstrainedLayoutBuilder](mcp://flutter/api/widgets/RenderConstrainedLayoutBuilder)<LayoutInfoType, ChildType extends [RenderObject](mcp://flutter/api/rendering/RenderObject)>
 = [RenderAbstractLayoutBuilderMixin](mcp://flutter/api/widgets/RenderAbstractLayoutBuilderMixin)<LayoutInfoType, ChildType>
Generic mixin for [RenderObject](mcp://flutter/api/rendering/RenderObject) s created by an [AbstractLayoutBuilder](mcp://flutter/api/widgets/AbstractLayoutBuilder) with
the the same `LayoutInfoType`.

[ReorderCallback](mcp://flutter/api/widgets/ReorderCallback)= void Function([int](mcp://flutter/api/dart-core/int) oldIndex, [int](mcp://flutter/api/dart-core/int) newIndex)
A callback used by [ReorderableList](mcp://flutter/api/widgets/ReorderableList) to report that a list item has moved
to a new position in the list.

[ReorderDragBoundaryProvider](mcp://flutter/api/widgets/ReorderDragBoundaryProvider)= [DragBoundaryDelegate](mcp://flutter/api/widgets/DragBoundaryDelegate)<[Rect](mcp://flutter/api/dart-ui/Rect)>? Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context)
Used to provide drag boundaries during drag-and-drop reordering.

[ReorderItemProxyDecorator](mcp://flutter/api/widgets/ReorderItemProxyDecorator)= [Widget](mcp://flutter/api/widgets/Widget) Function([Widget](mcp://flutter/api/widgets/Widget) child, [int](mcp://flutter/api/dart-core/int) index, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation)
Signature for the builder callback used to decorate the dragging item in
[ReorderableList](mcp://flutter/api/widgets/ReorderableList) and [SliverReorderableList](mcp://flutter/api/widgets/SliverReorderableList).

[RestorableRouteBuilder](mcp://flutter/api/widgets/RestorableRouteBuilder)<T>= [Route](mcp://flutter/api/widgets/Route)<T> Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Object](mcp://flutter/api/dart-core/Object)? arguments)
Creates a [Route](mcp://flutter/api/widgets/Route) that is to be added to a [Navigator](mcp://flutter/api/widgets/Navigator).

[RouteCompletionCallback](mcp://flutter/api/widgets/RouteCompletionCallback)<T>= void Function(T result)
A callback to handle the result of a completed [Route](mcp://flutter/api/widgets/Route).

[RouteFactory](mcp://flutter/api/widgets/RouteFactory)= [Route](mcp://flutter/api/widgets/Route)? Function([RouteSettings](mcp://flutter/api/widgets/RouteSettings) settings)
Creates a route for the given route settings.

[RouteListFactory](mcp://flutter/api/widgets/RouteListFactory)= [List](mcp://flutter/api/dart-core/List)<[Route](mcp://flutter/api/widgets/Route)> Function([NavigatorState](mcp://flutter/api/widgets/NavigatorState) navigator, [String](mcp://flutter/api/dart-core/String) initialRoute)
Creates a series of one or more routes.

[RoutePageBuilder](mcp://flutter/api/widgets/RoutePageBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> secondaryAnimation)
Signature for the function that builds a route's primary contents.
Used in [PageRouteBuilder](mcp://flutter/api/widgets/PageRouteBuilder) and [showGeneralDialog](mcp://flutter/api/widgets/showGeneralDialog).

[RoutePredicate](mcp://flutter/api/widgets/RoutePredicate)= [bool](mcp://flutter/api/dart-core/bool) Function([Route](mcp://flutter/api/widgets/Route) route)
Signature for the [Navigator.popUntil](mcp://flutter/api/widgets/Navigator/popUntil) predicate argument.

[RoutePresentationCallback](mcp://flutter/api/widgets/RoutePresentationCallback)= [String](mcp://flutter/api/dart-core/String) Function([NavigatorState](mcp://flutter/api/widgets/NavigatorState) navigator, [Object](mcp://flutter/api/dart-core/Object)? arguments)
A callback that given some `arguments` and a `navigator` adds a new
restorable route to that `navigator` and returns the opaque ID of that
new route.

[RouteTransitionsBuilder](mcp://flutter/api/widgets/RouteTransitionsBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> animation, [Animation](mcp://flutter/api/animation/Animation)<[double](mcp://flutter/api/dart-core/double)> secondaryAnimation, [Widget](mcp://flutter/api/widgets/Widget) child)
Signature for the function that builds a route's transitions.
Used in [PageRouteBuilder](mcp://flutter/api/widgets/PageRouteBuilder) and [showGeneralDialog](mcp://flutter/api/widgets/showGeneralDialog).

[ScrollableWidgetBuilder](mcp://flutter/api/widgets/ScrollableWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [ScrollController](mcp://flutter/api/widgets/ScrollController) scrollController)
The signature of a method that provides a [BuildContext](mcp://flutter/api/widgets/BuildContext) and
[ScrollController](mcp://flutter/api/widgets/ScrollController) for building a widget that may overflow the draggable
[Axis](mcp://flutter/api/painting/Axis) of the containing [DraggableScrollableSheet](mcp://flutter/api/widgets/DraggableScrollableSheet).

[ScrollControllerCallback](mcp://flutter/api/widgets/ScrollControllerCallback)= void Function([ScrollPosition](mcp://flutter/api/widgets/ScrollPosition) position)
Signature for when a [ScrollController](mcp://flutter/api/widgets/ScrollController) has added or removed a
[ScrollPosition](mcp://flutter/api/widgets/ScrollPosition).

[ScrollIncrementCalculator](mcp://flutter/api/widgets/ScrollIncrementCalculator)= [double](mcp://flutter/api/dart-core/double) Function([ScrollIncrementDetails](mcp://flutter/api/widgets/ScrollIncrementDetails) details)
A typedef for a function that can calculate the offset for a type of scroll
increment given a [ScrollIncrementDetails](mcp://flutter/api/widgets/ScrollIncrementDetails).

[ScrollNotificationCallback](mcp://flutter/api/widgets/ScrollNotificationCallback)= void Function([ScrollNotification](mcp://flutter/api/widgets/ScrollNotification) notification)
A [ScrollNotification](mcp://flutter/api/widgets/ScrollNotification) listener for [ScrollNotificationObserver](mcp://flutter/api/widgets/ScrollNotificationObserver).

[ScrollNotificationPredicate](mcp://flutter/api/widgets/ScrollNotificationPredicate)= [bool](mcp://flutter/api/dart-core/bool) Function([ScrollNotification](mcp://flutter/api/widgets/ScrollNotification) notification)
A predicate for [ScrollNotification](mcp://flutter/api/widgets/ScrollNotification), used to customize widgets that
listen to notifications from their children.

[SelectableDayPredicate](mcp://flutter/api/widgets/SelectableDayPredicate)= [bool](mcp://flutter/api/dart-core/bool) Function([DateTime](mcp://flutter/api/dart-core/DateTime) day)
Signature for predicating dates for enabled date selections.

[SelectableRegionContextMenuBuilder](mcp://flutter/api/widgets/SelectableRegionContextMenuBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [SelectableRegionState](mcp://flutter/api/widgets/SelectableRegionState) selectableRegionState)
Signature for a widget builder that builds a context menu for the given
[SelectableRegionState](mcp://flutter/api/widgets/SelectableRegionState).

[SelectionChangedCallback](mcp://flutter/api/widgets/SelectionChangedCallback)= void Function([TextSelection](mcp://flutter/api/services/TextSelection) selection, [SelectionChangedCause](mcp://flutter/api/services/SelectionChangedCause)? cause)
Signature for the callback that reports when the user changes the selection
(including the cursor location).

[SemanticIndexCallback](mcp://flutter/api/widgets/SemanticIndexCallback)= [int](mcp://flutter/api/dart-core/int)? Function([Widget](mcp://flutter/api/widgets/Widget) widget, [int](mcp://flutter/api/dart-core/int) localIndex)
A callback which produces a semantic index given a widget and the local index.

[SemanticsBuilderCallback](mcp://flutter/api/rendering/SemanticsBuilderCallback)= [List](mcp://flutter/api/dart-core/List)<[CustomPainterSemantics](mcp://flutter/api/rendering/CustomPainterSemantics)> Function([Size](mcp://flutter/api/dart-ui/Size) size)
Signature of the function returned by [CustomPainter.semanticsBuilder](mcp://flutter/api/rendering/CustomPainter/semanticsBuilder).

[ShaderCallback](mcp://flutter/api/rendering/ShaderCallback)= [Shader](mcp://flutter/api/dart-ui/Shader) Function([Rect](mcp://flutter/api/dart-ui/Rect) bounds)
Signature for a function that creates a [Shader](mcp://flutter/api/dart-ui/Shader) for a given [Rect](mcp://flutter/api/dart-ui/Rect).

[ShaderWarmUpImageCallback](mcp://flutter/api/painting/ShaderWarmUpImageCallback)= [bool](mcp://flutter/api/dart-core/bool) Function([Image](mcp://flutter/api/dart-ui/Image) image)
The signature of [debugCaptureShaderWarmUpImage](mcp://flutter/api/rendering/debugCaptureShaderWarmUpImage).

[ShaderWarmUpPictureCallback](mcp://flutter/api/painting/ShaderWarmUpPictureCallback)= [bool](mcp://flutter/api/dart-core/bool) Function([Picture](mcp://flutter/api/dart-ui/Picture) picture)
The signature of [debugCaptureShaderWarmUpPicture](mcp://flutter/api/rendering/debugCaptureShaderWarmUpPicture).

[SharedAppDataInitCallback](mcp://flutter/api/widgets/SharedAppDataInitCallback)<T>= T Function()
The type of the [SharedAppData.getValue](mcp://flutter/api/widgets/SharedAppData/getValue) `init` parameter.

[SliverLayoutWidgetBuilder](mcp://flutter/api/widgets/SliverLayoutWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [SliverConstraints](mcp://flutter/api/rendering/SliverConstraints) constraints)
The signature of the [SliverLayoutBuilder](mcp://flutter/api/widgets/SliverLayoutBuilder) builder function.

[StatefulWidgetBuilder](mcp://flutter/api/widgets/StatefulWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [StateSetter](mcp://flutter/api/widgets/StateSetter) setState)
Signature for the builder callback used by [StatefulBuilder](mcp://flutter/api/widgets/StatefulBuilder).

[StateSetter](mcp://flutter/api/widgets/StateSetter)= void Function([VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) fn)
The signature of [State.setState](mcp://flutter/api/widgets/State/setState) functions.

[TapBehaviorButtonBuilder](mcp://flutter/api/widgets/TapBehaviorButtonBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, {required [VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) onPressed, required [bool](mcp://flutter/api/dart-core/bool) selectionOnTapEnabled, required [String](mcp://flutter/api/dart-core/String) semanticsLabel})
Signature for the builder callback used by
[WidgetInspector.tapBehaviorButtonBuilder](mcp://flutter/api/widgets/WidgetInspector/tapBehaviorButtonBuilder).

[TapRegionCallback](mcp://flutter/api/widgets/TapRegionCallback)= void Function([PointerDownEvent](mcp://flutter/api/gestures/PointerDownEvent) event)
Signature for a callback called for a [PointerDownEvent](mcp://flutter/api/gestures/PointerDownEvent) relative to a [TapRegion](mcp://flutter/api/widgets/TapRegion).

[TapRegionUpCallback](mcp://flutter/api/widgets/TapRegionUpCallback)= void Function([PointerUpEvent](mcp://flutter/api/gestures/PointerUpEvent) event)
Signature for a callback called for a [PointerUpEvent](mcp://flutter/api/gestures/PointerUpEvent) relative to a [TapRegion](mcp://flutter/api/widgets/TapRegion).

[ToolbarBuilder](mcp://flutter/api/widgets/ToolbarBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Widget](mcp://flutter/api/widgets/Widget) child)
The type for a Function that builds a toolbar's container with the given
child.

[TransformCallback](mcp://flutter/api/widgets/TransformCallback)= [Matrix4](mcp://flutter/api/package-vector_math_vector_math_64/Matrix4) Function([double](mcp://flutter/api/dart-core/double) animationValue)
Signature for the callback to [MatrixTransition.onTransform](mcp://flutter/api/widgets/MatrixTransition/onTransform).

[TransitionBuilder](mcp://flutter/api/widgets/TransitionBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [Widget](mcp://flutter/api/widgets/Widget)? child)
A builder that builds a widget given a child.

[TraversalRequestFocusCallback](mcp://flutter/api/widgets/TraversalRequestFocusCallback)= void Function([FocusNode](mcp://flutter/api/widgets/FocusNode) node, {[double](mcp://flutter/api/dart-core/double)? alignment, [ScrollPositionAlignmentPolicy](mcp://flutter/api/widgets/ScrollPositionAlignmentPolicy)? alignmentPolicy, [Curve](mcp://flutter/api/animation/Curve)? curve, [Duration](mcp://flutter/api/dart-core/Duration)? duration})
Signature for the callback that's called when a traversal policy
requests focus.

[TreeSliverNodeBuilder](mcp://flutter/api/widgets/TreeSliverNodeBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode)<[Object](mcp://flutter/api/dart-core/Object)?> node, [AnimationStyle](mcp://flutter/api/animation/AnimationStyle) animationStyle)
Signature for a function that creates a [Widget](mcp://flutter/api/widgets/Widget) to represent the given
[TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode) in the [TreeSliver](mcp://flutter/api/widgets/TreeSliver).

[TreeSliverNodeCallback](mcp://flutter/api/widgets/TreeSliverNodeCallback)= void Function([TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode)<[Object](mcp://flutter/api/dart-core/Object)?> node)
Signature for a function that is called when a [TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode) is toggled,
changing its expanded state.

[TreeSliverRowExtentBuilder](mcp://flutter/api/widgets/TreeSliverRowExtentBuilder)= [double](mcp://flutter/api/dart-core/double) Function([TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode)<[Object](mcp://flutter/api/dart-core/Object)?> node, [SliverLayoutDimensions](mcp://flutter/api/rendering/SliverLayoutDimensions) dimensions)
Signature for a function that returns an extent for the given
[TreeSliverNode](mcp://flutter/api/widgets/TreeSliverNode) in the [TreeSliver](mcp://flutter/api/widgets/TreeSliver).

[TweenConstructor](mcp://flutter/api/widgets/TweenConstructor)<T extends [Object](mcp://flutter/api/dart-core/Object)>= [Tween](mcp://flutter/api/animation/Tween)<T> Function(T targetValue)
Signature for a [Tween](mcp://flutter/api/animation/Tween) factory.

[TweenVisitor](mcp://flutter/api/widgets/TweenVisitor)<T extends [Object](mcp://flutter/api/dart-core/Object)>= [Tween](mcp://flutter/api/animation/Tween)<T>? Function([Tween](mcp://flutter/api/animation/Tween)<T>? tween, T targetValue, [TweenConstructor](mcp://flutter/api/widgets/TweenConstructor)<T> constructor)
Signature for callbacks passed to [ImplicitlyAnimatedWidgetState.forEachTween](mcp://flutter/api/widgets/ImplicitlyAnimatedWidgetState/forEachTween).

[TwoDimensionalIndexedWidgetBuilder](mcp://flutter/api/widgets/TwoDimensionalIndexedWidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget)? Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [ChildVicinity](mcp://flutter/api/widgets/ChildVicinity) vicinity)
Signature for a function that creates a widget for a given [ChildVicinity](mcp://flutter/api/widgets/ChildVicinity),
e.g., in a [TwoDimensionalScrollView](mcp://flutter/api/widgets/TwoDimensionalScrollView), but may return null.

[TwoDimensionalViewportBuilder](mcp://flutter/api/widgets/TwoDimensionalViewportBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [ViewportOffset](mcp://flutter/api/rendering/ViewportOffset) verticalPosition, [ViewportOffset](mcp://flutter/api/rendering/ViewportOffset) horizontalPosition)
Signature used by [TwoDimensionalScrollable](mcp://flutter/api/widgets/TwoDimensionalScrollable) to build the viewport through
which the scrollable content is displayed.

[ValueChanged](mcp://flutter/api/foundation/ValueChanged)<T>= void Function(T value)
Signature for callbacks that report that an underlying value has changed.

[ValueGetter](mcp://flutter/api/foundation/ValueGetter)<T>= T Function()
Signature for callbacks that are to report a value on demand.

[ValueListenableTransformer](mcp://flutter/api/animation/ValueListenableTransformer)<T>= T Function(T)
Signature for method used to transform values in [Animation.fromValueListenable](mcp://flutter/api/animation/Animation/Animation.fromValueListenable).

[ValueSetter](mcp://flutter/api/foundation/ValueSetter)<T>= void Function(T value)
Signature for callbacks that report that a value has been set.

[ValueWidgetBuilder](mcp://flutter/api/widgets/ValueWidgetBuilder)<T>= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, T value, [Widget](mcp://flutter/api/widgets/Widget)? child)
Builds a [Widget](mcp://flutter/api/widgets/Widget) when given a concrete value of a [ValueListenable<T>](mcp://flutter/api/foundation/ValueListenable).

[ViewportBuilder](mcp://flutter/api/widgets/ViewportBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context, [ViewportOffset](mcp://flutter/api/rendering/ViewportOffset) position)
Signature used by [Scrollable](mcp://flutter/api/widgets/Scrollable) to build the viewport through which the
scrollable content is displayed.

[VoidCallback](mcp://flutter/api/dart-ui/VoidCallback)= void Function()
Signature of callbacks that have no arguments and return no data.

[WidgetBuilder](mcp://flutter/api/widgets/WidgetBuilder)= [Widget](mcp://flutter/api/widgets/Widget) Function([BuildContext](mcp://flutter/api/widgets/BuildContext) context)
Signature for a function that creates a widget, e.g. [StatelessWidget.build](mcp://flutter/api/widgets/StatelessWidget/build) or [State.build](mcp://flutter/api/widgets/State/build).

[WidgetPropertyResolver](mcp://flutter/api/widgets/WidgetPropertyResolver)<T>= T Function([Set](mcp://flutter/api/dart-core/Set)<[WidgetState](mcp://flutter/api/widgets/WidgetState)> states)
Signature for the function that returns a value of type `T` based on a given
set of states.

[WidgetStateMap](mcp://flutter/api/widgets/WidgetStateMap)<T>
 = [Map](mcp://flutter/api/dart-core/Map)<[WidgetStatesConstraint](mcp://flutter/api/widgets/WidgetStatesConstraint), T>
A [Map](mcp://flutter/api/dart-core/Map) used to resolve to a single value of type `T` based on
the current set of Widget states.

[WillPopCallback](mcp://flutter/api/widgets/WillPopCallback)= [Future](mcp://flutter/api/dart-async/Future)<[bool](mcp://flutter/api/dart-core/bool)> Function()
Signature for a callback that verifies that it's OK to call [Navigator.pop](mcp://flutter/api/widgets/Navigator/pop).

## Exceptions / Errors

[FlutterError](mcp://flutter/api/foundation/FlutterError)
Error class used to report Flutter-specific assertion failures and
contract violations.

[NetworkImageLoadException](mcp://flutter/api/painting/NetworkImageLoadException)
The exception thrown when the HTTP request to load a network image fails.

[TickerCanceled](mcp://flutter/api/scheduler/TickerCanceled)
Exception thrown by [Ticker](mcp://flutter/api/scheduler/Ticker) objects on the [TickerFuture.orCancel](mcp://flutter/api/scheduler/TickerFuture/orCancel) future
when the ticker is canceled.