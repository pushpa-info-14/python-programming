class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        ans = ""
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans += str1[i - 1]
                i -= 1
                j -= 1
            elif dp[i][j - 1] > dp[i - 1][j]:
                ans += str2[j - 1]
                j -= 1
            else:
                ans += str1[i - 1]
                i -= 1
        while i > 0:
            ans += str1[i - 1]
            i -= 1
        while j > 0:
            ans += str2[j - 1]
            j -= 1

        return ans[::-1]


# LeetCode 1092
s = Solution()
print(s.shortestCommonSupersequence("abac", "cab"))
print(s.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))
print(s.shortestCommonSupersequence("aaaaaaaaa", "aaaaaaaa"))
