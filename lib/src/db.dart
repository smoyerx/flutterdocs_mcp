import 'package:sqlite3/sqlite3.dart';

/// In-memory representation of a library record from the `library` table.
final class LibraryRecord {
  const LibraryRecord({
    required this.id,
    required this.name,
    required this.contentMarkdown,
  });

  final int id;
  final String name;
  final String contentMarkdown;
}

/// Wraps a sqlite3 database and provides typed query methods for Flutter/Dart
/// documentation retrieval.
///
/// At construction time, [DocDatabase] opens the database in read-only mode,
/// loads the four small lookup tables entirely into memory, and compiles all
/// runtime SQL statements into prepared statements. These are reused across
/// all subsequent requests.
final class DocDatabase {
  DocDatabase(String dbPath)
    : _db = sqlite3.open(dbPath, mode: OpenMode.readOnly) {
    _loadCaches();
    _prepareStatements();
  }

  final Database _db;

  // ---------------------------------------------------------------------------
  // In-memory caches
  // ---------------------------------------------------------------------------

  final Map<int, String> _identifierIdToName = {};
  final Map<String, int> _identifierNameToId = {};
  final Map<int, String> _entityTypeIdToName = {};
  final Map<int, String> _memberTypeIdToName = {};
  final Map<int, LibraryRecord> _libraryById = {};
  final Map<String, LibraryRecord> _libraryByName = {};

  // ---------------------------------------------------------------------------
  // Prepared statements
  // ---------------------------------------------------------------------------

  late final PreparedStatement _entityCountStmt;
  late final PreparedStatement _entityResultsStmt;
  late final PreparedStatement _memberCountNoHintStmt;
  late final PreparedStatement _memberCountWithHintStmt;
  late final PreparedStatement _memberResultsNoHintStmt;
  late final PreparedStatement _memberResultsWithHintStmt;
  late final PreparedStatement _entityDocStmt;
  late final PreparedStatement _memberDocStmt;

  // ---------------------------------------------------------------------------
  // Startup helpers
  // ---------------------------------------------------------------------------

  void _loadCaches() {
    for (final row in _db.select('SELECT id, name FROM identifier')) {
      final id = row['id'] as int;
      final name = row['name'] as String;
      _identifierIdToName[id] = name;
      _identifierNameToId[name] = id;
    }

    for (final row in _db.select('SELECT id, name FROM entity_type')) {
      _entityTypeIdToName[row['id'] as int] = row['name'] as String;
    }

    for (final row in _db.select('SELECT id, name FROM member_type')) {
      _memberTypeIdToName[row['id'] as int] = row['name'] as String;
    }

    for (final row in _db.select(
      'SELECT id, name, content_markdown FROM library',
    )) {
      final record = LibraryRecord(
        id: row['id'] as int,
        name: row['name'] as String,
        contentMarkdown: row['content_markdown'] as String,
      );
      _libraryById[record.id] = record;
      _libraryByName[record.name] = record;
    }
  }

  void _prepareStatements() {
    _entityCountStmt = _db.prepare(
      'SELECT COUNT(*) AS cnt FROM entity WHERE identifier_id = ?',
    );
    _entityResultsStmt = _db.prepare(
      'SELECT library_id, entity_type_id '
      'FROM entity WHERE identifier_id = ? LIMIT 10',
    );

    _memberCountNoHintStmt = _db.prepare(
      'SELECT COUNT(*) AS cnt FROM member WHERE identifier_id = ?',
    );
    _memberCountWithHintStmt = _db.prepare(
      'SELECT COUNT(*) AS cnt '
      'FROM member m '
      'JOIN entity e ON m.entity_id = e.id '
      'WHERE m.identifier_id = ? AND e.library_id = ?',
    );
    _memberResultsNoHintStmt = _db.prepare(
      'SELECT m.member_type_id, e.library_id, e.identifier_id '
      'FROM member m '
      'JOIN entity e ON m.entity_id = e.id '
      'WHERE m.identifier_id = ? '
      'LIMIT 10',
    );
    _memberResultsWithHintStmt = _db.prepare(
      'SELECT m.member_type_id, e.identifier_id '
      'FROM member m '
      'JOIN entity e ON m.entity_id = e.id '
      'WHERE m.identifier_id = ? AND e.library_id = ? '
      'LIMIT 10',
    );

    _entityDocStmt = _db.prepare(
      'SELECT content_markdown '
      'FROM entity WHERE identifier_id = ? AND library_id = ?',
    );
    _memberDocStmt = _db.prepare(
      'SELECT m.content_markdown '
      'FROM member m '
      'JOIN entity e ON m.entity_id = e.id '
      'WHERE e.library_id = ? AND e.identifier_id = ? AND m.identifier_id = ?',
    );
  }

  // ---------------------------------------------------------------------------
  // Public query methods
  // ---------------------------------------------------------------------------

  /// Looks up entities by [name]. Returns a tuple of the total match count and
  /// up to 10 results as `(library, entity, category)` triples.
  (int total, List<(String library, String entity, String category)> results)
  lookupEntity(String name) {
    final identifierId = _identifierNameToId[name];
    if (identifierId == null) return (0, const []);

    final countRow = _entityCountStmt.select([identifierId]);
    final total = countRow.first['cnt'] as int;
    if (total == 0) return (0, const []);

    final rows = _entityResultsStmt.select([identifierId]);
    final results = <(String, String, String)>[];
    for (final row in rows) {
      final libraryName =
          _libraryById[row['library_id'] as int]?.name ?? '';
      final category =
          _entityTypeIdToName[row['entity_type_id'] as int] ?? '';
      results.add((libraryName, name, category));
    }
    return (total, results);
  }

  /// Looks up members by [name], with an optional [libraryHint] to narrow
  /// results to a specific library. Returns a tuple of the total match count
  /// and up to 10 results as `(library, entity, member, category)` 4-tuples.
  (
    int total,
    List<(String library, String entity, String member, String category)>
        results,
  )
  lookupMember(String name, {String? libraryHint}) {
    final memberIdentifierId = _identifierNameToId[name];
    if (memberIdentifierId == null) return (0, const []);

    if (libraryHint != null) {
      final libraryRecord = _libraryByName[libraryHint];
      if (libraryRecord == null) return (0, const []);
      final libraryId = libraryRecord.id;

      final countRow = _memberCountWithHintStmt.select([
        memberIdentifierId,
        libraryId,
      ]);
      final total = countRow.first['cnt'] as int;
      if (total == 0) return (0, const []);

      final rows = _memberResultsWithHintStmt.select([
        memberIdentifierId,
        libraryId,
      ]);
      final results = <(String, String, String, String)>[];
      for (final row in rows) {
        final entityName =
            _identifierIdToName[row['identifier_id'] as int] ?? '';
        final category =
            _memberTypeIdToName[row['member_type_id'] as int] ?? '';
        results.add((libraryHint, entityName, name, category));
      }
      return (total, results);
    } else {
      final countRow = _memberCountNoHintStmt.select([memberIdentifierId]);
      final total = countRow.first['cnt'] as int;
      if (total == 0) return (0, const []);

      final rows = _memberResultsNoHintStmt.select([memberIdentifierId]);
      final results = <(String, String, String, String)>[];
      for (final row in rows) {
        final libraryName =
            _libraryById[row['library_id'] as int]?.name ?? '';
        final entityName =
            _identifierIdToName[row['identifier_id'] as int] ?? '';
        final category =
            _memberTypeIdToName[row['member_type_id'] as int] ?? '';
        results.add((libraryName, entityName, name, category));
      }
      return (total, results);
    }
  }

  /// Returns the content markdown for the given [library], served entirely
  /// from the in-memory cache. Returns `null` if the library is not found.
  String? libraryIndex(String library) =>
      _libraryByName[library]?.contentMarkdown;

  /// Returns the content markdown for the given [entity] in [library].
  /// Returns `null` if not found.
  String? entityDocumentation(String library, String entity) {
    final libraryId = _libraryByName[library]?.id;
    final identifierId = _identifierNameToId[entity];
    if (libraryId == null || identifierId == null) return null;

    final rows = _entityDocStmt.select([identifierId, libraryId]);
    if (rows.isEmpty) return null;
    return rows.first['content_markdown'] as String;
  }

  /// Returns the content markdown for [member] of [entity] in [library].
  /// Returns `null` if not found.
  String? memberDocumentation(String library, String entity, String member) {
    final libraryId = _libraryByName[library]?.id;
    final entityIdentifierId = _identifierNameToId[entity];
    final memberIdentifierId = _identifierNameToId[member];
    if (libraryId == null ||
        entityIdentifierId == null ||
        memberIdentifierId == null) {
      return null;
    }

    final rows = _memberDocStmt.select([
      libraryId,
      entityIdentifierId,
      memberIdentifierId,
    ]);
    if (rows.isEmpty) return null;
    return rows.first['content_markdown'] as String;
  }

  /// Disposes all prepared statements and closes the database.
  void close() {
    _entityCountStmt.close();
    _entityResultsStmt.close();
    _memberCountNoHintStmt.close();
    _memberCountWithHintStmt.close();
    _memberResultsNoHintStmt.close();
    _memberResultsWithHintStmt.close();
    _entityDocStmt.close();
    _memberDocStmt.close();
    _db.close();
  }
}
