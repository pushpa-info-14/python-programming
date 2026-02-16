from typing import Optional, List

from Common.TreeNode import TreeNode


class Solution:
    def printPath(self, root: Optional[TreeNode], val: int) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return False
            res.append(node.val)

            if node.val == val:
                return True
            if dfs(node.left) or dfs(node.right):
                return True
            res.pop()
            return False

        dfs(root)
        return res

    def printPath2(self, root: Optional[TreeNode], val: int) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return False
            if node.val == val:
                res.append(node.val)
                return True
            if dfs(node.left):
                res.append(node.val)
                return True
            if dfs(node.right):
                res.append(node.val)
                return True
            return False

        dfs(root)
        return res[::-1]


s = Solution()
tree = TreeNode.build([1, 2, 4, 3, 5, 7, 6])
print(s.printPath(tree, 7))
print(s.printPath(tree, 6))
print(s.printPath(tree, 3))
print("-------------------")
print(s.printPath2(tree, 7))
print(s.printPath2(tree, 6))
print(s.printPath2(tree, 3))
