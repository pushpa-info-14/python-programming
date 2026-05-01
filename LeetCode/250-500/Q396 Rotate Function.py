from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        prev = 0
        for i in range(n):
            total += nums[i]
            prev += i * nums[i]
        res = prev  # f(0)
        for i in range(n - 1, 0, -1):
            prev = prev + (total - nums[i]) - (n - 1) * nums[i]
            res = max(res, prev)
        return res


s = Solution()
print(s.maxRotateFunction(nums=[4, 3, 2, 6]))
print(s.maxRotateFunction(nums=[100]))
