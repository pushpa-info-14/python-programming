from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(node):
            if not node:
                return 0
            res = 0
            if node.val < low:
                res += traverse(node.right)
            elif node.val > high:
                res += traverse(node.left)
            else:
                res += node.val + traverse(node.left) + traverse(node.right)
            return res

        return traverse(root)


s = Solution()
root = TreeNode.build([10, 5, 15, 3, 7, None, 18])
print(s.rangeSumBST(root, 7, 15))
