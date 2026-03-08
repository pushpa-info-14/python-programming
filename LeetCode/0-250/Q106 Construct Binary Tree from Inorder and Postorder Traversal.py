from typing import List, Optional

from Common.TreeNode import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        root_index = inorder.index(postorder[-1])
        return TreeNode(
            postorder[-1],
            self.buildTree(inorder[:root_index], postorder[:root_index]),
            self.buildTree(inorder[root_index + 1:], postorder[root_index: -1])
        )


s = Solution()
s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]).preorder_traversal()
s.buildTree(inorder=[-1], postorder=[-1]).preorder_traversal()
