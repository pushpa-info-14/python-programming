from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, buy, limit):
            if (i, buy, limit) in memo:
                return memo[(i, buy, limit)]
            if i == n or limit == 0:
                return 0
            if buy:
                memo[(i, buy, limit)] = max(dfs(i + 1, 1, limit), - prices[i] + dfs(i + 1, 0, limit))
            else:
                memo[(i, buy, limit)] = max(dfs(i + 1, 0, limit), prices[i] + dfs(i + 1, 1, limit - 1))
            return memo[(i, buy, limit)]

        return dfs(0, 1, 2)

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for limit in range(1, 3):
                    if buy == 1:
                        dp[i][buy][limit] = max(dp[i + 1][1][limit], - prices[i] + dp[i + 1][0][limit])
                    else:
                        dp[i][buy][limit] = max(dp[i + 1][0][limit], prices[i] + dp[i + 1][1][limit - 1])

        return dp[0][1][2]

    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0] * 3 for _ in range(2)]

        for i in range(n - 1, -1, -1):
            cur = [[0] * 3 for _ in range(2)]
            for buy in range(2):
                for limit in range(1, 3):
                    if buy == 1:
                        cur[buy][limit] = max(ahead[1][limit], - prices[i] + ahead[0][limit])
                    else:
                        cur[buy][limit] = max(ahead[0][limit], prices[i] + ahead[1][limit - 1])
            ahead = cur
        return ahead[1][2]


# LeetCode 123
s = Solution()
print(s.maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit(prices=[1, 2, 3, 4, 5]))
print(s.maxProfit(prices=[7, 6, 4, 3, 1]))
print("------------------------")
print(s.maxProfit2(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit2(prices=[1, 2, 3, 4, 5]))
print(s.maxProfit2(prices=[7, 6, 4, 3, 1]))
print("------------------------")
print(s.maxProfit3(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit3(prices=[1, 2, 3, 4, 5]))
print(s.maxProfit3(prices=[7, 6, 4, 3, 1]))
