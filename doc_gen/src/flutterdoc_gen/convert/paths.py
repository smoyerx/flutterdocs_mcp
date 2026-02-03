"""Path construction utilities for the convert tool.

This module provides PathBuilder, an immutable dataclass that centralizes
all path construction logic for input and output files.
"""

from dataclasses import dataclass, field
from pathlib import Path
from flutterdoc_gen.convert.constants import CategoryType, MemberType


@dataclass(frozen=True)
class PathBuilder:
    """Immutable path builder for entity documentation processing.

    Captures entity context (section, name, type, directories) and provides
    methods for constructing all input and output paths. Maintains separation
    between logical names (CategoryType, MemberType) and filesystem structure.

    All filesystem path decisions are centralized in the generic methods:
    - _compute_entity_dir: Maps CategoryType to output subdirectories
    - _get_member_dir: Maps MemberType to member subdirectories
    - _get_member_file: Handles native vs inherited file naming

    Convenience aliases (get_properties_dir, get_native_method_file, etc.)
    wrap the generic methods for readability at call sites.
    """

    section: str
    entity_name: str
    entity_type: CategoryType
    doc_dir: Path
    output_dir: Path
    _entity_dir: Path = field(init=False)

    def __post_init__(self):
        """Pre-compute entity directory for efficiency."""
        object.__setattr__(self, "_entity_dir", self._compute_entity_dir())

    # --- Generic Implementation Methods (Documented) ---

    def _compute_entity_dir(self) -> Path:
        """Compute entity output directory from CategoryType.

        Maps logical CategoryType enum values to filesystem subdirectories.
        This is the single source of truth for output directory structure.

        Returns:
            Path like output_dir/api/{section}/{type_subdir}/{entity_name}
        """
        match self.entity_type:
            case CategoryType.CLASS:
                subdir = "classes"
            case CategoryType.MIXIN:
                subdir = "mixins"
            case CategoryType.ENUM:
                subdir = "enums"
            case CategoryType.CONSTANT:
                subdir = "constants"
            case CategoryType.LIBRARY:
                subdir = "libraries"
            case CategoryType.EXTENSION_TYPE:
                subdir = "extension_types"
            case CategoryType.EXTENSION:
                subdir = "extensions"
            case CategoryType.FUNCTION:
                subdir = "functions"
            case CategoryType.TYPEDEF:
                subdir = "typedefs"
            case _:
                subdir = "entities"

        return self.output_dir / "api" / self.section / subdir / self.entity_name

    def _get_member_dir(self, member_type: MemberType, inherited: bool) -> Path:
        """Get member type output directory.

        Maps MemberType to subdirectory structure. Properties, methods, and
        operators have native/inherited splits; constructors, statics, and
        snippets do not.

        Args:
            member_type: The type of member
            inherited: True for inherited subdirectory, False for native

        Returns:
            Path like entity_dir/properties/native or entity_dir/constructors
        """
        # Map enum to filesystem directory name
        match member_type:
            case MemberType.CONSTRUCTORS:
                base = "constructors"
            case MemberType.PROPERTIES:
                base = "properties"
            case MemberType.METHODS:
                base = "methods"
            case MemberType.OPERATORS:
                base = "operators"
            case MemberType.STATICS:
                base = "statics"
            case MemberType.SNIPPETS:
                base = "snippets"

        # Add inherited/native split for relevant types
        if member_type in (
            MemberType.PROPERTIES,
            MemberType.METHODS,
            MemberType.OPERATORS,
        ):
            subdir = f"{base}/{'inherited' if inherited else 'native'}"
        else:
            subdir = base

        return self._entity_dir / subdir

    def _get_member_file(
        self,
        member_type: MemberType,
        member_name: str,
        inherited: bool,
        source_section: str | None = None,
        source_entity: str | None = None,
    ) -> Path:
        """Get member output file path.

        Handles both native and inherited member file naming conventions:
        - Native: {member_name}.md
        - Inherited: {section}___{entity}___{member_name}.md

        Args:
            member_type: The type of member
            member_name: The member name
            inherited: True for inherited member file format
            source_section: Required for inherited - section defining the member
            source_entity: Required for inherited - entity defining the member

        Returns:
            Path to member markdown file
        """
        member_dir = self._get_member_dir(member_type, inherited)

        if inherited:
            filename = f"{source_section}___{source_entity}___{member_name}.md"
        else:
            filename = f"{member_name}.md"

        return member_dir / filename

    # --- Output Path Convenience Aliases ---

    def get_api_root_dir(self) -> Path:
        return self.output_dir / "api"

    def get_api_section_dir(self) -> Path:
        return self.output_dir / "api" / self.section

    def get_entity_dir(self) -> Path:
        return self._entity_dir

    def get_entity_file(self) -> Path:
        return self._entity_dir / f"{self.entity_name}.md"

    def get_constructors_dir(self) -> Path:
        return self._get_member_dir(MemberType.CONSTRUCTORS, inherited=False)

    def get_properties_dir(self, inherited: bool = False) -> Path:
        return self._get_member_dir(MemberType.PROPERTIES, inherited)

    def get_methods_dir(self, inherited: bool = False) -> Path:
        return self._get_member_dir(MemberType.METHODS, inherited)

    def get_operators_dir(self, inherited: bool = False) -> Path:
        return self._get_member_dir(MemberType.OPERATORS, inherited)

    def get_statics_dir(self) -> Path:
        return self._get_member_dir(MemberType.STATICS, inherited=False)

    def get_snippets_dir(self) -> Path:
        return self._get_member_dir(MemberType.SNIPPETS, inherited=False)

    def get_constructor_file(self, member_name: str) -> Path:
        return self._get_member_file(
            MemberType.CONSTRUCTORS, member_name, inherited=False
        )

    def get_native_property_file(self, member_name: str) -> Path:
        return self._get_member_file(
            MemberType.PROPERTIES, member_name, inherited=False
        )

    def get_native_method_file(self, member_name: str) -> Path:
        return self._get_member_file(MemberType.METHODS, member_name, inherited=False)

    def get_native_operator_file(self, member_name: str) -> Path:
        return self._get_member_file(MemberType.OPERATORS, member_name, inherited=False)

    def get_static_file(self, member_name: str) -> Path:
        return self._get_member_file(MemberType.STATICS, member_name, inherited=False)

    def get_snippet_file(self, short_name: str) -> Path:
        return self._get_member_file(MemberType.SNIPPETS, short_name, inherited=False)

    def get_inherited_property_file(
        self, source_section: str, source_entity: str, member_name: str
    ) -> Path:
        return self._get_member_file(
            MemberType.PROPERTIES,
            member_name,
            inherited=True,
            source_section=source_section,
            source_entity=source_entity,
        )

    def get_inherited_method_file(
        self, source_section: str, source_entity: str, member_name: str
    ) -> Path:
        return self._get_member_file(
            MemberType.METHODS,
            member_name,
            inherited=True,
            source_section=source_section,
            source_entity=source_entity,
        )

    def get_inherited_operator_file(
        self, source_section: str, source_entity: str, member_name: str
    ) -> Path:
        return self._get_member_file(
            MemberType.OPERATORS,
            member_name,
            inherited=True,
            source_section=source_section,
            source_entity=source_entity,
        )

    # --- Input Path Convenience Aliases ---

    def get_input_flutter_dir(self) -> Path:
        return self.doc_dir / "flutter"

    def get_input_section_dir(self) -> Path:
        return self.doc_dir / "flutter" / self.section

    def get_input_entity_file(self) -> Path:
        match self.entity_type:
            case CategoryType.CLASS:
                suffix = "-class"
            case CategoryType.MIXIN:
                suffix = "-mixin"
            case CategoryType.ENUM:
                suffix = ""
            case CategoryType.CONSTANT:
                suffix = "-constant"
            case CategoryType.LIBRARY:
                suffix = "-library"
            case CategoryType.EXTENSION_TYPE:
                suffix = "-extension-type"
            case CategoryType.EXTENSION:
                suffix = ""
            case CategoryType.FUNCTION:
                suffix = ""
            case CategoryType.TYPEDEF:
                suffix = ""
            case _:
                suffix = ""

        return self.get_input_section_dir() / f"{self.entity_name}{suffix}.html"

    def get_input_member_file(self, member_name: str) -> Path:
        return self.get_input_section_dir() / self.entity_name / f"{member_name}.html"

    def get_input_snippets_dir(self) -> Path:
        return self.doc_dir / "snippets"


# --- Standalone Helper Functions ---


def ensure_dir_exists(dir_path: Path) -> Path:
    """Create directory if it doesn't exist.

    Args:
        dir_path: The directory path to create.

    Returns:
        The same directory path (for chaining).
    """
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path
