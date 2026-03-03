"""Unit tests for db.py — database initialization and upsert helpers."""

import sqlite3

import pytest

from flutterdocs._shared.constants import ALL_CATEGORIES, ALL_MEMBERS
from flutterdocs.load.db import (
    get_entity_type_id,
    get_member_type_id,
    get_or_insert_identifier,
    init_db,
    upsert_entity,
    upsert_library,
    upsert_member,
)


@pytest.fixture
def mem_conn() -> sqlite3.Connection:
    """Create an in-memory sqlite3 connection with schema initialized."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    init_db(conn)
    return conn


class TestInitDb:
    """Tests for init_db: schema creation and pre-population."""

    def test_creates_all_tables(self, mem_conn: sqlite3.Connection) -> None:
        """All expected tables must exist after init_db."""
        expected = {
            "identifier",
            "entity_type",
            "member_type",
            "library",
            "entity",
            "member",
            "content_search",
        }
        rows = mem_conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        actual = {row["name"] for row in rows}
        assert expected.issubset(actual)

    def test_creates_triggers(self, mem_conn: sqlite3.Connection) -> None:
        """The three entity FTS5 triggers must be created."""
        expected = {"entity_ai", "entity_ad", "entity_au"}
        rows = mem_conn.execute(
            "SELECT name FROM sqlite_master WHERE type='trigger'"
        ).fetchall()
        actual = {row["name"] for row in rows}
        assert expected == actual

    def test_prepopulates_entity_types(self, mem_conn: sqlite3.Connection) -> None:
        """entity_type table must contain exactly the values from ALL_CATEGORIES."""
        rows = mem_conn.execute("SELECT name FROM entity_type").fetchall()
        names = {row["name"] for row in rows}
        assert names == {str(c) for c in ALL_CATEGORIES}

    def test_prepopulates_member_types(self, mem_conn: sqlite3.Connection) -> None:
        """member_type table must contain exactly the values from ALL_MEMBERS."""
        rows = mem_conn.execute("SELECT name FROM member_type").fetchall()
        names = {row["name"] for row in rows}
        assert names == {str(m) for m in ALL_MEMBERS}

    def test_creates_indexes(self, mem_conn: sqlite3.Connection) -> None:
        """Expected indexes must be created."""
        expected = {
            "idx_entity_unique",
            "idx_member_unique",
        }
        rows = mem_conn.execute(
            "SELECT name FROM sqlite_master WHERE type='index'"
        ).fetchall()
        actual = {row["name"] for row in rows}
        assert expected.issubset(actual)


class TestUpsertLibrary:
    """Tests for upsert_library."""

    def test_insert_returns_id(self, mem_conn: sqlite3.Connection) -> None:
        """upsert_library must return a positive integer id."""
        with mem_conn:
            lib_id = upsert_library(mem_conn, "material", "# material")
        assert isinstance(lib_id, int)
        assert lib_id > 0

    def test_update_preserves_id(self, mem_conn: sqlite3.Connection) -> None:
        """Re-upserting the same library must return the same id."""
        with mem_conn:
            id1 = upsert_library(mem_conn, "material", "# material v1")
        with mem_conn:
            id2 = upsert_library(mem_conn, "material", "# material v2")
        assert id1 == id2

    def test_update_changes_content(self, mem_conn: sqlite3.Connection) -> None:
        """Re-upserting must update content_markdown."""
        with mem_conn:
            upsert_library(mem_conn, "material", "# old")
        with mem_conn:
            upsert_library(mem_conn, "material", "# new")
        row = mem_conn.execute(
            "SELECT content_markdown FROM library WHERE name = 'material'"
        ).fetchone()
        assert row["content_markdown"] == "# new"


class TestUpsertEntity:
    """Tests for upsert_entity."""

    def _setup(self, conn: sqlite3.Connection) -> tuple[int, int]:
        """Insert prerequisite rows and return (library_id, entity_type_id)."""
        with conn:
            lib_id = upsert_library(conn, "material", "# material")
            type_id = get_entity_type_id(conn, "class")
        return lib_id, type_id

    def test_insert_returns_id(self, mem_conn: sqlite3.Connection) -> None:
        """upsert_entity must return a positive integer id."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            eid = upsert_entity(mem_conn, lib_id, "ListTile", type_id, "# content")
        assert isinstance(eid, int)
        assert eid > 0

    def test_update_preserves_id(self, mem_conn: sqlite3.Connection) -> None:
        """Re-upserting the same entity must return the same id."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            eid1 = upsert_entity(mem_conn, lib_id, "ListTile", type_id, "v1")
        with mem_conn:
            eid2 = upsert_entity(mem_conn, lib_id, "ListTile", type_id, "v2")
        assert eid1 == eid2

    def test_update_changes_content(self, mem_conn: sqlite3.Connection) -> None:
        """Re-upserting must update content_markdown."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "ListTile", type_id, "old")
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "ListTile", type_id, "new")
        row = mem_conn.execute("SELECT content_markdown FROM entity").fetchone()
        assert row["content_markdown"] == "new"

    def test_entity_has_no_snippet_markdown_column(
        self, mem_conn: sqlite3.Connection
    ) -> None:
        """The entity table must not have a snippet_markdown column."""
        rows = mem_conn.execute("PRAGMA table_info(entity)").fetchall()
        column_names = {row["name"] for row in rows}
        assert "snippet_markdown" not in column_names


class TestUpsertMember:
    """Tests for upsert_member."""

    def _setup(self, conn: sqlite3.Connection) -> tuple[int, int, int]:
        """Setup entity and return (entity_id, identifier_id, member_type_id)."""
        with conn:
            lib_id = upsert_library(conn, "material", "# material")
            etype_id = get_entity_type_id(conn, "class")
            entity_id = upsert_entity(conn, lib_id, "ListTile", etype_id, "content")

            conn.execute("INSERT OR IGNORE INTO identifier(name) VALUES ('build')")
            mem_ident_id = conn.execute(
                "SELECT id FROM identifier WHERE name = 'build'"
            ).fetchone()["id"]
            mtype_id = get_member_type_id(conn, "method")
        return entity_id, mem_ident_id, mtype_id

    def test_insert_member(self, mem_conn: sqlite3.Connection) -> None:
        """upsert_member must insert a member row."""
        entity_id, ident_id, mtype_id = self._setup(mem_conn)
        with mem_conn:
            upsert_member(mem_conn, entity_id, ident_id, mtype_id, "# build")
        row = mem_conn.execute("SELECT content_markdown FROM member").fetchone()
        assert row["content_markdown"] == "# build"

    def test_update_preserves_stable_row(self, mem_conn: sqlite3.Connection) -> None:
        """Re-upserting a member must preserve row count (no duplicate)."""
        entity_id, ident_id, mtype_id = self._setup(mem_conn)
        with mem_conn:
            upsert_member(mem_conn, entity_id, ident_id, mtype_id, "v1")
        with mem_conn:
            upsert_member(mem_conn, entity_id, ident_id, mtype_id, "v2")
        count = mem_conn.execute("SELECT COUNT(*) FROM member").fetchone()[0]
        assert count == 1

    def test_update_changes_content(self, mem_conn: sqlite3.Connection) -> None:
        """Re-upserting a member must update content_markdown."""
        entity_id, ident_id, mtype_id = self._setup(mem_conn)
        with mem_conn:
            upsert_member(mem_conn, entity_id, ident_id, mtype_id, "old")
        with mem_conn:
            upsert_member(mem_conn, entity_id, ident_id, mtype_id, "new")
        row = mem_conn.execute("SELECT content_markdown FROM member").fetchone()
        assert row["content_markdown"] == "new"


class TestGetOrInsertIdentifier:
    """Tests for get_or_insert_identifier."""

    def test_returns_id(self, mem_conn: sqlite3.Connection) -> None:
        """Must return a positive integer id."""
        with mem_conn:
            ident_id = get_or_insert_identifier(mem_conn, "Widget")
        assert isinstance(ident_id, int)
        assert ident_id > 0

    def test_deduplication(self, mem_conn: sqlite3.Connection) -> None:
        """Same name inserted twice must return the same id."""
        with mem_conn:
            id1 = get_or_insert_identifier(mem_conn, "Widget")
        with mem_conn:
            id2 = get_or_insert_identifier(mem_conn, "Widget")
        assert id1 == id2

    def test_different_names_different_ids(self, mem_conn: sqlite3.Connection) -> None:
        """Different names must produce different ids."""
        with mem_conn:
            id1 = get_or_insert_identifier(mem_conn, "Widget")
            id2 = get_or_insert_identifier(mem_conn, "State")
        assert id1 != id2


class TestContentSearchTriggers:
    """Tests that AFTER INSERT/UPDATE/DELETE triggers keep content_search in sync."""

    def _setup(self, conn: sqlite3.Connection) -> tuple[int, int]:
        """Insert prerequisite rows and return (library_id, entity_type_id)."""
        with conn:
            lib_id = upsert_library(conn, "material", "# material")
            type_id = get_entity_type_id(conn, "class")
        return lib_id, type_id

    def test_insert_populates_content_search(
        self, mem_conn: sqlite3.Connection
    ) -> None:
        """Inserting an entity must automatically add a row to content_search."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "InkWell", type_id, "# InkWell content")
        rows = mem_conn.execute(
            "SELECT rowid FROM content_search WHERE identifier MATCH 'InkWell'"
        ).fetchall()
        assert len(rows) > 0

    def test_update_reflects_new_content(self, mem_conn: sqlite3.Connection) -> None:
        """Updating an entity must update content_search to reflect new content."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "InkWell", type_id, "# original content")
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "InkWell", type_id, "# updated content")
        rows = mem_conn.execute(
            "SELECT rowid FROM content_search WHERE content_search MATCH 'updated'"
        ).fetchall()
        assert len(rows) > 0

    def test_update_removes_old_content(self, mem_conn: sqlite3.Connection) -> None:
        """After an update, the old FTS tokens must no longer match."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            upsert_entity(
                mem_conn, lib_id, "InkWell", type_id, "# uniqueOldToken content"
            )
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "InkWell", type_id, "# updated content")
        rows = mem_conn.execute(
            "SELECT rowid FROM content_search WHERE content_search MATCH 'uniqueOldToken'"
        ).fetchall()
        assert len(rows) == 0

    def test_update_does_not_duplicate_rows(self, mem_conn: sqlite3.Connection) -> None:
        """Re-upserting an entity must leave exactly one FTS row."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "InkWell", type_id, "# v1")
        with mem_conn:
            upsert_entity(mem_conn, lib_id, "InkWell", type_id, "# v2")
        rows = mem_conn.execute(
            "SELECT rowid FROM content_search WHERE identifier MATCH 'InkWell'"
        ).fetchall()
        assert len(rows) == 1

    def test_delete_removes_from_content_search(
        self, mem_conn: sqlite3.Connection
    ) -> None:
        """Deleting an entity row must remove its entry from content_search."""
        lib_id, type_id = self._setup(mem_conn)
        with mem_conn:
            upsert_entity(
                mem_conn, lib_id, "EphemeralWidget", type_id, "# EphemeralWidget"
            )
        with mem_conn:
            mem_conn.execute(
                "DELETE FROM entity WHERE identifier = ? AND library_id = ?",
                ("EphemeralWidget", lib_id),
            )
        rows = mem_conn.execute(
            "SELECT rowid FROM content_search WHERE identifier MATCH 'EphemeralWidget'"
        ).fetchall()
        assert len(rows) == 0
