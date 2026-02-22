"""Load-specific test fixtures and helpers."""

import shutil
import sqlite3
import subprocess
from pathlib import Path

import pytest


# Path to load sample markdown files (generated from convert samples)
SAMPLES_DIR = Path(__file__).parent / "integration" / "samples"


def run_load(
    doc_dir: Path,
    section: str,
    db_file: Path,
    verbose: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run the load command with the given arguments.

    Args:
        doc_dir: Path to markdown documents directory (convert.py output).
        section: Section name to load.
        db_file: Path to the sqlite3 database file to create or update.
        verbose: Whether to enable verbose output.

    Returns:
        CompletedProcess with stdout, stderr, and returncode.
    """
    uv_path = shutil.which("uv")
    if uv_path is None:
        pytest.skip("uv not found in PATH")

    cmd = [
        uv_path,
        "run",
        "load",
        "-d",
        str(doc_dir),
        "-s",
        section,
        "-o",
        str(db_file),
    ]
    if verbose:
        cmd.append("-v")

    return subprocess.run(cmd, capture_output=True, text=True)


def run_load_list(
    doc_dir: Path,
    section_list_file: Path,
    db_file: Path,
    verbose: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run the load command using a section list file (-S).

    Args:
        doc_dir: Path to markdown documents directory (convert.py output).
        section_list_file: Path to text file containing section names.
        db_file: Path to the sqlite3 database file to create or update.
        verbose: Whether to enable verbose output.

    Returns:
        CompletedProcess with stdout, stderr, and returncode.
    """
    uv_path = shutil.which("uv")
    if uv_path is None:
        pytest.skip("uv not found in PATH")

    cmd = [
        uv_path,
        "run",
        "load",
        "-d",
        str(doc_dir),
        "-S",
        str(section_list_file),
        "-o",
        str(db_file),
    ]
    if verbose:
        cmd.append("-v")

    return subprocess.run(cmd, capture_output=True, text=True)


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    """Provide a path for a sqlite3 database that does not yet exist.

    Returns:
        Path inside a temporary directory where the DB should be created.
    """
    return tmp_path / "test.db"


@pytest.fixture
def loaded_material_db(db_path: Path) -> sqlite3.Connection:
    """Run load on the material samples and return an open DB connection.

    Returns:
        Open sqlite3.Connection with row_factory = sqlite3.Row.
    """
    result = run_load(SAMPLES_DIR, "material", db_path)
    assert result.returncode == 0, f"load failed:\n{result.stderr}"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
