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
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ds = DisjointSet(n * m)

        for r in range(n):
            for c in range(m):
                if not grid[r][c]:
                    continue
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr == n or nc < 0 or nc == m or not grid[nr][nc]:
                        continue
                    node = r * m + c
                    new_node = nr * m + nc
                    if ds.findParent(node) != ds.findParent(new_node):
                        ds.union(node, new_node)
        max_size = max(ds.size)
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    continue
                size = 1
                parents = set()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr == n or nc < 0 or nc == m or not grid[nr][nc]:
                        continue
                    new_node = nr * m + nc
                    parent = ds.findParent(new_node)
                    if parent not in parents:
                        size += ds.size[parent]
                        parents.add(parent)
                max_size = max(max_size, size)

        return max_size


s = Solution()
print(s.largestIsland(grid=[[1, 0], [0, 1]]))
print(s.largestIsland(grid=[[1, 1], [1, 0]]))
print(s.largestIsland(grid=[[1, 1], [1, 1]]))
