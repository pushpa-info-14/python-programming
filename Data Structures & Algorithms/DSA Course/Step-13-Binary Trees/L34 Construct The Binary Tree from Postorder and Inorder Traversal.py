from typing import List, Optional

from Common.TreeNode import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        i_root = inorder.index(postorder[-1])
        return TreeNode(
            postorder[-1],
            self.buildTree(inorder[:i_root], postorder[:i_root]),
            self.buildTree(inorder[i_root + 1:], postorder[i_root: -1])
        )

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i

        def dfs(il, ir, pl, pr):
            if il > ir or pl > pr:
                return None
            i_root = mp[postorder[pr]]
            nums_left = i_root - il
            return TreeNode(
                postorder[pr],
                dfs(il, i_root - 1, pl, pl + nums_left - 1),
                dfs(i_root + 1, ir, pl + nums_left, pr - 1)
            )

        n = len(inorder)
        return dfs(0, n - 1, 0, n - 1)


s = Solution()
s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]).preorder_traversal()
s.buildTree2(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]).preorder_traversal()
s.buildTree(inorder=[-1], postorder=[-1]).preorder_traversal()
s.buildTree2(inorder=[-1], postorder=[-1]).preorder_traversal()
