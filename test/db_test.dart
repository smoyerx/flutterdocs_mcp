import 'dart:io';

import 'package:flutterdocs_mcp/src/db.dart';
import 'package:flutterdocs_mcp/src/version.dart';
import 'package:sqlite3/sqlite3.dart';
import 'package:test/test.dart';

late File _fixtureFile;
late DocDatabase _db;

/// Creates the schema and inserts deterministic fixture rows directly via the
/// sqlite3 package. Kept small: 2 libraries, a handful of entities/members.
void _populateFixture(Database raw) {
  raw.execute('''
    CREATE TABLE identifier (
      id INTEGER PRIMARY KEY,
      name TEXT UNIQUE NOT NULL
    );
    CREATE TABLE entity_type (
      id INTEGER PRIMARY KEY,
      name TEXT UNIQUE NOT NULL
    );
    CREATE TABLE member_type (
      id INTEGER PRIMARY KEY,
      name TEXT UNIQUE NOT NULL
    );
    CREATE TABLE library (
      id INTEGER PRIMARY KEY,
      name TEXT UNIQUE NOT NULL,
      display_name TEXT NOT NULL DEFAULT '',
      content_markdown TEXT NOT NULL
    );
    CREATE TABLE entity (
      id INTEGER PRIMARY KEY,
      library_id INTEGER NOT NULL,
      identifier TEXT NOT NULL,
      entity_type_id INTEGER NOT NULL,
      content_markdown TEXT NOT NULL,
      UNIQUE(identifier, library_id),
      FOREIGN KEY (library_id) REFERENCES library(id),
      FOREIGN KEY (entity_type_id) REFERENCES entity_type(id)
    );
    CREATE TABLE member (
      id INTEGER PRIMARY KEY,
      entity_id INTEGER NOT NULL,
      identifier_id INTEGER NOT NULL,
      member_type_id INTEGER NOT NULL,
      content_markdown TEXT NOT NULL,
      UNIQUE(identifier_id, entity_id),
      FOREIGN KEY (entity_id) REFERENCES entity(id),
      FOREIGN KEY (identifier_id) REFERENCES identifier(id),
      FOREIGN KEY (member_type_id) REFERENCES member_type(id)
    );
    CREATE INDEX idx_entity_unique ON entity(identifier, library_id);
    CREATE INDEX idx_member_unique ON member(identifier_id, entity_id);

    CREATE VIRTUAL TABLE content_search USING fts5(
        identifier,
        content_markdown,
        content='entity',
        content_rowid='id',
        tokenize='unicode61 remove_diacritics 2'
    );

    CREATE TRIGGER entity_ai AFTER INSERT ON entity BEGIN
        INSERT INTO content_search(rowid, identifier, content_markdown)
        VALUES (new.id, new.identifier, new.content_markdown);
    END;
  ''');
  raw.execute('PRAGMA user_version = $kDbVersion;');

  // Lookup tables
  raw.execute("INSERT INTO entity_type VALUES (1, 'class'), (2, 'enum')");
  raw.execute("INSERT INTO member_type VALUES (1, 'property'), (2, 'method')");

  // Identifiers (member names only — entity names live directly in entity.identifier)
  raw.execute('''
    INSERT INTO identifier VALUES
      (1, 'visualDensity'),
      (2, 'padding'),
      (3, 'onTap'),
      (4, 'listen')
  ''');

  // Libraries
  raw.execute('''
    INSERT INTO library VALUES
      (1, 'material',   'material',   '# material library'),
      (2, 'widgets',    'widgets',    '# widgets library'),
      (3, 'dart-async', 'dart:async', '# dart-async library')
  ''');

  // Entities
  //   ListTile      → material (class)
  //   Container     → widgets  (class)
  //   SharedEntity  → both material and widgets (class) — for multi-library test
  //   Stream        → dart-async (class)
  raw.execute('''
    INSERT INTO entity (id, library_id, identifier, entity_type_id, content_markdown) VALUES
      (1, 1, 'ListTile', 1, '# ListTile docs'),
      (2, 2, 'Container', 1, '# Container docs'),
      (3, 1, 'SharedEntity', 1, '# SharedEntity material docs'),
      (4, 2, 'SharedEntity', 2, '# SharedEntity widgets docs'),
      (5, 3, 'Stream', 1, '# Stream docs')
  ''');

  // Members
  //   visualDensity → ListTile/material (property)
  //   padding       → ListTile/material (property) AND Container/widgets (property)
  //   onTap         → ListTile/material (method)
  //   listen        → Stream/dart-async (method)
  raw.execute('''
    INSERT INTO member (id, entity_id, identifier_id, member_type_id, content_markdown) VALUES
      (1, 1, 1, 1, '# visualDensity docs'),
      (2, 1, 2, 1, '# padding/ListTile docs'),
      (3, 2, 2, 1, '# padding/Container docs'),
      (4, 1, 3, 2, '# onTap docs'),
      (5, 5, 4, 2, '# listen docs')
  ''');
}

void main() {
  setUpAll(() async {
    _fixtureFile = await File.fromUri(
      Directory.systemTemp.uri.resolve('flutterdocs_mcp_db_test.db'),
    ).create();
    final raw = sqlite3.open(_fixtureFile.path);
    _populateFixture(raw);
    raw.close();
  });

  setUp(() {
    _db = DocDatabase(_fixtureFile.path);
  });

  tearDown(() {
    _db.close();
  });

  tearDownAll(() async {
    await _fixtureFile.delete();
  });

  // -------------------------------------------------------------------------
  // lookupEntity
  // -------------------------------------------------------------------------

  group('lookupEntity', () {
    test('returns single match for unique entity name', () {
      final (total, results) = _db.lookupEntity('ListTile');
      expect(total, 1);
      expect(results, hasLength(1));
      final (library, entity, category) = results.first;
      expect(library, 'material');
      expect(entity, 'ListTile');
      expect(category, 'class');
    });

    test('returns multiple matches for entity in two libraries', () {
      final (total, results) = _db.lookupEntity('SharedEntity');
      expect(total, 2);
      expect(results, hasLength(2));
      final libraries = results.map((r) => r.$1).toSet();
      expect(libraries, containsAll(['material', 'widgets']));
    });

    test('returns (0, []) for unknown entity name', () {
      final (total, results) = _db.lookupEntity('NoSuchEntity');
      expect(total, 0);
      expect(results, isEmpty);
    });
  });

  // -------------------------------------------------------------------------
  // lookupMember
  // -------------------------------------------------------------------------

  group('lookupMember', () {
    test('returns single match for unique member name', () {
      final (total, results) = _db.lookupMember('visualDensity');
      expect(total, 1);
      expect(results, hasLength(1));
      final (library, entity, member, category) = results.first;
      expect(library, 'material');
      expect(entity, 'ListTile');
      expect(member, 'visualDensity');
      expect(category, 'property');
    });

    test('returns multiple matches for member in two entities', () {
      final (total, results) = _db.lookupMember('padding');
      expect(total, 2);
      expect(results, hasLength(2));
      final entities = results.map((r) => r.$2).toSet();
      expect(entities, containsAll(['ListTile', 'Container']));
    });

    test('filters by library hint', () {
      final (total, results) = _db.lookupMember(
        'padding',
        librarySlugHint: 'material',
      );
      expect(total, 1);
      expect(results, hasLength(1));
      expect(results.first.$2, 'ListTile');
    });

    test('returns (0, []) when library hint does not match', () {
      // 'visualDensity' belongs to material; hint for widgets should miss.
      final (total, results) = _db.lookupMember(
        'visualDensity',
        librarySlugHint: 'widgets',
      );
      expect(total, 0);
      expect(results, isEmpty);
    });

    test('returns (0, []) for unknown member name', () {
      final (total, results) = _db.lookupMember('noSuchMember');
      expect(total, 0);
      expect(results, isEmpty);
    });

    test('recognized hint scopes search — member absent in hinted library', () {
      // 'visualDensity' belongs to material; hint for widgets is recognized
      // but yields no match → (0, []).
      final (total, results) = _db.lookupMember(
        'visualDensity',
        librarySlugHint: 'widgets',
      );
      expect(total, 0);
      expect(results, isEmpty);
    });

    test('colon-form hint is normalized to slug', () {
      // 'dart:async' is not a slug, but after colon→hyphen it matches 'dart-async'.
      final (total, results) = _db.lookupMember(
        'listen',
        librarySlugHint: 'dart:async',
      );
      expect(total, 1);
      expect(results, hasLength(1));
      final (library, entity, member, _) = results.first;
      expect(library, 'dart-async'); // slug, not the colon-form
      expect(entity, 'Stream');
      expect(member, 'listen');
    });

    test('unrecognized hint is ignored — falls back to unscoped search', () {
      // 'unknownLib' is not a known slug even after normalization; the hint is
      // silently dropped and the full unscoped result set is returned.
      final (total, results) = _db.lookupMember(
        'visualDensity',
        librarySlugHint: 'unknownLib',
      );
      expect(total, 1);
      expect(results, hasLength(1));
      expect(results.first.$1, 'material');
    });
  });

  // -------------------------------------------------------------------------
  // listLibraries
  // -------------------------------------------------------------------------

  group('listLibraries', () {
    test('returns all library slug-displayName pairs', () {
      final libraries = _db.listLibraries();
      final slugs = libraries.map((e) => e.$1).toList();
      expect(slugs, containsAll(['material', 'widgets', 'dart-async']));
      expect(libraries, hasLength(3));
    });

    test('displayName reflects stored value', () {
      final libraries = _db.listLibraries();
      final dartAsync = libraries.firstWhere((e) => e.$1 == 'dart-async');
      expect(dartAsync.$2, 'dart:async');
    });

    test('result is sorted alphabetically by slug', () {
      final libraries = _db.listLibraries();
      final slugs = libraries.map((e) => e.$1).toList();
      expect(slugs, equals([...slugs]..sort()));
    });
  });

  // -------------------------------------------------------------------------
  // libraryIndex
  // -------------------------------------------------------------------------

  group('libraryIndex', () {
    test('returns content for known library', () {
      expect(_db.libraryIndex('material'), '# material library');
      expect(_db.libraryIndex('widgets'), '# widgets library');
    });

    test('returns null for unknown library', () {
      expect(_db.libraryIndex('unknownLib'), isNull);
    });
  });

  // -------------------------------------------------------------------------
  // entityDocumentation
  // -------------------------------------------------------------------------

  group('entityDocumentation', () {
    test('returns content for known entity', () {
      expect(
        _db.entityDocumentation('material', 'ListTile'),
        '# ListTile docs',
      );
      expect(
        _db.entityDocumentation('widgets', 'Container'),
        '# Container docs',
      );
    });

    test('returns correct content for each library when entity is shared', () {
      expect(
        _db.entityDocumentation('material', 'SharedEntity'),
        '# SharedEntity material docs',
      );
      expect(
        _db.entityDocumentation('widgets', 'SharedEntity'),
        '# SharedEntity widgets docs',
      );
    });

    test('returns null for unknown library', () {
      expect(_db.entityDocumentation('unknownLib', 'ListTile'), isNull);
    });

    test('returns null for unknown entity', () {
      expect(_db.entityDocumentation('material', 'NoSuch'), isNull);
    });

    test('returns null when entity exists but not in specified library', () {
      // Container is in widgets, not material.
      expect(_db.entityDocumentation('material', 'Container'), isNull);
    });
  });

  // -------------------------------------------------------------------------
  // memberDocumentation
  // -------------------------------------------------------------------------

  group('memberDocumentation', () {
    test('returns content for known member', () {
      expect(
        _db.memberDocumentation('material', 'ListTile', 'visualDensity'),
        '# visualDensity docs',
      );
      expect(
        _db.memberDocumentation('material', 'ListTile', 'onTap'),
        '# onTap docs',
      );
    });

    test('distinguishes same member name on different entities', () {
      expect(
        _db.memberDocumentation('material', 'ListTile', 'padding'),
        '# padding/ListTile docs',
      );
      expect(
        _db.memberDocumentation('widgets', 'Container', 'padding'),
        '# padding/Container docs',
      );
    });

    test('returns null for unknown library', () {
      expect(
        _db.memberDocumentation('unknownLib', 'ListTile', 'visualDensity'),
        isNull,
      );
    });

    test('returns null for unknown entity', () {
      expect(
        _db.memberDocumentation('material', 'NoSuch', 'visualDensity'),
        isNull,
      );
    });

    test('returns null for unknown member', () {
      expect(
        _db.memberDocumentation('material', 'ListTile', 'noSuchMember'),
        isNull,
      );
    });
  });

  // -------------------------------------------------------------------------
  // searchDocumentation
  // -------------------------------------------------------------------------

  group('searchDocumentation', () {
    test('returns matching results for a known term', () {
      // 'ListTile' appears as the identifier of entity 1.
      final (total, results) = _db.searchDocumentation('ListTile');
      expect(total, greaterThan(0));
      expect(results, isNotEmpty);
      final entities = results.map((r) => r.$2).toList();
      expect(entities, contains('ListTile'));
    });

    test('returns (0, []) for a term with no matches', () {
      final (total, results) = _db.searchDocumentation('xyzzy99nonexistent');
      expect(total, 0);
      expect(results, isEmpty);
    });

    test('result library slug is looked up from _libraryById', () {
      final (_, results) = _db.searchDocumentation('ListTile');
      expect(results.first.$1, 'material');
    });

    test('excerpt field is non-empty for a matching result', () {
      final (_, results) = _db.searchDocumentation('ListTile');
      expect(results.first.$3, isNotEmpty);
    });

    test('returns (0, []) for blank input', () {
      final (total, results) = _db.searchDocumentation('   ');
      expect(total, 0);
      expect(results, isEmpty);
    });

    test('returns (0, []) for symbol-only input', () {
      // Input with no \w+ tokens sanitizes to null → short-circuits before DB.
      final (total, results) = _db.searchDocumentation('--- *** :::');
      expect(total, 0);
      expect(results, isEmpty);
    });
  });

  // -------------------------------------------------------------------------
  // userVersion
  // -------------------------------------------------------------------------

  group('userVersion', () {
    test('returns kDbVersion from fixture database', () {
      expect(_db.userVersion, kDbVersion);
    });
  });
}
