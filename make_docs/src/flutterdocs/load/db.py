"""Database initialization and upsert helpers for load.py.

Manages connection creation, schema initialization, and all SQL operations
for the Flutter documentation database.
"""

import sqlite3
from pathlib import Path

from flutterdocs._shared.constants import ALL_CATEGORIES, ALL_MEMBERS

# Full DDL for database schema initialization
SCHEMA_DDL = """
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
    tokenize='porter'
);
"""


def init_db(conn: sqlite3.Connection) -> None:
    """Initialize database schema and pre-populate lookup tables.

    Executes DDL, then pre-populates entity_type and member_type tables
    using ALL_CATEGORIES and ALL_MEMBERS. All steps run in a single transaction.

    Args:
        conn: Open sqlite3 connection to a newly created database.
    """
    with conn:
        for statement in SCHEMA_DDL.strip().split(";"):
            stmt = statement.strip()
            if stmt:
                conn.execute(stmt)
        for category in ALL_CATEGORIES:
            conn.execute("INSERT INTO entity_type(name) VALUES (?)", (str(category),))
        for member in ALL_MEMBERS:
            conn.execute("INSERT INTO member_type(name) VALUES (?)", (str(member),))


def open_or_create_db(db_path: Path) -> sqlite3.Connection:
    """Open the database, initializing schema only if the file is new.

    Args:
        db_path: Path to the sqlite3 database file (may or may not exist).

    Returns:
        Open sqlite3.Connection with row_factory set to sqlite3.Row.

    Raises:
        sqlite3.Error: If opening or initializing the database fails.
    """
    needs_init = not db_path.exists()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    if needs_init:
        init_db(conn)
    return conn


def get_or_insert_identifier(conn: sqlite3.Connection, name: str) -> int:
    """Insert an identifier name if absent and return its id.

    Args:
        conn: Open sqlite3 connection (within an active transaction).
        name: The identifier name to insert or find.

    Returns:
        The integer id of the identifier row.
    """
    conn.execute("INSERT OR IGNORE INTO identifier(name) VALUES (?)", (name,))
    row = conn.execute("SELECT id FROM identifier WHERE name = ?", (name,)).fetchone()
    return int(row["id"])


def get_entity_type_id(conn: sqlite3.Connection, name: str) -> int:
    """Look up entity_type id by name.

    Args:
        conn: Open sqlite3 connection.
        name: CategoryType string value (e.g., "class").

    Returns:
        The integer id of the entity_type row.

    Raises:
        ValueError: If name is not found in entity_type table.
    """
    row = conn.execute("SELECT id FROM entity_type WHERE name = ?", (name,)).fetchone()
    if row is None:
        raise ValueError(f"Unknown entity_type: {name!r}")
    return int(row["id"])


def get_member_type_id(conn: sqlite3.Connection, name: str) -> int:
    """Look up member_type id by name.

    Args:
        conn: Open sqlite3 connection.
        name: MemberType string value (e.g., "method").

    Returns:
        The integer id of the member_type row.

    Raises:
        ValueError: If name is not found in member_type table.
    """
    row = conn.execute("SELECT id FROM member_type WHERE name = ?", (name,)).fetchone()
    if row is None:
        raise ValueError(f"Unknown member_type: {name!r}")
    return int(row["id"])


def upsert_library(
    conn: sqlite3.Connection,
    name: str,
    content_markdown: str,
) -> int:
    """Insert or update a library row and return its id.

    Uses ON CONFLICT DO UPDATE to preserve the existing id on update.

    Args:
        conn: Open sqlite3 connection (within an active transaction).
        name: Section name (e.g., "material").
        content_markdown: Markdown content of the library file.

    Returns:
        The integer id of the library row.
    """
    conn.execute(
        """
        INSERT INTO library(name, content_markdown)
        VALUES (?, ?)
        ON CONFLICT(name) DO UPDATE SET content_markdown = excluded.content_markdown
        """,
        (name, content_markdown),
    )
    row = conn.execute("SELECT id FROM library WHERE name = ?", (name,)).fetchone()
    return int(row["id"])


def upsert_entity(
    conn: sqlite3.Connection,
    library_id: int,
    identifier: str,
    entity_type_id: int,
    content_markdown: str,
) -> int:
    """Insert or update an entity row and return its id.

    Uses ON CONFLICT DO UPDATE to preserve the existing id on update.

    Args:
        conn: Open sqlite3 connection (within an active transaction).
        library_id: Foreign key to library.id.
        identifier: Entity name string (e.g., "InkWell").
        entity_type_id: Foreign key to entity_type.id.
        content_markdown: Markdown content of the entity root file, including
            any appended snippet content.

    Returns:
        The integer id of the entity row.
    """
    conn.execute(
        """
        INSERT INTO entity(library_id, identifier, entity_type_id, content_markdown)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(identifier, library_id) DO UPDATE SET
            content_markdown = excluded.content_markdown
        """,
        (library_id, identifier, entity_type_id, content_markdown),
    )
    row = conn.execute(
        "SELECT id FROM entity WHERE identifier = ? AND library_id = ?",
        (identifier, library_id),
    ).fetchone()
    return int(row["id"])


def upsert_member(
    conn: sqlite3.Connection,
    entity_id: int,
    identifier_id: int,
    member_type_id: int,
    content_markdown: str,
) -> None:
    """Insert or update a member row.

    Uses ON CONFLICT DO UPDATE to preserve the existing id on update.

    Args:
        conn: Open sqlite3 connection (within an active transaction).
        entity_id: Foreign key to entity.id.
        identifier_id: Foreign key to identifier.id for the member name.
        member_type_id: Foreign key to member_type.id.
        content_markdown: Markdown content of the member file.
    """
    conn.execute(
        """
        INSERT INTO member(entity_id, identifier_id, member_type_id, content_markdown)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(identifier_id, entity_id) DO UPDATE SET
            content_markdown = excluded.content_markdown
        """,
        (entity_id, identifier_id, member_type_id, content_markdown),
    )


def upsert_entity_search(
    conn: sqlite3.Connection,
    entity_id: int,
    identifier: str,
    content_markdown: str,
    old_identifier: str | None = None,
    old_content_markdown: str | None = None,
) -> None:
    """Insert or update a single entity row in the content_search FTS5 table.

    For external-content FTS5 tables, updates require explicitly deleting the
    old entry before inserting the new one. If old_identifier and
    old_content_markdown are provided, a delete command is issued first using
    the old values so that stale tokens are removed from the index.

    Args:
        conn: Open sqlite3 connection (within an active transaction).
        entity_id: The rowid (entity.id) of the entity to index.
        identifier: New entity identifier string.
        content_markdown: New entity markdown content.
        old_identifier: Pre-upsert identifier; provide when the entity already
            existed so the old FTS tokens are removed.
        old_content_markdown: Pre-upsert content_markdown; provide when the
            entity already existed so the old FTS tokens are removed.
    """
    if old_identifier is not None and old_content_markdown is not None:
        conn.execute(
            "INSERT INTO content_search(content_search, rowid, identifier, content_markdown)"
            " VALUES('delete', ?, ?, ?)",
            (entity_id, old_identifier, old_content_markdown),
        )
    conn.execute(
        "INSERT INTO content_search(rowid, identifier, content_markdown) VALUES (?, ?, ?)",
        (entity_id, identifier, content_markdown),
    )


def rebuild_search_index(conn: sqlite3.Connection) -> None:
    """Rebuild the FTS5 content_search index from the entity table.

    Should be called after all sections are loaded when the --reindex flag is
    used. Safe to call on an already-indexed database; it replaces the existing
    index content.

    Args:
        conn: Open sqlite3 connection.
    """
    with conn:
        conn.execute("INSERT INTO content_search(content_search) VALUES('rebuild')")
