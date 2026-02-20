# MaterialStateMixin<T extends StatefulWidget> mixin

Mixin for [State](flutter-docs://api/widgets/State) classes that require knowledge of changing [WidgetState](flutter-docs://api/widgets/WidgetState) values for their child widgets.

This mixin does nothing by mere application to a [State](flutter-docs://api/widgets/State) class, but is
helpful when writing `build` methods that include child [InkWell](flutter-docs://api/material/InkWell), [GestureDetector](flutter-docs://api/widgets/GestureDetector), [MouseRegion](flutter-docs://api/widgets/MouseRegion), or [Focus](flutter-docs://api/widgets/Focus) widgets. Instead of manually
creating handlers for each type of user interaction, such [State](flutter-docs://api/widgets/State) classes can
instead provide a `ValueChanged<bool>` function and allow [MaterialStateMixin](flutter-docs://api/material/MaterialStateMixin) to manage the set of active [WidgetState](flutter-docs://api/widgets/WidgetState) s, and the calling of [setState](flutter-docs://api/widgets/State/setState) as necessary.

This example shows how to write a [StatefulWidget](flutter-docs://api/widgets/StatefulWidget) that uses the
[MaterialStateMixin](flutter-docs://api/material/MaterialStateMixin) class to watch [WidgetState](flutter-docs://api/widgets/WidgetState) values.



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
- [State](flutter-docs://api/widgets/State)<T>

1. @[optionalTypeArgs](flutter-docs://api/meta/optionalTypeArgs)

## Properties

[context](flutter-docs://api/material/MaterialStateMixin/context) → [BuildContext](flutter-docs://api/widgets/BuildContext)
The location in the tree where this widget builds.


[hashCode](flutter-docs://api/material/MaterialStateMixin/hashCode) → [int](flutter-docs://api/dart-core/int)
The hash code for this object.


[isDisabled](flutter-docs://api/material/MaterialStateMixin/isDisabled) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.disabled](flutter-docs://api/widgets/WidgetState) to be active.


[isDragged](flutter-docs://api/material/MaterialStateMixin/isDragged) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.dragged](flutter-docs://api/widgets/WidgetState) to be active.


[isErrored](flutter-docs://api/material/MaterialStateMixin/isErrored) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.error](flutter-docs://api/widgets/WidgetState) to be active.


[isFocused](flutter-docs://api/material/MaterialStateMixin/isFocused) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.focused](flutter-docs://api/widgets/WidgetState) to be active.


[isHovered](flutter-docs://api/material/MaterialStateMixin/isHovered) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.hovered](flutter-docs://api/widgets/WidgetState) to be active.


[isPressed](flutter-docs://api/material/MaterialStateMixin/isPressed) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.pressed](flutter-docs://api/widgets/WidgetState) to be active.


[isScrolledUnder](flutter-docs://api/material/MaterialStateMixin/isScrolledUnder) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.scrolledUnder](flutter-docs://api/widgets/WidgetState) to be active.


[isSelected](flutter-docs://api/material/MaterialStateMixin/isSelected) → [bool](flutter-docs://api/dart-core/bool)
Getter for whether this class considers [WidgetState.selected](flutter-docs://api/widgets/WidgetState) to be active.


[materialStates](flutter-docs://api/material/MaterialStateMixin/materialStates) ↔ [Set](flutter-docs://api/dart-core/Set)<[WidgetState](flutter-docs://api/widgets/WidgetState)>
Managed set of active [WidgetState](flutter-docs://api/widgets/WidgetState) values; designed to be passed to
[WidgetStateProperty.resolve](flutter-docs://api/widgets/WidgetStateProperty/resolve) methods.


[mounted](flutter-docs://api/material/MaterialStateMixin/mounted) → [bool](flutter-docs://api/dart-core/bool)
Whether this [State](flutter-docs://api/widgets/State) object is currently in a tree.


[runtimeType](flutter-docs://api/material/MaterialStateMixin/runtimeType) → [Type](flutter-docs://api/dart-core/Type)
A representation of the runtime type of the object.


[widget](flutter-docs://api/material/MaterialStateMixin/widget) → T
The current configuration.


## Methods

[activate](flutter-docs://api/material/MaterialStateMixin/activate)() → void
Called when this object is reinserted into the tree after having been
removed via [deactivate](flutter-docs://api/widgets/State/deactivate).


[addMaterialState](flutter-docs://api/material/MaterialStateMixin/addMaterialState)([WidgetState](flutter-docs://api/widgets/WidgetState) state) → void
Mutator to mark a [WidgetState](flutter-docs://api/widgets/WidgetState) value as active.

[build](flutter-docs://api/material/MaterialStateMixin/build)([BuildContext](flutter-docs://api/widgets/BuildContext) context) → [Widget](flutter-docs://api/widgets/Widget)
Describes the part of the user interface represented by this widget.


[deactivate](flutter-docs://api/material/MaterialStateMixin/deactivate)() → void
Called when this object is removed from the tree.


[debugFillProperties](flutter-docs://api/material/MaterialStateMixin/debugFillProperties)([DiagnosticPropertiesBuilder](flutter-docs://api/foundation/DiagnosticPropertiesBuilder) properties) → void
Add additional properties associated with the node.


[didChangeDependencies](flutter-docs://api/material/MaterialStateMixin/didChangeDependencies)() → void
Called when a dependency of this [State](flutter-docs://api/widgets/State) object changes.


[didUpdateWidget](flutter-docs://api/material/MaterialStateMixin/didUpdateWidget)(covariant T oldWidget) → void
Called whenever the widget configuration changes.


[dispose](flutter-docs://api/material/MaterialStateMixin/dispose)() → void
Called when this object is removed from the tree permanently.


[initState](flutter-docs://api/material/MaterialStateMixin/initState)() → void
Called when this object is inserted into the tree.


[noSuchMethod](flutter-docs://api/material/MaterialStateMixin/noSuchMethod)([Invocation](flutter-docs://api/dart-core/Invocation) invocation) → dynamic
Invoked when a nonexistent method or property is accessed.


[reassemble](flutter-docs://api/material/MaterialStateMixin/reassemble)() → void
Called whenever the application is reassembled during debugging, for
example during hot reload.


[removeMaterialState](flutter-docs://api/material/MaterialStateMixin/removeMaterialState)([WidgetState](flutter-docs://api/widgets/WidgetState) state) → void
Mutator to mark a [WidgetState](flutter-docs://api/widgets/WidgetState) value as inactive.

[setMaterialState](flutter-docs://api/material/MaterialStateMixin/setMaterialState)([WidgetState](flutter-docs://api/widgets/WidgetState) state, [bool](flutter-docs://api/dart-core/bool) isSet) → void
Mutator to mark a [WidgetState](flutter-docs://api/widgets/WidgetState) value as either active or inactive.

[setState](flutter-docs://api/material/MaterialStateMixin/setState)([VoidCallback](flutter-docs://api/dart-ui/VoidCallback) fn) → void
Notify the framework that the internal state of this object has changed.


[toDiagnosticsNode](flutter-docs://api/material/MaterialStateMixin/toDiagnosticsNode)({[String](flutter-docs://api/dart-core/String)? name, [DiagnosticsTreeStyle](flutter-docs://api/foundation/DiagnosticsTreeStyle)? style}) → [DiagnosticsNode](flutter-docs://api/foundation/DiagnosticsNode)
Returns a debug representation of the object that is used by debugging
tools and by [DiagnosticsNode.toStringDeep](flutter-docs://api/foundation/DiagnosticsNode/toStringDeep).


[toString](flutter-docs://api/material/MaterialStateMixin/toString)({[DiagnosticLevel](flutter-docs://api/foundation/DiagnosticLevel) minLevel = DiagnosticLevel.info}) → [String](flutter-docs://api/dart-core/String)
A string representation of this object.


[toStringShort](flutter-docs://api/material/MaterialStateMixin/toStringShort)() → [String](flutter-docs://api/dart-core/String)
A brief description of this object, usually just the [runtimeType](flutter-docs://api/dart-core/Object/runtimeType) and the
[hashCode](flutter-docs://api/dart-core/Object/hashCode).


[updateMaterialState](flutter-docs://api/material/MaterialStateMixin/updateMaterialState)([WidgetState](flutter-docs://api/widgets/WidgetState) key, {[ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>? onChanged}) → [ValueChanged](flutter-docs://api/foundation/ValueChanged)<[bool](flutter-docs://api/dart-core/bool)>
Callback factory which accepts a [WidgetState](flutter-docs://api/widgets/WidgetState) value and returns a
closure to mutate [materialStates](flutter-docs://api/material/MaterialStateMixin/materialStates) and call [setState](flutter-docs://api/widgets/State/setState).

## Operators

[operator ==](flutter-docs://api/material/MaterialStateMixin/operator_equals)([Object](flutter-docs://api/dart-core/Object) other) → [bool](flutter-docs://api/dart-core/bool)
The equality operator.
