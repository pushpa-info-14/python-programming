import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0] * 32

        def updateBits(num):
            for i in range(32):
                if num >> i & 1:
                    bits[i] += 1

        def removeBits(num):
            for i in range(32):
                if num >> i & 1:
                    bits[i] -= 1

        def calculate():
            x = 0
            for i in range(32):
                if bits[i]:
                    x |= (1 << i)
            return x

        res = math.inf
        l = 0
        for r in range(n):
            updateBits(nums[r])
            or_val = calculate()
            res = min(res, abs(or_val - k))
            while l < r and or_val >= k:
                removeBits(nums[l])
                or_val = calculate()
                res = min(res, abs(or_val - k))
                l += 1
        return res


s = Solution()
# print(s.minimumDifference(nums=[1, 2, 4, 5], k=3))  # 0
# print(s.minimumDifference(nums=[1, 3, 1, 3], k=2))  # 1
# print(s.minimumDifference(nums=[1], k=10))  # 9
# print(s.minimumDifference(nums=[1, 10], k=6))  # 4
# print(s.minimumDifference(nums=[7, 6, 2, 8, 49], k=75))  # 12
