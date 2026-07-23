from collections import Counter
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False
        counter = Counter(nums)
        for i in range(1, n):
            if counter[i] != 1:
                return False
        return counter[n] == 2


s = Solution()
print(s.isGood(nums=[2, 1, 3]))
print(s.isGood(nums=[1, 3, 3, 2]))
print(s.isGood(nums=[1, 1]))
