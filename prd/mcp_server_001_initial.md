# flutterdocs_mcp PRD

`flutterdocs_mcp.dart` is a Model Context Protocol (MCP) server for Flutter and Dart documentation built with the `dart_mcp` package. It serves documentation content retrieved from a sqlite3 database file with the schema defined in `make_docs/DOCDB_SCHEMA.sql`. This PRD defines the requirements, design, and implementation plan for the `flutterdocs_mcp` server.

## Technology Stack

- Dart programming language and SDK for implementing the MCP server.
- The `dart_mcp` Dart package for building MCP servers. Supports only the stdio transport, which is sufficient for our use case and simplifies implementation and deployment.
- The `sqlite3` Dart package for retrieving Flutter/Dart documentation from a sqlite3 database file.

## Database File

The sqlite3 database file will be bundled with the package at `lib/db/flutter_docs.db`. The database content is controlled and quality-checked by the project maintainer using the `make_docs/` tooling.

Note: In the future, we will explore options for distributing the database file via pub.dev without having to clone the project repo. However, that will be a separate effort after the initial MCP server implementation is complete.

## Inputs

`flutterdocs_mcp.dart` accepts the following command-line argument:

- Mandatory: `--db <path>`: Path to the sqlite3 database file. If the path does not exist or is not readable, the server logs an error and exits with a non-zero exit code.

## Tools

The MCP server must implement the following tools.

### lookupEntity

- name: "lookupEntity"
- title: "Resolve Flutter/Dart entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) by name"
- description: "Finds Flutter/Dart entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) by identifier name. Use this when you have an entity name (e.g., ListTile, HourFormat) and need to know which library (or libraries) it belongs to. Navigation Tip: Use the returned [library, entity, category] values to construct resource URIs: flutter-docs://api/{library}/{entity}."
- inputSchema:
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the entity to find (e.g., 'ListTile'). Case-sensitive."
    }
  },
  "required": ["name"]
}
- outputSchema:
{
  "type": "array",
  "description": "A navigation tuple [totalMatches, resultList].",
  "prefixItems": [
    { "type": "integer", "description": "The total number of entity name matches found." },
    {
      "type": "array",
      "description": "List of up to 10 match results ([library, entity, category] tuples).",
      "items": {
        "type": "array",
        "prefixItems": [
          { "type": "string", "description": "Library name (e.g., 'material')." },
          { "type": "string", "description": "Entity name (e.g., 'ListTile')." },
          { "type": "string", "description": "Category of entity (e.g., 'class')." }
        ],
        "description": "Construct resource URIs from these results as: flutter-docs://api/{library}/{entity}"
      }
    }
  ]
}

### lookupMember

- name: "lookupMember"
- title: "Resolve Flutter/Dart member (constructor, property, method, operator, constant, static method) by name and optional library hint."
- description: "Finds Flutter/Dart member (constructor, property, method, operator, constant, static method) by identifier name and optional library name hint. Use this when you have a member name (e.g., visualDensity, addMaterialState) and need to know which entity it belongs to. The optional library name hint limits the search to that library, which is useful for common member names. Navigation Tip: Use the returned [library, entity, member, category] values to construct resource URIs: flutter-docs://api/{library}/{entity}/{member}."
- inputSchema:
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the member to find (e.g., 'visualDensisty'). Case-sensitive."
    },
    "libraryHint": {
      "type": "string",
      "description": "Optional: Limit search to a specific library (e.g., 'material'). Case-sensitive."
    },
  },
  "required": ["name"]
}
- outputSchema:
{
  "type": "array",
  "description": "A navigation tuple [totalMatches, resultList].",
  "prefixItems": [
    { "type": "integer", "description": "The total number of member name matches found." },
    {
      "type": "array",
      "description": "List of up to 10 match results ([library, entity, member, category] tuples).",
      "items": {
        "type": "array",
        "prefixItems": [
          { "type": "string", "description": "Library name (e.g., 'material')." },
          { "type": "string", "description": "Entity name (e.g., 'ListTile')." },
          { "type": "string", "description": "Member name (e.g., 'visualDensity')." },
          { "type": "string", "description": "Category of member (e.g., 'property')." }
        ],
        "description": "Construct resource URIs from these results as: flutter-docs://api/{library}/{entity}/{member}"
      }
    }
  ]
}

## Resource Templates

The MCP server must implement the following resource templates.

### libraryIndex

- uriTemplate: "flutter-docs://api/{library}"
- name: "libraryIndex"
- title: "Flutter/Dart library documentation index"
- description: "High-level summary of the library and all of its entities (classes, mixins, enums, extensions, extension types, typedefs, top-level functions, top-level constants). Contains embedded navigation links (resource URIs) to the detailed documentation for each entity."
- annotations: {"audience": ["user", "assistant"]}

### entityDocumentation

- uriTemplate: "flutter-docs://api/{library}/{entity}"
- name: "entityDocumentation"
- title: "Flutter/Dart entity documentation"
- description: "Detailed documentation for the Flutter/Dart entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) in the specified library. Includes a summary of all its members (constructors, properties, methods, operators, constants, static methods), with embedded navigation links (resource URIs) to the detailed documentation for each member."
- annotations: {"audience": ["user", "assistant"]}

### memberDocumentation

- uriTemplate: "flutter-docs://api/{library}/{entity}/{member}"
- name: "memberDocumentation"
- title: "Flutter/Dart member documentation"
- description: "Detailed documentation for the Flutter/Dart member (constructor, property, method, operator, constant, static method) of the specified entity in the specified library."
- annotations: {"audience": ["user", "assistant"]}

## Database Queries to Implement Tool and Resource Functionality

At startup, `DocDatabase` reads the four lookup/normalization tables (`identifier`, `entity_type`, `member_type`, `library`) entirely into in-memory maps (see Performance Optimizations). This eliminates all joins to those tables at query time. All runtime queries operate only on the `entity` and `member` tables and bind integer IDs resolved from the in-memory maps.

For each query, if a required name cannot be resolved to an ID from the in-memory maps, the handler short-circuits immediately without touching the database: tools return `(0, [])`, resources return a not-found error.

### lookupEntity

Pre-resolution: `identifierId = identifierNameToId[name]` — if absent, return `(0, [])` immediately.

**Count query** (binds `identifierId`):
```sql
SELECT COUNT(*) FROM entity WHERE identifier_id = ?
```

**Results query** (binds `identifierId`; up to 10 rows):
```sql
SELECT library_id, entity_type_id FROM entity WHERE identifier_id = ? LIMIT 10
```

Post-process each row: entity name = the input `name`; library name = `libraryById[library_id].name`; entity category = `entityTypeIdToName[entity_type_id]`.

Both queries use the `idx_entity_unique` index on `entity(identifier_id, library_id)`, with the leading `identifier_id` column satisfying the filter.

### lookupMember

Pre-resolution: `memberIdentifierId = identifierNameToId[name]` — if absent, return `(0, [])` immediately. When `libraryHint` is provided: `libraryId = libraryByName[libraryHint]?.id` — if absent, return `(0, [])` immediately.

**Count query, no library hint** (binds `memberIdentifierId`):
```sql
SELECT COUNT(*) FROM member WHERE identifier_id = ?
```

**Count query, with library hint** (binds `memberIdentifierId`, `libraryId`):
```sql
SELECT COUNT(*)
FROM member m
JOIN entity e ON m.entity_id = e.id
WHERE m.identifier_id = ? AND e.library_id = ?
```

**Results query, no library hint** (binds `memberIdentifierId`; up to 10 rows):
```sql
SELECT m.member_type_id, e.library_id, e.identifier_id
FROM member m
JOIN entity e ON m.entity_id = e.id
WHERE m.identifier_id = ?
LIMIT 10
```

**Results query, with library hint** (binds `memberIdentifierId`, `libraryId`; up to 10 rows):
```sql
SELECT m.member_type_id, e.identifier_id
FROM member m
JOIN entity e ON m.entity_id = e.id
WHERE m.identifier_id = ? AND e.library_id = ?
LIMIT 10
```

Post-process each row: member name = the input `name`; library name = `libraryById[library_id].name` (or the known `libraryHint`); entity name = `identifierIdToName[e.identifier_id]`; member category = `memberTypeIdToName[member_type_id]`.

Both variants use the `idx_member_unique` index on `member(identifier_id, entity_id)`, with the leading `identifier_id` column satisfying the filter.

### libraryIndex resource

Pure in-memory lookup — no SQL required:

```
library record = libraryByName[library]
if absent → not-found error
return library record's contentMarkdown
```

### entityDocumentation resource

Pre-resolution: `libraryId = libraryByName[library]?.id`; `identifierId = identifierNameToId[entity]` — if either is absent, return a not-found error.

```sql
SELECT content_markdown FROM entity WHERE identifier_id = ? AND library_id = ?
```

Uses the `idx_entity_unique` index on `entity(identifier_id, library_id)`.

### memberDocumentation resource

Pre-resolution: `libraryId = libraryByName[library]?.id`; `entityIdentifierId = identifierNameToId[entity]`; `memberIdentifierId = identifierNameToId[member]` — if any is absent, return a not-found error.

```sql
SELECT m.content_markdown
FROM member m
JOIN entity e ON m.entity_id = e.id
WHERE e.library_id = ? AND e.identifier_id = ? AND m.identifier_id = ?
```

Uses the `idx_member_unique` index on `member(identifier_id, entity_id)` (via the entity join).

## Error Handling

### Tool errors

Tools return a `CallToolResult` with `isError: true`. A short, human-readable error message should be returned in the content. Cases to handle:

- Database file not found or not readable at startup → server should log the error and exit with a non-zero exit code rather than starting up in a broken state.
- Query returns zero results → return a result with `isError: false` and content indicating no matches were found (empty result list with total count 0), not an error.

### Resource errors

Resource template handlers have the return type `FutureOr<ReadResourceResult?>`. Returning `null` signals "not matched" (the framework tries the next template); throwing an exception signals an error. The two cases to handle:

- **URI matched but content not found** (e.g., unknown library/entity/member): throw `RpcException(-32002, 'Resource not found', data: {'uri': request.uri})`. The `json_rpc_2` layer passes `RpcException` through unchanged, producing exactly the MCP-spec error response:
  ```json
  {
    "jsonrpc": "2.0",
    "id": 5,
    "error": {
      "code": -32002,
      "message": "Resource not found",
      "data": { "uri": "flutter-docs://api/{library}/{entity}" }
    }
  }
  ```
  `RpcException` is from `package:json_rpc_2/json_rpc_2.dart`. It is a direct dependency of `dart_mcp` and must also be declared as a direct dependency in `pubspec.yaml` so that the import is explicit.

- **URI not matched** (no template applies): return `null` to let the framework fall through. This should not occur in practice since the three templates cover all valid `flutter-docs://api/...` URIs.



## Performance Optimizations

### In-memory caches (startup)

`DocDatabase` reads the following tables in their entirety at startup and stores them in memory. These tables are small and static for the lifetime of the process.

| Table | Maps created |
|---|---|
| `identifier` | `Map<int, String> identifierIdToName`, `Map<String, int> identifierNameToId` |
| `entity_type` | `Map<int, String> entityTypeIdToName` |
| `member_type` | `Map<int, String> memberTypeIdToName` |
| `library` | `Map<int, LibraryRecord> libraryById`, `Map<String, LibraryRecord> libraryByName` |

`LibraryRecord` holds `id`, `name`, and `contentMarkdown`.

With these caches in place:
- The `identifier`, `entity_type`, `member_type`, and `library` tables are never queried at runtime.
- All joins to those tables are replaced by in-memory map lookups.
- The `libraryIndex` resource is served entirely from `libraryByName` — no SQL is executed.
- Input name-to-ID resolution failures (unknown entity/member/library names) are detected before any SQL is executed, allowing immediate short-circuit returns.

### Other optimizations

- The sqlite3 database is opened once in the `DocDatabase` constructor, in read-only mode (`OpenMode.readOnly`), and kept open for the lifetime of the process. Read-only mode prevents accidental writes and allows the OS to share a single memory-mapped copy of the file across multiple processes.
- All runtime SQL statements (`lookupEntity`, `lookupMember`, `entityDocumentation`, `memberDocumentation`) are compiled into prepared statements once at startup and reused across requests.

## Source Structure

> **Pre-implementation note**: Before implementation begins, the maintainer will manually create the `flutterdocs_mcp/` Dart package directory, initialize `pubspec.yaml`, and run `dart pub get` to install dependencies. This manual bootstrapping step is not part of implementing this PRD.

The package follows the standard Dart convention of separating public API (`lib/`) from implementation (`lib/src/`) to maximize the pub.dev pana score while keeping the server's internal structure clean.

```
flutterdocs_mcp/                  ← Dart package root (to be created)
  pubspec.yaml
  CHANGELOG.md
  README.md
  lib/
    flutterdocs_mcp.dart          ← public barrel file; library-level dartdoc; exports FlutterDocsMcpServer only
    db/
      flutter_docs.db             ← bundled sqlite3 database (committed to repo, distributed via pub.dev)
    src/
      server.dart                 ← FlutterDocsMcpServer class (extends MCPServer, mixes in ToolsSupport, ResourcesSupport, LoggingSupport)
      tools.dart                  ← lookupEntity and lookupMember tool handler implementations
      resources.dart              ← libraryIndex, entityDocumentation, memberDocumentation resource template handler implementations
      db.dart                     ← DocDatabase class: loads in-memory caches at startup, compiles prepared statements, exposes typed query methods
  bin/
    flutterdocs_mcp.dart          ← thin entry point (~3 lines): calls FlutterDocsMcpServer.run(args)
  example/
    example.md                    ← MCP client configuration snippets (Claude Desktop, VS Code Copilot, etc.)
  test/
    ...                           ← see Testing and Validation
```

### Key class: `FlutterDocsMcpServer`

- Extends `MCPServer` and mixes in `ToolsSupport`, `ResourcesSupport`, and `LoggingSupport` from `dart_mcp`.
- Constructor accepts the path to the sqlite3 database file as a required parameter.
- Exposes a static `run(List<String> args)` method that parses the database path from `args` and constructs and starts the server.
- Delegates all database access to a `DocDatabase` instance.

### Key class: `DocDatabase`

- Wraps the `sqlite3` package.
- In its constructor:
  1. Opens the database file.
  2. Reads the `identifier`, `entity_type`, `member_type`, and `library` tables into the in-memory maps described in Performance Optimizations.
  3. Compiles all runtime SQL statements into prepared statements.
- Exposes typed query methods:
  - `lookupEntity(String name) → (int total, List<(String library, String entity, String category)> results)`
  - `lookupMember(String name, {String? libraryHint}) → (int total, List<(String library, String entity, String member, String category)> results)`
  - `libraryIndex(String library) → String? contentMarkdown` — served entirely from the `libraryByName` cache; no SQL.
  - `entityDocumentation(String library, String entity) → String? contentMarkdown`
  - `memberDocumentation(String library, String entity, String member) → String? contentMarkdown`
- Provides a `close()` method to dispose prepared statements and close the database.

### `lib/flutterdocs_mcp.dart`

```dart
/// An MCP server for Flutter and Dart API documentation.
///
/// This library exposes [FlutterDocsMcpServer], which implements an MCP server
/// that serves Flutter/Dart API documentation over the stdio transport.
///
/// ## Activation
///
/// ```
/// dart pub global activate flutterdocs_mcp
/// flutterdocs_mcp --db /path/to/flutter_docs.db
/// ```
library;

export 'src/server.dart';
```

### `bin/flutterdocs_mcp.dart`

```dart
import 'package:flutterdocs_mcp/flutterdocs_mcp.dart';

void main(List<String> args) => FlutterDocsMcpServer.run(args);
```

## pub.dev Publishing

The package is published to pub.dev as a Dart executable. Key `pubspec.yaml` configuration:

```yaml
name: flutterdocs_mcp
description: An MCP server for Flutter and Dart API documentation. Provides tools and resources for navigating Flutter/Dart API docs via the Model Context Protocol.
version: 0.1.0
repository: https://github.com/smoyerx/flutterdocs_mcp

environment:
  sdk: '>=3.9.0 <4.0.0'

executables:
  flutterdocs_mcp: flutterdocs_mcp   # maps to bin/flutterdocs_mcp.dart

topics:
  - mcp
  - flutter
  - dart
  - documentation

dependencies:
  dart_mcp: ^0.4.1
  sqlite3: ^2.7.4        # bundles SQLite natively; no external libsqlite3 required
  args: ^2.6.0
  json_rpc_2: ^3.0.2    # for RpcException used in resource not-found error handling

dev_dependencies:
  lints: ^4.0.0
  test: ^1.25.0
```

Note: The `sqlite3` package bundles SQLite via hooks and does not require an external `libsqlite3` system library.

A `CHANGELOG.md` is required for a good pana score and must be present from the first publish.

## Testing and Validation

### Unit tests

- `test/db_test.dart`: tests for `DocDatabase` using a small in-memory or temporary sqlite3 database populated with fixture data. Covers each query method, empty-result cases, and the not-found cases.

### Integration tests

- `test/server_test.dart`: end-to-end tests using the `dart_mcp` `MCPClient` to connect to a `FlutterDocsMcpServer` instance backed by a test database. Covers:
  - `lookupEntity`: hit, partial hit (multiple libraries), miss.
  - `lookupMember`: hit without library hint, hit with library hint, miss.
  - `libraryIndex`: valid library, unknown library.
  - `entityDocumentation`: valid entity, unknown entity/library.
  - `memberDocumentation`: valid member, unknown member/entity/library.

### Test database

The fixture database is **not** committed to the repository. Instead, it is generated at test startup using `setUpAll()` and cleaned up in `tearDownAll()` via `dart:io`'s `Process.run()`.

**Tests must be run from the repository root.** This is a deliberate restriction — these tests are intended to be run by the repo maintainer only — and it eliminates the need to locate the repo root dynamically at runtime.

`setUpAll()` creates a temporary file, then invokes the two `uv run load` commands to populate it. All paths are relative to the repo root (the working directory):

```dart
import 'dart:io';

late File _testDb;

setUpAll(() async {
  _testDb = await File.fromUri(
    Directory.systemTemp.uri.resolve('flutterdocs_mcp_test.db'),
  ).create();

  for (final suite in ['material', 'widgets']) {
    final result = await Process.run(
      'uv',
      [
        'run', 'load',
        '-d', 'tests/load/integration/samples',
        '-s', suite,
        '-o', _testDb.path,
      ],
      workingDirectory: 'make_docs',
    );
    if (result.exitCode != 0) {
      throw StateError('uv run load failed for $suite:\n${result.stderr}');
    }
  }
});

tearDownAll(() async {
  await _testDb.delete();
});
```

This produces a two-library (`material`, `widgets`) database from the committed `make_docs/` integration test samples, which are fully deterministic. The approach requires `uv` to be installed and the `make_docs/` Python environment to be available, but avoids storing a binary sqlite3 file in git.



## Resolved Decisions

1. **Resource not-found error code**: Throw `RpcException(-32002, 'Resource not found', data: {'uri': request.uri})` from `package:json_rpc_2/json_rpc_2.dart`. The `dart_mcp` package does not define a `McpError` class or error-code constants; it delegates to `json_rpc_2`'s `Peer`, which passes `RpcException` instances through to the client unchanged. Any non-`RpcException` exception would be silently wrapped as a generic -32603 error, so `RpcException` must be used explicitly.

2. **Database distribution**: Deferred. The database file (`flutter_docs.db`) is committed to the repository and users can obtain it by cloning the repo or downloading it directly. For the initial implementation, `--db` is mandatory; there is no default path. Options for bundling the database in the pub.dev package (e.g., `lib/db/`) will be evaluated separately after the initial server implementation is complete.

3. **Dart SDK minimum version**: `>=3.9.0 <4.0.0` (required by the latest `dart_mcp` and `sqlite3`).

4. **sqlite3 dependency**: Use latest `sqlite3`. The package bundles SQLite via Dart hooks; no external `libsqlite3` system library is required.

5. **Pre-implementation setup**: The maintainer will manually create the `flutterdocs_mcp/` Dart package, `pubspec.yaml`, and run `dart pub get` before implementation begins. This is not a step in implementing the PRD.

