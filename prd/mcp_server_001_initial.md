# flutterdocs_mcp PRD

`flutterdocs_mcp.dart` is a Model Context Protocol (MCP) server for Flutter and Dart documentation built with the `dart_mcp` package. It serves documentation content retrieved from a sqlite3 database file with the schema defined in `make_docs/DOCDB_SCHEMA.sql`. This PRD defines the requirements, design, and implementation plan for the `flutterdocs_mcp` server.

## Technology Stack

- Dart programming language and SDK for implementing the MCP server.
- The `dart_mcp` Dart package for building MCP servers. Supports only the stdio transport, which is sufficient for our use case and simplifies implementation and deployment.
- The `sqlite3` Dart package for retrieving Flutter/Dart documentation from a sqlite3 database file.

## Database File

The sqlite3 database file is bundled with the package at `lib/db/flutter_docs.db`. It is committed to the GitHub repository and distributed as part of the pub.dev package, so users receive it automatically on `dart pub global activate flutterdocs_mcp`. The database content is controlled and quality-checked by the project maintainer using the `make_docs/` tooling.

## Inputs

`flutterdocs_mcp.dart` accepts the following command-line argument:

- Optional: `--db <path>`: Overrides the path to the sqlite3 database file. Useful for users who generate a custom database with the `make_docs/` tooling. If not provided, the server resolves the bundled database using `Isolate.packageUri('package:flutterdocs_mcp/db/flutter_docs.db')`. If the resolved path does not exist or is not readable, the server logs an error and exits with a non-zero exit code.

## Tools

The MCP server must implement the following tools.

### lookupEntity

- name: "lookupEntity"
- title: "Resolve Flutter entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) by name"
- description: "Finds Flutter entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) by identifier name. Use this when you have an entity name (e.g., ListTile, HourFormat) and need to know which library (or libraries) it belongs to. Navigation Tip: Use the returned [library, entity] values to construct resource URIs: flutter-docs://api/{library}/{entity}."
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
      "description": "List of up to 10 match results ([library, entity, entity category] tuples).",
      "items": {
        "type": "array",
        "prefixItems": [
          { "type": "string", "description": "Library name (e.g., 'material')." },
          { "type": "string", "description": "Entity name (e.g., 'ListTile')." },
          { "type": "string", "description": "Entity category (e.g., 'class')." }
        ],
        "description": "Construct resource URIs from these results as: flutter-docs://api/{library}/{entity}"
      }
    }
  ]
}

### lookupMember

- name: "lookupMember"
- title: "Resolve Flutter member (constructor, property, method, operator, constant, static method) by name and optional library hint."
- description: "Finds Flutter member (constructor, property, method, operator, constant, static method) by identifier name and optional library hint. Use this when you have a member name (e.g., visualDensity, addMaterialState) and need to know which entity it belongs to. The optional library name hint limits the search to that library, which is useful for common member names. Navigation Tip: Use the returned [library, entity, member] values to construct resource URIs: flutter-docs://api/{library}/{entity}/{member}."
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
      "description": "List of up to 10 match results ([library, entity, member, member category] tuples).",
      "items": {
        "type": "array",
        "prefixItems": [
          { "type": "string", "description": "Library name (e.g., 'material')." },
          { "type": "string", "description": "Entity name (e.g., 'ListTile')." },
          { "type": "string", "description": "Member name (e.g., 'visualDensity')." },
          { "type": "string", "description": "Member category (e.g., 'property')." }
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
- title: "Flutter library documentation index"
- description: "High-level summary of the library and all of its entities (classes, mixins, enums, extensions, extension types, typedefs, top-level functions, top-level constants). Contains embedded navigation links (resource URIs) to the detailed documentation for each entity."
- annotations: {"audience": ["user", "assistant"]}

### entityDocumentation

- uriTemplate: "flutter-docs://api/{library}/{entity}"
- name: "entityDocumentation"
- title: "Flutter entity documentation"
- description: "Detailed documentation for the Flutter entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) in the specified library. Includes a summary of all its members (constructors, properties, methods, operators, constants, static methods), with embedded navigation links (resource URIs) to the detailed documentation for each member."
- annotations: {"audience": ["user", "assistant"]}

### memberDocumentation

- uriTemplate: "flutter-docs://api/{library}/{entity}/{member}"
- name: "memberDocumentation"
- title: "Flutter member documentation"
- description: "Detailed documentation for the Flutter member (constructor, property, method, operator, constant, static method) of the specified entity in the specified library."
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

Both queries use the `idx_entity_identifier` index on `entity(identifier_id)`.

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

Both variants use the `idx_member_identifier` index on `member(identifier_id)`.

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

Resource reads return an `ReadResourceResult`. Cases to handle:

- `library`, `entity`, or `member` not found in the database → return an MCP error response (throw `McpError` with an appropriate error code and message).

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

- The sqlite3 database is opened once in the `DocDatabase` constructor and kept open for the lifetime of the process.
- All runtime SQL statements (`lookupEntity`, `lookupMember`, `entityDocumentation`, `memberDocumentation`) are compiled into prepared statements once at startup and reused across requests.

## Source Structure

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
library flutterdocs_mcp;

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

Tests use a minimal sqlite3 database created in-memory or written to a temp file during test setup (`setUp`) and deleted during teardown (`tearDown`). Fixture data should cover at least two libraries, one entity per library with multiple member types, to exercise the join logic.

## Open Questions

1. **Resource not-found behavior**: Unlike tools — where returning a total count of 0 with an empty result list is a valid non-error response — resources return text content, not structured result objects. There is no "zero results" concept for a resource: a resource either has content or it does not exist. The MCP spec recommends throwing an error for resources that cannot be resolved. The current design (throw `McpError`) reflects this guidance. **Confirm this is acceptable**, or clarify if a non-error empty-content response is preferred for any of the three resource types.

2. **Bundled database path resolution**: The default db path is resolved at runtime using `Isolate.packageUri('package:flutterdocs_mcp/db/flutter_docs.db')`. Confirm this resolution strategy is acceptable and clarify the expected behavior if the resolved path does not exist (e.g., during development before the db has been generated for the first time): should the server fail immediately with a clear error, or fall back to a well-known user-local path such as `~/.local/share/flutterdocs_mcp/flutter_docs.db`?