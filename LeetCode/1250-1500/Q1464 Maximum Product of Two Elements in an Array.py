from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


s = Solution()
print(s.maxProduct(nums=[3, 4, 5, 2]))
print(s.maxProduct(nums=[1, 5, 4, 5]))
print(s.maxProduct(nums=[3, 7]))
