# MaterialStateMixin<T extends StatefulWidget> mixin

Mixin for [State](mcp://flutter/api/widgets/State) classes that require knowledge of changing [WidgetState](mcp://flutter/api/widgets/WidgetState) values for their child widgets.

This mixin does nothing by mere application to a [State](mcp://flutter/api/widgets/State) class, but is
helpful when writing `build` methods that include child [InkWell](mcp://flutter/api/material/InkWell), [GestureDetector](mcp://flutter/api/widgets/GestureDetector), [MouseRegion](mcp://flutter/api/widgets/MouseRegion), or [Focus](mcp://flutter/api/widgets/Focus) widgets. Instead of manually
creating handlers for each type of user interaction, such [State](mcp://flutter/api/widgets/State) classes can
instead provide a `ValueChanged<bool>` function and allow [MaterialStateMixin](mcp://flutter/api/material/MaterialStateMixin) to manage the set of active [WidgetState](mcp://flutter/api/widgets/WidgetState) s, and the calling of [setState](mcp://flutter/api/widgets/State/setState) as necessary.

This example shows how to write a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) that uses the
[MaterialStateMixin](mcp://flutter/api/material/MaterialStateMixin) class to watch [WidgetState](mcp://flutter/api/widgets/WidgetState) values.



```dart
class MyWidget extends StatefulWidget {
  const MyWidget({super.key, required this.color, required this.child});

  final WidgetStateColor color;
  final Widget child;

  @override
  State<MyWidget> createState() => MyWidgetState();
}

class MyWidgetState extends State<MyWidget> with MaterialStateMixin<MyWidget> {
  @override
  Widget build(BuildContext context) {
    return InkWell(
      onFocusChange: updateMaterialState(WidgetState.focused),
      child: ColoredBox(
        color: widget.color.resolve(materialStates),
        child: widget.child,
      ),
    );
  }
}
```

Superclass constraints
- [State](mcp://flutter/api/widgets/State)<T>

1. @[optionalTypeArgs](mcp://flutter/api/meta/optionalTypeArgs)

## Properties

[context](mcp://flutter/api/material/MaterialStateMixin/context) → [BuildContext](mcp://flutter/api/widgets/BuildContext)
The location in the tree where this widget builds.


[hashCode](mcp://flutter/api/material/MaterialStateMixin/hashCode) → [int](mcp://flutter/api/dart-core/int)
The hash code for this object.


[isDisabled](mcp://flutter/api/material/MaterialStateMixin/isDisabled) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.disabled](mcp://flutter/api/widgets/WidgetState) to be active.


[isDragged](mcp://flutter/api/material/MaterialStateMixin/isDragged) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.dragged](mcp://flutter/api/widgets/WidgetState) to be active.


[isErrored](mcp://flutter/api/material/MaterialStateMixin/isErrored) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.error](mcp://flutter/api/widgets/WidgetState) to be active.


[isFocused](mcp://flutter/api/material/MaterialStateMixin/isFocused) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.focused](mcp://flutter/api/widgets/WidgetState) to be active.


[isHovered](mcp://flutter/api/material/MaterialStateMixin/isHovered) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.hovered](mcp://flutter/api/widgets/WidgetState) to be active.


[isPressed](mcp://flutter/api/material/MaterialStateMixin/isPressed) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.pressed](mcp://flutter/api/widgets/WidgetState) to be active.


[isScrolledUnder](mcp://flutter/api/material/MaterialStateMixin/isScrolledUnder) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.scrolledUnder](mcp://flutter/api/widgets/WidgetState) to be active.


[isSelected](mcp://flutter/api/material/MaterialStateMixin/isSelected) → [bool](mcp://flutter/api/dart-core/bool)
Getter for whether this class considers [WidgetState.selected](mcp://flutter/api/widgets/WidgetState) to be active.


[materialStates](mcp://flutter/api/material/MaterialStateMixin/materialStates) ↔ [Set](mcp://flutter/api/dart-core/Set)<[WidgetState](mcp://flutter/api/widgets/WidgetState)>
Managed set of active [WidgetState](mcp://flutter/api/widgets/WidgetState) values; designed to be passed to
[WidgetStateProperty.resolve](mcp://flutter/api/widgets/WidgetStateProperty/resolve) methods.


[mounted](mcp://flutter/api/material/MaterialStateMixin/mounted) → [bool](mcp://flutter/api/dart-core/bool)
Whether this [State](mcp://flutter/api/widgets/State) object is currently in a tree.


[runtimeType](mcp://flutter/api/material/MaterialStateMixin/runtimeType) → [Type](mcp://flutter/api/dart-core/Type)
A representation of the runtime type of the object.


[widget](mcp://flutter/api/material/MaterialStateMixin/widget) → T
The current configuration.


## Methods

[activate](mcp://flutter/api/material/MaterialStateMixin/activate)() → void
Called when this object is reinserted into the tree after having been
removed via [deactivate](mcp://flutter/api/widgets/State/deactivate).


[addMaterialState](mcp://flutter/api/material/MaterialStateMixin/addMaterialState)([WidgetState](mcp://flutter/api/widgets/WidgetState) state) → void
Mutator to mark a [WidgetState](mcp://flutter/api/widgets/WidgetState) value as active.

[build](mcp://flutter/api/material/MaterialStateMixin/build)([BuildContext](mcp://flutter/api/widgets/BuildContext) context) → [Widget](mcp://flutter/api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[deactivate](mcp://flutter/api/material/MaterialStateMixin/deactivate)() → void
Called when this object is removed from the tree.


[debugFillProperties](mcp://flutter/api/material/MaterialStateMixin/debugFillProperties)([DiagnosticPropertiesBuilder](mcp://flutter/api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[didChangeDependencies](mcp://flutter/api/material/MaterialStateMixin/didChangeDependencies)() → void
Called when a dependency of this [State](mcp://flutter/api/widgets/State) object changes.


[didUpdateWidget](mcp://flutter/api/material/MaterialStateMixin/didUpdateWidget)(covariant T oldWidget) → void
Called whenever the widget configuration changes.


[dispose](mcp://flutter/api/material/MaterialStateMixin/dispose)() → void
Called when this object is removed from the tree permanently.


[initState](mcp://flutter/api/material/MaterialStateMixin/initState)() → void
Called when this object is inserted into the tree.


[noSuchMethod](mcp://flutter/api/material/MaterialStateMixin/noSuchMethod)([Invocation](mcp://flutter/api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[reassemble](mcp://flutter/api/material/MaterialStateMixin/reassemble)() → void
Called whenever the application is reassembled during debugging, for
example during hot reload.


[removeMaterialState](mcp://flutter/api/material/MaterialStateMixin/removeMaterialState)([WidgetState](mcp://flutter/api/widgets/WidgetState) state) → void
Mutator to mark a [WidgetState](mcp://flutter/api/widgets/WidgetState) value as inactive.

[setMaterialState](mcp://flutter/api/material/MaterialStateMixin/setMaterialState)([WidgetState](mcp://flutter/api/widgets/WidgetState) state, [bool](mcp://flutter/api/dart-core/bool) isSet) → void
Mutator to mark a [WidgetState](mcp://flutter/api/widgets/WidgetState) value as either active or inactive.

[setState](mcp://flutter/api/material/MaterialStateMixin/setState)([VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) fn) → void
Notify the framework that the internal state of this object has changed.


[toDiagnosticsNode](mcp://flutter/api/material/MaterialStateMixin/toDiagnosticsNode)({[String](mcp://flutter/api/dart-core/String)? name, [DiagnosticsTreeStyle](mcp://flutter/api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](mcp://flutter/api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](mcp://flutter/api/foundation/DiagnosticsNode/toStringDeep).


[toString](mcp://flutter/api/material/MaterialStateMixin/toString)({[DiagnosticLevel](mcp://flutter/api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](mcp://flutter/api/dart-core/String)
A string representation of this object.


[toStringShort](mcp://flutter/api/material/MaterialStateMixin/toStringShort)() → [String](mcp://flutter/api/dart-core/String)
A brief description of this object, usually just the [runtimeType](mcp://flutter/api/dart-core/Object/runtimeType) and the
[hashCode](mcp://flutter/api/dart-core/Object/hashCode).


[updateMaterialState](mcp://flutter/api/material/MaterialStateMixin/updateMaterialState)([WidgetState](mcp://flutter/api/widgets/WidgetState) key, {[ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>? onChanged}) → [ValueChanged](mcp://flutter/api/foundation/ValueChanged)<[bool](mcp://flutter/api/dart-core/bool)>
Callback factory which accepts a [WidgetState](mcp://flutter/api/widgets/WidgetState) value and returns a
closure to mutate [materialStates](mcp://flutter/api/material/MaterialStateMixin/materialStates) and call [setState](mcp://flutter/api/widgets/State/setState).

## Operators

[operator ==](mcp://flutter/api/material/MaterialStateMixin/operator_equals)([Object](mcp://flutter/api/dart-core/Object) other) → [bool](mcp://flutter/api/dart-core/bool)
The equality operator.
