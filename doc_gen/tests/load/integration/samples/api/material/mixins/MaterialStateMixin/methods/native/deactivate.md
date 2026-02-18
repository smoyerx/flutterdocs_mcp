# deactivate method

1. @[protected](mcp://flutter/api/meta/protected)
2. @[mustCallSuper](mcp://flutter/api/meta/mustCallSuper)

voiddeactivate()


Called when this object is removed from the tree.

The framework calls this method whenever it removes this [State](mcp://flutter/api/widgets/State) object
from the tree. In some cases, the framework will reinsert the [State](mcp://flutter/api/widgets/State) object into another part of the tree (e.g., if the subtree containing this [State](mcp://flutter/api/widgets/State) object is grafted from one location in the tree to another due to
the use of a [GlobalKey](mcp://flutter/api/widgets/GlobalKey)). If that happens, the framework will call [activate](mcp://flutter/api/widgets/State/activate) to give the [State](mcp://flutter/api/widgets/State) object a chance to reacquire any resources
that it released in [deactivate](mcp://flutter/api/widgets/State/deactivate). It will then also call [build](mcp://flutter/api/widgets/State/build) to give
the [State](mcp://flutter/api/widgets/State) object a chance to adapt to its new location in the tree. If
the framework does reinsert this subtree, it will do so before the end of
the animation frame in which the subtree was removed from the tree. For
this reason, [State](mcp://flutter/api/widgets/State) objects can defer releasing most resources until the
framework calls their [dispose](mcp://flutter/api/widgets/State/dispose) method.

Subclasses should override this method to clean up any links between
this object and other elements in the tree (e.g. if you have provided an
ancestor with a pointer to a descendant's [RenderObject](mcp://flutter/api/rendering/RenderObject)).

Implementations of this method should end with a call to the inherited
method, as in `super.deactivate()`.

See also:

- [dispose](mcp://flutter/api/widgets/State/dispose), which is called after [deactivate](mcp://flutter/api/widgets/State/deactivate) if the widget is removed
from the tree permanently.


## Implementation

```dart
@protected
@mustCallSuper
void deactivate() {}
```