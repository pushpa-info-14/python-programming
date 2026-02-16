from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root.left, root.right)


s = Solution()
tree = TreeNode.build([1, 2, 2, 3, 4, 4, 3])
print(s.isSymmetric(tree))
tree = TreeNode.build([1, 2, 2, None, 3, None, 3])
print(s.isSymmetric(tree))