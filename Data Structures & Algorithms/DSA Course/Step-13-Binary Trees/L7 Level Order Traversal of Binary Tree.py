from collections import deque

from Common.TreeNode import TreeNode


def levelOrder(root):
    if root is None:
        return
    res = []
    q = deque()
    q.append(root)

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)

    return res


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

print(levelOrder(tree))
