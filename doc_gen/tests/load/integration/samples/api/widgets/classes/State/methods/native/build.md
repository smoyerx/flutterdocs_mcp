# build abstract method

@[protected](mcp://flutter/api/meta/protected)
[Widget](mcp://flutter/api/widgets/Widget) build(
[BuildContext](mcp://flutter/api/widgets/BuildContext) context
)

Describes the part of the user interface represented by this widget.

The framework calls this method in a number of different situations. For
example:

- After calling [initState](mcp://flutter/api/widgets/State/initState).
- After calling [didUpdateWidget](mcp://flutter/api/widgets/State/didUpdateWidget).
- After receiving a call to [setState](mcp://flutter/api/widgets/State/setState).
- After a dependency of this [State](mcp://flutter/api/widgets/State) object changes (e.g., an
[InheritedWidget](mcp://flutter/api/widgets/InheritedWidget) referenced by the previous [build](mcp://flutter/api/widgets/State/build) changes).
- After calling [deactivate](mcp://flutter/api/widgets/State/deactivate) and then reinserting the [State](mcp://flutter/api/widgets/State) object into
the tree at another location.


This method can potentially be called in every frame and should not have
any side effects beyond building a widget.

The framework replaces the subtree below this widget with the widget
returned by this method, either by updating the existing subtree or by
removing the subtree and inflating a new subtree, depending on whether the
widget returned by this method can update the root of the existing
subtree, as determined by calling [Widget.canUpdate](mcp://flutter/api/widgets/Widget/canUpdate).

Typically implementations return a newly created constellation of widgets
that are configured with information from this widget's constructor, the
given [BuildContext](mcp://flutter/api/widgets/BuildContext), and the internal state of this [State](mcp://flutter/api/widgets/State) object.

The given [BuildContext](mcp://flutter/api/widgets/BuildContext) contains information about the location in the
tree at which this widget is being built. For example, the context
provides the set of inherited widgets for this location in the tree. The [BuildContext](mcp://flutter/api/widgets/BuildContext) argument is always the same as the `context` property of
this [State](mcp://flutter/api/widgets/State) object and will remain the same for the lifetime of this
object. The [BuildContext](mcp://flutter/api/widgets/BuildContext) argument is provided redundantly here so that
this method matches the signature for a [WidgetBuilder](mcp://flutter/api/widgets/WidgetBuilder).

## Design discussion

### Why is the [build](mcp://flutter/api/widgets/State/build) method on [State](mcp://flutter/api/widgets/State), and not [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget)?

Putting a `Widget build(BuildContext context)` method on [State](mcp://flutter/api/widgets/State) rather
than putting a `Widget build(BuildContext context, State state)` method
on [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) gives developers more flexibility when subclassing [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget).

For example, [AnimatedWidget](mcp://flutter/api/widgets/AnimatedWidget) is a subclass of [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) that
introduces an abstract `Widget build(BuildContext context)` method for its
subclasses to implement. If [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) already had a [build](mcp://flutter/api/widgets/State/build) method
that took a [State](mcp://flutter/api/widgets/State) argument, [AnimatedWidget](mcp://flutter/api/widgets/AnimatedWidget) would be forced to provide
its [State](mcp://flutter/api/widgets/State) object to subclasses even though its [State](mcp://flutter/api/widgets/State) object is an
internal implementation detail of [AnimatedWidget](mcp://flutter/api/widgets/AnimatedWidget).

Conceptually, [StatelessWidget](mcp://flutter/api/widgets/StatelessWidget) could also be implemented as a subclass of [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) in a similar manner. If the [build](mcp://flutter/api/widgets/State/build) method were on [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) rather than [State](mcp://flutter/api/widgets/State), that would not be possible anymore.

Putting the [build](mcp://flutter/api/widgets/State/build) function on [State](mcp://flutter/api/widgets/State) rather than [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) also
helps avoid a category of bugs related to closures implicitly capturing `this`. If you defined a closure in a [build](mcp://flutter/api/widgets/State/build) function on a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget), that closure would implicitly capture `this`, which is
the current widget instance, and would have the (immutable) fields of that
instance in scope:

```dart
// (this is not valid Flutter code)
class MyButton extends StatefulWidgetX {
  MyButton({super.key, required this.color});

  final Color color;

  @override
  Widget build(BuildContext context, State state) {
    return SpecialWidget(
      handler: () { print('color: $color'); },
    );
  }
}

```
For example, suppose the parent builds `MyButton` with `color` being blue,
the `$color` in the print function refers to blue, as expected. Now,
suppose the parent rebuilds `MyButton` with green. The closure created by
the first build still implicitly refers to the original widget and the `$color` still prints blue even through the widget has been updated to
green; should that closure outlive its widget, it would print outdated
information.

In contrast, with the [build](mcp://flutter/api/widgets/State/build) function on the [State](mcp://flutter/api/widgets/State) object, closures
created during [build](mcp://flutter/api/widgets/State/build) implicitly capture the [State](mcp://flutter/api/widgets/State) instance instead of
the widget instance:

```dart
class MyButton extends StatefulWidget {
  const MyButton({super.key, this.color = Colors.teal});

  final Color color;
  // ...
}

class MyButtonState extends State<MyButton> {
  // ...
  @override
  Widget build(BuildContext context) {
    return SpecialWidget(
      handler: () { print('color: ${widget.color}'); },
    );
  }
}

```
Now when the parent rebuilds `MyButton` with green, the closure created by
the first build still refers to [State](mcp://flutter/api/widgets/State) object, which is preserved across
rebuilds, but the framework has updated that [State](mcp://flutter/api/widgets/State) object's [widget](mcp://flutter/api/widgets/State/widget) property to refer to the new `MyButton` instance and `${widget.color}` prints green, as expected.

See also:

- [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget), which contains the discussion on performance considerations.


## Implementation

```dart
@protected
Widget build(BuildContext context);
```