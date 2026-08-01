from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        inf = 10 ** 10
        n = len(nums)

        @cache
        def dfs(l, r, player):
            if l == r:
                return nums[l] if player == 1 else -nums[l]
            if player == 1:
                best = -inf
                best = max(
                    best,
                    nums[l] + dfs(l + 1, r, 2),
                    nums[r] + dfs(l, r - 1, 2)
                )
                return best
            else:
                best = inf
                best = min(
                    best,
                    -nums[l] + dfs(l + 1, r, 1),
                    -nums[r] + dfs(l, r - 1, 1)
                )
                return best

        return True if dfs(0, n - 1, 1) >= 0 else False


s = Solution()
print(s.predictTheWinner(nums=[1, 5, 2]))
print(s.predictTheWinner(nums=[1, 5, 233, 7]))
