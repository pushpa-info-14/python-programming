# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, left = False):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                if left:
                    return node.val
                else:
                    return 0

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root)

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s = Solution()
print(s.sumOfLeftLeaves(root))