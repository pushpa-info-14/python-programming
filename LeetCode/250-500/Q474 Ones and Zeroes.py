from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        len_strs = len(strs)

        @cache
        def dfs(i, zeros, ones):
            if i == len_strs:
                return 0

            # no take
            res1 = dfs(i + 1, zeros, ones)
            # take
            res2 = 0
            count_0 = strs[i].count('0')
            count_1 = strs[i].count('1')
            if count_0 <= zeros and count_1 <= ones:
                res2 = 1 + dfs(i + 1, zeros - count_0, ones - count_1)

            return max(res1, res2)

        return dfs(0, m, n)


s = Solution()
print(s.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
print(s.findMaxForm(strs=["10", "0", "1"], m=1, n=1))
print(s.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=4, n=3))
