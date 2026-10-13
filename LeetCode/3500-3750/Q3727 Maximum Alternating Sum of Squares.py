from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted([num ** 2 for num in nums])
        res = 0
        for i in range(n // 2):
            res -= nums[i]
        for i in range(n // 2, n):
            res += nums[i]
        return res


s = Solution()
print(s.maxAlternatingSum(nums=[1, 2, 3]))  # 12
print(s.maxAlternatingSum(nums=[1, -1, 2, -2, 3, -3]))  # 16
