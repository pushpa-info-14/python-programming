import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, 2 * w])

        dist = [10 ** 10] * n
        dist[0] = 0
        q = [[0, 0]]
        while q:
            cost, node = heapq.heappop(q)
            if node == n - 1:
                return cost
            for nei, w in adj[node]:
                if cost + w < dist[nei]:
                    dist[nei] = cost + w
                    heapq.heappush(q, [cost + w, nei])
        return -1


s = Solution()
print(s.minCost(n=4, edges=[[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]))
print(s.minCost(n=4, edges=[[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]]))
print(s.minCost(n=5, edges=[[1, 2, 8], [3, 1, 10], [0, 3, 3]]))
