from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = list(accumulate(stones))

        @cache
        def dfs(i):
            if i == n - 1:
                return prefix_sum[i]
            return max(dfs(i + 1), prefix_sum[i] - dfs(i + 1))

        return dfs(1)


s = Solution()
print(s.stoneGameVIII(stones=[-1, 2, -3, 4, -5]))
print(s.stoneGameVIII(stones=[7, -6, 5, 10, 5, -2, -6]))
print(s.stoneGameVIII(stones=[-10, -12]))
