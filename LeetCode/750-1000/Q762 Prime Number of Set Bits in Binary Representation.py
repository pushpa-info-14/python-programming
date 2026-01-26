import math


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}  # Max bit count math.log2(10 ** 6)
        res = 0
        for num in range(left, right + 1):
            bits = 0
            while num:
                bits += num % 2
                num //= 2
            if bits in primes:
                res += 1
        return res


s = Solution()
print(s.countPrimeSetBits(left=6, right=10))
print(s.countPrimeSetBits(left=10, right=15))
