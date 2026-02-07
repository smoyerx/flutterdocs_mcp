"""PathBuilder centralizes all path construction for documentation workflows.

Shared across multiple flutterdoc_gen tools (convert, load) to ensure consistent
path construction for reading/writing documentation files.

- With only section/doc_dir/output_dir, it builds directory-level paths (e.g., API root,
  section directories, input roots).
- With entity_name and entity_type, it also builds entity/member-specific paths (e.g.,
  class directories, member files).

All filesystem path logic is centralized in:
- _compute_entity_dir: Maps CategoryType to output subdirectories
- _get_member_dir: Maps MemberType to member subdirectories
- _get_member_file: Handles native vs inherited file naming

Convenience aliases (get_properties_dir, get_native_method_file, etc.) wrap the generic
methods for readability at call sites.
"""

from dataclasses import dataclass, field
from pathlib import Path
from flutterdoc_gen._shared.constants import CategoryType, MemberType


@dataclass(frozen=True)
class PathBuilder:
    """
    Immutable builder for documentation paths.

    - Directory-level methods require only section/output_dir.
    - Entity/member methods require both entity_name and entity_type.
    - Input methods (get_input_*) require doc_dir.
    """

    section: str
    output_dir: Path
    doc_dir: Path | None = None
    entity_name: str | None = None
    entity_type: CategoryType | None = None
    _entity_dir: Path | None = field(init=False, default=None)

    def __post_init__(self):
        """Validate entity context and pre-compute entity directory.

        Raises:
            ValueError: If only one of entity_name or entity_type is provided.
        """
        # Validate that both or neither entity fields are provided
        has_name = self.entity_name is not None
        has_type = self.entity_type is not None

        if has_name != has_type:
            raise ValueError(
                "entity_name and entity_type must both be provided or both be None. "
                f"Got entity_name={self.entity_name!r}, entity_type={self.entity_type!r}"
            )

        # Pre-compute entity directory if entity context provided
        if has_name and has_type:
            object.__setattr__(self, "_entity_dir", self._compute_entity_dir())

    def _require_entity_context(self) -> None:
        """Raise error if entity context is missing.

        Raises:
            ValueError: If entity_name or entity_type is None.
        """
        if self.entity_name is None or self.entity_type is None:
            raise ValueError(
                "This operation requires entity context (entity_name and entity_type), "
                "but PathBuilder was created without entity context."
            )

    def _require_doc_dir(self) -> None:
        """Raise error if doc_dir is missing.

        Raises:
            ValueError: If doc_dir is None.
        """
        if self.doc_dir is None:
            raise ValueError(
                "This operation requires doc_dir (input documentation directory), "
                "but PathBuilder was created without doc_dir."
            )

    # --- Generic Implementation Methods (Documented) ---

    @staticmethod
    def _get_category_subdir(category_type: CategoryType) -> str:
        """Map CategoryType to filesystem subdirectory name.

        Single source of truth for category structure mapping.

        Args:
            category_type: The category type to map.

        Returns:
            Subdirectory name (e.g., "classes", "mixins", "enums").
        """
        match category_type:
            case CategoryType.CLASS:
                return "classes"
            case CategoryType.MIXIN:
                return "mixins"
            case CategoryType.ENUM:
                return "enums"
            case CategoryType.CONSTANT:
                return "constants"
            case CategoryType.LIBRARY:
                return "library"
            case CategoryType.EXTENSION_TYPE:
                return "extension_types"
            case CategoryType.EXTENSION:
                return "extensions"
            case CategoryType.FUNCTION:
                return "functions"
            case CategoryType.TYPEDEF:
                return "typedefs"
            case _:
                return "entities"

    def _compute_entity_dir(self) -> Path:
        """Compute entity output directory from CategoryType.

        Maps logical CategoryType enum values to filesystem subdirectories.
        This is the single source of truth for output directory structure.

        Returns:
            Path like output_dir/api/{section}/{type_subdir}/{entity_name}
        """
        self._require_entity_context()
        assert self.entity_name is not None  # Type hint for mypy / Pylance
        assert self.entity_type is not None  # Type hint for mypy / Pylance
        subdir = PathBuilder._get_category_subdir(self.entity_type)
        return self.output_dir / "api" / self.section / subdir / self.entity_name

    def _get_member_dir(self, member_type: MemberType, inherited: bool) -> Path:
        """Get member type output directory.

        Maps MemberType to subdirectory structure. Properties, methods, and
        operators have native/inherited splits; constructors, constants, statics,
        and snippets do not.

        Args:
            member_type: The type of member
            inherited: True for inherited subdirectory, False for native

        Returns:
            Path like entity_dir/properties/native or entity_dir/constructors
        """
        self._require_entity_context()
        assert self._entity_dir is not None  # Type hint for mypy / Pylance
        # Map enum to filesystem directory name
        match member_type:
            case MemberType.CONSTRUCTORS:
                base = "constructors"
            case MemberType.CONSTANTS:
                base = "constants"
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
    ) -> Path:
        """Get member output file path.

        Handles both native and inherited member output file path naming conventions.

        Args:
            member_type: The type of member
            member_name: The member name
            inherited: True for inherited member file format

        Returns:
            Path to member markdown file
        """
        self._require_entity_context()
        member_dir = self._get_member_dir(member_type, inherited)

        return member_dir / f"{member_name}.md"

    # --- Output Path Convenience Aliases ---

    def get_api_root_dir(self) -> Path:
        return self.output_dir / "api"

    def get_api_section_dir(self) -> Path:
        return self.output_dir / "api" / self.section

    def get_entity_dir(self) -> Path:
        self._require_entity_context()
        assert self._entity_dir is not None  # Type hint for mypy / Pylance
        return self._entity_dir

    def get_entity_file(self) -> Path:
        self._require_entity_context()
        assert self._entity_dir is not None and self.entity_name is not None
        return self._entity_dir / f"{self.entity_name}.md"

    def get_constructors_dir(self) -> Path:
        return self._get_member_dir(MemberType.CONSTRUCTORS, inherited=False)

    def get_constants_dir(self) -> Path:
        return self._get_member_dir(MemberType.CONSTANTS, inherited=False)

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

    def get_constant_file(self, member_name: str) -> Path:
        return self._get_member_file(MemberType.CONSTANTS, member_name, inherited=False)

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

    def get_inherited_property_file(self, member_name: str) -> Path:
        return self._get_member_file(MemberType.PROPERTIES, member_name, inherited=True)

    def get_inherited_method_file(self, member_name: str) -> Path:
        return self._get_member_file(MemberType.METHODS, member_name, inherited=True)

    def get_inherited_operator_file(self, member_name: str) -> Path:
        return self._get_member_file(MemberType.OPERATORS, member_name, inherited=True)

    # --- Input Path Convenience Aliases ---

    def get_input_flutter_dir(self) -> Path:
        self._require_doc_dir()
        assert self.doc_dir is not None  # Type hint for mypy / Pylance
        return self.doc_dir / "flutter"

    def get_input_section_dir(self) -> Path:
        self._require_doc_dir()
        assert self.doc_dir is not None  # Type hint for mypy / Pylance
        return self.doc_dir / "flutter" / self.section

    def get_input_entity_file(self) -> Path:
        self._require_entity_context()
        # Special case: library files are always named index.html
        if self.entity_type == CategoryType.LIBRARY:
            return self.get_input_section_dir() / "index.html"

        match self.entity_type:
            case CategoryType.CLASS:
                suffix = "-class"
            case CategoryType.MIXIN:
                suffix = "-mixin"
            case CategoryType.ENUM:
                suffix = ""
            case CategoryType.CONSTANT:
                suffix = "-constant"
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
        self._require_entity_context()
        assert self.entity_name is not None
        return self.get_input_section_dir() / self.entity_name / f"{member_name}.html"

    def get_input_constant_file(self, member_name: str) -> Path:
        """Get input path for enum constant HTML file.

        Enum constants have a -constant.html suffix, unlike regular members.
        E.g., material/HourFormat/values-constant.html

        Args:
            member_name: The constant name (e.g., "values").

        Returns:
            Path like doc_dir/flutter/section/entity/member-constant.html
        """
        self._require_entity_context()
        assert self.entity_name is not None
        return (
            self.get_input_section_dir()
            / self.entity_name
            / f"{member_name}-constant.html"
        )

    def get_input_snippets_dir(self) -> Path:
        self._require_doc_dir()
        assert self.doc_dir is not None  # Type hint for mypy / Pylance
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


def list_entity_names(
    base_dir: Path, section: str, category_type: CategoryType
) -> list[str]:
    """List all entity names for a category type.

    Discovers entities by listing directories in the output category directory.
    Returns empty list if directory doesn't exist. Useful for discovering
    what entities exist without needing to create a PathBuilder instance.

    Args:
        base_dir: Output directory containing api/ subdirectory (convert.py's output_dir).
        section: Documentation section name (e.g., "material", "widgets").
        category_type: The category type to list entities for.

    Returns:
        Sorted list of entity names (directory names) for the category.
    """
    category_subdir = PathBuilder._get_category_subdir(category_type)
    category_dir = base_dir / "api" / section / category_subdir
    if not category_dir.exists():
        return []
    return sorted([d.name for d in category_dir.iterdir() if d.is_dir()])
