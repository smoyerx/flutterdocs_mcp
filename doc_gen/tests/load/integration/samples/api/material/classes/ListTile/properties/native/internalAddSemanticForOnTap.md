# internalAddSemanticForOnTap property

[bool](mcp://flutter/api/dart-core/bool) internalAddSemanticForOnTap


Whether to add button:true to the semantics if onTap is provided.
This is a temporary flag to help changing the behavior of ListTile onTap semantics.

## Implementation

```dart
// TODO(hangyujin): Remove this flag after fixing related g3 tests and flipping
// the default value to true.
final bool internalAddSemanticForOnTap;
```