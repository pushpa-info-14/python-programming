from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


s = Solution()
print(s.maxProductDifference(nums=[5, 6, 2, 7, 4]))
print(s.maxProductDifference(nums=[4, 2, 5, 9, 7, 4, 8]))
