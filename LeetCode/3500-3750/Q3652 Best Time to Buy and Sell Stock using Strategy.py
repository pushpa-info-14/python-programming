from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        pre_sum = [0] * (n + 1)
        pre_profit = [0] * (n + 1)
        for i in range(n):
            pre_profit[i + 1] = prices[i] * strategy[i] + pre_profit[i]
            pre_sum[i + 1] = prices[i] + pre_sum[i]

        original = pre_profit[n] - pre_profit[0]
        res = original
        for i in range(0, n - k + 1):
            cur = original - (pre_profit[i + k] - pre_profit[i]) + (pre_sum[i + k] - pre_sum[i + (k // 2)])
            res = max(res, cur)
        return res


s = Solution()
print(s.maxProfit(prices=[4, 2, 8], strategy=[-1, 0, 1], k=2))  # 10
print(s.maxProfit(prices=[5, 4, 3], strategy=[1, 1, 0], k=2))  # 9
print(s.maxProfit(prices=[5, 8], strategy=[-1, -1], k=2))  # 8
print(s.maxProfit(prices=[4, 7, 13], strategy=[-1, -1, 0], k=2))  # 9
