from collections import defaultdict
from typing import Optional, List

from Common.TreeNode import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def dfs(node):
            if node is None:
                return
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        max_freq = max(freq.values())
        return [x for x in freq.keys() if freq[x] == max_freq]


s = Solution()
t = TreeNode.build([1, None, 2, 2])
print(s.findMode(t))
