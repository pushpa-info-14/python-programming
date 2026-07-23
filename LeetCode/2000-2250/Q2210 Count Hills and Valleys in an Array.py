from itertools import groupby
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l, r = 0, 1
        while r < n - 1:
            while nums[r] == nums[r + 1]:
                r += 1
            if nums[l] < nums[r] > nums[r + 1]:
                res += 1
                l = r - 1
            elif nums[l] > nums[r] < nums[r + 1]:
                res += 1
                l = r - 1
            r += 1
            l += 1
        return res


s = Solution()
print(s.countHillValley(nums=[2, 4, 1, 1, 6, 5]))  # 3
print(s.countHillValley(nums=[6, 6, 5, 5, 4, 1]))  # 0

ns = [k for k, _ in groupby([2, 4, 1, 1, 6, 5])]
print(ns)
