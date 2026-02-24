from collections import deque
from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append([0, root])
        res = 0
        while q:
            res = max(res, q[-1][0] - q[0][0] + 1)
            for _ in range(len(q)):
                c, node = q.popleft()
                if node.left:
                    q.append([2 * c + 1, node.left])
                if node.right:
                    q.append([2 * c + 2, node.right])
        return res


s = Solution()
tree = TreeNode.build([1, 3, 2, 5, 3, None, 9])
print(s.widthOfBinaryTree(tree))
tree = TreeNode.build([1, 3, 2, 5, None, None, 9, 6, None, 7])
print(s.widthOfBinaryTree(tree))
tree = TreeNode.build([1, 3, 2, 5])
print(s.widthOfBinaryTree(tree))
