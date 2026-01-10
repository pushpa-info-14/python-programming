from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        inf = 10 ** 10

        @cache
        def dfs(i, j):
            if i == n1 or j == n2:
                rem = 0
                for c in s1[i:]:
                    rem += ord(c)
                for c in s2[j:]:
                    rem += ord(c)
                return rem
            res = inf
            if s1[i] == s2[j]:
                res = min(res, dfs(i + 1, j + 1))
            else:
                res = min(res, ord(s1[i]) + dfs(i + 1, j), ord(s2[j]) + dfs(i, j + 1))
            return res

        return dfs(0, 0)


s = Solution()
print(s.minimumDeleteSum(s1="sea", s2="eat"))
print(s.minimumDeleteSum(s1="delete", s2="leet"))
