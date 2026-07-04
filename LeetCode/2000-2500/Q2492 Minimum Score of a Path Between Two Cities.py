from collections import defaultdict, deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, distance in roads:
            adj[u].append([v, distance])
            adj[v].append([u, distance])

        res = 10 ** 10
        q = deque()
        q.append((1, -1))  # node, previous
        visited = set()
        visited.add(1)
        while q:
            node, prev = q.popleft()
            for nei, d in adj[node]:
                if nei == prev:
                    continue
                res = min(res, d)
                if nei in visited:
                    continue
                visited.add(nei)
                q.append((nei, node))
        return res


s = Solution()
print(s.minScore(n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
print(s.minScore(n=4, roads=[[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
