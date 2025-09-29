from functools import cache
from math import inf
from typing import List

from sortedcontainers import SortedList


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def gen_outcomes(n, first, second):
            for combo in range(2 ** (n // 2)):
                out = SortedList()
                for i in range(1, (n // 2) + 1):
                    if combo & 1 == 0:
                        out.add(i)
                    else:
                        out.add(n + 1 - i)
                    combo >>= 1
                if n & 1 == 1:
                    out.add((n + 1) // 2)
                if first in out and second in out:
                    yield out

        def norm(slst, first, second):
            return len(slst), slst.index(first) + 1, slst.index(second) + 1

        @cache
        def dp(n, first, second):
            if first + second == n + 1:
                return [1, 1]
            mi, ma = inf, 0
            for result in gen_outcomes(n, first, second):
                n_mi, n_ma = dp(*norm(result, first, second))
                mi = min(mi, n_mi + 1)
                ma = max(ma, n_ma + 1)
            return [mi, ma]

        return dp(n, firstPlayer, secondPlayer)


s = Solution()
print(s.earliestAndLatest(n=11, firstPlayer=2, secondPlayer=4))
print(s.earliestAndLatest(n=5, firstPlayer=1, secondPlayer=5))
