class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:  # index is shifted by 1
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        res = ""
        i = m
        j = n
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                res += text1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return res[::-1]


# LeetCode 1143
s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))
print(s.longestCommonSubsequence("abc", "abc"))
print(s.longestCommonSubsequence("abc", "def"))
