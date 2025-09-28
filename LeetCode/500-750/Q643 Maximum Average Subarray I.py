import math
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = -math.inf
        cur_sum = 0
        l = 0
        for r in range(n):
            cur_sum += nums[r]
            if r - l + 1 == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[l]
                l += 1
        return max_sum / k


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(s.findMaxAverage([5], 1))
