"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not left < node.val and node.val < right:
                return False

            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))


node1 = TreeNode(20, TreeNode(15), TreeNode(7))
root1 = TreeNode(-10, TreeNode(9), node1)

node2 = TreeNode(20, TreeNode(15), TreeNode(25))
root2 = TreeNode(10, TreeNode(9), node2)

solution = Solution()
print(solution.is_valid_bst(root1))
print(solution.is_valid_bst(root2))
