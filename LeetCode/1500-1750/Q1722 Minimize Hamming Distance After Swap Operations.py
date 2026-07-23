from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        ds = DisjointSet(n)
        for u, v in allowedSwaps:
            ds.union(u, v)

        groups = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            groups[ds.find(i)][source[i]] += 1

        res = 0
        for i in range(n):
            g = groups[ds.find(i)]
            t = target[i]
            if g[t] > 0:
                g[t] -= 1
            else:
                res += 1
        return res


s = Solution()
print(s.minimumHammingDistance(source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]))
print(s.minimumHammingDistance(source=[1, 2, 3, 4], target=[1, 3, 2, 4], allowedSwaps=[]))
print(s.minimumHammingDistance(source=[5, 1, 2, 4, 3], target=[1, 5, 4, 2, 3],
                               allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]]))
