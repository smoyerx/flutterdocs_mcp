---
name: flutterdocs-usage
description: 'Use when writing Flutter or Dart code, or answering questions about the Flutter or Dart API. Provides step-by-step guidance for using the flutterdocs MCP tools to look up accurate, version-grounded API documentation. Use when: generating Flutter widget code or Dart class usage; verifying constructor signatures, named parameters, or default values before writing code; answering questions about Flutter widget properties, methods, or constants; discovering the right widget or class for a task; checking any Flutter or Dart SDK API detail.'
---

# Using the flutterdocs MCP Server

This skill defines when and how to use the flutterdocs MCP tools to produce accurate, version-grounded responses about Flutter and Dart APIs.

## When to Use flutterdocs

**Use it** when any of the following apply:
- Generating code that depends on a specific constructor signature, named parameter, or default value
- Answering questions about a non-trivial, niche, or recently-changed API
- Enumerating properties, methods, or constants on a class (completeness matters)
- Not fully confident in a specific API detail
- Discovering which widget or class to use for a task (you don't know the exact symbol name)

**Skip it** when all of the following apply:
- The API is high-frequency and stable (e.g. `Text`, `Column`, `Row`, `Scaffold`, `Navigator`)
- The question is conceptual or architectural (widget tree, `BuildContext`, reactive patterns)
- You already fetched the relevant docs in the same conversation

## Tool Selection

```
Do you know the exact class/mixin/enum/typedef name?
  YES → lookupEntity(name)
        → getDocumentation(uri from result)

Do you know the method/property name (with or without its class)?
  YES → lookupMember(name, [library])
        → getDocumentation(uri from result)

Do you need to find a widget or class by concept/behavior?
  YES → searchDocumentation(query)  ← space-separated AND terms
        → getDocumentation(uri from best result)

Do you need all available library slugs?
  YES → listLibraries()
```

## Workflow

### 1. Discover the symbol

Use `lookupEntity`, `lookupMember`, or `searchDocumentation` to obtain:
- **library slug** (e.g. `material`, `dart-async`, `widgets`)
- **entity identifier** (e.g. `VisualDensity`, `ThemeData`)
- **member identifier** (e.g. `copyWith`, `baseSizeAdjustment`)

### 2. Fetch the docs

Call `getDocumentation` with a `flutter-docs://` URI constructed from the discovery result:

| Target | URI shape |
|--------|-----------|
| Library | `flutter-docs://api/{library_slug}` |
| Class / enum / mixin | `flutter-docs://api/{library_slug}/{entity}` |
| Constructor / method / property | `flutter-docs://api/{library_slug}/{entity}/{member}` |

**Important:** Only use identifiers obtained from tool results. Never guess URIs or construct them from training data.

### 3. Navigate deeper (as needed)

The markdown returned by `getDocumentation` contains embedded `flutter-docs://` links. Follow these links by passing them directly to `getDocumentation` to drill into related types (e.g. from `ThemeData` → `TextTheme` → `TextStyle`).

## MCP Server Name

The MCP tool names (`lookupEntity`, `lookupMember`, `searchDocumentation`, `listLibraries`, `getDocumentation`) are fixed in the server implementation. Your MCP client may prefix them with the configured server name (e.g., `mcp_flutterdocs_lookupEntity` when the server is named `flutterdocs`). The tool selection guidance above uses the short names; map to whatever prefix your client uses. If you rename the server, only the prefix changes — the tool names themselves do not.

## Notes on Library Slugs

Library slugs differ from display names:
- `dart:async` → `dart-async`
- `dart:io` → `dart-io`
- `dart:core` → `dart-core`

Use `listLibraries` to resolve the correct slug if uncertain.

## Example Patterns

**Before generating code using `ListTile`:**
1. `lookupEntity("ListTile")` → `["material", "ListTile", "class"]`
2. `getDocumentation("flutter-docs://api/material/ListTile")` → review constructor and properties

**Finding a widget for nested scrolling:**
1. `searchDocumentation("nested scrollable")` → review results
2. `getDocumentation(uri)` for the most relevant match

**Checking a specific method signature:**
1. `lookupMember("effectiveConstraints")` → `["material", "VisualDensity", "effectiveConstraints", "method"]`
2. `getDocumentation("flutter-docs://api/material/VisualDensity/effectiveConstraints")`
