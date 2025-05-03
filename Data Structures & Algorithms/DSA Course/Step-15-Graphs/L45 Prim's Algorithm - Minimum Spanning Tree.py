import heapq
from collections import defaultdict
from typing import List


class Solution:
    def spanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [0] * n
        q = [(0, 0)]  # w, node
        summation = 0
        while q:
            w, node = heapq.heappop(q)
            if visited[node]:
                continue
            summation += w
            visited[node] = 1
            for nei, nei_w in graph[node]:
                if not visited[nei]:
                    heapq.heappush(q, (nei_w, nei))

        return summation


s = Solution()
print(s.spanningTree(3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]))
