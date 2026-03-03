import 'package:dart_mcp/server.dart';
import 'package:json_rpc_2/json_rpc_2.dart';

import 'db.dart';

/// Registers the three resource templates ([libraryIndex],
/// [entityDocumentation], [memberDocumentation]) on [server].
void registerResources(ResourcesSupport server, DocDatabase db) {
  _registerLibraryIndex(server, db);
  _registerEntityDocumentation(server, db);
  _registerMemberDocumentation(server, db);
}

// ---------------------------------------------------------------------------
// Shared helpers
// ---------------------------------------------------------------------------

const _scheme = 'flutter-docs';
const _apiPrefix = 'flutter-docs://api/';

/// Splits a `flutter-docs://api/...` URI into path segments.
///
/// Returns `null` if the URI does not start with [_apiPrefix].
List<String>? _apiSegments(String uri) {
  if (!uri.startsWith(_apiPrefix)) return null;
  final path = uri.substring(_apiPrefix.length);
  if (path.isEmpty) return null;
  return path.split('/');
}

Never _notFound(String uri) =>
    throw RpcException(-32002, 'Resource not found', data: {'uri': uri});

// ---------------------------------------------------------------------------
// libraryIndex  flutter-docs://api/{library_slug}
// ---------------------------------------------------------------------------

final _libraryIndexTemplate = ResourceTemplate(
  uriTemplate: '$_scheme://api/{library_slug}',
  name: 'libraryIndex',
  title: 'Flutter/Dart library documentation index',
  description:
      'High-level summary of the library and all of its entities (classes, '
      'mixins, enums, extensions, extension types, typedefs, top-level '
      'functions, top-level constants). Contains embedded navigation links '
      '(resource URIs) to the detailed documentation for each entity. '
      'Note: The library_slug value in the URI template is a URI slug '
      '(not the library display name). '
      'Call listLibraries to see all available library_slug values.',
  annotations: Annotations(audience: [Role.user, Role.assistant]),
);

void _registerLibraryIndex(ResourcesSupport server, DocDatabase db) {
  server.addResourceTemplate(_libraryIndexTemplate, (request) {
    final segments = _apiSegments(request.uri);
    if (segments == null || segments.length != 1) return null;

    final library = Uri.decodeComponent(segments[0]);
    final content = db.libraryIndex(library);
    if (content == null) _notFound(request.uri);

    return ReadResourceResult(
      contents: [TextResourceContents(text: content, uri: request.uri)],
    );
  });
}

// ---------------------------------------------------------------------------
// entityDocumentation  flutter-docs://api/{library_slug}/{entity}
// ---------------------------------------------------------------------------

final _entityDocumentationTemplate = ResourceTemplate(
  uriTemplate: '$_scheme://api/{library_slug}/{entity}',
  name: 'entityDocumentation',
  title: 'Flutter/Dart entity documentation',
  description:
      'Detailed documentation for the Flutter/Dart entity (class, mixin, '
      'enum, extension, extension type, typedef, top-level function, '
      'top-level constant) in the specified library. Includes a summary of '
      'all its members (constructors, properties, methods, operators, '
      'constants, static methods), with embedded navigation links (resource '
      'URIs) to the detailed documentation for each member. '
      'Note: The library_slug value in the URI template is a URI slug '
      '(not the library display name). '
      'Call listLibraries to see all available library_slug values.',
  annotations: Annotations(audience: [Role.user, Role.assistant]),
);

void _registerEntityDocumentation(ResourcesSupport server, DocDatabase db) {
  server.addResourceTemplate(_entityDocumentationTemplate, (request) {
    final segments = _apiSegments(request.uri);
    if (segments == null || segments.length != 2) return null;

    final library = Uri.decodeComponent(segments[0]);
    final entity = Uri.decodeComponent(segments[1]);
    final content = db.entityDocumentation(library, entity);
    if (content == null) _notFound(request.uri);

    return ReadResourceResult(
      contents: [TextResourceContents(text: content, uri: request.uri)],
    );
  });
}

// ---------------------------------------------------------------------------
// memberDocumentation  flutter-docs://api/{library_slug}/{entity}/{member}
// ---------------------------------------------------------------------------

final _memberDocumentationTemplate = ResourceTemplate(
  uriTemplate: '$_scheme://api/{library_slug}/{entity}/{member}',
  name: 'memberDocumentation',
  title: 'Flutter/Dart member documentation',
  description:
      'Detailed documentation for the Flutter/Dart member (constructor, '
      'property, method, operator, constant, static method) of the specified '
      'entity in the specified library. '
      'Note: The library_slug value in the URI template is a URI slug '
      '(not the library display name). '
      'Call listLibraries to see all available library_slug values.',
  annotations: Annotations(audience: [Role.user, Role.assistant]),
);

void _registerMemberDocumentation(ResourcesSupport server, DocDatabase db) {
  server.addResourceTemplate(_memberDocumentationTemplate, (request) {
    final segments = _apiSegments(request.uri);
    if (segments == null || segments.length != 3) return null;

    final library = Uri.decodeComponent(segments[0]);
    final entity = Uri.decodeComponent(segments[1]);
    final member = Uri.decodeComponent(segments[2]);
    final content = db.memberDocumentation(library, entity, member);
    if (content == null) _notFound(request.uri);

    return ReadResourceResult(
      contents: [TextResourceContents(text: content, uri: request.uri)],
    );
  });
}
