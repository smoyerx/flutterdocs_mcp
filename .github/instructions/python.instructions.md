---
description: "doc_gen script instructions"
name: doc_gen
applyTo: "doc_gen/**/*.py"
---

# GitHub Copilot Instructions for Python Scripts in doc_gen Directory

Instructions for generating and managing Python scripts for converting Flutter/Dart documentation to Markdown format suitable for an MCP server.

## Python Script Management with uv

- **Use `uv` for script management**: All Python scripts in the `doc_gen` directory must be executed using [`uv`](https://github.com/astral-sh/uv) via `uv run`.
- **Inline dependencies**: Specify dependencies inline at the top of each script per [PEP 723](https://peps.python.org/pep-0723/). Do not maintain a `requirements.txt` file.
- **Manage dependencies with uv commands**: To add or remove inline dependencies, use `uv add --script script.py <dependency>` or `uv remove --script script.py <dependency>`. Do not edit inline dependencies directly.
- **No explicit virtual environments**: Do not use or require `venv` or `virtualenv`. Dependency isolation and management are handled by `uv`.
- **Script execution**: Always run scripts with `uv run script.py` to ensure dependencies are resolved and installed automatically.

## Python Tool Execution with uv

- **Use `uvx` to run tools**: All Python-based tools for linting, formatting, and testing must be executed using `uvx`, e.g., `uvx ruff .` for linting.

## General Python Best Practices

- **Follow PEP 8**: Adhere to the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code, including naming conventions, indentation, whitespace, and line length.
- **Type Annotations**: Use type hints as described in [PEP 484](https://peps.python.org/pep-0484/) to improve code clarity and enable better tooling support.
- **Docstrings**: Document all public modules, functions, classes, and methods using docstrings per [PEP 257](https://peps.python.org/pep-0257/).
- **Imports**: Group imports in the following order: standard library, third-party, local application/library. Use absolute imports where possible.
- **Error Handling**: Use exceptions for error handling. Catch specific exceptions and avoid bare `except:` clauses.
- **Testing**: Write tests for your code using the `pytest` framework.
- **Readability**: Write clear, readable code. Use meaningful variable and function names.
- **Version Control**: Commit code frequently with clear, descriptive messages.
- **Security**: Avoid hardcoding secrets or credentials in code. Use environment variables or configuration files.
- **Linting and Formatting**: Use [`ruff`](https://docs.astral.sh/ruff/) for all linting and code formatting tasks. Do not use other tools such as `flake8`, `pylint`, `black`, or `autopep8`.
