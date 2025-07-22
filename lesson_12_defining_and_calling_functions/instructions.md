# Lesson 12: Defining & Calling Functions

In programming, a **function** is a block of organized, reusable code that performs a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

## Why Use Functions?

1.  **Reusability:** Write code once and use it multiple times.
2.  **Modularity:** Break down complex problems into smaller, manageable pieces.
3.  **Readability:** Make your code easier to understand and maintain.
4.  **Debugging:** Easier to isolate and fix problems.

## Defining a Function

In Python, a function is defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. The code block that forms the body of the function must be indented.

**Syntax:**

```python
def function_name():
    # Code block (indented)
    statement_1
    statement_2
    # ...
```

*   `def`: Keyword to indicate the start of a function definition.
*   `function_name`: A descriptive name for your function. Follow Python's naming conventions (lowercase, words separated by underscores).
*   `()`: Parentheses, which may contain parameters (we'll cover this in the next lesson).
*   `:`: A colon, marking the end of the function header.
*   **Indentation:** All statements belonging to the function must be indented consistently (usually 4 spaces).

**Example:**

```python
def greet():
    print("Hello, welcome to the function!")
    print("This is inside the greet function.")

def show_message():
    print("This is a different message from another function.")
```

## Calling a Function

Defining a function only tells Python what the function does. To actually execute the code inside the function, you must **call** or **invoke** the function. You call a function by typing its name followed by parentheses `()`.

**Syntax:**

```python
function_name()
```

**Example:**

```python
# Define the function
def greet():
    print("Hello, welcome to the function!")

# Call the function
greet()
# Output:
# Hello, welcome to the function!

# Define another function
def perform_task():
    print("Performing a specific task...")
    # You can call other functions from within a function
    greet() # Calling the greet function from inside perform_task
    print("Task completed.")

# Call the second function
perform_task()
# Output:
# Performing a specific task...
# Hello, welcome to the function!
# Task completed.
```

Functions are the backbone of structured programming in Python. They allow you to organize your code into logical, manageable units.

--- 

### Quiz

1.  **Which keyword is used to define a function?**
    a) `function`
    b) `def`
    c) `define`

2.  **How do you execute a function?**
    a) By typing its name.
    b) By calling it with parentheses, e.g., `my_function()`.
    c) It runs automatically.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>