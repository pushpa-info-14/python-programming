from collections import deque

from Common.BinaryTreeNode import BinaryTreeNode


def getBottomView(root):
    q = deque([(0, root)])
    mp = {}

    while q:
        x, node = q.popleft()
        mp[x] = node.data
        if node.left:
            q.append((x - 1, node.left))
        if node.right:
            q.append((x + 1, node.right))
    res = []
    for x in sorted(mp.keys()):
        res.append(mp[x])
    return res


tree = BinaryTreeNode.build(
    [1, 2, 3, 4, 5, None, 6, None, 7, None, None, 8, None, 9, None, None, 11, 10, None, None, None, None, None])
print(getBottomView(tree))
