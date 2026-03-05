from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


s = Solution()
print(s.minOperations(nums=[3, 9, 7], k=5))
print(s.minOperations(nums=[4, 1, 3], k=4))
print(s.minOperations(nums=[3, 2], k=6))
