"""Template strings for generated markdown content.

This module contains template strings used to generate markdown content
for inherited members (properties, methods, operators).
"""

INHERITED_PROPERTY_TEMPLATE = """# {property} property

{result_type} {property}

{description}

This property is inherited from [{some_class}](mcp://flutter/api/{some_section}/{some_class}).
See further details at [{property}](mcp://flutter/api/{some_section}/{some_class}/{property}).
"""

INHERITED_METHOD_TEMPLATE = """# {method} method

{result_type} {method}(/* See {some_class} documentation for parameters */)

{description}

This method is inherited from [{some_class}](mcp://flutter/api/{some_section}/{some_class}).
See further details at [{method}](mcp://flutter/api/{some_section}/{some_class}/{method}).
"""

INHERITED_OPERATOR_TEMPLATE = """# {operator_symbol} ({operator}) method

{result_type} {operator_symbol}(/* See {some_class} documentation for parameters */)

{description}

This operator is inherited from [{some_class}](mcp://flutter/api/{some_section}/{some_class}).
See further details at [{operator_symbol}](mcp://flutter/api/{some_section}/{some_class}/{operator}).
"""
