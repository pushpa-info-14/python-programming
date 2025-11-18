from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + (k - 1) * k // 2


s = Solution()
print(s.maximizeSum(nums=[1, 2, 3, 4, 5], k=3))
print(s.maximizeSum(nums=[5, 5, 5], k=2))
