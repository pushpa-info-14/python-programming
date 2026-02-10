from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l - r) > 1:
                res = False
            return 1 + max(l, r)

        dfs(root)
        return res


s = Solution()
tree = TreeNode.build([3, 9, 20, None, None, 15, 7])
print(s.isBalanced(tree))
