from Common.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            cur = node.val
            if cur > p.val and cur > q.val:
                return dfs(node.left)
            if cur < p.val and cur < q.val:
                return dfs(node.right)
            return node

        return dfs(root)

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


s = Solution()
tree = TreeNode.build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
print(s.lowestCommonAncestor(tree, tree.left, tree.right).val)
print(s.lowestCommonAncestor2(tree, tree.left, tree.right).val)
print(s.lowestCommonAncestor2(tree, tree.left, tree.right).val)
