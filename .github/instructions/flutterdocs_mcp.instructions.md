---
description: "flutterdocs_mcp Dart MCP server: source structure, CLI, MCP surface, database coupling, versioning, and test structure."
name: flutterdocs_mcp_reference
applyTo: "bin/**,lib/**,test/**"
---

# flutterdocs_mcp Reference

## Purpose

A read-only Dart MCP server (`bin/flutterdocs_mcp.dart`) that exposes Flutter/Dart API documentation from a sqlite3 database produced by `load.py`. Communicates over stdio. Consult the `dart-mcp-builder` skill when adding or debugging MCP features.

## CLI

```
flutterdocs_mcp --db <path_to_docs.db>
flutterdocs_mcp --version          # print server version
flutterdocs_mcp --db-version       # print user_version of the --db file
```

Startup validates that `PRAGMA user_version` of `--db` equals `kDbVersion` (in `version.dart`). Exits 1 on mismatch or unreadable file.

## MCP Surface

### Tools (`lib/src/tools.dart`)

| Tool | Returns |
|---|---|
| `lookupEntity` | `{total, results: [[library_slug, entity, category]]}` — `name` param is case-insensitive; results always carry the canonical identifier name |
| `lookupMember` | `{total, results: [[library_slug, entity, member, category]]}` — `name` param is case-insensitive; results always carry canonical names |
| `listLibraries` | `{total, results: [[library_slug, library_display_name]]}` |
| `searchDocumentation` | `{total, results: [[library_slug, entity, excerpt]]}` — FTS5 unicode61-tokenized (case-insensitive) |
| `getDocumentation` | markdown string in `content[0].text` — dispatches on URI segment count: 1 → `libraryIndex`, 2 → `entityDocumentation`, 3 → `memberDocumentation`; returns `isError: true` on miss or unrecognized URI shape; **case-sensitive** (use canonical names from lookup results) |

Discovery tools (`lookupEntity`, `lookupMember`, `listLibraries`, `searchDocumentation`) return JSON in both `content[0].text` and `structuredContent`. `getDocumentation` returns plain markdown with no `structuredContent`.

All tools are read-only, idempotent, and closed-world.

### Resource Templates (`lib/src/resources.dart`)

All URIs use scheme `flutter-docs://`.

| Template | URI pattern |
|---|---|
| `libraryIndex` | `flutter-docs://api/{library_slug}` |
| `entityDocumentation` | `flutter-docs://api/{library_slug}/{entity}` |
| `memberDocumentation` | `flutter-docs://api/{library_slug}/{entity}/{member}` |

Returned markdown embeds `flutter-docs://` URIs as navigation links. `_notFound()` throws `RpcException(-32002)`.

## Source Structure

```
lib/src/
  server.dart    # FlutterDocsMcpServer (MCPServer + ToolsSupport + ResourcesSupport + LoggingSupport)
  db.dart        # DocDatabase — read-only sqlite3 wrapper; prepared stmts; in-memory caches
  tools.dart     # registerTools(), one handler per tool
  resources.dart # registerResources(), one handler per resource template
  version.dart   # kVersion (semver str), kDbVersion (int: major*1_000_000 + minor*1_000 + patch)
```

`DocDatabase` opens the database read-only, caches all four small lookup tables (`identifier`, `entity_type`, `member_type`, `library`) at construction, and compiles all SQL into `PreparedStatement`s reused across requests. FTS5 queries go through `_sanitizeFtsQuery()` to prevent injection.

## Versioning

`kVersion` and `kDbVersion` in `version.dart` are kept in sync with `pubspec.yaml` and `_shared/version.py` (Python side) by `dart run tool/set_version.dart`. Never edit these constants manually.

`set_version.dart` accepts an optional `--db <path>` flag. When provided, it also updates `PRAGMA user_version` of the given sqlite3 database file to the same integer as `DB_VERSION` / `kDbVersion`. Use this for releases that do not change the database schema or content (e.g. a README-only change) so that the existing database file stays compatible with the new server version without needing to be regenerated.

## Testing

Tests live in `test/`. The test suite uses an in-process `StreamChannelController` — no subprocess, no `dart run` contamination on the MCP stdio channel.

```
test/
  server_test.dart  # End-to-end MCP tool/resource tests via in-process client
  db_test.dart      # DocDatabase unit tests with a hand-crafted sqlite3 fixture
  cli_test.dart     # FlutterDocsMcpServer.run() argument/flag handling
```

Run tests: `dart test`

`server_test.dart` loads a real docs database via `uv run load` (make_docs/) for integration coverage. `db_test.dart` builds a minimal fixture directly with `sqlite3` to avoid that dependency.
