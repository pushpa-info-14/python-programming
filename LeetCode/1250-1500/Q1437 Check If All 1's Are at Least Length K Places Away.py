import math
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -math.inf
        for i in range(len(nums)):
            if nums[i]:
                if i - last_one - 1 < k:
                    return False
                last_one = i
        return True


s = Solution()
print(s.kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
print(s.kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))
print(s.kLengthApart(nums=[1, 1, 1, 0], k=3))  # False
print(s.kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1, 0], k=2))  # True
