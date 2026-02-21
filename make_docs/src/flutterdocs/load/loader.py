"""Entity and member loading logic for load.py.

Handles reading markdown files and persisting entity/member data to the
database using helpers from db.py. Analogous to rootdocs.py and processors.py
in the convert module.
"""

import sqlite3
from pathlib import Path

from flutterdocs._shared.constants import MemberType
from flutterdocs._shared.paths import PathBuilder
from flutterdocs.load.db import (
    get_entity_type_id,
    get_member_type_id,
    get_or_insert_identifier,
    upsert_entity,
    upsert_member,
)

# Mapping of (getter_method_name, MemberType) for all member directories.
# Each entry is (method_name_on_builder, member_type).
_MEMBER_DIR_SPECS: list[tuple[str, MemberType]] = [
    ("get_constructors_dir", MemberType.CONSTRUCTOR),
    ("get_constants_dir", MemberType.CONSTANT),
    ("get_native_properties_dir", MemberType.PROPERTY),
    ("get_inherited_properties_dir", MemberType.PROPERTY),
    ("get_native_methods_dir", MemberType.METHOD),
    ("get_inherited_methods_dir", MemberType.METHOD),
    ("get_native_operators_dir", MemberType.OPERATOR),
    ("get_inherited_operators_dir", MemberType.OPERATOR),
    ("get_statics_dir", MemberType.STATIC),
]


def collect_snippets(builder: PathBuilder) -> str | None:
    """Collect and concatenate snippet markdown for an entity.

    Globs all *.md files from the snippets directory, sorts alphabetically
    by filename, and joins their contents with two blank lines between each.

    Args:
        builder: PathBuilder configured for the entity.

    Returns:
        Concatenated snippet markdown string, or None if no snippets found.
    """
    snippets_dir = builder.get_snippets_dir()
    if not snippets_dir.exists():
        return None
    snippet_files = sorted(snippets_dir.glob("*.md"), key=lambda p: p.name)
    if not snippet_files:
        return None
    return "\n\n".join(f.read_text() for f in snippet_files)


def collect_members(
    builder: PathBuilder,
) -> list[tuple[str, MemberType, Path]]:
    """Collect all member files for an entity.

    Iterates all member directories (constructors, constants, properties,
    methods, operators, statics — both native and inherited). Silently skips
    directories that do not exist.

    Args:
        builder: PathBuilder configured for the entity.

    Returns:
        List of (member_name_stem, MemberType, file_path) tuples, one per
        member file found. The list is in directory-iteration order (no
        guaranteed additional sort beyond directory glob ordering).
    """
    members: list[tuple[str, MemberType, Path]] = []
    for method_name, member_type in _MEMBER_DIR_SPECS:
        member_dir: Path = getattr(builder, method_name)()
        if not member_dir.exists():
            continue
        for md_file in member_dir.glob("*.md"):
            members.append((md_file.stem, member_type, md_file))
    return members


def load_entity(
    conn: sqlite3.Connection,
    builder: PathBuilder,
    library_id: int,
    entity_name: str,
    category_type_str: str,
) -> int:
    """Load a single entity and all its members into the database.

    Reads entity root file, collects snippets, collects member files,
    then writes everything in a single transaction (Transaction 3).

    Args:
        conn: Open sqlite3 connection.
        builder: PathBuilder configured for the entity.
        library_id: Foreign key to the library row for this section.
        entity_name: Name of the entity (used as identifier).
        category_type_str: String value of the CategoryType (e.g., "class").

    Returns:
        Number of member files loaded.
    """
    entity_file = builder.get_entity_file()
    content_markdown = entity_file.read_text()
    snippet_markdown = collect_snippets(builder)
    members = collect_members(builder)

    entity_type_id = get_entity_type_id(conn, category_type_str)

    with conn:
        identifier_id = get_or_insert_identifier(conn, entity_name)
        entity_id = upsert_entity(
            conn,
            library_id=library_id,
            identifier_id=identifier_id,
            entity_type_id=entity_type_id,
            content_markdown=content_markdown,
            snippet_markdown=snippet_markdown,
        )
        for member_name, member_type, member_file in members:
            member_markdown = member_file.read_text()
            member_type_id = get_member_type_id(conn, str(member_type))
            member_identifier_id = get_or_insert_identifier(conn, member_name)
            upsert_member(
                conn,
                entity_id=entity_id,
                identifier_id=member_identifier_id,
                member_type_id=member_type_id,
                content_markdown=member_markdown,
            )

    return len(members)
