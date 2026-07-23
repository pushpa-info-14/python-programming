import math
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        mod = 10 ** 9 + 7
        min_heap = [(0, 0)]  # (cost, node)
        min_cost = [math.inf] * n
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)

            for nei, nei_cost in adj[node]:
                new_cost = cost + nei_cost
                if new_cost < min_cost[nei]:
                    min_cost[nei] = new_cost
                    path_count[nei] = path_count[node]
                    heappush(min_heap, (new_cost, nei))
                elif new_cost == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % mod
        return path_count[n - 1]


s = Solution()
print(s.countPaths(n=7, roads=[[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                               [0, 4, 5], [4, 6, 2]]))
print(s.countPaths(n=2, roads=[[1, 0, 10]]))
