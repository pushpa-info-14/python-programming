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
    def spanningTree(self, n: int, edges: List[List[int]]) -> int:
        sorted_edges = []
        for u, v, w in edges:
            sorted_edges.append((w, u, v))
        sorted_edges.sort()
        summation = 0

        ds = DisjointSet(n)
        for w, u, v in sorted_edges:
            if ds.findParent(u) != ds.findParent(v):
                summation += w
                ds.union(u, v)
        return summation


s = Solution()
print(s.spanningTree(3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]))
