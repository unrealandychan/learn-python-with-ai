# Lesson 18: Error Handling (Try/Except)

In programming, errors (also known as exceptions) are inevitable. They can occur due to various reasons, such as invalid user input, file not found, network issues, or logical mistakes in your code. Without proper **error handling**, your program would simply crash when an error occurs, leading to a poor user experience.

Python provides a robust mechanism for handling errors using the `try...except` block.

## The `try...except` Block

The `try...except` block allows you to gracefully handle errors, preventing your program from crashing and allowing you to provide meaningful feedback or take corrective actions.

**Syntax:**

```python
try:
    # Code that might raise an exception
    statement_1
    statement_2
except ExceptionType as e: # Optional: catch a specific type of exception
    # Code to execute if an exception of ExceptionType occurs in the try block
    handle_error_statement_1
    handle_error_statement_2
except AnotherExceptionType:
    # Code to handle another specific exception
except: # Optional: catch any other exception (general except)
    # Code to handle any unhandled exception
else: # Optional: code to run if no exception occurs in the try block
    # Code to execute if the try block completes without an error
finally: # Optional: code to run regardless of whether an exception occurred or not
    # Code to execute always (e.g., cleanup operations)
```

*   **`try` block:** This is where you place the code that you suspect might cause an error. Python will attempt to execute this code.
*   **`except` block:** If an error occurs within the `try` block, Python immediately stops executing the `try` block and jumps to the `except` block. You can specify the type of exception you want to catch (e.g., `ValueError`, `ZeroDivisionError`). If you don't specify an exception type, it will catch any exception.
*   **`else` block (optional):** The code inside the `else` block is executed only if the `try` block completes without raising any exceptions.
*   **`finally` block (optional):** The code inside the `finally` block is *always* executed, regardless of whether an exception occurred or not, and whether it was handled or not. This is useful for cleanup operations (like closing files or database connections).

## Common Exception Types

Python has many built-in exception types. Here are a few common ones:

*   **`ValueError`:** Raised when a function receives an argument of the correct type but an inappropriate value (e.g., `int("hello")`).
*   **`TypeError`:** Raised when an operation or function is applied to an object of an inappropriate type (e.g., `"5" + 2`).
*   **`ZeroDivisionError`:** Raised when the second operand of a division or modulo operation is zero.
*   **`FileNotFoundError`:** Raised when a file or directory is requested but doesn't exist.
*   **`IndexError`:** Raised when a sequence subscript is out of range (e.g., accessing `my_list[10]` when `my_list` only has 5 elements).
*   **`KeyError`:** Raised when a dictionary key is not found.

## Examples of Error Handling

**Example 1: Handling `ZeroDivisionError`**

```python
def divide(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

divide(10, 2) # Output: The result of 10 / 2 is: 5.0
divide(10, 0) # Output: Error: Cannot divide by zero!
```

**Example 2: Handling `ValueError` from user input**

```python
try:
    age_str = input("Enter your age: ")
    age = int(age_str)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a valid number for age.")
```

**Example 3: Handling multiple exceptions**

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input. Please enter integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e: # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Division successful! Result: {result}")
finally:
    print("Execution of division attempt complete.")
```

Effective error handling makes your programs more robust, user-friendly, and professional.

--- 

### Quiz

1.  **What is the purpose of a `try` block?**
    a) To run code that is guaranteed to work.
    b) To contain code that might raise an error.
    c) To define a new type of error.

2.  **What happens if an error occurs in the `try` block?**
    a) The program crashes.
    b) The code in the corresponding `except` block is executed.
    c) The `try` block is executed again.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>