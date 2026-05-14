# Lesson 15: Modules & Importing

As your Python programs grow larger, it becomes impractical to keep all your code in a single file. **Modules** provide a way to organize related code into separate files, making your projects more manageable, reusable, and readable.

## What are Modules?

A module is simply a Python file (`.py` extension) containing Python definitions and statements. The file name is the module name. For example, a file named `my_module.py` defines a module named `my_module`.

Modules can define functions, classes, and variables. They can also contain runnable code.

## Importing Modules

The `import` statement is used to bring code from one module into another Python script or interactive session. This allows you to use the functions, classes, and variables defined in that module.

**Syntax:**

```python
import module_name
```

Once imported, you access the contents of the module using the dot (`.`) operator:

```python
module_name.function_name()
module_name.variable_name
```

**Example: Using the `math` module**

The `math` module is a built-in Python module that provides mathematical functions and constants.

```python
import math

# Accessing a constant from the math module
print(f"The value of pi is: {math.pi}")

# Using a function from the math module
number = 16
sqrt_number = math.sqrt(number)
print(f"The square root of {number} is: {sqrt_number}")
```

## Different Ways to Import

1.  **`import module_name` (Standard Import):**
    *   Imports the entire module.
    *   You must use the module name as a prefix to access its contents.
    *   Good for avoiding name conflicts.

2.  **`import module_name as alias` (Import with Alias):**
    *   Imports the entire module but gives it a shorter, more convenient alias.
    *   Commonly used for modules with long names or standard aliases (e.g., `import pandas as pd`).
    ```python
    import math as m

    print(f"Pi using alias: {m.pi}")
    ```

3.  **`from module_name import item1, item2` (Selective Import):**
    *   Imports only specific items (functions, classes, variables) from a module.
    *   You can use the imported items directly without the module prefix.
    *   Useful when you only need a few things from a large module.
    ```python
    from math import pi, sqrt

    print(f"Pi directly: {pi}")
    print(f"Square root of 9: {sqrt(9)}")
    ```

4.  **`from module_name import *` (Wildcard Import - Generally Discouraged):**
    *   Imports all public names from a module directly into the current namespace.
    *   **Discouraged** because it can lead to name conflicts and make it harder to tell where functions/variables came from.
    ```python
    from math import *

    print(f"Pi directly (wildcard): {pi}")
    ```

## Creating Your Own Modules

Any `.py` file you create can be imported as a module. Let's say you have a file named `my_utils.py`:

`my_utils.py`:
```python
def greet_user(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

Then, in another file (e.g., your `exercise.py` or `main.py`):

```python
import my_utils

print(my_utils.greet_user("Eve"))
print(my_utils.add(10, 20))

from my_utils import greet_user
print(greet_user("Frank"))
```

Modules are fundamental for structuring larger Python projects and leveraging the vast ecosystem of Python's standard library and third-party packages.

--- 

### Quiz

1.  **Which keyword is used to import a module?**
    a) `include`
    b) `import`
    c) `use`

2.  **How would you get a random integer between 1 and 10 (inclusive)?**
    a) `random.randint(1, 10)`
    b) `random.integer(1, 10)`
    c) `random.get(1, 10)`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>