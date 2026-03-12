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
            return True
        return False


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ds = DisjointSet(n)
        used = 0
        weights = []
        candidates = []
        for u, v, s, must in edges:
            if must == 1:
                if not ds.union(u, v):
                    return -1
                used += 1
                weights.append(s)
            else:
                candidates.append((u, v, s))

        candidates.sort(key=lambda x: -x[2])

        upgradable_weights = []
        for u, v, s in candidates:
            if ds.union(u, v):
                used += 1
                upgradable_weights.append(s)

        if used != n - 1:
            return -1

        upgradable_weights.sort()
        for i in range(min(k, len(upgradable_weights))):
            upgradable_weights[i] *= 2

        weights.extend(upgradable_weights)
        return min(weights)


s = Solution()
print(s.maxStability(n=3, edges=[[0, 1, 2, 1], [1, 2, 3, 0]], k=1))
print(s.maxStability(n=3, edges=[[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], k=2))
print(s.maxStability(n=3, edges=[[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]], k=0))
print(s.maxStability(n=3, edges=[[0, 1, 84165, 1], [0, 2, 96588, 1], [1, 2, 24710, 0]], k=2))
