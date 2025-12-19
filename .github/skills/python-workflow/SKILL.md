---
description: "Python development workflow using uv (reference only)"
name: python_workflow
applyTo: "**/*.do_not_auto_include"
---

# Python Development Workflow Using uv

**Note**: This file is for manual reference only. It will not be automatically included in the context when AI generates Python code.

Instructions for managing Python single-file scripts and multi-file applications using [`uv`](https://github.com/astral-sh/uv).

## Python Single-File Scripts

- **Script execution**: Always run scripts with `uv run path/to/script.py` to ensure dependencies are resolved and installed automatically.
- **Inline dependencies**: Specify dependencies inline at the top of each script per [PEP 723](https://peps.python.org/pep-0723/).
- **Add or remove inline dependencies**:
  - Use `uv add --script path/to/script.py <packages>` to add a dependency, specifying version constraints as needed
  - Use `uv remove --script path/to/script.py <packages>` to remove a dependency
- **Update inline dependencies**: Use `uv lock --upgrade-package <package> --script path/to/script.py` to update a package to a specific version or the latest version.
- **Testing**:
  - Write tests using the `pytest` framework
  - Run tests with `uvx pytest path/to/tests`

## Python Multi-File Applications

- **Application structure**: Always structure applications as `uv` **projects** in their own directories initialized with `uv init`.
- **Add or remove dependencies**: Use `uv add <package>` or `uv remove <package>`. When adding dependencies, specify version constraints as needed.
- **Update dependencies**: Use `uv lock --upgrade-package <package>` to update a package to a specific version or the latest version.
- **Testing**:
  - Write tests using the `pytest` framework
  - Add `pytest` as a dev dependency for the project: `uv add --dev pytest`
  - Run tests with `uv run pytest path/to/tests`

## External Python Tools (Tools Not Implemented in This Repository)

- **Use `uvx` to run external tools**: External Python tools must be executed using `uvx`, e.g., `uvx ruff .` for linting. The only exceptions are external tools that require a multi-file application **project** to be installed, e.g., `pytest` or `mypy`, which must be run using `uv run`.
