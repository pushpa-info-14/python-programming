from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        res = 0
        for i in range(n - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a + b > c and a + c > b and b + c > a:
                return a + b + c
        return res


s = Solution()
print(s.largestPerimeter(nums=[2, 1, 2]))
print(s.largestPerimeter(nums=[1, 2, 1, 10]))
print(s.largestPerimeter(nums=[3, 2, 3, 4]))
print(s.largestPerimeter(nums=[3, 6, 2, 3]))
