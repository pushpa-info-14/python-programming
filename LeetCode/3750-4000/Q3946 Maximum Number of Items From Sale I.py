from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        counter = defaultdict(int)
        n = len(items)
        for index1, item1 in enumerate(items):
            for index2, item2 in enumerate(items):
                if index1 != index2:
                    if item1[0] % item2[0] == 0:
                        counter[index2] += 1

        @cache
        def dp(left, idx):
            if idx == n or left == 0:
                return 0
            pick, pick_again = 0, 0
            if items[idx][1] <= left:
                pick = 1 + counter[idx] + dp(left - items[idx][1], idx + 1)
                pick_again = 1 + dp(left - items[idx][1], idx)
            not_pick = dp(left, idx + 1)
            return max(pick, not_pick, pick_again)

        res = dp(budget, 0)
        dp.cache_clear()
        return res


s = Solution()
print(s.maximumSaleItems(items=[[6, 2], [2, 6], [3, 4]], budget=9))
print(s.maximumSaleItems(items=[[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], budget=8))
