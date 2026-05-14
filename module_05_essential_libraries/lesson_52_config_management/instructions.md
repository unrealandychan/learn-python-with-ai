# Lesson 52: Configuration Management with `.env` files

In modern application development, managing configuration settings is crucial. These settings often include sensitive information (like API keys, database credentials) or values that change between different deployment environments (development, testing, production).

Hardcoding such values directly into your source code is a significant security risk and makes your application inflexible. `.env` files, combined with libraries like `python-dotenv`, provide a simple, secure, and flexible solution for managing these configurations.

## Why use `.env` files?

1.  **Security:** Keeps sensitive data out of your version control system (e.g., Git). You typically add `.env` to your `.gitignore` file.
2.  **Flexibility:** Easily change configurations without modifying code, simply by updating the `.env` file.
3.  **Environment-Specific Settings:** Allows different settings for development, testing, and production environments.
4.  **Simplicity:** Easy to understand and implement.

## How it works with `python-dotenv`

`python-dotenv` is a Python library that reads key-value pairs from a `.env` file and sets them as environment variables in your running process.

### Installation

First, install the library:

```bash
pip install python-dotenv
```

### Basic Usage

**Step 1: Create a `.env` file**

In the root of your project directory, create a file named `.env` (note the leading dot). Add your configuration variables in `KEY=VALUE` format. No quotes are needed for simple strings, but they can be used for values with spaces or special characters.

Example `my_project/.env`:

```dotenv
DATABASE_URL="postgresql://user:password@host:5432/mydatabase"
API_KEY=your_super_secret_api_key_12345
DEBUG_MODE=True
APP_VERSION=1.0.0
# Comments start with #
# You can also have empty lines
```

**Step 2: Add `.env` to `.gitignore`**

To prevent your `.env` file from being committed to version control, add it to your `.gitignore` file:

```gitignore
# .gitignore
.env
```

**Step 3: Load variables in your Python code**

In your Python script, import `load_dotenv` from `dotenv` and call it at the very beginning of your application. Then, use `os.getenv()` to access the variables.

Example `my_project/main.py`:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables using os.getenv()
db_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG_MODE", "False") # Provide a default value
app_version = os.getenv("APP_VERSION")

print(f"Database URL: {db_url}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")
print(f"App Version: {app_version}")

# Example of type conversion (os.getenv always returns strings)
if debug_mode.lower() == "true":
    print("Application is running in DEBUG mode.")
else:
    print("Application is running in PRODUCTION mode.")

# You can also access them via os.environ, but getenv is safer as it returns None if not found
# print(os.environ["API_KEY"]) # This would raise a KeyError if API_KEY is not set
```

### Advanced Usage and Best Practices

*   **Default Values:** Always use `os.getenv("VAR_NAME", "default_value")` to provide a fallback if the environment variable is not set. This prevents `TypeError` if the variable is missing.
*   **Type Conversion:** Environment variables are always loaded as strings. Remember to convert them to the appropriate type (e.g., `int()`, `float()`, `bool()` or custom logic for booleans) if needed.
*   **Loading Specific `.env` files:** You can specify the path to a `.env` file if it's not in the current working directory or if you have multiple:
    ```python
    load_dotenv(dotenv_path='/path/to/my_config/.env.production')
    ```
*   **Environment Variables Precedence:** If an environment variable is already set in the shell (e.g., `export API_KEY=shell_key`), `python-dotenv` will *not* override it by default. The shell environment takes precedence. You can force override with `load_dotenv(override=True)`.
*   **Sensitive Data Handling:** For highly sensitive data (e.g., production database passwords), consider more robust solutions like dedicated secret management services (e.g., HashiCorp Vault, AWS Secrets Manager) in production environments, in addition to or instead of `.env` files.

By adopting `.env` files for configuration, you enhance the security, flexibility, and maintainability of your Python applications.