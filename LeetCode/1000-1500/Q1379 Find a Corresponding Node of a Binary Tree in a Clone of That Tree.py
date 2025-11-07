from Common.TreeNode import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node1, node2):
            if not node1:
                return
            if node1 == target:
                return node2
            res1 = dfs(node1.left, node2.left)
            if res1:
                return res1
            res2 = dfs(node1.right, node2.right)
            if res2:
                return res2

        return dfs(original, cloned)


s = Solution()
tree1 = TreeNode.build([7, 4, 3, None, None, 6, 19])
tree2 = TreeNode.build([7, 4, 3, None, None, 6, 19])

print(s.getTargetCopy(tree1, tree2, tree1.right).val)
