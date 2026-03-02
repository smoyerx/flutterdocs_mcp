# Project Overview

This project is a Model Context Protocol (MCP) server for Flutter and Dart documentation.

## Technology Stack

- **MCP Server**: Dart, the `dart_mcp` Dart package for building MCP servers, and the `sqlite3` Dart package for retrieving Flutter/Dart documentation from a sqlite3 database file.
- **Documentation Generation**: Python, the `html_to_markdown` Python package for converting Flutter/Dart documentation from HTML to markdown, and the `sqlite3` Python module for storing the converted documentation in a sqlite3 database file.

## Project Structure

The project repository is organized as a Dart CLI project following the pub package layout conventions.

In addition to the standard Dart project files and directories, the repository includes the following top-level directories:
- make_docs/: Python scripts `convert.py` and `load.py` for generating Flutter/Dart documentation in markdown format and storing it in a sqlite3 database file, respectively. Managed with `uv`.
- prd/: Product requirement documents (PRDs) for the components of this project that were used to support agent-based code generation; they are **not** actively maintained as project components evolve.

## Instructions File Maintenance

`.github/instructions/convert.instructions.md` and `.github/instructions/load.instructions.md` document the CLI, source structure, and test structure for `convert.py` and `load.py` respectively. Any change to those tools or their shared code (`_shared/`) that renders either instructions file inaccurate or incomplete must include a corresponding update to the affected instructions file(s) in the same change set.
