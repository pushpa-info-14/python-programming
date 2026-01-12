from collections import deque


class BinaryTreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def build(nums):
        n = len(nums)
        if not nums or nums[0] is None:
            return None
        root = BinaryTreeNode(nums[0])
        queue = deque([root])
        i = 1

        while queue and i < n:
            node = queue.popleft()

            # Left child
            if i < n and nums[i] is not None:
                node.left = BinaryTreeNode(nums[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < n and nums[i] is not None:
                node.right = BinaryTreeNode(nums[i])
                queue.append(node.right)
            i += 1

        return root


    def preorder_traversal(self):
        res = []

        def dfs(node):
            if node is None:
                res.append(None)
                return
            res.append(node.data)
            dfs(node.left)
            dfs(node.right)
        dfs(self)
        print(res)
        return res