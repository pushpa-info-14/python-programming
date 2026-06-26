class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10 ** 9 + 7

        def mul(a, b):
            n1, m1 = len(a), len(a[0])
            res = [[0] * m1 for _ in range(n1)]
            for i in range(n1):
                for k in range(m1):
                    if a[i][k] == 0:
                        continue
                    for j in range(m1):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % mod
            return res

        def pow_mul(base, exp, res):
            while exp:
                if exp & 1:
                    res = mul(res, base)
                base = mul(base, base)
                exp //= 2
            return res

        items = r - l + 1
        size = 2 * items
        mat = [[0] * size for _ in range(size)]
        for i in range(items):
            for j in range(i):
                mat[i][j + items] = 1  # move DOWN to j, next go UP
            for j in range(i + 1, items):
                mat[i + items][j] = 1  # move UP to j, next go DOWN

        dp = [[1] * size]
        dp = pow_mul(mat, n - 1, dp)
        return sum(dp[-1]) % mod


s = Solution()
print(s.zigZagArrays(n=3, l=4, r=5))
print(s.zigZagArrays(n=3, l=1, r=3))
