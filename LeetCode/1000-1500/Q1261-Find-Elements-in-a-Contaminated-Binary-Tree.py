from typing import Optional

from Leetcode.Common.TreeNode import TreeNode


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = set()

        def dfs(node, correct_val):
            if node is None:
                return

            node.val = correct_val
            self.values.add(correct_val)
            dfs(node.left, correct_val * 2 + 1)
            dfs(node.right, correct_val * 2 + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        # def dfs(node):
        #     if node is None:
        #         return False
        #     if node.val == target:
        #         return True
        #     if node.val > target:
        #         return False
        #
        #     return dfs(node.left) or dfs(node.right)
        # return dfs(self.root)

        return True if target in self.values else False


root = TreeNode(-1, None, TreeNode(-1))

s = FindElements(root)
print(s.find(1))
print(s.find(2))
