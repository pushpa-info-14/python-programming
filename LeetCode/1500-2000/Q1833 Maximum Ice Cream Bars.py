from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if cost <= coins:
                res += 1
                coins -= cost
            else:
                break
        return res


s = Solution()
print(s.maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))
print(s.maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5))
print(s.maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))
