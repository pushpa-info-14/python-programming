from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        int_max = 10 ** 9
        distance = [int_max] * n
        q = deque()
        q.append((0, src, 0))  # (stops, node, distance)
        distance[src] = 0

        while q:
            stops, node, dis = q.popleft()
            if stops == k + 1:
                break
            for nei, w in adj[node]:
                if distance[nei] > dis + w:
                    distance[nei] = dis + w
                    q.append((stops + 1, nei, dis + w))

        if distance[dst] == int_max:
            return -1
        return distance[dst]


s = Solution()
print(s.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3,
                          k=1))
print(s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))
print(s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
