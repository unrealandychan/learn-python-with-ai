# Lesson 31: Decorators

**Decorators** are a powerful and elegant feature in Python that allow you to modify or enhance the behavior of functions or methods without permanently altering their source code. They are essentially functions that take another function as an argument, add some functionality, and then return a new function.

## Understanding Decorators

Think of a decorator as a wrapper. It wraps around another function, adding new capabilities before or after the original function executes, or even replacing it entirely. This is often used for:

*   **Logging:** Recording function calls, arguments, and return values.
*   **Timing:** Measuring how long a function takes to execute.
*   **Authentication/Authorization:** Checking user permissions before allowing a function to run.
*   **Caching:** Storing results of expensive function calls.
*   **Validation:** Validating inputs or outputs.

## Basic Decorator Structure

A decorator is a function that takes a function as input and returns a new function.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func() # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Define a simple function
def say_hello():
    print("Hello!")

# Manually apply the decorator
declared_say_hello = my_decorator(say_hello)
declared_say_hello() # Call the decorated function
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

## The `@` Syntax (Syntactic Sugar)

Python provides a convenient syntactic sugar using the `@` symbol to apply decorators. The following two pieces of code are equivalent:

```python
# Using the @ syntax
@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# Is equivalent to:
# def say_whee():
#     print("Whee!")
# say_whee = my_decorator(say_whee)
# say_whee()
```

## Decorators with Arguments

If the function being decorated takes arguments, the `wrapper` function inside the decorator must also accept those arguments and pass them to the original function.

```python
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs) # Pass arguments to original function
        print(f"{func.__name__} returned: {result}")
        return result # Return the result of the original function
    return wrapper

@log_arguments
def add(a, b):
    return a + b

@log_arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(10, 5) # Output:
# Calling add with args: (10, 5), kwargs: {}
# add returned: 15

greet("Alice", greeting="Hi") # Output:
# Calling greet with args: ('Alice',), kwargs: {'greeting': 'Hi'}
# greet returned: Hi, Alice!
```

*   `*args`: Gathers all positional arguments into a tuple.
*   `**kwargs`: Gathers all keyword arguments into a dictionary.

## Decorators with Arguments (for the Decorator Itself)

Sometimes, you want to pass arguments to the decorator itself. This requires an extra layer of nesting.

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_something(word):
    print(word)

say_something("Python")
# Output:
# Python
# Python
# Python
```

Decorators are a powerful and elegant way to extend the functionality of functions and methods in Python, leading to cleaner and more modular code.

--- 

### Quiz

1.  **What is the primary purpose of a decorator?**
    a) To delete a function.
    b) To modify or enhance a function without changing its source code.
    c) To create a new class.

2.  **What symbol is commonly used for applying a decorator?**
    a) `#`
    b) `&`
    c) `@`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
</details>