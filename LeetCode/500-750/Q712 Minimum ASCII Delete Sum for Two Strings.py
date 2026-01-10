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

    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        # min sum = sum(ord chars) - ord(max string that is equal)
        for i in range(len(s2) - 1, -1, - 1):
            for j in range(len(s1) - 1, -1, -1):
                if s2[i] == s1[j]:
                    dp[i][j] = ord(s2[i]) + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        sum_s1 = 0
        sum_s2 = 0
        for c in s1:
            sum_s1 += ord(c)
        for c in s2:
            sum_s2 += ord(c)
        return sum_s1 + sum_s2 - 2 * dp[0][0]


s = Solution()
print(s.minimumDeleteSum(s1="sea", s2="eat"))
print(s.minimumDeleteSum(s1="delete", s2="leet"))
print("---------------------------")
print(s.minimumDeleteSum2(s1="sea", s2="eat"))
print(s.minimumDeleteSum2(s1="delete", s2="leet"))
