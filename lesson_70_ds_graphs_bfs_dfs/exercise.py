# Lesson 70: Exercise — Graphs BFS & DFS
from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self._adj = defaultdict(list)

    # TODO: add_edge(u, v) — undirected edge

    # TODO: bfs(start: str) -> list — return traversal order

    # TODO: dfs(start: str) -> list — iterative, return traversal order

    # TODO: shortest_path(start: str, end: str) -> int | None
    #   Return number of edges in shortest path, None if unreachable

    # TODO: is_connected() -> bool
    #   All nodes must be reachable from the first node added


# Test
# g = Graph()
# for u, v in [("A","B"), ("A","C"), ("B","D"), ("C","D"), ("D","E")]:
#     g.add_edge(u, v)
# print(g.bfs("A"))              # A B C D E (order may vary by adj order)
# print(g.dfs("A"))              # A B D C E (or similar)
# print(g.shortest_path("A","E"))  # 3
# print(g.shortest_path("A","Z"))  # None
# print(g.is_connected())        # True
