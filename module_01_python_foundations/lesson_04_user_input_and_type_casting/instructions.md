# Lesson 04: User Input & Type Casting

In this lesson, you'll learn how to make your Python programs interactive by getting input from the user and how to change the data type of a variable, a process known as **type casting**.

## Getting User Input with `input()`

The `input()` function is a built-in Python function that allows your program to pause and wait for the user to type something and press Enter. Whatever the user types is then returned by the `input()` function.

**Important Note:** The `input()` function *always* returns the user's input as a **string** (`str`), regardless of what the user types (even if they type numbers).

**Syntax:**

```python
variable_name = input("Prompt message for the user: ")
```

**Example:**

```python
# Ask the user for their name
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Ask for a number - it will still be a string!
favorite_number_str = input("What is your favorite number? ")
print(f"You entered: {favorite_number_str}, which is of type {type(favorite_number_str)}")
```

## Type Casting (Type Conversion)

Since `input()` always returns a string, you often need to convert that string to another data type if you want to perform operations that are specific to numbers (like arithmetic calculations) or other data types. This conversion process is called **type casting** or **type conversion**.

Python provides several built-in functions for type casting:

*   `int(value)`: Converts `value` to an integer.
    *   Can convert strings containing whole numbers (e.g., `"123"` to `123`).
    *   Can convert floats by truncating the decimal part (e.g., `3.14` to `3`).
*   `float(value)`: Converts `value` to a floating-point number.
    *   Can convert strings containing numbers (e.g., `"12.34"` to `12.34`).
    *   Can convert integers (e.g., `5` to `5.0`).
*   `str(value)`: Converts `value` to a string.
    *   Useful when you want to concatenate numbers with strings using the `+` operator.
*   `bool(value)`: Converts `value` to a boolean.
    *   Most values are `True` (e.g., non-empty strings, non-zero numbers).
    *   `False` for empty strings (`""`), zero (`0`), `None`, empty lists, etc.

**Examples of Type Casting:**

```python
# Converting string to integer
str_age = "25"
int_age = int(str_age)
print(f"Integer age: {int_age}, Type: {type(int_age)}")

# Converting string to float
str_price = "99.99"
float_price = float(str_price)
print(f"Float price: {float_price}, Type: {type(float_price)}")

# Converting integer to string (useful for concatenation)
num_apples = 5
message = "I have " + str(num_apples) + " apples."
print(message)

# Combining input and type casting
age_input = input("How old are you? ")
age_as_int = int(age_input) # Convert the string input to an integer
print(f"Next year, you will be {age_as_int + 1} years old.")

# Example of potential error: trying to convert non-numeric string to int/float
# invalid_num_str = "hello"
# int(invalid_num_str) # This would cause a ValueError!
```

Understanding how to get user input and perform type casting is essential for building interactive and functional Python applications.

--- 

### Quiz

1.  **The `input()` function returns data of what type?**
    a) `int`
    b) `string`
    c) `str`

2.  **Which function converts a string to an integer?**
    a) `to_int()`
    b) `int()`
    c) `integer()`

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. b
</details>