from typing import List


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self._adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self._diagonal = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        self._coordinates = {}
        self._n = len(grid)
        self._grid = grid
        for r in range(self._n):
            for c in range(self._n):
                self._coordinates[grid[r][c]] = [r, c]

    def cal(self, value, directions):
        res = 0
        r, c = self._coordinates[value]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr == self._n or nc == self._n:
                continue
            res += self._grid[nr][nc]
        return res

    def adjacentSum(self, value: int) -> int:
        return self.cal(value, self._adjacent)

    def diagonalSum(self, value: int) -> int:
        return self.cal(value, self._diagonal)


s = NeighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(s.adjacentSum(1))
print(s.adjacentSum(4))
print(s.diagonalSum(4))
print(s.diagonalSum(8))
