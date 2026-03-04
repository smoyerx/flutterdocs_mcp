import 'dart:io' as io;

import 'package:args/args.dart';
import 'package:dart_mcp/server.dart';
import 'package:dart_mcp/stdio.dart';

import 'db.dart';
import 'resources.dart';
import 'tools.dart';

/// An MCP server that serves Flutter/Dart API documentation.
///
/// The server connects over the stdio transport and provides two tools
/// ([lookupEntity], [lookupMember]) and three resource templates
/// ([libraryIndex], [entityDocumentation], [memberDocumentation]).
base class FlutterDocsMcpServer extends MCPServer
    with ToolsSupport, ResourcesSupport, LoggingSupport {
  FlutterDocsMcpServer.fromChannel(super.channel, DocDatabase db)
    : super.fromStreamChannel(
        implementation: Implementation(
          name: 'flutterdocs_mcp',
          version: '0.1.0',
        ),
        instructions:
            'This server provides tools and resources for navigating '
            'Flutter/Dart API documentation. Use searchDocumentation to find '
            'entities by keyword or phrase. Use lookupEntity to find which '
            'library an entity belongs to, and lookupMember to find which '
            'entity a member belongs to. Then use the resource URIs to '
            'retrieve the full documentation.',
      ) {
    registerTools(this, db);
    registerResources(this, db);
  }

  /// Parses [args], validates the `--db` path, and starts the server on stdio.
  ///
  /// Exits with code 1 if `--db` is missing or the file cannot be read.
  static void run(List<String> args) {
    final parser = ArgParser()
      ..addOption(
        'db',
        help: 'Path to the sqlite3 documentation database file.',
        valueHelp: 'path',
      )
      ..addFlag(
        'help',
        abbr: 'h',
        negatable: false,
        help: 'Print usage information.',
      );

    late ArgResults results;
    try {
      results = parser.parse(args);
    } on FormatException catch (e) {
      io.stderr.writeln(e.message);
      io.stderr.writeln(parser.usage);
      io.exit(1);
    }

    if (results.flag('help')) {
      io.stdout.writeln(
        'Usage: flutterdocs_mcp --db <path>\n\n${parser.usage}',
      );
      return;
    }

    final dbPath = results.option('db');
    if (dbPath == null) {
      io.stderr.writeln('Error: --db is required.');
      io.stderr.writeln(parser.usage);
      io.exit(1);
    }

    final dbFile = io.File(dbPath);
    if (!dbFile.existsSync()) {
      io.stderr.writeln('Error: database file not found: $dbPath');
      io.exit(1);
    }

    late DocDatabase db;
    try {
      db = DocDatabase(dbPath);
    } catch (e) {
      io.stderr.writeln('Error: failed to open database: $e');
      io.exit(1);
    }

    FlutterDocsMcpServer.fromChannel(
      stdioChannel(input: io.stdin, output: io.stdout),
      db,
    );
  }
}
