import math


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 0
        for i in range(1, n + 1):
            res = (res << (int(math.log2(i)) + 1) | i) % mod
        return res


s = Solution()
print(s.concatenatedBinary(1))
print(s.concatenatedBinary(3))
print(s.concatenatedBinary(12))
