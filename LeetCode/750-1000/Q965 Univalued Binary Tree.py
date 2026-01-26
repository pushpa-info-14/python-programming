from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        seen = {root.val}

        def dfs(node):
            if not node:
                return True
            if node.val not in seen:
                return False
            seen.add(node.val)

            return dfs(node.left) and dfs(node.right)

        return dfs(root)


s = Solution()
tree = TreeNode.build([1, 1, 1, 1, 1, None, 1])
print(s.isUnivalTree(tree))
