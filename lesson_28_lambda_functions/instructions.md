# Lesson 28: Lambda Functions

In Python, a **lambda function** (also known as an anonymous function) is a small, single-expression function that doesn't have a name. They are typically used for short, throwaway functions that you only need once.

## Syntax of Lambda Functions

A lambda function is defined using the `lambda` keyword, followed by arguments, a colon, and a single expression.

**Syntax:**

```python
lambda arguments: expression
```

*   `lambda`: The keyword used to define an anonymous function.
*   `arguments`: One or more arguments, separated by commas (similar to regular function parameters).
*   `expression`: A single expression. The result of this expression is implicitly returned by the lambda function.

**Key Characteristics:**

*   **Anonymous:** They don't have a name.
*   **Single Expression:** They can only contain one expression, which is implicitly returned.
*   **No Statements:** They cannot contain statements like `if`, `for`, `while`, `return` (explicitly), etc.

## Examples of Lambda Functions

**Example 1: Simple addition**

```python
# A lambda function that adds two numbers
add_two_numbers = lambda x, y: x + y

print(add_two_numbers(5, 3))  # Output: 8
print(add_two_numbers(10, 2)) # Output: 12
```

**Example 2: Squaring a number**

```python
square = lambda x: x * x

print(square(4))  # Output: 16
print(square(7))  # Output: 49
```

**Example 3: Checking for even numbers**

```python
is_even = lambda num: num % 2 == 0

print(is_even(4)) # Output: True
print(is_even(7)) # Output: False
```

## When to Use Lambda Functions

Lambda functions are most commonly used in situations where a small function is required for a short period, often as an argument to higher-order functions (functions that take other functions as arguments).

Common scenarios include:

*   **Sorting:** As the `key` argument for `sorted()`, `list.sort()`, etc.
*   **`map()`, `filter()`, `reduce()`:** (Covered in the next lesson) To define simple operations.

**Example: Sorting a list of tuples**

Suppose you have a list of tuples, where each tuple represents a person's name and age, and you want to sort them by age.

```python
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Sort by age (the second element of each tuple)
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people) # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
```

Here, `lambda person: person[1]` is a small anonymous function that takes a `person` tuple and returns its second element (`person[1]`, which is the age). The `sorted()` function then uses this returned age as the key for sorting.

While you could define a regular function for this, a lambda function is more concise for such a simple, one-off operation.

--- 

### Quiz

1.  **Can a lambda function have more than one expression?**
    a) Yes
    b) No

2.  **Are lambda functions named?**
    a) Yes
    b) No, they are anonymous.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>