"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
structure and node values of subRoot and false otherwise.

A subtree of a binary tree 'tree' is a tree that consists of a node in tree and all of this node's descendants.
The tree 'tree' could also be considered as a subtree of itself.
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.same_tree(s, t):
            return True

        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def same_tree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right)
        return False


node1 = TreeNode(20, TreeNode(15), TreeNode(7))
root1 = TreeNode(-10, TreeNode(9), node1)

root2 = TreeNode(20, TreeNode(15), TreeNode(7))
root3 = TreeNode(21, TreeNode(15), TreeNode(7))

solution = Solution()
print(solution.is_subtree(root1, root2))
print(solution.is_subtree(root1, root3))
