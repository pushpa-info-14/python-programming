from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)
        return profit


# LeetCode 121
s = Solution()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(s.maxProfit(prices=[7, 6, 4, 3, 1]))
