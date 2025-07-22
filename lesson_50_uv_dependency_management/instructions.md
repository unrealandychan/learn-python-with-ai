# Lesson 50: uv - A Fast Python Package and Environment Manager

`uv` is a modern, high-performance Python package and environment manager written in Rust. It aims to be a fast, drop-in replacement for `pip`, `pip-tools`, and `venv`, streamlining your Python development workflow.

## Why uv?

*   **Blazing Fast:** `uv` is significantly faster than traditional Python package managers, making dependency resolution and installation almost instantaneous.
*   **All-in-One:** It combines virtual environment creation, package installation, dependency compilation (locking), and synchronization into a single tool.
*   **Reliable:** `uv` uses a robust dependency resolver, ensuring consistent and reproducible builds.

## Installation

You can install `uv` using `pipx` (recommended for global tools) or `pip`:

```bash
pipx install uv
# Or, if you prefer pip (though pipx is better for CLI tools)
pip install uv
```

## Core Concepts and Commands

### 1. Virtual Environments (`uv venv`)

`uv` makes creating and managing virtual environments simple and fast. It replaces `python -m venv`.

**Create a new virtual environment:**

```bash
uv venv
```

This will create a `.venv` directory in your current project. You can specify a different name:

```bash
uv venv my-env
```

**Activate the virtual environment:**

*   **Linux/macOS:**
    ```bash
    source .venv/bin/activate
    ```
*   **Windows (Command Prompt):**
    ```bash
    .venv\Scripts\activate.bat
    ```
*   **Windows (PowerShell):**
    ```bash
    .venv\Scripts\Activate.ps1
    ```

### 2. Installing Packages (`uv pip install`)

`uv pip install` is a direct replacement for `pip install`. It's much faster.

**Install a single package:**

```bash
uv pip install requests
```

**Install multiple packages:**

```bash
uv pip install requests pandas
```

**Install from `requirements.txt`:**

```bash
uv pip install -r requirements.txt
```

### 3. Dependency Compilation (Locking) (`uv pip compile`)

This command generates a `uv.lock` file (or a `requirements.txt` file) that precisely pins all direct and transitive dependencies. This ensures reproducible installations across different environments.

**Create a `requirements.in` file (e.g., `requirements.in`):

```
requests
pandas
```

**Compile dependencies to `requirements.txt`:**

```bash
uv pip compile requirements.in -o requirements.txt
```

This will generate a `requirements.txt` file with exact versions of all dependencies.

**Compile to `uv.lock` (recommended for `uv` projects):**

If you have a `pyproject.toml` with a `[project]` section, `uv` can automatically detect your dependencies. Otherwise, you can specify them directly or use `requirements.in`.

```bash
uv pip compile
```

This will create a `uv.lock` file in your project root, which is `uv`'s preferred lock file format.

### 4. Synchronizing Environments (`uv pip sync`)

`uv pip sync` installs the exact dependencies specified in a lock file (`uv.lock` or `requirements.txt`), ensuring your environment matches the locked state.

**Sync from `uv.lock`:**

```bash
uv pip sync
```

**Sync from `requirements.txt`:**

```bash
uv pip sync requirements.txt
```

This command is idempotent: if your environment already matches the lock file, it does nothing. If packages are missing or have incorrect versions, it installs/updates them. If extra packages are present, it uninstalls them.

## Example Workflow

1.  **Start a new project:**
    ```bash
    mkdir my_project
    cd my_project
    ```

2.  **Create a virtual environment:**
    ```bash
    uv venv
    source .venv/bin/activate # Activate it
    ```

3.  **Define direct dependencies (e.g., in `pyproject.toml` or `requirements.in`):

    **`pyproject.toml` example:**
    ```toml
    [project]
    name = "my-project"
    version = "0.1.0"
    dependencies = [
        "requests",
        "pandas",
    ]
    ```

    **`requirements.in` example:**
    ```
    requests
    pandas
    ```

4.  **Compile dependencies (generate lock file):**
    ```bash
uv pip compile # If using pyproject.toml
# OR
uv pip compile requirements.in -o requirements.txt # If using requirements.in
    ```

5.  **Install/Sync dependencies:**
    ```bash
uv pip sync # Installs from uv.lock or requirements.txt
    ```

This workflow ensures that everyone working on the project uses the exact same versions of all dependencies, preventing "works on my machine" issues.