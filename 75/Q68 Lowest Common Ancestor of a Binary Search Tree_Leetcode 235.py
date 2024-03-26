"""
Given a binary search tree (BST), find the lowest common
ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest
common ancestor is defined between two nodes p and q as the
lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


solution = Solution()

node1 = TreeNode(15)
node2 = TreeNode(25)
node3 = TreeNode(20, node1, node2)
root1 = TreeNode(10, TreeNode(9), node3)

result = solution.lowest_common_ancestor(root1, node1, node2)
print(result.val)
