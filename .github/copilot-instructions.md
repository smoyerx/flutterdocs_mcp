# Project Overview

This project is a Model Context Protocol (MCP) server for Flutter and Dart documentation.

## Technology Stack

- **MCP Server**: Dart, the `dart_mcp` package for building MCP servers, and the `sqlite_async` package for retrieving documentation data from a sqlite3 database.
- **Documentation Generation**: Python, the `html_to_markdown` package for converting Flutter/Dart documentation from HTML to markdown, and the `sqlite3` module for storing the converted documentation in a sqlite3 database.

## Project Structure

- flutterdoc_mcp/: Contains the Dart-based MCP server implementation.
- doc_gen/: Contains Python scripts for generating Flutter/Dart documentation in markdown format and storing it in a sqlite3 database.
- prd/: Contains product requirement documents (PRDs) for the components of this project.
