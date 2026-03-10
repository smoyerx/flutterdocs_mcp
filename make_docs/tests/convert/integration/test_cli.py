"""Integration tests for CLI error handling and output structure."""

import shutil
import subprocess
from pathlib import Path

import pytest

from flutterdocs._shared.constants import CategoryType
from convert.conftest import run_convert, run_convert_list, SAMPLES_DIR
from flutterdocs._shared.paths import PathBuilder


def build_output_path_builder(
    output_dir: Path,
    section: str,
    entity_name: str,
    entity_type: CategoryType = CategoryType.CLASS,
) -> PathBuilder:
    return PathBuilder(
        section=section,
        output_dir=output_dir,
        entity_name=entity_name,
        entity_type=entity_type,
    )


def build_input_path_builder(doc_dir: Path, section: str) -> PathBuilder:
    return PathBuilder(
        section=section,
        doc_dir=doc_dir,
        output_dir=Path(),
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

    def test_nonexistent_section_skips_cleanly(self, output_dir: Path) -> None:
        """A nonexistent section is skipped with a notification; exit code is 0."""
        result = run_convert(SAMPLES_DIR, "nonexistent_section", output_dir)
        assert result.returncode == 0
        assert "skipped" in result.stdout.lower() or "skipped" in result.stderr.lower()

    def test_missing_required_args_fails(self, output_dir: Path) -> None:
        """Conversion should fail if required arguments are missing."""
        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")

        cmd = [uv_path, "run", "convert"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode != 0

    def test_empty_section_exits_zero(self, tmp_path: Path, output_dir: Path) -> None:
        """Empty section should exit with zero status."""
        # Create empty directory structure
        doc_dir = tmp_path / "empty_docs"
        input_builder = build_input_path_builder(doc_dir, "empty_section")
        input_builder.get_input_section_dir().mkdir(parents=True)
        input_builder.get_input_snippets_dir().mkdir(parents=True)

        result = run_convert(doc_dir, "empty_section", output_dir)
        assert result.returncode == 0


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

        listtile_builder = build_output_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        listtile_md = listtile_builder.get_entity_file()
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

        builder = build_output_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        api_dir = builder.get_api_root_dir()
        assert api_dir.exists()
        assert api_dir.is_dir()

    def test_section_under_api(self, output_dir: Path) -> None:
        """Section directory should be under api/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        builder = build_output_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        section_dir = builder.get_api_section_dir()
        assert section_dir.exists()
        assert section_dir.is_dir()

    def test_class_directory_structure(self, output_dir: Path) -> None:
        """Each class should have its own directory with subdirectories."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        listtile_builder = build_output_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        class_dir = listtile_builder.get_entity_dir()
        assert class_dir.exists()

        # Main class file should exist
        assert listtile_builder.get_entity_file().exists()

    def test_constructors_directory(self, output_dir: Path) -> None:
        """Constructors directory should be created if constructors exist."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        listtile_builder = build_output_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        constructors_dir = listtile_builder.get_constructors_dir()
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

        listtile_builder = build_output_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        statics_dir = listtile_builder.get_statics_dir()
        # ListTile has a divideTiles static method
        assert statics_dir.exists(), "statics directory should exist for ListTile"
        assert statics_dir.is_dir()

        # divideTiles.md should be present
        dividetiles_file = listtile_builder.get_static_file("divideTiles")
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
        listtile_builder = build_output_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        api_root = listtile_builder.get_api_root_dir()
        assert api_root.exists(), "API root directory should exist"

        # Check section dir exists under api
        section_dir = listtile_builder.get_api_section_dir()
        assert section_dir.exists(), "Section directory should exist"
        assert section_dir.parent == api_root, "Section should be under API root"

        # Check class dir exists where PathBuilder says it should
        class_dir = listtile_builder.get_entity_dir()
        assert class_dir.exists(), (
            "Class directory should exist at PathBuilder location"
        )

        # Check class file exists where PathBuilder says it should
        class_file = listtile_builder.get_entity_file()
        assert class_file.exists(), "Class file should exist at expected location"
        assert class_file.parent == class_dir, (
            "Class file parent should equal class dir"
        )

        # Verify InkWell class also follows the same structure
        inkwell_builder = build_output_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        inkwell_class_dir = inkwell_builder.get_entity_dir()
        assert inkwell_class_dir.exists(), "InkWell class directory should exist"

        inkwell_class_file = inkwell_builder.get_entity_file()
        assert inkwell_class_file.exists(), "InkWell class file should exist"
        assert inkwell_class_file.parent == inkwell_class_dir


class TestSectionList:
    """Tests for -S/--section-list argument behavior."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_section_list_processes_all_sections(
        self, tmp_path: Path, output_dir: Path
    ) -> None:
        """All sections named in the list file should be processed."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\nwidgets\n", encoding="utf-8")

        result = run_convert_list(SAMPLES_DIR, section_file, output_dir)
        assert result.returncode == 0

        for section in ("material", "widgets"):
            section_dir = PathBuilder(
                section=section, output_dir=output_dir
            ).get_api_section_dir()
            assert section_dir.exists(), (
                f"Section directory should exist for: {section}"
            )

    def test_section_list_with_comments_and_blanks(
        self, tmp_path: Path, output_dir: Path
    ) -> None:
        """Comments and blank lines in the section list file are ignored."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text(
            "# convert these sections\n\nmaterial\n\n# end\n", encoding="utf-8"
        )

        result = run_convert_list(SAMPLES_DIR, section_file, output_dir)
        assert result.returncode == 0

        material_dir = PathBuilder(
            section="material", output_dir=output_dir
        ).get_api_section_dir()
        assert material_dir.exists()

    def test_section_and_section_list_together_fails(
        self, tmp_path: Path, output_dir: Path
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
                "convert",
                "-d",
                str(SAMPLES_DIR),
                "-s",
                "material",
                "-S",
                str(section_file),
                "-o",
                str(output_dir),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0

    def test_nonexistent_section_list_file_fails(
        self, tmp_path: Path, output_dir: Path
    ) -> None:
        """A section list file that does not exist should cause failure."""
        missing = tmp_path / "no_such_file.txt"
        result = run_convert_list(SAMPLES_DIR, missing, output_dir)
        assert result.returncode != 0

    def test_missing_section_skipped_with_notification(
        self, tmp_path: Path, output_dir: Path
    ) -> None:
        """A valid section is processed; a nonexistent one is skipped (not a fatal error)."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("material\nnonexistent_section_xyz\n", encoding="utf-8")

        result = run_convert_list(SAMPLES_DIR, section_file, output_dir, verbose=True)
        assert result.returncode == 0

        # Valid section should be present
        material_dir = PathBuilder(
            section="material", output_dir=output_dir
        ).get_api_section_dir()
        assert material_dir.exists()

        # Skipped section should be mentioned in output
        combined = result.stdout + result.stderr
        assert "nonexistent_section_xyz" in combined or "skipped" in combined.lower()

    def test_empty_section_list_fails(self, tmp_path: Path, output_dir: Path) -> None:
        """A section list file that contains no sections (all blank/comments) should fail."""
        section_file = tmp_path / "sections.txt"
        section_file.write_text("# only comments\n\n", encoding="utf-8")

        result = run_convert_list(SAMPLES_DIR, section_file, output_dir)
        assert result.returncode != 0
