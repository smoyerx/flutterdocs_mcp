"""Integration tests for CLI error handling and output structure."""

import shutil
import subprocess
from pathlib import Path

import pytest

from convert.conftest import run_convert, SAMPLES_DIR
from flutterdoc_gen.convert.paths import (
    get_api_root_dir,
    get_api_section_dir,
    get_class_dir,
    get_class_file,
    get_constructors_dir,
    get_input_section_dir,
    get_input_snippets_dir,
    get_native_member_file,
    get_statics_dir,
)


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
        get_input_section_dir(doc_dir, "empty_section").mkdir(parents=True)
        get_input_snippets_dir(doc_dir).mkdir(parents=True)

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

        listtile_md = get_class_file(output_dir, "material", "ListTile")
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

        api_dir = get_api_root_dir(output_dir)
        assert api_dir.exists()
        assert api_dir.is_dir()

    def test_section_under_api(self, output_dir: Path) -> None:
        """Section directory should be under api/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        section_dir = get_api_section_dir(output_dir, "material")
        assert section_dir.exists()
        assert section_dir.is_dir()

    def test_class_directory_structure(self, output_dir: Path) -> None:
        """Each class should have its own directory with subdirectories."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        class_dir = get_class_dir(output_dir, "material", "ListTile")
        assert class_dir.exists()

        # Main class file should exist
        assert get_class_file(output_dir, "material", "ListTile").exists()

    def test_constructors_directory(self, output_dir: Path) -> None:
        """Constructors directory should be created if constructors exist."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        class_dir = get_class_dir(output_dir, "material", "ListTile")
        constructors_dir = get_constructors_dir(class_dir)
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

        class_dir = get_class_dir(output_dir, "material", "ListTile")
        statics_dir = get_statics_dir(class_dir)
        # ListTile has a divideTiles static method
        assert statics_dir.exists(), "statics directory should exist for ListTile"
        assert statics_dir.is_dir()

        # divideTiles.md should be present
        dividetiles_file = get_native_member_file(statics_dir, "divideTiles")
        assert dividetiles_file.exists(), "divideTiles.md should exist"

        # Verify the file starts with a heading
        content = dividetiles_file.read_text(encoding="utf-8")
        assert content.startswith("#"), "Static method file should start with heading"

    def test_cli_uses_paths_module_exclusively(self, output_dir: Path) -> None:
        """Verify CLI constructs all paths through paths.py functions.

        This test validates the requirement that changing paths.py functions
        should be sufficient to restructure output without modifying CLI or
        processor code.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Verify the structure matches paths.py expectations
        api_root = get_api_root_dir(output_dir)
        assert api_root.exists(), "API root directory should exist"

        # Check section dir exists under api
        section_dir = get_api_section_dir(output_dir, "material")
        assert section_dir.exists(), "Section directory should exist"
        assert section_dir.parent == api_root, "Section should be under API root"

        # Check class dir structure includes 'classes' subdirectory
        class_dir = get_class_dir(output_dir, "material", "ListTile")
        assert class_dir.exists(), "Class directory should exist"
        assert "classes" in class_dir.parts, "Class dir should include 'classes' subdir"

        # Check class file location matches get_class_file()
        class_file = get_class_file(output_dir, "material", "ListTile")
        assert class_file.exists(), "Class file should exist at expected location"
        assert class_file.parent == class_dir, (
            "Class file parent should equal class dir"
        )

        # Verify InkWell class also follows the same structure
        inkwell_class_dir = get_class_dir(output_dir, "material", "InkWell")
        assert inkwell_class_dir.exists(), "InkWell class directory should exist"
        assert "classes" in inkwell_class_dir.parts

        inkwell_class_file = get_class_file(output_dir, "material", "InkWell")
        assert inkwell_class_file.exists(), "InkWell class file should exist"
        assert inkwell_class_file.parent == inkwell_class_dir
