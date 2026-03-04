import 'package:sqlite3/sqlite3.dart';

/// Sanitizes [input] for safe use as an FTS5 MATCH expression.
///
/// Extracts Unicode word tokens and wraps each in double quotes, producing a
/// space-joined AND query. This neutralizes all FTS5 operators and special
/// characters (AND, OR, NOT, NEAR, -, *, etc.) while preserving porter
/// stemming (quoting tokens does not suppress it).
///
/// Returns `null` if [input] contains no word tokens (blank or symbol-only
/// input); callers should return `(0, [])` without issuing a database query.
String? _sanitizeFtsQuery(String input) {
  final words = RegExp(
    r'\w+',
    unicode: true,
  ).allMatches(input).map((m) => m.group(0)!).toList();
  if (words.isEmpty) return null;
  return words.map((w) => '"$w"').join(' ');
}

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
  late final PreparedStatement _searchDocumentationStmt;

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
      'SELECT COUNT(*) AS cnt FROM entity WHERE identifier = ?',
    );
    _entityResultsStmt = _db.prepare(
      'SELECT library_id, entity_type_id '
      'FROM entity WHERE identifier = ? LIMIT 10',
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
      'SELECT m.member_type_id, e.library_id, e.identifier '
      'FROM member m '
      'JOIN entity e ON m.entity_id = e.id '
      'WHERE m.identifier_id = ? '
      'LIMIT 10',
    );
    _memberResultsWithHintStmt = _db.prepare(
      'SELECT m.member_type_id, e.identifier '
      'FROM member m '
      'JOIN entity e ON m.entity_id = e.id '
      'WHERE m.identifier_id = ? AND e.library_id = ? '
      'LIMIT 10',
    );

    _entityDocStmt = _db.prepare(
      'SELECT content_markdown '
      'FROM entity WHERE identifier = ? AND library_id = ?',
    );
    _memberDocStmt = _db.prepare(
      'SELECT m.content_markdown '
      'FROM member m '
      'JOIN entity e ON m.entity_id = e.id '
      'WHERE e.library_id = ? AND e.identifier = ? AND m.identifier_id = ?',
    );

    _searchDocumentationStmt = _db.prepare(
      'SELECT '
      '    e.library_id, '
      '    e.identifier, '
      '    fts.excerpt, '
      '    COUNT(*) OVER() AS total '
      'FROM ('
      '    SELECT '
      '        rowid AS fts_rowid, '
      '        snippet(content_search, 1, \'***\', \'***\', \'...\', 15) AS excerpt, '
      '        bm25(content_search, 10.0, 1.0) AS rank '
      '    FROM content_search '
      '    WHERE content_search MATCH ? '
      ') AS fts '
      'JOIN entity e ON fts.fts_rowid = e.id '
      'ORDER BY fts.rank '
      'LIMIT 20',
    );
  }

  // ---------------------------------------------------------------------------
  // Public query methods
  // ---------------------------------------------------------------------------

  /// Looks up entities by [name]. Returns a tuple of the total match count and
  /// up to 10 results as `(library, entity, category)` triples.
  (int total, List<(String library, String entity, String category)> results)
  lookupEntity(String name) {
    final countRow = _entityCountStmt.select([name]);
    final total = countRow.first['cnt'] as int;
    if (total == 0) return (0, const []);

    final rows = _entityResultsStmt.select([name]);
    final results = <(String, String, String)>[];
    for (final row in rows) {
      final libraryName = _libraryById[row['library_id'] as int]?.name ?? '';
      final category = _entityTypeIdToName[row['entity_type_id'] as int] ?? '';
      results.add((libraryName, name, category));
    }
    return (total, results);
  }

  /// Resolves a [hint] to a [LibraryRecord] by trying it as-is first, then
  /// with colons replaced by hyphens (e.g., `dart:io` → `dart-io`). Returns
  /// `null` if neither form matches a known library slug.
  LibraryRecord? _resolveLibraryHint(String hint) =>
      _libraryByName[hint] ?? _libraryByName[hint.replaceAll(':', '-')];

  /// Looks up members by [name], with an optional [libraryHint] to narrow
  /// results to a specific library. Returns a tuple of the total match count
  /// and up to 10 results as `(library, entity, member, category)` 4-tuples.
  ///
  /// [libraryHint] is matched against known library slugs. If it is not
  /// recognized (even after colon→hyphen normalization), the hint is silently
  /// ignored and an unscoped search is performed.
  (
    int total,
    List<(String library, String entity, String member, String category)>
    results,
  )
  lookupMember(String name, {String? libraryHint}) {
    final memberIdentifierId = _identifierNameToId[name];
    if (memberIdentifierId == null) return (0, const []);

    final resolvedLibrary = libraryHint != null
        ? _resolveLibraryHint(libraryHint)
        : null;

    if (resolvedLibrary != null) {
      final libraryId = resolvedLibrary.id;

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
        final entityName = row['identifier'] as String;
        final category =
            _memberTypeIdToName[row['member_type_id'] as int] ?? '';
        // Use the resolved slug, not the raw hint, so results are always slugs.
        results.add((resolvedLibrary.name, entityName, name, category));
      }
      return (total, results);
    } else {
      // No hint, or hint was not recognized — perform unscoped search.
      final countRow = _memberCountNoHintStmt.select([memberIdentifierId]);
      final total = countRow.first['cnt'] as int;
      if (total == 0) return (0, const []);

      final rows = _memberResultsNoHintStmt.select([memberIdentifierId]);
      final results = <(String, String, String, String)>[];
      for (final row in rows) {
        final libraryName = _libraryById[row['library_id'] as int]?.name ?? '';
        final entityName = row['identifier'] as String;
        final category =
            _memberTypeIdToName[row['member_type_id'] as int] ?? '';
        results.add((libraryName, entityName, name, category));
      }
      return (total, results);
    }
  }

  /// Returns all library slugs sorted alphabetically. These are the URI-safe
  /// identifiers used in resource URIs and the `libraryHint` parameter.
  List<String> listLibraries() => _libraryByName.keys.toList()..sort();

  /// Returns the content markdown for the given [library], served entirely
  /// from the in-memory cache. Returns `null` if the library is not found.
  String? libraryIndex(String library) =>
      _libraryByName[library]?.contentMarkdown;

  /// Returns the content markdown for the given [entity] in [library].
  /// Returns `null` if not found.
  String? entityDocumentation(String library, String entity) {
    final libraryId = _libraryByName[library]?.id;
    if (libraryId == null) return null;

    final rows = _entityDocStmt.select([entity, libraryId]);
    if (rows.isEmpty) return null;
    return rows.first['content_markdown'] as String;
  }

  /// Returns the content markdown for [member] of [entity] in [library].
  /// Returns `null` if not found.
  String? memberDocumentation(String library, String entity, String member) {
    final libraryId = _libraryByName[library]?.id;
    final memberIdentifierId = _identifierNameToId[member];
    if (libraryId == null || memberIdentifierId == null) return null;

    final rows = _memberDocStmt.select([libraryId, entity, memberIdentifierId]);
    if (rows.isEmpty) return null;
    return rows.first['content_markdown'] as String;
  }

  /// Full-text searches entity documentation for [query]. Returns a tuple of
  /// the total match count and up to 20 results as
  /// `(library_slug, entity, excerpt)` triples.
  ///
  /// [query] is sanitized via [_sanitizeFtsQuery] before being passed to the
  /// FTS5 `MATCH` operator. Returns `(0, [])` if [query] contains no word
  /// tokens.
  (int total, List<(String library, String entity, String excerpt)> results)
  searchDocumentation(String query) {
    final sanitized = _sanitizeFtsQuery(query);
    if (sanitized == null) return (0, const []);
    final rows = _searchDocumentationStmt.select([sanitized]);
    if (rows.isEmpty) return (0, const []);
    final total = rows.first['total'] as int;
    final results = <(String, String, String)>[];
    for (final row in rows) {
      final library = _libraryById[row['library_id'] as int]?.name ?? '';
      final entity = row['identifier'] as String;
      final excerpt = row['excerpt'] as String;
      results.add((library, entity, excerpt));
    }
    return (total, results);
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
    _searchDocumentationStmt.close();
    _db.close();
  }
}
