---
description: "Python coding standards and best practices"
name: python_coding
applyTo: "**/*.py"
---

# Python Coding Standards

Instructions for developing Python code in this project.

## Code Style and Structure

- **Coding Style**: ALWAYS adhere to [PEP 8](https://peps.python.org/pep-0008/) style guide
- **Type Annotations**: ALWAYS use type hints per [PEP 484](https://peps.python.org/pep-0484/)
- **Docstrings**: Document all public modules, functions, classes, and methods per [PEP 257](https://peps.python.org/pep-0257/)
- **Imports**: Group in order: standard library, third-party, local
- **Error Handling**: Use specific exceptions, avoid bare `except:` clauses

## General Best Practices

- Write clear, readable code with meaningful variable and function names
- Never hardcode secrets or credentials; use environment variables

## Testing

- Write tests using the `pytest` framework

## Process Workflow

When completing a Python coding task, run the following in the Python project root (e.g., `doc_gen/`):
1. Run `uvx ruff check --fix` to lint the code. If any lint errors were not auto-fixed:
   - Fix each lint error
   - Run `uvx ruff check --fix` again
   - Repeat until clean
2. Run `uvx ruff format` to auto-format the code
3. Run `uv run pytest` to ensure all tests pass. If any tests fail:
   - Fix each test failure
   - Run `uv run pytest` again
   - Repeat until all tests pass
4. Only mark the coding task as complete when all commands run without errors
