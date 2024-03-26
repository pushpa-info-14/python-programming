"""
Given the root of a binary search tree, and an integer k, return the kth-smallest value (1-indexed) of all the
values of the nodes in the tree.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        empty = False
        while not empty:
            while cur:
                stack.append(cur)
                cur = cur.left

            if not stack:
                empty = True
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


node1 = TreeNode(20, TreeNode(15), TreeNode(25))
root1 = TreeNode(10, TreeNode(9), node1)

solution = Solution()
print(solution.kth_smallest(root1, 1))
print(solution.kth_smallest(root1, 2))
print(solution.kth_smallest(root1, 3))
print(solution.kth_smallest(root1, 4))
print(solution.kth_smallest(root1, 5))
