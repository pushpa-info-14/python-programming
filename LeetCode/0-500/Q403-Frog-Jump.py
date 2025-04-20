from collections import defaultdict
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = defaultdict(set)
        dp[1].add(1)

        for i in range(1, n):
            jump_sizes = dp[stones[i]].copy()
            for jump_size in jump_sizes:
                dp[stones[i] + jump_size].add(jump_size)
                dp[stones[i] + jump_size - 1].add(jump_size - 1)
                dp[stones[i] + jump_size + 1].add(jump_size + 1)
        return len(dp[stones[-1]]) != 0


s = Solution()
print(s.canCross([0, 1, 3, 5, 6, 8, 12, 17]))
print(s.canCross([0, 1, 2, 3, 4, 8, 9, 11]))
print(s.canCross([0, 2]))
