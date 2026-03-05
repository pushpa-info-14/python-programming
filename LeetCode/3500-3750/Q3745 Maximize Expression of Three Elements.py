from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return -nums[0] + nums[-2] + nums[-1]


s = Solution()
print(s.maximizeExpressionOfThree(nums=[1, 4, 2, 5]))
print(s.maximizeExpressionOfThree(nums=[-2, 0, 5, -2, 4]))
