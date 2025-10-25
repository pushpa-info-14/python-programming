from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = 0
        even = 0
        for x in nums:
            if x & 1:
                odd += 1
            else:
                even += 1
        for i in range(even):
            nums[i] = 0
        for i in range(even, len(nums)):
            nums[i] = 1
        return nums


s = Solution()
print(s.transformArray(nums=[4, 3, 2, 1]))
print(s.transformArray(nums=[1, 5, 1, 4, 2]))
