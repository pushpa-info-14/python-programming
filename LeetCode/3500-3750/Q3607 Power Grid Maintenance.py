import heapq
from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))

    def findParent(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.findParent(x)
        y = self.findParent(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        ds = DisjointSet(c)
        for u, v in connections:
            ds.union(u, v)

        status = [1] * (c + 1)
        stations = defaultdict(list)
        for i in range(1, c + 1):
            parent = ds.findParent(i)
            heapq.heappush(stations[parent], i)

        res = []
        for t, station in queries:
            if t == 1:
                if status[station]:
                    res.append(station)
                    continue
                parent = ds.findParent(station)
                while stations[parent] and status[stations[parent][0]] != 1:
                    heapq.heappop(stations[parent])
                if stations[parent]:
                    res.append(stations[parent][0])
                else:
                    res.append(-1)
            else:
                status[station] = 0
        return res


s = Solution()
print(s.processQueries(c=5, connections=[[1, 2], [2, 3], [3, 4], [4, 5]],
                       queries=[[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]))
print(s.processQueries(c=3, connections=[], queries=[[1, 1], [2, 1], [1, 1]]))
