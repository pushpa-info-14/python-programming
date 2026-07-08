from typing import List

mod = 10 ** 9 + 7
pow10 = [1] * 100001
for i in range(1, 100001):
    pow10[i] = pow10[i - 1] * 10 % mod


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pref_sum = [0] * (n + 1)
        x = [0] * (n + 1)
        count = [0] * (n + 1)
        for i, c in enumerate(s):
            d = int(c)
            pref_sum[i + 1] = pref_sum[i] + d
            x[i + 1] = (x[i] * 10 + d) % mod if d > 0 else x[i]
            count[i + 1] = count[i] + (d > 0)

        m = len(queries)
        res = [0] * m
        for i in range(m):
            l = queries[i][0]
            r = queries[i][1] + 1
            length = count[r] - count[l]
            res[i] = (x[r] - x[l] * pow10[length]) * (pref_sum[r] - pref_sum[l]) % mod

        return res


s = Solution()
print(s.sumAndMultiply(s="10203004", queries=[[0, 7], [1, 3], [4, 6]]))
print(s.sumAndMultiply(s="1000", queries=[[0, 3], [1, 1]]))
print(s.sumAndMultiply(s="9876543210", queries=[[0, 9]]))
