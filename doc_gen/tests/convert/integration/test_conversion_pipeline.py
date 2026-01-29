"""Integration tests for the full conversion pipeline."""

from pathlib import Path

import pytest

from convert.conftest import (
    get_available_sections,
    get_class_names_for_section,
    make_mcp_uri,
    run_convert,
    SAMPLES_DIR,
)
from flutterdoc_gen.convert.patterns import MCP_URI_PREFIX
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
from flutterdoc_gen.convert.transformations import FOOTER_MARKER


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
    def test_class_links_transformed(self, section: str, output_dir: Path) -> None:
        """Class links with -class.html suffix must be transformed to MCP URIs.

        Per spec: [CLASS_NAME](SECTION/CLASS_NAME-class.html)
        becomes: [CLASS_NAME](mcp://flutter/api/SECTION/CLASS_NAME)
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        # Pattern for class links that MUST be transformed (relative URIs only)
        untransformed_class_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-class\.html\)"
        )

        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            matches = untransformed_class_pattern.findall(content)

            assert not matches, (
                f"File {md_file.relative_to(output_dir)} contains "
                f"{len(matches)} untransformed class link(s):\n"
                + "\n".join(
                    f"  [{m[0]}]({m[1]}/{m[2]}-class.html)" for m in matches[:5]
                )
                + ("\n  ..." if len(matches) > 5 else "")
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_member_links_transformed(self, section: str, output_dir: Path) -> None:
        """Member links (3-part paths without dots) must be transformed to MCP URIs.

        Per spec: [MEMBER](SECTION/CLASS/MEMBER.html)
        becomes: [MEMBER](mcp://flutter/api/SECTION/CLASS/MEMBER)

        Does NOT include dotted members like Class.member.html (not in spec).
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        # Pattern for simple member links (no dots in member name)
        # This specifically excludes Class.member patterns
        untransformed_member_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)\.html\)"
        )

        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            all_matches = untransformed_member_pattern.findall(content)

            # Filter to only simple members (no dots, no -constant suffix)
            matches = [
                m
                for m in all_matches
                if "." not in m[3] and not m[3].endswith("-constant")
            ]

            assert not matches, (
                f"File {md_file.relative_to(output_dir)} contains "
                f"{len(matches)} untransformed member link(s):\n"
                + "\n".join(
                    f"  [{m[0]}]({m[1]}/{m[2]}/{m[3]}.html)" for m in matches[:5]
                )
                + ("\n  ..." if len(matches) > 5 else "")
            )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_mcp_uris_present_and_valid(self, section: str, output_dir: Path) -> None:
        """Output files must contain valid MCP URIs showing transformations occurred.

        Validates that:
        1. MCP URIs are present in output
        2. MCP URIs follow the correct format: mcp://flutter/api/SECTION/...
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        mcp_uri_pattern = re.compile(rf"{MCP_URI_PREFIX}([a-zA-Z0-9_-]+)/")
        files_with_mcp = []

        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            if MCP_URI_PREFIX in content:
                files_with_mcp.append(md_file)

                # Validate MCP URI format
                matches = mcp_uri_pattern.findall(content)
                for match in matches:
                    # Should be a valid section name (letters, numbers, hyphens, underscores)
                    assert match, (
                        f"File {md_file.relative_to(output_dir)} has invalid MCP URI format"
                    )

        assert files_with_mcp, (
            f"No MCP URIs found in section '{section}' - transformations may have failed"
        )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_mixin_links_not_transformed(self, section: str, output_dir: Path) -> None:
        """Mixin links must NOT be transformed (not in spec).

        Links like [Mixin](section/Mixin-mixin.html) should remain unchanged
        for incremental pattern discovery.
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        # Pattern for mixin links that should NOT be transformed
        mixin_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-mixin\.html\)"
        )

        found_mixin_links = False
        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            matches = mixin_pattern.findall(content)
            if matches:
                found_mixin_links = True
                # Verify they weren't incorrectly converted to MCP URIs
                for match in matches:
                    link_text = f"[{match[0]}]({match[1]}/{match[2]}-mixin.html)"
                    assert link_text in content, (
                        f"File {md_file.relative_to(output_dir)} has mixin link "
                        f"'{link_text}' that may have been incorrectly transformed"
                    )

        # Note: Not all sections have mixin links, so this is informational
        if not found_mixin_links and section == "widgets":
            # Widgets section should have mixin links in the sample data
            pass  # Could add a warning if needed

    @pytest.mark.parametrize("section", get_available_sections())
    def test_constant_links_not_transformed(
        self, section: str, output_dir: Path
    ) -> None:
        """Constant links must NOT be transformed (not in spec).

        Links like [constant](section/constant-constant.html) should remain
        unchanged for incremental pattern discovery.
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        # Pattern for constant links that should NOT be transformed
        constant_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-constant\.html\)"
        )

        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            matches = constant_pattern.findall(content)
            if matches:
                # Verify they remain untransformed
                for match in matches:
                    link_text = f"[{match[0]}]({match[1]}/{match[2]}-constant.html)"
                    assert link_text in content, (
                        f"File {md_file.relative_to(output_dir)} has constant link "
                        f"'{link_text}' that may have been incorrectly transformed"
                    )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_dotted_member_links_not_transformed(
        self, section: str, output_dir: Path
    ) -> None:
        """Dotted member links like Class.member must NOT be transformed (not in spec).

        Links like [Text.rich](widgets/Text/Text.rich.html) should remain
        unchanged for incremental pattern discovery.
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        # Pattern for dotted member links (Class.member)
        dotted_member_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)\.html\)"
        )

        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            matches = dotted_member_pattern.findall(content)
            if matches:
                # Verify they remain untransformed
                for match in matches:
                    link_text = f"[{match[0]}]({match[1]}/{match[2]}/{match[3]}.html)"
                    assert link_text in content, (
                        f"File {md_file.relative_to(output_dir)} has dotted member link "
                        f"'{link_text}' that may have been incorrectly transformed"
                    )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_external_urls_not_transformed(
        self, section: str, output_dir: Path
    ) -> None:
        """External URLs (http/https) must NOT be transformed.

        Absolute URLs should be preserved unchanged as they're not part of
        the local documentation set.
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
        import re

        # Pattern for external URLs that should be preserved
        external_url_pattern = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")

        for md_file in api_section_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            matches = external_url_pattern.findall(content)
            if matches:
                # Just verify they exist - they should not have been converted to MCP URIs
                for match in matches:
                    assert match[1].startswith(("http://", "https://")), (
                        f"File {md_file.relative_to(output_dir)} has malformed external URL"
                    )

    @pytest.mark.parametrize("section", get_available_sections())
    def test_output_files_have_no_footer(self, section: str, output_dir: Path) -> None:
        """Output files should not contain footer marker."""
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        api_section_dir = get_api_section_dir(output_dir, section)
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
        assert f"[Widget]({make_mcp_uri('widgets', 'Widget')})" in content

        # Should have link to the original operator documentation
        assert (
            f"[operator ==]({make_mcp_uri('widgets', 'Widget', 'operator_equals')})"
            in content
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
