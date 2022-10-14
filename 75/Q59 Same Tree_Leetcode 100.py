"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))

p2 = TreeNode(1, left=TreeNode(2))
q2 = TreeNode(1, right=TreeNode(2))

print(is_same_tree(p1, q1))
print(is_same_tree(p2, q2))
