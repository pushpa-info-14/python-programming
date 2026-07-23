from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, value):
            if not node:
                return 0
            if not node.left and not node.right:
                return (value << 1) + node.val
            value = (value << 1) + node.val
            left = dfs(node.left, value)
            right = dfs(node.right, value)
            return left + right

        return dfs(root, 0)


s = Solution()
tree = TreeNode.build([1, 0, 1, 0, 1, 0, 1])
print(s.sumRootToLeaf(tree))

print(1 << 2 + 1)
