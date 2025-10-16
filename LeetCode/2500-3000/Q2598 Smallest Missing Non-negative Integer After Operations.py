from collections import defaultdict
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = defaultdict(int)
        for num in nums:
            mods[num % value] += 1
        missing = 0
        while mods[missing % value] != 0:
            mods[missing % value] -= 1
            missing += 1
        return missing


s = Solution()
print(s.findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=5))
print(s.findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=7))
print(s.findSmallestInteger(nums=[3, 0, 3, 2, 4, 2, 1, 1, 0, 4], value=5))
print(s.findSmallestInteger(nums=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], value=10))
