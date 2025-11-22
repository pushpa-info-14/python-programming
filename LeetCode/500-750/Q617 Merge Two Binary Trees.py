from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if not node1 and not node2:
                return
            elif node1 and not node2:
                return node1
            elif not node1 and node2:
                return node2
            else:
                node1.val += node2.val
                node1.left = dfs(node1.left, node2.left)
                node1.right = dfs(node1.right, node2.right)
                return node1

        return dfs(root1, root2)


s = Solution()
tree1 = TreeNode.build([1, 3, 2, 5])
tree2 = TreeNode.build([2, 1, 3, None, 4, None, 7])
s.mergeTrees(tree1, tree2).preorder_traversal()
