# build method

@[override](mcp://flutter/api/dart-core/override)
[Widget](mcp://flutter/api/widgets/Widget) build(
[BuildContext](mcp://flutter/api/widgets/BuildContext) context
)


Describes the part of the user interface represented by this widget.

The framework calls this method when this widget is inserted into the tree
in a given [BuildContext](mcp://flutter/api/widgets/BuildContext) and when the dependencies of this widget change
(e.g., an [InheritedWidget](mcp://flutter/api/widgets/InheritedWidget) referenced by this widget changes). This
method can potentially be called in every frame and should not have any side
effects beyond building a widget.

The framework replaces the subtree below this widget with the widget
returned by this method, either by updating the existing subtree or by
removing the subtree and inflating a new subtree, depending on whether the
widget returned by this method can update the root of the existing
subtree, as determined by calling [Widget.canUpdate](mcp://flutter/api/widgets/Widget/canUpdate).

Typically implementations return a newly created constellation of widgets
that are configured with information from this widget's constructor and
from the given [BuildContext](mcp://flutter/api/widgets/BuildContext).

The given [BuildContext](mcp://flutter/api/widgets/BuildContext) contains information about the location in the
tree at which this widget is being built. For example, the context
provides the set of inherited widgets for this location in the tree. A
given widget might be built with multiple different [BuildContext](mcp://flutter/api/widgets/BuildContext) arguments over time if the widget is moved around the tree or if the
widget is inserted into the tree in multiple places at once.

The implementation of this method must only depend on:

- the fields of the widget, which themselves must not change over time,
and
- any ambient state obtained from the `context` using
[BuildContext.dependOnInheritedWidgetOfExactType](mcp://flutter/api/widgets/BuildContext/dependOnInheritedWidgetOfExactType).


If a widget's [build](mcp://flutter/api/widgets/Text/build) method is to depend on anything else, use a [StatefulWidget](mcp://flutter/api/widgets/StatefulWidget) instead.

See also:

- [StatelessWidget](mcp://flutter/api/widgets/StatelessWidget), which contains the discussion on performance considerations.


## Implementation

```dart
@override
Widget build(BuildContext context) {
  final DefaultTextStyle defaultTextStyle = DefaultTextStyle.of(context);
  TextStyle? effectiveTextStyle = style;
  if (style == null || style!.inherit) {
    effectiveTextStyle = defaultTextStyle.style.merge(style);
  }
  if (MediaQuery.boldTextOf(context)) {
    effectiveTextStyle = effectiveTextStyle!.merge(const TextStyle(fontWeight: FontWeight.bold));
  }
  final SelectionRegistrar? registrar = SelectionContainer.maybeOf(context);
  final TextScaler textScaler = switch ((this.textScaler, textScaleFactor)) {
    (final TextScaler textScaler, _) => textScaler,
    // For unmigrated apps, fall back to textScaleFactor.
    (null, final double textScaleFactor) => TextScaler.linear(textScaleFactor),
    (null, null) => MediaQuery.textScalerOf(context),
  };
  late Widget result;
  if (registrar != null) {
    result = MouseRegion(
      cursor: DefaultSelectionStyle.of(context).mouseCursor ?? SystemMouseCursors.text,
      child: _SelectableTextContainer(
        textAlign: textAlign ?? defaultTextStyle.textAlign ?? TextAlign.start,
        textDirection:
            textDirection, // RichText uses Directionality.of to obtain a default if this is null.
        locale:
            locale, // RichText uses Localizations.localeOf to obtain a default if this is null
        softWrap: softWrap ?? defaultTextStyle.softWrap,
        overflow: overflow ?? effectiveTextStyle?.overflow ?? defaultTextStyle.overflow,
        textScaler: textScaler,
        maxLines: maxLines ?? defaultTextStyle.maxLines,
        strutStyle: strutStyle,
        textWidthBasis: textWidthBasis ?? defaultTextStyle.textWidthBasis,
        textHeightBehavior:
            textHeightBehavior ??
            defaultTextStyle.textHeightBehavior ??
            DefaultTextHeightBehavior.maybeOf(context),
        selectionColor:
            selectionColor ??
            DefaultSelectionStyle.of(context).selectionColor ??
            DefaultSelectionStyle.defaultColor,
        text: TextSpan(
          style: effectiveTextStyle,
          text: data,
          locale: locale,
          children: textSpan != null ? <InlineSpan>[textSpan!] : null,
        ),
      ),
    );
  } else {
    result = RichText(
      textAlign: textAlign ?? defaultTextStyle.textAlign ?? TextAlign.start,
      textDirection:
          textDirection, // RichText uses Directionality.of to obtain a default if this is null.
      locale: locale, // RichText uses Localizations.localeOf to obtain a default if this is null
      softWrap: softWrap ?? defaultTextStyle.softWrap,
      overflow: overflow ?? effectiveTextStyle?.overflow ?? defaultTextStyle.overflow,
      textScaler: textScaler,
      maxLines: maxLines ?? defaultTextStyle.maxLines,
      strutStyle: strutStyle,
      textWidthBasis: textWidthBasis ?? defaultTextStyle.textWidthBasis,
      textHeightBehavior:
          textHeightBehavior ??
          defaultTextStyle.textHeightBehavior ??
          DefaultTextHeightBehavior.maybeOf(context),
      selectionColor:
          selectionColor ??
          DefaultSelectionStyle.of(context).selectionColor ??
          DefaultSelectionStyle.defaultColor,
      text: TextSpan(
        style: effectiveTextStyle,
        text: data,
        locale: locale,
        children: textSpan != null ? <InlineSpan>[textSpan!] : null,
      ),
    );
  }
  if (semanticsLabel != null || semanticsIdentifier != null) {
    result = Semantics(
      textDirection: textDirection,
      label: semanticsLabel,
      identifier: semanticsIdentifier,
      child: ExcludeSemantics(excluding: semanticsLabel != null, child: result),
    );
  }
  return result;
}
```