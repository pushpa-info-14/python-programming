from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, can_buy):
            if i == n:
                return 0
            if (i, can_buy) in memo:
                return memo[(i, can_buy)]
            if can_buy:
                memo[(i, can_buy)] = max(dfs(i + 1, True), -prices[i] + dfs(i + 1, False))
            else:
                memo[(i, can_buy)] = max(dfs(i + 1, False), prices[i] - fee + dfs(i + 1, True))
            return memo[(i, can_buy)]

        return dfs(0, True)


s = Solution()
print(s.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
print(s.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
