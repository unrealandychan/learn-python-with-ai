# Lesson 66: Stack & Queue

## Stack — Last In, First Out (LIFO)

Think of a stack of plates — you add and remove from the top.

**Operations:** push (add), pop (remove top), peek (read top), is_empty

**Use cases:** undo/redo, function call stack, DFS traversal, bracket matching

```python
class Stack:
    def __init__(self):
        self._data: list = []

    def push(self, item) -> None:
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
```

All operations are **O(1)**.

---

## Queue — First In, First Out (FIFO)

Think of a queue at a coffee shop — first person in, first served.

**Use `collections.deque`** — not a plain list! `list.pop(0)` is O(n); `deque.popleft()` is O(1).

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data: deque = deque()

    def enqueue(self, item) -> None:
        self._data.append(item)       # Add to right (back)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()   # Remove from left (front) — O(1)!

    def peek(self):
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
```

---

## Real-World: Valid Parentheses (Stack Classic)

```python
def is_valid_parens(s: str) -> bool:
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()

print(is_valid_parens("({[]})"))  # True
print(is_valid_parens("({[})"))   # False
```

---

## Deque — Double-Ended Queue

`collections.deque` supports O(1) append and pop from **both ends**.

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)    # [0, 1, 2, 3]
d.append(4)        # [0, 1, 2, 3, 4]
d.popleft()        # 0
d.pop()            # 4
```

**Sliding window maximum, BFS, and rate-limiter queues all use `deque`.**

---

## Exercise

1. Implement a `MinStack` class: standard stack with an additional `get_min()` method that returns the current minimum in O(1). Hint: maintain a second stack tracking minimums.
2. Implement a `BrowserHistory` class using two stacks: `visit(url)`, `back()`, `forward()`.
