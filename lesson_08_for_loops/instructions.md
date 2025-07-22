# Lesson 08: For Loops & Iterating Over Lists

In programming, **loops** are used to execute a block of code repeatedly. The `for` loop is particularly useful for iterating over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.

## The `for` Loop

The `for` loop in Python is designed to iterate over items that are part of a collection. It executes the code block once for each item in the sequence.

**Syntax:**

```python
for item in iterable:
    # Code to execute for each item
    statement_1
    statement_2
    # ...
```

*   `item`: A temporary variable that takes on the value of each element in the `iterable` during each iteration.
*   `iterable`: Any Python object that can be iterated over (e.g., lists, strings, tuples, ranges).
*   The colon (`:`) and indentation are crucial, similar to `if` statements.

**Examples of `for` loops:**

```python
# Iterating over a list of strings
fruits = ["apple", "banana", "cherry"]
print("Iterating over fruits:")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Iterating over a string (each character)
word = "Python"
print("\nIterating over a word:")
for char in word:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n

# Iterating over a list of numbers and performing an operation
numbers = [1, 2, 3, 4, 5]
sum_numbers = 0
print("\nCalculating sum of numbers:")
for num in numbers:
    sum_numbers += num # Equivalent to: sum_numbers = sum_numbers + num
print(f"The sum is: {sum_numbers}") # Output: The sum is: 15
```

## The `range()` Function

The `range()` function is often used with `for` loops when you need to iterate a specific number of times or generate a sequence of numbers.

**Syntax:**

*   `range(stop)`: Generates numbers from `0` up to (but not including) `stop`.
*   `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.
*   `range(start, stop, step)`: Generates numbers from `start` up to (but not including) `stop`, incrementing by `step`.

**Examples with `range()`:**

```python
# Loop 5 times (from 0 to 4)
print("\nLooping 5 times:")
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Loop from 1 to 5 (inclusive)
print("\nLooping from 1 to 5:")
for i in range(1, 6):
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5

# Loop with a step (even numbers from 0 to 10)
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i)
# Output:
# 0
# 2
# 4
# 6
# 8
# 10
```

## Combining `for` loops with `if` statements

You can combine loops with conditional statements to perform actions only when certain criteria are met.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nEven numbers in the list:")
for num in numbers:
    if num % 2 == 0: # Check if the number is even
        print(num)
# Output:
# 2
# 4
# 6
# 8
# 10
```

`for` loops are incredibly powerful for processing collections of data and automating repetitive tasks.

--- 

### Quiz

1.  **What does `range(3)` generate?**
    a) `[1, 2, 3]`
    b) `[0, 1, 2]`
    c) `[0, 1, 2, 3]`

2.  **Can you loop directly over the characters in a string?**
    a) Yes
    b) No

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>