from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val


s = Solution()
tree = TreeNode.build([10, 4, 6])

print(s.checkTree(tree))
