from typing import List, Optional

from Leetcode.Common.TreeNode import TreeNode


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        post_val_to_idx = {}

        for i, num in enumerate(postorder):
            post_val_to_idx[num] = i

        def build(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return None

            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1 + 1]
                mid = post_val_to_idx[left_val]
                left_size = mid - j1 + 1

                root.left = build(i1 + 1, i1 + left_size, j1, mid)
                root.right = build(i1 + left_size + 1, i2, mid + 1, j2 - 1)
            return root

        return build(0, n - 1, 0, n - 1)


s = Solution()
print(s.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]).preorder_traversal())
print(s.constructFromPrePost([1], [1]).preorder_traversal())
