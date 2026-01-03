from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, can_buy):
            if i >= n:
                return 0

            if (i, can_buy) in memo:
                return memo[(i, can_buy)]
            if can_buy:
                memo[(i, can_buy)] = max(dfs(i + 1, True), -prices[i] + dfs(i + 1, False))
            else:
                memo[(i, can_buy)] = max(dfs(i + 1, False), prices[i] + dfs(i + 2, True))
            return memo[(i, can_buy)]

        return dfs(0, True)


s = Solution()
print(s.maxProfit(prices=[1, 2, 3, 0, 2]))
print(s.maxProfit(prices=[1]))
