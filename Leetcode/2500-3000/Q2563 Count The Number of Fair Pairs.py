from typing import List


class Solution:
    def countFairPairs2(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                if lower <= nums[i] + nums[j] <= upper:
                    res += 1
        return res

    @staticmethod
    def lessThanCount(nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        left, right = 0, n - 1
        while left < right:
            summation = nums[left] + nums[right]
            if summation < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lessThanCount(nums, upper + 1) - self.lessThanCount(nums, lower)


s = Solution()
print(s.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6))
print(s.countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11))

print(s.countFairPairs2(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6))
print(s.countFairPairs2(nums=[1, 7, 9, 2, 5], lower=11, upper=11))
