from collections import deque, defaultdict

from Common.BinaryTreeNode import BinaryTreeNode

"""
Note: If there are multiple nodes passing through a vertical line, then they should be printed as they 
appear in level order traversal of the tree.
"""


def verticalOrderTraversalModerate(root):
    mp = defaultdict(list)
    q = deque([(0, 0, root)])

    while q:
        for _ in range(len(q)):
            x, y, node = q.popleft()
            mp[x].append(node.data)
            if node.left:
                q.append((x - 1, y + 1, node.left))
            if node.right:
                q.append((x + 1, y + 1, node.right))

    res = []
    for i in sorted(mp.keys()):
        res += mp[i]
    return res


"""
If multiple nodes have the same 'x' and 'y' coordinates, they will be accessed in non-decreasing order of values.
"""


def verticalOrderTraversalHard(root):
    q = deque([(0, 0, root)])
    mp = defaultdict(list)

    while q:
        for _ in range(len(q)):
            x, y, node = q.popleft()
            mp[(x, y)].append(node.data)
            if node.left:
                q.append((x - 1, y + 1, node.left))
            if node.right:
                q.append((x + 1, y + 1, node.right))
    res = []
    for key in sorted(mp.keys()):
        for val in sorted(mp[key]):
            res.append(val)
    return res


"""
https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1

Given the root of a Binary Tree, find the vertical traversal of the tree starting from the leftmost level 
to the rightmost level.

Note: If there are multiple nodes passing through a vertical line, then they should be printed as they 
appear in level order traversal of the tree.
"""


class Solution:
    def verticalOrder(self, root):
        mp = defaultdict(list)
        q = deque([(0, 0, root)])

        while q:
            for _ in range(len(q)):
                x, y, node = q.popleft()
                mp[x].append(node.data)
                if node.left:
                    q.append((x - 1, y + 1, node.left))
                if node.right:
                    q.append((x + 1, y + 1, node.right))

        res = []
        for i in sorted(mp.keys()):
            res.append(mp[i])
        return res


tree = BinaryTreeNode.build([2, 7, 5, 2, 6, None, 9, None, None, 5, 11, 4, None, None, None, None, None, None, None])
print(verticalOrderTraversalModerate(tree))
print(verticalOrderTraversalHard(tree))

s = Solution()
print(s.verticalOrder(tree))
