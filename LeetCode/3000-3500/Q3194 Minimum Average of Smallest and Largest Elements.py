import math
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        res = math.inf
        for i in range(n // 2):
            res = min(res, (nums[i] + nums[n - i - 1]) / 2)
        return res


s = Solution()
print(s.minimumAverage(nums=[7, 8, 3, 4, 15, 13, 4, 1]))
print(s.minimumAverage(nums=[1, 9, 8, 3, 10, 5]))
print(s.minimumAverage(nums=[1, 2, 3, 7, 8, 9]))
