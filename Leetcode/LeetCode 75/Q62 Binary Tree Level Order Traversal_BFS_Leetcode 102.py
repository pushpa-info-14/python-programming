"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []
"""
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res

    queue = deque()
    queue.appendleft(root)
    while queue:
        level = []
        length = len(queue)
        for i in range(length):
            node = queue.pop()
            level.append(node.val)
            left = node.left
            right = node.right
            if left:
                queue.appendleft(left)
            if right:
                queue.appendleft(right)

        res.append(level)

    return res


root1 = TreeNode(1, TreeNode(2), TreeNode(3))

root2 = TreeNode(1, left=TreeNode(2))

node1 = TreeNode(2, TreeNode(4), TreeNode(5))
root3 = TreeNode(1, node1, TreeNode(3))

print(level_order(root1))
print(level_order(root2))
print(level_order(root3))
