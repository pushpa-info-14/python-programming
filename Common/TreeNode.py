class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build(nums):
        n = len(nums)
        def dfs(i):
            if i > n - 1 or nums[i] is None:
                return None
            node = TreeNode(nums[i])
            node.left = dfs(2 * i + 1)
            node.right = dfs(2 * i + 2)
            return node
        return dfs(0)


    def preorder_traversal(self):
        res = []

        def dfs(node):
            if node is None:
                res.append(None)
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(self)
        return res