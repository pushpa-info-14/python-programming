from math import inf
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = inf
        for i in range(n - l + 1):
            left = i
            cur = 0
            for right in range(i, min(i + r, n)):
                cur += nums[right]
                if right - left + 1 >= l:
                    if cur > 0:
                        res = min(res, cur)
        return res if res != inf else -1


s = Solution()
print(s.minimumSumSubarray(nums=[3, -2, 1, 4], l=2, r=3))
print(s.minimumSumSubarray(nums=[-2, 2, -3, 1], l=2, r=3))
print(s.minimumSumSubarray(nums=[1, 2, 3, 4], l=2, r=4))
print(s.minimumSumSubarray(nums=[17, 13], l=1, r=2))
print(s.minimumSumSubarray(nums=[-23, 3], l=2, r=2))
print(s.minimumSumSubarray(nums=[-12, 8], l=1, r=1))
