"""

"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth1(root: TreeNode) -> int:
    if not root:
        return 0

    return 1 + max(max_depth1(root.left), max_depth1(root.right))


def max_depth2(root: TreeNode) -> int:
    if not root:
        return 0

    level = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


def max_depth3(root: TreeNode) -> int:
    if not root:
        return 0

    level = 0
    stack = [[root, 1]]
    while stack:
        node, depth = stack.pop()

        if node:
            level = max(level, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return level


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

print(max_depth1(node1))
print(max_depth2(node1))
print(max_depth3(node1))
