# Lesson 67: Linked Lists

A **linked list** is a sequence of nodes where each node stores a value and a pointer to the next node.

```
[3] -> [1] -> [4] -> [1] -> [5] -> None
```

Unlike a Python list (backed by an array), a linked list:
- **O(1) insert/delete** at a known position
- **O(n) access** by index (no random access)

---

## Node and LinkedList Classes

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self._size: int = 0

    def append(self, val) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def prepend(self, val) -> None:
        self.head = Node(val, self.head)
        self._size += 1

    def delete(self, val) -> bool:
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next
            self._size -= 1
            return True
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                self._size -= 1
                return True
            curr = curr.next
        return False

    def to_list(self) -> list:
        result, curr = [], self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
```

---

## Classic Algorithms

### Reverse a Linked List (Iterative)

```python
def reverse(self) -> None:
    prev, curr = None, self.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    self.head = prev
```

### Detect a Cycle (Floyd's Algorithm)

```python
def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

### Find Middle Node (Slow/Fast Pointers)

```python
def find_middle(head: Node) -> Node:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

---

## Doubly Linked List

Each node has both `next` and `prev` pointers:

```python
class DNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```

Used internally by Python's `collections.deque` and for implementing LRU Cache.

---

## Exercise

Implement `LinkedList` with:
1. `append(val)`, `prepend(val)`, `delete(val)`, `to_list()`
2. `reverse()` — in-place reversal
3. `find_middle()` — returns the middle node's value
4. `remove_duplicates()` — remove all duplicate values, keep first occurrence
