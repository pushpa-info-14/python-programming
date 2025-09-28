from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = 0
        for c, b, a in zip(nums, nums[1:], nums[2:]):
            if a + b > c:
                return a + b + c
        return res


s = Solution()
print(s.largestPerimeter(nums=[2, 1, 2]))
print(s.largestPerimeter(nums=[1, 2, 1, 10]))
print(s.largestPerimeter(nums=[3, 2, 3, 4]))
print(s.largestPerimeter(nums=[3, 6, 2, 3]))
