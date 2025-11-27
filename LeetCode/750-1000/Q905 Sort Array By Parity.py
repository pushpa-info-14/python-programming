from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            while l < r and nums[l] & 1 == 0:
                l += 1
            while l < r and nums[r] & 1:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


s = Solution()
print(s.sortArrayByParity(nums=[3, 1, 2, 4]))
print(s.sortArrayByParity(nums=[0]))
print(s.sortArrayByParity(nums=[0, 2]))
print(s.sortArrayByParity(nums=[0, 1]))
print(s.sortArrayByParity2(nums=[3, 1, 2, 4]))
print(s.sortArrayByParity2(nums=[0]))
print(s.sortArrayByParity2(nums=[0, 2]))
print(s.sortArrayByParity2(nums=[0, 1]))
