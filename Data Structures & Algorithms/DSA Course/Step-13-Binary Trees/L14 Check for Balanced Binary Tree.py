from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root):
            if not root:
                return 0
            lh = maxDepth(root.left)
            rh = maxDepth(root.right)
            if lh == -1 or rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1

            return 1 + max(lh, rh)

        return True if maxDepth(root) != -1 else False


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

s = Solution()
print(s.isBalanced(tree))
