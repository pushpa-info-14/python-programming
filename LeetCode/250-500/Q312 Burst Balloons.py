from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @cache
        def dfs(i, j):
            if i > j:
                return 0
            res = 0
            for k in range(i, j + 1):
                res = max(res, nums[i - 1] * nums[k] * nums[j + 1] + dfs(i, k - 1) + dfs(k + 1, j))
            return res

        return dfs(0, n - 1)


s = Solution()
print(s.maxCoins(nums=[3, 1, 5, 8]))
print(s.maxCoins(nums=[1, 5]))
