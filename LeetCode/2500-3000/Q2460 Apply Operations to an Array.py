from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        cnt = 0
        j = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[j] = nums[i]
                j += 1
        while j < n:
            nums[j] = 0
            j += 1
        return nums

    def applyOperations2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0
        for i in range(n):
            if nums[i]:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        return nums


s = Solution()
print(s.applyOperations([1, 2, 2, 1, 1, 0]))
print(s.applyOperations2([1, 2, 2, 1, 1, 0]))
print(s.applyOperations([0, 1]))
print(s.applyOperations2([0, 1]))
