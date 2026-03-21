from Common.TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = -1
        count = 0

        def dfs(node):
            nonlocal res, count
            if not node:
                return
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
            dfs(node.right)

        dfs(root)
        return res

    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = -1
        count = 0

        def dfs(node):
            nonlocal res, count
            if not node:
                return
            dfs(node.right)
            count += 1
            if count == k:
                res = node.val
            dfs(node.left)

        dfs(root)
        return res


s = Solution()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
print(s.kthSmallest(tree, 1))
print(s.kthSmallest(tree, 2))
print(s.kthSmallest(tree, 3))
print(s.kthLargest(tree, 1))
print(s.kthLargest(tree, 2))
print(s.kthLargest(tree, 3))
