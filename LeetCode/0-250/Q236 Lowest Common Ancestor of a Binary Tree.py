from Common.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node

            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            elif l:
                return l
            else:
                return r

        return dfs(root)


s = Solution()
tree = TreeNode.build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(s.lowestCommonAncestor(tree, tree.left, tree.right).val)
