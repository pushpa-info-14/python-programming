from typing import List


class DisjointSet:
    def __init__(self, n):
        self.size = [0] * (n + 1)
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)

        extra_edges = 0
        for u, v in connections:
            if ds.findParent(u) == ds.findParent(v):
                extra_edges += 1
            else:
                ds.union(u, v)

        components = 0
        for i in range(n):
            if ds.findParent(i) == i:
                components += 1

        if extra_edges >= components - 1:
            return components - 1
        return -1


s = Solution()
print(s.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))
print(s.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
print(s.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))
