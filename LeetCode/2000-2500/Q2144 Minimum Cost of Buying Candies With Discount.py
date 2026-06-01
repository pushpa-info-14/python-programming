from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse=True)
        res = 0
        for i in range(0, n, 3):
            res += cost[i]
            if i + 1 < n:
                res += cost[i + 1]
        return res


s = Solution()
print(s.minimumCost(cost=[1, 2, 3]))
print(s.minimumCost(cost=[6, 5, 7, 9, 2, 2]))
print(s.minimumCost(cost=[5, 5]))
print(s.minimumCost(cost=[5]))
