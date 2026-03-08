from typing import List, Optional

from Common.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root_index = inorder.index(preorder[0])
        return TreeNode(
            preorder[0],
            self.buildTree(preorder[1:root_index + 1], inorder[:root_index]),
            self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        )


s = Solution()
s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]).preorder_traversal()
s.buildTree(preorder=[-1], inorder=[-1]).preorder_traversal()
