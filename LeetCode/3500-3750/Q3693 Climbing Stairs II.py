from functools import cache
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        inf = 10 ** 20
        costs = [0] + costs
        n += 1

        @cache
        def dfs(i):
            if i == n - 1:
                return 0
            res = inf
            if i + 1 < n:
                res = min(res, costs[i + 1] + 1 + dfs(i + 1))
            if i + 2 < n:
                res = min(res, costs[i + 2] + 4 + dfs(i + 2))
            if i + 3 < n:
                res = min(res, costs[i + 3] + 9 + dfs(i + 3))
            return res

        return dfs(0)


s = Solution()
print(s.climbStairs(n=4, costs=[1, 2, 3, 4]))
print(s.climbStairs(n=4, costs=[5, 1, 6, 2]))
print(s.climbStairs(n=3, costs=[9, 8, 3]))
