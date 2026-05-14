# Lesson 27: Dictionary and Set Comprehensions

Just like list comprehensions, Python offers similar concise syntax for creating **dictionaries** and **sets** using comprehensions. These are powerful tools for building these data structures efficiently and expressively.

## Dictionary Comprehensions

**Dictionary comprehensions** allow you to create new dictionaries from an iterable, applying an expression to each item to form key-value pairs.

**Syntax:**

```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```

*   `key_expression`: The expression that determines the key for each item.
*   `value_expression`: The expression that determines the value for each item.
*   `item`: The variable representing each element from the `iterable`.
*   `iterable`: The source sequence.
*   `if condition` (optional): A filter to include items based on a condition.

**Example: Creating a dictionary of squares**

```python
# Using a for loop
squares_dict_loop = {}
for num in range(1, 6):
    squares_dict_loop[num] = num**2
print(squares_dict_loop) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Using a dictionary comprehension
squares_dict_comp = {num: num**2 for num in range(1, 6)}
print(squares_dict_comp) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Example: Filtering and transforming a dictionary**

```python
original_prices = {'apple': 1.20, 'banana': 0.80, 'cherry': 2.50, 'date': 1.50}

# Create a new dictionary with items priced over 1.00, with a 10% discount
discounted_prices = {fruit: price * 0.90 for fruit, price in original_prices.items() if price > 1.00}
print(discounted_prices) # Output: {'apple': 1.08, 'cherry': 2.25, 'date': 1.35}
```

## Set Comprehensions

**Set comprehensions** allow you to create new sets from an iterable, applying an expression to each item. Remember that sets only store unique elements, so any duplicates generated will be automatically removed.

**Syntax:**

```python
new_set = {expression for item in iterable if condition}
```

*   `expression`: The operation to perform on each `item`.
*   `item`: The variable representing each element from the `iterable`.
*   `iterable`: The source sequence.
*   `if condition` (optional): A filter to include items based on a condition.

**Example: Creating a set of unique characters**

```python
sentence = "hello world"

# Using a for loop
unique_chars_loop = set()
for char in sentence:
    unique_chars_loop.add(char)
print(unique_chars_loop) # Output: {' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w'}

# Using a set comprehension
unique_chars_comp = {char for char in sentence}
print(unique_chars_comp) # Output: {' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w'}
```

**Example: Filtering and transforming for a set**

```python
numbers = [1, 2, 2, 3, 4, 4, 5, 6]

# Get unique even numbers
unique_even_numbers = {num for num in numbers if num % 2 == 0}
print(unique_even_numbers) # Output: {2, 4, 6}
```

Dictionary and set comprehensions are powerful, Pythonic ways to construct these data structures, often leading to more readable and efficient code than traditional loops.

--- 

### Quiz

1.  **What kind of brackets are used for dictionary and set comprehensions?**
    a) `[]`
    b) `()`
    c) `{}`

2.  **What is the key difference in the syntax between a dictionary and a set comprehension?**
    a) Dictionary comprehensions have a colon (`:`) to separate keys and values.
    b) Set comprehensions are faster.
    c) There is no difference.

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. a
</details>