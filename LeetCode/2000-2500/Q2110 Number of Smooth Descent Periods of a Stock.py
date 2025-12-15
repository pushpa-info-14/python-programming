from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        res = 1
        for r in range(1, n):
            if prices[r - 1] - prices[r] != 1:
                l = r
            res += r - l + 1
        return res


s = Solution()
print(s.getDescentPeriods(prices=[3, 2, 1, 4]))
print(s.getDescentPeriods(prices=[8, 6, 7, 7]))
print(s.getDescentPeriods(prices=[1]))
