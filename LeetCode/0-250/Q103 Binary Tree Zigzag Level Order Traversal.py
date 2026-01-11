from collections import deque
from typing import Optional, List

from Common.TreeNode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        flag = True

        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if flag:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            flag = not flag
            res.append(list(level))
        return res


s = Solution()
tree = TreeNode.build([3, 9, 20, None, None, 15, 7])
print(s.zigzagLevelOrder(tree))
