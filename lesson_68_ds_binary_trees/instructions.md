# Lesson 68: Binary Trees & Binary Search Trees (BST)

## Binary Tree

A **binary tree** is a tree where each node has at most **two children**: `left` and `right`.

```
        5
       / \
      3   8
     / \   \
    1   4   9
```

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Tree Traversals

### Inorder (Left → Root → Right)
Visits nodes in **sorted order** for a BST.
```python
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)
```

### Preorder (Root → Left → Right)
Good for **serialising** the tree.
```python
def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)
```

### Level-Order (BFS)
Visit nodes **level by level**, using a queue.
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    return result
```

---

## Binary Search Tree (BST)

A BST maintains the invariant:
- **Left subtree** values < current node value
- **Right subtree** values > current node value

This makes **search O(log n)** on a balanced tree.

```python
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val: int) -> bool:
        curr = self.root
        while curr:
            if val == curr.val:
                return True
            curr = curr.left if val < curr.val else curr.right
        return False
```

---

## Useful Tree Problems

### Maximum Depth
```python
def max_depth(node) -> int:
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

### Is Valid BST
```python
def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')) -> bool:
    if not node:
        return True
    if not (min_val < node.val < max_val):
        return False
    return (is_valid_bst(node.left, min_val, node.val) and
            is_valid_bst(node.right, node.val, max_val))
```

---

## Exercise

Implement a `BST` class with:
1. `insert(val)` — add a value
2. `search(val) -> bool` — find a value
3. `inorder() -> list` — return all values in sorted order
4. `height() -> int` — return the tree height
5. `is_balanced() -> bool` — True if no subtree height differs by more than 1
