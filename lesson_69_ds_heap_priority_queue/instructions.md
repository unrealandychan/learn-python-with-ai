# Lesson 69: Heap & Priority Queue

## What is a Heap?

A **heap** is a complete binary tree where:
- **Min-heap:** Parent ≤ children (root = smallest element)
- **Max-heap:** Parent ≥ children (root = largest element)

Python's `heapq` module implements a **min-heap**.

```
Min-heap:
        1
       / \
      3   2
     / \
    5   4
```

---

## Python's heapq

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heap[0])               # 1 — peek minimum (don't pop!)
print(heapq.heappop(heap))   # 1 — pop minimum
print(heap)                  # [2, 3]

# Build heap from list — O(n)
data = [5, 3, 8, 1, 9]
heapq.heapify(data)
print(data[0])               # 1
```

**Max-heap trick:** negate values.
```python
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))  # 5 — largest first
```

---

## Priority Queue

`heapq` supports tuple comparison — use `(priority, item)` for a priority queue:

```python
import heapq

pq = []
heapq.heappush(pq, (3, "low priority task"))
heapq.heappush(pq, (1, "urgent task"))
heapq.heappush(pq, (2, "medium task"))

while pq:
    priority, task = heapq.heappop(pq)
    print(f"[{priority}] {task}")
# [1] urgent task
# [2] medium task
# [3] low priority task
```

**Or use `queue.PriorityQueue`** for thread-safe priority queues.

---

## Classic Heap Problems

### Top K Elements

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    from collections import Counter
    count = Counter(nums)
    # Use min-heap of size k — heapq.nlargest is simpler
    return heapq.nlargest(k, count.keys(), key=count.get)

print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]
```

### K Closest Points to Origin

```python
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(heap, (dist, x, y))
    return [[x, y] for _, x, y in heapq.nsmallest(k, heap)]
```

### Merge K Sorted Lists

```python
def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    return result
```

---

## Exercise

1. Implement a `MedianFinder` class:
   - `add_num(num)` — add a number to the data stream
   - `find_median() -> float` — return current median in O(log n) add, O(1) median
   - Hint: use two heaps — a max-heap for lower half and a min-heap for upper half

2. Write `k_most_frequent(words: list[str], k: int) -> list[str]`
