# Lesson 52: Configuration Management (using `.env` files) - Exercise

## Objective
This exercise will guide you through creating a `.env` file and then loading and accessing its variables within a Python script using the `python-dotenv` library.

## Instructions

1.  **Install `python-dotenv`:** If you haven't already, install the necessary library:
    ```bash
    pip install python-dotenv
    ```

2.  **Create a `.env` file:** In the same directory as this `exercise.py` file (`lesson_52_config_management`), create a new file named `.env`.

3.  **Add variables to `.env`:** Open the newly created `.env` file and add the following lines to it:

    ```dotenv
    # .env
    APP_NAME="My Awesome Python App"
    API_KEY=your_super_secret_api_key_123
    DEBUG_MODE=True
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    ```

4.  **Run this `exercise.py` script:** Execute this Python script. It will load the variables from your `.env` file and print them to the console.

5.  **Experiment (Optional):**
    *   Try changing the values in the `.env` file and re-running the script to see the changes reflected.
    *   Comment out one of the variables in `.env` (e.g., `API_KEY`) and observe what `os.getenv()` returns (it will be `None` unless you provide a default).
    *   Add a new variable to `.env` and try to access it in the script.

---

```python
import os
from dotenv import load_dotenv

# Load environment variables from the .env file.
# By default, load_dotenv() looks for a .env file in the current directory
# or its parent directories.
load_dotenv()

print("\n--- Loaded Configuration ---")

# Access the variables using os.getenv()
# It's good practice to provide a default value in case the variable is not set.

app_name = os.getenv("APP_NAME", "Default App")
api_key = os.getenv("API_KEY", "NO_API_KEY_SET")

# For boolean values, os.getenv returns a string. You need to convert it.
debug_mode_str = os.getenv("DEBUG_MODE", "False")
debug_mode = debug_mode_str.lower() == "true"

database_host = os.getenv("DATABASE_HOST", "127.0.0.1")

# For integer values, also convert from string
database_port_str = os.getenv("DATABASE_PORT", "5432")
try:
    database_port = int(database_port_str)
except ValueError:
    database_port = 5432 # Fallback to default if conversion fails

print(f"Application Name: {app_name}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode} (Type: {type(debug_mode)}) ")
print(f"Database Host: {database_host}")
print(f"Database Port: {database_port} (Type: {type(database_port)}) ")

print("\n--- End Configuration ---")

# Example usage of a loaded variable
if debug_mode:
    print("\nApplication is running in DEBUG mode. Extra logging enabled.")
else:
    print("\nApplication is running in PRODUCTION mode.")

# Simulate using the API key
if api_key != "NO_API_KEY_SET":
    print(f"\nConnecting to external service with API Key: {api_key[:5]}... (truncated)")
else:
    print("\nWarning: API Key not set. External service access might be limited.")

```