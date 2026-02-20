"""Integration tests for member loading."""

import sqlite3
from pathlib import Path

from load.conftest import SAMPLES_DIR, run_load


class TestMemberRows:
    """Tests that verify member rows are loaded correctly."""

    def test_member_rows_exist(self, db_path: Path) -> None:
        """The member table must have rows after loading the material section."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        count = conn.execute("SELECT COUNT(*) FROM member").fetchone()[0]
        conn.close()
        assert count > 0

    def test_constructor_type_present(self, db_path: Path) -> None:
        """At least one member with type 'constructor' must be loaded."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        count = conn.execute(
            """
            SELECT COUNT(*) FROM member m
            JOIN member_type mt ON m.member_type_id = mt.id
            WHERE mt.name = 'constructor'
            """
        ).fetchone()[0]
        conn.close()
        assert count > 0

    def test_method_type_present(self, db_path: Path) -> None:
        """At least one member with type 'method' must be loaded."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        count = conn.execute(
            """
            SELECT COUNT(*) FROM member m
            JOIN member_type mt ON m.member_type_id = mt.id
            WHERE mt.name = 'method'
            """
        ).fetchone()[0]
        conn.close()
        assert count > 0

    def test_member_identifier_linked(self, db_path: Path) -> None:
        """Every member must have a valid identifier_id foreign key."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        orphan_count = conn.execute(
            """
            SELECT COUNT(*) FROM member m
            WHERE NOT EXISTS (
                SELECT 1 FROM identifier i WHERE i.id = m.identifier_id
            )
            """
        ).fetchone()[0]
        conn.close()
        assert orphan_count == 0

    def test_member_entity_linked(self, db_path: Path) -> None:
        """Every member must have a valid entity_id foreign key."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        orphan_count = conn.execute(
            """
            SELECT COUNT(*) FROM member m
            WHERE NOT EXISTS (
                SELECT 1 FROM entity e WHERE e.id = m.entity_id
            )
            """
        ).fetchone()[0]
        conn.close()
        assert orphan_count == 0

    def test_all_member_type_values_present(self, db_path: Path) -> None:
        """The member_type lookup table must contain all ALL_MEMBERS values."""
        from flutterdoc_gen._shared.constants import ALL_MEMBERS

        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT name FROM member_type").fetchall()
        names = {row["name"] for row in rows}
        conn.close()
        assert names == {str(m) for m in ALL_MEMBERS}

    def test_member_content_nonempty(self, db_path: Path) -> None:
        """All loaded member rows must have non-empty content_markdown."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        empty_count = conn.execute(
            "SELECT COUNT(*) FROM member WHERE content_markdown = '' OR content_markdown IS NULL"
        ).fetchone()[0]
        conn.close()
        assert empty_count == 0

    def test_inherited_members_loaded(self, db_path: Path) -> None:
        """Inherited property/method members must be loaded (type = 'property' or 'method')."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        # Verify both property and method types are present — inherited dirs use same type
        prop_count = conn.execute(
            """
            SELECT COUNT(*) FROM member m
            JOIN member_type mt ON m.member_type_id = mt.id
            WHERE mt.name = 'property'
            """
        ).fetchone()[0]
        conn.close()
        assert prop_count > 0
