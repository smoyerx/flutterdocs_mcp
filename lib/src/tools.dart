import 'dart:async';
import 'dart:convert';

import 'package:dart_mcp/server.dart';

import 'db.dart';

/// Registers the [lookupEntity] and [lookupMember] tools on [server].
void registerTools(ToolsSupport server, DocDatabase db) {
  server.registerTool(_lookupEntityTool, (request) => _lookupEntity(request, db));
  server.registerTool(_lookupMemberTool, (request) => _lookupMember(request, db));
}

// ---------------------------------------------------------------------------
// lookupEntity
// ---------------------------------------------------------------------------

final _lookupEntityTool = Tool(
  name: 'lookupEntity',
  title:
      'Resolve Flutter/Dart entity (class, mixin, enum, extension, extension '
      'type, typedef, top-level function, top-level constant) by name',
  description:
      'Finds Flutter/Dart entity (class, mixin, enum, extension, extension '
      'type, typedef, top-level function, top-level constant) by identifier '
      'name. Use this when you have an entity name (e.g., ListTile, '
      'HourFormat) and need to know which library (or libraries) it belongs '
      'to. Navigation Tip: Use the returned [library, entity, category] '
      'values to construct resource URIs: '
      'flutter-docs://api/{library}/{entity}.',
  inputSchema: Schema.object(
    properties: {
      'name': Schema.string(
        description:
            "The name of the entity to find (e.g., 'ListTile'). "
            'Case-sensitive.',
      ),
    },
    required: ['name'],
  ),
);

FutureOr<CallToolResult> _lookupEntity(
  CallToolRequest request,
  DocDatabase db,
) {
  final name = request.arguments!['name'] as String;
  final (total, results) = db.lookupEntity(name);
  final encoded = jsonEncode([
    total,
    results.map((r) => [r.$1, r.$2, r.$3]).toList(),
  ]);
  return CallToolResult(content: [TextContent(text: encoded)]);
}

// ---------------------------------------------------------------------------
// lookupMember
// ---------------------------------------------------------------------------

final _lookupMemberTool = Tool(
  name: 'lookupMember',
  title:
      'Resolve Flutter/Dart member (constructor, property, method, operator, '
      'constant, static method) by name and optional library hint.',
  description:
      'Finds Flutter/Dart member (constructor, property, method, operator, '
      'constant, static method) by identifier name and optional library name '
      'hint. Use this when you have a member name (e.g., visualDensity, '
      'addMaterialState) and need to know which entity it belongs to. The '
      'optional library name hint limits the search to that library, which is '
      'useful for common member names. Navigation Tip: Use the returned '
      '[library, entity, member, category] values to construct resource URIs: '
      'flutter-docs://api/{library}/{entity}/{member}.',
  inputSchema: Schema.object(
    properties: {
      'name': Schema.string(
        description:
            "The name of the member to find (e.g., 'visualDensity'). "
            'Case-sensitive.',
      ),
      'libraryHint': Schema.string(
        description:
            "Optional: Limit search to a specific library (e.g., 'material'). "
            'Case-sensitive.',
      ),
    },
    required: ['name'],
  ),
);

FutureOr<CallToolResult> _lookupMember(
  CallToolRequest request,
  DocDatabase db,
) {
  final args = request.arguments!;
  final name = args['name'] as String;
  final libraryHint = args['libraryHint'] as String?;
  final (total, results) = db.lookupMember(name, libraryHint: libraryHint);
  final encoded = jsonEncode([
    total,
    results.map((r) => [r.$1, r.$2, r.$3, r.$4]).toList(),
  ]);
  return CallToolResult(content: [TextContent(text: encoded)]);
}
