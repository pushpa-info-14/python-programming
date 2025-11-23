import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)

        closest_sum = math.inf
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum == target:
                    return current_sum
                elif current_sum <= target:
                    l += 1
                else:
                    r -= 1
        return closest_sum


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([0, 0, 0], 0))
