from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traversal(node):
            if not node:
                return None
            inorder_traversal(node.left)
            inorder.append(node.val)
            inorder_traversal(node.right)

        def set_sum(node):
            if not node:
                return None
            set_sum(node.left)
            node.val = mp[node.val]
            set_sum(node.right)

        inorder = []
        inorder_traversal(root)
        cur = sum(inorder)
        mp = {}
        for num in inorder:
            mp[num] = cur
            cur -= num
        set_sum(root)
        return root


s = Solution()
root = TreeNode.build([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
s.bstToGst(root).preorder_traversal()

root = TreeNode.build([0, None, 1])
s.bstToGst(root).preorder_traversal()
