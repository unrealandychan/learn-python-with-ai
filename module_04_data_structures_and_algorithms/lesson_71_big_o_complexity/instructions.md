# Lesson 71: Big-O Notation & Complexity Analysis

## What is Big-O?

Big-O notation describes how an algorithm's **time** or **space** requirements grow as input size `n` increases. It focuses on the **worst-case** scenario and drops constants.

---

## Common Complexities (Best to Worst)

| Big-O | Name | Example |
|---|---|---|
| O(1) | Constant | dict lookup, stack push/pop |
| O(log n) | Logarithmic | binary search, BST operations |
| O(n) | Linear | linear search, single loop |
| O(n log n) | Linearithmic | merge sort, heap sort |
| O(n²) | Quadratic | nested loops, bubble sort |
| O(2ⁿ) | Exponential | naive recursion (Fibonacci) |
| O(n!) | Factorial | permutations |

---

## How to Analyse Code

### Rule 1: Drop Constants
```python
for i in range(n):     # O(n)
    pass
for i in range(n):     # O(n)
    pass
# Total: O(2n) → O(n)
```

### Rule 2: Drop Non-Dominant Terms
```python
for i in range(n):         # O(n)
    for j in range(n):     # O(n²)
        pass
# Total: O(n + n²) → O(n²)
```

### Rule 3: Different Inputs = Different Variables
```python
def func(a: list, b: list):
    for x in a:    # O(a)
        pass
    for y in b:    # O(b)
        pass
# Total: O(a + b), NOT O(n)
```

---

## Space Complexity

```python
def sum_list(lst: list) -> int:    # O(1) space — no extra memory
    total = 0
    for x in lst:
        total += x
    return total

def copy_list(lst: list) -> list:  # O(n) space — creates new list
    return [x for x in lst]
```

Recursive calls use **stack space**:
```python
def factorial(n: int) -> int:      # O(n) space — n frames on call stack
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

## Python Built-in Complexities

| Operation | List | Dict/Set |
|---|---|---|
| Access by index | O(1) | N/A |
| Search (`in`) | O(n) | O(1) |
| Insert at end | O(1) amortised | O(1) |
| Insert at start | O(n) | N/A |
| Delete by value | O(n) | O(1) |
| `sorted()` | O(n log n) | — |

**`deque.popleft()`** = O(1) vs **`list.pop(0)`** = O(n) — always use `deque` for queues!

---

## Annotating Your Own Code

Good interview practice: annotate each block.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}              # O(n) space
    for i, num in enumerate(nums):    # O(n)
        complement = target - num
        if complement in seen:        # O(1) — dict lookup
            return [seen[complement], i]
        seen[num] = i
    return []
# Time: O(n) | Space: O(n)
```

---

## Exercise

For each of the following functions, determine **Time** and **Space** complexity and explain why:

1. A function that returns whether a list contains any duplicates
2. A function that finds the longest common prefix of a list of strings
3. Binary search on a sorted list
4. Recursive Fibonacci (naive)
5. Iterative Fibonacci

Write the implementations AND annotate them with `# Time: O(?) | Space: O(?)`.
