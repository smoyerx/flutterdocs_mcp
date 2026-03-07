"""Unit tests for _shared/version.py constants."""

from flutterdocs._shared.version import DB_VERSION, VERSION


class TestVersion:
    """Tests for the consistency of version constants."""

    def test_db_version_encodes_version_string(self) -> None:
        """DB_VERSION must be the integer encoding of VERSION.

        Encoding: major * 1_000_000 + minor * 1_000 + patch.
        """
        major, minor, patch = (int(p) for p in VERSION.split("."))
        expected = major * 1_000_000 + minor * 1_000 + patch
        assert DB_VERSION == expected
