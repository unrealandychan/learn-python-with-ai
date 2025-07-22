# Lesson 49: Ruff - A Fast Python Linter and Formatter

Ruff is an extremely fast Python linter and formatter, written in Rust. It aims to be a drop-in replacement for many existing tools like Flake8, isort, Black, and more, offering significant performance improvements.

## Why Ruff?

1.  **Speed:** Ruff is incredibly fast, often linting and formatting entire codebases in milliseconds.
2.  **All-in-one:** It combines linting, formatting, and import sorting into a single tool, simplifying your development workflow.
3.  **Compatibility:** It supports a wide range of existing linting rules and can be configured to mimic the behavior of other tools.

## Basic Usage

### Linting

To check your code for linting errors, navigate to your project root and run:

```bash
ruff check .
```

This command will scan all Python files in the current directory and its subdirectories and report any issues.

**Example Output:**

```
my_script.py:1:1: F401 `os` imported but unused
my_script.py:5:80: E501 Line too long (80 > 79 characters)
```

### Fixing Issues

Ruff can automatically fix many linting issues. Use the `--fix` flag:

```bash
ruff check . --fix
```

### Formatting

Ruff also includes a built-in formatter, similar to Black. To format your code:

```bash
ruff format .
```

This will reformat your Python files according to Ruff's default style, which is largely compatible with Black.

## Common Ruff Rules and Examples

Ruff supports a vast number of rules, often prefixed with a letter indicating their category (e.g., `F` for Pyflakes, `E` for Pycodestyle, `I` for isort).

Here are a few common ones:

*   **F401 (Unused Import):**
    ```python
    # Before
    import os
    import sys

    print(sys.version)

    # After (after ruff check --fix)
    import sys

    print(sys.version)
    ```

*   **E501 (Line Too Long):**
    ```python
    # Before
    def very_long_function_name(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        pass

    # After (after ruff format)
    def very_long_function_name(
        arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10
    ):
        pass
    ```

*   **W292 (No Newline at End of File):** Ruff will automatically add a newline if missing when formatting.

*   **N806 (Invalid Variable Name):** (e.g., `myVariable` instead of `my_variable`)
    ```python
    # Before
    myVariable = 10

    # After (requires manual fix or specific configuration for auto-fix)
    my_variable = 10
    ```

## Configuration

Ruff can be configured using a `pyproject.toml` file in your project root. This allows you to specify rules to ignore, target Python version, line length, and more.

**Example `pyproject.toml`:**

```toml
[tool.ruff]
line-length = 88
target-version = "py310"
select = ["E", "F", "W", "I"] # Enable pycodestyle, pyflakes, warnings, isort
ignore = ["E501"] # Ignore line too long errors

[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"] # Ignore unused imports in __init__.py files
```

## Integration

Ruff can be integrated into your development workflow:

*   **Pre-commit Hooks:** Use `pre-commit` to automatically run `ruff check --fix` and `ruff format` before every commit.
*   **IDE Integration:** Most modern IDEs (like VS Code, PyCharm) have extensions that integrate Ruff for real-time linting and formatting.

By using Ruff, you can maintain a consistent and high-quality codebase with minimal effort.