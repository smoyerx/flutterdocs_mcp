---
name: python-workflow
description: "Python script, project, package, and workflow management using uv. Use for running, testing, managing, and defining dependencies for Python single-file scripts and multi-file applications."
---

# Python Workflow Management Using uv

Instruction for managing Python single-file scripts and multi-file applications using [`uv`](https://github.com/astral-sh/uv).

## Python Single-File Scripts

- **Script execution**: Run scripts with `uv run path/to/script.py` to ensure dependencies are resolved and installed automatically.
- **Inline dependencies**: Specify dependencies inline at the top of each script per [PEP 723](https://peps.python.org/pep-0723/).
- **Add or remove inline dependencies**:
  - Use `uv add --script path/to/script.py <packages>` to add a dependency, specifying version constraints as needed
  - Use `uv remove --script path/to/script.py <packages>` to remove a dependency
- **Update inline dependencies**: Use `uv lock --upgrade-package <package> --script path/to/script.py` to update a package to a specific version or the latest version.
- **Testing**:
  - Write tests using the `pytest` framework
  - Run tests with `uvx pytest path/to/tests`

## Python Multi-File Applications

- **Application structure**: Structure applications as `uv` **projects** in their own directories initialized with `uv init`.
- **Add or remove dependencies**:
  - Use `uv add <package>` to add a dependency to the project, specifying version constraints as needed
  - Use `uv remove <package>` to remove a dependency from the project
- **Update dependencies**: Use `uv lock --upgrade-package <package>` to update a project package to a specific version or the latest version.
- **Testing**:
  - Write tests using the `pytest` framework
  - Add `pytest` as a dev dependency for the project using `uv add --dev pytest`
  - Run tests with `uv run pytest path/to/tests`

## External Python Tools (which are any Python tools not implemented in this repository)

- **Executing tools**: Run external tools with `uvx <tool>`, e.g., `uvx ruff .` for linting and formatting. The only exceptions are external tools that require a multi-file application **project** to be installed, e.g., `pytest` or `mypy`, which must be run using `uv run <tool>`.
