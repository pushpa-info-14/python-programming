class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod = 10 ** 9 + 7
        n = r - l + 1

        # Sum of digits in [l, r]
        s = (l + r) * n // 2
        s %= mod

        # n^(k-1) % mod
        pow_n = pow(n, k - 1, mod)

        # (10^k - 1) / 9 under modulo
        pow_10k = pow(10, k, mod)
        geom = (pow_10k - 1) % mod
        inv9 = pow(9, mod - 2, mod)
        geom = geom * inv9 % mod

        # Final answer
        return s * pow_n % mod * geom % mod


s = Solution()
print(s.sumOfNumbers(l=1, r=2, k=2))
print(s.sumOfNumbers(l=0, r=1, k=3))
print(s.sumOfNumbers(l=5, r=5, k=10))
