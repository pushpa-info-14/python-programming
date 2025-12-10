import math
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0] * 6

        def add_num(num):
            i = 0
            while num:
                bit = num & 1
                if bit:
                    bits[i] += 1
                i += 1
                num >>= 1

        def remove_num(num):
            i = 0
            while num:
                bit = num & 1
                if bit:
                    bits[i] -= 1
                i += 1
                num >>= 1

        def cal_or():
            x = 0
            for bit in bits[::-1]:
                x <<= 1
                if bit:
                    x += 1
            return x

        n = len(nums)
        l = 0
        res = math.inf
        for r in range(n):
            add_num(nums[r])
            while l <= r and cal_or() >= k:
                res = min(res, r - l + 1)
                remove_num(nums[l])
                l += 1
        return res if res != math.inf else -1


s = Solution()
print(s.minimumSubarrayLength(nums=[1, 2, 3], k=2))
print(s.minimumSubarrayLength(nums=[2, 1, 8], k=10))
print(s.minimumSubarrayLength(nums=[1, 2], k=0))
