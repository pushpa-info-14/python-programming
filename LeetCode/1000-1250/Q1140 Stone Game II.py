from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        inf = 10 ** 10
        n = len(piles)
        suffix_sum = piles[:]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        @cache
        def dfs(index, m):
            if index + 2 * m >= n:
                return suffix_sum[index]
            res = inf
            for x in range(1, 2 * m + 1):
                res = min(res, dfs(index + x, max(x, m)))
            return suffix_sum[index] - res

        return dfs(0, 1)


s = Solution()
print(s.stoneGameII(piles=[2, 7, 9, 4, 4]))
print(s.stoneGameII(piles=[1, 2, 3, 4, 5, 100]))
