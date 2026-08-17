from functools import cache
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = stoneValue[i] + prefix_sum[i]

        @cache
        def dfs(l, r):
            if l == r:
                return 0
            cur = 0
            for m in range(l, r):
                l_sum = prefix_sum[m + 1] - prefix_sum[l]
                r_sum = prefix_sum[r + 1] - prefix_sum[m + 1]
                if l_sum > r_sum:
                    cur = max(cur, r_sum + dfs(m + 1, r))
                elif l_sum < r_sum:
                    cur = max(cur, l_sum + dfs(l, m))
                else:
                    cur = max(cur, l_sum + max(dfs(l, m), dfs(m + 1, r)))

                if 2 * min(l_sum, r_sum) <= cur:
                    break
            return cur

        return dfs(0, n - 1)


s = Solution()
print(s.stoneGameV(stoneValue=[6, 2, 3, 4, 5, 5]))
print(s.stoneGameV(stoneValue=[7, 7, 7, 7, 7, 7, 7]))
print(s.stoneGameV(stoneValue=[4]))
