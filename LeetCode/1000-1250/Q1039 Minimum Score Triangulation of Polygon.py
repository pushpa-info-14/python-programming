from functools import cache
from math import inf
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(i, j):
            if j - i == 1: return 0
            res = inf
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])
            return res

        return dfs(0, len(values) - 1)

    def minScoreTriangulation2(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = min((dp[i][k] + dp[k][j] + values[i] * values[j] * values[k] for k in range(i + 1, j)))

        return dp[0][n - 1]


s = Solution()
print(s.minScoreTriangulation(values=[1, 2, 3]))
print(s.minScoreTriangulation(values=[3, 7, 4, 5]))
print(s.minScoreTriangulation(values=[1, 3, 1, 4, 1, 5]))
print(s.minScoreTriangulation2(values=[1, 2, 3]))
print(s.minScoreTriangulation2(values=[3, 7, 4, 5]))
print(s.minScoreTriangulation2(values=[1, 3, 1, 4, 1, 5]))
