class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10 ** 9 + 7
        r -= l
        dp = [[0] * (r + 1) for _ in range(n)]
        for j in range(r + 1):
            dp[0][j] = 1
        for i in range(1, n):
            prev = 0
            if i % 2 == 1:
                for j in range(r + 1):
                    dp[i][j] = prev
                    prev = (prev + dp[i - 1][j]) % mod
            else:
                for j in range(r, -1, -1):
                    dp[i][j] = prev
                    prev = (prev + dp[i - 1][j]) % mod

        return sum(dp[-1] * 2) % mod


s = Solution()
print(s.zigZagArrays(n=3, l=4, r=5))
print(s.zigZagArrays(n=3, l=1, r=3))
