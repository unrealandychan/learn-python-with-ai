# Lesson 26: List Comprehensions

**List comprehensions** provide a concise, readable, and efficient way to create lists in Python. They are a powerful feature that allows you to construct new lists from existing iterables (like other lists, tuples, strings, or ranges) in a single line of code.

## Basic Syntax

The basic syntax of a list comprehension is:

```python
new_list = [expression for item in iterable]
```

*   `expression`: The operation to perform on each `item`.
*   `item`: The variable representing each element from the `iterable`.
*   `iterable`: The source sequence (e.g., a list, tuple, string, or `range()`).

**Example: Squaring numbers**

Let's compare the traditional `for` loop approach with a list comprehension.

**Traditional `for` loop:**

```python
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(squares) # Output: [1, 4, 9, 16, 25]
```

**List Comprehension:**

```python
squares_comp = [x**2 for x in range(1, 6)]
print(squares_comp) # Output: [1, 4, 9, 16, 25]
```

As you can see, the list comprehension achieves the same result in a much more compact and often more readable way.

## Adding Conditional Logic (`if` clause)

You can include an `if` clause in a list comprehension to filter items from the iterable. Only items for which the condition is `True` will be included in the new list.

**Syntax:**

```python
new_list = [expression for item in iterable if condition]
```

**Example: Filtering even numbers**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional for loop with if
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers) # Output: [2, 4, 6, 8, 10]

# List Comprehension with if
even_numbers_comp = [num for num in numbers if num % 2 == 0]
print(even_numbers_comp) # Output: [2, 4, 6, 8, 10]
```

## Nested `if` clauses

You can have multiple `if` conditions. They are evaluated from left to right.

```python
numbers = [10, 15, 20, 25, 30, 35, 40]
# Numbers divisible by both 5 and 2 (i.e., by 10)
divisible_by_10 = [num for num in numbers if num % 5 == 0 if num % 2 == 0]
print(divisible_by_10) # Output: [10, 20, 30, 40]
```

## `if...else` in List Comprehensions

If you need to apply different expressions based on a condition (an `if-else` logic), the `if-else` part comes *before* the `for` loop.

**Syntax:**

```python
new_list = [expression_if_true if condition else expression_if_false for item in iterable]
```

**Example: Categorizing numbers**

```python
numbers = [1, 2, 3, 4, 5]

categorized_numbers = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(categorized_numbers) # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

## Nested List Comprehensions

You can also use nested list comprehensions to flatten lists or create matrices.

**Example: Flattening a list of lists**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for row in matrix for num in row]
print(flattened_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List comprehensions are a powerful and Pythonic way to create lists. They often lead to more readable and efficient code compared to traditional `for` loops for simple list creation and transformation tasks.

--- 

### Quiz

1.  **What is the primary benefit of list comprehensions?**
    a) They are faster than `for` loops.
    b) They are more concise and often more readable.
    c) They can do things `for` loops cannot.

2.  **Is the `if` part of a list comprehension optional?**
    a) Yes
    b) No

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>