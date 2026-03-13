import 'dart:io' as io;

import 'package:args/args.dart';
import 'package:dart_mcp/server.dart';
import 'package:dart_mcp/stdio.dart';

import 'db.dart';
import 'resources.dart';
import 'tools.dart';
import 'version.dart';

/// An MCP server for Flutter/Dart API documentation.
///
/// The server connects over the stdio transport and provides tools and resource
/// templates for navigating and fetching Flutter/Dart API documentation.
base class FlutterDocsMcpServer extends MCPServer
    with ToolsSupport, ResourcesSupport, LoggingSupport {
  /// Constructs a [FlutterDocsMcpServer] with the given stdio channel and
  /// documentation database.
  FlutterDocsMcpServer.fromChannel(super.channel, DocDatabase db)
    : super.fromStreamChannel(
        implementation: Implementation(
          name: 'flutter-docs',
          version: kVersion,
          title: 'Flutter/Dart API Documentation',
          description:
              'Flutter/Dart API documentation for AI assistants and tools.',
        ),
        instructions:
            'Workflow: (1) use listLibraries, lookupEntity, lookupMember, or '
            'searchDocumentation to obtain library slug and identifier values; '
            '(2) call getDocumentation with a constructed flutter-docs://api/... '
            'URI to fetch markdown content; (3) follow any embedded '
            'flutter-docs:// links in that markdown by passing them directly '
            'to getDocumentation. '
            'URI shapes: flutter-docs://api/{library_slug} for a library, '
            'flutter-docs://api/{library_slug}/{entity} for an '
            'entity (class, mixin, etc.), '
            'flutter-docs://api/{library_slug}/{entity}/{member} for a '
            'member (constructor, property, method, etc.). '
            'Only use identifiers from tool results or embedded links — never '
            'guess URIs or rely on internal training data. '
            'Note: library slugs differ from display names '
            '(e.g., dart:io → dart-io). '
            'Note: flutter-docs:// URIs are also accessible as resources to '
            'resource-capable clients.',
      ) {
    registerTools(this, db);
    registerResources(this, db);
  }

  /// Parses [args], validates the `--db` path, and starts the server on stdio.
  ///
  /// Exits with code 1 if `--db` is missing, the file cannot be read, or the
  /// database version does not match [kDbVersion].
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
      )
      ..addFlag(
        'version',
        negatable: false,
        help: 'Print the server version and exit.',
      )
      ..addFlag(
        'db-version',
        negatable: false,
        help: 'Print the version of the --db database file and exit.',
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

    if (results.flag('version')) {
      io.stdout.writeln(kVersion);
      return;
    }

    final dbPath = results.option('db');
    final dbFile = dbPath != null ? io.File(dbPath) : null;

    if (results.flag('db-version')) {
      if (dbPath == null) {
        io.stderr.writeln('Error: --db is required with --db-version.');
        io.stderr.writeln(parser.usage);
        io.exit(1);
      }
      if (!dbFile!.existsSync()) {
        io.stderr.writeln('Error: database file not found: $dbPath');
        io.exit(1);
      }
      late int userVersion;
      try {
        userVersion = DocDatabase.readUserVersion(dbPath);
      } catch (e) {
        io.stderr.writeln('Error: failed to read database version: $e');
        io.exit(1);
      }
      if (userVersion == 0) {
        io.stderr.writeln('Error: database has no version information.');
        io.exit(1);
      }
      io.stdout.writeln(_dbVersionToSemver(userVersion));
      return;
    }

    if (dbPath == null) {
      io.stderr.writeln('Error: --db is required.');
      io.stderr.writeln(parser.usage);
      io.exit(1);
    }
    if (!dbFile!.existsSync()) {
      io.stderr.writeln('Error: database file not found: $dbPath');
      io.exit(1);
    }

    late int dbUserVersion;
    try {
      dbUserVersion = DocDatabase.readUserVersion(dbPath);
    } catch (e) {
      io.stderr.writeln('Error: failed to read database version: $e');
      io.exit(1);
    }
    if (dbUserVersion != kDbVersion) {
      io.stderr.writeln(
        'Error: database version mismatch: '
        'server expects ${_dbVersionToSemver(kDbVersion)}, '
        'database has ${_dbVersionToSemver(dbUserVersion)}.',
      );
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

/// Decodes a db version integer (major * 1_000_000 + minor * 1_000 + patch)
/// back to a semver string.
String _dbVersionToSemver(int v) {
  final major = v ~/ 1000000;
  final minor = (v ~/ 1000) % 1000;
  final patch = v % 1000;
  return '$major.$minor.$patch';
}
