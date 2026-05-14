# Lesson 70: Solution
from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self._adj: dict[str, list] = defaultdict(list)
        self._nodes: set = set()

    def add_edge(self, u: str, v: str) -> None:
        self._adj[u].append(v)
        self._adj[v].append(u)
        self._nodes.update([u, v])

    def bfs(self, start: str) -> list:
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nb in self._adj[node]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        return order

    def dfs(self, start: str) -> list:
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for nb in reversed(self._adj[node]):
                if nb not in visited:
                    stack.append(nb)
        return order

    def shortest_path(self, start: str, end: str):
        if start == end:
            return 0
        visited = {start}
        queue = deque([(start, 0)])
        while queue:
            node, dist = queue.popleft()
            for nb in self._adj[node]:
                if nb == end:
                    return dist + 1
                if nb not in visited:
                    visited.add(nb)
                    queue.append((nb, dist + 1))
        return None

    def is_connected(self) -> bool:
        if not self._nodes:
            return True
        start = next(iter(self._nodes))
        return len(self.bfs(start)) == len(self._nodes)


g = Graph()
for u, v in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]:
    g.add_edge(u, v)
print(g.bfs("A"))                  # ['A', 'B', 'C', 'D', 'E']
print(g.dfs("A"))                  # ['A', 'B', 'D', 'C', 'E'] or similar
print(g.shortest_path("A", "E"))   # 3
print(g.shortest_path("A", "Z"))   # None
print(g.is_connected())            # True
