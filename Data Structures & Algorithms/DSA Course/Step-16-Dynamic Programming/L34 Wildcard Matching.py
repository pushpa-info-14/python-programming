class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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
                for x in range(j + 1):
                    if p[x] != '*':
                        return False
                return True

            memo[(i, j)] = False
            if s[i] == p[j] or p[j] == '?':
                memo[(i, j)] = dfs(i - 1, j - 1)
            elif p[j] == '*':
                memo[(i, j)] = dfs(i, j - 1) or dfs(i - 1, j)
            return memo[(i, j)]

        return dfs(m - 1, n - 1)


s = Solution()
print(s.isMatch(s="aa", p="a"))
print(s.isMatch(s="aa", p="*"))
print(s.isMatch(s="cb", p="?a"))
print(s.isMatch(s="aab", p="c*a*b"))
print(s.isMatch(s="", p="******"))
print(s.isMatch(s="ho", p="**ho"))
