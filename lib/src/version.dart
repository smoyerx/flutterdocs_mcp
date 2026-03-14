// Embedded application version — kept in sync with `pubspec.yaml` by
// `dart run tool/set_version.dart`.

/// The application version string (semver).
const String kVersion = '0.1.1';

/// The expected database `PRAGMA user_version`.
///
/// Encoded as `major * 1_000_000 + minor * 1_000 + patch`.
/// Set by `load.py` when creating the docs database and validated against
/// the `--db` database file on server startup.
const int kDbVersion = 1001;
