from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def childrenSum(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        children = 0
        if root.left:
            children += root.left.val
        if root.right:
            children += root.right.val
        if children >= root.val:
            root.val = children
        else:
            if root.left:
                root.left.val = root.val
            if root.right:
                root.right.val = root.val
        self.childrenSum(root.left)
        self.childrenSum(root.right)

        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val
        if root.left or root.right:
            root.val = total


s = Solution()
tree = TreeNode.build([2, 35, 10, 2, 3, 5, 2])
tree.preorder_traversal()
s.childrenSum(tree)
tree.preorder_traversal()
