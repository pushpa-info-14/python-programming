from bisect import bisect_right
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        total = 0
        for i in range(n):
            j = bisect_right(nums, target - nums[i])
            j -= 1
            if i > j:
                break
            total += pow(2, j - i, mod)
        return total % mod


s = Solution()
print(s.numSubseq(nums=[3, 5, 6, 7], target=9))
print(s.numSubseq(nums=[3, 3, 6, 8], target=10))
print(s.numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))
