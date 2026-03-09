class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

        # dp[i][j][0] Valid ending with 0
        # dp[i][j][1] Valid ending with 1

        for i in range(min(limit, zero) + 1):
            dp[i][0][0] = 1
        for j in range(min(limit, one) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]) % mod
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0]) % mod
        return (dp[zero][one][0] + dp[zero][one][1]) % mod


s = Solution()
print(s.numberOfStableArrays(zero=1, one=1, limit=2))
print(s.numberOfStableArrays(zero=1, one=2, limit=1))
print(s.numberOfStableArrays(zero=3, one=3, limit=2))
