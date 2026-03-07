# flutterdocs_mcp Search PRD

This PRD defines the approach for adding a search tool to the `flutterdocs_mcp.dart` MCP server.


## searchDocumentation Tool

- name: "searchDocumentation"
- title: "Search Flutter/Dart documentation"
- description: "Perform a full-text search across the Flutter/Dart documentation to find Flutter/Dart entities (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) whose documentation contains the given keywords. All words are matched with AND semantics — every word must appear somewhere in the entity's documentation, but not necessarily adjacent. Navigation Tip: Use the returned [library_slug, entity, documentation_excerpt] values to construct resource URIs: flutter-docs://api/{library_slug}/{entity}. Note: The returned library_slug value is a URI slug (not the library display name)."
- inputSchema:
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "The search keywords (e.g., 'scrolling', 'stateful widget'). All words are matched with AND semantics — every word must appear somewhere in the entity's documentation. Word order and punctuation are ignored."
    }
  },
  "required": ["query"]
}
- outputSchema:
{
  "type": "object",
  "description": "An object with a total query match count and up to 20 results.",
  "properties": {
    "total": { "type": "integer", "description": "The total number of query matches found."},
    "results": {
      "type": "array",
      "description": "List of up to 20 query match results",
      "items": {
        "type": "array",
        "description": "A [library_slug, entity, documentation_excerpt] array. Construct resource URIs as: flutter-docs://api/{library_slug}/{entity}",
        "prefixItems": [
          { "type": "string", "description": "Library slug (e.g., 'material')" },
          { "type": "string", "description": "Entity name (e.g., 'ListTile')" },
          { "type": "string", "description": "Documentation excerpt with query matches emphasized" }
        ]
      }
    }
  }
}


## searchDocumentation Database Query

```sql
SELECT 
    e.library_id, 
    e.identifier,
    snippet(content_search, 1, '***', '***', '...', 15) AS excerpt,
    bm25(content_search, 10.0, 1.0) AS rank,
    COUNT(*) OVER() AS total
FROM content_search
JOIN entity e ON content_search.rowid = e.id
WHERE content_search MATCH ?
ORDER BY rank
LIMIT 20;
```

Notes on the query:
- Use positional `?` (not `:query`) to match the existing prepared-statement style in `db.dart`.
- `bm25(content_search, 10.0, 1.0)` weights the `identifier` column (index 0, weight 10.0) higher than `content_markdown` (index 1, weight 1.0), so exact identifier matches rank first.
- `snippet(content_search, 1, '***', '***', '...', 15)` extracts a context fragment from `content_markdown` (column index 1), wrapping each matched token with `***`, and joining non-contiguous fragments with `...`.
- `COUNT(*) OVER()` is a window function that embeds the total match count in every result row. When the query returns zero rows, the total is derived as 0 in Dart (no rows to read from).
- The raw user query is sanitized before being passed to `MATCH` (see `_sanitizeFtsQuery` below), so `SqliteException` for malformed input cannot occur in normal operation.

Results from this SQL query map to the searchDocumentation tool output schema as follows:
- SQL query "total" maps to output schema "total"
- SQL query tuples [e.library_id, e.identifier, excerpt] map to output schema [library_slug, entity, documentation_excerpt]
  - **Important**: Use `_libraryById` to map `e.library_id` to the text library_slug


## Implementation Plan

### 1. `lib/src/db.dart` — `DocDatabase` changes

#### Query sanitizer `_sanitizeFtsQuery`

Add a private top-level function (outside `DocDatabase`, alongside the file's other helpers) that converts raw user input into a safe FTS5 AND query:

```dart
/// Sanitizes [input] for safe use as an FTS5 MATCH expression.
///
/// Extracts Unicode word tokens and wraps each in double quotes, producing a
/// space-joined AND query. This neutralizes all FTS5 operators and special
/// characters (AND, OR, NOT, NEAR, -, *, etc.).
///
/// Returns `null` if [input] contains no word tokens (blank or symbol-only
/// input); callers should return `(0, [])` without issuing a database query.
String? _sanitizeFtsQuery(String input) {
  final words = RegExp(r'\w+', unicode: true)
      .allMatches(input)
      .map((m) => m.group(0)!)
      .toList();
  if (words.isEmpty) return null;
  return words.map((w) => '"$w"').join(' ');
}
```

Examples:
- `'stateful widget'` → `'"stateful" "widget"'`
- `'GetIt-service'` → `'"GetIt" "service"'`
- `'dart:io'` → `'"dart" "io"'`
- `'   '` → `null`

#### New prepared statement field

Add a `late final PreparedStatement _searchDocumentationStmt;` field in the prepared-statement section alongside the existing fields.

#### `_prepareStatements()` update

Compile the search query into `_searchDocumentationStmt`:

```dart
_searchDocumentationStmt = _db.prepare(
  'SELECT '
  '    e.library_id, '
  '    e.identifier, '
  '    snippet(content_search, 1, \'***\', \'***\', \'...\', 15) AS excerpt, '
  '    bm25(content_search, 10.0, 1.0) AS rank, '
  '    COUNT(*) OVER() AS total '
  'FROM content_search '
  'JOIN entity e ON content_search.rowid = e.id '
  'WHERE content_search MATCH ? '
  'ORDER BY rank '
  'LIMIT 20',
);
```

#### New public method `searchDocumentation`

Add at the end of the public-query-methods section (before `close()`):

```dart
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
```

#### `close()` update

Add `_searchDocumentationStmt.close();` alongside the existing `close()` calls.

---

### 2. `lib/src/tools.dart` — tool registration, definition, and handler

#### `registerTools()` update

Register the new tool alongside the existing three:

```dart
server.registerTool(
  _searchDocumentationTool,
  (request) => _searchDocumentation(request, db),
);
```

#### Tool definition `_searchDocumentationTool`

Add after the `_listLibrariesTool` definition, reusing `_toolAnnotations`:

```dart
final _searchDocumentationTool = Tool(
  name: 'searchDocumentation',
  title: 'Search Flutter/Dart documentation',
  description:
      'Perform a full-text search across the Flutter/Dart documentation '
      'to find Flutter/Dart entities (class, mixin, enum, extension, '
      'extension type, typedef, top-level function, top-level constant) '
      'whose documentation contains the given keywords. All words are '
      'matched with AND semantics — every word must appear somewhere in '
      'the entity\'s documentation, but not necessarily adjacent. '
      'Navigation Tip: Use the returned [library_slug, entity, '
      'documentation_excerpt] values to construct resource URIs: '
      'flutter-docs://api/{library_slug}/{entity}. '
      'Note: The returned library_slug value is a URI slug (not the library '
      'display name).',
  inputSchema: Schema.object(
    properties: {
      'query': Schema.string(
        description:
            'The search keywords (e.g., "scrolling", "stateful widget"). '
            'All words are matched with AND semantics — every word must '
            'appear somewhere in the entity\'s documentation. Word order '
            'and punctuation are ignored.',
      ),
    },
    required: ['query'],
  ),
  outputSchema: Schema.object(
    description:
        'An object with a total query match count and up to 20 results.',
    properties: {
      'total': Schema.int(
        description: 'The total number of query matches found.',
      ),
      'results': Schema.list(
        description: 'List of up to 20 query match results.',
        items: Schema.list(
          description:
              'A [library_slug, entity, documentation_excerpt] array. '
              'Construct resource URIs as: '
              'flutter-docs://api/{library_slug}/{entity}',
          prefixItems: [
            Schema.string(description: "Library slug (e.g., 'material')."),
            Schema.string(description: "Entity name (e.g., 'ListTile')."),
            Schema.string(
              description: 'Documentation excerpt with query matches emphasized.',
            ),
          ],
        ),
      ),
    },
    required: ['total', 'results'],
  ),
  annotations: _toolAnnotations,
);
```

#### Tool handler `_searchDocumentation`

Add after the `_listLibraries` handler:

```dart
FutureOr<CallToolResult> _searchDocumentation(
  CallToolRequest request,
  DocDatabase db,
) {
  final query = request.arguments!['query'] as String;
  final (total, results) = db.searchDocumentation(query);
  final structured = {
    'total': total,
    'results': results.map((r) => [r.$1, r.$2, r.$3]).toList(),
  };
  return CallToolResult(
    content: [TextContent(text: jsonEncode(structured))],
    structuredContent: structured,
  );
}
```

No `SqliteException` handling is needed: `searchDocumentation` sanitizes the query before passing it to FTS5, making a malformed-query exception impossible.

---

### 3. `lib/src/server.dart` — update server instructions

Update the `instructions` string to mention `searchDocumentation`:

```dart
instructions:
    'This server provides tools and resources for navigating '
    'Flutter/Dart API documentation. Use searchDocumentation to find '
    'entities by keyword or phrase. Use lookupEntity to find which '
    'library an entity belongs to, and lookupMember to find which '
    'entity a member belongs to. Then use the resource URIs to '
    'retrieve the full documentation.',
```

---

## Tests

### `test/db_test.dart` — unit tests for `DocDatabase.searchDocumentation`

#### Fixture update

The `content_search` FTS5 virtual table and its `entity_ai` trigger must be added to `_populateFixture()` **before** the entity inserts. Add the following SQL to the existing `raw.execute(...)` call that creates the schema (or as a separate call immediately after the table/index creation block):

```sql
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
```

With this trigger in place, the existing entity INSERT statements in the fixture automatically populate the FTS5 index. No additional data is needed.

#### Test cases

Add a `searchDocumentation` group:

```dart
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
```

---

### `test/server_test.dart` — integration tests for `searchDocumentation` tool

The existing test setup already loads the `material` and `widgets` suites, which contain real Flutter documentation text.

Add a `searchDocumentation tool` group:

```dart
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
```

