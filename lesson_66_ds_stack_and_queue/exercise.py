# Lesson 66: Exercise — Stack & Queue
from collections import deque

# TODO: MinStack
# Methods: push(val), pop(), peek(), get_min()
# get_min() must be O(1)
# Hint: use a second stack (_min_stack) that tracks the current minimum

# TODO: BrowserHistory
# __init__(homepage: str)
# visit(url: str) — navigate to new page, clear forward history
# back() -> str — go back one page (return current url, or stay if at start)
# forward() -> str — go forward one page (return current url, or stay if at end)

# Test MinStack
# ms = MinStack()
# ms.push(5)
# ms.push(3)
# ms.push(7)
# ms.push(1)
# print(ms.get_min())  # 1
# ms.pop()
# print(ms.get_min())  # 3

# Test BrowserHistory
# bh = BrowserHistory("google.com")
# bh.visit("github.com")
# bh.visit("openai.com")
# print(bh.back())      # github.com
# print(bh.back())      # google.com
# print(bh.forward())   # github.com
# bh.visit("anthropic.com")
# print(bh.forward())   # anthropic.com (forward cleared)
