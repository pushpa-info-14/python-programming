from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        x = [[0] * (n + 1) for _ in range(m + 1)]
        y = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                val_x = 1 if grid[r - 1][c - 1] == "X" else 0
                val_y = 1 if grid[r - 1][c - 1] == "Y" else 0
                x[r][c] = val_x + x[r - 1][c] + x[r][c - 1] - x[r - 1][c - 1]
                y[r][c] = val_y + y[r - 1][c] + y[r][c - 1] - y[r - 1][c - 1]
                if x[r][c] == y[r][c] and x[r][c] > 0:
                    res += 1
        return res


s = Solution()
print(s.numberOfSubmatrices(grid=[["X", "Y", "."], ["Y", ".", "."]]))
print(s.numberOfSubmatrices(grid=[["X", "X"], ["X", "Y"]]))
print(s.numberOfSubmatrices(grid=[[".", "."], [".", "."]]))
