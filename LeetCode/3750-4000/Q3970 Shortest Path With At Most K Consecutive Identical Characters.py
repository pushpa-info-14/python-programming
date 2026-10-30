import heapq
from collections import defaultdict
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj_matrix = defaultdict(list)
        for u, v, w in edges:
            adj_matrix[u].append([v, w])
        visited = set()
        q = [(0, 0, 1)]  # dist, node, count

        while q:
            dist, u, count = heapq.heappop(q)
            if count > k: continue
            if (u, count) in visited: continue
            if u == n - 1: return dist
            visited.add((u, count))
            for v, w in adj_matrix[u]:
                heapq.heappush(q, (dist + w, v, count + 1 if labels[u] == labels[v] else 1))
        return -1


s = Solution()
print(s.shortestPath(n=3, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 3]], labels="aab", k=1))
print(s.shortestPath(n=3, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 3]], labels="aab", k=2))
print(s.shortestPath(n=3, edges=[[0, 1, 1], [1, 2, 1]], labels="aaa", k=2))
