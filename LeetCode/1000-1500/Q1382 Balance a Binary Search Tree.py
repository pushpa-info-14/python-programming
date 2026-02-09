from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        def build(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            node = nodes[mid]
            node.left = build(low, mid - 1)
            node.right = build(mid + 1, high)
            return node

        return build(0, len(nodes) - 1)


s = Solution()
tree = TreeNode.build([1, None, 2, None, 3, None, 4, None, None])
print(s.balanceBST(tree).inorder_traversal())
