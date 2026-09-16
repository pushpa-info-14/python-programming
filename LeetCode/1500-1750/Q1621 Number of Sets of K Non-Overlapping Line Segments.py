import math
from functools import cache


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dfs(i, segments, first):
            if segments == k:
                return 1
            if i == n:
                return 0
            cur = dfs(i + 1, segments, first)
            if first:
                cur += dfs(i + 1, segments, False)
            else:
                cur += dfs(i, segments + 1, True)

            return cur % mod

        return dfs(0, 0, True)

    def numberOfSets2(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        return math.comb(n + k - 1, k * 2) % mod


s = Solution()
print(s.numberOfSets(n=4, k=2))
print(s.numberOfSets(n=3, k=1))
print(s.numberOfSets(n=30, k=7))
print(s.numberOfSets(n=573, k=46))
print("------------")
print(s.numberOfSets2(n=4, k=2))
print(s.numberOfSets2(n=3, k=1))
print(s.numberOfSets2(n=30, k=7))
print(s.numberOfSets2(n=573, k=46))
