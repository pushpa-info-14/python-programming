from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val == node2.val:
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            return False

        return dfs(p, q)


s = Solution()
tree1 = TreeNode.build([1, 2, 3])
tree2 = TreeNode.build([1, 2, 3])
print(s.isSameTree(tree1, tree2))
