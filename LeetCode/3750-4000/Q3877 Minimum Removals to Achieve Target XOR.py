from functools import cache
from typing import List


class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, val):
            if i == n:
                if val == target:
                    return 0
                else:
                    return -1
            x = dfs(i + 1, val)
            y = dfs(i + 1, val ^ nums[i])
            if y != -1:
                y += 1
            return max(x, y)

        res = dfs(0, 0)
        return n - res if res != -1 else -1


s = Solution()
print(s.minRemovals(nums=[1, 2, 3], target=2))
print(s.minRemovals(nums=[2, 4], target=1))
print(s.minRemovals(nums=[7], target=7))
print(s.minRemovals(nums=[80, 15, 37, 4, 33, 43, 43, 98, 49, 105, 16, 173, 110, 65], target=132))
