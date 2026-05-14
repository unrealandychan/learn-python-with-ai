# Lesson 75: Quick Reference Implementations

from collections import deque, OrderedDict


# LRU Cache
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# MinStack
class MinStack:
    def __init__(self):
        self._s, self._m = [], []

    def push(self, v):
        self._s.append(v)
        self._m.append(v if not self._m else min(v, self._m[-1]))

    def pop(self):
        self._m.pop(); return self._s.pop()

    def get_min(self): return self._m[-1]


# Valid parentheses
def is_valid(s: str) -> bool:
    stack, pairs = [], {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "([{": stack.append(c)
        elif not stack or stack.pop() != pairs[c]: return False
    return not stack


# Binary search
def binary_search(arr, target) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target: return m
        elif arr[m] < target: l = m + 1
        else: r = m - 1
    return -1


# BFS shortest path
def bfs_shortest(graph, start, end):
    q, visited = deque([(start, 0)]), {start}
    while q:
        node, dist = q.popleft()
        if node == end: return dist
        for nb in graph.get(node, []):
            if nb not in visited:
                visited.add(nb); q.append((nb, dist + 1))
    return -1


print("All reference implementations ready!")
