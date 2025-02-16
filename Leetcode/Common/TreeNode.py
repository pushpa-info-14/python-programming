class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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