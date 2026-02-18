# State<T extends StatefulWidget> class [abstract](https://dart.dev/language/class-modifiers#abstract "This type can not be directly constructed.")

The logic and internal state for a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget).

State is information that (1) can be read synchronously when the widget is
built and (2) might change during the lifetime of the widget. It is the
responsibility of the widget implementer to ensure that the [State](mcp://flutter/api/widgets/State) is
promptly notified when such state changes, using [State.setState](mcp://flutter/api/widgets/State/setState).

[State](mcp://flutter/api/widgets/State) objects are created by the framework by calling the [StatefulWidget.createState](mcp://flutter/api/widgets/StatefulWidget/createState) method when inflating a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) to
insert it into the tree. Because a given [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) instance can be
inflated multiple times (e.g., the widget is incorporated into the tree in
multiple places at once), there might be more than one [State](mcp://flutter/api/widgets/State) object
associated with a given [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) instance. Similarly, if a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) is removed from the tree and later inserted in to the tree
again, the framework will call [StatefulWidget.createState](mcp://flutter/api/widgets/StatefulWidget/createState) again to create
a fresh [State](mcp://flutter/api/widgets/State) object, simplifying the lifecycle of [State](mcp://flutter/api/widgets/State) objects.

[State](mcp://flutter/api/widgets/State) objects have the following lifecycle:

- The framework creates a [State](mcp://flutter/api/widgets/State) object by calling
[StatefulWidget.createState](mcp://flutter/api/widgets/StatefulWidget/createState).
- The newly created [State](mcp://flutter/api/widgets/State) object is associated with a [BuildContext](mcp://flutter/api/widgets/BuildContext).
This association is permanent: the [State](mcp://flutter/api/widgets/State) object will never change its
[BuildContext](mcp://flutter/api/widgets/BuildContext). However, the [BuildContext](mcp://flutter/api/widgets/BuildContext) itself can be moved around
the tree along with its subtree. At this point, the [State](mcp://flutter/api/widgets/State) object is
considered [mounted](mcp://flutter/api/widgets/State/mounted).
- The framework calls [initState](mcp://flutter/api/widgets/State/initState). Subclasses of [State](mcp://flutter/api/widgets/State) should override
[initState](mcp://flutter/api/widgets/State/initState) to perform one-time initialization that depends on the
[BuildContext](mcp://flutter/api/widgets/BuildContext) or the widget, which are available as the [context](mcp://flutter/api/widgets/State/context) and
[widget](mcp://flutter/api/widgets/State/widget) properties, respectively, when the [initState](mcp://flutter/api/widgets/State/initState) method is
called.
- The framework calls [didChangeDependencies](mcp://flutter/api/widgets/State/didChangeDependencies). Subclasses of [State](mcp://flutter/api/widgets/State) should
override [didChangeDependencies](mcp://flutter/api/widgets/State/didChangeDependencies) to perform initialization involving
[InheritedWidget](mcp://flutter/api/widgets/InheritedWidget) s. If [BuildContext.dependOnInheritedWidgetOfExactType](mcp://flutter/api/widgets/BuildContext/dependOnInheritedWidgetOfExactType) is
called, the [didChangeDependencies](mcp://flutter/api/widgets/State/didChangeDependencies) method will be called again if the
inherited widgets subsequently change or if the widget moves in the tree.
- At this point, the [State](mcp://flutter/api/widgets/State) object is fully initialized and the framework
might call its [build](mcp://flutter/api/widgets/State/build) method any number of times to obtain a
description of the user interface for this subtree. [State](mcp://flutter/api/widgets/State) objects can
spontaneously request to rebuild their subtree by calling their
[setState](mcp://flutter/api/widgets/State/setState) method, which indicates that some of their internal state
has changed in a way that might impact the user interface in this
subtree.
- During this time, a parent widget might rebuild and request that this
location in the tree update to display a new widget with the same
[runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) and [Widget.key](mcp://flutter/api/widgets/Widget/key). When this happens, the framework will
update the [widget](mcp://flutter/api/widgets/State/widget) property to refer to the new widget and then call the
[didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget) method with the previous widget as an argument. [State](mcp://flutter/api/widgets/State) objects should override [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget) to respond to changes in their
associated widget (e.g., to start implicit animations). The framework
always calls [build](mcp://flutter/api/widgets/State/build) after calling [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget), which means any
calls to [setState](mcp://flutter/api/widgets/State/setState) in [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget) are redundant. (See also the
discussion at [Element.rebuild](mcp://flutter/api/widgets/Element/rebuild).)
- During development, if a hot reload occurs (whether initiated from the
command line `flutter` tool by pressing `r`, or from an IDE), the
[reassemble](mcp://flutter/api/widgets/State/reassemble) method is called. This provides an opportunity to
reinitialize any data that was prepared in the [initState](mcp://flutter/api/widgets/State/initState) method.
- If the subtree containing the [State](mcp://flutter/api/widgets/State) object is removed from the tree
(e.g., because the parent built a widget with a different [runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) or [Widget.key](mcp://flutter/api/widgets/Widget/key)), the framework calls the [deactivate](mcp://flutter/api/widgets/State/deactivate) method. Subclasses
should override this method to clean up any links between this object
and other elements in the tree (e.g. if you have provided an ancestor
with a pointer to a descendant's [RenderObject](mcp://flutter/api/rendering/RenderObject)).
- At this point, the framework might reinsert this subtree into another
part of the tree. If that happens, the framework will ensure that it
calls [build](mcp://flutter/api/widgets/State/build) to give the [State](mcp://flutter/api/widgets/State) object a chance to adapt to its new
location in the tree. If the framework does reinsert this subtree, it
will do so before the end of the animation frame in which the subtree was
removed from the tree. For this reason, [State](mcp://flutter/api/widgets/State) objects can defer
releasing most resources until the framework calls their [dispose](mcp://flutter/api/widgets/State/dispose) method.
- If the framework does not reinsert this subtree by the end of the current
animation frame, the framework will call [dispose](mcp://flutter/api/widgets/State/dispose), which indicates that
this [State](mcp://flutter/api/widgets/State) object will never build again. Subclasses should override
this method to release any resources retained by this object (e.g.,
stop any active animations).
- After the framework calls [dispose](mcp://flutter/api/widgets/State/dispose), the [State](mcp://flutter/api/widgets/State) object is considered
unmounted and the [mounted](mcp://flutter/api/widgets/State/mounted) property is false. It is an error to call
[setState](mcp://flutter/api/widgets/State/setState) at this point. This stage of the lifecycle is terminal: there
is no way to remount a [State](mcp://flutter/api/widgets/State) object that has been disposed.


See also:

- [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget), where the current configuration of a [State](mcp://flutter/api/widgets/State) is hosted,
and whose documentation has sample code for [State](mcp://flutter/api/widgets/State).
- [StatelessWidget](mcp://flutter/api/widgets/StatelessWidget), for widgets that always build the same way given a
particular configuration and ambient state.
- [InheritedWidget](mcp://flutter/api/widgets/InheritedWidget), for widgets that introduce ambient state that can
be read by descendant widgets.
- [Widget](mcp://flutter/api/widgets/Widget), for an overview of widgets in general.


Mixed-in types
- [Diagnosticable](mcp://flutter/api/foundation/Diagnosticable)

Implementers
- [AnimatedGridState](mcp://flutter/api/widgets/AnimatedGridState)
- [AnimatedListState](mcp://flutter/api/widgets/AnimatedListState)
- [AutofillGroupState](mcp://flutter/api/widgets/AutofillGroupState)
- [AutomaticKeepAliveClientMixin](mcp://flutter/api/widgets/AutomaticKeepAliveClientMixin)
- [DrawerControllerState](mcp://flutter/api/material/DrawerControllerState)
- [EditableTextState](mcp://flutter/api/widgets/EditableTextState)
- [FormFieldState](mcp://flutter/api/widgets/FormFieldState)
- [FormState](mcp://flutter/api/widgets/FormState)
- [ImplicitlyAnimatedWidgetState](mcp://flutter/api/widgets/ImplicitlyAnimatedWidgetState)
- [MaterialStateMixin](mcp://flutter/api/material/MaterialStateMixin)
- [NavigatorState](mcp://flutter/api/widgets/NavigatorState)
- [NestedScrollViewState](mcp://flutter/api/widgets/NestedScrollViewState)
- [OverlayState](mcp://flutter/api/widgets/OverlayState)
- [PaginatedDataTableState](mcp://flutter/api/material/PaginatedDataTableState)
- [PopupMenuButtonState](mcp://flutter/api/material/PopupMenuButtonState)
- [PopupMenuItemState](mcp://flutter/api/material/PopupMenuItemState)
- [RawGestureDetectorState](mcp://flutter/api/widgets/RawGestureDetectorState)
- [RawScrollbarState](mcp://flutter/api/widgets/RawScrollbarState)
- [RefreshIndicatorState](mcp://flutter/api/material/RefreshIndicatorState)
- [ReorderableListState](mcp://flutter/api/widgets/ReorderableListState)
- [RestorationMixin](mcp://flutter/api/widgets/RestorationMixin)
- [ScaffoldMessengerState](mcp://flutter/api/material/ScaffoldMessengerState)
- [ScaffoldState](mcp://flutter/api/material/ScaffoldState)
- [ScrollableState](mcp://flutter/api/widgets/ScrollableState)
- [ScrollNotificationObserverState](mcp://flutter/api/widgets/ScrollNotificationObserverState)
- [SegmentedButtonState](mcp://flutter/api/material/SegmentedButtonState)
- [SelectableRegionState](mcp://flutter/api/widgets/SelectableRegionState)
- [SelectionAreaState](mcp://flutter/api/material/SelectionAreaState)
- [SingleTickerProviderStateMixin](mcp://flutter/api/widgets/SingleTickerProviderStateMixin)
- [SliverAnimatedGridState](mcp://flutter/api/widgets/SliverAnimatedGridState)
- [SliverAnimatedListState](mcp://flutter/api/widgets/SliverAnimatedListState)
- [SliverReorderableListState](mcp://flutter/api/widgets/SliverReorderableListState)
- [TickerProviderStateMixin](mcp://flutter/api/widgets/TickerProviderStateMixin)
- [TooltipState](mcp://flutter/api/material/TooltipState)
- [TwoDimensionalScrollableState](mcp://flutter/api/widgets/TwoDimensionalScrollableState)
- [UndoHistoryState](mcp://flutter/api/widgets/UndoHistoryState)

Annotations
- @[optionalTypeArgs](mcp://flutter/api/meta/optionalTypeArgs)

## Constructors

[State](mcp://flutter/api/widgets/State/State)()

## Properties

[context](mcp://flutter/api/widgets/State/context) → [BuildContext](mcp://flutter/api/widgets/BuildContext)
The location in the tree where this widget builds.


[hashCode](mcp://flutter/api/dart-core/Object/hashCode) → [int](mcp://flutter/api/dart-core/int)
The hash code for this object.


[mounted](mcp://flutter/api/widgets/State/mounted) → [bool](mcp://flutter/api/dart-core/bool)
Whether this [State](mcp://flutter/api/widgets/State) object is currently in a tree.


[runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) → [Type](mcp://flutter/api/dart-core/Type)
A representation of the runtime type of the object.


[widget](mcp://flutter/api/widgets/State/widget) → T
The current configuration.


## Methods

[activate](mcp://flutter/api/widgets/State/activate)() → void
Called when this object is reinserted into the tree after having been
removed via [deactivate](mcp://flutter/api/widgets/State/deactivate).

[build](mcp://flutter/api/widgets/State/build)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [Widget](mcp://flutter/api/widgets/Widget)
Describes the part of the user interface represented by this widget.

[deactivate](mcp://flutter/api/widgets/State/deactivate)() → void
Called when this object is removed from the tree.

[debugFillProperties](mcp://flutter/api/widgets/State/debugFillProperties)([DiagnosticPropertiesBuilder](mcp://flutter/api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[didChangeDependencies](mcp://flutter/api/widgets/State/didChangeDependencies)() → void
Called when a dependency of this [State](mcp://flutter/api/widgets/State) object changes.

[didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget)(covariant T oldWidget) → void
Called whenever the widget configuration changes.

[dispose](mcp://flutter/api/widgets/State/dispose)() → void
Called when this object is removed from the tree permanently.

[initState](mcp://flutter/api/widgets/State/initState)() → void
Called when this object is inserted into the tree.

[noSuchMethod](mcp://flutter/api/dart-core/Object/noSuchMethod)([Invocation](mcp://flutter/api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[reassemble](mcp://flutter/api/widgets/State/reassemble)() → void
Called whenever the application is reassembled during debugging, for
example during hot reload.

[setState](mcp://flutter/api/widgets/State/setState)([VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) fn) → void
Notify the framework that the internal state of this object has changed.

[toDiagnosticsNode](mcp://flutter/api/foundation/Diagnosticable/toDiagnosticsNode)({[String](mcp://flutter/api/dart-core/String)? name, [DiagnosticsTreeStyle](mcp://flutter/api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](mcp://flutter/api/foundation/DiagnosticsNode/toStringDeep).


[toString](mcp://flutter/api/foundation/Diagnosticable/toString)({[DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](mcp://flutter/api/dart-core/String)
A string representation of this object.


[toStringShort](mcp://flutter/api/foundation/Diagnosticable/toStringShort)() → [String](mcp://flutter/api/dart-core/String)
A brief description of this object, usually just the [runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) and the
[hashCode](mcp://flutter/api/dart-core/Object/hashCode).


## Operators

[operator ==](mcp://flutter/api/dart-core/Object/operator_equals)([Object](mcp://flutter/api/dart-core/Object) other) → [bool](mcp://flutter/api/dart-core/bool)
The equality operator.
