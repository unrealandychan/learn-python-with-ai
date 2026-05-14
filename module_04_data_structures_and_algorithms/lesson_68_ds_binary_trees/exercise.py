# Lesson 68: Exercise — Binary Trees & BST
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    # TODO: insert(val) — recursive helper _insert(node, val) -> TreeNode

    # TODO: search(val) -> bool — iterative

    # TODO: inorder() -> list — returns sorted list of all values

    # TODO: height() -> int — recursive, 0 for empty tree

    # TODO: is_balanced() -> bool
    #   Hint: write a helper that returns height or -1 if subtree is unbalanced


# Test
# bst = BST()
# for v in [5, 3, 8, 1, 4, 9]:
#     bst.insert(v)
# print(bst.inorder())         # [1, 3, 4, 5, 8, 9]
# print(bst.search(4))         # True
# print(bst.search(7))         # False
# print(bst.height())          # 3
# print(bst.is_balanced())     # True
