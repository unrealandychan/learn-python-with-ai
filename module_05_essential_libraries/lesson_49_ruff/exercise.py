# Lesson 49: Ruff - Exercise

## Objective
The goal of this exercise is to practice using Ruff to identify and fix common linting and formatting issues in Python code.

## Instructions

1.  **Install Ruff:** If you haven't already, install Ruff in your virtual environment:
    ```bash
    pip install ruff
    ```

2.  **Analyze the code:** The code below contains several common linting and formatting issues. Your task is to use Ruff to identify these issues.

3.  **Run Ruff Check:** From your terminal, navigate to the `lesson_49_ruff` directory and run Ruff to check this `exercise.py` file:
    ```bash
    ruff check exercise.py
    ```
    Observe the output and identify the reported errors.

4.  **Fix Automatically:** Use Ruff's auto-fix feature to resolve as many issues as possible:
    ```bash
    ruff check exercise.py --fix
    ```
    Then, run `ruff check exercise.py` again to see which issues remain.

5.  **Format with Ruff:** Apply Ruff's formatter to this file:
    ```bash
    ruff format exercise.py
    ```
    Check if any formatting issues were resolved.

6.  **Manual Fixes:** Manually correct any remaining issues that Ruff could not fix automatically (e.g., unused variables that are not imports, logical errors).

7.  **Verify:** Run `ruff check exercise.py` one last time. There should be no errors reported.

---

## Code to be fixed:

```python
import os
import sys

def calculate_area(length, width):
    # This is a very long comment that exceeds the typical line length limit of 79 or 88 characters, and it should be wrapped or shortened.
    AREA = length * width
    return AREA

class MyClass:
    def __init__(self, value):
        self.Value = value # This variable name does not follow snake_case convention

    def print_value(self):
        print(f"The value is: {self.Value}")

def main():
    x = 10
    y = 20
    result = calculate_area(x, y)
    print(f"The area is {result}")

    my_object = MyClass(100)
    my_object.print_value()

if __name__ == "__main__":
    main()
    # There is an extra space at the end of this line.
```