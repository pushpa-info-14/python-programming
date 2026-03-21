from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = 10 ** 10

        def dfs(node, l, r):
            if not node:
                return True
            if node.val <= l or r <= node.val:
                return False
            return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)

        return dfs(root, -inf, inf)


s = Solution()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
print(s.isValidBST(tree))
tree = TreeNode.build([2, 2, 2])
print(s.isValidBST(tree))
