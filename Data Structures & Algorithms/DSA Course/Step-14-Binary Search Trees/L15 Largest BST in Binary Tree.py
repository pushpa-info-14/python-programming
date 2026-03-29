from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def largestBST(self, root: Optional[TreeNode]) -> int:
        inf = 10 ** 10

        def dfs(node):
            if not node:
                return 0, inf, -inf  # size, minimum, maximum
            l_size, l_min, l_max = dfs(node.left)
            r_size, r_min, r_max = dfs(node.right)

            if l_max < node.val < r_min:
                size = l_size + r_size + 1
                return size, min(node.val, l_min), max(node.val, r_max)
            else:
                return max(l_size, r_size), -inf, inf

        return dfs(root)[0]


s = Solution()
tree = TreeNode.build([10, 5, 15, 1, 8, None, 7])
print(s.largestBST(tree))
