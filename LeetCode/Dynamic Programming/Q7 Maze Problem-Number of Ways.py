class Solution:
    def number_of_ways(self, n: int, m: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(1, n + 1):
            dp[r][1] = 1
        for c in range(1, m + 1):
            dp[1][c] = 1
        for r in range(2, n + 1):
            for c in range(2, m + 1):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[n][m]


s = Solution()
print(s.number_of_ways(18, 6))  # 26334
print(s.number_of_ways(75, 19))  # 5873182941643167150
