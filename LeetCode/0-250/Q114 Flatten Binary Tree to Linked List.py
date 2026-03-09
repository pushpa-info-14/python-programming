from typing import Optional

from Common.TreeNode import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None

        def dfs(node):
            nonlocal prev
            if not node:
                return
            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None
            prev = node

        dfs(root)

    def flatten2(self, root: Optional[TreeNode]) -> None:
        st = [root]

        while st:
            cur = st.pop()
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
            if st:
                cur.right = st[-1]
            cur.left = None

    def flatten3(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right


s = Solution()
tree = TreeNode.build([1, 2, 5, 3, 4, None, 6])
s.flatten(tree)
tree.preorder_traversal()

s.flatten(None)

tree = TreeNode.build([0])
s.flatten(tree)
tree.preorder_traversal()

print("-------------")
tree = TreeNode.build([1, 2, 5, 3, 4, None, 6])
s.flatten2(tree)
tree.preorder_traversal()

print("-------------")
tree = TreeNode.build([1, 2, 5, 3, 4, None, 6])
s.flatten3(tree)
tree.preorder_traversal()
