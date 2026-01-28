"""Integration tests for the full conversion pipeline."""

from pathlib import Path

import pytest

from convert.conftest import (
    get_available_sections,
    get_class_names_for_section,
    run_convert,
    SAMPLES_DIR,
)
from flutterdoc_gen.convert.paths import (
    get_api_section_dir,
    get_class_dir,
    get_class_file,
    get_class_inherited_member_file,
    get_class_methods_inherited_dir,
    get_class_operators_inherited_dir,
    get_class_properties_inherited_dir,
    get_class_snippets_dir,
    get_inherited_member_file,
)


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

        for class_name in expected_class_names:
            class_dir = get_class_dir(output_dir, section, class_name)
            assert class_dir.exists(), f"Missing class directory: {class_dir}"
            assert class_dir.is_dir()

    @pytest.mark.parametrize("section", get_available_sections())
    def test_creates_main_class_file(self, section: str, output_dir: Path) -> None:
        """Main class markdown file should be created."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        expected_class_names = get_class_names_for_section(section)

        for class_name in expected_class_names:
            class_file = get_class_file(output_dir, section, class_name)
            assert class_file.exists(), f"Missing class file: {class_file}"

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_start_with_heading(
        self, section: str, output_dir: Path
    ) -> None:
        """All output files should start with a markdown heading."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert content.startswith("#"), (
                f"File {md_file} does not start with heading"
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_spec_defined_link_patterns_are_transformed(
        self, section: str, output_dir: Path
    ) -> None:
        """Spec-defined link patterns should be transformed to MCP URIs.

        The converter transforms class links (-class.html, .html) and member links
        (section/class/member.html) to MCP URIs. Other patterns like -mixin.html
        and -constant.html are intentionally left untransformed and logged for
        future pattern discovery.
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        # Patterns that SHOULD be transformed (should NOT appear in output)
        class_link_pattern = re.compile(
            r"\[[^\]]+\]\((?!https?://)[a-zA-Z0-9_-]+/[a-zA-Z0-9_]+-class\.html\)"
        )
        member_link_pattern = re.compile(
            r"\[[^\]]+\]\((?!https?://)[a-zA-Z0-9_-]+/[a-zA-Z0-9_]+/[a-zA-Z0-9_.]+\.html\)"
        )

        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")

            class_matches = class_link_pattern.findall(content)
            assert not class_matches, (
                f"File {md_file} contains untransformed class links: {class_matches}"
            )

            member_matches = member_link_pattern.findall(content)
            # Filter out known unhandled patterns (-constant.html in 3-part paths)
            member_matches = [m for m in member_matches if "-constant.html" not in m]
            assert not member_matches, (
                f"File {md_file} contains untransformed member links: {member_matches}"
            )

        # Verify MCP URIs are present (transformations occurred)
        mcp_pattern = re.compile(r"mcp://flutter/api/")
        has_mcp_links = False
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            if mcp_pattern.search(content):
                has_mcp_links = True
                break
        assert has_mcp_links, "No MCP URIs found - transformations may have failed"

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_have_no_footer(self, section: str, output_dir: Path) -> None:
        """Output files should not contain footer marker."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        footer_marker = "1. [Flutter](index.html)"
        api_section_dir = get_api_section_dir(output_dir, section)
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

        for class_name in expected_class_names:
            class_file = get_class_file(output_dir, section, class_name)
            content = class_file.read_text(encoding="utf-8")
            # Should have at least some MCP links
            assert "mcp://flutter/api/" in content, (
                f"File {class_file} has no MCP links"
            )


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

        snippets_dir = get_class_snippets_dir(output_dir, "material", "ListTile")
        assert snippets_dir.exists(), "Snippets directory not created"
        assert snippets_dir.is_dir()

    def test_snippet_files_created(self, output_dir: Path) -> None:
        """Individual snippet files should be created."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_dir = get_class_snippets_dir(output_dir, "material", "ListTile")
        snippet_files = list(snippets_dir.glob("*.md"))
        assert len(snippet_files) > 0, "No snippet files created"

    def test_snippet_header_format(self, output_dir: Path) -> None:
        """Snippet files should have correct header format."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_dir = get_class_snippets_dir(output_dir, "material", "ListTile")
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

        snippets_dir = get_class_snippets_dir(output_dir, "material", "ListTile")
        snippet_files = list(snippets_dir.glob("*.md"))

        for snippet_file in snippet_files:
            # File should not contain "material.ListTile" prefix
            assert not snippet_file.name.startswith("material.")
            assert not snippet_file.name.startswith("ListTile.")


class TestInheritedMemberGeneration:
    """Tests for inherited member file generation."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_inherited_operator_file_generated(self, output_dir: Path) -> None:
        """Inherited operator files should be generated for classes with inherited operators."""
        # InkWell inherits operator == from Widget
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        operator_file = get_class_inherited_member_file(
            output_dir,
            "material",
            "InkWell",
            "operators",
            "widgets",
            "Widget",
            "operator_equals",
        )
        assert operator_file.exists(), (
            f"Missing inherited operator file: {operator_file}"
        )

    def test_inherited_operator_file_content(self, output_dir: Path) -> None:
        """Inherited operator files should have correct content."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        operator_file = get_class_inherited_member_file(
            output_dir,
            "material",
            "InkWell",
            "operators",
            "widgets",
            "Widget",
            "operator_equals",
        )
        content = operator_file.read_text(encoding="utf-8")

        # Should have title with operator symbol and member name
        assert content.startswith("# operator == (operator_equals)")

        # Should reference the parent class
        assert "This operator is inherited from" in content
        assert "[Widget](mcp://flutter/api/widgets/Widget)" in content

        # Should have link to the original operator documentation
        assert (
            "[operator ==](mcp://flutter/api/widgets/Widget/operator_equals)" in content
        )

    def test_inherited_properties_generated(self, output_dir: Path) -> None:
        """Inherited property files should be generated."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # InkWell inherits properties from InkResponse and Widget
        inherited_props_dir = get_class_properties_inherited_dir(
            output_dir, "material", "InkWell"
        )
        assert inherited_props_dir.exists()

        # Check for at least some inherited properties
        prop_files = list(inherited_props_dir.glob("*.md"))
        assert len(prop_files) > 0, "No inherited property files generated"

        # Verify one specific inherited property from Widget
        hashcode_file = get_inherited_member_file(
            inherited_props_dir, "widgets", "Widget", "hashCode"
        )
        assert hashcode_file.exists(), f"Missing inherited property: {hashcode_file}"

    def test_inherited_methods_generated(self, output_dir: Path) -> None:
        """Inherited method files should be generated."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # InkWell inherits methods from InkResponse and StatelessWidget
        inherited_methods_dir = get_class_methods_inherited_dir(
            output_dir, "material", "InkWell"
        )
        assert inherited_methods_dir.exists()

        # Check for at least some inherited methods
        method_files = list(inherited_methods_dir.glob("*.md"))
        assert len(method_files) > 0, "No inherited method files generated"

        # Verify one specific inherited method
        build_file = get_inherited_member_file(
            inherited_methods_dir, "material", "InkResponse", "build"
        )
        assert build_file.exists(), f"Missing inherited method: {build_file}"

    def test_inherited_operators_generated(self, output_dir: Path) -> None:
        """Inherited operator files should be generated."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # InkWell inherits operators from Widget
        inherited_operators_dir = get_class_operators_inherited_dir(
            output_dir, "material", "InkWell"
        )
        assert inherited_operators_dir.exists()

        # Check for at least some inherited operators
        operator_files = list(inherited_operators_dir.glob("*.md"))
        assert len(operator_files) > 0, "No inherited operator files generated"

        # Verify one specific inherited operator from Widget
        equals_file = get_inherited_member_file(
            inherited_operators_dir, "widgets", "Widget", "operator_equals"
        )
        assert equals_file.exists(), f"Missing inherited operator: {equals_file}"
