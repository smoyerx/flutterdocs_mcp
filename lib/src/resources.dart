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
// Annotations common to all resources.
// ---------------------------------------------------------------------------

final _annotations = Annotations(audience: [Role.user, Role.assistant]);

// ---------------------------------------------------------------------------
// libraryIndex  flutter-docs://api/{library_slug}
// ---------------------------------------------------------------------------

final _libraryIndexTemplate = ResourceTemplate(
  uriTemplate: '$_scheme://api/{library_slug}',
  name: 'libraryIndex',
  title: 'Flutter/Dart library documentation',
  description:
      'Summary of the library and its entities (classes, mixins, enums, '
      'extensions, extension types, typedefs, top-level functions/constants). '
      'The markdown content returned embeds actionable resource URIs '
      '($_scheme://) as navigation links.',
  annotations: _annotations,
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
      'enum, extension, extension type, typedef, top-level function/constant). '
      'The markdown content returned embeds actionable resource URIs '
      '($_scheme://) as navigation links.',
  annotations: _annotations,
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
      'property, method, operator, constant, static method). '
      'The markdown content returned embeds actionable resource URIs '
      '($_scheme://) as navigation links.',
  annotations: _annotations,
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
