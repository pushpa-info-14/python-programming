import bisect
from functools import cache
from math import sqrt

square_numbers = [i * i for i in range(1, int(sqrt(10 ** 5 + 1)))]


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dfs(x):
            if x <= 0:
                return False
            index = bisect.bisect_left(square_numbers, x)
            for i in range(index, -1, -1):
                if x - square_numbers[i] >= 0 and dfs(x - square_numbers[i]) == False:
                    return True
            return False

        return dfs(n)


s = Solution()
print(s.winnerSquareGame(1))
print(s.winnerSquareGame(2))
print(s.winnerSquareGame(4))
