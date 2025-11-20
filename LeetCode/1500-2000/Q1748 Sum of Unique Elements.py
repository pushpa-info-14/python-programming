from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for num, freq in counter.items():
            if freq == 1:
                res += num
        return res


s = Solution()
print(s.sumOfUnique(nums=[1, 2, 3, 2]))
print(s.sumOfUnique(nums=[1, 1, 1, 1, 1]))
print(s.sumOfUnique(nums=[1, 2, 3, 4, 5]))
