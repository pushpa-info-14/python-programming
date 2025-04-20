from collections import defaultdict, deque
from typing import Optional, List

from Leetcode.Common.TreeNode import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        min_col, max_col = [0], [0]

        def dfs(node, col):
            if not node:
                return
            min_col[0] = min(min_col[0], col)
            max_col[0] = max(max_col[0], col)
            if col not in cols:
                cols[col] = []
            cols[col].append(node.val)
            dfs(node.left, col - 1)
            dfs(node.right, col + 1)

        dfs(root, 0)

        res = []
        for key in range(min_col[0], max_col[0] + 1):
            res.append(cols[key])
        return res

    def verticalOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])  # (node, col)
        cols = defaultdict(list)
        min_col, max_col = 0, 0

        while q:
            node, col = q.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            cols[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        return [cols[col] for col in range(min_col, max_col + 1)]


t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
t2 = TreeNode(3, TreeNode(9, TreeNode(11), TreeNode(14)), TreeNode(20, TreeNode(15), TreeNode(7)))

s = Solution()
print(s.verticalOrder(t1))
print(s.verticalOrder(t2))
print(s.verticalOrder2(t1))
print(s.verticalOrder2(t2))
