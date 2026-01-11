from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, ):
            if not node:
                return [0, None]
            l_depth, l_node = dfs(node.left)
            r_depth, r_node = dfs(node.right)
            if l_depth == r_depth:
                return [1 + l_depth, node]
            elif l_depth > r_depth:
                return [1 + l_depth, l_node]
            else:
                return [1 + r_depth, r_node]

        return dfs(root)[1]


s = Solution()
tree = TreeNode.build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(s.subtreeWithAllDeepest(tree))
tree = TreeNode.build([1])
print(s.subtreeWithAllDeepest(tree))
tree = TreeNode.build([0, 1, 3, None, 2])
print(s.subtreeWithAllDeepest(tree))
