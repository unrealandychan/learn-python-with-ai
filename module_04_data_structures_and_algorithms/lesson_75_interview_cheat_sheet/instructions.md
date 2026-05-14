# Lesson 75: Interview Cheat Sheet

A rapid-reference for coding interviews. Review this the night before.

---

## OOP Quick Reference

| Concept | Python Syntax | When to Use |
|---|---|---|
| Abstract class | `from abc import ABC, abstractmethod` | Define a contract all subclasses must follow |
| Property | `@property` + `@x.setter` | Validation / computed attributes |
| Dataclass | `@dataclass` | Data containers without boilerplate |
| MRO | `ClassName.__mro__` | Debug multiple inheritance order |
| Singleton | `__new__` pattern | Global config, connection pool |
| Factory | `dict` of classes | Create objects without knowing type |
| Strategy | Swap object with same interface | Pluggable algorithms |
| Observer | `subscribe()` + `emit()` | Event-driven systems |

---

## Data Structures Quick Reference

| Structure | Python | Access | Insert | Delete | Search |
|---|---|---|---|---|---|
| Array | `list` | O(1) | O(1) end / O(n) mid | O(n) | O(n) |
| Hash Map | `dict` | O(1) | O(1) | O(1) | O(1) |
| Hash Set | `set` | O(1) | O(1) | O(1) | O(1) |
| Stack | `list` + `.append/.pop` | O(1) | O(1) | O(1) | O(n) |
| Queue | `collections.deque` | O(1) | O(1) | O(1) | O(n) |
| Linked List | Custom `Node` class | O(n) | O(1) | O(1) | O(n) |
| BST | Custom | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | `heapq` | O(1) min | O(log n) | O(log n) | O(n) |
| Graph | `dict[list]` | O(1) | O(1) | O(V+E) BFS/DFS | — |

---

## Algorithm Patterns

| Pattern | Use When | Key Tool |
|---|---|---|
| Two Pointers | Sorted array, palindrome | `left, right = 0, len-1` |
| Sliding Window | Subarray/substring, fixed/variable window | `deque` or two pointers |
| Fast & Slow Pointers | Linked list cycle, find middle | `slow, fast` |
| BFS | Shortest path, level-order | `collections.deque` |
| DFS | Explore all paths, cycle detection | Stack or recursion |
| Binary Search | Sorted input, O(log n) needed | `left, right, mid` |
| Prefix Sum | Subarray sum queries | `prefix[i] = prefix[i-1] + nums[i]` |
| Dynamic Programming | Overlapping subproblems | `dp` array + recurrence |
| Heap | Top-K, streaming median | `heapq` (min) / negate for max |

---

## Python Gotchas in Interviews

```python
# Mutable default argument bug
def append_to(item, lst=[]):   # WRONG — shared across calls!
    lst.append(item)
    return lst

def append_to(item, lst=None): # CORRECT
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Integer division
7 / 2    # 3.5  (float)
7 // 2   # 3    (int)

# Negative modulo
-7 % 3   # 2    (Python always non-negative mod)

# List multiplication — shallow copy!
matrix = [[0] * 3] * 3    # WRONG — all rows are same object
matrix = [[0] * 3 for _ in range(3)]  # CORRECT

# String immutability — use list for character manipulation
chars = list(s)
# ... modify ...
result = "".join(chars)
```

---

## Complexity Cheat Sheet

```
O(1)        → hash lookup, stack push/pop, heap peek
O(log n)    → binary search, BST ops, heap push/pop
O(n)        → linear scan, BFS/DFS
O(n log n)  → sorting, heap sort
O(n²)       → nested loops, bubble/insertion sort
O(2ⁿ)       → naive recursion (Fibonacci, subsets)
```

---

## Interview Framework

1. **Clarify** — ask about constraints, edge cases, input types
2. **Examples** — walk through 2-3 examples including edge cases
3. **Brute Force** — state the naive solution + its complexity
4. **Optimise** — think about better approaches (hash map? binary search? DP?)
5. **Code** — write clean, readable code; name variables well
6. **Test** — trace through your code with examples; find bugs
7. **Complexity** — state time and space complexity

---

## Collections Module Cheat Sheet

```python
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

Counter("abracadabra")           # {'a':5,'b':2,'r':2,'c':1,'d':1}
Counter.most_common(3)           # Top 3
defaultdict(list)                # Missing key returns []
defaultdict(int)                 # Missing key returns 0
deque.appendleft(x)              # O(1)
deque.popleft()                  # O(1)
OrderedDict.move_to_end(key)     # For LRU cache
```
