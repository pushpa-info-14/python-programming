from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        mp = {}
        q = deque([(1, 0, -1)])  # (node, level, parent)
        while q:
            node, level, parent = q.popleft()
            mp[node] = [level, parent]
            for nei in adj[node]:
                if nei != parent:
                    q.append((nei, level + 1, node))

        @cache
        def lca(u, v):
            while mp[u][0] > mp[v][0]:
                u = mp[u][1]
            while mp[u][0] < mp[v][0]:
                v = mp[v][1]
            while u != v:
                u = mp[u][1]
                v = mp[v][1]
            return u

        res = []
        for u, v in queries:
            l = lca(u, v)
            levels = mp[u][0] - mp[l][0] + mp[v][0] - mp[l][0]
            res.append(0 if levels == 0 else pow(2, levels - 1, mod))

        return res


s = Solution()
print(s.assignEdgeWeights(edges=[[1, 2]], queries=[[1, 1], [1, 2]]))
print(s.assignEdgeWeights(edges=[[1, 2], [1, 3], [3, 4], [3, 5]], queries=[[1, 4], [3, 4], [2, 5]]))
