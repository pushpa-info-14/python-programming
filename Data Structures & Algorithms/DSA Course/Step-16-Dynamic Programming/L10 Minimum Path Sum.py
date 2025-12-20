from functools import cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = 10 ** 10
        directions = [[0, 1], [1, 0]]

        @cache
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return grid[m - 1][n - 1]
            cur = inf
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr == m or nc == n:
                    continue
                cur = min(cur, grid[r][c] + dfs(nr, nc))
            return cur

        return dfs(0, 0)

    def minPathSum2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = 10 ** 10
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        dp[1][0] = 0
        dp[0][1] = 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                dp[r][c] = grid[r - 1][c - 1] + min(dp[r - 1][c], dp[r][c - 1])
        return dp[m][n]

# LeetCode 64
s = Solution()
print(s.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
print("------------------------------------")
print(s.minPathSum2(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum2(grid=[[1, 2, 3], [4, 5, 6]]))
