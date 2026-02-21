"""Shared test fixtures for all flutterdocs tools."""

import pytest
from pathlib import Path


@pytest.fixture
def output_dir(tmp_path: Path) -> Path:
    """Temporary output directory for any tool.

    Args:
        tmp_path: pytest's temporary directory fixture.

    Returns:
        Path to a temporary output directory.
    """
    return tmp_path / "output"
