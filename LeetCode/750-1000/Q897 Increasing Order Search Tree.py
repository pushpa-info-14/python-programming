from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)

        new_root = TreeNode(inorder[0])
        cur = new_root
        for num in inorder[1:]:
            cur.right = TreeNode(num)
            cur = cur.right

        return new_root


s = Solution()
tree = TreeNode.build([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
s.increasingBST(tree).preorder_traversal()
