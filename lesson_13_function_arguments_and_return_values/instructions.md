# Lesson 13: Function Arguments & Return Values

In the previous lesson, you learned how to define and call basic functions. Now, let's make functions more powerful by allowing them to accept **arguments** (inputs) and produce **return values** (outputs).

## Function Arguments (Parameters)

**Arguments** are pieces of information that you can pass into a function when you call it. These arguments are received by the function as **parameters**.

Parameters are listed inside the parentheses in the function definition, separated by commas.

**Syntax:**

```python
def function_name(parameter1, parameter2, ...):
    # Use parameter1, parameter2 in the function body
    pass
```

**Examples:**

```python
# Function that takes one argument: name
def greet(name):
    print(f"Hello, {name}!")

# Call the function with different arguments
greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!

# Function that takes multiple arguments: num1, num2
def add_numbers(num1, num2):
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}.")

# Call the function with different numerical arguments
add_numbers(10, 5)   # Output: The sum of 10 and 5 is 15.
add_numbers(1.5, 2.5) # Output: The sum of 1.5 and 2.5 is 4.0.
```

### Default Parameter Values

You can provide default values for parameters. If an argument is not provided for that parameter when the function is called, the default value will be used.

```python
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()        # Output: Hello, Guest!
greet_with_default("Charlie") # Output: Hello, Charlie!
```

## Function Return Values

Functions don't just have to print things; they can also **return** values. The `return` statement is used to send a value back to the part of the code that called the function. When a `return` statement is executed, the function immediately stops, and the returned value is passed back.

**Syntax:**

```python
def function_name(parameters):
    # ... calculations ...
    return value
```

**Examples:**

```python
# Function that returns the sum of two numbers
def multiply_numbers(num1, num2):
    product = num1 * num2
    return product # The function sends back the value of 'product'

# Call the function and store the returned value in a variable
result1 = multiply_numbers(4, 6)
print(f"The product is: {result1}") # Output: The product is: 24

result2 = multiply_numbers(7, 2)
print(f"Another product: {result2}") # Output: Another product: 14

# You can also use the returned value directly
print(f"Directly using return: {multiply_numbers(3, 3)}") # Output: Directly using return: 9

# Function that returns multiple values (as a tuple)
def get_user_info():
    name = "Diana"
    age = 28
    return name, age # Returns a tuple (name, age)

user_name, user_age = get_user_info() # Unpack the tuple into two variables
print(f"User: {user_name}, Age: {user_age}") # Output: User: Diana, Age: 28
```

Functions with arguments and return values are incredibly powerful, allowing you to create modular, reusable, and flexible code that can process inputs and produce outputs.

--- 

### Quiz

1.  **What is the purpose of the `return` keyword?**
    a) To print a value.
    b) To send a value back from a function.
    c) To stop the function.

2.  **Can a function take multiple arguments?**
    a) Yes
    b) No

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>