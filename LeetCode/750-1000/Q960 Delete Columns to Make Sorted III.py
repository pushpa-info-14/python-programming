from functools import cache
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        inf = 10 ** 9
        @cache
        def dfs(i, prev):
            if i == m:
                return 0
            not_take = 1 + dfs(i + 1, prev)
            take = inf
            is_valid = True
            for word in strs:
                if prev != -1 and word[prev] > word[i]:
                    is_valid = False
                    break
            if is_valid:
                take = dfs(i + 1, i)
            return min(not_take, take)

        return dfs(0, -1)


s = Solution()
print(s.minDeletionSize(strs=["babca", "bbazb"]))
print(s.minDeletionSize(strs=["edcba"]))
print(s.minDeletionSize(strs=["ghi", "def", "abc"]))
