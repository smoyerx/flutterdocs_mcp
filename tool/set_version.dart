import 'dart:io';

import 'package:args/args.dart';
import 'package:sqlite3/sqlite3.dart';

/// Updates all version strings and constants across the project to a new
/// semver, keeping every derived location in sync with a single command.
///
/// Usage: dart run tool/set_version.dart `<major.minor.patch>` [--db `<path>`]
///
/// Files updated:
///   - pubspec.yaml                                          (version: field)
///   - lib/src/version.dart                                  (kVersion, kDbVersion)
///   - make_docs/pyproject.toml                              (version = field)
///   - make_docs/src/flutterdocs/_shared/version.py          (VERSION, DB_VERSION)
///
/// Optional:
///   --db `<path>`   Path to a sqlite3 documentation database file. When
///                   provided, sets PRAGMA user_version of that file to the same
///                   integer (major * 1_000_000 + minor * 1_000 + patch) that
///                   load.py writes when it creates the database. Use this when
///                   releasing a version that does not change the database schema
///                   or content (e.g. a README-only change).
void main(List<String> args) {
  final parser = ArgParser()
    ..addOption('db', valueHelp: 'path', help: 'Path to docs sqlite3 file');

  final ArgResults parsed;
  try {
    parsed = parser.parse(args);
  } on FormatException catch (e) {
    stderr.writeln('Error: ${e.message}');
    stderr.writeln(
      'Usage: dart run tool/set_version.dart <major.minor.patch> [--db <path>]',
    );
    exit(1);
  }

  if (parsed.rest.length != 1) {
    stderr.writeln(
      'Usage: dart run tool/set_version.dart <major.minor.patch> [--db <path>]',
    );
    exit(1);
  }

  final version = parsed.rest[0];
  final parts = version.split('.');
  if (parts.length != 3) {
    stderr.writeln(
      'Error: version must be in major.minor.patch format: $version',
    );
    exit(1);
  }

  final major = int.tryParse(parts[0]);
  final minor = int.tryParse(parts[1]);
  final patch = int.tryParse(parts[2]);
  if (major == null || minor == null || patch == null) {
    stderr.writeln(
      'Error: version components must be non-negative integers: $version',
    );
    exit(1);
  }

  final dbVersion = major * 1000000 + minor * 1000 + patch;

  _replacePattern(
    'pubspec.yaml',
    RegExp(r'^version: .+$', multiLine: true),
    'version: $version',
  );

  _replacePattern(
    'lib/src/version.dart',
    RegExp(r"^const String kVersion = '.+';$", multiLine: true),
    "const String kVersion = '$version';",
  );
  _replacePattern(
    'lib/src/version.dart',
    RegExp(r'^const int kDbVersion = \d+;$', multiLine: true),
    'const int kDbVersion = $dbVersion;',
  );

  _replacePattern(
    'make_docs/pyproject.toml',
    RegExp(r'^version = ".+"$', multiLine: true),
    'version = "$version"',
  );

  _replacePattern(
    'make_docs/src/flutterdocs/_shared/version.py',
    RegExp(r'^VERSION = ".+"$', multiLine: true),
    'VERSION = "$version"',
  );
  _replacePattern(
    'make_docs/src/flutterdocs/_shared/version.py',
    RegExp(r'^DB_VERSION = \d+$', multiLine: true),
    'DB_VERSION = $dbVersion',
  );

  stdout.writeln('Version updated to $version  (DB_VERSION=$dbVersion)');

  final dbPath = parsed['db'] as String?;
  if (dbPath != null) {
    final dbFile = File(dbPath);
    if (!dbFile.existsSync()) {
      stderr.writeln('Error: database file not found: $dbPath');
      exit(1);
    }
    Database? db;
    try {
      db = sqlite3.open(dbPath);
      db.execute('PRAGMA user_version = $dbVersion');
      stdout.writeln('user_version set to $dbVersion in $dbPath');
    } on SqliteException catch (e) {
      stderr.writeln('Error: failed to set user_version in $dbPath: $e');
      exit(1);
    } finally {
      db?.close();
    }
  }
}

/// Replaces the first (and expected only) match of [pattern] in [filePath]
/// with [replacement]. Exits with code 1 if the file is not found or the
/// pattern produces no match.
void _replacePattern(String filePath, RegExp pattern, String replacement) {
  final file = File(filePath);
  if (!file.existsSync()) {
    stderr.writeln('Error: file not found: $filePath');
    exit(1);
  }
  final original = file.readAsStringSync();
  final updated = original.replaceAll(pattern, replacement);
  if (!pattern.hasMatch(original)) {
    stderr.writeln('Warning: no match found in $filePath for: $pattern');
  }
  file.writeAsStringSync(updated);
}
