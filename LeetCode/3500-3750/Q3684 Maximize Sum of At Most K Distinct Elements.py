from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(set(nums), reverse=True)
        if len(nums) < k:
            return nums
        else:
            return nums[:k]


s = Solution()
print(s.maxKDistinct(nums=[84, 93, 100, 77, 90], k=3))
print(s.maxKDistinct(nums=[84, 93, 100, 77, 93], k=3))
print(s.maxKDistinct(nums=[1, 1, 1, 2, 2, 2], k=6))
