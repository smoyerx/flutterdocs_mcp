---
description: "Python development workflow using uv (reference only)"
name: python_workflow
applyTo: "**/*.do_not_auto_include"
---

# Python Development Workflow Using uv

**Note**: This file is for manual reference only. It will not be automatically included when AI generates Python code.

Instructions for managing Python single-file scripts and multi-file applications using [`uv`](https://github.com/astral-sh/uv).

## Python Single-File Scripts

- **Script execution**: Always run scripts with `uv run path/to/script.py` to ensure dependencies are resolved and installed automatically.
- **Inline dependencies**: Specify dependencies inline at the top of each script per [PEP 723](https://peps.python.org/pep-0723/). Do not maintain a `requirements.txt` file.
- **Add or remove inline dependencies**: To add or remove inline dependencies, use `uv add --script path/to/script.py <packages>` or `uv remove --script path/to/script.py <packages>`. When adding dependencies, specify version constraints as needed.
- **Update inline dependencies**: Use `uv lock --upgrade-package <package> --script path/to/script.py` to update a package to a specific version or the latest version.

## Python Multi-File Applications

- **Application structure**: Always structure applications as `uv` projects in their own directories initialized with `uv init`.
- **Add or remove dependencies**: To add or remove project dependencies, use `uv add <package>` or `uv remove <package>`. When adding dependencies, specify version constraints as needed.
- **Update dependencies**: Use `uv lock --upgrade-package <package>` to update a package to a specific version or the latest version.

## External Python Tools (Tools Not Implemented in This Repository)

- **Use `uvx` to run tools**: External Python tools must be executed using `uvx`, e.g., `uvx ruff .` for linting. The only exceptions are external tools that require an application project to be installed, e.g., `pytest`, which must be run using `uv run`.

## Testing Python Code

- **Testing**:
  - Write tests for your code using the `pytest` framework. 
  - Add `pytest` as a dev dependency: `uv add --dev pytest` for applications or include it in script dependencies for single-file scripts with tests.
- **Running tests**:
  - Use `uv run pytest` for applications
  - Use `uv run pytest path/to/tests` for scripts
