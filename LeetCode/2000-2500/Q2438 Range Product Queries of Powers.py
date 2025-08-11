import math
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        max_power = int(math.log2(n))
        powers = []
        prefix_powers = [1]
        for i in range(max_power + 1):
            if n >> i & 1:
                x = 1 << i
                powers.append(x)
                prefix_powers.append(prefix_powers[-1] * x)

        # print(powers)
        # print(prefix_powers)

        res = []
        for start, end in queries:
            if start == end:
                res.append(powers[start] % mod)
            else:
                res.append((prefix_powers[end + 1] // prefix_powers[start]) % mod)
        return res


s = Solution()
print(s.productQueries(n=15, queries=[[0, 1], [2, 2], [0, 3]]))
print(s.productQueries(n=2, queries=[[0, 0]]))
print(s.productQueries(n=13, queries=[[1, 2], [1, 1]]))
print(s.productQueries(n=919, queries=[[5, 5], [4, 4], [0, 1], [1, 5], [4, 6], [6, 6]]))
