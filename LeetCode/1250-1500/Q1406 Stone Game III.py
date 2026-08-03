from functools import cache
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        inf = 10 ** 10
        n = len(stoneValue)

        @cache
        def dfs(i):
            if i >= n:
                return 0
            best, cur = -inf, 0
            for j in range(i, i + 3):
                if j >= n:
                    break
                cur += stoneValue[j]
                best = max(best, cur - dfs(j + 1))
            return best

        score = dfs(0)
        if score == 0:
            return "Tie"
        return "Alice" if score > 0 else "Bob"


s = Solution()
print(s.stoneGameIII(stoneValue=[1, 2, 3, 7]))
print(s.stoneGameIII(stoneValue=[1, 2, 3, -9]))
print(s.stoneGameIII(stoneValue=[1, 2, 3, 6]))
