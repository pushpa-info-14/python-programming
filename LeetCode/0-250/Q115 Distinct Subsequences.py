class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            if j < 0: return 1
            if i < 0: return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = dfs(i - 1, j - 1) + dfs(i - 1, j)
            else:
                dp[i][j] = dfs(i - 1, j)
            return dp[i][j]

        return dfs(m - 1, n - 1)

    def numDistinct2(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]

    def numDistinct3(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        prev = [0] * (n + 1)
        prev[0] = 1
        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            cur[0] = 1
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    cur[j] = prev[j - 1] + prev[j]
                else:
                    cur[j] = prev[j]
            prev = cur
        return prev[n]


# LeetCode 115
s = Solution()
print(s.numDistinct(s="rabbbit", t="rabbit"))
print(s.numDistinct(s="babgbag", t="bag"))
print("---------------------")
print(s.numDistinct2(s="rabbbit", t="rabbit"))
print(s.numDistinct2(s="babgbag", t="bag"))
print("---------------------")
print(s.numDistinct3(s="rabbbit", t="rabbit"))
print(s.numDistinct3(s="babgbag", t="bag"))
