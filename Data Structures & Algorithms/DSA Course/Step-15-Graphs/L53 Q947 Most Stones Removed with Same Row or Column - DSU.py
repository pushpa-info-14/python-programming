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
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row = 0
        max_col = 0
        for row, col in stones:
            max_row = max(max_row, row)
            max_col = max(max_col, col)

        ds = DisjointSet(max_row + max_col + 1)
        nodes = set()
        for row, col in stones:
            node_row = row
            node_col = max_row + col + 1
            ds.union(node_row, node_col)
            nodes.add(node_row)
            nodes.add(node_col)

        count = 0
        for node in nodes:
            if ds.findParent(node) == node:
                count += 1

        return len(stones) - count


s = Solution()
print(s.removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
print(s.removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
print(s.removeStones(stones=[[0, 0]]))
