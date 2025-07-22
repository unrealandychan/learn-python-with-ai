# Lesson 05: Conditional Statements

In programming, **conditional statements** allow your program to make decisions. They enable your code to execute different blocks of instructions based on whether a certain condition is true or false. This is fundamental for creating dynamic and responsive programs.

## The `if` Statement

The `if` statement is the most basic conditional statement. It executes a block of code only if a specified condition is `True`.

**Syntax:**

```python
if condition:
    # Code to execute if condition is True
    statement_1
    statement_2
    # ...
```

*   The `condition` is typically a boolean expression (something that evaluates to `True` or `False`), often using comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`).
*   The colon (`:`) at the end of the `if` line is mandatory.
*   The code block under the `if` statement must be **indented**. Python uses indentation to define code blocks, unlike many other languages that use curly braces `{}`. Consistent indentation (usually 4 spaces) is crucial.

**Example:**

```python
age = 20

if age >= 18:
    print("You are old enough to vote.")

# This code will not execute because the condition (age < 10) is False
if age < 10:
    print("You are a child.")
```

## The `else` Statement

The `else` statement provides an alternative block of code to execute if the `if` condition is `False`.

**Syntax:**

```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

**Example:**

```python
weather = "rainy"

if weather == "sunny":
    print("Let's go for a walk!")
else:
    print("Maybe stay indoors and read a book.")
```

## The `elif` Statement

The `elif` (short for "else if") statement allows you to check multiple conditions sequentially. If the `if` condition is `False`, Python checks the `elif` condition. You can have multiple `elif` blocks.

**Syntax:**

```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition2 is True (and condition1 was False)
elif condition3:
    # Code if condition3 is True (and condition1, condition2 were False)
else:
    # Code if all above conditions are False
```

**Example:**

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# You can combine conditions using logical operators (and, or, not)
hour = 14
is_weekend = False

if hour < 12 and not is_weekend:
    print("Good morning, it's a weekday!")
elif hour >= 12 and hour < 18 and not is_weekend:
    print("Good afternoon, it's a weekday!")
elif is_weekend:
    print("Enjoy your weekend!")
else:
    print("Good evening!")
```

Conditional statements are fundamental to programming logic, allowing your programs to respond intelligently to different inputs and situations.

--- 

### Quiz

1.  **Which keyword is used to check for another condition if the first `if` statement is false?**
    a) `else if`
    b) `elif`
    c) `next`

2.  **Can you have an `if` statement without an `else`?**
    a) Yes
    b) No

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>