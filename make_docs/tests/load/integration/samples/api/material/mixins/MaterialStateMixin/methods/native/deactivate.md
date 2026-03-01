# deactivate method

1. @[protected](flutter-docs://api/meta/protected)
2. @[mustCallSuper](flutter-docs://api/meta/mustCallSuper)

void deactivate()


Called when this object is removed from the tree.

The framework calls this method whenever it removes this [State](flutter-docs://api/widgets/State) object
from the tree. In some cases, the framework will reinsert the [State](flutter-docs://api/widgets/State) object into another part of the tree (e.g., if the subtree containing this [State](flutter-docs://api/widgets/State) object is grafted from one location in the tree to another due to
the use of a [GlobalKey](flutter-docs://api/widgets/GlobalKey)). If that happens, the framework will call [activate](flutter-docs://api/widgets/State/activate) to give the [State](flutter-docs://api/widgets/State) object a chance to reacquire any resources
that it released in [deactivate](flutter-docs://api/widgets/State/deactivate). It will then also call [build](flutter-docs://api/widgets/State/build) to give
the [State](flutter-docs://api/widgets/State) object a chance to adapt to its new location in the tree. If
the framework does reinsert this subtree, it will do so before the end of
the animation frame in which the subtree was removed from the tree. For
this reason, [State](flutter-docs://api/widgets/State) objects can defer releasing most resources until the
framework calls their [dispose](flutter-docs://api/widgets/State/dispose) method.

Subclasses should override this method to clean up any links between
this object and other elements in the tree (e.g. if you have provided an
ancestor with a pointer to a descendant's [RenderObject](flutter-docs://api/rendering/RenderObject)).

Implementations of this method should end with a call to the inherited
method, as in `super.deactivate()`.

See also:

- [dispose](flutter-docs://api/widgets/State/dispose), which is called after [deactivate](flutter-docs://api/widgets/State/deactivate) if the widget is removed
from the tree permanently.


## Implementation

```dart
@protected
@mustCallSuper
void deactivate() {}
```