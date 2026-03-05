from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        res = 0
        counter = Counter(nums)
        for key, value in counter.items():
            if value % k == 0:
                res += key * value
        return res


s = Solution()
print(s.sumDivisibleByK(nums=[1, 2, 2, 3, 3, 3, 3, 4], k=2))
print(s.sumDivisibleByK(nums=[1, 2, 3, 4, 5], k=2))
print(s.sumDivisibleByK(nums=[4, 4, 4, 1, 2, 3], k=3))
