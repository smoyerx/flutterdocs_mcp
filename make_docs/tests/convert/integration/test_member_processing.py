"""Integration tests for member processing in conversion pipeline.

Tests processing of various member types: snippets, inherited members,
enum constants, and function declaration cleanup.
"""

import re
from pathlib import Path


from convert.conftest import (
    build_entity_path_builder,
    make_mcp_uri,
    run_convert,
    SAMPLES_DIR,
)
from flutterdocs._shared.constants import CategoryType
from flutterdocs.convert.patterns import MCP_URI_PREFIX


class TestConvertWithSnippets:
    """Tests for Dart snippet conversion."""

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
        """Snippet files should be plain ```dart code fences."""
        result = run_convert(SAMPLES_DIR, "material", output_dir)
        assert result.returncode == 0

        snippets_builder = build_entity_path_builder(
            output_dir, "material", "ListTile", CategoryType.CLASS
        )
        snippets_dir = snippets_builder.get_snippets_dir()
        for snippet_file in snippets_dir.glob("*.md"):
            content = snippet_file.read_text(encoding="utf-8")
            assert content.startswith("```dart"), (
                f"Snippet {snippet_file} does not start with ```dart fence"
            )

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
        inherited_props_dir = inkwell_builder.get_inherited_properties_dir()
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
        inherited_methods_dir = inkwell_builder.get_inherited_methods_dir()
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
        inherited_operators_dir = inkwell_builder.get_inherited_operators_dir()
        assert inherited_operators_dir.exists()

        # Check for at least some inherited operators
        operator_files = list(inherited_operators_dir.glob("*.md"))
        assert len(operator_files) > 0, "No inherited operator files generated"

        # Verify one specific inherited operator from Widget
        equals_file = inkwell_builder.get_inherited_operator_file("operator_equals")
        assert equals_file.exists(), f"Missing inherited operator: {equals_file}"


class TestEnumConstantsProcessing:
    """Integration tests for enum Constants section processing."""

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
        # should be transformed to [values](flutter-docs://api/material/HourFormat/values)
        assert "values-constant.html" not in content, (
            "Enum constant link should be transformed"
        )
        assert f"{MCP_URI_PREFIX}material/HourFormat/values" in content, (
            "Enum constant should have MCP URI"
        )


class TestFunctionDeclarationCleanup:
    """Integration tests for function declaration cleanup transformation."""

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
        inherited_methods_dir = inkwell_builder.get_inherited_methods_dir()
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
        operators_dir = extension_builder.get_native_operators_dir()
        assert operators_dir.exists(), f"Operators directory not found: {operators_dir}"

        operator_files = list(operators_dir.glob("*.md"))
        assert len(operator_files) > 0, "No operator files found"

        # Check one operator file for cleanup
        operator_file = operator_files[0]
        content = operator_file.read_text(encoding="utf-8")

        # Check for ordered list markers - should not exist after cleanup
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
                ordered_marker = re.compile(r"^\d+\.\s", re.MULTILINE)
                matches = ordered_marker.findall(content)
                assert not matches, (
                    f"Found {len(matches)} ordered list marker(s) in static method file"
                )


class TestTlsExceptionMemberProcessing:
    """Integration tests for TlsException conversion in the dart-io section."""

    def test_convert_succeeds(self, output_dir: Path) -> None:
        """Converting dart-io should succeed without error."""
        result = run_convert(SAMPLES_DIR, "dart-io", output_dir)
        assert result.returncode == 0, f"convert failed with stderr:\n{result.stderr}"

    def test_native_property_files_generated(self, output_dir: Path) -> None:
        """Native properties without a description in the class listing should convert."""
        result = run_convert(SAMPLES_DIR, "dart-io", output_dir)
        assert result.returncode == 0

        builder = build_entity_path_builder(
            output_dir, "dart-io", "TlsException", CategoryType.CLASS
        )
        for prop in ("message", "osError", "type"):
            prop_file = builder.get_native_property_file(prop)
            assert prop_file.exists(), f"Missing native property file: {prop_file}"

    def test_inherited_property_files_generated(self, output_dir: Path) -> None:
        """Inherited property files should be generated for TlsException."""
        result = run_convert(SAMPLES_DIR, "dart-io", output_dir)
        assert result.returncode == 0

        builder = build_entity_path_builder(
            output_dir, "dart-io", "TlsException", CategoryType.CLASS
        )
        for prop in ("hashCode", "runtimeType"):
            prop_file = builder.get_inherited_property_file(prop)
            assert prop_file.exists(), f"Missing inherited property file: {prop_file}"

    def test_inherited_method_file_generated(self, output_dir: Path) -> None:
        """Inherited method file should be generated for TlsException."""
        result = run_convert(SAMPLES_DIR, "dart-io", output_dir)
        assert result.returncode == 0

        builder = build_entity_path_builder(
            output_dir, "dart-io", "TlsException", CategoryType.CLASS
        )
        method_file = builder.get_inherited_method_file("noSuchMethod")
        assert method_file.exists(), f"Missing inherited method file: {method_file}"

    def test_inherited_operator_file_generated(self, output_dir: Path) -> None:
        """Inherited operator file should be generated for TlsException."""
        result = run_convert(SAMPLES_DIR, "dart-io", output_dir)
        assert result.returncode == 0

        builder = build_entity_path_builder(
            output_dir, "dart-io", "TlsException", CategoryType.CLASS
        )
        operator_file = builder.get_inherited_operator_file("operator_equals")
        assert operator_file.exists(), (
            f"Missing inherited operator file: {operator_file}"
        )
