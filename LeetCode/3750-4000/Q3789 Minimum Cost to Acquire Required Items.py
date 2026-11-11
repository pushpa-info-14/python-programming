class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        min_need = min(need1, need2)
        res = min(costBoth, cost1 + cost2) * min_need
        if need1 > min_need:
            res += min(costBoth, cost1) * (need1 - min_need)
        elif need2 > min_need:
            res += min(costBoth, cost2) * (need2 - min_need)
        return res


s = Solution()
print(s.minimumCost(cost1=3, cost2=2, costBoth=1, need1=3, need2=2))
print(s.minimumCost(cost1=5, cost2=4, costBoth=15, need1=2, need2=3))
print(s.minimumCost(cost1=5, cost2=4, costBoth=15, need1=0, need2=0))
