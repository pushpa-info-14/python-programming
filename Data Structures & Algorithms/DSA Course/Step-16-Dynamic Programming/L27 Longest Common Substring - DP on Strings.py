class Solution:
    def lengthOfLongestCommonSubstring(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res

    def lengthOfLongestCommonSubstring2(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        prev = [0] * (n + 1)
        res = 0
        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                    res = max(res, cur[j])
                else:
                    cur[j] = 0
            prev = cur
        return res

    def longestCommonSubstring(self, text1: str, text2: str) -> int:
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
        cur = ""
        i = m
        j = n
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                while i > 0 and j > 0 and text1[i - 1] == text2[j - 1]:
                    cur += text1[i - 1]
                    i -= 1
                    j -= 1
                if len(res) < len(cur):
                    res = cur
                cur = ""
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return res[::-1]


s = Solution()
print(s.lengthOfLongestCommonSubstring("abcde", "ace"))
print(s.lengthOfLongestCommonSubstring("abc", "abc"))
print(s.lengthOfLongestCommonSubstring("abc", "def"))
print("---------------------")
print(s.lengthOfLongestCommonSubstring2("abcde", "ace"))
print(s.lengthOfLongestCommonSubstring2("abc", "abc"))
print(s.lengthOfLongestCommonSubstring2("abc", "def"))
print("---------------------")
print(s.longestCommonSubstring("abcde", "ace"))
print(s.longestCommonSubstring("abc", "abc"))
print(s.longestCommonSubstring("abc", "def"))
