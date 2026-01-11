from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            res = max(res, l + r + node.val)

            return node.val + max(l, r)

        dfs(root)
        return res

# LeetCode 124
tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

s = Solution()
print(s.maxPathSum(tree))