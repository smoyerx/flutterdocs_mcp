import 'dart:io';

/// Updates all version strings and constants across the project to a new
/// semver, keeping every derived location in sync with a single command.
///
/// Usage: dart run tool/set_version.dart `<major.minor.patch>`
///
/// Files updated:
///   - pubspec.yaml                                          (version: field)
///   - lib/src/version.dart                                  (kVersion, kDbVersion)
///   - make_docs/pyproject.toml                              (version = field)
///   - make_docs/src/flutterdocs/_shared/version.py          (VERSION, DB_VERSION)
void main(List<String> args) {
  if (args.length != 1) {
    stderr.writeln('Usage: dart run tool/set_version.dart <major.minor.patch>');
    exit(1);
  }

  final version = args[0];
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
