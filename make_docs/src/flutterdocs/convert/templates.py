"""Template strings for generated markdown content.

This module contains template strings used to generate markdown content
for inherited members (properties, methods, operators).
"""

from flutterdocs.convert.patterns import MCP_URI_PREFIX

INHERITED_PROPERTY_TEMPLATE = f"""# {{property}} property

{{result_type}} {{property}}

{{description}}

This property is inherited from [{{some_entity}}]({MCP_URI_PREFIX}{{some_section}}/{{some_entity}}).
See further details at [{{property}}]({MCP_URI_PREFIX}{{some_section}}/{{some_entity}}/{{property}}).
"""

INHERITED_METHOD_TEMPLATE = f"""# {{method}} method

{{result_type}} {{method}}(/* See {{some_entity}} documentation for parameters */)

{{description}}

This method is inherited from [{{some_entity}}]({MCP_URI_PREFIX}{{some_section}}/{{some_entity}}).
See further details at [{{method}}]({MCP_URI_PREFIX}{{some_section}}/{{some_entity}}/{{method}}).
"""

INHERITED_OPERATOR_TEMPLATE = f"""# {{operator_symbol}} ({{operator}}) method

{{result_type}} {{operator_symbol}}(/* See {{some_entity}} documentation for parameters */)

{{description}}

This operator is inherited from [{{some_entity}}]({MCP_URI_PREFIX}{{some_section}}/{{some_entity}}).
See further details at [{{operator_symbol}}]({MCP_URI_PREFIX}{{some_section}}/{{some_entity}}/{{operator}}).
"""
