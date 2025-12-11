from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[-3] * nums[-2] * nums[-1]
        y = nums[0] * nums[1] * nums[-1]
        return max(x, y)


s = Solution()
print(s.maximumProduct(nums=[1, 2, 3]))
print(s.maximumProduct(nums=[1, 2, 3, 4]))
print(s.maximumProduct(nums=[-1, -2, -3]))
print(s.maximumProduct(nums=[-1, -2, -300, -200, 1, 2, 3]))
print(s.maximumProduct(nums=[-8, -7, -2, 10, 20]))
