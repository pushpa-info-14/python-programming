from collections import defaultdict, deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q = deque([(1, 0, -1)])  # (node, level, parent)
        max_level = 0
        while q:
            node, level, parent = q.popleft()
            max_level = max(max_level, level)
            for nei in adj[node]:
                if nei != parent:
                    q.append((nei, level + 1, node))
        return pow(2, max_level - 1, mod)


s = Solution()
print(s.assignEdgeWeights(edges=[[1, 2]]))
print(s.assignEdgeWeights(edges=[[1, 2], [1, 3], [3, 4], [3, 5]]))
