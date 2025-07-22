# Lesson 30: Generators and the `yield` Keyword

In Python, **generators** are a special type of iterator that allow you to iterate over a sequence of values without creating the entire sequence in memory at once. This makes them incredibly memory-efficient, especially when dealing with very large or infinite sequences.

## What are Generators?

Generators are functions that behave like iterators. They are defined like normal functions, but instead of using the `return` statement to return a value and terminate, they use the **`yield` keyword**.

When a generator function is called, it doesn't execute the function body immediately. Instead, it returns a **generator object**. The code in the function only runs when `next()` is called on the generator object (either explicitly or implicitly by a `for` loop).

## The `yield` Keyword

*   When `yield` is encountered, the function's execution is paused, and the value specified after `yield` is returned.
*   The state of the function (local variables, instruction pointer) is saved.
*   When `next()` is called again, the function resumes from where it left off.
*   If the function finishes without another `yield` or reaches a `return` statement, a `StopIteration` exception is raised, signaling the end of the sequence.

**Example: Simple Generator**

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# Iterate through the generator using next()
print(next(gen)) # Output: 1
print(next(gen)) # Output: 2
print(next(gen)) # Output: 3

# After all yields are exhausted, calling next() will raise StopIteration
# print(next(gen)) # Uncomment to see StopIteration error

# More commonly, generators are used with for loops
print("\nUsing for loop with generator:")
for value in simple_generator():
    print(value)
# Output:
# 1
# 2
# 3
```

## Why Use Generators?

1.  **Memory Efficiency:** They produce items one at a time, only when requested. This is crucial for large datasets that wouldn't fit into memory if stored as a complete list.
2.  **Lazy Evaluation:** Values are generated on the fly, only when needed. This can save computation time if not all values in a sequence are required.
3.  **Infinite Sequences:** You can create generators for potentially infinite sequences (e.g., all prime numbers) without running out of memory.
4.  **Readability:** Often, generator functions are more readable and cleaner than implementing a custom iterator class.

**Example: Fibonacci Sequence Generator**

```python
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Generate the first 10 Fibonacci numbers
print("\nFirst 10 Fibonacci numbers:")
for num in fibonacci_generator(10):
    print(num)
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
```

## Generator Expressions

Similar to list comprehensions, you can create simple generators using **generator expressions**. They use parentheses `()` instead of square brackets `[]`.

**Syntax:**

```python
gen_obj = (expression for item in iterable if condition)
```

**Example:**

```python
# Generator expression for squares
squares_gen = (x**2 for x in range(10))

print(type(squares_gen)) # Output: <class 'generator'>

print(next(squares_gen)) # Output: 0
print(next(squares_gen)) # Output: 1

# You can also iterate over it
for sq in squares_gen:
    print(sq)
```

Generators are a powerful tool for handling large data streams and creating efficient, iterable sequences in Python.

--- 

### Quiz

1.  **What is the main advantage of using a generator?**
    a) They are faster than lists.
    b) They are more memory-efficient for large sequences.
    c) They can be modified after creation.

2.  **Which keyword is used to produce a value from a generator?**
    a) `return`
    b) `generate`
    c) `yield`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
</details>