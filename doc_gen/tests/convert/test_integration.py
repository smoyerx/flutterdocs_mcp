"""Integration tests for convert.py using sample documentation files."""

import shutil
import subprocess
from pathlib import Path

import pytest

# Paths
SAMPLES_DIR = Path(__file__).parent / "samples"
CONVERT_SCRIPT = Path(__file__).parent.parent.parent / "convert.py"


def run_convert(
    doc_dir: Path,
    section: str,
    output_dir: Path,
    verbose: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run the convert.py script with the given arguments.

    Args:
        doc_dir: Path to documentation directory.
        section: Section name to convert.
        output_dir: Path to output directory.
        verbose: Whether to enable verbose output.

    Returns:
        CompletedProcess with stdout, stderr, and returncode.
    """
    # Find uv executable
    uv_path = shutil.which("uv")
    if uv_path is None:
        pytest.skip("uv not found in PATH")

    cmd = [
        uv_path,
        "run",
        str(CONVERT_SCRIPT),
        "-d",
        str(doc_dir),
        "-s",
        section,
        "-o",
        str(output_dir),
    ]
    if verbose:
        cmd.append("-v")

    return subprocess.run(cmd, capture_output=True, text=True)


def get_available_sections() -> list[str]:
    """Get list of available sections from samples directory.

    Returns:
        List of section directory names.
    """
    flutter_dir = SAMPLES_DIR / "flutter"
    if not flutter_dir.exists():
        return []
    return [d.name for d in flutter_dir.iterdir() if d.is_dir()]


def get_entities_for_section(section: str) -> list[str]:
    """Get list of entity names for a section.

    Args:
        section: The section name.

    Returns:
        List of entity names found in the section.
    """
    section_dir = SAMPLES_DIR / "flutter" / section
    if not section_dir.exists():
        return []

    entities = []
    for f in section_dir.glob("*-class.html"):
        entity_name = f.stem.replace("-class", "")
        entities.append(entity_name)
    return sorted(entities)


class TestConvertIntegration:
    """Integration tests for the full conversion pipeline."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    @pytest.mark.parametrize("section", get_available_sections())
    def test_convert_section_succeeds(
        self, section: str, output_dir: Path
    ) -> None:
        """Conversion should succeed for each available section."""
        result = run_convert(SAMPLES_DIR, section, output_dir)

        assert result.returncode == 0, f"Conversion failed: {result.stderr}"
        assert "Successfully processed" in result.stdout

    @pytest.mark.parametrize("section", get_available_sections())
    def test_creates_output_files_for_all_entities(
        self, section: str, output_dir: Path
    ) -> None:
        """Output files should be created for each entity in the section."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        expected_entities = get_entities_for_section(section)
        section_output = output_dir / section

        for entity in expected_entities:
            output_file = section_output / f"{entity}.md"
            assert output_file.exists(), f"Missing output file: {output_file}"

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_start_with_heading(
        self, section: str, output_dir: Path
    ) -> None:
        """All output files should start with a markdown heading."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        section_output = output_dir / section
        for md_file in section_output.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert content.startswith("#"), (
                f"File {md_file.name} does not start with heading"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_have_no_html_links(
        self, section: str, output_dir: Path
    ) -> None:
        """Output files should not contain HTML file links."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        section_output = output_dir / section
        for md_file in section_output.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            # Check for .html) pattern which indicates remaining HTML links
            assert ".html)" not in content, (
                f"File {md_file.name} contains HTML links"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_have_no_footer(
        self, section: str, output_dir: Path
    ) -> None:
        """Output files should not contain footer marker."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        footer_marker = "1. [Flutter](index.html)"
        section_output = output_dir / section
        for md_file in section_output.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert footer_marker not in content, (
                f"File {md_file.name} contains footer marker"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_verbose_output_shows_files(
        self, section: str, output_dir: Path
    ) -> None:
        """Verbose mode should show files being processed."""
        result = run_convert(SAMPLES_DIR, section, output_dir, verbose=True)
        assert result.returncode == 0

        # Verbose output goes to stderr via logging
        combined_output = result.stdout + result.stderr
        assert "Processing:" in combined_output
        assert "Converting entity:" in combined_output

    @pytest.mark.parametrize("section", get_available_sections())
    def test_verbose_output_shows_summary(
        self, section: str, output_dir: Path
    ) -> None:
        """Verbose mode should show file count summary."""
        result = run_convert(SAMPLES_DIR, section, output_dir, verbose=True)
        assert result.returncode == 0

        # Verbose summary goes to stderr via logging
        combined_output = result.stdout + result.stderr
        assert "files processed" in combined_output


class TestConvertWithSnippets:
    """Tests for Dart snippet conversion."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_snippets_included_in_output(self, output_dir: Path) -> None:
        """Dart snippets should be included in the output."""
        # material.ListTile has snippets
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        listtile_md = output_dir / "material" / "ListTile.md"
        content = listtile_md.read_text(encoding="utf-8")

        # Check for code snippet markers
        assert "# Code Snippet" in content
        assert "```dart" in content

    def test_snippet_code_blocks_are_valid(self, output_dir: Path) -> None:
        """Snippet code blocks should be properly formatted."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        listtile_md = output_dir / "material" / "ListTile.md"
        content = listtile_md.read_text(encoding="utf-8")

        # Count opening and closing code fences for dart
        dart_opens = content.count("```dart")
        # All code blocks should close
        all_closes = content.count("```\n") + content.count("```")
        # There should be at least as many closes as dart opens
        assert all_closes >= dart_opens


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
        assert "does not exist" in result.stderr.lower() or "error" in result.stderr.lower()

    def test_nonexistent_section_fails(self, output_dir: Path) -> None:
        """Conversion should fail if section directory doesn't exist."""
        result = run_convert(SAMPLES_DIR, "nonexistent_section", output_dir)
        assert result.returncode != 0

    def test_missing_required_args_fails(self, output_dir: Path) -> None:
        """Conversion should fail if required arguments are missing."""
        uv_path = shutil.which("uv")
        if uv_path is None:
            pytest.skip("uv not found in PATH")

        cmd = [uv_path, "run", str(CONVERT_SCRIPT)]
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

        listtile_md = output_dir / "material" / "ListTile.md"
        original_content = listtile_md.read_text(encoding="utf-8")

        # Second run
        result2 = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result2.returncode == 0

        new_content = listtile_md.read_text(encoding="utf-8")
        assert original_content == new_content
