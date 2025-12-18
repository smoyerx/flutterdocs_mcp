---
description: "Python coding standards and best practices"
name: python_coding
applyTo: "**/*.py"
---

# Python Coding Standards

Instructions for developing Python single-file scripts and multi-file applications.

## Code Style and Structure

- **Coding Style**: Adhere to [PEP 8](https://peps.python.org/pep-0008/) style guide
- **Type Annotations**: Use type hints per [PEP 484](https://peps.python.org/pep-0484/)
- **Docstrings**: Document all public modules, functions, classes, and methods per [PEP 257](https://peps.python.org/pep-0257/)
- **Imports**: Group in order: standard library, third-party, local. Use absolute imports
- **Error Handling**: Use specific exceptions, avoid bare `except:` clauses

## Dependencies

- **Single-file scripts**: Include [PEP 723](https://peps.python.org/pep-0723/) inline script metadata at the top of the file
- **Multi-file applications**: Use `pyproject.toml` for dependency management

## Testing

- Write tests using `pytest` framework
- Structure tests in parallel directory structure to source code

## General Best Practices

- Write clear, readable code with meaningful variable and function names
- Use `ruff` for linting and formatting
- Never hardcode secrets or credentials; use environment variables
