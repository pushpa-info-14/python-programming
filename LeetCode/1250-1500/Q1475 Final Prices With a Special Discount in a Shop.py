from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        res = prices.copy()
        for i in reversed(range(n)):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                res[i] -= stack[-1]
            stack.append(prices[i])
        return res


s = Solution()
print(s.finalPrices(prices=[8, 4, 6, 2, 3]))
print(s.finalPrices(prices=[1, 2, 3, 4, 5]))
print(s.finalPrices(prices=[10, 1, 1, 6]))
