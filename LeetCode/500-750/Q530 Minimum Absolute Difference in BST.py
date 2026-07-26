from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 10 ** 10
        prev = -1

        def dfs(node):
            nonlocal res, prev
            if node is None:
                return
            dfs(node.left)
            if prev != -1:
                res = min(res, node.val - prev)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return res


s = Solution()
t = TreeNode.build([4, 2, 6, 1, 3])
print(s.getMinimumDifference(t))
t = TreeNode.build([1, 0, 48, None, None, 12, 49])
print(s.getMinimumDifference(t))
