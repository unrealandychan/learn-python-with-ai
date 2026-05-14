# Lesson 66: Solution
from collections import deque


class MinStack:
    def __init__(self):
        self._stack: list = []
        self._min_stack: list = []   # Tracks current min at each level

    def push(self, val: int) -> None:
        self._stack.append(val)
        current_min = val if not self._min_stack else min(val, self._min_stack[-1])
        self._min_stack.append(current_min)

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("pop from empty stack")
        self._min_stack.pop()
        return self._stack.pop()

    def peek(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]

    def is_empty(self) -> bool:
        return len(self._stack) == 0


class BrowserHistory:
    def __init__(self, homepage: str):
        self._back_stack: list[str] = []
        self._current: str = homepage
        self._forward_stack: list[str] = []

    def visit(self, url: str) -> None:
        self._back_stack.append(self._current)
        self._current = url
        self._forward_stack.clear()   # Visiting clears forward history

    def back(self) -> str:
        if self._back_stack:
            self._forward_stack.append(self._current)
            self._current = self._back_stack.pop()
        return self._current

    def forward(self) -> str:
        if self._forward_stack:
            self._back_stack.append(self._current)
            self._current = self._forward_stack.pop()
        return self._current


# MinStack test
ms = MinStack()
for v in [5, 3, 7, 1]:
    ms.push(v)
print(f"Min: {ms.get_min()}")   # 1
ms.pop()
print(f"Min: {ms.get_min()}")   # 3

# BrowserHistory test
bh = BrowserHistory("google.com")
bh.visit("github.com")
bh.visit("openai.com")
print(bh.back())     # github.com
print(bh.back())     # google.com
print(bh.forward())  # github.com
bh.visit("anthropic.com")
print(bh.forward())  # anthropic.com (still there — forward was cleared on visit)
