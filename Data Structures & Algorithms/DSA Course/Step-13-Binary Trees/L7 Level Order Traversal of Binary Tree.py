from collections import deque

from Common.TreeNode import TreeNode


def levelOrder(node):
    if node is None:
        return
    res = []
    q = deque()
    q.append(node)

    while q:
        level = []
        for _ in range(len(q)):
            element = q.popleft()
            level.append(element.val)
            if element.left:
                q.append(element.left)
            if element.right:
                q.append(element.right)
        res.append(level)

    print(res)


root = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

levelOrder(root)
