from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 ** 9 + 7

        def cal_total(node):
            if not node:
                return 0
            return node.val + cal_total(node.left) + cal_total(node.right)

        total = cal_total(root)
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left * (total - left), right * (total - right))
            return node.val + left + right

        dfs(root)
        return res % mod


s = Solution()
tree = TreeNode.build([1, 2, 3, 4, 5, 6])
print(s.maxProduct(tree))
