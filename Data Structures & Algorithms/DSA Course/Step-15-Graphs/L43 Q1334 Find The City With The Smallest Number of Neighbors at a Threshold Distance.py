import math
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = math.inf
        adj = [[inf] * n for _ in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for u, v, w in edges:
            adj[u][v] = w
            adj[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[i][k] != inf and adj[k][j] != inf:
                        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

        min_count = n
        city = 0
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and adj[i][j] <= distanceThreshold:
                    count += 1
            if min_count >= count:
                min_count = count
                city = i

        return city


s = Solution()
print(s.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4))
print(s.findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold=2))
