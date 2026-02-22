# Project Overview

This project is a Model Context Protocol (MCP) server for Flutter and Dart documentation.

## Technology Stack

- **MCP Server**: Dart, the `dart_mcp` Dart package for building MCP servers, and the `sqlite3` Dart package for retrieving Flutter/Dart documentation from a sqlite3 database file.
- **Documentation Generation**: Python, the `html_to_markdown` Python package for converting Flutter/Dart documentation from HTML to markdown, and the `sqlite3` Python module for storing the converted documentation in a sqlite3 database file.

## Project Structure

- flutterdocs_mcp/: Contains the Dart-based MCP server implementation that retrieves Flutter/Dart documentation from a sqlite3 database file.
- make_docs/: Contains Python scripts for generating Flutter/Dart documentation in markdown format and storing it in a sqlite3 database file.
- prd/: Contains product requirement documents (PRDs) for the components of this project that were used to support agent-based code generation; they are not actively maintained.
