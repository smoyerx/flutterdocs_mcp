# activate method

1. @[protected](mcp://flutter/api/meta/protected)
2. @[mustCallSuper](mcp://flutter/api/meta/mustCallSuper)

voidactivate()


Called when this object is reinserted into the tree after having been
removed via [deactivate](mcp://flutter/api/widgets/State/deactivate).

In most cases, after a [State](mcp://flutter/api/widgets/State) object has been deactivated, it is *not* reinserted into the tree, and its [dispose](mcp://flutter/api/widgets/State/dispose) method will be called to
signal that it is ready to be garbage collected.

In some cases, however, after a [State](mcp://flutter/api/widgets/State) object has been deactivated, the
framework will reinsert it into another part of the tree (e.g., if the
subtree containing this [State](mcp://flutter/api/widgets/State) object is grafted from one location in
the tree to another due to the use of a [GlobalKey](mcp://flutter/api/widgets/GlobalKey)). If that happens,
the framework will call [activate](mcp://flutter/api/widgets/State/activate) to give the [State](mcp://flutter/api/widgets/State) object a chance to
reacquire any resources that it released in [deactivate](mcp://flutter/api/widgets/State/deactivate). It will then
also call [build](mcp://flutter/api/widgets/State/build) to give the object a chance to adapt to its new
location in the tree. If the framework does reinsert this subtree, it
will do so before the end of the animation frame in which the subtree was
removed from the tree. For this reason, [State](mcp://flutter/api/widgets/State) objects can defer
releasing most resources until the framework calls their [dispose](mcp://flutter/api/widgets/State/dispose) method.

The framework does not call this method the first time a [State](mcp://flutter/api/widgets/State) object
is inserted into the tree. Instead, the framework calls [initState](mcp://flutter/api/widgets/State/initState) in
that situation.

Implementations of this method should start with a call to the inherited
method, as in `super.activate()`.

See also:

- [Element.activate](mcp://flutter/api/widgets/Element/activate), the corresponding method when an element
transitions from the "inactive" to the "active" lifecycle state.


## Implementation

```dart
@protected
@mustCallSuper
void activate() {}
```