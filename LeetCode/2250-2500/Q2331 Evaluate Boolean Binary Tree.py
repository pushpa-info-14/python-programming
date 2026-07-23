from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            else:
                return dfs(node.left) and dfs(node.right)

        return dfs(root)


s = Solution()
tree = TreeNode.build([2, 1, 3, None, 0, 1])
print(s.evaluateTree(tree))
