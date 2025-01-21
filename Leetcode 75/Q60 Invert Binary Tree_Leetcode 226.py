"""
Given the root of a binary tree, invert the tree, and return its root.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> TreeNode:
    if not root:
        return root

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert_tree(root.left)
    invert_tree(root.right)
    return root


root1 = TreeNode(1, TreeNode(2), TreeNode(3))

root2 = TreeNode(1, left=TreeNode(2))

print(invert_tree(root1))
print(invert_tree(root2))
