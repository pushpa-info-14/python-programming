from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp_row = [[0] * (n + 1) for _ in range(m)]
        dp_col = [[0] * n for _ in range(m + 1)]
        dp_diagonal1 = [[0] * (n + 1) for _ in range(m + 1)]
        dp_diagonal2 = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                dp_row[r][c + 1] = grid[r][c] + dp_row[r][c]
                dp_col[r + 1][c] = grid[r][c] + dp_col[r][c]
                dp_diagonal1[r + 1][c + 1] = grid[r][c] + dp_diagonal1[r][c]
                dp_diagonal2[r + 1][c] = grid[r][c] + dp_diagonal2[r][c + 1]
        res = 1
        for r in range(m):
            for c in range(n):
                for k in range(1, min(m - r, n - c)):
                    sums = set()
                    for x in range(k + 1):
                        sum_row = dp_row[r + x][c + k + 1] - dp_row[r + x][c]
                        sum_col = dp_col[r + k + 1][c + x] - dp_col[r][c + x]
                        sums.add(sum_row)
                        sums.add(sum_col)
                    sum_diagonal1 = dp_diagonal1[r + k + 1][c + k + 1] - dp_diagonal1[r][c]
                    sum_diagonal2 = dp_diagonal2[r + k + 1][c] - dp_diagonal2[r][c + k + 1]
                    sums.add(sum_diagonal1)
                    sums.add(sum_diagonal2)
                    if len(sums) == 1:
                        res = max(res, k + 1)
        return res


s = Solution()
print(s.largestMagicSquare(grid=[[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]))
print(s.largestMagicSquare(grid=[[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]))
