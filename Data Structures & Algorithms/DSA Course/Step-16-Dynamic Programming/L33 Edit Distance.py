class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0: return j + 1;
            if j < 0: return i + 1
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i - 1, j - 1)
            else:
                memo[(i, j)] = 1 + min(dfs(i, j - 1), dfs(i - 1, j), dfs(i - 1, j - 1))
            return memo[(i, j)]

        return dfs(m - 1, n - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[m][n]

    def minDistance3(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        prev = [0] * (n + 1)
        for j in range(n + 1):
            prev[j] = j
        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            cur[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(cur[j - 1], prev[j], prev[j - 1])
            prev = cur
        return prev[n]


# LeetCode 72
s = Solution()
print(s.minDistance(word1="horse", word2="ros"))
print(s.minDistance(word1="intention", word2="execution"))
print(s.minDistance(word1="", word2="a"))
print("---------------")
print(s.minDistance2(word1="horse", word2="ros"))
print(s.minDistance2(word1="intention", word2="execution"))
print(s.minDistance2(word1="", word2="a"))
print("---------------")
print(s.minDistance3(word1="horse", word2="ros"))
print(s.minDistance3(word1="intention", word2="execution"))
print(s.minDistance3(word1="", word2="a"))
