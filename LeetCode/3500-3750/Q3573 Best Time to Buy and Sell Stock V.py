from functools import cache
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        inf = 10 ** 10
        n = len(prices)
        none, normal, short_selling = tuple(range(3))

        @cache
        def dp(i, transactions, action):
            if i == n:
                return 0 if action == none else -inf
            if action == none:
                if transactions == 0:
                    return 0
                return max(
                    dp(i + 1, transactions, none),
                    dp(i + 1, transactions - 1, normal) - prices[i],
                    dp(i + 1, transactions - 1, short_selling) + prices[i],
                )
            elif action == normal:
                return max(
                    dp(i + 1, transactions, none) + prices[i],
                    dp(i + 1, transactions, normal)
                )
            else:
                return max(
                    dp(i + 1, transactions, none) - prices[i],
                    dp(i + 1, transactions, short_selling)
                )

        ret = dp(0, k, none)
        dp.cache_clear()
        return ret

    def maximumProfit2(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]

        # Initialize the state on day 0
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
            dp[0][j][2] = prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(
                    dp[i - 1][j][0],
                    max(dp[i - 1][j][1] + prices[i], dp[i - 1][j][2] - prices[i]),
                )
                dp[i][j][1] = max(
                    dp[i - 1][j][1],
                    dp[i - 1][j - 1][0] - prices[i]
                )
                dp[i][j][2] = max(
                    dp[i - 1][j][2],
                    dp[i - 1][j - 1][0] + prices[i]
                )
        return dp[n - 1][k][0]

    def maximumProfit3(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(k + 1)]

        # Initialize the state on day 0
        for j in range(1, k + 1):
            dp[j][1] = -prices[0]
            dp[j][2] = prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], max(dp[j][1] + prices[i], dp[j][2] - prices[i]))
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + prices[i])

        return dp[k][0]


s = Solution()
print(s.maximumProfit(prices=[1, 7, 9, 8, 2], k=2))
print(s.maximumProfit(prices=[12, 16, 19, 19, 8, 1, 19, 13, 9], k=3))
print(s.maximumProfit2(prices=[1, 7, 9, 8, 2], k=2))
print(s.maximumProfit2(prices=[12, 16, 19, 19, 8, 1, 19, 13, 9], k=3))
print(s.maximumProfit3(prices=[1, 7, 9, 8, 2], k=2))
print(s.maximumProfit3(prices=[12, 16, 19, 19, 8, 1, 19, 13, 9], k=3))
