from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return -1
        nums.sort()
        return nums[1]

    def findNonMinOrMax2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return -1
        return sorted([nums[0], nums[1], nums[2]])[1]


s = Solution()
print(s.findNonMinOrMax(nums=[3, 2, 1, 4]))
print(s.findNonMinOrMax(nums=[1, 2]))
print(s.findNonMinOrMax(nums=[2, 1, 3]))
print(s.findNonMinOrMax2(nums=[3, 2, 1, 4]))
print(s.findNonMinOrMax2(nums=[1, 2]))
print(s.findNonMinOrMax2(nums=[2, 1, 3]))
