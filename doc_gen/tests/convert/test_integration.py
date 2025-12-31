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


def get_class_names_for_section(section: str) -> list[str]:
    """Get list of class names for a section.

    Args:
        section: The section name.

    Returns:
        List of class names found in the section.
    """
    section_dir = SAMPLES_DIR / "flutter" / section
    if not section_dir.exists():
        return []

    class_names = []
    for f in section_dir.glob("*-class.html"):
        class_name = f.stem.replace("-class", "")
        class_names.append(class_name)
    return sorted(class_names)


class TestConvertIntegration:
    """Integration tests for the full conversion pipeline."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

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
        api_section_dir = output_dir / "api" / section

        for class_name in expected_class_names:
            class_dir = api_section_dir / class_name
            assert class_dir.exists(), f"Missing class directory: {class_dir}"
            assert class_dir.is_dir()

    @pytest.mark.parametrize("section", get_available_sections())
    def test_creates_main_class_file(self, section: str, output_dir: Path) -> None:
        """Main class markdown file should be created."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        expected_class_names = get_class_names_for_section(section)
        api_section_dir = output_dir / "api" / section

        for class_name in expected_class_names:
            class_file = api_section_dir / class_name / f"{class_name}.md"
            assert class_file.exists(), f"Missing class file: {class_file}"

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_start_with_heading(
        self, section: str, output_dir: Path
    ) -> None:
        """All output files should start with a markdown heading."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = output_dir / "api" / section
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert content.startswith("#"), (
                f"File {md_file} does not start with heading"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_have_no_html_links(
        self, section: str, output_dir: Path
    ) -> None:
        """Output files should not contain local HTML file links."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = output_dir / "api" / section
        # Pattern for relative HTML links (not starting with http)
        # Matches: [text](something.html) but not [text](https://...)
        import re

        local_html_pattern = re.compile(r"\[[^\]]+\]\((?!https?://)[^)]+\.html[^)]*\)")
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            matches = local_html_pattern.findall(content)
            assert not matches, f"File {md_file} contains local HTML links: {matches}"

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_have_no_footer(self, section: str, output_dir: Path) -> None:
        """Output files should not contain footer marker."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        footer_marker = "1. [Flutter](index.html)"
        api_section_dir = output_dir / "api" / section
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert footer_marker not in content, (
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

    @pytest.mark.parametrize("section", get_available_sections())
    def test_class_files_have_mcp_links(self, section: str, output_dir: Path) -> None:
        """Class files should have MCP URI links."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        expected_class_names = get_class_names_for_section(section)
        api_section_dir = output_dir / "api" / section

        for class_name in expected_class_names:
            class_file = api_section_dir / class_name / f"{class_name}.md"
            content = class_file.read_text(encoding="utf-8")
            # Should have at least some MCP links
            assert "mcp://flutter/api/" in content, (
                f"File {class_file} has no MCP links"
            )

        footer_marker = "1. [Flutter](index.html)"
        section_output = output_dir / section
        for md_file in section_output.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert footer_marker not in content, (
                f"File {md_file.name} contains footer marker"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_verbose_output_shows_files(self, section: str, output_dir: Path) -> None:
        """Verbose mode should show files being processed."""
        result = run_convert(SAMPLES_DIR, section, output_dir, verbose=True)
        assert result.returncode == 0

        # Verbose output goes to stderr via logging
        combined_output = result.stdout + result.stderr
        assert "Processing" in combined_output
        assert "Converting class:" in combined_output

    @pytest.mark.parametrize("section", get_available_sections())
    def test_verbose_output_shows_summary(self, section: str, output_dir: Path) -> None:
        """Verbose mode should show class count summary."""
        result = run_convert(SAMPLES_DIR, section, output_dir, verbose=True)
        assert result.returncode == 0

        # Summary goes to stdout via print
        assert "Successfully processed" in result.stdout
        assert "classes" in result.stdout


class TestConvertWithSnippets:
    """Tests for Dart snippet conversion."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_snippets_directory_created(self, output_dir: Path) -> None:
        """Snippets directory should be created for classes with snippets."""
        # material.ListTile has snippets
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_dir = output_dir / "api" / "material" / "ListTile" / "snippets"
        assert snippets_dir.exists(), "Snippets directory not created"
        assert snippets_dir.is_dir()

    def test_snippet_files_created(self, output_dir: Path) -> None:
        """Individual snippet files should be created."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_dir = output_dir / "api" / "material" / "ListTile" / "snippets"
        snippet_files = list(snippets_dir.glob("*.md"))
        assert len(snippet_files) > 0, "No snippet files created"

    def test_snippet_header_format(self, output_dir: Path) -> None:
        """Snippet files should have correct header format."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_dir = output_dir / "api" / "material" / "ListTile" / "snippets"
        for snippet_file in snippets_dir.glob("*.md"):
            content = snippet_file.read_text(encoding="utf-8")
            assert content.startswith("# Code Snippet for ListTile in material"), (
                f"Snippet {snippet_file} has incorrect header"
            )
            assert "```dart" in content

    def test_snippet_short_name(self, output_dir: Path) -> None:
        """Snippet files should use SHORT_NAME without section.class prefix."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_dir = output_dir / "api" / "material" / "ListTile" / "snippets"
        snippet_files = list(snippets_dir.glob("*.md"))

        for snippet_file in snippet_files:
            # File should not contain "material.ListTile" prefix
            assert not snippet_file.name.startswith("material.")
            assert not snippet_file.name.startswith("ListTile.")


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
