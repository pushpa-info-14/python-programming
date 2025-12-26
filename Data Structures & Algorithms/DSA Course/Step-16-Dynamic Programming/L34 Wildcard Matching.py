import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub(r'\*+', '*', p)
        m = len(s)
        n = len(p)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0 and j < 0:
                return True
            elif i >= 0 > j:
                return False
            elif i < 0 <= j:
                return j == 0 and p[j] == '*'

            memo[(i, j)] = False
            if s[i] == p[j] or p[j] == '?':
                memo[(i, j)] = dfs(i - 1, j - 1)
            elif p[j] == '*':
                memo[(i, j)] = dfs(i, j - 1) or dfs(i - 1, j)
            return memo[(i, j)]

        return dfs(m - 1, n - 1)

    def isMatch2(self, s: str, p: str) -> bool:
        # shifted by 1
        p = re.sub(r'\*+', '*', p)
        m = len(s)
        n = len(p)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            if i == 0 and j == 0:
                return True
            elif j == 0 < i:
                return False
            elif i == 0 < j:
                return j == 1 and p[j - 1] == '*'

            dp[i][j] = False
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dfs(i - 1, j - 1)
            elif p[j - 1] == '*':
                dp[i][j] = dfs(i, j - 1) or dfs(i - 1, j)
            return dp[i][j]

        return dfs(m, n)

    def isMatch3(self, s: str, p: str) -> bool:
        p = re.sub(r'\*+', '*', p)
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = False
        for j in range(1, n + 1):
            dp[0][j] = j == 1 and p[j - 1] == '*'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[m][n]

    def isMatch4(self, s: str, p: str) -> bool:
        p = re.sub(r'\*+', '*', p)
        m = len(s)
        n = len(p)
        prev = [False] * (n + 1)
        prev[0] = True
        for j in range(1, n + 1):
            prev[j] = j == 1 and p[j - 1] == '*'
        for i in range(1, m + 1):
            cur = [False] * (n + 1)
            cur[0] = False
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    cur[j] = prev[j - 1]
                elif p[j - 1] == '*':
                    cur[j] = cur[j - 1] or prev[j]
            prev = cur
        return prev[n]


s = Solution()
print(s.isMatch(s="aa", p="a"))
print(s.isMatch(s="aa", p="*"))
print(s.isMatch(s="cb", p="?a"))
print(s.isMatch(s="aab", p="c*a*b"))
print(s.isMatch(s="", p="******"))
print(s.isMatch(s="ho", p="**ho"))
print("------------")
print(s.isMatch2(s="aa", p="a"))
print(s.isMatch2(s="aa", p="*"))
print(s.isMatch2(s="cb", p="?a"))
print(s.isMatch2(s="aab", p="c*a*b"))
print(s.isMatch2(s="", p="******"))
print(s.isMatch2(s="ho", p="**ho"))
print("------------")
print(s.isMatch3(s="aa", p="a"))
print(s.isMatch3(s="aa", p="*"))
print(s.isMatch3(s="cb", p="?a"))
print(s.isMatch3(s="aab", p="c*a*b"))
print(s.isMatch3(s="", p="******"))
print(s.isMatch3(s="ho", p="**ho"))
print("------------")
print(s.isMatch4(s="aa", p="a"))
print(s.isMatch4(s="aa", p="*"))
print(s.isMatch4(s="cb", p="?a"))
print(s.isMatch4(s="aab", p="c*a*b"))
print(s.isMatch4(s="", p="******"))
print(s.isMatch4(s="ho", p="**ho"))
