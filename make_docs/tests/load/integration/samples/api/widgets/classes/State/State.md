# State<T extends StatefulWidget> class [abstract](https://dart.dev/language/class-modifiers#abstract "This type can not be directly constructed.")

The logic and internal state for a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget).

State is information that (1) can be read synchronously when the widget is
built and (2) might change during the lifetime of the widget. It is the
responsibility of the widget implementer to ensure that the [State](flutter-docs://api/widgets/State) is
promptly notified when such state changes, using [State.setState](flutter-docs://api/widgets/State/setState).

[State](flutter-docs://api/widgets/State) objects are created by the framework by calling the [StatefulWidget.createState](flutter-docs://api/widgets/StatefulWidget/createState) method when inflating a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) to
insert it into the tree. Because a given [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) instance can be
inflated multiple times (e.g., the widget is incorporated into the tree in
multiple places at once), there might be more than one [State](flutter-docs://api/widgets/State) object
associated with a given [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) instance. Similarly, if a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) is removed from the tree and later inserted in to the tree
again, the framework will call [StatefulWidget.createState](flutter-docs://api/widgets/StatefulWidget/createState) again to create
a fresh [State](flutter-docs://api/widgets/State) object, simplifying the lifecycle of [State](flutter-docs://api/widgets/State) objects.

[State](flutter-docs://api/widgets/State) objects have the following lifecycle:

- The framework creates a [State](flutter-docs://api/widgets/State) object by calling
[StatefulWidget.createState](flutter-docs://api/widgets/StatefulWidget/createState).
- The newly created [State](flutter-docs://api/widgets/State) object is associated with a [BuildContext](flutter-docs://api/widgets/BuildContext).
This association is permanent: the [State](flutter-docs://api/widgets/State) object will never change its
[BuildContext](flutter-docs://api/widgets/BuildContext). However, the [BuildContext](flutter-docs://api/widgets/BuildContext) itself can be moved around
the tree along with its subtree. At this point, the [State](flutter-docs://api/widgets/State) object is
considered [mounted](flutter-docs://api/widgets/State/mounted).
- The framework calls [initState](flutter-docs://api/widgets/State/initState). Subclasses of [State](flutter-docs://api/widgets/State) should override
[initState](flutter-docs://api/widgets/State/initState) to perform one-time initialization that depends on the
[BuildContext](flutter-docs://api/widgets/BuildContext) or the widget, which are available as the [context](flutter-docs://api/widgets/State/context) and
[widget](flutter-docs://api/widgets/State/widget) properties, respectively, when the [initState](flutter-docs://api/widgets/State/initState) method is
called.
- The framework calls [didChangeDependencies](flutter-docs://api/widgets/State/didChangeDependencies). Subclasses of [State](flutter-docs://api/widgets/State) should
override [didChangeDependencies](flutter-docs://api/widgets/State/didChangeDependencies) to perform initialization involving
[InheritedWidget](flutter-docs://api/widgets/InheritedWidget) s. If [BuildContext.dependOnInheritedWidgetOfExactType](flutter-docs://api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) is
called, the [didChangeDependencies](flutter-docs://api/widgets/State/didChangeDependencies) method will be called again if the
inherited widgets subsequently change or if the widget moves in the tree.
- At this point, the [State](flutter-docs://api/widgets/State) object is fully initialized and the framework
might call its [build](flutter-docs://api/widgets/State/build) method any number of times to obtain a
description of the user interface for this subtree. [State](flutter-docs://api/widgets/State) objects can
spontaneously request to rebuild their subtree by calling their
[setState](flutter-docs://api/widgets/State/setState) method, which indicates that some of their internal state
has changed in a way that might impact the user interface in this
subtree.
- During this time, a parent widget might rebuild and request that this
location in the tree update to display a new widget with the same
[runtimeType](flutter-docs://api/dart-core/Object/runtimeType) and [Widget.key](flutter-docs://api/widgets/Widget/key). When this happens, the framework will
update the [widget](flutter-docs://api/widgets/State/widget) property to refer to the new widget and then call the
[didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget) method with the previous widget as an argument. [State](flutter-docs://api/widgets/State) objects should override [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget) to respond to changes in their
associated widget (e.g., to start implicit animations). The framework
always calls [build](flutter-docs://api/widgets/State/build) after calling [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget), which means any
calls to [setState](flutter-docs://api/widgets/State/setState) in [didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget) are redundant. (See also the
discussion at [Element.rebuild](flutter-docs://api/widgets/Element/rebuild).)
- During development, if a hot reload occurs (whether initiated from the
command line `flutter` tool by pressing `r`, or from an IDE), the
[reassemble](flutter-docs://api/widgets/State/reassemble) method is called. This provides an opportunity to
reinitialize any data that was prepared in the [initState](flutter-docs://api/widgets/State/initState) method.
- If the subtree containing the [State](flutter-docs://api/widgets/State) object is removed from the tree
(e.g., because the parent built a widget with a different [runtimeType](flutter-docs://api/dart-core/Object/runtimeType) or [Widget.key](flutter-docs://api/widgets/Widget/key)), the framework calls the [deactivate](flutter-docs://api/widgets/State/deactivate) method. Subclasses
should override this method to clean up any links between this object
and other elements in the tree (e.g. if you have provided an ancestor
with a pointer to a descendant's [RenderObject](flutter-docs://api/rendering/RenderObject)).
- At this point, the framework might reinsert this subtree into another
part of the tree. If that happens, the framework will ensure that it
calls [build](flutter-docs://api/widgets/State/build) to give the [State](flutter-docs://api/widgets/State) object a chance to adapt to its new
location in the tree. If the framework does reinsert this subtree, it
will do so before the end of the animation frame in which the subtree was
removed from the tree. For this reason, [State](flutter-docs://api/widgets/State) objects can defer
releasing most resources until the framework calls their [dispose](flutter-docs://api/widgets/State/dispose) method.
- If the framework does not reinsert this subtree by the end of the current
animation frame, the framework will call [dispose](flutter-docs://api/widgets/State/dispose), which indicates that
this [State](flutter-docs://api/widgets/State) object will never build again. Subclasses should override
this method to release any resources retained by this object (e.g.,
stop any active animations).
- After the framework calls [dispose](flutter-docs://api/widgets/State/dispose), the [State](flutter-docs://api/widgets/State) object is considered
unmounted and the [mounted](flutter-docs://api/widgets/State/mounted) property is false. It is an error to call
[setState](flutter-docs://api/widgets/State/setState) at this point. This stage of the lifecycle is terminal: there
is no way to remount a [State](flutter-docs://api/widgets/State) object that has been disposed.


See also:

- [StatefulWidget](flutter-docs://api/widgets/StatefulWidget), where the current configuration of a [State](flutter-docs://api/widgets/State) is hosted,
and whose documentation has sample code for [State](flutter-docs://api/widgets/State).
- [StatelessWidget](flutter-docs://api/widgets/StatelessWidget), for widgets that always build the same way given a
particular configuration and ambient state.
- [InheritedWidget](flutter-docs://api/widgets/InheritedWidget), for widgets that introduce ambient state that can
be read by descendant widgets.
- [Widget](flutter-docs://api/widgets/Widget), for an overview of widgets in general.


Mixed-in types
- [Diagnosticable](flutter-docs://api/foundation/Diagnosticable)

Implementers
- [AnimatedGridState](flutter-docs://api/widgets/AnimatedGridState)
- [AnimatedListState](flutter-docs://api/widgets/AnimatedListState)
- [AutofillGroupState](flutter-docs://api/widgets/AutofillGroupState)
- [AutomaticKeepAliveClientMixin](flutter-docs://api/widgets/AutomaticKeepAliveClientMixin)
- [DrawerControllerState](flutter-docs://api/material/DrawerControllerState)
- [EditableTextState](flutter-docs://api/widgets/EditableTextState)
- [FormFieldState](flutter-docs://api/widgets/FormFieldState)
- [FormState](flutter-docs://api/widgets/FormState)
- [ImplicitlyAnimatedWidgetState](flutter-docs://api/widgets/ImplicitlyAnimatedWidgetState)
- [MaterialStateMixin](flutter-docs://api/material/MaterialStateMixin)
- [NavigatorState](flutter-docs://api/widgets/NavigatorState)
- [NestedScrollViewState](flutter-docs://api/widgets/NestedScrollViewState)
- [OverlayState](flutter-docs://api/widgets/OverlayState)
- [PaginatedDataTableState](flutter-docs://api/material/PaginatedDataTableState)
- [PopupMenuButtonState](flutter-docs://api/material/PopupMenuButtonState)
- [PopupMenuItemState](flutter-docs://api/material/PopupMenuItemState)
- [RawGestureDetectorState](flutter-docs://api/widgets/RawGestureDetectorState)
- [RawScrollbarState](flutter-docs://api/widgets/RawScrollbarState)
- [RefreshIndicatorState](flutter-docs://api/material/RefreshIndicatorState)
- [ReorderableListState](flutter-docs://api/widgets/ReorderableListState)
- [RestorationMixin](flutter-docs://api/widgets/RestorationMixin)
- [ScaffoldMessengerState](flutter-docs://api/material/ScaffoldMessengerState)
- [ScaffoldState](flutter-docs://api/material/ScaffoldState)
- [ScrollableState](flutter-docs://api/widgets/ScrollableState)
- [ScrollNotificationObserverState](flutter-docs://api/widgets/ScrollNotificationObserverState)
- [SegmentedButtonState](flutter-docs://api/material/SegmentedButtonState)
- [SelectableRegionState](flutter-docs://api/widgets/SelectableRegionState)
- [SelectionAreaState](flutter-docs://api/material/SelectionAreaState)
- [SingleTickerProviderStateMixin](flutter-docs://api/widgets/SingleTickerProviderStateMixin)
- [SliverAnimatedGridState](flutter-docs://api/widgets/SliverAnimatedGridState)
- [SliverAnimatedListState](flutter-docs://api/widgets/SliverAnimatedListState)
- [SliverReorderableListState](flutter-docs://api/widgets/SliverReorderableListState)
- [TickerProviderStateMixin](flutter-docs://api/widgets/TickerProviderStateMixin)
- [TooltipState](flutter-docs://api/material/TooltipState)
- [TwoDimensionalScrollableState](flutter-docs://api/widgets/TwoDimensionalScrollableState)
- [UndoHistoryState](flutter-docs://api/widgets/UndoHistoryState)

Annotations
- @[optionalTypeArgs](flutter-docs://api/meta/optionalTypeArgs)

## Constructors

[State](flutter-docs://api/widgets/State/State)()

## Properties

[context](flutter-docs://api/widgets/State/context) → [BuildContext](flutter-docs://api/widgets/BuildContext)
The location in the tree where this widget builds.


[hashCode](flutter-docs://api/dart-core/Object/hashCode) → [int](flutter-docs://api/dart-core/int)
The hash code for this object.


[mounted](flutter-docs://api/widgets/State/mounted) → [bool](flutter-docs://api/dart-core/bool)
Whether this [State](flutter-docs://api/widgets/State) object is currently in a tree.


[runtimeType](flutter-docs://api/dart-core/Object/runtimeType) → [Type](flutter-docs://api/dart-core/Type)
A representation of the runtime type of the object.


[widget](flutter-docs://api/widgets/State/widget) → T
The current configuration.


## Methods

[activate](flutter-docs://api/widgets/State/activate)() → void
Called when this object is reinserted into the tree after having been
removed via [deactivate](flutter-docs://api/widgets/State/deactivate).

[build](flutter-docs://api/widgets/State/build)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [Widget](flutter-docs://api/widgets/Widget)
Describes the part of the user interface represented by this widget.

[deactivate](flutter-docs://api/widgets/State/deactivate)() → void
Called when this object is removed from the tree.

[debugFillProperties](flutter-docs://api/widgets/State/debugFillProperties)([DiagnosticPropertiesBuilder](flutter-docs://api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[didChangeDependencies](flutter-docs://api/widgets/State/didChangeDependencies)() → void
Called when a dependency of this [State](flutter-docs://api/widgets/State) object changes.

[didUpdateWidget](flutter-docs://api/widgets/State/didUpdateWidget)(covariant T oldWidget) → void
Called whenever the widget configuration changes.

[dispose](flutter-docs://api/widgets/State/dispose)() → void
Called when this object is removed from the tree permanently.

[initState](flutter-docs://api/widgets/State/initState)() → void
Called when this object is inserted into the tree.

[noSuchMethod](flutter-docs://api/dart-core/Object/noSuchMethod)([Invocation](flutter-docs://api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[reassemble](flutter-docs://api/widgets/State/reassemble)() → void
Called whenever the application is reassembled during debugging, for
example during hot reload.

[setState](flutter-docs://api/widgets/State/setState)([VoidCallback](flutter-docs://api/dart-ui/VoidCallback) fn) → void
Notify the framework that the internal state of this object has changed.

[toDiagnosticsNode](flutter-docs://api/foundation/Diagnosticable/toDiagnosticsNode)({[String](flutter-docs://api/dart-core/String)? name, [DiagnosticsTreeStyle](flutter-docs://api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](flutter-docs://api/foundation/DiagnosticsNode/toStringDeep).


[toString](flutter-docs://api/foundation/Diagnosticable/toString)({[DiagnosticLevel](flutter-docs://api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](flutter-docs://api/dart-core/String)
A string representation of this object.


[toStringShort](flutter-docs://api/foundation/Diagnosticable/toStringShort)() → [String](flutter-docs://api/dart-core/String)
A brief description of this object, usually just the [runtimeType](flutter-docs://api/dart-core/Object/runtimeType) and the
[hashCode](flutter-docs://api/dart-core/Object/hashCode).


## Operators

[operator ==](flutter-docs://api/dart-core/Object/operator_equals)([Object](flutter-docs://api/dart-core/Object) other) → [bool](flutter-docs://api/dart-core/bool)
The equality operator.
