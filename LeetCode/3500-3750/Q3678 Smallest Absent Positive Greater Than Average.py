from math import floor
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        seen = set(nums)
        average = sum(nums) / len(nums)
        x = floor(average) + 1
        if x <= 0:
            x = 1
        while x in seen:
            x += 1
        return x


s = Solution()
print(s.smallestAbsent(nums=[3, 5]))
print(s.smallestAbsent(nums=[-1, 1, 2]))
print(s.smallestAbsent(nums=[4, -1]))
print(s.smallestAbsent(nums=[-34]))
