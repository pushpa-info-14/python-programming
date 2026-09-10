from Common.TreeNode import TreeNode


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if node is None:
                return 0, 0
            l_sum, l_count = dfs(node.left)
            r_sum, r_count = dfs(node.right)
            t_sum = l_sum + node.val + r_sum
            t_count = l_count + 1 + r_count
            if node.val == t_sum // t_count:
                res += 1
            return t_sum, t_count

        dfs(root)
        return res


s = Solution()
tree = TreeNode.build([4, 8, 5, 0, 1, None, 6])
print(s.averageOfSubtree(tree))
tree = TreeNode.build([1])
print(s.averageOfSubtree(tree))
