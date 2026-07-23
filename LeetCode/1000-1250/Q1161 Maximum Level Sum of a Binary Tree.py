from collections import deque
from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -10 ** 10
        max_level = 1
        level = 1
        q = deque([root])
        while q:
            cur = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if cur > max_sum:
                max_sum = cur
                max_level = level
            level += 1
        return max_level


s = Solution()
tree = TreeNode.build([1, 7, 0, 7, -8])
print(s.maxLevelSum(tree))
