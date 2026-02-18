# setState method

@[protected](mcp://flutter/api/meta/protected)
voidsetState(
[VoidCallback](mcp://flutter/api/dart-ui/VoidCallback) fn
)


Notify the framework that the internal state of this object has changed.

Whenever you change the internal state of a [State](mcp://flutter/api/widgets/State) object, make the
change in a function that you pass to [setState](mcp://flutter/api/widgets/State/setState):

```dart
setState(() { _myState = newValue; });

```
The provided callback is immediately called synchronously. It must not
return a future (the callback cannot be `async`), since then it would be
unclear when the state was actually being set.

Calling [setState](mcp://flutter/api/widgets/State/setState) notifies the framework that the internal state of this
object has changed in a way that might impact the user interface in this
subtree, which causes the framework to schedule a [build](mcp://flutter/api/widgets/State/build) for this [State](mcp://flutter/api/widgets/State) object.

If you just change the state directly without calling [setState](mcp://flutter/api/widgets/State/setState), the
framework might not schedule a [build](mcp://flutter/api/widgets/State/build) and the user interface for this
subtree might not be updated to reflect the new state.

Generally it is recommended that the [setState](mcp://flutter/api/widgets/State/setState) method only be used to
wrap the actual changes to the state, not any computation that might be
associated with the change. For example, here a value used by the [build](mcp://flutter/api/widgets/State/build) function is incremented, and then the change is written to disk, but only
the increment is wrapped in the [setState](mcp://flutter/api/widgets/State/setState):

```dart
Future<void> _incrementCounter() async {
  setState(() {
    _counter++;
  });
  Directory directory = await getApplicationDocumentsDirectory(); // from path_provider package
  final String dirName = directory.path;
  await File('$dirName/counter.txt').writeAsString('$_counter');
}

```
Sometimes, the changed state is in some other object not owned by the
widget [State](mcp://flutter/api/widgets/State), but the widget nonetheless needs to be updated to react to
the new state. This is especially common with [Listenable](mcp://flutter/api/foundation/Listenable) s, such as [AnimationController](mcp://flutter/api/animation/AnimationController) s.

In such cases, it is good practice to leave a comment in the callback
passed to [setState](mcp://flutter/api/widgets/State/setState) that explains what state changed:

```dart
void _update() {
  setState(() { /* The animation changed. */ });
}
//...
animation.addListener(_update);

```
It is an error to call this method after the framework calls [dispose](mcp://flutter/api/widgets/State/dispose).
You can determine whether it is legal to call this method by checking
whether the [mounted](mcp://flutter/api/widgets/State/mounted) property is true. That said, it is better practice
to cancel whatever work might trigger the [setState](mcp://flutter/api/widgets/State/setState) rather than merely
checking for [mounted](mcp://flutter/api/widgets/State/mounted) before calling [setState](mcp://flutter/api/widgets/State/setState), as otherwise CPU cycles
will be wasted.

## Design discussion

The original version of this API was a method called `markNeedsBuild`, for
consistency with [RenderObject.markNeedsLayout](mcp://flutter/api/rendering/RenderObject/markNeedsLayout), [RenderObject.markNeedsPaint](mcp://flutter/api/rendering/RenderObject/markNeedsPaint), *et al*.

However, early user testing of the Flutter framework revealed that people
would call `markNeedsBuild()` much more often than necessary. Essentially,
people used it like a good luck charm, any time they weren't sure if they
needed to call it, they would call it, just in case.

Naturally, this led to performance issues in applications.

When the API was changed to take a callback instead, this practice was
greatly reduced. One hypothesis is that prompting developers to actually
update their state in a callback caused developers to think more carefully
about what exactly was being updated, and thus improved their understanding
of the appropriate times to call the method.

In practice, the [setState](mcp://flutter/api/widgets/State/setState) method's implementation is trivial: it calls
the provided callback synchronously, then calls [Element.markNeedsBuild](mcp://flutter/api/widgets/Element/markNeedsBuild).

## Performance considerations

There is minimal *direct* overhead to calling this function, and as it is
expected to be called at most once per frame, the overhead is irrelevant
anyway. Nonetheless, it is best to avoid calling this function redundantly
(e.g. in a tight loop), as it does involve creating a closure and calling
it. The method is idempotent, there is no benefit to calling it more than
once per [State](mcp://flutter/api/widgets/State) per frame.

The *indirect* cost of causing this function, however, is high: it causes
the widget to rebuild, possibly triggering rebuilds for the entire subtree
rooted at this widget, and further triggering a relayout and repaint of
the entire corresponding [RenderObject](mcp://flutter/api/rendering/RenderObject) subtree.

For this reason, this method should only be called when the [build](mcp://flutter/api/widgets/State/build) method
will, as a result of whatever state change was detected, change its result
meaningfully.

See also:

- [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget), the API documentation for which has a section on
performance considerations that are relevant here.


## Implementation

```dart
@protected
void setState(VoidCallback fn) {
  assert(() {
    if (_debugLifecycleState == _StateLifecycle.defunct) {
      throw FlutterError.fromParts(<DiagnosticsNode>[
        ErrorSummary('setState() called after dispose(): $this'),
        ErrorDescription(
          'This error happens if you call setState() on a State object for a widget that '
          'no longer appears in the widget tree (e.g., whose parent widget no longer '
          'includes the widget in its build). This error can occur when code calls '
          'setState() from a timer or an animation callback.',
        ),
        ErrorHint(
          'The preferred solution is '
          'to cancel the timer or stop listening to the animation in the dispose() '
          'callback. Another solution is to check the "mounted" property of this '
          'object before calling setState() to ensure the object is still in the '
          'tree.',
        ),
        ErrorHint(
          'This error might indicate a memory leak if setState() is being called '
          'because another object is retaining a reference to this State object '
          'after it has been removed from the tree. To avoid memory leaks, '
          'consider breaking the reference to this object during dispose().',
        ),
      ]);
    }
    if (_debugLifecycleState == _StateLifecycle.created && !mounted) {
      throw FlutterError.fromParts(<DiagnosticsNode>[
        ErrorSummary('setState() called in constructor: $this'),
        ErrorHint(
          'This happens when you call setState() on a State object for a widget that '
          "hasn't been inserted into the widget tree yet. It is not necessary to call "
          'setState() in the constructor, since the state is already assumed to be dirty '
          'when it is initially created.',
        ),
      ]);
    }
    return true;
  }());
  final Object? result = fn() as dynamic;
  assert(() {
    if (result is Future) {
      throw FlutterError.fromParts(<DiagnosticsNode>[
        ErrorSummary('setState() callback argument returned a Future.'),
        ErrorDescription(
          'The setState() method on $this was called with a closure or method that '
          'returned a Future. Maybe it is marked as "async".',
        ),
        ErrorHint(
          'Instead of performing asynchronous work inside a call to setState(), first '
          'execute the work (without updating the widget state), and then synchronously '
          'update the state inside a call to setState().',
        ),
      ]);
    }
    // We ignore other types of return values so that you can do things like:
    //   setState(() => x = 3);
    return true;
  }());
  _element!.markNeedsBuild();
}
```