import math
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total = 0
        for row in grid:
            for n in row:
                total += n
                if n % x != grid[0][0] % x:
                    return -1

        nums = [n for row in grid for n in row]
        nums.sort()

        prefix_sum = 0
        res = math.inf
        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix_sum
            cost_right = total - prefix_sum - (nums[i] * (len(nums) - i))
            operations = (cost_left + cost_right) // x
            res = min(res, operations)
            prefix_sum += nums[i]
        return res


s = Solution()
print(s.minOperations(grid=[[2, 4], [6, 8]], x=2))
print(s.minOperations(grid=[[1, 5], [2, 3]], x=1))
print(s.minOperations(grid=[[1, 2], [3, 4]], x=2))
