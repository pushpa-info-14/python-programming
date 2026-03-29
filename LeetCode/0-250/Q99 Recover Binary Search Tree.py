from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        first = None
        last = None
        def dfs(node):
            nonlocal prev, first, last
            if not node:
                return
            dfs(node.left)
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                    last = node
                else:
                    last = node
            prev = node
            dfs(node.right)

        dfs(root)
        first.val, last.val = last.val, first.val


s = Solution()
tree = TreeNode.build([1, 3, None, None, 2])
s.recoverTree(tree)
tree.inorder_traversal()
