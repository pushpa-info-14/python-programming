class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10 ** 9 + 7
        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i % mod
        left = pos
        right = n - left - 1
        res = 0
        for l in range(k + 1):
            r = k - l
            if l <= left and r <= right:
                ways_l = fac[left] * pow(fac[l], -1, mod) * pow(fac[left - l], -1, mod) % mod
                ways_r = fac[right] * pow(fac[r], -1, mod) * pow(fac[right - r], -1, mod) % mod
                res += ways_l * ways_r
                res %= mod
        return res * 2 % mod

    def countVisiblePeople2(self, n: int, pos: int, k: int) -> int:
        mod = 10 ** 9 + 7

        fact = [1] * (n + 1)
        inv = [1] * (n + 1)

        # factorial
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod

        # fast power
        def power(a, b):
            res = 1
            while b:
                if b & 1:
                    res = res * a % mod
                a = a * a % mod
                b >>= 1
            return res

        # inverse factorial
        inv[n] = power(fact[n], mod - 2)
        for i in range(n - 1, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % mod

        def comb(n, r):
            return fact[n] * inv[r] % mod * inv[n - r] % mod

        left = pos
        right = n - pos - 1
        ans = 0

        for i in range(max(0, k - right), min(left, k) + 1):
            ans = (ans + comb(left, i) * comb(right, k - i)) % mod

        return (ans * 2) % mod


s = Solution()
print(s.countVisiblePeople(n=3, pos=1, k=0))
print(s.countVisiblePeople(n=3, pos=2, k=1))
print(s.countVisiblePeople(n=1, pos=0, k=0))
print("--------")
print(s.countVisiblePeople2(n=3, pos=1, k=0))
print(s.countVisiblePeople2(n=3, pos=2, k=1))
print(s.countVisiblePeople2(n=1, pos=0, k=0))
