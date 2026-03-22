from typing import List, Optional

from Common.TreeNode import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if len(nums) == 0:
                return None
            node = TreeNode(nums[0])
            left = []
            right = []
            for num in nums[1:]:
                if num < node.val:
                    left.append(num)
                else:
                    right.append(num)
            node.left = dfs(left)
            node.right = dfs(right)
            return node

        return dfs(preorder)

    def bstFromPreorder2(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        i = 0

        def dfs(bound):
            nonlocal i
            if i == n or preorder[i] > bound:
                return None
            node = TreeNode(preorder[i])
            i += 1
            node.left = dfs(node.val)
            node.right = dfs(bound)
            return node

        return dfs(10 ** 10)


s = Solution()
s.bstFromPreorder(preorder=[8, 5, 1, 7, 10, 12]).inorder_traversal()
s.bstFromPreorder(preorder=[1, 3]).inorder_traversal()
print("-----------")
s.bstFromPreorder2(preorder=[8, 5, 1, 7, 10, 12]).inorder_traversal()
s.bstFromPreorder2(preorder=[1, 3]).inorder_traversal()
