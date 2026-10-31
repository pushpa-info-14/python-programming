from functools import cache
from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7

        @cache
        def dfs(r, c, d):  # d = 0 - right, 1 - down
            if r < 0 or r == m or c < 0 or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            cur = 0
            if grid[r][c] == 0:
                cur += dfs(r, c + 1, 0) + dfs(r + 1, c, 1)
            elif d == 0:
                cur += dfs(r + 1, c, 1)
            else:
                cur += dfs(r, c + 1, 0)
            return cur % mod

        return dfs(0, 0, -1)


s = Solution()
print(s.uniquePaths(grid=[[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
print(s.uniquePaths(grid=[[0, 0], [0, 0]]))
print(s.uniquePaths(grid=[[0, 1, 1], [1, 1, 0]]))
