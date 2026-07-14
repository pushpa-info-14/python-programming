from functools import cache
from math import gcd
from typing import List


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)

        @cache
        def dfs(g1, g2, i):
            if i == n:
                if g1 == 0 or g2 == 0 or g1 != g2:
                    return 0
                return 1
            res1 = dfs(gcd(g1, nums[i]), g2, i + 1)
            res2 = dfs(g1, (gcd(g2, nums[i])), i + 1)
            res3 = dfs(g1, g2, i + 1)
            return (res1 + res2 + res3) % mod

        return dfs(0, 0, 0)


s = Solution()
print(s.subsequencePairCount(nums=[1, 2, 3, 4]))
print(s.subsequencePairCount(nums=[10, 20, 30]))
print(s.subsequencePairCount(nums=[1, 1, 1, 1]))
