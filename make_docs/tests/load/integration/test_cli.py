"""Integration tests for load CLI argument parsing and validation."""

from pathlib import Path

import pytest

from load.conftest import SAMPLES_DIR, run_load


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

    def test_invalid_section_exits_nonzero(self, db_path: Path) -> None:
        """Running load with a section that doesn't exist must fail."""
        result = run_load(SAMPLES_DIR, "doesnotexist", db_path)
        assert result.returncode != 0

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
