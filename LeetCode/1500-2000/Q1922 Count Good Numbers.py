from math import ceil


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        def pow(x, n):
            res = 1
            while n > 0:
                if n % 2:
                    res *= x
                x = (x * x) % mod
                n = n // 2
            return res

        even = ceil(n / 2)
        odd = n // 2
        return (pow(5, even) * pow(4, odd)) % mod


s = Solution()
print(s.countGoodNumbers(1))
print(s.countGoodNumbers(4))
print(s.countGoodNumbers(50))
