# Lesson 68: Solution
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root: TreeNode | None = None

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

    def inorder(self) -> list:
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def height(self) -> int:
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def is_balanced(self) -> bool:
        def _check(node):
            # Returns height if balanced, -1 if not
            if not node:
                return 0
            left = _check(node.left)
            if left == -1:
                return -1
            right = _check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return _check(self.root) != -1


bst = BST()
for v in [5, 3, 8, 1, 4, 9]:
    bst.insert(v)
print(bst.inorder())         # [1, 3, 4, 5, 8, 9]
print(bst.search(4))         # True
print(bst.search(7))         # False
print(bst.height())          # 3
print(bst.is_balanced())     # True
