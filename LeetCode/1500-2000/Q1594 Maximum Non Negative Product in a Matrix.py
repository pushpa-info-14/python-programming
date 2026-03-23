from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        mn = [[0] * n for _ in range(m)]
        mx = [[0] * n for _ in range(m)]
        mn[0][0] = grid[0][0]
        mx[0][0] = grid[0][0]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    mn[r][c] = mn[r][c - 1] * grid[r][c]
                    mx[r][c] = mx[r][c - 1] * grid[r][c]
                elif c == 0:
                    mn[r][c] = mn[r - 1][c] * grid[r][c]
                    mx[r][c] = mx[r - 1][c] * grid[r][c]
                else:
                    v1 = mn[r][c - 1] * grid[r][c]
                    v2 = mx[r][c - 1] * grid[r][c]
                    v3 = mn[r - 1][c] * grid[r][c]
                    v4 = mx[r - 1][c] * grid[r][c]
                    mn[r][c] = min(v1, v2, v3, v4)
                    mx[r][c] = max(v1, v2, v3, v4)
        res = mx[-1][-1]
        return res % mod if res >= 0 else -1


s = Solution()
print(s.maxProductPath(grid=[[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
print(s.maxProductPath(grid=[[1, -2, 1], [1, -2, 1], [3, -4, 1]]))
print(s.maxProductPath(grid=[[1, 3], [0, -4]]))
