from typing import List


class DisjointSet:
    def __init__(self):
        self._parent = {}

    def findParent(self, x):
        if x not in self._parent:
            self._parent[x] = x
        while x != self._parent[x]:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x

    def union(self, x, y):
        px = self.findParent(x)
        py = self.findParent(y)
        if px < py:
            self._parent[py] = self._parent[px]
        else:
            self._parent[px] = self._parent[py]


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0] * col for _ in range(row)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def can_cross():
            q = []
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
            visited = [[False] * col for _ in range(row)]
            while q:
                r, c = q.pop()
                if r == row - 1:
                    return True
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr == row or nc == col or grid[nr][nc] == 1 or visited[nr][nc]:
                        continue
                    q.append((nr, nc))
                    visited[nr][nc] = True
            return False

        low, high = 0, len(cells) - 1
        while low <= high:
            mid = (low + high) // 2
            grid = [[0] * col for _ in range(row)]
            for i in range(mid):
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1

            if can_cross():
                low = mid + 1
            else:
                high = mid - 1
        return high

    def latestDayToCross2(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = len(cells)
        grid = [[1] * col for _ in range(row)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ds = DisjointSet()
        top, bottom = -1, n

        for c in range(col):
            ds.union(top, c)
            ds.union(bottom, (row - 1) * col + c)
        for i in reversed(range(len(cells))):
            cell = cells[i]
            r = cell[0] - 1
            c = cell[1] - 1
            grid[r][c] = 0

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr == row or nc == col or grid[nr][nc] == 1:
                    continue
                ds.union(r * col + c, nr * col + nc)

            if ds.findParent(top) == ds.findParent(bottom):
                return i
        return -1


s = Solution()
print(s.latestDayToCross(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))
print(s.latestDayToCross(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]))
print(s.latestDayToCross(row=3, col=3, cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))
print(s.latestDayToCross(row=6, col=2,
                         cells=[[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2],
                                [1, 2]]))
print(s.latestDayToCross(row=2, col=6,
                         cells=[[1, 4], [1, 3], [2, 1], [2, 5], [2, 2], [1, 5], [2, 4], [1, 2], [1, 6], [2, 3], [2, 6],
                                [1, 1]]))
print("-------------------------")
print(s.latestDayToCross2(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))
print(s.latestDayToCross2(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]))
print(s.latestDayToCross2(row=3, col=3, cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))
print(s.latestDayToCross2(row=6, col=2,
                          cells=[[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2],
                                 [1, 2]]))
print(s.latestDayToCross2(row=2, col=6,
                          cells=[[1, 4], [1, 3], [2, 1], [2, 5], [2, 2], [1, 5], [2, 4], [1, 2], [1, 6], [2, 3], [2, 6],
                                 [1, 1]]))
