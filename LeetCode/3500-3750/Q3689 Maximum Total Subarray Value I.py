from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k


s = Solution()
print(s.maxTotalValue(nums=[1, 3, 2], k=2))
print(s.maxTotalValue(nums=[4, 2, 5, 1], k=3))
