import math
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = math.inf
        for num in nums:
            cur = 0
            while num:
                cur += num % 10
                num //= 10
            res = min(res, cur)
        return res


s = Solution()
print(s.minElement(nums=[10, 12, 13, 14]))
print(s.minElement(nums=[1, 2, 3, 4]))
print(s.minElement(nums=[999, 19, 199]))
