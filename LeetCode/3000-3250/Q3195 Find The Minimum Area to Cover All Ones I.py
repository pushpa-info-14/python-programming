from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row_min, row_max, col_min, col_max = m, 0, n, 0

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    row_min = min(row_min, r)
                    row_max = max(row_max, r)
                    col_min = min(col_min, c)
                    col_max = max(col_max, c)

        return (row_max - row_min + 1) * (col_max - col_min + 1)


s = Solution()
print(s.minimumArea(grid=[[0, 1, 0], [1, 0, 1]]))
print(s.minimumArea(grid=[[1, 0], [0, 0]]))
print(s.minimumArea(grid=[[0], [1]]))
