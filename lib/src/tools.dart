import 'dart:async';
import 'dart:convert';

import 'package:dart_mcp/server.dart';

import 'db.dart';

/// Registers the [lookupEntity], [lookupMember], and [listLibraries] tools
/// on [server].
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
      'to. Navigation Tip: Use the returned [library_slug, entity, category] '
      'values to construct resource URIs: '
      'flutter-docs://api/{library_slug}/{entity}. '
      'Note: The returned library_slug value is a URI slug (not the display name) '
      '— use it as-is in resource URIs and as libraryHint. Call '
      'listLibraries to see all available library_slug values.',
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
  outputSchema: ObjectSchema.fromMap({
    'type': 'array',
    'description': 'A navigation tuple [totalMatches, resultList].',
    'prefixItems': [
      {
        'type': 'integer',
        'description': 'The total number of entity name matches found.',
      },
      {
        'type': 'array',
        'description':
            'List of up to 10 match results ([library_slug, entity, category] tuples).',
        'items': {
          'type': 'array',
          'description':
              'Construct resource URIs from these results as: '
              'flutter-docs://api/{library_slug}/{entity}',
          'prefixItems': [
            {
              'type': 'string',
              'description': "Library slug (e.g., 'material').",
            },
            {
              'type': 'string',
              'description': "Entity name (e.g., 'ListTile').",
            },
            {
              'type': 'string',
              'description': "Category of entity (e.g., 'class').",
            },
          ],
        },
      },
    ],
  }),
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
      'constant, static method) by identifier name and optional library slug '
      'hint. Use this when you have a member name (e.g., visualDensity, '
      'addMaterialState) and need to know which entity it belongs to. The '
      'optional library slug hint limits the search to that library, which is '
      'useful for common member names. Navigation Tip: Use the returned '
      '[library_slug, entity, member, category] values to construct resource URIs: '
      'flutter-docs://api/{library_slug}/{entity}/{member}. '
      'Note: The returned library_slug value is a URI slug (not the display name) '
      '— use it as-is in resource URIs and as libraryHint. Call '
      'listLibraries to see all available library_slug values.',
  inputSchema: Schema.object(
    properties: {
      'name': Schema.string(
        description:
            "The name of the member to find (e.g., 'visualDensity'). "
            'Case-sensitive.',
      ),
      'libraryHint': Schema.string(
        description:
            'Optional: Limit search to a specific library using its slug '
            "(e.g., 'material', 'dart-io'). Colon forms are also accepted "
            "(e.g., 'dart:io' is treated as 'dart-io'). If the value is not "
            'recognized as a known slug, the hint is ignored and an unscoped '
            'search is performed. Call listLibraries to see all available slugs.',
      ),
    },
    required: ['name'],
  ),
  outputSchema: ObjectSchema.fromMap({
    'type': 'array',
    'description': 'A navigation tuple [totalMatches, resultList].',
    'prefixItems': [
      {
        'type': 'integer',
        'description': 'The total number of member name matches found.',
      },
      {
        'type': 'array',
        'description':
            'List of up to 10 match results '
            '([library_slug, entity, member, category] tuples).',
        'items': {
          'type': 'array',
          'description':
              'Construct resource URIs from these results as: '
              'flutter-docs://api/{library_slug}/{entity}/{member}',
          'prefixItems': [
            {
              'type': 'string',
              'description': "Library slug (e.g., 'material').",
            },
            {
              'type': 'string',
              'description': "Entity name (e.g., 'ListTile').",
            },
            {
              'type': 'string',
              'description': "Member name (e.g., 'visualDensity').",
            },
            {
              'type': 'string',
              'description': "Category of member (e.g., 'property').",
            },
          ],
        },
      },
    ],
  }),
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

// ---------------------------------------------------------------------------
// listLibraries
// ---------------------------------------------------------------------------

final _listLibrariesTool = Tool(
  name: 'listLibraries',
  title: 'List all available Flutter/Dart library slugs',
  description:
      'Returns all available library slugs — the URI-safe identifiers used '
      'in resource URIs (flutter-docs://api/{library_slug}/...) and as the '
      'libraryHint parameter. Library slugs do not always match the library '
      'display name (e.g., dart:io uses slug dart-io; package libraries use '
      'slugs like package-material_color_utilities_blend_blend). Call this '
      'to discover available library_slug values or confirm the correct library '
      'slug before constructing resource URIs.',
  inputSchema: Schema.object(properties: {}),
);

FutureOr<CallToolResult> _listLibraries(
  CallToolRequest request,
  DocDatabase db,
) {
  final slugs = db.listLibraries();
  return CallToolResult(content: [TextContent(text: jsonEncode(slugs))]);
}
