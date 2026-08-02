from functools import cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        inf = 10 ** 10
        n = len(piles)

        @cache
        def dfs(l, r, player):
            if l == r:
                return piles[l] if player == 1 else -piles[l]
            if player == 1:
                best = -inf
                best = max(
                    best,
                    piles[l] + dfs(l + 1, r, 2),
                    piles[r] + dfs(l, r - 1, 2)
                )
                return best
            else:
                best = inf
                best = min(
                    best,
                    -piles[l] + dfs(l + 1, r, 1),
                    -piles[r] + dfs(l, r - 1, 1)
                )
                return best

        return True if dfs(0, n - 1, 1) >= 0 else False

    def stoneGame2(self, piles: List[int]) -> bool:
        return True


s = Solution()
print(s.stoneGame(piles=[5, 3, 4, 5]))
print(s.stoneGame(piles=[3, 7, 2, 3]))
print("---------------")
print(s.stoneGame2(piles=[5, 3, 4, 5]))
print(s.stoneGame2(piles=[3, 7, 2, 3]))
