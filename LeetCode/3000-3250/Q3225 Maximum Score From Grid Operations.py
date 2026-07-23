from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        dp = [[(0, 0) for _ in range(n)] for _ in range(n + 1)]
        for j in range(1, n):
            for i in range(n + 1):
                dp0, dp1 = dp[i][j - 1]
                prev = 0
                cur = sum(grid[p][j] for p in range(i))
                for k in range(n + 1):
                    if 0 < k <= i:
                        cur -= grid[k - 1][j]
                    if k > i:
                        prev += grid[k - 1][j - 1]
                    max_prev = max(dp0 + prev, dp1)
                    n0 = max(dp[k][j][0], max_prev)
                    n1 = max(dp[k][j][1], max_prev + cur)
                    dp[k][j] = (n0, n1)
        return max(dp[i][-1][1] for i in range(n + 1))


s = Solution()
print(s.maximumScore(grid=[[0, 0, 0, 0, 0], [0, 0, 3, 0, 0], [0, 1, 0, 0, 0], [5, 0, 0, 3, 0], [0, 0, 0, 0, 2]]))
print(s.maximumScore(grid=[[10, 9, 0, 0, 15], [7, 1, 0, 8, 0], [5, 20, 0, 11, 0], [0, 0, 0, 1, 2], [8, 12, 1, 10, 3]]))
