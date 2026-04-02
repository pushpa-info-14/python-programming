from functools import cache
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        inf = 10 ** 10

        @cache
        def dfs(i, j, k):
            if i == m or j == n:
                return -inf
            if i == m - 1 and j == n - 1:
                cur = coins[i][j]
                if k:
                    cur = max(cur, 0)
                return cur
            cur = coins[i][j] + max(dfs(i + 1, j, k), dfs(i, j + 1, k))
            if k and coins[i][j] < 0:
                cur = max(cur, 0 + max(dfs(i + 1, j, k - 1), dfs(i, j + 1, k - 1)))
            return cur

        res = dfs(0, 0, 2)
        dfs.cache_clear()
        return res

    def maximumAmount2(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        inf = 10 ** 10

        dp = [[[-inf] * 3 for _ in range(n + 1)] for _ in range(m + 1)]
        for k in range(3):
            cur = coins[m - 1][n - 1]
            if k:
                cur = max(cur, 0)
            dp[m - 1][n - 1][k] = cur

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                for k in range(3):
                    dp[i][j][k] = coins[i][j] + max(dp[i + 1][j][k], dp[i][j + 1][k])
                    if k and coins[i][j] < 0:
                        dp[i][j][k] = max(dp[i][j][k], 0 + max(dp[i + 1][j][k - 1], dp[i][j + 1][k - 1]))

        return max(dp[0][0])


s = Solution()
print(s.maximumAmount(coins=[[0, 1, -1], [1, -2, 3], [2, -3, 4]]))
print(s.maximumAmount(coins=[[10, 10, 10], [10, 10, 10]]))
print(s.maximumAmount(coins=[[-7, 12, 12, 13], [-6, 19, 19, -6], [9, -2, -10, 16], [-4, 14, -10, -9]]))
print("--------------")
print(s.maximumAmount2(coins=[[0, 1, -1], [1, -2, 3], [2, -3, 4]]))
print(s.maximumAmount2(coins=[[10, 10, 10], [10, 10, 10]]))
print(s.maximumAmount2(coins=[[-7, 12, 12, 13], [-6, 19, 19, -6], [9, -2, -10, 16], [-4, 14, -10, -9]]))
