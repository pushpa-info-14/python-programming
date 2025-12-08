from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)
        prefix = nums[0]
        i = 1
        while i < n and nums[i - 1] + 1 == nums[i]:
            prefix += nums[i]
            i += 1
        while prefix in seen:
            prefix += 1
        return prefix


s = Solution()
print(s.missingInteger(nums=[1, 2, 3, 2, 5]))
print(s.missingInteger(nums=[3, 4, 5, 1, 12, 14, 13]))
print(s.missingInteger(nums=[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 9]))
