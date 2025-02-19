import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -math.inf
        cur_sum = 0
        start_index = -1
        end_index = -1
        for i in range(n):
            if cur_sum == 0:
                start_index = i
            cur_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
                end_index = i
            if cur_sum < 0:
                cur_sum = 0

        print(nums[start_index:end_index + 1])
        return max_sum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([3, 2, -6, 8, -3, 5]))
