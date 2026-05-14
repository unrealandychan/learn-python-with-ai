# Lesson 03: Basic Operators

In this lesson, you will learn about the fundamental **operators** in Python. Operators are special symbols that perform operations on one or more values (operands).

## 1. Arithmetic Operators

These operators are used to perform mathematical calculations.

*   `+` (Addition): Adds two operands.
    ```python
    result = 10 + 5
    print(result)  # Output: 15
    ```

*   `-` (Subtraction): Subtracts the second operand from the first.
    ```python
    result = 10 - 5
    print(result)  # Output: 5
    ```

*   `*` (Multiplication): Multiplies two operands.
    ```python
    result = 10 * 5
    print(result)  # Output: 50
    ```

*   `/` (Division): Divides the first operand by the second. The result is always a float.
    ```python
    result = 10 / 5
    print(result)  # Output: 2.0
    result = 7 / 2
    print(result)  # Output: 3.5
    ```

*   `%` (Modulus): Returns the remainder of a division.
    ```python
    result = 10 % 3
    print(result)  # Output: 1 (because 10 divided by 3 is 3 with a remainder of 1)
    ```

*   `**` (Exponentiation): Raises the first operand to the power of the second.
    ```python
    result = 2 ** 3
    print(result)  # Output: 8 (2 * 2 * 2)
    ```

*   `//` (Floor Division): Divides the first operand by the second and returns the integer part of the quotient (discards the fractional part).
    ```python
    result = 7 // 2
    print(result)  # Output: 3
    result = 10 // 3
    print(result)  # Output: 3
    ```

## 2. Comparison (Relational) Operators

These operators are used to compare two values and always return a boolean result (`True` or `False`).

*   `==` (Equal to): Returns `True` if both operands are equal.
    ```python
    print(5 == 5)   # Output: True
    print(5 == 10)  # Output: False
    ```

*   `!=` (Not equal to): Returns `True` if operands are not equal.
    ```python
    print(5 != 10)  # Output: True
    print(5 != 5)   # Output: False
    ```

*   `>` (Greater than): Returns `True` if the first operand is greater than the second.
    ```python
    print(10 > 5)   # Output: True
    print(5 > 10)   # Output: False
    ```

*   `<` (Less than): Returns `True` if the first operand is less than the second.
    ```python
    print(5 < 10)   # Output: True
    print(10 < 5)   # Output: False
    ```

*   `>=` (Greater than or equal to): Returns `True` if the first operand is greater than or equal to the second.
    ```python
    print(10 >= 10) # Output: True
    print(5 >= 10)  # Output: False
    ```

*   `<=` (Less than or equal to): Returns `True` if the first operand is less than or equal to the second.
    ```python
    print(5 <= 5)   # Output: True
    print(10 <= 5)  # Output: False
    ```

## 3. Logical Operators

These operators are used to combine conditional statements and evaluate boolean expressions.

*   `and`: Returns `True` if both statements are `True`.
    ```python
    print(True and True)    # Output: True
    print(True and False)   # Output: False
    ```

*   `or`: Returns `True` if at least one of the statements is `True`.
    ```python
    print(True or False)    # Output: True
    print(False or False)   # Output: False
    ```

*   `not`: Reverses the logical state of its operand. If a condition is `True`, `not` makes it `False`, and vice versa.
    ```python
    print(not True)     # Output: False
    print(not False)    # Output: True
    ```

Understanding these basic operators is crucial for performing calculations, making comparisons, and building logical conditions in your Python programs.

--- 

### Quiz

1.  **What is the result of `10 % 3`?**
    a) 3
    b) 1
    c) 0

2.  **Which operator checks for equality?**
    a) `=`
    b) `==`
    c) `!=`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>