# Lesson 29: The `map()`, `filter()`, and `reduce()` Functions

Python provides several built-in higher-order functions that allow you to perform common operations on iterables in a functional programming style. These functions often work well with lambda functions for concise code.

## 1. The `map()` Function

The `map()` function applies a given function to each item in an iterable (like a list or tuple) and returns an iterator that yields the results. It's useful when you want to transform every element in a sequence.

**Syntax:**

```python
map(function, iterable)
```

*   `function`: The function to apply to each item.
*   `iterable`: The sequence (list, tuple, etc.) whose elements will be processed.

**Example:**

```python
# Double each number in a list
numbers = [1, 2, 3, 4, 5]

# Using a regular function
def double(x):
    return x * 2
doubled_numbers_map = list(map(double, numbers))
print(doubled_numbers_map) # Output: [2, 4, 6, 8, 10]

# Using a lambda function (more common with map)
doubled_numbers_lambda = list(map(lambda x: x * 2, numbers))
print(doubled_numbers_lambda) # Output: [2, 4, 6, 8, 10]

# Convert a list of strings to integers
str_numbers = ["10", "20", "30"]
int_numbers = list(map(int, str_numbers))
print(int_numbers) # Output: [10, 20, 30]
```

## 2. The `filter()` Function

The `filter()` function constructs an iterator from elements of an iterable for which a function returns `True`. It's useful when you want to select specific elements from a sequence based on a condition.

**Syntax:**

```python
filter(function, iterable)
```

*   `function`: A function that returns `True` or `False` for each item.
*   `iterable`: The sequence whose elements will be filtered.

**Example:**

```python
# Get only the even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a regular function
def is_even(x):
    return x % 2 == 0
even_numbers_filter = list(filter(is_even, numbers))
print(even_numbers_filter) # Output: [2, 4, 6, 8, 10]

# Using a lambda function (more common with filter)
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_lambda) # Output: [2, 4, 6, 8, 10]

# Filter out empty strings
words = ["hello", "", "world", "", "python"]
non_empty_words = list(filter(None, words)) # None acts as identity function, filters out falsy values
print(non_empty_words) # Output: ['hello', 'world', 'python']
```

## 3. The `reduce()` Function

The `reduce()` function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. It's useful for performing aggregations.

**Important:** `reduce()` is not a built-in function. You need to import it from the `functools` module.

**Syntax:**

```python
from functools import reduce
reduce(function, iterable[, initializer])
```

*   `function`: A function that takes two arguments.
*   `iterable`: The sequence to reduce.
*   `initializer` (optional): An initial value for the computation.

**Example:**

```python
from functools import reduce

# Calculate the sum of all numbers in a list
numbers = [1, 2, 3, 4, 5]

# Using a lambda function
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers) # Output: 15

# Calculate the product of all numbers in a list
product_numbers = reduce(lambda x, y: x * y, numbers)
print(product_numbers) # Output: 120 (1*2*3*4*5)

# Using an initializer
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_initial) # Output: 25 (10 + 1+2+3+4+5)
```

While list comprehensions are often preferred for simple transformations and filtering, `map()`, `filter()`, and `reduce()` offer powerful alternatives, especially when combined with lambda functions, for functional programming paradigms.

--- 

### Quiz

1.  **Which function would you use to apply the same operation to every element in a list?**
    a) `filter`
    b) `reduce`
    c) `map`

2.  **Which function requires an import from `functools`?**
    a) `map`
    b) `filter`
    c) `reduce`

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. c
</details>