class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i - 1, j - 1)
            else:
                dp[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))
            return dp[i][j]

        return dfs(m - 1, n - 1)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]: # index is shifted by 1
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]

    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]: # index is shifted by 1
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(cur[j - 1], prev[j])
            prev = cur
        return prev[n]

    def longestCommonSubsequence4(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


# LeetCode 1143
s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))
print(s.longestCommonSubsequence("abc", "abc"))
print(s.longestCommonSubsequence("abc", "def"))
print("------------------")
print(s.longestCommonSubsequence2("abcde", "ace"))
print(s.longestCommonSubsequence2("abc", "abc"))
print(s.longestCommonSubsequence2("abc", "def"))
print("------------------")
print(s.longestCommonSubsequence3("abcde", "ace"))
print(s.longestCommonSubsequence3("abc", "abc"))
print(s.longestCommonSubsequence3("abc", "def"))
print("------------------")
print(s.longestCommonSubsequence4("abcde", "ace"))
print(s.longestCommonSubsequence4("abc", "abc"))
print(s.longestCommonSubsequence4("abc", "def"))
