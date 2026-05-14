# Lesson 09: While Loops

In addition to `for` loops, Python also has **`while` loops**. A `while` loop is used to execute a block of code repeatedly as long as a specified condition remains `True`.

## The `while` Loop

The `while` loop is ideal when you don't know in advance how many times you need to loop. It continues to execute as long as its condition is met.

**Syntax:**

```python
while condition:
    # Code to execute as long as the condition is True
    statement_1
    statement_2
    # ...
```

*   The `condition` is evaluated at the beginning of each iteration.
*   If the `condition` is `True`, the code block inside the loop is executed.
*   If the `condition` becomes `False`, the loop terminates, and execution continues with the code immediately after the loop.

**Important:** You must ensure that the condition eventually becomes `False` inside the loop, otherwise, you will create an **infinite loop**, which will run forever (or until your program runs out of memory or you manually stop it).

**Example:**

```python
# Counting up to 5
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count to eventually make the condition False
# Output:
# 1
# 2
# 3
# 4
# 5

# Simulating a simple game loop
player_health = 100
while player_health > 0:
    print(f"Player health: {player_health}")
    damage = 10 # Simulate taking damage
    player_health -= damage
    if player_health <= 0:
        print("Game Over!")
```

## The `break` Statement

The `break` statement is used to **exit a loop immediately**, regardless of whether the loop's condition is still `True`. When `break` is encountered, the program jumps to the statement immediately following the loop.

**Example:**

```python
i = 1
while i <= 10:
    print(i)
    if i == 5:
        print("Breaking loop at 5")
        break  # Exit the loop when i is 5
    i += 1
print("Loop finished.")
# Output:
# 1
# 2
# 3
# 4
# 5
# Breaking loop at 5
# Loop finished.
```

## The `continue` Statement

The `continue` statement is used to **skip the rest of the current iteration** of the loop and move to the next iteration. The loop's condition is re-evaluated.

**Example:**

```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 != 0: # If number is odd
        continue     # Skip to the next iteration
    print(num)       # Only even numbers will be printed
# Output:
# 2
# 4
# 6
```

`while` loops are powerful for scenarios where the number of iterations is not fixed, and `break` and `continue` provide fine-grained control over loop execution.

--- 

### Quiz

1.  **What is a potential risk with `while` loops that is not present with `for` loops over a list?**
    a) They are slower.
    b) They can result in an infinite loop if the condition is always true.
    c) They cannot be stopped.

2.  **What is `i += 1` a shorthand for?**
    a) `i = i + 1`
    b) `i = 1`
    c) `i = i + i`

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. a
</details>