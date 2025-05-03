import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        mod = 10 ** 9 + 7
        int_max = math.inf
        distance = [int_max] * n
        ways = [0] * n

        distance[0] = 0
        ways[0] = 1
        q = [(0, 0)]

        while q:
            dist, node = heapq.heappop(q)
            for nei, w in adj[node]:
                new_dist = dist + w
                if distance[nei] > new_dist:
                    distance[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(q, (new_dist, nei))
                elif distance[nei] == new_dist:
                    ways[nei] = (ways[nei] + ways[node]) % mod

        return ways[n - 1] % mod


s = Solution()
print(s.countPaths(n=7, roads=[[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                               [0, 4, 5], [4, 6, 2]]))
print(s.countPaths(n=2, roads=[[1, 0, 10]]))
