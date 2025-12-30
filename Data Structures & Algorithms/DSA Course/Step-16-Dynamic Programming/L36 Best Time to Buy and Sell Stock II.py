from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, buy):
            if (i, buy) in memo:
                return memo[(i, buy)]
            if i == n:
                return 0
            if buy:
                memo[(i, buy)] = max(dfs(i + 1, 1), - prices[i] + dfs(i + 1, 0))
            else:
                memo[(i, buy)] = max(dfs(i + 1, 0), prices[i] + dfs(i + 1, 1))
            return memo[(i, buy)]

        return dfs(0, 1)

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    dp[i][buy] = max(dp[i + 1][1], - prices[i] + dp[i + 1][0])
                else:
                    dp[i][buy] = max(dp[i + 1][0], prices[i] + dp[i + 1][1])

        return dp[0][1]

    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        ahead = [0] * 2

        for i in range(n - 1, -1, -1):
            cur = [0] * 2
            for buy in range(2):
                if buy == 1:
                    cur[buy] = max(ahead[1], - prices[i] + ahead[0])
                else:
                    cur[buy] = max(ahead[0], prices[i] + ahead[1])
            ahead = cur
        return ahead[1]


# LeetCode 122
s = Solution()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(s.maxProfit(prices=[1, 2, 3, 4, 5]))
print(s.maxProfit(prices=[7, 6, 4, 3, 1]))
print("------------------------")
print(s.maxProfit2(prices=[7, 1, 5, 3, 6, 4]))
print(s.maxProfit2(prices=[1, 2, 3, 4, 5]))
print(s.maxProfit2(prices=[7, 6, 4, 3, 1]))
print("------------------------")
print(s.maxProfit3(prices=[7, 1, 5, 3, 6, 4]))
print(s.maxProfit3(prices=[1, 2, 3, 4, 5]))
print(s.maxProfit3(prices=[7, 6, 4, 3, 1]))
