from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(
            nums[-1] - nums[2],  # removing first 2 elements
            nums[-2] - nums[1],  # removing first and last elements
            nums[-3] - nums[0]  # removing last 2 elements
        )


s = Solution()
print(s.minimizeSum(nums=[1, 4, 7, 8, 5]))
print(s.minimizeSum(nums=[1, 4, 3]))
