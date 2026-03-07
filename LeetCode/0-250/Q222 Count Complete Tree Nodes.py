from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            hl = findHeightLeft(node)
            hr = findHeightRight(node)
            if hl == hr:
                return (1 << hl) - 1
            return 1 + dfs(node.left) + dfs(node.right)

        def findHeightLeft(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def findHeightRight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        return dfs(root)


s = Solution()
tree = TreeNode.build([1, 2, 3, 4, 5, 6])
print(s.countNodes(tree))
tree = TreeNode.build([])
print(s.countNodes(tree))
tree = TreeNode.build([1])
print(s.countNodes(tree))
