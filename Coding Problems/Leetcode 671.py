"""
Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes,
then this node's value is the smaller value among its two sub-nodes. More formally, the property
root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes'
value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        n = 0
        stack = [root]
        left = -1
        right = -1

        while stack:
            cur = stack.pop()
            if cur.left and cur.right:
                left = cur.val
                right = max(cur.left.val, cur.right.val)
                stack.append(cur.left)
                stack.append(cur.right)
            elif cur.left:
                left = cur.val
            elif cur.right:
                right = 0

node1 = TreeNode(5, TreeNode(5), TreeNode(7))
root1 = TreeNode(2, TreeNode(2), node1)

solution = Solution()
print(solution.findSecondMinimumValue(root1))
