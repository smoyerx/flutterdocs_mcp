---
description: "Python development instructions"
name: python_dev
applyTo: "**/*.py"
---

# Instructions for Python Coding and Development

Instructions for developing and managing Python single-file scripts and multi-file applications.

All Python scripts and applications are managed using [`uv`](https://github.com/astral-sh/uv). Do not use or require `venv` or `virtualenv`. `uv` automatically manages isolated environments per-project and caches them globally for efficiency.

## Choosing Between Single-File Scripts and Multi-File Applications

- **Use single-file scripts for**:
  - Standalone utilities, tools, or data processing tasks
  - Code that doesn't need to be imported by other modules

- **Use multi-file applications for**:
  - Projects with multiple modules or packages
  - Code that needs to be installed or distributed
  - Code that will be imported and reused across the repository

## Python Single-File Script Management with uv

These instructions apply only to single-file Python scripts implemented in this repository.
- **Script execution**: Always run scripts with `uv run path/to/script.py` to ensure dependencies are resolved and installed automatically.
- **Inline dependencies**: Specify dependencies inline at the top of each script per [PEP 723](https://peps.python.org/pep-0723/). Do not maintain a `requirements.txt` file.
- **Add or remove inline dependencies**: To add or remove inline dependencies, use `uv add --script path/to/script.py <packages>` or `uv remove --script path/to/script.py <packages>`. When adding dependencies, specify version constraints as needed.
- **Update inline dependencies**: Use `uv lock --upgrade-package <package> --script path/to/script.py` to update a package to a specific version or the latest version.

### Example of Inline Script Metadata

The following is an example of inline script metadata per PEP 723 which always appears at the top of the file, before any code, but possibly after a shebang.

  ```python
  # /// script
  # requires-python = ">=3.11"
  # dependencies = [
  #     "markitdown",
  #     "requests>=2.30.0,<3.0.0",
  # ]
  # ///
  ```

## Python Multi-File Application Management with uv

These instructions apply only to multi-file Python applications implemented in this repository.
- **Application structure**: Always structure applications as `uv` projects in their own directories initialized with `uv init`.
- **Add or remove dependencies**: To add or remove project dependencies, use `uv add <package>` or `uv remove <package>`. When adding dependencies, specify version constraints as needed.
- **Update dependencies**: Use `uv lock --upgrade-package <package>` to update a package to a specific version or the latest version.

## Python Tool Execution with uv

These instructions apply to all Python-based tools used in this repository but not implemented in this repository.
- **Use `uvx` to run tools**: All Python-based tools for linting, formatting, etc., must be executed using `uvx`, e.g., `uvx ruff .` for linting. The only exceptions are tools that require an application project is installed, e.g., `pytest`, which must be run using `uv run`.

## Python Version Management with uv

- **Check available Python versions**: Use `uv python list` to see installed versions.
- **Project Python version**: Specify the required Python version in single-file scripts using the `requires-python` field in the inline script metadata.
- **System Python versions**: Use `uv python install <version>` to install specific Python versions managed by `uv`.
- **Pin versions**: Use `uv python pin <version>` in application directories to lock the Python version for that project.

## Testing Python Code with uv

- **Testing**:
  - Write tests for your code using the `pytest` framework. 
  - Add pytest as a dev dependency: `uv add --dev pytest` for applications or include it in script dependencies for single-file scripts with tests.
- **Running tests**:
  - Use `uv run pytest` for applications
  - Use `uv run pytest path/to/tests` for scripts

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
