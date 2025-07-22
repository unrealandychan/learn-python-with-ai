
# Lesson 35: Interacting with the Operating System (`os` and `sys` modules)

Python's `os` and `sys` modules are fundamental for interacting with the operating system and the Python interpreter itself. They provide a way to perform tasks that are typically done through the command line, such as file system operations, environment variable access, and managing program execution.

## 1. The `os` Module: Operating System Interface

The `os` module provides a portable way of using operating system dependent functionality. It allows you to interact with the file system, environment variables, processes, and more.

### Common `os` Module Functions:

*   `os.getcwd()`: Returns the current working directory.
*   `os.chdir(path)`: Changes the current working directory to `path`.
*   `os.listdir(path='.')`: Returns a list containing the names of the entries in the directory given by `path`.
*   `os.mkdir(path)`: Creates a directory named `path`.
*   `os.makedirs(path)`: Creates directories recursively. If an intermediate directory in `path` does not exist, it will be created.
*   `os.remove(path)`: Removes (deletes) the file `path`.
*   `os.rmdir(path)`: Removes (deletes) the empty directory `path`.
*   `os.rename(src, dst)`: Renames the file or directory `src` to `dst`.
*   `os.path.exists(path)`: Returns `True` if `path` refers to an existing path or an open file descriptor.
*   `os.path.isfile(path)`: Returns `True` if `path` is an existing regular file.
*   `os.path.isdir(path)`: Returns `True` if `path` is an existing directory.
*   `os.path.join(path, *paths)`: Joins one or more path components intelligently. This is crucial for creating paths that work correctly across different operating systems (Windows, macOS, Linux).
*   `os.environ`: A dictionary-like object that represents the user's environment variables.

### Examples of `os` Module Usage:

```python
import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# List contents of current directory
print("\nContents of current directory:")
for item in os.listdir():
    print(f"- {item}")

# Create a new directory
new_dir = "my_new_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"\nCreated directory: {new_dir}")
else:
    print(f"\nDirectory '{new_dir}' already exists.")

# Change directory and then change back
print(f"\nChanging to {new_dir}...")
os.chdir(new_dir)
print(f"Current working directory: {os.getcwd()}")
os.chdir(current_dir) # Change back to original directory
print(f"Changed back to: {os.getcwd()}")

# Create a file inside the new directory and then remove it
file_path = os.path.join(new_dir, "test_file.txt")
with open(file_path, 'w') as f:
    f.write("Hello from test file!")
print(f"\nCreated file: {file_path}")

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Removed file: {file_path}")

# Remove the created directory (must be empty)
if os.path.exists(new_dir) and not os.listdir(new_dir):
    os.rmdir(new_dir)
    print(f"Removed directory: {new_dir}")
else:
    print(f"Directory '{new_dir}' is not empty or does not exist, cannot remove.")

# Accessing environment variables
path_env = os.environ.get('PATH')
if path_env:
    print(f"\nPATH environment variable (first 100 chars): {path_env[:100]}...")
else:
    print("\nPATH environment variable not found.")
```

## 2. The `sys` Module: System-Specific Parameters and Functions

The `sys` module provides access to system-specific parameters and functions. It allows you to interact with the Python interpreter directly.

### Common `sys` Module Attributes and Functions:

*   `sys.argv`: A list of command-line arguments passed to a Python script. `sys.argv[0]` is the script name itself.
*   `sys.platform`: A string indicating the platform (e.g., 'linux', 'win32', 'darwin').
*   `sys.version`: A string containing the Python interpreter version.
*   `sys.path`: A list of strings that specifies the search path for modules. When you `import` a module, Python searches these directories.
*   `sys.exit(status)`: Exits the Python interpreter. The optional argument `status` can be an integer (0 for success, non-zero for error) or another type of object.
*   `sys.stdin`, `sys.stdout`, `sys.stderr`: File objects corresponding to the interpreter's standard input, output, and error streams.

### Examples of `sys` Module Usage:

```python
import sys

# Command-line arguments
print(f"\nCommand-line arguments: {sys.argv}")
if len(sys.argv) > 1:
    print(f"First argument (after script name): {sys.argv[1]}")
else:
    print("No command-line arguments provided (run like: python your_script.py arg1 arg2)")

# Platform information
print(f"\nOperating System Platform: {sys.platform}")

# Python version
print(f"Python Version: {sys.version.split('\n')[0]}")

# Module search path
print("\nPython Module Search Path (first 5 entries):")
for i, path in enumerate(sys.path[:5]):
    print(f"- {path}")
if len(sys.path) > 5:
    print("...")

# Exiting the script (uncomment to test)
# if "exit_now" in sys.argv:
#     print("Exiting script as requested.")
#     sys.exit(0)
```

---

### Quiz

1.  **Which `os` module function is used to get the current working directory?**
    a) `os.path.cwd()`
    b) `os.get_current_dir()`
    c) `os.getcwd()`
    d) `os.current_directory()`

2.  **What does `sys.argv` typically contain?**
    a) The Python interpreter's version.
    b) A list of environment variables.
    c) A list of command-line arguments passed to the script, including the script name itself.
    d) The current date and time.

3.  **Which `os.path` function should you use to create a file path that works correctly on both Windows and Linux?**
    a) `os.path.concat()`
    b) `os.path.combine()`
    c) `os.path.join()`
    d) `os.path.merge()`

4.  **If you want to create a directory and any necessary parent directories that don't exist, which `os` function would you use?**
    a) `os.mkdir()`
    b) `os.makedirs()`
    c) `os.create_dir()`
    d) `os.make_dirs_recursive()`

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. c
  3. c
  4. b
</details>

