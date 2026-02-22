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

## Resource Templates

## Performance Optimizations

## dart_mcp Dart Package Usage Examples

## sqlite3 Dart Package Usage Examples

## Testing and Validation

