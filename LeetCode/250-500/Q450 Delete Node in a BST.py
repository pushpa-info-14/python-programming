from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            return self.helper(root)
        cur = root
        while cur:
            if key < cur.val:
                if cur.left and cur.left.val == key:
                    cur.left = self.helper(cur.left)
                    break
                else:
                    cur = cur.left
            else:
                if cur.right and cur.right.val == key:
                    cur.right = self.helper(cur.right)
                    break
                else:
                    cur = cur.right
        return root

    @staticmethod
    def helper(root: TreeNode):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        right_child = root.right

        last_right = root.left
        while last_right.right:
            last_right = last_right.right
        last_right.right = right_child

        return root.left


s = Solution()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
s.deleteNode(tree, 10).preorder_traversal()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
s.deleteNode(tree, 9).preorder_traversal()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
s.deleteNode(tree, 6).preorder_traversal()
