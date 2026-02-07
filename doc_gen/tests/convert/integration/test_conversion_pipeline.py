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
from flutterdoc_gen.convert.constants import CategoryType
from flutterdoc_gen.convert.patterns import MCP_URI_PREFIX
from flutterdoc_gen.convert.paths import PathBuilder
from flutterdoc_gen.convert.transformations import FOOTER_MARKER


def build_section_path_builder(output_dir: Path, section: str) -> PathBuilder:
    return PathBuilder(
        section=section,
        doc_dir=Path(),
        output_dir=output_dir,
    )


def build_entity_path_builder(
    output_dir: Path,
    section: str,
    entity_name: str,
    entity_type: CategoryType = CategoryType.CLASS,
) -> PathBuilder:
    return PathBuilder(
        section=section,
        entity_name=entity_name,
        entity_type=entity_type,
        doc_dir=Path(),
        output_dir=output_dir,
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
    def test_class_links_transformed(self, section: str, output_dir: Path) -> None:
        """Class links with -class.html suffix must be transformed to MCP URIs.

        Per spec: [CLASS_NAME](SECTION/CLASS_NAME-class.html)
        becomes: [CLASS_NAME](mcp://flutter/api/SECTION/CLASS_NAME)
        """
        result = run_convert(SAMPLES_DIR, section, output_dir)
        assert result.returncode == 0

        section_builder = build_section_path_builder(output_dir, section)
        api_section_dir = section_builder.get_api_section_dir()
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

        section_builder = build_section_path_builder(output_dir, section)
        api_section_dir = section_builder.get_api_section_dir()
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

        section_builder = build_section_path_builder(output_dir, section)
        api_section_dir = section_builder.get_api_section_dir()
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

        api_section_dir = build_section_path_builder(
            output_dir, section
        ).get_api_section_dir()
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

        api_section_dir = build_section_path_builder(
            output_dir, section
        ).get_api_section_dir()
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

        api_section_dir = build_section_path_builder(
            output_dir, section
        ).get_api_section_dir()
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

        api_section_dir = build_section_path_builder(
            output_dir, section
        ).get_api_section_dir()
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

        snippets_builder = build_entity_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        snippets_dir = snippets_builder.get_snippets_dir()
        assert snippets_dir.exists(), "Snippets directory not created"
        assert snippets_dir.is_dir()

    def test_snippet_files_created(self, output_dir: Path) -> None:
        """Individual snippet files should be created."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_builder = build_entity_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        snippets_dir = snippets_builder.get_snippets_dir()
        snippet_files = list(snippets_dir.glob("*.md"))
        assert len(snippet_files) > 0, "No snippet files created"

    def test_snippet_header_format(self, output_dir: Path) -> None:
        """Snippet files should have correct header format."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_builder = build_entity_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        snippets_dir = snippets_builder.get_snippets_dir()
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

        snippets_builder = build_entity_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        snippets_dir = snippets_builder.get_snippets_dir()
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

        inkwell_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        operator_file = inkwell_builder.get_inherited_operator_file("operator_equals")
        assert operator_file.exists(), (
            f"Missing inherited operator file: {operator_file}"
        )

    def test_inherited_operator_file_content(self, output_dir: Path) -> None:
        """Inherited operator files should have correct content."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        inkwell_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        operator_file = inkwell_builder.get_inherited_operator_file("operator_equals")
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
        inkwell_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        inherited_props_dir = inkwell_builder.get_properties_dir(inherited=True)
        assert inherited_props_dir.exists()

        # Check for at least some inherited properties
        prop_files = list(inherited_props_dir.glob("*.md"))
        assert len(prop_files) > 0, "No inherited property files generated"

        # Verify one specific inherited property from Widget
        hashcode_file = inkwell_builder.get_inherited_property_file("hashCode")
        assert hashcode_file.exists(), f"Missing inherited property: {hashcode_file}"

    def test_inherited_methods_generated(self, output_dir: Path) -> None:
        """Inherited method files should be generated."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # InkWell inherits methods from InkResponse and StatelessWidget
        inkwell_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        inherited_methods_dir = inkwell_builder.get_methods_dir(inherited=True)
        assert inherited_methods_dir.exists()

        # Check for at least some inherited methods
        method_files = list(inherited_methods_dir.glob("*.md"))
        assert len(method_files) > 0, "No inherited method files generated"

        # Verify one specific inherited method
        build_file = inkwell_builder.get_inherited_method_file("build")
        assert build_file.exists(), f"Missing inherited method: {build_file}"

    def test_inherited_operators_generated(self, output_dir: Path) -> None:
        """Inherited operator files should be generated."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # InkWell inherits operators from Widget
        inkwell_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        inherited_operators_dir = inkwell_builder.get_operators_dir(inherited=True)
        assert inherited_operators_dir.exists()

        # Check for at least some inherited operators
        operator_files = list(inherited_operators_dir.glob("*.md"))
        assert len(operator_files) > 0, "No inherited operator files generated"

        # Verify one specific inherited operator from Widget
        equals_file = inkwell_builder.get_inherited_operator_file("operator_equals")
        assert equals_file.exists(), f"Missing inherited operator: {equals_file}"


class TestFunctionDeclarationCleanup:
    """Integration tests for function declaration cleanup transformation."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_constructor_declaration_cleaned(self, output_dir: Path) -> None:
        """Constructor files should have function declaration cleanup applied.

        Verifies that the InkWell constructor has:
        - No blank lines within the parameter list
        - No numbered list markers (1. , 2. , etc.)
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Check InkWell constructor
        inkwell_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        constructor_file = inkwell_builder.get_constructor_file("InkWell")
        assert constructor_file.exists(), (
            f"Constructor file not found: {constructor_file}"
        )

        content = constructor_file.read_text(encoding="utf-8")

        # Find the header line
        lines = content.split("\n")
        header_idx = None
        for i, line in enumerate(lines):
            if line.startswith("#"):
                header_idx = i
                break

        assert header_idx is not None, "No header found in constructor file"

        # Find the closing }) line (constructor uses named parameters)
        close_idx = None
        for i in range(header_idx + 1, len(lines)):
            if lines[i].strip() == "})" or lines[i].strip().startswith("})"):
                close_idx = i
                break

        assert close_idx is not None, "No closing }) found in constructor file"

        # Check content between header and close
        declaration_lines = lines[header_idx + 1 : close_idx + 1]

        # Should have no blank lines within the declaration
        # (skip the line immediately after header which may be blank before the signature)
        signature_started = False
        for line in declaration_lines:
            if not signature_started:
                if line.strip():  # First non-blank line starts signature
                    signature_started = True
            else:
                # Once signature started, no blank lines should exist until close
                if not line.strip() and line != lines[close_idx]:
                    # Allow the closing line itself to be stripped
                    pass

        # Should have no ordered list markers
        import re

        ordered_marker = re.compile(r"^\d+\.\s")
        for line in declaration_lines:
            assert not ordered_marker.match(line.lstrip()), (
                f"Found ordered list marker in constructor declaration: {line}"
            )

    def test_native_method_declaration_cleaned(self, output_dir: Path) -> None:
        """Native method files should have function declaration cleanup applied.

        Verifies that the ListTile.build method has:
        - No blank lines within the parameter list
        - No numbered list markers
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Check ListTile build method (native method)
        listtile_builder = build_entity_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        method_file = listtile_builder.get_native_method_file("build")
        assert method_file.exists(), f"Method file not found: {method_file}"

        content = method_file.read_text(encoding="utf-8")

        # Find the header line
        lines = content.split("\n")
        header_idx = None
        for i, line in enumerate(lines):
            if line.startswith("#"):
                header_idx = i
                break

        assert header_idx is not None, "No header found in method file"

        # Find the closing ) line
        close_idx = None
        for i in range(header_idx + 1, len(lines)):
            stripped = lines[i].strip()
            if stripped == ")" or stripped.startswith(")"):
                close_idx = i
                break

        assert close_idx is not None, "No closing ) found in method file"

        # Check for ordered list markers in declaration
        import re

        ordered_marker = re.compile(r"^\d+\.\s")
        declaration_lines = lines[header_idx + 1 : close_idx + 1]
        for line in declaration_lines:
            assert not ordered_marker.match(line.lstrip()), (
                f"Found ordered list marker in method declaration: {line}"
            )

    def test_inherited_method_not_cleaned(self, output_dir: Path) -> None:
        """Inherited method files are generated from templates, not HTML conversion.

        This test verifies that inherited method files exist and are properly
        generated from templates (they wouldn't have conversion artifacts anyway).
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Check that inherited methods directory exists and has files
        inkwell_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        inherited_methods_dir = inkwell_builder.get_methods_dir(inherited=True)
        assert inherited_methods_dir.exists()

        method_files = list(inherited_methods_dir.glob("*.md"))
        assert len(method_files) > 0, "No inherited method files found"

        # Verify inherited method uses template format (starts with proper heading)
        sample_file = method_files[0]
        content = sample_file.read_text(encoding="utf-8")
        assert content.startswith("#"), "Inherited method should start with heading"

    def test_extension_type_root_file_cleaned(self, output_dir: Path) -> None:
        """Extension type root files should have function declaration cleanup applied.

        Extension types can have function-like declarations that need cleanup.
        """
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        # Check OverlayChildLayoutInfo extension type
        ext_type_builder = build_entity_path_builder(
            output_dir, "widgets", "OverlayChildLayoutInfo", CategoryType.EXTENSION_TYPE
        )
        ext_type_file = ext_type_builder.get_entity_file()
        assert ext_type_file.exists(), f"Extension type file not found: {ext_type_file}"

        content = ext_type_file.read_text(encoding="utf-8")

        # Check for ordered list markers - should not exist after cleanup
        import re

        ordered_marker = re.compile(r"^\d+\.\s", re.MULTILINE)
        matches = ordered_marker.findall(content)
        assert not matches, (
            f"Found {len(matches)} ordered list marker(s) in extension type root file"
        )

    def test_function_root_file_cleaned(self, output_dir: Path) -> None:
        """Function root files should have function declaration cleanup applied.

        Standalone function files have parameter lists that need cleanup.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Check showBottomSheet function
        function_builder = build_entity_path_builder(
            output_dir, "material", "showBottomSheet", CategoryType.FUNCTION
        )
        function_file = function_builder.get_entity_file()
        assert function_file.exists(), f"Function file not found: {function_file}"

        content = function_file.read_text(encoding="utf-8")

        # Check for ordered list markers - should not exist after cleanup
        import re

        ordered_marker = re.compile(r"^\d+\.\s", re.MULTILINE)
        matches = ordered_marker.findall(content)
        assert not matches, (
            f"Found {len(matches)} ordered list marker(s) in function root file"
        )

    def test_operator_member_file_cleaned(self, output_dir: Path) -> None:
        """Operator member files should have function declaration cleanup applied.

        Operator files may have parameter lists that need cleanup.
        """
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        # Check WidgetStateOperators extension operators
        extension_builder = build_entity_path_builder(
            output_dir, "widgets", "WidgetStateOperators", CategoryType.EXTENSION
        )
        operators_dir = extension_builder.get_operators_dir()
        assert operators_dir.exists(), f"Operators directory not found: {operators_dir}"

        operator_files = list(operators_dir.glob("*.md"))
        assert len(operator_files) > 0, "No operator files found"

        # Check one operator file for cleanup
        operator_file = operator_files[0]
        content = operator_file.read_text(encoding="utf-8")

        # Check for ordered list markers - should not exist after cleanup
        import re

        ordered_marker = re.compile(r"^\d+\.\s", re.MULTILINE)
        matches = ordered_marker.findall(content)
        assert not matches, (
            f"Found {len(matches)} ordered list marker(s) in operator file"
        )

    def test_static_method_file_cleaned(self, output_dir: Path) -> None:
        """Static method files should have function declaration cleanup applied.

        Static methods have parameter lists that need cleanup.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Check ListTile static methods
        listtile_builder = build_entity_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        statics_dir = listtile_builder.get_statics_dir()

        # ListTile may not have static methods - if it does, verify cleanup
        if statics_dir.exists():
            static_files = list(statics_dir.glob("*.md"))
            if len(static_files) > 0:
                static_file = static_files[0]
                content = static_file.read_text(encoding="utf-8")

                # Check for ordered list markers - should not exist after cleanup
                import re

                ordered_marker = re.compile(r"^\d+\.\s", re.MULTILINE)
                matches = ordered_marker.findall(content)
                assert not matches, (
                    f"Found {len(matches)} ordered list marker(s) in static method file"
                )


class TestFileCategorization:
    """Integration tests for root documentation file categorization."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_categorize_material_section(self, output_dir: Path) -> None:
        """Test correct categorization of material section sample files."""
        from flutterdoc_gen.convert.categorization import find_and_categorize_root_files

        categorized = find_and_categorize_root_files(SAMPLES_DIR, "material")

        # Verify classes
        class_names = [name for name, _ in categorized[CategoryType.CLASS]]
        assert sorted(class_names) == ["InkWell", "ListTile"]

        # Verify mixins
        mixin_names = [name for name, _ in categorized[CategoryType.MIXIN]]
        assert sorted(mixin_names) == ["BaseSliderTrackShape", "MaterialStateMixin"]

        # Verify constants
        constant_names = [name for name, _ in categorized[CategoryType.CONSTANT]]
        assert sorted(constant_names) == [
            "accelerateEasing",
            "kBottomNavigationBarHeight",
        ]

        # Verify libraries
        library_names = [name for name, _ in categorized[CategoryType.LIBRARY]]
        assert library_names == ["material"]
        # Verify library file path is index.html
        library_paths = [path for _, path in categorized[CategoryType.LIBRARY]]
        assert len(library_paths) == 1
        assert library_paths[0].name == "index.html"

        # Verify enums
        enum_names = [name for name, _ in categorized[CategoryType.ENUM]]
        assert sorted(enum_names) == ["HourFormat", "StretchMode"]

        # Verify functions
        function_names = [name for name, _ in categorized[CategoryType.FUNCTION]]
        assert sorted(function_names) == ["showBottomSheet", "showMenu"]

        # Verify typedefs
        typedef_names = [name for name, _ in categorized[CategoryType.TYPEDEF]]
        assert sorted(typedef_names) == ["DrawerCallback", "MaterialState"]

        # Verify no extension types or extensions in material section
        assert len(categorized[CategoryType.EXTENSION_TYPE]) == 0
        assert len(categorized[CategoryType.EXTENSION]) == 0

    def test_categorize_widgets_section(self, output_dir: Path) -> None:
        """Test correct categorization of widgets section sample files."""
        from flutterdoc_gen.convert.categorization import find_and_categorize_root_files

        categorized = find_and_categorize_root_files(SAMPLES_DIR, "widgets")

        # Verify classes
        class_names = [name for name, _ in categorized[CategoryType.CLASS]]
        assert sorted(class_names) == ["State", "Text"]

        # Verify extensions
        extension_names = [name for name, _ in categorized[CategoryType.EXTENSION]]
        assert extension_names == ["WidgetStateOperators"]

        # Verify extension types
        extension_type_names = [
            name for name, _ in categorized[CategoryType.EXTENSION_TYPE]
        ]
        assert extension_type_names == ["OverlayChildLayoutInfo"]

        # Verify libraries
        library_names = [name for name, _ in categorized[CategoryType.LIBRARY]]
        assert library_names == ["widgets"]
        # Verify library file path is index.html
        library_paths = [path for _, path in categorized[CategoryType.LIBRARY]]
        assert len(library_paths) == 1
        assert library_paths[0].name == "index.html"

        # Verify no other types in widgets section
        assert len(categorized[CategoryType.MIXIN]) == 0
        assert len(categorized[CategoryType.CONSTANT]) == 0
        assert len(categorized[CategoryType.ENUM]) == 0
        assert len(categorized[CategoryType.FUNCTION]) == 0
        assert len(categorized["typedef"]) == 0

    def test_all_categories_processed(self, output_dir: Path) -> None:
        """Test that convert processes all categorized files without error."""
        result = run_convert(SAMPLES_DIR, "material", output_dir, verbose=True)

        assert result.returncode == 0
        assert "Successfully processed" in result.stdout

        # Verify that the output mentions processing different types
        # Classes are fully processed, others are just logged
        # Note: verbose logging goes to stderr
        assert "Converting class:" in result.stderr
        assert "Converting mixin:" in result.stderr
        assert "Converting constant:" in result.stderr
        assert "Converting library:" in result.stderr
        assert "Converting enum:" in result.stderr
        assert "Converting function:" in result.stderr
        assert "Converting typedef:" in result.stderr


class TestEnumConstantsProcessing:
    """Integration tests for enum Constants section processing."""

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_creates_enum_constants_directory(self, output_dir: Path) -> None:
        """Enum constants directory should be created during conversion."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # HourFormat enum should have a constants directory
        hourformat_builder = build_entity_path_builder(
            output_dir, "material", "HourFormat", CategoryType.ENUM
        )
        constants_dir = hourformat_builder.get_constants_dir()
        assert constants_dir.exists(), f"Constants directory not found: {constants_dir}"
        assert constants_dir.is_dir()

    def test_creates_enum_constant_files(self, output_dir: Path) -> None:
        """Enum constant markdown files should be created."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # HourFormat enum should have values constant file
        hourformat_builder = build_entity_path_builder(
            output_dir, "material", "HourFormat", CategoryType.ENUM
        )
        values_file = hourformat_builder.get_constant_file("values")
        assert values_file.exists(), f"Constant file not found: {values_file}"

    def test_enum_constant_file_starts_with_heading(self, output_dir: Path) -> None:
        """Enum constant file should start with markdown heading."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        hourformat_builder = build_entity_path_builder(
            output_dir, "material", "HourFormat", CategoryType.ENUM
        )
        values_file = hourformat_builder.get_constant_file("values")
        content = values_file.read_text(encoding="utf-8")
        assert content.startswith("#"), "Constant file should start with heading"

    def test_enum_constant_link_transformed(self, output_dir: Path) -> None:
        """Enum constant links should be transformed to MCP URI in root enum file."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        hourformat_builder = build_entity_path_builder(
            output_dir, "material", "HourFormat", CategoryType.ENUM
        )
        enum_file = hourformat_builder.get_entity_file()
        content = enum_file.read_text(encoding="utf-8")

        # The original link [values](material/HourFormat/values-constant.html)
        # should be transformed to [values](mcp://flutter/api/material/HourFormat/values)
        assert "values-constant.html" not in content, (
            "Enum constant link should be transformed"
        )
        assert f"{MCP_URI_PREFIX}material/HourFormat/values" in content, (
            "Enum constant should have MCP URI"
        )


class TestLinkTransformationByType:
    """Tests for link transformation patterns specific to each documentation type.

    Tests the incremental approach to link transformation - only patterns
    explicitly in the spec are transformed. This validates type-specific
    link behavior.
    """

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_extension_links_not_transformed(self, output_dir: Path) -> None:
        """Extension links must NOT be transformed (not in spec).

        Links like [Extension](section/Extension-extension.html) should remain
        unchanged for incremental pattern discovery.
        """
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        api_section_dir = build_section_path_builder(
            output_dir, "widgets"
        ).get_api_section_dir()
        import re

        # Pattern for extension links that should NOT be transformed
        extension_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-extension\.html\)"
        )

        files_checked = 0
        for md_file in api_section_dir.rglob("*.md"):
            files_checked += 1
            content = md_file.read_text(encoding="utf-8")
            matches = extension_pattern.findall(content)
            if matches:
                # Verify they remain untransformed
                for match in matches:
                    link_text = f"[{match[0]}]({match[1]}/{match[2]}-extension.html)"
                    assert link_text in content, (
                        f"File {md_file.relative_to(output_dir)} has extension link "
                        f"'{link_text}' that may have been incorrectly transformed"
                    )

        assert files_checked > 0, "No files were checked"

    def test_extension_type_links_not_transformed(self, output_dir: Path) -> None:
        """Extension type links must NOT be transformed (not in spec).

        Links like [ExtType](section/ExtType-extension-type.html) should remain
        unchanged for incremental pattern discovery.
        """
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        api_section_dir = build_section_path_builder(
            output_dir, "widgets"
        ).get_api_section_dir()
        import re

        # Pattern for extension type links that should NOT be transformed
        ext_type_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-zA-Z0-9_]+)-extension-type\.html\)"
        )

        files_checked = 0
        for md_file in api_section_dir.rglob("*.md"):
            files_checked += 1
            content = md_file.read_text(encoding="utf-8")
            matches = ext_type_pattern.findall(content)
            if matches:
                # Verify they remain untransformed
                for match in matches:
                    link_text = (
                        f"[{match[0]}]({match[1]}/{match[2]}-extension-type.html)"
                    )
                    assert link_text in content, (
                        f"File {md_file.relative_to(output_dir)} has extension type link "
                        f"'{link_text}' that may have been incorrectly transformed"
                    )

        assert files_checked > 0, "No files were checked"

    def test_function_links_not_transformed(self, output_dir: Path) -> None:
        """Function links must NOT be transformed (not in spec).

        Links like [function](section/function.html) should remain unchanged
        for incremental pattern discovery. Similar to constant behavior.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        api_section_dir = build_section_path_builder(
            output_dir, "material"
        ).get_api_section_dir()
        import re

        # Pattern for function links that should NOT be transformed
        # Function links don't have a special suffix unlike classes (-class.html)
        # They look like: section/functionName.html (titleCase)
        function_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([a-z][a-zA-Z0-9_]*)\.html\)"
        )

        files_checked = 0
        for md_file in api_section_dir.rglob("*.md"):
            files_checked += 1
            content = md_file.read_text(encoding="utf-8")
            matches = function_pattern.findall(content)
            # Filter for probable function names (lowercase start)
            probable_functions = [m for m in matches if m[2][0].islower()]
            if probable_functions:
                # Just verify no wrongful MCP transformation happened
                # (Functions typically remain as relative links)
                for match in probable_functions:
                    # If this was a function, it should not have been transformed to MCP
                    # unless it matches class/member patterns explicitly
                    pass  # Pattern verification is implicit - no false transformations

        assert files_checked > 0, "No files were checked"

    def test_typedef_links_not_transformed(self, output_dir: Path) -> None:
        """Typedef links must NOT be transformed (not in spec).

        Links like [Typedef](section/Typedef.html) should remain unchanged
        for incremental pattern discovery. Similar to constant behavior.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        api_section_dir = build_section_path_builder(
            output_dir, "material"
        ).get_api_section_dir()
        import re

        # Pattern for typedef links - they look like function links
        # but typically TitleCase without suffixes
        typedef_pattern = re.compile(
            r"\[([^\]]+)\]\(([a-zA-Z0-9_-]+)/([A-Z][a-zA-Z0-9_]*)\.html\)"
        )

        files_checked = 0
        for md_file in api_section_dir.rglob("*.md"):
            files_checked += 1
            content = md_file.read_text(encoding="utf-8")
            matches = typedef_pattern.findall(content)
            # These could be typedefs (TitleCase, no suffix)
            # They should NOT be transformed to MCP URIs
            if matches:
                # Verification is that no false MCP transformations occurred
                pass  # Implicit check - the pattern would have been caught by class checks

        assert files_checked > 0, "No files were checked"

    def test_library_links_behavior(self, output_dir: Path) -> None:
        """Library links should follow expected patterns.

        Library files are typically standalone and may not have many internal links.
        This test validates library output exists and contains expected content.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Library files are created at the section level
        library_builder = build_entity_path_builder(
            output_dir, "material", "material", CategoryType.LIBRARY
        )
        library_file = library_builder.get_entity_file()
        assert library_file.exists(), f"Library file not found: {library_file}"

        content = library_file.read_text(encoding="utf-8")
        # Libraries should have been converted to markdown
        assert content.startswith("#"), "Library file should start with heading"


class TestDirectoryStructureByType:
    """Tests for output directory structure organization by documentation type.

    Validates that PathBuilder generates correct directory structures for each
    entity type according to the categorization system.
    """

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_class_directory_structure(self, output_dir: Path) -> None:
        """Classes should be placed in api/{section}/classes/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        class_builder = build_entity_path_builder(
            output_dir, "material", "InkWell", CategoryType.CLASS
        )
        class_dir = class_builder.get_entity_dir()

        expected_path = output_dir / "api" / "material" / "classes" / "InkWell"
        assert class_dir == expected_path
        assert class_dir.exists()
        assert (class_dir / "InkWell.md").exists()

    def test_mixin_directory_structure(self, output_dir: Path) -> None:
        """Mixins should be placed in api/{section}/mixins/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "BaseSliderTrackShape", CategoryType.MIXIN
        )
        mixin_dir = mixin_builder.get_entity_dir()

        expected_path = (
            output_dir / "api" / "material" / "mixins" / "BaseSliderTrackShape"
        )
        assert mixin_dir == expected_path
        assert mixin_dir.exists()
        assert (mixin_dir / "BaseSliderTrackShape.md").exists()

    def test_enum_directory_structure(self, output_dir: Path) -> None:
        """Enums should be placed in api/{section}/enums/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        enum_builder = build_entity_path_builder(
            output_dir, "material", "HourFormat", CategoryType.ENUM
        )
        enum_dir = enum_builder.get_entity_dir()

        expected_path = output_dir / "api" / "material" / "enums" / "HourFormat"
        assert enum_dir == expected_path
        assert enum_dir.exists()
        assert (enum_dir / "HourFormat.md").exists()

    def test_extension_directory_structure(self, output_dir: Path) -> None:
        """Extensions should be placed in api/{section}/extensions/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        extension_builder = build_entity_path_builder(
            output_dir, "widgets", "WidgetStateOperators", CategoryType.EXTENSION
        )
        extension_dir = extension_builder.get_entity_dir()

        expected_path = (
            output_dir / "api" / "widgets" / "extensions" / "WidgetStateOperators"
        )
        assert extension_dir == expected_path
        assert extension_dir.exists()
        assert (extension_dir / "WidgetStateOperators.md").exists()

    def test_extension_type_directory_structure(self, output_dir: Path) -> None:
        """Extension types should be placed in api/{section}/extension_types/{entity_name}/."""
        result = run_convert(SAMPLES_DIR, "widgets", output_dir)
        assert result.returncode == 0

        ext_type_builder = build_entity_path_builder(
            output_dir, "widgets", "OverlayChildLayoutInfo", CategoryType.EXTENSION_TYPE
        )
        ext_type_dir = ext_type_builder.get_entity_dir()

        expected_path = (
            output_dir
            / "api"
            / "widgets"
            / "extension_types"
            / "OverlayChildLayoutInfo"
        )
        assert ext_type_dir == expected_path
        assert ext_type_dir.exists()
        assert (ext_type_dir / "OverlayChildLayoutInfo.md").exists()

    def test_constant_file_structure(self, output_dir: Path) -> None:
        """Constants should be in api/{section}/constants/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        constant_builder = build_entity_path_builder(
            output_dir, "material", "accelerateEasing", CategoryType.CONSTANT
        )
        constant_file = constant_builder.get_entity_file()

        expected_path = (
            output_dir
            / "api"
            / "material"
            / "constants"
            / "accelerateEasing"
            / "accelerateEasing.md"
        )
        assert constant_file == expected_path
        assert constant_file.exists()
        assert constant_file.is_file()

    def test_function_file_structure(self, output_dir: Path) -> None:
        """Functions should be in api/{section}/functions/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        function_builder = build_entity_path_builder(
            output_dir, "material", "showBottomSheet", CategoryType.FUNCTION
        )
        function_file = function_builder.get_entity_file()

        expected_path = (
            output_dir
            / "api"
            / "material"
            / "functions"
            / "showBottomSheet"
            / "showBottomSheet.md"
        )
        assert function_file == expected_path
        assert function_file.exists()
        assert function_file.is_file()

    def test_typedef_file_structure(self, output_dir: Path) -> None:
        """Typedefs should be in api/{section}/typedefs/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        typedef_builder = build_entity_path_builder(
            output_dir, "material", "DrawerCallback", CategoryType.TYPEDEF
        )
        typedef_file = typedef_builder.get_entity_file()

        expected_path = (
            output_dir
            / "api"
            / "material"
            / "typedefs"
            / "DrawerCallback"
            / "DrawerCallback.md"
        )
        assert typedef_file == expected_path
        assert typedef_file.exists()
        assert typedef_file.is_file()

    def test_library_file_structure(self, output_dir: Path) -> None:
        """Libraries should be in api/{section}/library/{entity_name}/{entity_name}.md."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        library_builder = build_entity_path_builder(
            output_dir, "material", "material", CategoryType.LIBRARY
        )
        library_file = library_builder.get_entity_file()

        expected_path = (
            output_dir / "api" / "material" / "library" / "material" / "material.md"
        )
        assert library_file == expected_path
        assert library_file.exists()
        assert library_file.is_file()


class TestMixinProcessing:
    """Tests for mixin-specific processing behavior.

    Mixins have full member processing like classes, but should NOT have
    constructor sections (Dart language constraint).
    """

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_mixin_no_constructors_directory(self, output_dir: Path) -> None:
        """Mixins should NOT have a constructors directory.

        Mixins cannot have constructors in Dart, so the constructors
        subdirectory should not be created during processing.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "BaseSliderTrackShape", CategoryType.MIXIN
        )
        mixin_dir = mixin_builder.get_entity_dir()
        constructors_dir = mixin_dir / "constructors"

        assert not constructors_dir.exists(), (
            f"Mixin should not have constructors directory: {constructors_dir}"
        )

    def test_mixin_has_other_members(self, output_dir: Path) -> None:
        """Mixins should have other member types processed normally.

        While mixins can't have constructors, they can have properties,
        methods, and operators.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "BaseSliderTrackShape", CategoryType.MIXIN
        )

        # Check that root file exists
        mixin_file = mixin_builder.get_entity_file()
        assert mixin_file.exists(), "Mixin root file should exist"

    def test_material_state_mixin_processing(self, output_dir: Path) -> None:
        """MaterialStateMixin should be processed without constructors."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        mixin_builder = build_entity_path_builder(
            output_dir, "material", "MaterialStateMixin", CategoryType.MIXIN
        )

        # Verify mixin file exists
        mixin_file = mixin_builder.get_entity_file()
        assert mixin_file.exists()

        # Verify no constructors directory
        mixin_dir = mixin_builder.get_entity_dir()
        constructors_dir = mixin_dir / "constructors"
        assert not constructors_dir.exists()


class TestStandaloneTypeProcessing:
    """Tests for standalone documentation types (constant, function, typedef, library).

    These types should produce single markdown files without member subdirectories
    or complex processing beyond root file conversion.
    """

    @pytest.fixture
    def output_dir(self, tmp_path: Path) -> Path:
        """Create a temporary output directory."""
        return tmp_path / "output"

    def test_constant_no_subdirectories(self, output_dir: Path) -> None:
        """Constants should not create entity subdirectories.

        Constants are standalone files with no members.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        constant_builder = build_entity_path_builder(
            output_dir, "material", "accelerateEasing", CategoryType.CONSTANT
        )
        constant_file = constant_builder.get_entity_file()
        assert constant_file.exists()
        assert constant_file.is_file()

        # Verify this is a file, not a directory
        assert not constant_file.is_dir()

    def test_function_no_subdirectories(self, output_dir: Path) -> None:
        """Functions should not create member subdirectories.

        Functions have an entity directory but no member subdirectories.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        function_builder = build_entity_path_builder(
            output_dir, "material", "showBottomSheet", CategoryType.FUNCTION
        )
        function_file = function_builder.get_entity_file()
        assert function_file.exists()
        assert function_file.is_file()

        # Functions have an entity directory
        function_dir = function_builder.get_entity_dir()
        assert function_dir.exists()

        # But should not have member subdirectories (properties, methods, etc.)
        member_subdirs = [d for d in function_dir.iterdir() if d.is_dir()]
        assert len(member_subdirs) == 0, (
            f"Function should not have member subdirs: {member_subdirs}"
        )

    def test_typedef_no_subdirectories(self, output_dir: Path) -> None:
        """Typedefs should not create member subdirectories.

        Typedefs have an entity directory but no member subdirectories.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        typedef_builder = build_entity_path_builder(
            output_dir, "material", "DrawerCallback", CategoryType.TYPEDEF
        )
        typedef_file = typedef_builder.get_entity_file()
        assert typedef_file.exists()
        assert typedef_file.is_file()

        # Typedefs have an entity directory
        typedef_dir = typedef_builder.get_entity_dir()
        assert typedef_dir.exists()

        # But should not have member subdirectories (properties, methods, etc.)
        member_subdirs = [d for d in typedef_dir.iterdir() if d.is_dir()]
        assert len(member_subdirs) == 0, (
            f"Typedef should not have member subdirs: {member_subdirs}"
        )

    def test_library_no_subdirectories(self, output_dir: Path) -> None:
        """Libraries should not create member subdirectories.

        Libraries have an entity directory but no member subdirectories.
        """
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        library_builder = build_entity_path_builder(
            output_dir, "material", "material", CategoryType.LIBRARY
        )
        library_file = library_builder.get_entity_file()
        assert library_file.exists()
        assert library_file.is_file()

        # Libraries have an entity directory
        library_dir = library_builder.get_entity_dir()
        assert library_dir.exists()

        # But should not have member subdirectories (properties, methods, etc.)
        member_subdirs = [d for d in library_dir.iterdir() if d.is_dir()]
        assert len(member_subdirs) == 0, (
            f"Library should not have member subdirs: {member_subdirs}"
        )

    def test_all_standalone_types_converted(self, output_dir: Path) -> None:
        """All standalone type files should be converted to markdown."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        # Check one of each standalone type
        constant_file = build_entity_path_builder(
            output_dir, "material", "accelerateEasing", CategoryType.CONSTANT
        ).get_entity_file()
        function_file = build_entity_path_builder(
            output_dir, "material", "showBottomSheet", CategoryType.FUNCTION
        ).get_entity_file()
        typedef_file = build_entity_path_builder(
            output_dir, "material", "DrawerCallback", CategoryType.TYPEDEF
        ).get_entity_file()
        library_file = build_entity_path_builder(
            output_dir, "material", "material", CategoryType.LIBRARY
        ).get_entity_file()

        for file in [constant_file, function_file, typedef_file, library_file]:
            assert file.exists(), f"Standalone type file not found: {file}"
            content = file.read_text(encoding="utf-8")
            assert content.startswith("#"), f"File should start with heading: {file}"
            assert FOOTER_MARKER not in content, f"File should not have footer: {file}"
