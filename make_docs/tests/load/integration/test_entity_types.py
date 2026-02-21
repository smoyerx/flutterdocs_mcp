"""Integration tests for entity-type loading coverage."""

import sqlite3
from pathlib import Path

from load.conftest import SAMPLES_DIR, run_load


class TestEntityLoading:
    """Tests that verify entities are loaded correctly by type."""

    def test_classes_loaded(self, db_path: Path) -> None:
        """At least one class entity must be loaded from the material section."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        count = conn.execute(
            """
            SELECT COUNT(*) FROM entity e
            JOIN entity_type et ON e.entity_type_id = et.id
            WHERE et.name = 'class'
            """
        ).fetchone()[0]
        conn.close()
        assert count > 0

    def test_entity_has_content_markdown(self, db_path: Path) -> None:
        """The ListTile entity must have non-empty content_markdown."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            """
            SELECT e.content_markdown
            FROM entity e
            JOIN identifier i ON e.identifier_id = i.id
            WHERE i.name = 'ListTile'
            """
        ).fetchone()
        conn.close()
        assert row is not None
        assert len(row["content_markdown"]) > 0

    def test_entity_identifier_linked(self, db_path: Path) -> None:
        """Each entity row must reference a valid identifier."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        # Entities whose identifier_id has no matching identifier row
        orphan_count = conn.execute(
            """
            SELECT COUNT(*) FROM entity e
            WHERE NOT EXISTS (
                SELECT 1 FROM identifier i WHERE i.id = e.identifier_id
            )
            """
        ).fetchone()[0]
        conn.close()
        assert orphan_count == 0

    def test_entity_snippet_markdown(self, db_path: Path) -> None:
        """At least one entity with snippets must have non-null snippet_markdown."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        count = conn.execute(
            "SELECT COUNT(*) FROM entity WHERE snippet_markdown IS NOT NULL"
        ).fetchone()[0]
        conn.close()
        # The material samples include snippet files for some entities
        assert count > 0

    def test_all_entity_type_values_present(self, db_path: Path) -> None:
        """The entity_type lookup table must contain all ALL_CATEGORIES values."""
        from flutterdocs._shared.constants import ALL_CATEGORIES

        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT name FROM entity_type").fetchall()
        names = {row["name"] for row in rows}
        conn.close()
        assert names == {str(c) for c in ALL_CATEGORIES}
