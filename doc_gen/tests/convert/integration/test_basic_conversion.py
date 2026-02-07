"""Integration tests for basic conversion pipeline functionality.

Tests core conversion mechanics: directory and file creation, success checks,
output formatting, and verbose mode.
"""

from pathlib import Path

import pytest

from convert.conftest import (
    build_entity_path_builder,
    build_section_path_builder,
    get_available_sections,
    get_class_names_for_section,
    run_convert,
    SAMPLES_DIR,
)
from flutterdoc_gen.convert.constants import CategoryType
from flutterdoc_gen.convert.transformations import FOOTER_MARKER


class TestBasicConversion:
    """Integration tests for basic conversion functionality."""

    @pytest.mark.parametrize("section", get_available_sections())
    def test_convert_section_succeeds(self, section: str, output_dir: Path) -> None:
        """Conversion should succeed for each available section."""
        result = run_convert(SAMPLES_DIR, section, output_dir)

        assert result.returncode == 0, f"Conversion failed: {result.stderr}"
        assert "Successfully processed" in result.stdout

    @pytest.mark.parametrize("section", get_available_sections())
    def test_creates_class_directories(self, section: str, output_dir: Path) -> None:
        """Class directories should be created under api/{section}/{class}/."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        expected_class_names = get_class_names_for_section(section)

        for class_name in expected_class_names:
            class_builder = build_entity_path_builder(
                output_dir, section, class_name, CategoryType.CLASS
            )
            class_dir = class_builder.get_entity_dir()
            assert class_dir.exists(), f"Missing class directory: {class_dir}"
            assert class_dir.is_dir()

    @pytest.mark.parametrize("section", get_available_sections())
    def test_creates_main_class_file(self, section: str, output_dir: Path) -> None:
        """Main class markdown file should be created."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        expected_class_names = get_class_names_for_section(section)

        for class_name in expected_class_names:
            class_builder = build_entity_path_builder(
                output_dir, section, class_name, CategoryType.CLASS
            )
            class_file = class_builder.get_entity_file()
            assert class_file.exists(), f"Missing class file: {class_file}"

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_start_with_heading(
        self, section: str, output_dir: Path
    ) -> None:
        """All output files should start with a markdown heading."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        section_builder = build_section_path_builder(output_dir, section)
        api_section_dir = section_builder.get_api_section_dir()
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert content.startswith("#"), (
                f"File {md_file} does not start with heading"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_have_no_footer(self, section: str, output_dir: Path) -> None:
        """Output files should not contain footer marker."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = build_section_path_builder(
            output_dir, section
        ).get_api_section_dir()
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert FOOTER_MARKER not in content, (
                f"File {md_file} contains footer marker"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_verbose_output_shows_processing(
        self, section: str, output_dir: Path
    ) -> None:
        """Verbose mode should show processing information."""
        result = run_convert(SAMPLES_DIR, section, output_dir, verbose=True)
        assert result.returncode == 0

        # Verbose output goes to stderr via logging
        combined_output = result.stdout + result.stderr
        assert "Processing" in combined_output
        assert "Converting class:" in combined_output
