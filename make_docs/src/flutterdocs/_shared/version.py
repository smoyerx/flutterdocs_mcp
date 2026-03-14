"""Version constants for the flutterdocs tools.

``DB_VERSION`` is the integer encoding of ``VERSION`` as
``major * 1_000_000 + minor * 1_000 + patch``.

Both constants are maintained in sync by ``dart run tool/set_version.dart``
— do not edit manually.
"""

VERSION = "0.1.1"
DB_VERSION = 1001
