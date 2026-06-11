from collections import defaultdict, deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q = deque([1])
        level = 0
        seen = set()
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                seen.add(node)
                for nei in adj[node]:
                    if nei not in seen:
                        q.append(nei)
            level += 1
        return pow(2, level - 2, mod)


s = Solution()
print(s.assignEdgeWeights(edges=[[1, 2]]))
print(s.assignEdgeWeights(edges=[[1, 2], [1, 3], [3, 4], [3, 5]]))
