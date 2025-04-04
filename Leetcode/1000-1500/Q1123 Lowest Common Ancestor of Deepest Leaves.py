from typing import Optional

from Leetcode.Common.TreeNode import TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None, 0

            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height == right_height:
                return node, 1 + left_height
            elif left_height > right_height:
                return left_node, 1 + left_height
            else:
                return right_node, 1 + right_height

        def dfs2(node, depth):
            if not node:
                return None, depth + 1

            left_node, left_depth = dfs2(node.left, depth + 1)
            right_node, right_depth = dfs2(node.right, depth + 1)

            if left_depth == right_depth:
                return node, left_depth
            elif left_depth > right_depth:
                return left_node, left_depth
            else:
                return right_node, right_depth

        # lca, _ = dfs(root)
        lca, _ = dfs2(root, 0)
        return lca
