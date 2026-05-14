# Lesson 14: Variable Scope (Local vs. Global)

In programming, **scope** refers to the region of a program where a variable is accessible. Understanding variable scope is crucial to avoid unexpected behavior and bugs in your code.

Python primarily has two types of scope:

1.  **Local Scope**
2.  **Global Scope**

## Local Scope

A variable created inside a function is said to be in that function's **local scope**. It can only be accessed from within that function. Once the function finishes execution, the local variables are destroyed.

**Example:**

```python
def my_function():
    local_variable = 10 # This variable is local to my_function
    print(f"Inside the function, local_variable is: {local_variable}")

my_function()

# Trying to access local_variable outside the function will cause an error
# print(local_variable) # This would raise a NameError
```

Each time a function is called, a new local scope is created for that call. This means variables in one function's local scope do not interfere with variables in another function's local scope, even if they have the same name.

```python
def func_a():
    x = 10 # Local to func_a
    print(f"Inside func_a, x is: {x}")

def func_b():
    x = 20 # Local to func_b (different from x in func_a)
    print(f"Inside func_b, x is: {x}")

func_a()
func_b()
```

## Global Scope

A variable created outside of any function (at the top level of a script) is a **global variable** and belongs to the **global scope**. Global variables can be accessed from anywhere in the program, both inside and outside functions.

**Example:**

```python
global_message = "Hello from global scope!" # This is a global variable

def display_global_message():
    print(global_message) # Accessing the global variable

print(global_message) # Output: Hello from global scope!
display_global_message()
# Output: Hello from global scope!
```

### Modifying Global Variables Inside a Function

By default, if you try to assign a new value to a variable inside a function that has the same name as a global variable, Python will create a *new local variable* with that name, rather than modifying the global one. This is to prevent accidental modification of global state.

**Example (Incorrect way to modify global):**

```python
counter = 0 # Global variable

def increment_counter():
    counter = 1 # This creates a NEW LOCAL variable named 'counter'
    print(f"Inside function (local counter): {counter}")

increment_counter()
print(f"Outside function (global counter): {counter}")
# Output:
# Inside function (local counter): 1
# Outside function (global counter): 0 (The global variable was NOT changed)
```

To explicitly modify a global variable from within a function, you must use the `global` keyword.

**Example (Correct way to modify global):**

```python
counter = 0 # Global variable

def increment_global_counter():
    global counter # Declare that we intend to modify the GLOBAL 'counter'
    counter += 1
    print(f"Inside function (global counter): {counter}")

increment_global_counter()
print(f"Outside function (global counter): {counter}")
# Output:
# Inside function (global counter): 1
# Outside function (global counter): 1 (The global variable WAS changed)
```

While `global` keyword allows modification, it's generally good practice to minimize the use of global variables, especially for modification, as it can make code harder to understand and debug. Passing values as arguments and returning them is often a cleaner approach.

--- 

### Quiz

1.  **Can you access a local variable outside of the function where it was created?**
    a) Yes
    b) No

2.  **What keyword do you use to modify a global variable inside a function?**
    a) `global`
    b) `modify`
    c) `var`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>