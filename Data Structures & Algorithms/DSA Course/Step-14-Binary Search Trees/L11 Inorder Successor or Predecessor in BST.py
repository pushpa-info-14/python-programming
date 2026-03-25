from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor

    def inorderPredecessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        predecessor = None
        while root:
            if p.val <= root.val:
                root = root.left
            else:
                predecessor = root
                root = root.right
        return predecessor


s = Solution()
tree = TreeNode.build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
print(s.inorderSuccessor(tree, tree.right).val)
print(s.inorderSuccessor(tree, tree.left).val)
print(s.inorderPredecessor(tree, tree.right).val)
print(s.inorderPredecessor(tree, tree.left).val)
