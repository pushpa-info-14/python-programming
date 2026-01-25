from collections import deque
from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.children:
                    for child in node.children:
                        q.append(child)
            res += 1
        return res


s = Solution()
tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(s.maxDepth(tree))
