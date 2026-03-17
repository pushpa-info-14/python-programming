from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val > val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)

    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        while cur and cur.val != val:
            cur = cur.left if val < cur.val else cur.right

        return cur


s = Solution()
tree = TreeNode.build([4, 2, 7, 1, 3])
s.searchBST(tree, 2).preorder_traversal()
s.searchBST2(tree, 2).preorder_traversal()