MOD = 10 ** 9 + 7


class Solution:
    def __init__(self):
        self.fact = None
        self.inv_fact = None

    def binary_exp(self, a, b):
        res = 1
        a = a % MOD
        while b > 0:
            if b & 1:
                res = (res * a) % MOD
            a = (a * a) % MOD
            b >>= 1
        return res

    def mmi(self, val):
        return self.binary_exp(val, MOD - 2)

    def inverse_fact(self, n):
        self.inv_fact = [0] * (n + 1)
        self.inv_fact[n] = self.mmi(self.fact[n])
        for i in range(n, 0, -1):
            self.inv_fact[i - 1] = (self.inv_fact[i] * i) % MOD

    def factorial(self, n):
        self.fact = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % MOD

    def precompute(self, n):
        self.factorial(n)
        self.inverse_fact(n)

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        self.precompute(n)

        run_ways = (self.fact[n - 1] * self.inv_fact[n - k - 1] % MOD) * self.inv_fact[k] % MOD
        ways_to_assign = m * self.binary_exp(m - 1, n - k - 1) % MOD
        return run_ways * ways_to_assign % MOD


"""
-CountNumber pf Balanced Permutations-3343
-Binary Exponentiation
-Fermat's Little Theorem
-Modulo Multiplicative Inverse(MMI)
-Modulo Arithmetic
-Precompute
    -Factorial
    -Inverse Factorial
"""
s = Solution()
print(s.countGoodArrays(n=3, m=2, k=1))
print(s.countGoodArrays(n=4, m=2, k=2))
print(s.countGoodArrays(n=5, m=2, k=0))
