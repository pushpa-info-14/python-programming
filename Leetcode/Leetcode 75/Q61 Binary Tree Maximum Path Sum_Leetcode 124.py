"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge connecting them. A node can only appear in the sequence at most once. Note that the path
does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum_my(root: Optional[TreeNode]) -> int:
    results = [root.val]

    def dfs(root: TreeNode):
        if not root:
            return 0

        left_max = dfs(root.left)
        right_max = dfs(root.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        results[0] = max(results[0], root.val + left_max + right_max)
        return root.val + max(left_max, right_max)

    dfs(root)
    return results[0]


root1 = TreeNode(1, TreeNode(2), TreeNode(3))

node1 = TreeNode(20, TreeNode(15), TreeNode(7))
root2 = TreeNode(-10, TreeNode(9), node1)

root3 = TreeNode(2, TreeNode(-1), TreeNode(-2))

root4 = TreeNode(-3)

root5 = TreeNode(1, TreeNode(-2), TreeNode(3))

node1 = TreeNode(20, TreeNode(-15), TreeNode(-7))
root6 = TreeNode(-10, TreeNode(9), node1)

root7 = TreeNode(1, TreeNode(2))
root8 = TreeNode(0)

print(max_path_sum_my(root1))
print(max_path_sum_my(root2))
print(max_path_sum_my(root3))
print(max_path_sum_my(root4))
print(max_path_sum_my(root5))
print(max_path_sum_my(root6))
print(max_path_sum_my(root7))
print(max_path_sum_my(root8))
