from typing import List, Optional

from Common.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        i_root = inorder.index(preorder[0])
        return TreeNode(
            preorder[0],
            self.buildTree(preorder[1:i_root + 1], inorder[:i_root]),
            self.buildTree(preorder[i_root + 1:], inorder[i_root + 1:])
        )

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i

        def dfs(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            i_root = mp[preorder[pl]]
            nums_left = i_root - il
            return TreeNode(
                preorder[pl],
                dfs(pl + 1, pl + nums_left, il, i_root - 1),
                dfs(pl + nums_left + 1, pr, i_root + 1, ir)
            )

        n = len(preorder)
        return dfs(0, n - 1, 0, n - 1)


s = Solution()
s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]).preorder_traversal()
s.buildTree2(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]).preorder_traversal()
s.buildTree(preorder=[-1], inorder=[-1]).preorder_traversal()
s.buildTree2(preorder=[-1], inorder=[-1]).preorder_traversal()
