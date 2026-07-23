from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0
        for i in range(1, n):
            max_diff = max(max_diff, abs(nums[i - 1] - nums[i]))
        max_diff = max(max_diff, abs(nums[0] - nums[n - 1]))

        return max_diff


s = Solution()
print(s.maxAdjacentDistance([1, 2, 4]))
print(s.maxAdjacentDistance([-5, -10, -5]))
