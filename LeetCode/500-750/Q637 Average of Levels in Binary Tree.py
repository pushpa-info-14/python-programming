from collections import defaultdict, deque
from typing import Optional, List

from Common.TreeNode import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_map = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            level_map[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        res = []
        for i in range(len(level_map.keys())):
            res.append(sum(level_map[i]) / len(level_map[i]))
        return res

    def averageOfLevels2(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            res.append(sum(level) / len(level))
        return res


s = Solution()
tree = TreeNode.build([3, 9, 20, None, None, 15, 7])
print(s.averageOfLevels(tree))
print(s.averageOfLevels2(tree))
