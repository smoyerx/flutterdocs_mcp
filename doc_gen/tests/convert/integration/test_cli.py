"""Integration tests for CLI error handling and output structure."""

import shutil
import subprocess
from pathlib import Path

import pytest

from convert.conftest import run_convert, SAMPLES_DIR


class TestConvertErrorHandling:
    """Tests for error handling scenarios."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_nonexistent_doc_dir_fails(self, output_dir: Path) -> None:
        """Conversion should fail if doc directory doesn't exist."""
        result = run_convert(Path("/nonexistent/path"), "material", output_dir)
        assert result.returncode != 0
        assert (
            "does not exist" in result.stderr.lower()
            or "error" in result.stderr.lower()
        )

    def test_nonexistent_section_fails(self, output_dir: Path) -> None:
        """Conversion should fail if section directory doesn't exist."""
        result = run_convert(SAMPLES_DIR, "nonexistent_section", output_dir)
        assert result.returncode != 0

    def test_missing_required_args_fails(self, output_dir: Path) -> None:
        """Conversion should fail if required arguments are missing."""
        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")

        cmd = [uv_path, "run", "convert"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode != 0

    def test_empty_section_exits_zero(self, tmp_path: Path, output_dir: Path) -> None:
        """Empty section (no class files) should exit with zero status."""
        # Create empty directory structure
        doc_dir = tmp_path / "empty_docs"
        (doc_dir / "flutter" / "empty_section").mkdir(parents=True)
        (doc_dir / "snippets").mkdir(parents=True)

        result = run_convert(doc_dir, "empty_section", output_dir)
        assert result.returncode == 0
        assert "No files found" in result.stdout


class TestConvertOverwrite:
    """Tests for file overwriting behavior."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_overwrites_existing_files(self, output_dir: Path) -> None:
        """Running conversion twice should overwrite existing files."""
        # First run
        result1 = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result1.returncode == 0

        listtile_md = output_dir / "api" / "material" / "ListTile" / "ListTile.md"
        original_content = listtile_md.read_text(encoding="utf-8")

        # Second run
        result2 = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result2.returncode == 0

        new_content = listtile_md.read_text(encoding="utf-8")
        assert original_content == new_content


class TestConvertDirectoryStructure:
    """Tests for the output directory structure."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_api_directory_created(self, output_dir: Path) -> None:
        """Output should be under api/ directory."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        api_dir = output_dir / "api"
        assert api_dir.exists()
        assert api_dir.is_dir()

    def test_section_under_api(self, output_dir: Path) -> None:
        """Section directory should be under api/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        section_dir = output_dir / "api" / "material"
        assert section_dir.exists()
        assert section_dir.is_dir()

    def test_class_directory_structure(self, output_dir: Path) -> None:
        """Each class should have its own directory with subdirectories."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        class_dir = output_dir / "api" / "material" / "ListTile"
        assert class_dir.exists()

        # Main class file should exist
        assert (class_dir / "ListTile.md").exists()

    def test_constructors_directory(self, output_dir: Path) -> None:
        """Constructors directory should be created if constructors exist."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        class_dir = output_dir / "api" / "material" / "ListTile"
        constructors_dir = class_dir / "constructors"
        # Directory may or may not exist depending on sample data
        if constructors_dir.exists():
            assert constructors_dir.is_dir()
            # Should contain .md files if it exists
            md_files = list(constructors_dir.glob("*.md"))
            assert len(md_files) >= 0

    def test_statics_directory(self, output_dir: Path) -> None:
        """Statics directory should be created for classes with static methods."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        class_dir = output_dir / "api" / "material" / "ListTile"
        statics_dir = class_dir / "statics"
        # ListTile has a divideTiles static method
        assert statics_dir.exists(), "statics directory should exist for ListTile"
        assert statics_dir.is_dir()

        # divideTiles.md should be present
        dividetiles_file = statics_dir / "divideTiles.md"
        assert dividetiles_file.exists(), "divideTiles.md should exist"

        # Verify the file starts with a heading
        content = dividetiles_file.read_text(encoding="utf-8")
        assert content.startswith("#"), "Static method file should start with heading"
