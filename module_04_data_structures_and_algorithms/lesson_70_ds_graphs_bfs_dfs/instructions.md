# Lesson 70: Graphs — BFS & DFS

## What is a Graph?

A **graph** is a set of **nodes (vertices)** connected by **edges**.

- **Directed vs Undirected:** edges have direction or not
- **Weighted vs Unweighted:** edges have costs or not
- **Cyclic vs Acyclic:** may or may not have cycles

## Representing Graphs

### Adjacency List (most common in interviews)

```python
# Undirected graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}
```

### Adjacency Matrix (dense graphs)

```python
# 4 nodes, edge matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
```

---

## BFS — Breadth-First Search

Explores level by level. Uses a **queue**. Finds **shortest path** in unweighted graphs.

```python
from collections import deque

def bfs(graph: dict, start: str) -> list:
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                queue.append(neighbour)
    return order
```

**Shortest path with BFS:**

```python
def shortest_path(graph, start, end) -> int | None:
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))
    return None  # No path
```

---

## DFS — Depth-First Search

Explores as deep as possible first. Uses a **stack** (or recursion). Used for cycle detection, topological sort, connected components.

### Recursive DFS

```python
def dfs(graph: dict, node: str, visited: set = None) -> list:
    if visited is None:
        visited = set()
    visited.add(node)
    result = [node]
    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            result.extend(dfs(graph, neighbour, visited))
    return result
```

### Iterative DFS

```python
def dfs_iterative(graph: dict, start: str) -> list:
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbour in reversed(graph.get(node, [])):
            stack.append(neighbour)
    return order
```

---

## Cycle Detection (Directed Graph)

```python
def has_cycle(graph: dict) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY:   # Back edge — cycle!
                return True
            if color[nb] == WHITE and dfs(nb):
                return True
        color[node] = BLACK
        return False

    return any(dfs(node) for node in graph if color[node] == WHITE)
```

---

## Exercise

Build a `Graph` class for an **undirected, unweighted** graph:

1. `add_edge(u, v)` — adds a bidirectional edge
2. `bfs(start) -> list` — BFS traversal order
3. `dfs(start) -> list` — DFS traversal order (iterative)
4. `shortest_path(start, end) -> int | None` — BFS shortest path length
5. `is_connected() -> bool` — True if all nodes reachable from any node
