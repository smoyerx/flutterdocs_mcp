import 'dart:async';
import 'dart:convert';

import 'package:dart_mcp/server.dart';

import 'db.dart';

/// Registers the [lookupEntity], [lookupMember], [listLibraries], and
/// [searchDocumentation] tools on [server].
void registerTools(ToolsSupport server, DocDatabase db) {
  server.registerTool(
    _lookupEntityTool,
    (request) => _lookupEntity(request, db),
  );
  server.registerTool(
    _lookupMemberTool,
    (request) => _lookupMember(request, db),
  );
  server.registerTool(
    _listLibrariesTool,
    (request) => _listLibraries(request, db),
  );
  server.registerTool(
    _searchDocumentationTool,
    (request) => _searchDocumentation(request, db),
  );
}

// ---------------------------------------------------------------------------
// Annotations common to all tools.
// ---------------------------------------------------------------------------

final _toolAnnotations = ToolAnnotations(
  destructiveHint: false,
  idempotentHint: true,
  openWorldHint: false,
  readOnlyHint: true,
);

// ---------------------------------------------------------------------------
// lookupEntity
// ---------------------------------------------------------------------------

final _lookupEntityTool = Tool(
  name: 'lookupEntity',
  title: 'Resolve Flutter/Dart entity (class, mixin, etc.) by name.',
  description:
      'Finds Flutter/Dart entity (class, mixin, enum, extension, extension '
      'type, typedef, top-level function/constant) by identifier name. '
      'Use the returned [library_slug, entity, category] values to construct '
      'resource URIs for entityDocumentation.',
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
  outputSchema: Schema.object(
    description: 'An object with a total match count and up to 10 results.',
    properties: {
      'total': Schema.int(
        description: 'The total number of entity name matches found.',
      ),
      'results': Schema.list(
        description: 'List of up to 10 match results.',
        items: Schema.list(
          description: 'A [library_slug, entity, category] array.',
          prefixItems: [
            Schema.string(description: "Library slug (e.g., 'material')."),
            Schema.string(description: "Entity name (e.g., 'ListTile')."),
            Schema.string(description: "Category of entity (e.g., 'class')."),
          ],
        ),
      ),
    },
    required: ['total', 'results'],
  ),
  annotations: _toolAnnotations,
);

FutureOr<CallToolResult> _lookupEntity(
  CallToolRequest request,
  DocDatabase db,
) {
  final name = request.arguments!['name'] as String;
  final (total, results) = db.lookupEntity(name);
  final structured = {
    'total': total,
    'results': results.map((r) => [r.$1, r.$2, r.$3]).toList(),
  };
  return CallToolResult(
    content: [TextContent(text: jsonEncode(structured))],
    structuredContent: structured,
  );
}

// ---------------------------------------------------------------------------
// lookupMember
// ---------------------------------------------------------------------------

final _lookupMemberTool = Tool(
  name: 'lookupMember',
  title:
      'Resolve Flutter/Dart member (constructor, property, method, etc.) '
      'by name and optional library slug hint.',
  description:
      'Finds Flutter/Dart member (constructor, property, method, operator, '
      'constant, static method) by identifier name and optional library slug '
      'hint. '
      'Use the returned [library_slug, entity, member, category] values to '
      'construct resource URIs for memberDocumentation.',
  inputSchema: Schema.object(
    properties: {
      'name': Schema.string(
        description:
            "The name of the member to find (e.g., 'visualDensity'). "
            'Case-sensitive.',
      ),
      'librarySlugHint': Schema.string(
        description:
            'Optional: Limit search to a specific library slug '
            "(e.g., 'material', 'dart-io'). If the slug is not valid, the "
            'hint is ignored and an unscoped search is performed.',
      ),
    },
    required: ['name'],
  ),
  outputSchema: Schema.object(
    description: 'An object with a total match count and up to 10 results.',
    properties: {
      'total': Schema.int(
        description: 'The total number of member name matches found.',
      ),
      'results': Schema.list(
        description: 'List of up to 10 match results.',
        items: Schema.list(
          description: 'A [library_slug, entity, member, category] array.',
          prefixItems: [
            Schema.string(description: "Library slug (e.g., 'material')."),
            Schema.string(description: "Entity name (e.g., 'ListTile')."),
            Schema.string(description: "Member name (e.g., 'visualDensity')."),
            Schema.string(
              description: "Category of member (e.g., 'property').",
            ),
          ],
        ),
      ),
    },
    required: ['total', 'results'],
  ),
  annotations: _toolAnnotations,
);

FutureOr<CallToolResult> _lookupMember(
  CallToolRequest request,
  DocDatabase db,
) {
  final args = request.arguments!;
  final name = args['name'] as String;
  final librarySlugHint = args['librarySlugHint'] as String?;
  final (total, results) = db.lookupMember(
    name,
    librarySlugHint: librarySlugHint,
  );
  final structured = {
    'total': total,
    'results': results.map((r) => [r.$1, r.$2, r.$3, r.$4]).toList(),
  };
  return CallToolResult(
    content: [TextContent(text: jsonEncode(structured))],
    structuredContent: structured,
  );
}

// ---------------------------------------------------------------------------
// listLibraries
// ---------------------------------------------------------------------------

final _listLibrariesTool = Tool(
  name: 'listLibraries',
  title: 'List all available Flutter/Dart library slugs.',
  description:
      'Returns all available library slugs that can be used to construct '
      'resource URIs (flutter-docs://api/{library_slug}/...). '
      'Library slugs and library display names often differ '
      '(e.g., library dart:io uses slug dart-io; package libraries use '
      'slugs like package-material_color_utilities_blend_blend).',
  inputSchema: Schema.object(properties: {}),
  annotations: _toolAnnotations,
);

FutureOr<CallToolResult> _listLibraries(
  CallToolRequest request,
  DocDatabase db,
) {
  final slugs = db.listLibraries();
  return CallToolResult(content: [TextContent(text: jsonEncode(slugs))]);
}

// ---------------------------------------------------------------------------
// searchDocumentation
// ---------------------------------------------------------------------------

final _searchDocumentationTool = Tool(
  name: 'searchDocumentation',
  title: 'Search Flutter/Dart API documentation',
  description:
      'Performs a full-text search across the Flutter/Dart API documentation '
      'to find entities (classes, mixins, etc.) whose documentation contains '
      'the specified keywords. '
      'All words are matched with AND semantics — every word must appear, '
      'but not necessarily adjacent. '
      'Use the returned [library_slug, entity, documentation_excerpt] values '
      'to construct resource URIs for entityDocumentation.',
  inputSchema: Schema.object(
    properties: {
      'query': Schema.string(
        description:
            'The search keywords (e.g., "scrolling", "stateful widget").',
      ),
    },
    required: ['query'],
  ),
  outputSchema: Schema.object(
    description:
        'An object with a total query match count and up to 20 results.',
    properties: {
      'total': Schema.int(
        description: 'The total number of query matches found.',
      ),
      'results': Schema.list(
        description: 'List of up to 20 query match results.',
        items: Schema.list(
          description: 'A [library_slug, entity, documentation_excerpt] array.',
          prefixItems: [
            Schema.string(description: "Library slug (e.g., 'material')."),
            Schema.string(description: "Entity name (e.g., 'ListTile')."),
            Schema.string(
              description: 'Documentation excerpt matching the query.',
            ),
          ],
        ),
      ),
    },
    required: ['total', 'results'],
  ),
  annotations: _toolAnnotations,
);

FutureOr<CallToolResult> _searchDocumentation(
  CallToolRequest request,
  DocDatabase db,
) {
  final query = request.arguments!['query'] as String;
  final (total, results) = db.searchDocumentation(query);
  final structured = {
    'total': total,
    'results': results.map((r) => [r.$1, r.$2, r.$3]).toList(),
  };
  return CallToolResult(
    content: [TextContent(text: jsonEncode(structured))],
    structuredContent: structured,
  );
}
