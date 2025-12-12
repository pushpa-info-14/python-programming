from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        seen = set()

        def dfs(node):
            if not node:
                return
            seen.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        res = sorted(seen)
        return res[1] if len(res) > 1 else -1


s = Solution()
tree = TreeNode.build([2, 2, 5, None, None, 5, 7])
print(s.findSecondMinimumValue(tree))
tree = TreeNode.build([1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1])
print(s.findSecondMinimumValue(tree))
