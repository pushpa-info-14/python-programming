from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(node):
            if not node:
                return 0
            dl = dfs(node.left)
            dr = dfs(node.right)
            diameter[0] = max(diameter[0], dl + dr)
            return 1 + max(dl, dr)

        dfs(root)
        return diameter[0]


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

s = Solution()
print(s.diameterOfBinaryTree(tree))
