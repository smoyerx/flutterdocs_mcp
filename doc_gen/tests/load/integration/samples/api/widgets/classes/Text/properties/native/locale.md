# locale property

[Locale](flutter-docs://api/dart-ui/Locale)? locale


Used to select a font when the same Unicode character can
be rendered differently, depending on the locale.

It's rarely necessary to set this property. By default its value
is inherited from the enclosing app with `Localizations.localeOf(context)`.

See [RenderParagraph.locale](flutter-docs://api/rendering/RenderParagraph/locale) for more information.

## Implementation

```dart
final Locale? locale;
```