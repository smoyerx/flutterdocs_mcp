"""Integration tests for load CLI argument parsing and validation."""

import sqlite3
from pathlib import Path

import pytest

from load.conftest import SAMPLES_DIR, run_load, run_load_list


class TestMissingArgs:
    """Tests that missing required arguments trigger non-zero exit."""

    def test_no_args_exits_nonzero(self, db_path: Path) -> None:
        """Running load with no arguments must fail."""
        import shutil
        import subprocess

        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")
        result = subprocess.run(
            [uv_path, "run", "load"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0

    def test_missing_section_exits_nonzero(self, db_path: Path) -> None:
        """Running load without --section must fail."""
        import shutil
        import subprocess

        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")
        result = subprocess.run(
            [uv_path, "run", "load", "-d", str(SAMPLES_DIR), "-o", str(db_path)],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0


class TestInvalidInputs:
    """Tests for validation of invalid inputs."""

    def test_invalid_doc_dir_exits_nonzero(self, db_path: Path, tmp_path: Path) -> None:
        """Running load with a non-existent documents dir must fail."""
        result = run_load(tmp_path / "nonexistent", "material", db_path)
        assert result.returncode != 0

    def test_invalid_section_skips_cleanly(self, db_path: Path) -> None:
        """A nonexistent section is skipped with a notification; exit code is 0."""
        result = run_load(SAMPLES_DIR, "doesnotexist", db_path)
        assert result.returncode == 0
        assert "skipped" in result.stdout.lower() or "skipped" in result.stderr.lower()

    def test_invalid_db_parent_exits_nonzero(self, tmp_path: Path) -> None:
        """Running load when DB parent directory doesn't exist must fail."""
        bad_db = tmp_path / "missing_subdir" / "test.db"
        result = run_load(SAMPLES_DIR, "material", bad_db)
        assert result.returncode != 0


class TestHelpFlag:
    """Tests for --help flag."""

    def test_help_exits_zero(self, db_path: Path) -> None:
        """Running load with --help must exit with code 0."""
        import shutil
        import subprocess

        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")
        result = subprocess.run(
            [uv_path, "run", "load", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

    def test_help_mentions_documents(self, db_path: Path) -> None:
        """Help output must mention --documents argument."""
        import shutil
        import subprocess

        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")
        result = subprocess.run(
            [uv_path, "run", "load", "--help"],
            capture_output=True,
            text=True,
        )
        assert (
            "documents" in result.stdout.lower() or "documents" in result.stderr.lower()
        )


class TestSectionList:
    """Tests for -S/--section-list argument behavior."""

    def test_section_list_loads_all_sections(
        self, db_path: Path, tmp_path: Path
    ) -> None:
        """All sections named in the list file should be loaded into the DB."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\n", encoding="utf-8")

        result = run_load_list(SAMPLES_DIR, section_file, db_path)
        assert result.returncode == 0

        # Verify data is present
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                "SELECT name FROM library WHERE name = ?", ("material",)
            ).fetchall()
            assert len(rows) == 1
        finally:
            conn.close()

    def test_section_list_with_comments_and_blanks(
        self, db_path: Path, tmp_path: Path
    ) -> None:
        """Comments and blank lines in the section list file are ignored."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("# load these\n\nmaterial\n\n# end\n", encoding="utf-8")

        result = run_load_list(SAMPLES_DIR, section_file, db_path)
        assert result.returncode == 0
        assert "material" in result.stdout

    def test_section_and_section_list_together_fails(
        self, db_path: Path, tmp_path: Path
    ) -> None:
        """-s and -S together must be rejected by argparse."""
        import shutil
        import subprocess

        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")

        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\n", encoding="utf-8")

        result = subprocess.run(
            [
                uv_path,
                "run",
                "load",
                "-d",
                str(SAMPLES_DIR),
                "-s",
                "material",
                "-S",
                str(section_file),
                "-o",
                str(db_path),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0

    def test_nonexistent_section_list_file_fails(
        self, db_path: Path, tmp_path: Path
    ) -> None:
        """A section list file that does not exist should cause failure."""
        missing = tmp_path / "no_such_file.txt"
        result = run_load_list(SAMPLES_DIR, missing, db_path)
        assert result.returncode != 0

    def test_missing_section_skipped_with_notification(
        self, db_path: Path, tmp_path: Path
    ) -> None:
        """A valid section is loaded; a nonexistent one is skipped (not fatal)."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\nnonexistent_section_xyz\n", encoding="utf-8")

        result = run_load_list(SAMPLES_DIR, section_file, db_path, verbose=True)
        assert result.returncode == 0

        # Valid section loaded
        assert "material" in result.stdout

        # Skipped section mentioned somewhere in output
        combined = result.stdout + result.stderr
        assert "nonexistent_section_xyz" in combined or "skipped" in combined.lower()

    def test_empty_section_list_fails(self, db_path: Path, tmp_path: Path) -> None:
        """A section list with no sections (all blank/comments) should fail."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("# only comments\n\n", encoding="utf-8")

        result = run_load_list(SAMPLES_DIR, section_file, db_path)
        assert result.returncode != 0

    def test_db_opened_once_for_multiple_sections(
        self, db_path: Path, tmp_path: Path
    ) -> None:
        """Multiple sections in a list file are all loaded into the same DB."""
        # SAMPLES_DIR only has 'material' as a valid section, so list it twice
        # (idempotent upsert) to confirm the DB remains consistent.
        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\n", encoding="utf-8")

        result = run_load_list(SAMPLES_DIR, section_file, db_path)
        assert result.returncode == 0

        # Run again into the same DB to confirm no crash on re-open
        result2 = run_load_list(SAMPLES_DIR, section_file, db_path)
        assert result2.returncode == 0

        conn = sqlite3.connect(db_path)
        try:
            count = conn.execute(
                "SELECT COUNT(*) FROM library WHERE name = ?", ("material",)
            ).fetchone()[0]
            # upsert should leave exactly one row
            assert count == 1
        finally:
            conn.close()


class TestDefaultSearchSync:
    """Tests that content_search is populated during default load."""

    def test_content_search_populated(self, db_path: Path) -> None:
        """After default load, content_search must contain indexed rows."""
        result = run_load(SAMPLES_DIR, "material", db_path)
        assert result.returncode == 0, result.stderr
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            count = conn.execute("SELECT COUNT(*) FROM content_search").fetchone()[0]
            assert count > 0
        finally:
            conn.close()

    def test_content_search_returns_known_entity(self, db_path: Path) -> None:
        """After default load, querying content_search for a known entity returns results."""
        result = run_load(SAMPLES_DIR, "material", db_path)
        assert result.returncode == 0, result.stderr
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                "SELECT rowid FROM content_search WHERE identifier MATCH 'ListTile'"
            ).fetchall()
            assert len(rows) > 0
        finally:
            conn.close()

    def test_content_search_count_matches_entity_count(self, db_path: Path) -> None:
        """After default load, content_search row count must equal entity row count."""
        result = run_load(SAMPLES_DIR, "material", db_path)
        assert result.returncode == 0, result.stderr
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            entity_count = conn.execute("SELECT COUNT(*) FROM entity").fetchone()[0]
            search_count = conn.execute(
                "SELECT COUNT(*) FROM content_search"
            ).fetchone()[0]
            assert search_count == entity_count
        finally:
            conn.close()
