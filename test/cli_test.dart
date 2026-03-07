import 'dart:io';

import 'package:flutterdocs_mcp/src/version.dart';
import 'package:sqlite3/sqlite3.dart';
import 'package:test/test.dart';

/// Directory holding the compiled CLI binary. Created once in [setUpAll] and
/// deleted in [tearDownAll].
late Directory _binDir;

/// Path to the AOT-compiled CLI binary.
///
/// Using a pre-compiled native executable instead of `dart run` prevents
/// build-hook writes from racing with the test runner's memory-mapped native
/// libraries (.so files), which would otherwise cause a SIGBUS crash in
/// concurrently running test suites.
late String _cliExe;

/// Runs the compiled CLI binary as a subprocess and returns the result.
Future<ProcessResult> _runCli(List<String> args) => Process.run(_cliExe, args);

void main() {
  setUpAll(() async {
    _binDir = await Directory.systemTemp.createTemp('flutterdocs_cli_bin_');
    // dart build cli -o <dir> writes the bundle to <dir>/bundle/.
    final result = await Process.run('dart', [
      'build',
      'cli',
      '-o',
      _binDir.path,
    ]);
    if (result.exitCode != 0) {
      throw StateError('dart build cli failed:\n${result.stderr}');
    }
    _cliExe = '${_binDir.path}/bundle/bin/flutterdocs_mcp';
  });

  tearDownAll(() async {
    await _binDir.delete(recursive: true);
  });

  // -------------------------------------------------------------------------
  // --version flag
  // -------------------------------------------------------------------------

  group('--version flag', () {
    test('exits 0 and prints version string to stdout', () async {
      final result = await _runCli(['--version']);
      expect(result.exitCode, 0);
      expect(result.stdout as String, contains(kVersion));
    });
  });

  // -------------------------------------------------------------------------
  // --db-version flag
  // -------------------------------------------------------------------------

  group('--db-version flag', () {
    late Directory tempDir;

    setUp(() async {
      tempDir = await Directory.systemTemp.createTemp('flutterdocs_cli_test_');
    });

    tearDown(() async {
      await tempDir.delete(recursive: true);
    });

    test('exits 1 with error when --db is not provided', () async {
      final result = await _runCli(['--db-version']);
      expect(result.exitCode, 1);
      expect(result.stderr as String, contains('Error'));
    });

    test('exits 1 with error when db file does not exist', () async {
      final result = await _runCli([
        '--db-version',
        '--db',
        '${tempDir.path}/nonexistent.db',
      ]);
      expect(result.exitCode, 1);
      expect(result.stderr as String, contains('Error'));
    });

    test(
      'exits 1 with error when db has no version information (user_version=0)',
      () async {
        final dbPath = '${tempDir.path}/unversioned.db';
        final db = sqlite3.open(dbPath);
        db.execute('CREATE TABLE t (id INTEGER)');
        // user_version defaults to 0 — deliberately not set
        db.close();

        final result = await _runCli(['--db-version', '--db', dbPath]);
        expect(result.exitCode, 1);
        expect(result.stderr as String, contains('Error'));
      },
    );

    test(
      'exits 0 and prints semver string when db has valid user_version',
      () async {
        final dbPath = '${tempDir.path}/versioned.db';
        final db = sqlite3.open(dbPath);
        db.execute('CREATE TABLE t (id INTEGER)');
        db.execute('PRAGMA user_version = $kDbVersion');
        db.close();

        final result = await _runCli(['--db-version', '--db', dbPath]);
        expect(result.exitCode, 0);
        expect(result.stdout as String, contains(kVersion));
      },
    );
  });

  // -------------------------------------------------------------------------
  // version mismatch check on startup
  // -------------------------------------------------------------------------

  group('version mismatch', () {
    late Directory tempDir;

    setUp(() async {
      tempDir = await Directory.systemTemp.createTemp(
        'flutterdocs_cli_mismatch_',
      );
    });

    tearDown(() async {
      await tempDir.delete(recursive: true);
    });

    test(
      'exits 1 with error when db user_version does not match kDbVersion',
      () async {
        final dbPath = '${tempDir.path}/mismatch.db';
        final db = sqlite3.open(dbPath);
        // Any value that is not kDbVersion triggers the mismatch error; the
        // database does not need a valid schema since the version check runs
        // before DocDatabase is constructed.
        db.execute('PRAGMA user_version = 999');
        db.close();

        final result = await _runCli(['--db', dbPath]);
        expect(result.exitCode, 1);
        expect(result.stderr as String, contains('Error'));
      },
    );
  });
}
