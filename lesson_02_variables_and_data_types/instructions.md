# Lesson 02: Variables & Data Types

In this lesson, you'll learn about one of the most fundamental concepts in programming: **variables** and the basic **data types** in Python.

## What are Variables?

Imagine you have a piece of information, like a name, an age, or a price, that you want to store and use later in your program. Instead of writing the value directly every time, you can give it a name. This named storage location is called a **variable**.

Think of a variable as a named container or a label that points to a value in your computer's memory. When you assign a value to a variable, you're essentially putting that value into the container and labeling it.

**Creating Variables (Assignment)**

In Python, you create a variable by simply giving it a name and using the equals sign (`=`) to assign a value to it. This process is called **assignment**.

```python
# Assigning a string value to the variable 'user_name'
user_name = "Alice"

# Assigning an integer value to the variable 'age'
age = 30

# Assigning a float value to the variable 'price'
price = 19.99

# Assigning a boolean value to the variable 'is_active'
is_active = True

# You can also reassign values to variables
message = "Hello"
print(message) # Output: Hello

message = "Goodbye"
print(message) # Output: Goodbye
```

**Variable Naming Rules:**

*   Variable names must start with a letter (a-z, A-Z) or an underscore (`_`).
*   They cannot start with a number.
*   They can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
*   Variable names are case-sensitive (`age` is different from `Age`).
*   Avoid using Python keywords (like `if`, `for`, `while`, `print`) as variable names.

## Data Types

Every value in Python has a **data type**. The data type tells Python what kind of data the value is and what operations can be performed on it. Python is dynamically typed, meaning you don't have to explicitly declare the type of a variable; Python infers it based on the value you assign.

Here are the most common built-in data types you'll encounter:

1.  **String (`str`):**
    *   Used for sequences of characters, i.e., text.
    *   You can create strings by enclosing text in single quotes (`'...'`), double quotes (`"..."`), or even triple quotes (`"""..."""` or `'''...'''`) for multi-line strings.
    ```python
    greeting = "Hello, Python!"  # Double quotes
    name = 'Charlie'            # Single quotes
    multiline_text = """This is a
    multi-line string."""
    ```

2.  **Integer (`int`):**
    *   Used for whole numbers (positive, negative, or zero) without a decimal point.
    ```python
    count = 10
    year = 2023
    negative_num = -5
    ```

3.  **Float (`float`):**
    *   Used for numbers with a decimal point, representing real numbers.
    ```python
    price = 29.99
    temperature = 98.6
    pi_value = 3.14159
    ```

4.  **Boolean (`bool`):**
    *   Represents one of two values: `True` or `False`.
    *   Booleans are fundamental for making decisions and controlling the flow of your program.
    *   Note that `True` and `False` must start with a capital letter.
    ```python
    is_logged_in = True
    has_permission = False
    ```

## The `type()` Function

Python provides a built-in function called `type()` that allows you to check the data type of any variable or value. This is very useful for understanding your data.

**Example:**

```python
my_string = "Python is fun"
my_integer = 123
my_float = 45.67
my_boolean = False

print(type(my_string))   # Output: <class 'str'>
print(type(my_integer))  # Output: <class 'int'>
print(type(my_float))    # Output: <class 'float'>
print(type(my_boolean))  # Output: <class 'bool'>
```

Understanding variables and data types is crucial as they are the building blocks for almost every program you will write.

--- 

### Quiz

1.  **Which data type would you use to store a person's age in whole years?**
    a) `str`
    b) `float`
    c) `int`

2.  **What will `type("Hello")` return?**
    a) `<class 'string'>`
    b) `<class 'str'>`
    c) `<class 'text'>`

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. b
</details>