# flutterdocs_mcp prompt

This file is simply a prompt to facilitate generating a full PRD for the flutterdocs_mcp server.

## Goal

Implement a Model Context Protocol (MCP) server for Flutter and Dart documentation that:
- Supports only the MCP stdio transport.
- Implements the tools and resource templates defined below.
- Responds to MCP client requests (tools and resource templates) with Flutter/Dart documentation retrieved from a sqlite3 database file with the schema defined in make_docs/DOCDB_SCHEMA.sql.

## Technology Stack

- Dart programming language and SDK for implementing the MCP server.
- The `dart_mcp` Dart package for building MCP servers.
- The `sqlite3` Dart package for retrieving Flutter/Dart documentation from a sqlite3 database file.

## Tools

The MCP server must implement the following tools.

### lookupEntity

- name: "lookupEntity"
- title: "Resolve Flutter entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) by name"
- description: "Finds Flutter entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) by identifier name. Use this when you have an entity name (e.g., ListTile, HourFormat) and need to know which library (or libraries) it belongs to. Navigation Tip: Use the returned [library, entity] values to construct resource URIs: flutter-docs://api/{library}/{entity}."
- inputSchema:
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the entity to find (e.g., 'ListTile'). Case-sensitive."
    }
  },
  "required": ["name"]
}
- outputSchema:
{
  "type": "array",
  "description": "A navigation tuple [totalMatches, resultList].",
  "prefixItems": [
    { "type": "integer", "description": "The total number of entity name matches found." },
    {
      "type": "array",
      "description": "List of up to 10 match results ([library, entity, entity category] tuples).",
      "items": {
        "type": "array",
        "prefixItems": [
          { "type": "string", "description": "Library name (e.g., 'material')." },
          { "type": "string", "description": "Entity name (e.g., 'ListTile')." },
          { "type": "string", "description": "Entity category (e.g., 'class')." }
        ],
        "description": "Construct resource URIs from these results as: flutter-docs://api/{library}/{entity}"
      }
    }
  ]
}

### lookupMember

- name: "lookupMember"
- title: "Resolve Flutter member (constructor, property, method, operator, constant, static method) by name and optional library hint."
- description: "Finds Flutter member (constructor, property, method, operator, constant, static method) by identifier name and optional library hint. Use this when you have a member name (e.g., visualDensity, addMaterialState) and need to know which entity it belongs to. The optional library name hint limits the search to that library, which is useful for common member names. Navigation Tip: Use the returned [library, entity, member] values to construct resource URIs: flutter-docs://api/{library}/{entity}/{member}."
- inputSchema:
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the member to find (e.g., 'visualDensisty'). Case-sensitive."
    },
    "libraryHint": {
      "type": "string",
      "description": "Optional: Limit search to a specific library (e.g., 'material'). Case-sensitive."
    },
  },
  "required": ["name"]
}
- outputSchema:
{
  "type": "array",
  "description": "A navigation tuple [totalMatches, resultList].",
  "prefixItems": [
    { "type": "integer", "description": "The total number of member name matches found." },
    {
      "type": "array",
      "description": "List of up to 10 match results ([library, entity, member, member category] tuples).",
      "items": {
        "type": "array",
        "prefixItems": [
          { "type": "string", "description": "Library name (e.g., 'material')." },
          { "type": "string", "description": "Entity name (e.g., 'ListTile')." },
          { "type": "string", "description": "Member name (e.g., 'visualDensity')." },
          { "type": "string", "description": "Member category (e.g., 'property')." }
        ],
        "description": "Construct resource URIs from these results as: flutter-docs://api/{library}/{entity}/{member}"
      }
    }
  ]
}

## Resource Templates

The MCP server must implement the following resource templates.

### libraryIndex

- uriTemplate: "flutter-docs://api/{library}"
- name: "libraryIndex"
- title: "Flutter library documentation index"
- description: "High-level summary of the library and all of its entities (classes, mixins, enums, extensions, extension types, typedefs, top-level functions, top-level constants). Contains embedded navigation links (resource URIs) to the detailed documentation for each entity."
- annotations: {"audience": ["user", "assistant"]}

### entityDocumentation

- uriTemplate: "flutter-docs://api/{library}/{entity}"
- name: "entityDocumentation"
- title: "Flutter entity documentation"
- description: "Detailed documentation for the Flutter entity (class, mixin, enum, extension, extension type, typedef, top-level function, top-level constant) in the specified library. Includes a summary of all its members (constructors, properties, methods, operators, constants, static methods), with embedded navigation links (resource URIs) to the detailed documentation for each member."
- annotations: {"audience": ["user", "assistant"]}

### memberDocumentation

- uriTemplate: "flutter-docs://api/{library}/{entity}/{member}"
- name: "memberDocumentation"
- title: "Flutter member documentation"
- description: "Detailed documentation for the Flutter member (constructor, property, method, operator, constant, static method) of the specified entity in the specified library. Use the reserved member name '_snippets' to retrieve code snippets for entity, if any are available."
- annotations: {"audience": ["user", "assistant"]}

## Logging

## Performance Optimizations

## dart_mcp Dart Package Usage Examples

## sqlite3 Dart Package Usage Examples

## Source Structure

## Testing and Validation
