from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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

        return dfs(0, 1, k)

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for limit in range(1, k + 1):
                    if buy == 1:
                        dp[i][buy][limit] = max(dp[i + 1][1][limit], - prices[i] + dp[i + 1][0][limit])
                    else:
                        dp[i][buy][limit] = max(dp[i + 1][0][limit], prices[i] + dp[i + 1][1][limit - 1])

        return dp[0][1][k]

    def maxProfit3(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0] * 3 for _ in range(2)]

        for i in range(n - 1, -1, -1):
            cur = [[0] * 3 for _ in range(2)]
            for buy in range(2):
                for limit in range(1, k + 1):
                    if buy == 1:
                        cur[buy][limit] = max(ahead[1][limit], - prices[i] + ahead[0][limit])
                    else:
                        cur[buy][limit] = max(ahead[0][limit], prices[i] + ahead[1][limit - 1])
            ahead = cur
        return ahead[1][k]

    def maxProfit4(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, transaction):
            if (i, transaction) in memo:
                return memo[(i, transaction)]
            if i == n or transaction == 0:
                return 0
            if transaction % 2 == 0:  # buy
                memo[(i, transaction)] = max(dfs(i + 1, transaction), - prices[i] + dfs(i + 1, transaction - 1))
            else:
                memo[(i, transaction)] = max(dfs(i + 1, transaction), prices[i] + dfs(i + 1, transaction - 1))
            return memo[(i, transaction)]

        return dfs(0, 2 * k)

    def maxProfit5(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (2 * k + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for transaction in range(1, 2 * k + 1):
                if transaction % 2 == 0:  # buy
                    dp[i][transaction] = max(dp[i + 1][transaction], - prices[i] + dp[i + 1][transaction - 1])
                else:
                    dp[i][transaction] = max(dp[i + 1][transaction], prices[i] + dp[i + 1][transaction - 1])
        return dp[0][2 * k]


# LeetCode 188
s = Solution()
print(s.maxProfit(k=2, prices=[2, 4, 1]))
print(s.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
print("------------------------")
print(s.maxProfit2(k=2, prices=[2, 4, 1]))
print(s.maxProfit2(k=2, prices=[3, 2, 6, 5, 0, 3]))
print("------------------------")
print(s.maxProfit3(k=2, prices=[2, 4, 1]))
print(s.maxProfit3(k=2, prices=[3, 2, 6, 5, 0, 3]))
print("------------------------")
print(s.maxProfit4(k=2, prices=[2, 4, 1]))
print(s.maxProfit4(k=2, prices=[3, 2, 6, 5, 0, 3]))
print("------------------------")
print(s.maxProfit5(k=2, prices=[2, 4, 1]))
print(s.maxProfit5(k=2, prices=[3, 2, 6, 5, 0, 3]))
