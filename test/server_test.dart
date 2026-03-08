import 'dart:convert';
import 'dart:io';

import 'package:dart_mcp/client.dart';
import 'package:flutterdocs_mcp/src/db.dart';
import 'package:flutterdocs_mcp/src/server.dart';
import 'package:json_rpc_2/json_rpc_2.dart';
import 'package:stream_channel/stream_channel.dart';
import 'package:test/test.dart';

// ---------------------------------------------------------------------------
// Test fixtures and shared state
// ---------------------------------------------------------------------------

late File _testDb;
late DocDatabase _db;
late MCPClient _client;
late ServerConnection _server;
bool _setupDone = false;

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/// Decodes the JSON-encoded tool result and returns [total, resultList].
///
/// [resultList] is a `List<List<dynamic>>` where each inner list is a tuple.
(int total, List<List<dynamic>> results) _decodeTool(CallToolResult result) {
  expect(result.isError, isNot(true));
  final text = (result.content.first as TextContent).text;
  final decoded = jsonDecode(text) as Map<String, dynamic>;
  return (
    decoded['total'] as int,
    (decoded['results'] as List<dynamic>).cast<List<dynamic>>(),
  );
}

/// Starts the server in-process and connects the shared [_client] to it.
///
/// Uses an in-memory [StreamChannelController] so no subprocess is spawned
/// and `dart run`'s "Running build hooks…" output cannot contaminate the
/// MCP stdio channel.
Future<void> _startServer() async {
  _client = MCPClient(
    Implementation(name: 'flutterdocs_mcp_test_client', version: '0.1.0'),
  );

  final controller = StreamChannelController<String>(allowForeignErrors: false);
  FlutterDocsMcpServer.fromChannel(controller.local, _db);
  _server = _client.connectServer(controller.foreign);

  final initResult = await _server.initialize(
    InitializeRequest(
      protocolVersion: ProtocolVersion.latestSupported,
      capabilities: _client.capabilities,
      clientInfo: _client.implementation,
    ),
  );

  expect(initResult.capabilities.tools, isNotNull);
  expect(initResult.capabilities.resources, isNotNull);

  _server.notifyInitialized();
  _setupDone = true;
}

Future<void> _stopServer() async {
  if (!_setupDone) return;
  await _client.shutdown();
  _db.close();
}

// ---------------------------------------------------------------------------
// Test database setup
// ---------------------------------------------------------------------------

/// Loads [suite] into [_testDb] using `uv run load` in the `make_docs/`
/// working directory.
///
/// Must be run from the repository root.
Future<void> _loadSuite(String suite) async {
  final result = await Process.run('uv', [
    'run',
    'load',
    '-d',
    'tests/load/integration/samples',
    '-s',
    suite,
    '-o',
    _testDb.path,
  ], workingDirectory: 'make_docs');
  if (result.exitCode != 0) {
    throw StateError('uv run load failed for $suite:\n${result.stderr}');
  }
}

// ---------------------------------------------------------------------------
// main
// ---------------------------------------------------------------------------

void main() {
  setUpAll(() async {
    // Do NOT pre-create the file — open_or_create_db() creates the schema
    // only when the file does not exist yet.
    _testDb = File.fromUri(
      Directory.systemTemp.uri.resolve('flutterdocs_mcp_server_test.db'),
    );
    // Remove any leftover file from a previous interrupted run.
    if (_testDb.existsSync()) await _testDb.delete();

    for (final suite in ['material', 'widgets']) {
      await _loadSuite(suite);
    }

    _db = DocDatabase(_testDb.path);
    await _startServer();
  });

  tearDownAll(() async {
    await _stopServer();
    if (_testDb.existsSync()) await _testDb.delete();
  });

  // -------------------------------------------------------------------------
  // lookupEntity tool
  // -------------------------------------------------------------------------

  group('lookupEntity tool', () {
    test('hit — single library', () async {
      final result = await _server.callTool(
        CallToolRequest(name: 'lookupEntity', arguments: {'name': 'ListTile'}),
      );
      final (total, results) = _decodeTool(result);
      expect(total, greaterThan(0));
      expect(results, isNotEmpty);
      final libraries = results.map((r) => r[0] as String).toList();
      expect(libraries, contains('material'));
      final entities = results.map((r) => r[1] as String).toList();
      expect(entities, everyElement('ListTile'));
    });

    test('miss — unknown entity', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'lookupEntity',
          arguments: {'name': 'NoSuchEntity42'},
        ),
      );
      final (total, results) = _decodeTool(result);
      expect(total, 0);
      expect(results, isEmpty);
    });
  });

  // -------------------------------------------------------------------------
  // lookupMember tool
  // -------------------------------------------------------------------------

  group('lookupMember tool', () {
    test('hit — no library hint', () async {
      final result = await _server.callTool(
        CallToolRequest(name: 'lookupMember', arguments: {'name': 'autofocus'}),
      );
      final (total, results) = _decodeTool(result);
      expect(total, greaterThan(0));
      expect(results, isNotEmpty);
      final members = results.map((r) => r[2] as String).toList();
      expect(members, everyElement('autofocus'));
    });

    test('hit — multiple results for common member name', () async {
      // enableFeedback appears on both ListTile (native) and InkWell
      // (inherited) in the material library.
      final result = await _server.callTool(
        CallToolRequest(
          name: 'lookupMember',
          arguments: {'name': 'enableFeedback'},
        ),
      );
      final (total, _) = _decodeTool(result);
      expect(total, greaterThan(1));
    });

    test('hit — with library hint narrows results', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'lookupMember',
          arguments: {'name': 'autofocus', 'librarySlugHint': 'material'},
        ),
      );
      final (total, results) = _decodeTool(result);
      expect(total, greaterThan(0));
      final libraries = results.map((r) => r[0] as String).toList();
      expect(libraries, everyElement('material'));
    });

    test('miss — unknown member name', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'lookupMember',
          arguments: {'name': 'noSuchMember99'},
        ),
      );
      final (total, results) = _decodeTool(result);
      expect(total, 0);
      expect(results, isEmpty);
    });
  });

  // -------------------------------------------------------------------------
  // listLibraries tool
  // -------------------------------------------------------------------------

  group('listLibraries tool', () {
    test('returns non-empty sorted list of slug-displayName pairs', () async {
      final result = await _server.callTool(
        CallToolRequest(name: 'listLibraries', arguments: {}),
      );
      expect(result.isError, isNot(true));
      final text = (result.content.first as TextContent).text;
      final decoded = jsonDecode(text) as Map<String, dynamic>;
      final total = decoded['total'] as int;
      final results = (decoded['results'] as List<dynamic>)
          .map((e) => e as List<dynamic>)
          .toList();
      expect(total, isPositive);
      expect(results, isNotEmpty);
      final slugs = results.map((r) => r[0] as String).toList();
      expect(slugs, contains('material'));
      expect(slugs, contains('widgets'));
      expect(slugs, equals([...slugs]..sort()));
    });
  });

  // -------------------------------------------------------------------------
  // libraryIndex resource
  // -------------------------------------------------------------------------

  group('libraryIndex resource', () {
    test('returns content for valid library', () async {
      final result = await _server.readResource(
        ReadResourceRequest(uri: 'flutter-docs://api/material'),
      );
      expect(result.contents, isNotEmpty);
      final text = (result.contents.first as TextResourceContents).text;
      expect(text, isNotEmpty);
    });

    test('throws RpcException(-32002) for unknown library', () async {
      expect(
        () => _server.readResource(
          ReadResourceRequest(uri: 'flutter-docs://api/unknownLib99'),
        ),
        throwsA(isA<RpcException>().having((e) => e.code, 'code', -32002)),
      );
    });
  });

  // -------------------------------------------------------------------------
  // entityDocumentation resource
  // -------------------------------------------------------------------------

  group('entityDocumentation resource', () {
    test('returns content for valid entity', () async {
      final result = await _server.readResource(
        ReadResourceRequest(uri: 'flutter-docs://api/material/ListTile'),
      );
      expect(result.contents, isNotEmpty);
      final text = (result.contents.first as TextResourceContents).text;
      expect(text, isNotEmpty);
    });

    test('throws RpcException(-32002) for unknown entity', () async {
      expect(
        () => _server.readResource(
          ReadResourceRequest(
            uri: 'flutter-docs://api/material/NoSuchEntity99',
          ),
        ),
        throwsA(isA<RpcException>().having((e) => e.code, 'code', -32002)),
      );
    });

    test('throws RpcException(-32002) for unknown library', () async {
      expect(
        () => _server.readResource(
          ReadResourceRequest(uri: 'flutter-docs://api/unknownLib99/ListTile'),
        ),
        throwsA(isA<RpcException>().having((e) => e.code, 'code', -32002)),
      );
    });
  });

  // -------------------------------------------------------------------------
  // memberDocumentation resource
  // -------------------------------------------------------------------------

  group('memberDocumentation resource', () {
    test('returns content for valid member', () async {
      final result = await _server.readResource(
        ReadResourceRequest(
          uri: 'flutter-docs://api/material/ListTile/autofocus',
        ),
      );
      expect(result.contents, isNotEmpty);
      final text = (result.contents.first as TextResourceContents).text;
      expect(text, isNotEmpty);
    });

    test('throws RpcException(-32002) for unknown member', () async {
      expect(
        () => _server.readResource(
          ReadResourceRequest(
            uri: 'flutter-docs://api/material/ListTile/noSuchMember99',
          ),
        ),
        throwsA(isA<RpcException>().having((e) => e.code, 'code', -32002)),
      );
    });

    test('throws RpcException(-32002) for unknown entity', () async {
      expect(
        () => _server.readResource(
          ReadResourceRequest(
            uri: 'flutter-docs://api/material/NoSuchEntity99/autofocus',
          ),
        ),
        throwsA(isA<RpcException>().having((e) => e.code, 'code', -32002)),
      );
    });

    test('throws RpcException(-32002) for unknown library', () async {
      expect(
        () => _server.readResource(
          ReadResourceRequest(
            uri: 'flutter-docs://api/unknownLib99/ListTile/autofocus',
          ),
        ),
        throwsA(isA<RpcException>().having((e) => e.code, 'code', -32002)),
      );
    });
  });

  // -------------------------------------------------------------------------
  // searchDocumentation tool
  // -------------------------------------------------------------------------

  group('searchDocumentation tool', () {
    test('hit — returns results with total, entities, and excerpts', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'searchDocumentation',
          arguments: {'query': 'widget'},
        ),
      );
      final (total, results) = _decodeTool(result);
      expect(total, greaterThan(0));
      expect(results, isNotEmpty);
      // Each result is a 3-element array: [library_slug, entity, excerpt].
      for (final r in results) {
        expect(r, hasLength(3));
        expect(r[0], isA<String>());
        expect(r[1], isA<String>());
        expect(r[2], isA<String>());
      }
    });

    test('miss — returns total 0 and empty results', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'searchDocumentation',
          arguments: {'query': 'xyzzy99nonexistent'},
        ),
      );
      final (total, results) = _decodeTool(result);
      expect(total, 0);
      expect(results, isEmpty);
    });

    test('symbol-only input — returns total 0 and empty results', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'searchDocumentation',
          arguments: {'query': '--- *** :::'},
        ),
      );
      final (total, results) = _decodeTool(result);
      expect(total, 0);
      expect(results, isEmpty);
    });
  });

  // -------------------------------------------------------------------------
  // getDocumentation tool
  // -------------------------------------------------------------------------

  group('getDocumentation tool', () {
    test('library hit — returns non-empty markdown', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'getDocumentation',
          arguments: {'uri': 'flutter-docs://api/material'},
        ),
      );
      expect(result.isError, isNot(true));
      final text = (result.content.first as TextContent).text;
      expect(text, isNotEmpty);
    });

    test('entity hit — returns non-empty markdown', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'getDocumentation',
          arguments: {'uri': 'flutter-docs://api/material/ListTile'},
        ),
      );
      expect(result.isError, isNot(true));
      final text = (result.content.first as TextContent).text;
      expect(text, isNotEmpty);
    });

    test('member hit — returns non-empty markdown', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'getDocumentation',
          arguments: {'uri': 'flutter-docs://api/material/ListTile/autofocus'},
        ),
      );
      expect(result.isError, isNot(true));
      final text = (result.content.first as TextContent).text;
      expect(text, isNotEmpty);
    });

    test('miss — unknown library returns isError true', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'getDocumentation',
          arguments: {'uri': 'flutter-docs://api/unknownLib99'},
        ),
      );
      expect(result.isError, true);
    });

    test('miss — unknown entity returns isError true', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'getDocumentation',
          arguments: {'uri': 'flutter-docs://api/material/NoSuchEntity99'},
        ),
      );
      expect(result.isError, true);
    });

    test('miss — unknown member returns isError true', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'getDocumentation',
          arguments: {
            'uri': 'flutter-docs://api/material/ListTile/noSuchMember99',
          },
        ),
      );
      expect(result.isError, true);
    });

    test('invalid URI — too many segments returns isError true', () async {
      final result = await _server.callTool(
        CallToolRequest(
          name: 'getDocumentation',
          arguments: {'uri': 'flutter-docs://api/a/b/c/d'},
        ),
      );
      expect(result.isError, true);
    });
  });
}
