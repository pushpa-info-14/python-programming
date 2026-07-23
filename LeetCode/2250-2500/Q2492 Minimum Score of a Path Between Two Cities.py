from collections import defaultdict, deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append([v, w])
            adj[v].append([u, w])

        res = 10 ** 10
        q = deque([1])
        visited = {1}
        while q:
            node = q.popleft()
            for nei, d in adj[node]:
                res = min(res, d)
                if nei in visited:
                    continue
                visited.add(nei)
                q.append(nei)
        return res


s = Solution()
print(s.minScore(n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
print(s.minScore(n=4, roads=[[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
