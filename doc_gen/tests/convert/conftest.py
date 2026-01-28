"""Convert-specific test fixtures and helpers."""

import shutil
import subprocess
from pathlib import Path

import pytest

from flutterdoc_gen.convert.paths import (
    get_input_flutter_dir,
    get_input_section_dir,
)


# Path to convert sample documentation files
SAMPLES_DIR = Path(__file__).parent / "integration" / "samples"


@pytest.fixture
def samples_dir() -> Path:
    """Path to convert sample documentation files.

    Returns:
        Path to the samples directory containing test documentation.
    """
    return SAMPLES_DIR


def run_convert(
    doc_dir: Path,
    section: str,
    output_dir: Path,
    verbose: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run the convert command with the given arguments.

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
        "convert",
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
    flutter_dir = get_input_flutter_dir(SAMPLES_DIR)
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
    section_dir = get_input_section_dir(SAMPLES_DIR, section)
    if not section_dir.exists():
        return []

    class_names = []
    for f in section_dir.glob("*-class.html"):
        class_name = f.stem.replace("-class", "")
        class_names.append(class_name)
    return sorted(class_names)
