# Lesson 72: Recursion & Dynamic Programming

## Recursion

A function that **calls itself** with a smaller input, until it reaches a **base case**.

```python
def factorial(n: int) -> int:
    if n <= 1:        # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case
```

Every recursive solution needs:
1. **Base case** — when to stop
2. **Recursive case** — how to reduce the problem

### Recursive Tree Traversal

```python
def sum_tree(node) -> int:
    if not node:
        return 0
    return node.val + sum_tree(node.left) + sum_tree(node.right)
```

---

## Dynamic Programming (DP)

DP solves problems by breaking them into **overlapping subproblems** and storing results to avoid recomputation.

Two approaches:

### Top-Down (Memoisation)

```python
def fib(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

Or with `functools.lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

### Bottom-Up (Tabulation)

```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

---

## Classic DP Problems

### Coin Change (Minimum Coins)

```python
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 5, 10, 25], 36))  # 3 (25+10+1)
```

### Longest Common Subsequence

```python
def lcs(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### 0/1 Knapsack

```python
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    return dp[n][capacity]
```

---

## Exercise

1. Implement `climb_stairs(n: int) -> int`: count ways to climb n stairs (1 or 2 steps at a time). Use DP.

2. Implement `max_subarray(nums: list[int]) -> int`: Kadane's algorithm — find the maximum sum of a contiguous subarray.

3. Implement `word_break(s: str, word_dict: list[str]) -> bool`: can `s` be segmented into words from `word_dict`?
