"""Integration tests for basic end-to-end load behavior."""

import sqlite3
from pathlib import Path

from load.conftest import SAMPLES_DIR, run_load


class TestDbCreation:
    """Tests that verify the database file and tables are created correctly."""

    def test_creates_db_file(self, db_path: Path) -> None:
        """Running load must create the database file."""
        assert not db_path.exists()
        result = run_load(SAMPLES_DIR, "material", db_path)
        assert result.returncode == 0, f"load failed:\n{result.stderr}"
        assert db_path.exists()

    def test_creates_all_tables(self, db_path: Path) -> None:
        """The database must contain all six expected tables."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        tables = {row["name"] for row in rows}
        expected = {
            "identifier",
            "entity_type",
            "member_type",
            "library",
            "entity",
            "member",
        }
        assert expected == tables
        conn.close()

    def test_library_row_created(self, db_path: Path) -> None:
        """A library row for the loaded section must be present."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT name FROM library WHERE name = 'material'"
        ).fetchone()
        assert row is not None
        conn.close()


class TestIdempotency:
    """Tests that loading twice produces a stable result."""

    def test_load_twice_no_error(self, db_path: Path) -> None:
        """Loading the same section twice must succeed both times."""
        r1 = run_load(SAMPLES_DIR, "material", db_path)
        assert r1.returncode == 0, r1.stderr
        r2 = run_load(SAMPLES_DIR, "material", db_path)
        assert r2.returncode == 0, r2.stderr

    def test_load_twice_stable_row_counts(self, db_path: Path) -> None:
        """Row counts must be unchanged after a second load."""
        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        count1_entity = conn.execute("SELECT COUNT(*) FROM entity").fetchone()[0]
        count1_member = conn.execute("SELECT COUNT(*) FROM member").fetchone()[0]
        conn.close()

        run_load(SAMPLES_DIR, "material", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        count2_entity = conn.execute("SELECT COUNT(*) FROM entity").fetchone()[0]
        count2_member = conn.execute("SELECT COUNT(*) FROM member").fetchone()[0]
        conn.close()

        assert count1_entity == count2_entity
        assert count1_member == count2_member


class TestMultipleSections:
    """Tests that loading two sections into the same database works."""

    def test_two_sections_load_cleanly(self, db_path: Path) -> None:
        """Loading material then widgets must both succeed."""
        r1 = run_load(SAMPLES_DIR, "material", db_path)
        assert r1.returncode == 0, r1.stderr
        r2 = run_load(SAMPLES_DIR, "widgets", db_path)
        assert r2.returncode == 0, r2.stderr

    def test_two_sections_have_separate_library_rows(self, db_path: Path) -> None:
        """Each section must produce its own library row."""
        run_load(SAMPLES_DIR, "material", db_path)
        run_load(SAMPLES_DIR, "widgets", db_path)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        count = conn.execute("SELECT COUNT(*) FROM library").fetchone()[0]
        conn.close()
        assert count == 2
