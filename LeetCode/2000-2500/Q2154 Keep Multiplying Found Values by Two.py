from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        while original in nums_set:
            original *= 2
        return original


s = Solution()
print(s.findFinalValue(nums=[5, 3, 6, 1, 12], original=3))
print(s.findFinalValue(nums=[2, 7, 9], original=4))
