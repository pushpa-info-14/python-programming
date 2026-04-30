from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == -1:
                        continue
                    if i + 1 < m:
                        val = grid[i + 1][j]
                        nc = 1 if val > 0 else 0
                        if c + nc <= k:
                            dp[i + 1][j][c + nc] = max(dp[i + 1][j][c + nc], dp[i][j][c] + val)
                    if j + 1 < n:
                        val = grid[i][j + 1]
                        nc = 1 if val > 0 else 0
                        if c + nc <= k:
                            dp[i][j + 1][c + nc] = max(dp[i][j + 1][c + nc], dp[i][j][c] + val)
        return max(dp[-1][-1])


s = Solution()
print(s.maxPathScore(grid=[[0, 1], [2, 0]], k=1))
print(s.maxPathScore(grid=[[0, 1], [1, 2]], k=1))
print(s.maxPathScore(grid=[[0], [2], [1], [0], [1]], k=2))
